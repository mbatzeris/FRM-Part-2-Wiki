#!/usr/bin/env python3
"""Verify Schema B §1 formulas trace to the raw Gemini extract (symbol-coverage check).

For each bold formula in a Schema B reading's §1 Foundational Propositions, this
script checks that every distinctive symbol (Unicode Greek letters, multi-letter
uppercase abbreviations like CVA/LGD/EAD, common math operators) appears somewhere
in the R{N}.raw.gemini.md extract — in either Unicode or LaTeX form.

Designed to catch fabrication: if a Schema B formula contains a Greek letter or
abbreviation that is NOT present in the raw PDF extract, that is evidence the
formula was reconstructed from training data instead of sourced from the PDF.

Usage:
    python scripts/verify_formulas.py --reading 30 --book 2
    python scripts/verify_formulas.py --reading 31 --book 2 --schema <path> --raw <path>

Exit codes:
    0 - all formulas have full symbol coverage in raw extract
    1 - one or more formulas flagged (listed in stdout)
    2 - IO / args / file-not-found error
"""
import argparse
import re
import sys
from pathlib import Path

GREEK_UNICODE_TO_LATEX = {
    'λ': r'\lambda',  'ρ': r'\rho',    'σ': r'\sigma',
    'μ': r'\mu',      'α': r'\alpha',  'β': r'\beta',
    'γ': r'\gamma',   'τ': r'\tau',    'π': r'\pi',
    'θ': r'\theta',   'φ': r'\phi',    'Φ': r'\Phi',
    'Σ': r'\Sigma',   'Δ': r'\Delta',  'ω': r'\omega',
    'ε': r'\epsilon', 'δ': r'\delta',
}


def find_symbols(formula: str) -> set[str]:
    """Return the set of distinctive symbols appearing in a formula."""
    syms: set[str] = {ch for ch in formula if ch in GREEK_UNICODE_TO_LATEX}
    syms |= set(re.findall(r'\b[A-Z]{2,6}\b', formula))
    for marker in ('N⁻¹', '√', 'e^'):
        if marker in formula:
            syms.add(marker)
    return syms


def in_raw(sym: str, raw: str) -> bool:
    """Return True if `sym` appears in `raw` (Unicode or common LaTeX form)."""
    if sym in raw:
        return True
    if sym in GREEK_UNICODE_TO_LATEX and GREEK_UNICODE_TO_LATEX[sym] in raw:
        return True
    if sym == 'N⁻¹':
        return any(alt in raw for alt in ('N^{-1}', 'N^-1', 'N^{−1}'))
    if sym == '√':
        return r'\sqrt' in raw
    if sym == 'e^':
        return 'e^' in raw or r'\exp' in raw or 'exp(' in raw
    return False


def locate_files(repo: Path, book: int, reading: int,
                 schema_override: str | None, raw_override: str | None):
    """Resolve the Schema B path and raw Gemini path. Returns (schema, raw) or (None, None)."""
    if schema_override:
        schema = Path(schema_override)
    else:
        cands = [
            p for p in (repo / 'wiki').glob(f'Book {book} - */R{reading}_*.md')
            if not any(p.name.endswith(s) for s in
                       ('.raw.gemini.md', '.gemini.md', '.partial.gemini.md'))
        ]
        if len(cands) != 1:
            print(f"ERROR: expected 1 Schema B match under wiki/Book {book} - */R{reading}_*.md, "
                  f"got {len(cands)}: {cands}", file=sys.stderr)
            return None, None
        schema = cands[0]
    raw = Path(raw_override) if raw_override else schema.parent / f'R{reading}.raw.gemini.md'
    if not schema.exists():
        print(f"ERROR: Schema B file not found: {schema}", file=sys.stderr)
        return None, None
    if not raw.exists():
        print(f"ERROR: raw Gemini extract not found: {raw}", file=sys.stderr)
        return None, None
    return schema, raw


def extract_bold_formulas(section_1: str) -> list[tuple[str, str]]:
    """Return list of (proposition_id, formula_text) for bold formulas in §1.

    Splits each proposition body on `**` so odd-indexed parts are exactly the bold
    blocks. A naive regex like `\\*\\*([^*]*[=≈][^*]*)\\*\\*` is incorrect because in
    `**A** prose with = **B**` the closing `**` of A and opening `**` of B form a
    spurious match capturing ` prose with = ` as if it were bold.
    """
    rows = re.findall(r'\| P(\d+) \|(.+?)(?=\n\| P\d+ \||\Z)', section_1, re.DOTALL)
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str]] = []
    for pid, body in rows:
        parts = body.split('**')
        # parts[0] is pre-bold; odd indices are inside bold; even>0 are between bolds.
        for i in range(1, len(parts), 2):
            f = parts[i].strip()
            if f and ('=' in f or '≈' in f):
                key = (f'P{pid}', f)
                if key not in seen:
                    seen.add(key)
                    out.append(key)
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--reading', type=int, required=True)
    p.add_argument('--book', type=int, required=True)
    p.add_argument('--schema', help='Override Schema B path (default: auto-glob)')
    p.add_argument('--raw', help='Override raw extract path (default: <schema_dir>/R{N}.raw.gemini.md)')
    a = p.parse_args()

    repo = Path(__file__).resolve().parent.parent
    schema, raw = locate_files(repo, a.book, a.reading, a.schema, a.raw)
    if schema is None:
        return 2

    text = schema.read_text(encoding='utf-8')
    m = re.search(r'## 1\. Foundational Propositions[^\n]*\n(.*?)(?=\n## 2\.)', text, re.DOTALL)
    if not m:
        print(f"ERROR: could not locate §1 in {schema}", file=sys.stderr)
        return 2

    formulas = extract_bold_formulas(m.group(1))
    if not formulas:
        print(f"WARN: no bold formulas found in §1 of {schema.name}")
        return 0

    raw_text = raw.read_text(encoding='utf-8')
    print(f"Checking {len(formulas)} bold formula(s) from {schema.name} against {raw.name}\n")
    flagged = 0
    for pid, f in formulas:
        syms = find_symbols(f)
        if not syms:
            continue
        missing = sorted(s for s in syms if not in_raw(s, raw_text))
        if missing:
            flagged += 1
            preview = f if len(f) <= 80 else f[:77] + '...'
            print(f"  [{pid}] missing {missing}")
            print(f"    formula: {preview}")

    total = len(formulas)
    if flagged:
        print(f"\n{flagged}/{total} formula(s) flagged. Hand-verify against raw extract before committing.")
        return 1
    print(f"OK: all {total} bold formula(s) in §1 have symbol coverage in raw extract.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
