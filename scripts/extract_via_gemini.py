"""Extract a Schweser reading by sending the chapter PDF directly to Gemini 2.5 Pro.

This replaces the broken `pdftotext -layout` pipeline. Gemini reads the PDF as a
vision-aware LLM and reproduces formulas/tables verbatim — no silent loss.

Usage:
    python scripts/extract_via_gemini.py --book 2 --reading 30
    python scripts/extract_via_gemini.py --book 2 --reading 30 --output schema_b
    python scripts/extract_via_gemini.py --book 2 --reading 30 --output raw
    python scripts/extract_via_gemini.py --book 2 --reading 30 --pdf raw/custom.pdf --force

Modes:
    --output schema_b  (default): emits the full Schema B reading file
    --output raw     : emits a clean Markdown rendering of the chapter
                        (formulas in LaTeX, tables preserved) for diff/audit purposes

Outputs land in `wiki/Book {B} - .../R{N}.gemini.md` (gitignored). The user
hand-merges into the canonical `R{N}_{Title}.md` after review.
"""

from __future__ import annotations
import argparse
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
import pypdfium2 as pdfium

sys.path.insert(0, str(Path(__file__).parent))
from slice_pdf import slice_pdf  # noqa: E402

try:
    from google.genai import errors as genai_errors
    _RETRYABLE_EXC = (genai_errors.ServerError,)
except (ImportError, AttributeError):
    _RETRYABLE_EXC = ()


BOOK_DIRS = {
    1: "Book 1 - Market Risk",
    2: "Book 2 - Credit Risk",
    3: "Book 3 - Operational Risk",
    4: "Book 4 - Liquidity Risk",
    5: "Book 5 - Investment Risk + Current Issues",
}

# Top-of-page window (chars) to scan for a "Reading N:" title marker.
READING_HEAD_CHARS = 300

# A chapter-start page begins with "Reading N:" or "Reading N\n" anchored to
# the start of a line, within the first READING_HEAD_CHARS chars. This
# intentionally excludes cross-references like "see Reading 28" that appear
# inline within body text, and captures title/LO pages regardless of density.
_READING_START_RE = re.compile(
    r"^\s*Reading\s+(\d{1,3})\s*[:\n]",
    re.MULTILINE | re.IGNORECASE,
)

# Network retry knobs for Gemini calls (transient ServerError only).
_MAX_ATTEMPTS = 3
_BACKOFF_SECONDS = (4, 16, 64)


def find_reading_pages(pdf_path: Path) -> tuple[dict[int, int], int]:
    """Return ({reading_number: 1-indexed-start-page}, total_pages)."""
    with pdfium.PdfDocument(str(pdf_path)) as pdf:
        total = len(pdf)
        pages: dict[int, int] = {}
        for i in range(total):
            txt = pdf[i].get_textpage().get_text_bounded()
            head = txt[:READING_HEAD_CHARS]
            for m in _READING_START_RE.finditer(head):
                n = int(m.group(1))
                if n not in pages:
                    pages[n] = i + 1
        return pages, total


def build_raw_prompt() -> str:
    return """You are extracting a chapter from a Schweser FRM Part 2 study book.
The PDF is attached. Output a SINGLE clean Markdown document that preserves:

1. Section headings (MODULE N.X, LO N.x) as Markdown headings.
2. Every display formula as a LaTeX block: $$...$$
3. Every inline formula as inline LaTeX: $...$
4. Every table as a Markdown table.
5. Every figure caption (Figure N.M: ...) followed by a faithful description AND
   the table data shown in or beneath the figure if any.
6. Module Quiz questions verbatim, with the answer key at the end of the chapter.
7. Greek letters as Unicode (λ ρ σ μ etc.) within Markdown prose; LaTeX inside
   formula blocks.

CRITICAL RULES:
- Reproduce all formulas EXACTLY as rendered in the PDF. Do not paraphrase.
- Do not add commentary, explanation, or restructuring.
- Do not skip content. If a formula is hard to read, transcribe what you see and
  add a comment like `% [unclear: ...]` next to it.
- Preserve the order of the source material.

Output only the Markdown. No preamble, no postscript.
"""


