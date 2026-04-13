# FRM Part 2 Wiki — Knowledge Base & Study System

A comprehensive, 4-layer knowledge base for the FRM Part 2 Exam (2026 cycle). Contains 107 Boole Scaffolds covering all 5 core books with cross-domain boundary event mapping.

## Architecture

```
FRM 2/
├── raw/              # Immutable source PDFs + extracted text
├── system/           # AI engine prompts, templates, workflow docs
├── wiki/             # 107 Boole Scaffolds + boundary events
├── ops/              # Operational tools (tracker, formulas, drills, calendar)
└── temp/             # Temporary/processed files (excluded from git)
```

## The Boole Scaffold Framework

Each reading uses a 5-section structure designed for falsification training:

1. **Foundational Propositions** — Core axioms tagged by constraint hierarchy `[REG] > [APP] > [ECO] > [THE]`
2. **Constraint Stress-Tests** — "What flips the answer?" falsification drills
3. **Dependency & Noise Map** — Signal detection vs exam distractors
4. **Directional Intuition** — Rapid ↑/↓ relationship chains
5. **Ambiguity Traps** — Anti-decoder tips for GARP distractor patterns

## Quick Start

### Study a Reading
1. Navigate to `wiki/Book N - Topic/R[XX]_[Topic].md`
2. Read the scaffold sections 1-5
3. Run the system prompt drill: "Execute system prompt for R[XX]"
4. Practice with drill bank questions in `ops/06_DRILL_BANK.md`

### Track Progress
- Update `wiki/Book N/_index.md` after completing each reading
- Use `ops/04_LO_TRACKER.md` for Learning Objective tracking
- Follow the schedule in `ops/08_STUDY_CALENDAR.md`

### Cross-Domain Practice
- Review `wiki/_boundary_events.md` for 10 cascading risk scenarios
- Practice with `ops/09_BOUNDARY_EVENTS.md` vignette templates
- Focus on boundary events that span multiple books

## Key Files

| File | Purpose |
|------|---------|
| `index.md` | Root sitemap with quick commands |
| `wiki/_index.md` | Wiki overview with book status |
| `wiki/_boundary_events.md` | Cross-domain cascade map |
| `ops/05_FORMULA_ENGINE.md` | Directional math reference by domain |
| `ops/06_DRILL_BANK.md` | 45 tagged practice questions |
| `ops/10_LO_READING_MAP.md` | LO → Reading mapping table |

## Constraint Hierarchy

When answering GARP-style questions, apply constraints in order:
1. **[REG]** Regulatory mandates (Basel/FRTB/Supervisory)
2. **[APP]** Vignette constraints (Risk Appetite/Stem cues)
3. **[ECO]** First-order economic logic
4. **[THE]** Theoretical purity (only if explicitly asked)

## Version Control

This project uses git for version control. Source PDFs and temporary files are excluded via `.gitignore`.

## License

Personal study material for FRM Part 2 exam preparation.
