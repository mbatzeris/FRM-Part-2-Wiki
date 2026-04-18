# FRM Part 2 — LLM Wiki Master Map

Welcome to the root directory. This architecture turns passive study materials into an active, compiled knowledge base using a 4-folder layout (`raw/`, `system/`, `wiki/`, `ops/`) with a 5-section Boole Scaffold per reading.

## 📁 Architecture

### `raw/` — Source Data (Immutable)
Raw readings provided by GARP/Schweser. **Do not edit files in this folder.**
- `FRM 2026 Part II Book 1.pdf` + `.md` — Market Risk source
- `FRM 2026 Part II Book 2.pdf` + `.md` — Credit Risk source
- `FRM 2026 Part II Book 3.pdf` + `.md` — Operational Risk source
- `FRM 2026 Part II Book 4.pdf` + `.md` — Liquidity Risk source
- `FRM 2026 Part II Book 5.pdf` + `.md` — Investment Risk + Current Issues source
- `2026-04-13-CR-10-Credit-Value-at-Risk-*.pdf` — Credit VaR chapter extracts
- `Exam Question Ambiguity Training Roadmap.txt` — Distractor taxonomy reference

### `system/` — AI Engine (Prompts & Templates)
Frameworks and instructions that Antigravity uses to process `raw/` files into `wiki/` output.
- `00_SYSTEM_PROMPT.md` — Core persona and constraint hierarchy
- `01_BOOLE_SCAFFOLD_TEMPLATE.md` — Scaffold output template (5 sections)
- `02_AMBIGUITY_DECODER.md` — Distractor archetypes taxonomy
- `03_ANTIGRAVITY_WORKFLOW.md` — Operational pipeline and study loop

### `wiki/` — Compiled Knowledge Base (Boole Scaffolds by Book)
Your actual study environment. Contains per-chapter scaffolds organized by GARP Book.
- `Book 1 - Market Risk/` (R1–R18) — 20% exam weight
- `Book 2 - Credit Risk/` (R19–R41) — 20% exam weight
- `Book 3 - Operational Risk/` (R42–R65) — 20% exam weight
- `Book 4 - Liquidity Risk/` (R66–R82) — 15% exam weight
- `Book 5 - Investment Risk/` (R83–R99) — 15% exam weight
- `Book 5 - Investment Risk/` (R100–R107, *Current Issues in Financial Markets*) — 10% exam weight

*Total: 100%. R100–R107 live inside the Book 5 folder but constitute GARP's separate "Current Issues" domain.*

Each Book folder has an `_index.md` tracking progress across readings.

### `ops/` — Operational Tools (Tracking, Drills, Schedule)
Cross-cutting tools that span all domains.
- `04_LO_TRACKER.md` — Executive dashboard for Learning Objectives
- `05_FORMULA_ENGINE.md` — Directional math reference by domain
- `06_DRILL_BANK.md` — 62 tagged combat simulation questions
- `07_ERROR_LOG.md` — Mistake tracking with distractor archetype analysis
- `08_STUDY_CALENDAR.md` — 16-week study schedule with spaced repetition
- `09_BOUNDARY_EVENTS.md` — Cross-domain drill templates
- `10_LO_READING_MAP.md` — LO → Reading mapping table
- `12_WEAK_LINK_RADAR.md` — Adaptive weak-area diagnostic
- `13_CHEAT_SHEETS.md` — Condensed last-mile reference sheets
- `wiki/_boundary_events.md` — Structural cross-domain linkage map (Ref Class)

---

## Operational Workflow

### Compiling a New Reading
1. Drop the PDF into `raw/`
2. Open a session with Antigravity and prompt:
   > *"Compile the Boole Scaffold for Reading [XX] from `raw/[filename]`."*
3. Save output to `wiki/Book [N]/R[XX]_[Topic].md`
4. Update the Book's `_index.md` and `ops/04_LO_TRACKER.md`

### Quick Commands
| Command | Action |
|---------|--------|
| `"Compile the Boole Scaffold for [Topic]"` | Full scaffold output (Sections 1-4) |
| `"Generate a Twin-Question Drill for [Topic]"` | Combat simulation with REG vs ECO questions |
| `"Distractor Autopsy: [paste question]"` | Analyze wrong answer → identify trap archetype |
| `"Run a Sensitivity Drill on [Topic]"` | 3 directional scenarios (↑/↓ intuition test) |
| `"Constraint Layering Vignette on [Topic]"` | Heavy vignette with ≥2 conflicting constraints |
| `"Map the reading"` | Dependency & Noise Map only |
