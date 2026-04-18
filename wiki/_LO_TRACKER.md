# Learning Objective Tracker

**Purpose:** Single source of truth for your mastery across every FRM Part 2 LO. This file **is** your spaced-repetition system — no external tool needed.

**How to use:**
1. Open this file every **Sunday** during your weekly review.
2. Sort by `Next Review` date — drill the LOs at the top.
3. After each drill session, update `Last Reviewed`, `Confidence`, `Q Attempts / Correct`, and re-compute `Readiness`.
4. Advance `Next Review` via the Leitner schedule (see below).

---

## Readiness Formula

```
LO_Readiness = 0.60 × (accuracy on last 5 questions)
             + 0.30 × (self-confidence / 5)
             + 0.10 × (recency factor)

where recency_factor = max(0, 1 − days_since_review / 30)
```

**Status legend:**
- 🔴 **Red** — Readiness < 0.50 · drill this week
- 🟡 **Amber** — 0.50 ≤ Readiness < 0.75 · active rotation
- 🟢 **Green** — Readiness ≥ 0.75 · monthly review only
- ⭐ **Graduated** — 2 consecutive ≥ 80% reviews at Green · quarterly touch

## Leitner Review Schedule

| Current Box | Next Review After |
|:--|:--|
| New LO (never drilled) | +3 days |
| Last session < 60% | +3 days (repeat box) |
| Last session 60–79% | +7 days |
| Last session 80–100% (first time) | +14 days |
| Last session 80–100% (second time) | +30 days (→ Green) |
| Green, ≥80% | +60 days (→ ⭐) |
| Any drop below 60% | reset to 3 days (→ 🔴) |

---

## Aggregate Snapshot

| Metric | Value |
|:--|:--:|
| LOs tracked | 7 |
| 🔴 Red | 0 |
| 🟡 Amber | 7 |
| 🟢 Green | 0 |
| ⭐ Graduated | 0 |
| **Overall readiness** | **~0.45** (baseline, pre-calibration) |
| Target (week 28) | **≥ 0.75** |

*Auto-recompute after each weekly log entry.*

---

## LO Table

**Columns:** LO ID · Reading · Topic · First Studied · Last Reviewed · Confidence (0-5) · Qs Correct/Attempted · Accuracy · Readiness · Next Review · Status

### Book 2 — Credit Risk (20% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Next Rev | Status |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 30.a | R30 | ISDA event of default & unsecured creditor situations (P3) | 2026-04-18 | 2026-04-18 | 3 | 0/0 | — | 0.45 | 2026-04-21 | 🟡 |
| 30.b | R30 | CVA & DVA; wrong-way / right-way risk (P4) | 2026-04-18 | 2026-04-18 | 3 | 0/0 | — | 0.45 | 2026-04-21 | 🟡 |
| 30.c | R30 | PD from credit spreads; risk-neutral vs real-world PD (P1, P2) | 2026-04-18 | 2026-04-18 | 4 | 0/0 | — | 0.51 | 2026-04-21 | 🟡 |
| 30.d | R30 | Credit risk mitigants: netting, collateral, downgrade triggers (P5) | 2026-04-18 | 2026-04-18 | 3 | 0/0 | — | 0.45 | 2026-04-21 | 🟡 |
| 30.e | R30 | Default correlation: reduced-form vs structural models (P6) | 2026-04-18 | 2026-04-18 | 3 | 0/0 | — | 0.45 | 2026-04-21 | 🟡 |
| 30.f | R30 | Gaussian copula for time-to-default; one-factor model (P7) | 2026-04-18 | 2026-04-18 | 2 | 0/0 | — | 0.39 | 2026-04-21 | 🟡 |
| 30.g | R30 | Credit VaR via Gaussian copula; CreditMetrics (P8) | 2026-04-18 | 2026-04-18 | 2 | 0/0 | — | 0.39 | 2026-04-21 | 🟡 |

### Book 1 — Market Risk (20% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Next Rev | Status |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _To be populated as Book 1 readings are re-converted via /new-reading_ | | | | | | | | | | |

### Book 3 — Operational Risk (20% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Next Rev | Status |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _Pending_ | | | | | | | | | | |

### Book 4 — Liquidity Risk (15% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Next Rev | Status |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _Pending_ | | | | | | | | | | |

### Book 5 — Investment Risk + Current Issues (25% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Next Rev | Status |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _Pending_ | | | | | | | | | | |

---

## First-Week Calibration (ACTION REQUIRED)

Your Week 1 task (Sunday 20 April or sooner): open the R30 Schweser Module Quiz, do all 7 questions, log results here per LO. Replace the placeholder `0/0` with real `correct/attempted`. Re-compute each Readiness cell via the formula. That becomes your real baseline.

## Process Per Drill Session (the "guaranteed-success" loop)

1. **Pick top 3 LOs** by urgency from `Next Rev` column.
2. **Read the proposition** in the linked Schema B file (5 min each).
3. **Answer 3 questions** (AnalystPrep filtered to that LO, or Schweser Module Quiz).
4. **For each wrong answer:** log the archetype in `_ERROR_ARCHETYPES.md`.
5. **Update this file's row** for the LO: `Last Reviewed = today`, `Confidence`, `Q C/A`, `Accuracy`, new `Readiness`, new `Next Rev` per Leitner.
6. **Add to _ANKI-style self-quiz** in §5 of the Schema B file if a new trap is discovered.
7. **Close session** — 5 min passive: NotebookLM audio on today's LOs for tomorrow's commute.

## Dashboard Link

See `@c:\Users\user\Documents\FRM 2\wiki\_READINESS_DASHBOARD.md` for the rolled-up exam-readiness score updated from this tracker.
