# FRM Part 2 — Study Calendar & Spaced Repetition

> **Instructions:** Fill in your exam date below. The calendar auto-structures your study into 3 phases. Update the checkboxes as you complete each block. Move topics you get wrong to the "Review Queue" — they cycle back faster.

---

## Configuration

| Field | Value |
|-------|-------|
| **Exam Date** | `November 17, 2026` |
| **Study Start Date** | `April 13, 2026` |
| **Total Days Available** | `217 days` |
| **Daily Study Hours** | `2 hours` |

---

## Phase Structure

| Phase | When | Focus | Method |
|-------|------|-------|--------|
| **Phase 1: Build** | Days 1 → 50% mark | Content ingestion + Boole Extraction | NotebookLM + Antigravity Step 1-2 |
| **Phase 2: Drill** | 50% → 25% mark | Twin-Questions + Practice Questions | Antigravity Step 3 + Drill Bank |
| **Phase 3: Combat** | Final 25% | Timed mocks + Distractor Autopsies | Full mock exams + Error Log review |

---

## Phase 1: Build (Content Coverage)

Study domains in order of weight × difficulty. Suggested sequence:

| Week | Domain | Weight | Daily Tasks | Status |
|------|--------|--------|-------------|--------|
| 1 | Credit Risk | 20% | Read chapters → NotebookLM primer → Boole Extraction | `[✓]` |
| 2 | Market Risk | 20% | Read chapters → NotebookLM primer → Boole Extraction | `[✓]` |
| 3 | Operational Risk | 20% | Read chapters → NotebookLM primer → Boole Extraction | `[✓]` |
| 4 | Liquidity & Treasury | 15% | Read chapters → NotebookLM primer → Boole Extraction | `[✓]` |
| 5 | Investment Mgmt | 15% | Read chapters → NotebookLM primer → Boole Extraction | `[✓]` |
| 6 | Current Issues | 10% | Read assigned papers → summarize implications | `[✓]` |

> After each week, update `04_LO_TRACKER.md` — all LOs in that domain should be at least `[~]`.

---

## Phase 2: Drill (Active Testing)

| Week | Activity | Target | Status |
|------|----------|--------|--------|
| 7 | Credit Risk: Twin-Questions + Drill Bank Q11-Q20 | ≥ 70% accuracy | `[ ]` |
| 8 | Market Risk: Twin-Questions + Drill Bank Q1-Q10 | ≥ 70% accuracy | `[ ]` |
| 9 | OpRisk + Liquidity: Drill Bank Q21-Q30 | ≥ 70% accuracy | `[ ]` |
| 10 | InvMgmt + Current Issues: Drill Bank Q31-Q40 | ≥ 70% accuracy | `[ ]` |
| 11 | Boundary Events: Drill Bank Q41-Q45 + Sensitivity Drills | Build cross-domain intuition | `[ ]` |
| 12 | Weakest 2 domains (from Error Log): intensive review | Close gaps | `[ ]` |

> After each week, update `04_LO_TRACKER.md` — drilled topics should move to `[✓]`.

---

## Phase 3: Combat (Timed Mocks)

| Week | Activity | Target | Status |
|------|----------|--------|--------|
| 13 | Full Mock Exam #1 (GARP Practice) — 4 hours, 80 questions | Score ≥ 60% | `[ ]` |
| — | Distractor Autopsy on ALL wrong answers → update Error Log | Identify patterns | `[ ]` |
| 14 | Full Mock Exam #2 (Schweser/AnalystPrep) — timed | Score ≥ 65% | `[ ]` |
| — | Review Error Log patterns → targeted re-drill | Break recurring traps | `[ ]` |
| 15 | Full Mock Exam #3 + Formula Engine speed drill | Score ≥ 70% | `[ ]` |
| 16 | **Exam Week**: Light review of Error Log + Directional Intuition Drill only | Confidence, not cramming | `[ ]` |

> After mocks, update `04_LO_TRACKER.md` — successfully answered topics move to `[★]`.

---

## Spaced Repetition: Review Queue (Leitner System)

Topics you get wrong cycle back on an accelerating schedule:

| Box | Review Interval | Rule |
|-----|----------------|------|
| **Box 1** (New/Wrong) | Every day | Topic enters here when you get it wrong |
| **Box 2** | Every 3 days | Moves here after 1 correct answer from Box 1 |
| **Box 3** | Every 7 days | Moves here after 1 correct answer from Box 2 |
| **Box 4** | Every 14 days | Moves here after 1 correct answer from Box 3 |
| **Mastered** | Before exam only | Moves here after correct answer from Box 4 |

> **If you get a topic wrong at any box → it drops back to Box 1.**

### Active Review Queue

| Topic | Current Box | Last Reviewed | Next Review |
|-------|------------|--------------|-------------|
| *(empty — add topics as you miss them)* | | | |

---

## Weekly Sunday Checklist

- [ ] Update all LO statuses in `04_LO_TRACKER.md`
- [ ] Recalculate domain readiness scores
- [ ] Review `07_ERROR_LOG.md` — identify top 2 recurring archetypes
- [ ] Move Review Queue topics between boxes
- [ ] Adjust next week's plan based on weakest areas
- [ ] Verify you're on track with the phase schedule
