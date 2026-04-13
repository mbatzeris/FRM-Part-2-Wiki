# FRM Part 2 — LLM Wiki Master Map

Welcome to the root directory. This architecture turns passive study materials into an active, compiled knowledge base using a 4-layer design.

## 📁 Architecture

### `raw/` — Source Data (Immutable)
Raw readings provided by GARP/Schweser. **Do not edit files in this folder.**
- `FRM 2026 Part II Book 2.pdf`
- `CR-10 Credit VaR PDFs`
- `Exam Question Ambiguity Training Roadmap.txt`

### `system/` — AI Engine (Prompts & Templates)
Frameworks and instructions that Antigravity uses to process `raw/` files into `wiki/` output.
- `00_SYSTEM_PROMPT.md` — Core persona and constraint hierarchy
- `01_BOOLE_SCAFFOLD_TEMPLATE.md` — Scaffold output template (3 sections)
- `02_AMBIGUITY_DECODER.md` — Distractor archetypes taxonomy
- `03_ANTIGRAVITY_WORKFLOW.md` — Operational pipeline and study loop

### `wiki/` — Compiled Knowledge Base (Boole Scaffolds by Book)
Your actual study environment. Contains per-chapter scaffolds organized by GARP Book.
- `Book 1 - Market Risk/` — 20% exam weight
- `Book 2 - Credit Risk/` — 20% exam weight
- `Book 3 - Operational Risk/` — 20% exam weight
- `Book 4 - Liquidity Risk/` — 15% exam weight
- `Book 5 - Investment Risk/` — 15% exam weight

Each Book folder has an `_index.md` tracking progress across readings.

### `ops/` — Operational Tools (Tracking, Drills, Schedule)
Cross-cutting tools that span all domains.
- `04_LO_TRACKER.md` — Executive dashboard for Learning Objectives
- `05_FORMULA_ENGINE.md` — Directional math reference by domain
- `06_DRILL_BANK.md` — 45 tagged combat simulation questions
- `07_ERROR_LOG.md` — Mistake tracking with distractor archetype analysis
- `08_STUDY_CALENDAR.md` — 16-week study schedule with spaced repetition
- `09_BOUNDARY_EVENTS.md` — Cross-domain drill templates
- `../wiki/_boundary_events.md` — Structural cross-domain linkage map (Ref Class)

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
