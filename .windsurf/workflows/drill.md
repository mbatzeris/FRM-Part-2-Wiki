---
description: Run a structured FRM Part 2 drill session using the Antigravity graduated-difficulty framework
---

# /drill — FRM Part 2 Drill Session Protocol

Use this workflow every time you run a drill session. The format escalates automatically through three phases based on the target LO's current Readiness score in `_LO_TRACKER.md`.

---

## Pre-Session Setup

### Step 1 — Check `_EVENT_LOG.md` for incomplete sessions
Open `wiki/_EVENT_LOG.md` and read the last row.
- If Status = `⚠️ In Progress`: tell the user — *"Incomplete session found: [Subject] from [Date]. Resume or start fresh?"* Wait for response before proceeding.
- If Status = `✅ Complete` or log is empty: proceed normally.

### Step 2 — Read the LO tracker
Open `wiki/_LO_TRACKER.md`. Identify:
- Target reading(s) and LO(s) for this session (🔴 High priority first, then 🟡 Medium)
- Current Readiness score for each target LO
- Determine the Phase for each LO (see table below)

### Step 3 — Load source material
Open the target Schema B file(s). The question bank draws from:
- **§3 Noise** bullets → red-herring ingredients for vignettes
- **§4 Directional Intuition** → Phase 1 directional questions
- **§5 Ambiguity Traps** → Phase 2–3 distractor material
- **§2 Constraint Stress-Test** → Phase 1 calculation anchors

### Step 4 — Open the event log row and state the session
Append a new row to `wiki/_EVENT_LOG.md` **before asking the first question**:
```
| {next #} | {YYYY-MM-DD} | DRILL | Session {N} · R{X} · Phase {P} | LOs: {list} — in progress | ⚠️ In Progress |
```
Then open with: *"Session [X] · R{N} · Phase {1/2/3} · Target LOs: {list}"*

Session number = last `DRILL` event # in the log + 1 (count only DRILL rows).

---

## Phase Determination

| Phase | Trigger | Core Goal |
|:---|:---|:---|
| **Phase 1 — Foundation** | First drill on LO **OR** Readiness < 0.50 | Verify mechanical competence |
| **Phase 2 — Consolidation** | 0.50 ≤ Readiness < 0.70 | Introduce exam-format friction |
| **Phase 3 — Exam Simulation** | Readiness ≥ 0.70 | Full Antigravity exam replication |

**Discipline rule:** Maximum ONE Phase 1 session per LO cluster. If the user gets the core mechanic correct twice in Phase 1, advance to Phase 2 within the same session — do not wait for the next session.

> **Priority vs Phase:** Priority (🔴/🟡/🟢 in `_LO_TRACKER.md`) determines **when** to drill next — set by last-session accuracy. Phase (1/2/3) determines **how** to drill — set by current Readiness score. A 🔴 High priority LO with Readiness 0.55 correctly triggers Phase 2, not Phase 1.

---

## Phase 1 — Foundation

**Conditions:** First drill on a new LO or Readiness < 0.50.

**Question mix (5 questions):**
- Q1–Q2: Core formula or calculation — clean stem, no noise, exact numerical answer
- Q3: Directional intuition — "If X increases, what happens to Y?" (↑/↓/unchanged)
- Q4: Reverse-engineer — given an output, solve for a missing input
- Q5: Contrast pair — "What is the difference between A and B?" (targets A2 Swapped Definitions archetype)

**Feedback rules:**
- Correct/Incorrect verdict + explanation
- If wrong: explain root cause and provide the corrected working
- Distractor archetype labels: NOT required in Phase 1 (focus is on getting the right answer, not meta-analysis)

---

## Phase 2 — Consolidation

**Conditions:** 0.50 ≤ Readiness < 0.70.

**Question mix (5 questions):**
- Q1: Warm-up calculation (confidence anchor — clean, Phase 1 style)
- Q2–Q3: MCQ with one red-herring data point embedded in the stem. The question must be answerable without the irrelevant data. Teach the "Surgical Skim" — read the question last sentence first.
- Q4: Distractor Autopsy — present a plausible wrong answer and ask "why is this wrong?" (no calculation required; pure reasoning)
- Q5: First Twin Question — same scenario, one perspective: either "From a regulatory (Basel) perspective..." or "From an internal risk/economic capital perspective..."

**Feedback rules:**
- Distractor archetype label required on Q2–Q5 when user answers incorrectly: `[TRUE-IRRELEVANT]` / `[REG-ECO FLIP]` / `[INVERSE INTUITION]` / `[ABSOLUTE]`
- If wrong: full Distractor Autopsy — identify which linguistic or structural cue in the stem was missed

