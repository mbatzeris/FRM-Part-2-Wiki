# FRM Part 2 Wiki — Clean Slate

A single-reading knowledge base with a reusable Schema B pipeline for converting Schweser chapters into structured FRM Part 2 study files.

## Status

- ✅ **Completed:** R30 Credit Risk — gold-standard reference, 16/16 on Schema B checklist
- ⏳ **Pending:** R1–R29, R31–R107 — add one at a time via the `/new-reading` workflow

## Architecture

```
FRM 2/
├── .gitignore
├── README.md                                 ← this file
├── .windsurf/
│   └── workflows/
│       └── new-reading.md                    ← pipeline + LLM master prompt
├── raw/                                       ← immutable source PDFs
│   ├── FRM 2026 Part II Book 1.pdf           (Market Risk, R1–R18)
│   ├── FRM 2026 Part II Book 2.pdf           (Credit Risk, R19–R41)
│   ├── FRM 2026 Part II Book 3.pdf           (Operational Risk, R42–R65)
│   ├── FRM 2026 Part II Book 4.pdf           (Liquidity Risk, R66–R82)
│   └── FRM 2026 Part II Book 5.pdf           (Investment Risk + Current Issues, R83–R107)
├── system/                                    ← legacy LLM prompts (reference only)
│   ├── 00_SYSTEM_PROMPT.md
│   ├── 01_BOOLE_SCAFFOLD_TEMPLATE.md
│   ├── 02_AMBIGUITY_DECODER.md
│   └── 03_ANTIGRAVITY_WORKFLOW.md
└── wiki/
    ├── _TEMPLATE_Reading.md                   ← Schema B skeleton
    └── Book 2 - Credit Risk/
        ├── R30_Credit_Risk.md                 ← gold standard
        ├── Book2.txt                          ← pdftotext extract
        └── FRM 2026 Part II Book 2.pdf        ← convenience copy
```

## Adding a New Reading

1. Type `/new-reading` in Cascade.
2. Provide **reading number** and **book number**.
3. Workflow auto-extracts the chapter, calls the LLM, produces a Schema B `.md`.
4. Manual 16-item §9 checklist pass.
5. Commit.

Full pipeline details in `.windsurf/workflows/new-reading.md`.

## Schema B Structure (per reading)

| § | Section | Content |
|:--:|:--|:--|
| 1 | **Foundational Propositions** | One per LO; 5-column table (ID / Prop + Intuition / Tag / Exam Dominance / Trigger Phrase) |
| 2 | **Constraint Stress-Test** | 3-column falsification drills with numerical answers |
| 3 | **Dependency & Noise Map** | Signal / Noise / **Tensions** (two canonical tags) |
| 4 | **Directional Intuition** | Unicode-arrow sensitivity chains (no LaTeX) |
| 5 | **Ambiguity Traps** | ≥8 anti-decoder bullets |

## 16-Item Compliance Checklist

1. Em-dash title `—` (not hyphen)
2. Exam Priority emoji (🔴 🟡 🟢)
3. Metadata block (Source / LOs / Related)
4. §1 header has 5 columns
5. §1 alignment row `|:---|:---|:---:|:---|:---|`
6. Proposition IDs `P1`, `P2`, … sequential
7. Every proposition has `*Intuition: …*` inlined
8. Canonical tags only: `[THE]` `[REG]` `[OPS]` `[ECO]`
9. Exam Dominance format: `{rating} — {reason}`
10. Trigger Phrase: comma-separated `"quoted"` terms
11. §2 3-column table with `|:---|:---|:---|`
12. §3 has Signal / Noise / **Tensions** (Tensions mandatory)
13. §4 uses Unicode arrows, zero LaTeX
14. §5 ≥8 bullets
15. Footer `**Cross-Domain Linkage:** [[Boundary Events]]`
16. No LaTeX rendering errors

## Canonical Tag Set

| Tag | Meaning |
|:--:|:--|
| `[THE]` | Theory / mathematics / formulas |
| `[REG]` | Regulation / Basel / supervisory rules |
| `[OPS]` | Operations / governance / process |
| `[ECO]` | Economics / valuation / pricing |

## LLM Recommendation

**Claude Sonnet 4.5** — best schema fidelity, no formula hallucination.
- Cost: ~$0.14/reading
- Total for ~106 remaining readings: ~$15
- Full cost/quality comparison in `.windsurf/workflows/new-reading.md`

## PDF Text Extraction

The pipeline uses **Poppler `pdftotext`** (already installed):
```powershell
& "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdftotext.exe" -layout "raw\FRM 2026 Part II Book N.pdf" "wiki\Book N - Name\BookN.txt"
```

## Git Safety

All deletions are recoverable via `git restore <path>` from prior commits. Source PDFs (`raw/*.pdf`) and `temp/` are `.gitignore`d.

## License

Personal study material for FRM Part 2 exam preparation.
