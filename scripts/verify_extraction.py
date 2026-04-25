#!/usr/bin/env python3
"""
verify_extraction.py — Pre-LLM extraction verifier for FRM Schema B pipeline.

Detects silent extraction failures in pdftotext output:
  B1  Orphan "defined-as" sentences (formula vanished)
  B2  Figure/Table caption without numeric payload
  W1  Subscript/superscript collapse (E0, VT, etc.)
  W2  Hyphenation broken at line wraps
  W3  Greek-letter expectation violated
  W4  Page-density below sane threshold

Usage:
  python scripts/verify_extraction.py \
    --reading R30 \
    --book "Book 2 - Credit Risk" \
    --start-marker "READING 30" \
    --end-marker "READING 31"

Exit codes:
  0  clean
  1  warnings only
  2  blockers present (pipeline must stop)

Stdlib-only. Reads the book .txt extract, slices the chapter, runs all checks,
emits a markdown audit file next to the source.
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
from datetime import datetime


# --- Patterns ------------------------------------------------------------

# B1: a line ending in a "defined-as" cue with a colon
DEFINED_AS_PATTERN = re.compile(
    r"\b("
    r"is\s+defined\s+as|"
    r"are\s+defined\s+as|"
    r"can\s+be\s+defined\s+as|"
    r"is\s+equal\s+to|"
    r"is\s+approximated\s+as|"
    r"can\s+be\s+approximated\s+as|"
    r"is\s+computed\s+as|"
    r"is\s+given\s+by|"
    r"is\s+written\s+as|"
    r"is\s+expressed\s+as|"
    r"takes?\s+the\s+form|"
    r"can\s+be\s+written\s+as|"
    r"can\s+be\s+expressed\s+as"
    r")\s*:\s*$",
    re.IGNORECASE,
)

# A line that "looks like" a formula: has math operators, Greek, numbers w/ ops, etc.
FORMULA_HINT = re.compile(
    r"[=+\-*/^√∫∑∏≈≤≥≠±·×÷⋅]"               # math operators
    r"|[αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ]"  # Greek
    r"|[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]"                       # superscripts
    r"|[₀₁₂₃₄₅₆₇₈₉]"                          # subscripts
    r"|\bln\(|\blog\(|\bexp\(|\bmax\(|\bmin\(|\bN\(|\bN\^|\bE\["
    r"|\$"                                    # LaTeX dollar
    r"|^\s*[A-Za-z][A-Za-z0-9_]{0,3}\s*=",    # `X =` style assignment
)

CAPTION_PATTERN = re.compile(r"^\s*(Figure|Table)\s+\d+\.\d+\s*:", re.IGNORECASE)
NUMERIC_PAYLOAD = re.compile(r"\d+(\.\d+)?\s*%?|\bN\(|[=+\-*/]")
SUBSCRIPT_COLLAPSE = re.compile(r"\b([A-Z][a-z]?)([0-9])\b")  # E0, VT not matched by lowercase first letter
HYPHEN_BREAK = re.compile(r"([a-z])-\n([a-z])")
GREEK_LETTERS = re.compile(r"[αβγδεζηθικλμνξοπρστυφχψω]")
GREEK_TRIGGERS = re.compile(
    r"\b(hazard\s+rate|correlation|volatilit(?:y|ies)|intensity|sigma|rho|lambda|mu)\b",
    re.IGNORECASE,
)


# --- Slicer --------------------------------------------------------------

def slice_chapter(text: str, start_marker: str, end_marker: str) -> tuple[str, int, int]:
    """Return (chapter_text, start_line, end_line). Lines are 1-indexed.

    Strategy: find ALL occurrences of start_marker and end_marker, then pick the
    pairing that yields the LARGEST slice. This skips TOC/index false matches
    (which produce tiny slices) and locks onto the actual chapter body.
    """
    lines = text.splitlines()
    starts = [i for i, ln in enumerate(lines) if start_marker.lower() in ln.lower()]
    ends = [i for i, ln in enumerate(lines) if end_marker.lower() in ln.lower()]
    if not starts:
        raise ValueError(f"Start marker {start_marker!r} not found")

    best_pair = None
    best_size = -1
    for s in starts:
        # find smallest end > s; if none, end-of-file
        candidate_ends = [e for e in ends if e > s]
        e = min(candidate_ends) if candidate_ends else len(lines)
        size = e - s
        if size > best_size:
            best_size = size
            best_pair = (s, e)

    if best_pair is None:
        raise ValueError(f"Could not pair {start_marker!r} with {end_marker!r}")
    s, e = best_pair
    return "\n".join(lines[s:e]), s + 1, e


# --- Checks --------------------------------------------------------------

def check_orphan_definitions(lines: list[str], start_offset: int) -> list[dict]:
    """B1: 'defined as:' followed by a non-formula line."""
    findings = []
    for i, ln in enumerate(lines):
        m = DEFINED_AS_PATTERN.search(ln)
        if not m:
            continue
        # Look ahead up to 3 non-blank lines for a formula token
        looked_ahead = 0
        formula_found = False
        for j in range(i + 1, min(i + 6, len(lines))):
            nxt = lines[j].strip()
            if not nxt:
                continue
            looked_ahead += 1
            if FORMULA_HINT.search(nxt):
                formula_found = True
                break
            if looked_ahead >= 3:
                break
        if not formula_found:
            findings.append({
                "level": "BLOCKER",
                "code": "B1",
                "line": i + start_offset,
                "snippet": ln.strip()[-80:],
                "msg": f"Sentence ends with '{m.group(1)}:' but no formula follows within 3 non-blank lines.",
            })
    return findings


def check_caption_payload(lines: list[str], start_offset: int) -> list[dict]:
    """B2: Figure/Table caption without numeric payload nearby."""
    findings = []
    for i, ln in enumerate(lines):
        if not CAPTION_PATTERN.search(ln):
            continue
        payload_found = False
        for j in range(i + 1, min(i + 9, len(lines))):
            if NUMERIC_PAYLOAD.search(lines[j]):
                payload_found = True
                break
        if not payload_found:
            findings.append({
                "level": "BLOCKER",
                "code": "B2",
                "line": i + start_offset,
                "snippet": ln.strip()[:80],
                "msg": "Caption with no numeric/formula payload in next 8 lines (likely table/figure dropped).",
            })
    return findings


def check_subscript_collapse(text: str, start_offset: int) -> list[dict]:
    """W1: tokens like E0, VT, PD1 likely collapsed subscripts."""
    findings = []
    seen = {}
    # Only flag when the token sits in math context: surrounded by math-ish tokens within a small window
    for m in SUBSCRIPT_COLLAPSE.finditer(text):
        token = m.group(0)
        # Skip common non-math tokens
        if token.lower() in {"r1", "r2", "r3", "h1", "h2", "h3", "g7", "g8", "g20", "p1", "p2"}:
            continue
        # Math context heuristic: nearby = sign or parenthesis or another math token
        window = text[max(0, m.start() - 30): m.end() + 30]
        if "=" in window or FORMULA_HINT.search(window):
            seen[token] = seen.get(token, 0) + 1
    for token, count in sorted(seen.items(), key=lambda x: -x[1]):
        if count >= 2:  # require repetition to reduce noise
            findings.append({
                "level": "WARN",
                "code": "W1",
                "line": "—",
                "snippet": token,
                "msg": f"Token '{token}' appears {count}× in math context — likely collapsed subscript/superscript.",
            })
    return findings


def check_hyphen_breaks(text: str, start_offset: int) -> list[dict]:
    """W2: hyphenation broken across line wraps."""
    matches = HYPHEN_BREAK.findall(text)
    if not matches:
        return []
    return [{
        "level": "WARN",
        "code": "W2",
        "line": "—",
        "snippet": f"{len(matches)} occurrences",
        "msg": f"Hyphenated line-breaks detected ({len(matches)}× pattern '[a-z]-\\n[a-z]'). Recommend rejoin pre-LLM.",
    }]


def check_greek_expectation(text: str) -> list[dict]:
    """W3: text mentions hazard/correlation/etc. but no Greek letters present."""
    triggers = len(GREEK_TRIGGERS.findall(text))
    greeks = len(GREEK_LETTERS.findall(text))
    if triggers >= 2 and greeks == 0:
        return [{
            "level": "WARN",
            "code": "W3",
            "line": "—",
            "snippet": f"{triggers} Greek-trigger terms / 0 Greek letters",
            "msg": "Text discusses concepts that require Greek symbols (λ, ρ, σ, etc.) but none appear in extract.",
        }]
    return []


def check_page_density(text: str, est_pages: int | None) -> list[dict]:
    """W4: char count vs estimated pages."""
    chars = len(text)
    if est_pages and est_pages > 0:
        density = chars / est_pages
        if density < 1500:
            return [{
                "level": "WARN",
                "code": "W4",
                "line": "—",
                "snippet": f"{chars} chars / {est_pages} pages = {density:.0f} chars/page",
                "msg": "Density below 1500 chars/page — extraction may have dropped large regions.",
            }]
    return []


# --- Audit writer --------------------------------------------------------

def write_audit(out_path: Path, reading: str, src_path: Path, start_line: int,
                end_line: int, findings: list[dict]) -> tuple[int, int]:
    blockers = [f for f in findings if f["level"] == "BLOCKER"]
    warnings = [f for f in findings if f["level"] == "WARN"]

    lines = []
    lines.append(f"# Extraction Audit — {reading}")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Source:** `{src_path.as_posix()}`")
    lines.append(f"**Slice:** lines {start_line}–{end_line}")
    lines.append(f"**Result:** {len(blockers)} blocker(s), {len(warnings)} warning(s)")
    lines.append("")
    lines.append("---")
    lines.append("")

    if blockers:
        lines.append("## 🔴 Blockers (must fix before LLM call)")
        lines.append("")
        lines.append("| Code | Line | Issue | Snippet |")
        lines.append("|:--|:--:|:--|:--|")
        for f in blockers:
            snip = f["snippet"].replace("|", "\\|")
            lines.append(f"| {f['code']} | {f['line']} | {f['msg']} | `{snip}` |")
        lines.append("")

    if warnings:
        lines.append("## 🟡 Warnings (review recommended)")
        lines.append("")
        lines.append("| Code | Line | Issue | Snippet |")
        lines.append("|:--|:--:|:--|:--|")
        for f in warnings:
            snip = f["snippet"].replace("|", "\\|")
            lines.append(f"| {f['code']} | {f['line']} | {f['msg']} | `{snip}` |")
        lines.append("")

    if not findings:
        lines.append("## ✅ Clean")
        lines.append("")
        lines.append("No issues detected.")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Check legend")
    lines.append("")
    lines.append("- **B1** — Orphan 'defined-as:' sentence (formula vanished)")
    lines.append("- **B2** — Figure/Table caption without numeric payload")
    lines.append("- **W1** — Subscript/superscript collapse (e.g., `E_0` → `E0`)")
    lines.append("- **W2** — Hyphenation broken at line wrap")
    lines.append("- **W3** — Greek-letter expectation violated")
    lines.append("- **W4** — Page-density below 1500 chars/page")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return len(blockers), len(warnings)


# --- Main ----------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description="Verify FRM PDF extraction quality.")
    p.add_argument("--reading", required=True, help="Reading code, e.g., R30")
    p.add_argument("--book", required=True, help="Book folder name, e.g., 'Book 2 - Credit Risk'")
    p.add_argument("--start-marker", required=True, help="Chapter start marker, e.g., 'READING 30'")
    p.add_argument("--end-marker", required=True, help="Chapter end marker, e.g., 'READING 31'")
    p.add_argument("--book-txt", default=None, help="Override path to book .txt extract")
    p.add_argument("--est-pages", type=int, default=None, help="Estimated PDF pages for density check")
    p.add_argument("--repo-root", default=".", help="Repo root path")
    args = p.parse_args()

    repo = Path(args.repo_root).resolve()
    book_dir = repo / "wiki" / args.book
    if not book_dir.exists():
        print(f"ERROR: Book directory not found: {book_dir}", file=sys.stderr)
        return 3

    if args.book_txt:
        src = Path(args.book_txt)
    else:
        # Find Book{N}.txt by glob
        candidates = list(book_dir.glob("Book*.txt"))
        if not candidates:
            print(f"ERROR: No Book*.txt found in {book_dir}", file=sys.stderr)
            return 3
        src = candidates[0]

    if not src.exists():
        print(f"ERROR: Source text not found: {src}", file=sys.stderr)
        return 3

    text = src.read_text(encoding="utf-8", errors="replace")

    try:
        chapter, start_line, end_line = slice_chapter(text, args.start_marker, args.end_marker)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 3

    chapter_lines = chapter.splitlines()

    findings: list[dict] = []
    findings += check_orphan_definitions(chapter_lines, start_line)
    findings += check_caption_payload(chapter_lines, start_line)
    findings += check_subscript_collapse(chapter, start_line)
    findings += check_hyphen_breaks(chapter, start_line)
    findings += check_greek_expectation(chapter)
    findings += check_page_density(chapter, args.est_pages)

    out_path = book_dir / f"{args.reading}_extraction_audit.md"
    blockers, warnings = write_audit(out_path, args.reading, src, start_line, end_line, findings)

    print(f"Audit written: {out_path}")
    print(f"  Blockers: {blockers}")
    print(f"  Warnings: {warnings}")

    if blockers:
        return 2
    if warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
