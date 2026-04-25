"""Extract a Schweser reading by sending the chapter PDF directly to Gemini 2.5 Pro.

This replaces the broken `pdftotext -layout` pipeline. Gemini reads the PDF as a
vision-aware LLM and reproduces formulas/tables verbatim — no silent loss.

Usage:
    python scripts/extract_via_gemini.py --book 2 --reading 30
    python scripts/extract_via_gemini.py --book 2 --reading 30 --output schema_b
    python scripts/extract_via_gemini.py --book 2 --reading 30 --output raw

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
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
import pypdfium2 as pdfium

sys.path.insert(0, str(Path(__file__).parent))
from slice_pdf import slice_pdf  # noqa: E402


BOOK_DIRS = {
    1: "Book 1 - Market Risk",
    2: "Book 2 - Credit Risk",
    3: "Book 3 - Operational Risk",
    4: "Book 4 - Liquidity Risk",
    5: "Book 5 - Investment Risk + Current Issues",
}


def find_reading_pages(pdf_path: Path) -> dict[int, int]:
    """Return {reading_number: 1-indexed-start-page} (chapter body pages only)."""
    pdf = pdfium.PdfDocument(str(pdf_path))
    pages = {}
    for i in range(len(pdf)):
        txt = pdf[i].get_textpage().get_text_bounded()
        if len(txt) < 1500:
            continue
        for m in re.finditer(r"\bReading\s+(\d{1,3})\b", txt[:400], re.IGNORECASE):
            n = int(m.group(1))
            if n not in pages:
                pages[n] = i + 1
    return pages


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


def main() -> int:
    p = argparse.ArgumentParser(description="Extract a reading via Gemini direct PDF.")
    p.add_argument("--book", type=int, required=True, choices=BOOK_DIRS.keys())
    p.add_argument("--reading", type=int, required=True)
    p.add_argument("--output", choices=["raw", "schema_b"], default="schema_b")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--end-padding", type=int, default=0,
                   help="Pages past the next reading start (default 0).")
    p.add_argument("--keep-mini-pdf", action="store_true",
                   help="Keep the chapter mini-PDF after extraction.")
    args = p.parse_args()

    repo = Path(args.repo_root).resolve()
    load_dotenv(repo / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-pro")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set (check .env)", file=sys.stderr)
        return 2

    book_pdf = repo / "raw" / f"FRM 2026 Part II Book {args.book}.pdf"
    if not book_pdf.exists():
        print(f"ERROR: PDF not found: {book_pdf}", file=sys.stderr)
        return 2

    print(f"[1/5] Scanning {book_pdf.name} for chapter boundaries...")
    pages = find_reading_pages(book_pdf)
    if args.reading not in pages:
        print(f"ERROR: Reading {args.reading} not found. Available: {sorted(pages)}",
              file=sys.stderr)
        return 2

    start = pages[args.reading]
    next_readings = sorted(n for n in pages if n > args.reading)
    end = pages[next_readings[0]] - 1 if next_readings else len(
        pdfium.PdfDocument(str(book_pdf))
    )
    end += args.end_padding
    print(f"      Reading {args.reading}: pages {start}-{end} ({end - start + 1} pages)")

    print(f"[2/5] Slicing chapter into mini-PDF...")
    out_dir = repo / "out"
    out_dir.mkdir(exist_ok=True)
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

    print(f"[4/5] Sending to Gemini ({model_name})...")
    client = genai.Client(api_key=api_key)
    pdf_bytes = mini_pdf.read_bytes()
    contents = [
        types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
        prompt,
    ]
    resp = client.models.generate_content(
        model=model_name,
        contents=contents,
    )
    text = resp.text or ""
    if not text.strip():
        print("ERROR: Gemini returned empty response", file=sys.stderr)
        return 3
    # Token usage report
    if hasattr(resp, "usage_metadata") and resp.usage_metadata:
        u = resp.usage_metadata
        print(f"      Tokens: in={getattr(u, 'prompt_token_count', '?')} "
              f"out={getattr(u, 'candidates_token_count', '?')} "
              f"total={getattr(u, 'total_token_count', '?')}")

    print(f"[5/5] Writing output...")
    dst_dir = repo / "wiki" / BOOK_DIRS[args.book]
    dst_dir.mkdir(parents=True, exist_ok=True)
    suffix = "gemini.md" if args.output == "schema_b" else "raw.gemini.md"
    dst = dst_dir / f"R{args.reading}.{suffix}"
    dst.write_text(text, encoding="utf-8")
    print(f"      Wrote {dst} ({len(text):,} chars)")

    if not args.keep_mini_pdf:
        mini_pdf.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