---

## Phase 3 — Exam Simulation

**Conditions:** Readiness ≥ 0.70.

**Question mix (5 questions):**
- Q1: Noisy vignette — 3–5 sentence narrative with ≥2 irrelevant data points; single focused question. Label which data was noise in the feedback.
- Q2: Twin Question pair — Q2a (REG perspective) + Q2b (ECO perspective) on the same vignette. Both answers required before feedback is given.
- Q3: Constraint-layered Best Fit — competing business/regulatory constraints; "most appropriate" or "most likely" format; all four options are plausible.
- Q4: Boundary Event — cross-reading scenario drawn from `wiki/_boundary_events.md`. Requires applying concepts from two different readings simultaneously.
- Q5: Synthesis — combines two LOs from the same reading in one vignette; tests whether the user can identify which LO each question element belongs to.

**Feedback rules:**
- Distractor archetype label required on ALL feedback, correct or incorrect
- For wrong answers: full Distractor Autopsy + identify the constraint hierarchy applied
- For correct answers: confirm which constraint (REG/APP/ECO/THE) drove the correct selection

---

## Post-Session Close-Out

### Step 5 — Update `_LO_TRACKER.md`
For each drilled LO, update:
- Q C/A (add session results)
- Acc (recalculate cumulative)
- Readiness (recalculate using full formula):
  ```
  Readiness = 0.60 × Acc + 0.30 × (Conf/5) + 0.10 × recency_factor
  where recency_factor = max(0, 1 − days_since_review / 30)
  Note: immediately post-session recency_factor = 1.0, so formula simplifies to:
  Readiness = 0.60 × Acc + 0.30 × (Conf/5) + 0.10
  ```
- Priority (re-evaluate using accuracy-based Leitner thresholds):
  - 🔴 High — last session accuracy < 60%, OR new LO with 0 questions
  - 🟡 Medium — 60–79%, OR first session ≥ 80%
  - 🟢 Low — second consecutive session ≥ 80%
- Last Rev (today's date)

After updating individual LO rows, also update the **Aggregate Snapshot** at the top of `_LO_TRACKER.md`:
- Increment LOs tracked (if new LOs added)
- Recount 🔴 High / 🟡 Medium / 🟢 Low by Priority column
- Recompute Avg LO Readiness = sum of all Readiness values / total LOs

### Step 6 — Update `_ERROR_ARCHETYPES.md`
For each error made:
- Increment the archetype count in the summary table
- Add an instance log entry: date · LO · question summary · user answer → correct answer · archetype · lesson

### Step 7 — Update event log, commit and push
Update the open session row in `wiki/_EVENT_LOG.md`:
- Change Status from `⚠️ In Progress` → `✅ Complete`
- Update Detail to include final error count: `LOs: {list} · {n} errors ({archetypes})`

```powershell
git add "wiki/_LO_TRACKER.md" "wiki/_ERROR_ARCHETYPES.md" "wiki/_EVENT_LOG.md"
git commit -m "[DRILL] Session {N}: R{X} LOs {list}; Phase {P}; {n} errors"
git push
```

> **Commit format:** `[TYPE] Description` where TYPE = `DRILL` / `READING` / `SYSTEM` / `REVIEW` / `FIX`

---

## Distractor Archetype Reference (for feedback labels)

| Tag | What it means | Exam tell |
|:---|:---|:---|
| `[TRUE-IRRELEVANT]` | Statement is factually correct but answers the wrong question | "That's true, but the question asked about X, not Y" |
| `[REG-ECO FLIP]` | Correct under the wrong framework (regulatory vs economic) | Missed a stem cue: "from a prudential perspective" / "to maximise shareholder value" |
| `[INVERSE INTUITION]` | Direction of relationship is counter-intuitive | Sign flip; non-linear relationship; correlation that inverts at extremes |
| `[ABSOLUTE]` | Used "always" / "never" / "eliminates" in risk management | Risk management rarely has absolutes; these are usually wrong |

---

## Constraint Hierarchy Reference (for Phase 3 feedback)

Apply in order when evaluating answer correctness:
1. **[REG]** Regulatory mandates (Basel/FRTB/Supervisory) — always overrides theory
2. **[APP]** Vignette constraints (Risk Appetite / specific stem cues) — overrides general best practice
3. **[ECO]** First-order economic logic — applies when no regulatory or vignette constraint is active
4. **[THE]** Theoretical purity — only if the question explicitly asks for it
