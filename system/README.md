# System Architecture & Documentation

This directory contains the **AI Engine** of the FRM Wiki. It houses the 4 core instruction frameworks that dictate how the Assistant (Antigravity) processes raw readings, synthesizes knowledge, and conducts combat drills. 

**DO NOT store study material in this folder.** This folder is strictly for system logic and prompt templates.

---

## 1. `00_SYSTEM_PROMPT.md`
**Role:** The Core Persona & Operating System
**Purpose:** This file defines the *behavior* of the AI. It establishes the "Antigravity" persona—an elite, aggressive FRM tutor focused on falsification and structural dominance rather than passive summarization. 
**Key Mechanisms:**
- Enforces the `[REG]` (Regulatory/Basel) vs `[ECO]` (Economic/Market Reality) classification system.
- Sets strict constraints prohibiting fluff, generic advice, and non-exam-tested material.
- Defines the conversational tone (blunt, surgical, Socratic).

## 2. `01_BOOLE_SCAFFOLD_TEMPLATE.md`
**Role:** The Knowledge Extraction Compiler
**Purpose:** This is the universal blueprint for how all `raw/` PDFs are transformed into `wiki/` study notes. It forces the AI to output knowledge in a highly specific, standardized format.
**Key Mechanisms:**
- **Section 1:** Tabular Foundational Propositions (tagged by `[THE]`, `[OPS]`, `[REG]`, `[ECO]`).
- **Section 2:** Constraint Stress-Tests (Falsification) that flip variables to see how outcomes change.
- **Section 3:** Dependency & Noise Maps (separating actual exam signals from distractor noise).
- **Section 4:** Directional Intuition for key formulas (focusing on $X \uparrow \rightarrow Y \downarrow$ rather than raw math).

## 3. `02_AMBIGUITY_DECODER.md`
**Role:** The Threat Intelligence & Question Analysis Engine
**Purpose:** This file teaches the AI how GARP weaponizes the English language. It is used during the "Drill" phase or when conducting a "Distractor Autopsy" on a question the candidate answered incorrectly.
**Key Mechanisms:**
- Categorizes traps into specific recognized archetypes: *The False Equivalency*, *The Chronology Trap*, *The Phantom Nuance*, and *The Regulatory Fiction*.
- Provides a protocol for tearing down answer choices by identifying the exact linguistic hinge that makes a distractor false.

## 4. `03_ANTIGRAVITY_WORKFLOW.md`
**Role:** The Operational Pipeline
**Purpose:** This document maps out the study loop. It dictates how the system moves a candidate from passive reading to active combat.
**Key Mechanisms:**
- **Phase 1 (Ingest):** Pull PDF → Run `01_BOOLE_SCAFFOLD_TEMPLATE` → Save to `wiki/`.
- **Phase 2 (Drill):** Use `00_SYSTEM_PROMPT` to generate Twin-Question or Sensitivity drills.
- **Phase 3 (Autopsy):** Use `02_AMBIGUITY_DECODER` to log mistakes into the `ops/07_ERROR_LOG.md`.
- **Phase 4 (Review):** Use `ops/04_LO_TRACKER.md` to track progress.

---

## How They Work Together

When you start a new study session, the AI effectively "loads" these 4 files into its context. 
1. The **Workflow (`03`)** tells it *what step* of the study journey you are on.
2. The **System Prompt (`00`)** tells it *how to act* and speak.
3. If you ask it to summarize a reading, it fetches the **Scaffold Template (`01`)**.
4. If you ask it to analyze a practice question, it fires up the **Ambiguity Decoder (`02`)**.