def build_schema_b_prompt(reading_num: int, system_prompt: str, template: str) -> str:
    return f"""You are receiving the source PDF of a single chapter from the Schweser
FRM Part 2 study book (Reading {reading_num}). Your task: produce the Schema B
reading file.

You must follow these instructions strictly:

==== ROLE & CORE CONSTRAINTS ====
{system_prompt}

==== SCHEMA B TEMPLATE ====
You must produce output in EXACTLY this structure. Do not deviate.

{template}

==== ADDITIONAL EXTRACTION RULES ====
1. The PDF is the ONLY source of truth. If a formula or table is in the PDF,
   reproduce it verbatim. Do not substitute formulas from your training data.
2. Reproduce every display formula as a LaTeX block: $$...$$
3. Reproduce every inline formula as inline LaTeX: $...$
4. Greek letters: Unicode in prose (λ, ρ, σ), LaTeX inside formula blocks.
5. The proposition tags are exactly: [REG] | [ECO] | [OPS] | [THE].
   The Constraint Hierarchy is [REG] > [VIG] > [ECO] > [THE]. [VIG] is a
   question-answering priority tag only — never use it as a proposition tag.
6. Every formula you write in §1 must trace to a specific PDF page. After
   each formula, add a parenthetical source reference: (PDF p. N).
7. Every Stress-Test row in §2 must use the formula or numerical structure
   present in the PDF.

Output ONLY the Schema B markdown file content. No preamble, no explanation."""


def resolve_book_pdf(repo: Path, book: int, pdf_override: str | None) -> Path | None:
    """Locate the source PDF. Returns None on failure (error already printed)."""
    if pdf_override:
        p = Path(pdf_override)
        if not p.is_absolute():
            p = (repo / p).resolve()
        if not p.exists():
            print(f"ERROR: --pdf not found: {p}", file=sys.stderr)
            return None
        return p
    raw_dir = repo / "raw"
    pattern = f"FRM*Book*{book}.pdf"
    matches = sorted(raw_dir.glob(pattern))
    if not matches:
        print(f"ERROR: No PDF matching raw/{pattern}", file=sys.stderr)
        print(f"       Place the Schweser PDF in {raw_dir} or pass --pdf PATH.",
              file=sys.stderr)
        return None
    if len(matches) > 1:
        print(f"ERROR: Multiple PDFs match raw/{pattern}:", file=sys.stderr)
        for m in matches:
            print(f"       {m.name}", file=sys.stderr)
        print("       Use --pdf to pick one.", file=sys.stderr)
        return None
    return matches[0]


def call_gemini_with_retry(client, model_name: str, contents):
    """Call Gemini generate_content with retry on transient ServerError only."""
    last_exc: BaseException | None = None
    for attempt in range(_MAX_ATTEMPTS):
        try:
            return client.models.generate_content(model=model_name, contents=contents)
        except _RETRYABLE_EXC as e:
            last_exc = e
            if attempt == _MAX_ATTEMPTS - 1:
                break
            wait = _BACKOFF_SECONDS[attempt]
            print(f"      (attempt {attempt + 1}/{_MAX_ATTEMPTS} failed: "
                  f"{type(e).__name__}; retrying in {wait}s)", file=sys.stderr)
            time.sleep(wait)
    assert last_exc is not None
    raise last_exc


def extract_text_and_finish(resp) -> tuple[str, str]:
    """Return (text, finish_reason_name) without relying on resp.text shortcut."""
    candidates = getattr(resp, "candidates", None) or []
    if not candidates:
        return "", "NO_CANDIDATES"
    cand = candidates[0]
    fr = getattr(cand, "finish_reason", None)
    if fr is None:
        fr_name = "UNKNOWN"
    else:
        fr_name = getattr(fr, "name", None) or str(fr)
    content = getattr(cand, "content", None)
    parts = (getattr(content, "parts", None) or []) if content is not None else []
    text = "".join((getattr(p, "text", "") or "") for p in parts)
    return text, fr_name


