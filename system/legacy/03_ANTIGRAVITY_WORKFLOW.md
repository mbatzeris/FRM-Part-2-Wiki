> **🗄️ ARCHIVED 2026-04-30.** Content frozen as of this date. The active pipeline lives in `../../.windsurf/workflows/new-reading.md` and `../../.windsurf/workflows/drill.md`. The active system prompt is `../system_prompt.md`. Some references below (e.g., to `pdftotext`) reflect the pre-Gemini extraction pipeline and are intentionally preserved for historical context — do not trust them as current documentation. For the live behavior of `/new-reading` and `/drill`, read the workflow files directly.

---

# FRM Part 2: The Antigravity + NotebookLM Study Workflow

> **⚠️ Status — conceptual design doc.** The active, executable implementation lives in:
> - `.windsurf/workflows/new-reading.md` — `/new-reading` (converts a chapter PDF into a Schema B markdown file; includes Step 9 boundary-events update and Step 10 `_LO_TRACKER.md` append)
> - `.windsurf/workflows/drill.md` — `/drill` (Phase 1/2/3 graduated difficulty, LO tracker updates, error archetype logging, event log integration)
>
> This file describes the *why* behind the workflow. The slash commands are *how* to execute it. If the two diverge, the slash-command files win — they are the enforced pipeline.

To conquer the FRM Part 2, passive reading and rote memorization are insufficient. You need an active, constraint-stress-testing environment. 

By combining **NotebookLM** with **Antigravity**, you create a hybrid learning engine: NotebookLM acts as your passive synthesizer and summarizer, while Antigravity acts as your active **Elite Tutor and CRO interrogator**.

## The Tech Stack Synergy

| Tool | Core Function in Your Study | Cognitive Mode |
| :--- | :--- | :--- |
| **NotebookLM** | Audio overviews, extracting key definitions, summarizing chapter narratives, finding specific text quickly. | **Passive / Ingestion** (Building the base knowledge) |
| **Antigravity** | Stress-testing constraints, generating twin-questions, simulating the "Distractor Engine", running ambiguity drills. | **Active / Falsification** (Building judgment and exam defense) |

---

## The 4-Step "Elite Tutor" Loop

Here is the most efficient, high-yield methodology you can run with me to rapidly accelerate your learning:

### Step 1: The NotebookLM Primer (15 mins)
Before you come to me, load your chapter PDF (e.g., Credit VaR) into NotebookLM. 
* Generate an audio overview to listen to while commuting or prepping.
* Ask NotebookLM to extract the 5 main formulas or definitions.
* **Goal:** You should walk away knowing *what* the concepts are.

### Step 2: The "Boole Extraction" via `/new-reading` (10 mins)
Run the `/new-reading` slash-command workflow on the chapter. This is the enforced pipeline — it handles extraction, proposition generation, §9 compliance checklist, boundary-event linkage, LO tracker append, event log row, and git commit in one sequence.
* **Your Prompt:** *"/new-reading R{N}"* (the workflow in `.windsurf/workflows/new-reading.md` takes it from there)
* **What the workflow does:** Runs `pdftotext` extraction, builds propositions (one per LO minimum), tags each as `[REG]` / `[ECO]` / `[OPS]` / `[THE]`, maps Signal/Noise, verifies the 16-item §9 checklist, updates `_boundary_events.md`, appends rows to `_LO_TRACKER.md` with baseline Readiness = 0.28, and logs a `READING` row to `_EVENT_LOG.md`.

### Step 3: The Graduated Drill via `/drill` (20 mins)
This is where the real learning happens. The `/drill` slash command automatically selects a Phase (1 Foundation, 2 Consolidation, or 3 Exam Simulation) based on the target LO's current Readiness score in `_LO_TRACKER.md`. Twin-Question combat is built into Phase 2 and Phase 3.
* **Your Prompt:** *"/drill"* (the workflow in `.windsurf/workflows/drill.md` checks for incomplete sessions, picks target LOs by priority, and runs a 5-question session)
* **What the workflow does:** Appends a `⚠️ In Progress` row to `_EVENT_LOG.md`, runs phase-appropriate questions, applies Distractor Autopsy labels (`[TRUE-IRRELEVANT]` / `[REG-ECO FLIP]` / `[INVERSE INTUITION]` / `[ABSOLUTE]`) on incorrect answers, updates `_LO_TRACKER.md` (Confidence first, then Readiness, then Priority per Leitner), logs errors to `_ERROR_ARCHETYPES.md`, closes out the event row, and commits.

### Step 4: The Distractor Autopsy (If you get a question wrong outside of `/drill`)
For ad-hoc GARP or Schweser practice questions outside a drill session, do not just check the answer key. 
* **Your Prompt:** *(Paste the question and your wrong answer)* *"Distractor Autopsy."*
* **What I will do:** I will run the question through the **Ambiguity Decoder** in `02_AMBIGUITY_DECODER.md`. I will tell you exactly which of the four archetypes you fell into and how to identify the linguistic cue you missed — then manually log the archetype to `_ERROR_ARCHETYPES.md`.

---

## Antigravity Quick-Commands to Use 

To speed up your workflow, use these standardized prompts whenever we open a new study session.

> **Compile a scaffold (full Boole output):**
> `Compile the Boole Scaffold for [Topic].`

> **Map a reading (Noise map only, faster):**
> `Initialize standard framework. Read [PDF NAME] and output the Dependency and Noise Map.`

> **Twin-Question combat drill:**
> `Generate a Twin-Question Drill for [Topic] based on the Ambiguity Roadmap.`

> **Test quantitative intuition without calculator (High Yield):**
> `Run a Qualitative Greeks/Sensitivity drill on [Topic]. Give me 3 scenarios where inputs change, and ask me for the directional impact.`

> **Pre-Exam drill (hardest):**
> `Give me a heavy 'Constraint Layering' vignette on [Topic]. Introduce at least two conflicting constraints (e.g. liquidity vs capital) and force me to pick the Best Fit.`

> **Distractor Autopsy (post-mistake):**
> `Distractor Autopsy: [paste the question + my wrong answer].`

---

## Why this is faster than traditional studying:
Before, you might spend 2 hours reading and 1 hour doing multiple choice. By forcing yourself into the **Distractor Autopsies** and **Twin-Question Drills**, you actively reverse-engineer the exam writers' minds. You learn to spot the "Red Herrings" instantly. This cuts down your time spent "staring at the page" during the exam and drastically reduces the anxiety of ambiguous choices.
