# System Architecture & Documentation

This directory contains the **AI Engine** of the FRM Wiki. It houses the 4 core instruction frameworks that dictate how the Assistant (Antigravity) processes raw readings, synthesizes knowledge, and conducts combat drills. 

**DO NOT store study material in this folder.** This folder is strictly for system logic and prompt templates.

---

## 1. `00_SYSTEM_PROMPT.md`
**Role:** The Core Persona & Operating System
**Purpose:** This file defines the *behavior* of the AI. It establishes the "Antigravity" persona—an elite, aggressive FRM tutor focused on falsification and structural dominance rather than passive summarization. 
**Key Mechanisms:**
- Enforces two parallel taxonomies: the **Constraint Hierarchy** `[REG] > [APP] > [ECO] > [THE]` (which tag wins in a vignette) and the **Proposition Tags** `[REG] | [ECO] | [OPS] | [THE]` (how each axiom is classified).
- Sets strict constraints prohibiting fluff, generic advice, and non-exam-tested material.
- Defines the conversational tone (blunt, surgical, Socratic).

## 2. `01_BOOLE_SCAFFOLD_TEMPLATE.md`
**Role:** Pointer to the active Schema B template
**Status:** This file is now a **pointer**. The active, canonical Schema B template lives at `wiki/_TEMPLATE_Reading.md` and is the single source of truth for `/new-reading` conversions. The legacy 5-section version was retired to eliminate split-brain drift between two templates.
**Key mechanisms (defined in the wiki template):**
- **§1 Foundational Propositions** — one proposition per LO (minimum), tagged by `[REG]`, `[ECO]`, `[OPS]`, `[THE]`, with Trigger Phrases.
- **§2 Constraint Stress-Test** — falsification table showing what flips the answer.
- **§3 Dependency & Noise Map** — Signal / Noise / Tensions triage.
- **§4 Directional Intuition** — qualitative ↑/↓ chains.
- **§5 Ambiguity Traps** — distinctions GARP blurs; scope flips; historical-intuition failures.
- **§9 Compliance Checklist** — 16-item gate enforced by `/new-reading` Step 8.

## 3. `02_AMBIGUITY_DECODER.md`
**Role:** The Threat Intelligence & Question Analysis Engine
**Purpose:** This file teaches the AI how GARP weaponizes the English language. It is used during the "Drill" phase or when conducting a "Distractor Autopsy" on a question the candidate answered incorrectly.
**Key Mechanisms:**
- Categorizes traps into four distractor archetypes used throughout the drill bank and autopsy logs: `[TRUE-IRRELEVANT]` (factually right, wrong question), `[REG-ECO FLIP]` (correct under wrong framework), `[INVERSE INTUITION]` (direction reverses — e.g., DVA↑ = P&L↑ but credit health↓), and `[ABSOLUTE]` ("always/never/eliminates").
- Provides linguistic & directional cues ("Most/Least Likely", "From a ___ perspective"), a Twin-Question Drill generator, and a Regulatory Maturity Flag (Explicit / Principle-based / Emerging).
- Used to tear down answer choices by identifying the exact linguistic hinge that makes a distractor false.

## 4. `03_ANTIGRAVITY_WORKFLOW.md`
**Role:** The Operational Pipeline
**Purpose:** This document maps out the study loop. It dictates how the system moves a candidate from passive reading to active combat.
**Key Mechanisms — the 4-Step Elite Tutor Loop** (now implemented as slash commands; see `.windsurf/workflows/`):
- **Step 1 (NotebookLM Primer, 15 min):** Load the chapter PDF into NotebookLM for audio overview and baseline definitions before combat. (Manual step.)
- **Step 2 (Boole Extraction via `/new-reading`, 10 min):** Run the `/new-reading` workflow on the chapter. Handles proposition extraction, §9 checklist, `_boundary_events.md` update, `_LO_TRACKER.md` append (Readiness = 0.28 baseline), and event-log row in one pipeline.
- **Step 3 (Graduated Drill via `/drill`, 20 min):** Run the `/drill` workflow. Automatically selects Phase 1/2/3 by target LO Readiness; Twin-Question combat lives in Phase 2–3.
- **Step 4 (Distractor Autopsy, as needed):** For ad-hoc GARP/Schweser practice questions outside a drill, route the question through the Ambiguity Decoder (`02_AMBIGUITY_DECODER.md`) to name the trap and log it in `wiki/_ERROR_ARCHETYPES.md` manually.

---

## How They Work Together

When you start a new study session, the AI effectively "loads" these 4 files into its context. 
1. The **Workflow (`03`)** tells it *what step* of the study journey you are on.
2. The **System Prompt (`00`)** tells it *how to act* and speak.
3. If you ask it to summarize a reading, it fetches the **Scaffold Template (`01`)**.
4. If you ask it to analyze a practice question, it fires up the **Ambiguity Decoder (`02`)**.

---

## Operational Workflows (in `.windsurf/workflows/`)

These are the active slash-command workflows that implement the above system in practice:

| Workflow | Command | Purpose |
|:--|:--|:--|
| **new-reading.md** | `/new-reading` | Convert a Schweser chapter into a Schema B `.md` file; includes Step 9 to update `wiki/_boundary_events.md` |
| **drill.md** | `/drill` | Run a drill session using the 3-phase graduated difficulty framework (Phase 1 Foundation → Phase 2 Consolidation → Phase 3 Exam Simulation) |

## Supporting Wiki Files

| File | Purpose |
|:--|:--|
| `wiki/_boundary_events.md` | Cross-domain linkage index: maps concepts shared across readings and logs multi-risk boundary event chains (updated by Step 9 of `/new-reading`) |
| `wiki/_ERROR_ARCHETYPES.md` | Personal distractor decoder: logs every error by archetype (A1–A12) with instance-level entries and lessons |
| `wiki/_EVENT_LOG.md` | Append-only event log: records all READING, DRILL, SYSTEM, and REVIEW events with resume-detection for incomplete sessions |
| `wiki/_LO_TRACKER.md` | Master readiness tracker: drives phase selection in `/drill` and priority in weekly planning |
