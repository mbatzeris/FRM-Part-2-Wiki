# FRM Part 2 Wiki — Personal Study System

An active-recall + spaced-repetition study system for FRM Part 2 (Nov 2026 exam), combining **Schema B reading compression**, **LO-level readiness tracking**, and **error archetype logging**. Built for a working parent with ~5 study hours per week.

## Exam target

- **Date:** Saturday 21 November 2026
- **Historical pass rate:** ~52%
- **Personal target:** 75%+ on mocks (≥ 90% estimated pass probability)
- **Readiness goal:** Overall LO readiness ≥ 0.75 by Week 28 (2 Nov 2026)

## Status

- ✅ **Completed:** R30 Credit Risk (gold-standard Schema B, 7 LOs tracked)
- ⏳ **Pending:** 77 readings remaining (R1–R29, R31–R107)
- 📊 **Current readiness:** 0.5% (baseline, Week 1)

## Architecture

```
FRM 2/
├── .gitignore
├── README.md                                  ← this file
├── .windsurf/workflows/new-reading.md         ← conversion pipeline + LLM prompt
├── raw/                                        ← immutable source PDFs (5 books)
├── system/                                     ← legacy prompts (reference only)
└── wiki/
    ├── _TEMPLATE_Reading.md                    ← Schema B skeleton
    ├── _LO_TRACKER.md                          ← master LO readiness (your SRS)
    ├── _WEEKLY_LOG.md                          ← Sunday check-in template
    ├── _READINESS_DASHBOARD.md                 ← rolled-up exam-readiness %
    ├── _ERROR_ARCHETYPES.md                    ← your personal distractor decoder
    └── Book 2 - Credit Risk/
        ├── R30_Credit_Risk.md                  ← gold-standard reading
        ├── Book2.txt                           ← pdftotext extract
        └── FRM 2026 Part II Book 2.pdf
```

## Adding a New Reading

1. Type `/new-reading` in Cascade.
2. Provide **reading number** and **book number**.
3. Workflow auto-extracts the chapter, calls the LLM, produces a Schema B `.md`.
4. Manual 16-item §9 checklist pass.
5. Append the reading's LOs to `wiki/_LO_TRACKER.md` (new row per LO).
6. Commit.

Full pipeline details in `.windsurf/workflows/new-reading.md`.

---

## Methodology

This system rests on three evidence-backed learning mechanisms plus one diagnostic:

1. **Active recall** (Roediger & Karpicke, 2006) — every reading is compressed into Schema B propositions you must reconstruct, not re-read.
2. **Spaced repetition** (Leitner; Ebbinghaus) — the `_LO_TRACKER.md` schedules each LO for re-drill at 3 → 7 → 14 → 30 → 60 day intervals based on last performance.
3. **Error-driven learning** — wrong answers are logged in `_ERROR_ARCHETYPES.md` and folded back into `§5 Ambiguity Traps` of the relevant Schema B file.
4. **Readiness indicator** — a single number, updated weekly, that quantifies exam preparedness and forecasts vs target.

### The Weekly Loop (every Sunday, ~10 min)

```
1. Open _LO_TRACKER.md → sort by Next Review date
2. Identify the 3 most urgent LOs (top of list, or 🔴 status)
3. Plan 2-3 readings + those 3 LO drills for the coming week
4. Fill in a new entry in _WEEKLY_LOG.md
5. Check _READINESS_DASHBOARD.md trajectory vs target
6. git commit -m "Week N log"
```

### Per-LO Drill Session (~45 min per LO cluster of 3)

```
1. LEARN     → Open Schema B proposition, read + AnalystPrep video clip
2. APPLY     → 3 questions from AnalystPrep filtered to that LO
3. DIAGNOSE  → For each wrong Q, log archetype in _ERROR_ARCHETYPES.md
4. COMPRESS  → Add any new trap to that reading's §5
5. RECORD    → Update _LO_TRACKER.md row: Last Reviewed, Confidence (0-5),
              Q C/A, Accuracy, new Readiness, new Next Review date
6. REINFORCE → NotebookLM audio of the Schema B for tomorrow's commute
```

### Readiness Formula

```
LO_Readiness  = 0.60 × accuracy(last 5 questions)
              + 0.30 × self_confidence/5
              + 0.10 × max(0, 1 − days_since_review/30)

Book_Readiness = Σ (LO_Readiness × coverage_fraction)
Exam_Readiness = Σ (Book_Readiness × Book_exam_weight)

Book weights: Market 20% · Credit 20% · OpRisk 20% · Liquidity 15% · Invest+Issues 25%
```

### Leitner Schedule (spaced repetition)

| Last Session | Next Review After |
|:--|:--|
| New LO | +3 days |
| < 60% | +3 days (repeat) |
| 60–79% | +7 days |
| 80–100% (1st time) | +14 days |
| 80–100% (2nd consecutive) | +30 days → 🟢 Green |
| Green + ≥80% | +60 days → ⭐ Graduated |
| Any drop < 60% | Reset to +3 days → 🔴 Red |

### Success Gates

| Milestone | Readiness Threshold | If below |
|:--|:--:|:--|
| Week 13 (end of Book 3) | ≥ 0.35 | Cut 1 reading/week, focus drills |
| Week 22 (end of foundation) | ≥ 0.60 | Add Sunday double-session |
| Week 24 (Mock 1) | Mock ≥ 55% | Deep archetype post-mortem Week 25 |
| Week 28 (target date) | ≥ 0.75 | On track to pass |
| Week 30 (Mock 4) | Mock ≥ 72% | Confident in exam week |

## Weekly Time Budget

| Slot | Duration | Mode | Content |
|:--|:--:|:--|:--|
| Mon evening | 1h | Active | AnalystPrep video(s) |
| Tue evening | 1h | Active | AnalystPrep reading, highlight LOs |
| Wed evening | 1h | Active | `/new-reading` Schema B build |
| Thu lunch | 30m | Active | AnalystPrep Q-bank on new LOs |
| Fri lunch | 30m | Active | Q-bank + update `_LO_TRACKER.md` |
| Sun 14:00–16:00 | 2h | Active | Second reading of week, condensed |
| Mon–Fri commute | ~40m × 5 | Passive | NotebookLM audio on last week's Schema B |
| Daily gaps | 5–15m | Passive | Anki-style self-quiz from Schema B §5 |

**Active total: 6h/week · Passive total: ~5h/week · Skip Saturday entirely** (parenting).

## Tool Stack

| Tool | Role | Cost |
|:--|:--|:--|
| **AnalystPrep** | Primary content: videos, Q-bank, mocks | already paid |
| **NotebookLM** | Audio podcasts from Schema B files → commute | free |
| **This wiki** | Active synthesis + LO SRS + error taxonomy | free |
| **Cascade + Claude Sonnet 4.5** | `/new-reading` pipeline | ~$15 for all readings |
| **GARP Part 1 formula sheet** | Quant refresher, Weeks 1–8 | free |
| **GARP practice exam** | Final mock (Week 28) | free / in registration |

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
