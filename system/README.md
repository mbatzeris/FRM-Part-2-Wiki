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
**Role:** The Knowledge Extraction Compiler
**Purpose:** This is the universal blueprint for how all `raw/` PDFs are transformed into `wiki/` study notes. It forces the AI to output knowledge in a highly specific, standardized format.
**Key Mechanisms:**
- **Section 1:** Tabular Foundational Propositions (tagged by `[REG]`, `[ECO]`, `[OPS]`, `[THE]`).
- **Section 2:** Constraint Stress-Tests (Falsification) that flip variables to see how outcomes change.
- **Section 3:** Dependency & Noise Maps (separating actual exam signals from distractor noise).
- **Section 4:** Directional Intuition for key formulas (focusing on X ↑ → Y ↓ rather than raw math).
- **Section 5:** Ambiguity Traps (Anti-Decoder) — distinctions GARP loves to blur (e.g., "Insolvency ≠ Default"), scope flips, and historical-intuition failures.

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
**Key Mechanisms — the 4-Step Elite Tutor Loop:**
- **Step 1 (NotebookLM Primer, 15 min):** Load the chapter PDF into NotebookLM for audio overview and baseline definitions before combat.
- **Step 2 (Boole Extraction via Antigravity, 10 min):** Run the Boole Scaffold on the PDF; tag every concept and map Signal/Noise. Save output to `wiki/`.
- **Step 3 (Twin-Question Combat, 20 min):** Attempt dense vignettes under REG then ECO framing; apply the Strict Output Template.
- **Step 4 (Distractor Autopsy, as needed):** Paste any wrongly-answered GARP/Schweser question; route it through the Ambiguity Decoder to name the trap and log it in `wiki/_ERROR_ARCHETYPES.md`.

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
| **new-reading.md** | `/new-reading` | Convert a Schweser chapter into a Schema B `.md` file; includes Step 8b to update `wiki/_boundary_events.md` |
| **drill.md** | `/drill` | Run a drill session using the 3-phase graduated difficulty framework (Phase 1 Foundation → Phase 2 Consolidation → Phase 3 Exam Simulation) |

## Supporting Wiki Files

| File | Purpose |
|:--|:--|
| `wiki/_boundary_events.md` | Cross-domain linkage index: maps concepts shared across readings and logs multi-risk boundary event chains (updated by Step 8b of `/new-reading`) |
| `wiki/_ERROR_ARCHETYPES.md` | Personal distractor decoder: logs every error by archetype (A1–A12) with instance-level entries and lessons |
| `wiki/_LO_TRACKER.md` | Master readiness tracker: drives phase selection in `/drill` and priority in weekly planning |