def main() -> int:
    p = argparse.ArgumentParser(description="Extract a reading via Gemini direct PDF.")
    p.add_argument("--book", type=int, required=True, choices=BOOK_DIRS.keys())
    p.add_argument("--reading", type=int, required=True)
    p.add_argument("--output", choices=["raw", "schema_b"], default="schema_b")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--pdf", default=None,
                   help="Path to source PDF (overrides raw/FRM*Book{B}.pdf auto-detect).")
    p.add_argument("--end-padding", type=int, default=0,
                   help="Pages past the next reading start (clamped to total pages).")
    p.add_argument("--keep-mini-pdf", action="store_true",
                   help="Keep the chapter mini-PDF after extraction.")
    p.add_argument("--force", action="store_true",
                   help="Overwrite existing output (backs up previous to .bak).")
    args = p.parse_args()

    repo = Path(args.repo_root).resolve()
    load_dotenv(repo / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-pro")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set (check .env)", file=sys.stderr)
        return 2

    book_pdf = resolve_book_pdf(repo, args.book, args.pdf)
    if book_pdf is None:
        return 2

    print(f"[1/5] Scanning {book_pdf.name} for chapter boundaries...")
    pages, total_pages = find_reading_pages(book_pdf)
    if args.reading not in pages:
        print(f"ERROR: Reading {args.reading} not found. Available: {sorted(pages)}",
              file=sys.stderr)
        return 2

    start = pages[args.reading]
    next_readings = sorted(n for n in pages if n > args.reading)
    if next_readings:
        end = pages[next_readings[0]] - 1
    else:
        end = total_pages
    requested_end = end + args.end_padding
    end = min(requested_end, total_pages)
    if requested_end > total_pages:
        print(f"      NOTE: end-padding clamped from {requested_end} to {total_pages} "
              f"(PDF has {total_pages} pages)", file=sys.stderr)
    print(f"      Reading {args.reading}: pages {start}-{end} ({end - start + 1} pages)")

    print(f"[2/5] Slicing chapter into mini-PDF...")
    out_dir = repo / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    mini_pdf = out_dir / f"R{args.reading}_chapter.pdf"
    slice_pdf(book_pdf, mini_pdf, start, end)

    print(f"[3/5] Building prompt ({args.output} mode)...")
    if args.output == "raw":
        prompt = build_raw_prompt()
    else:
        sys_prompt = (repo / "system" / "00_SYSTEM_PROMPT.md").read_text(encoding="utf-8")
        # Use the active Schema B template
        template_path = repo / "wiki" / "_TEMPLATE_Reading.md"
        if not template_path.exists():
            print(f"ERROR: Schema B template missing: {template_path}", file=sys.stderr)
            return 2
        template = template_path.read_text(encoding="utf-8")
        prompt = build_schema_b_prompt(args.reading, sys_prompt, template)

    # Resolve destination early so we can fail fast on overwrite conflict
    # before burning Gemini tokens.
    dst_dir = repo / "wiki" / BOOK_DIRS[args.book]
    dst_dir.mkdir(parents=True, exist_ok=True)
    suffix = "gemini.md" if args.output == "schema_b" else "raw.gemini.md"
    dst = dst_dir / f"R{args.reading}.{suffix}"
    if dst.exists() and not args.force:
        print(f"ERROR: {dst} already exists. Use --force to overwrite "
              f"(will back up to {dst.name}.bak).", file=sys.stderr)
        if not args.keep_mini_pdf:
            mini_pdf.unlink(missing_ok=True)
        return 2

    print(f"[4/5] Sending to Gemini ({model_name})...")
    client = genai.Client(api_key=api_key)
    pdf_bytes = mini_pdf.read_bytes()
    contents = [
        types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
        prompt,
    ]
    try:
        resp = call_gemini_with_retry(client, model_name, contents)
    except Exception as e:
        print(f"ERROR: Gemini call failed after {_MAX_ATTEMPTS} attempts: "
              f"{type(e).__name__}: {e}", file=sys.stderr)
        if not args.keep_mini_pdf:
            mini_pdf.unlink(missing_ok=True)
        return 3

    text, fr_name = extract_text_and_finish(resp)
    # Token usage report (best-effort).
    if hasattr(resp, "usage_metadata") and resp.usage_metadata:
        u = resp.usage_metadata
        print(f"      Tokens: in={getattr(u, 'prompt_token_count', '?')} "
              f"out={getattr(u, 'candidates_token_count', '?')} "
              f"total={getattr(u, 'total_token_count', '?')} "
              f"finish={fr_name}")

    # Handle non-STOP finish reasons.
    if fr_name == "MAX_TOKENS":
        partial = dst_dir / f"R{args.reading}.partial.{suffix}"
        partial.write_text(text, encoding="utf-8")
        print(f"WARNING: Gemini output truncated (MAX_TOKENS). "
              f"Partial saved to {partial} ({len(text):,} chars). "
              f"Canonical output NOT written.", file=sys.stderr)
        if not args.keep_mini_pdf:
            mini_pdf.unlink(missing_ok=True)
        return 4
    if fr_name != "STOP":
        print(f"ERROR: Gemini finish_reason={fr_name} (not STOP). "
              f"No output written.", file=sys.stderr)
        if not args.keep_mini_pdf:
            mini_pdf.unlink(missing_ok=True)
        return 5
    if not text.strip():
        print("ERROR: Gemini returned empty response despite STOP", file=sys.stderr)
        if not args.keep_mini_pdf:
            mini_pdf.unlink(missing_ok=True)
        return 3

    print(f"[5/5] Writing output...")
    if args.force and dst.exists():
        backup = dst.with_name(dst.name + ".bak")
        dst.replace(backup)
        print(f"      Backed up existing {dst.name} → {backup.name}")
    dst.write_text(text, encoding="utf-8")
    print(f"      Wrote {dst} ({len(text):,} chars)")

    if not args.keep_mini_pdf:
        mini_pdf.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
