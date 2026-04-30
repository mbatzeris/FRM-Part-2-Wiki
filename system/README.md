# System Architecture & Documentation

This directory houses the **AI Engine** of the FRM Wiki — the instruction frameworks that dictate how the Assistant processes raw readings, synthesizes knowledge, and conducts combat drills.

**DO NOT store study material in this folder.** This folder is strictly for system logic and prompt templates.

As of 2026-04-30 the system docs have been consolidated: the former 4-file structure (`00_SYSTEM_PROMPT`, `01_BOOLE_SCAFFOLD_TEMPLATE`, `02_AMBIGUITY_DECODER`, `03_ANTIGRAVITY_WORKFLOW`) collapsed into a single live prompt (`system_prompt.md`) plus a pointer (`01_BOOLE_SCAFFOLD_TEMPLATE.md`). The conceptual workflow narrative lives in `legacy/` for historical reference only.

---

## Active files

### `system_prompt.md`
**Role:** The single live system prompt — persona, constraints, taxonomy, distractor archetypes, linguistic cues, twin-question drill, regulatory maturity flag, and strict output template.
**Loaded by:** external LLM sessions when the user wants Antigravity-style tutoring outside Cascade workflows.
**Key mechanisms:**
- **Two parallel taxonomies** — the **Constraint Hierarchy** `[REG] > [STEM] > [ECO] > [THE]` (which tag wins in a vignette) and the **Proposition Tags** `[REG] | [ECO] | [OPS] | [THE]` (how each axiom is classified). `[STEM]` exists **only** in the Constraint Hierarchy — never use it as a proposition tag in Schema B files.
- **Four distractor archetypes** used in drill feedback: `[TRUE-IRRELEVANT]` · `[REG-ECO FLIP]` · `[INVERSE INTUITION]` · `[ABSOLUTE]`.
- **Regulatory maturity flag** triaging questions into `[EXPLICIT RULE]` · `[PRINCIPLE-BASED]` · `[EMERGING]`.

### `01_BOOLE_SCAFFOLD_TEMPLATE.md`
**Role:** Pointer to the active Schema B template at `wiki/_TEMPLATE_Reading.md`.
**Status:** Kept only so that any outdated reference to `01_BOOLE_SCAFFOLD_TEMPLATE.md` from external tools still resolves to the canonical location. The legacy multi-section template was retired to eliminate split-brain drift.

---

## Legacy (historical reference only — do not trust as current docs)

### `legacy/03_ANTIGRAVITY_WORKFLOW.md`
**Role:** The original 4-step "Elite Tutor" loop design document (NotebookLM primer → Boole extraction → graduated drill → distractor autopsy).
**Status:** Frozen 2026-04-30. References the old `pdftotext` extraction pipeline and other pre-Gemini terminology; intentionally not corrected because the active pipeline is now canonical in `.windsurf/workflows/`.

---

## Where the live system actually runs

| Layer | File | What it does |
|:--|:--|:--|
| **Persona + rules** | `system/system_prompt.md` | Loaded into external LLM sessions |
| **Schema B template** | `wiki/_TEMPLATE_Reading.md` | Shape of every reading file |
| **Reading pipeline** | `.windsurf/workflows/new-reading.md` | `/new-reading` slash command |
| **Drill pipeline** | `.windsurf/workflows/drill.md` | `/drill` slash command |
| **Extraction script** | `scripts/extract_via_gemini.py` | PDF → Gemini → raw markdown |
| **Formula linter** | `scripts/verify_formulas.py` | Checks §1 formulas appear in raw extract |

## Supporting wiki files

| File | Purpose |
|:--|:--|
| `wiki/_boundary_events.md` | Cross-domain linkage index (Step 8 of `/new-reading`) |
| `wiki/_ERROR_ARCHETYPES.md` | Personal distractor decoder: A1–A12 archetypes + instance log |
| `wiki/_EVENT_LOG.md` | Append-only event log (all READING / DRILL / SYSTEM / REVIEW / FIX events) |
| `wiki/_LO_TRACKER.md` | Master readiness tracker; drives phase selection in `/drill` |
| `wiki/_READINESS_DASHBOARD.md` | Rolled-up exam-readiness score |
| `wiki/_WEEKLY_LOG.md` | Sunday check-in template |
