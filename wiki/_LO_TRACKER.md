# Learning Objective Tracker

**Purpose:** Single source of truth for your mastery across every FRM Part 2 LO. This file **is** your spaced-repetition system — no external tool needed.

**How to use:**
1. When you have a study session, open this file.
2. Filter or sort for `🔴 High` priority LOs — these are your focus.
3. After each drill session, update `Last Reviewed`, `Confidence`, `Q Attempts / Correct`, and re-compute `Readiness`.
4. Update the `Priority` for the LOs you drilled using the Priority Engine logic below.

---

## Readiness Formula

```
LO_Readiness = 0.60 × (accuracy on last 5 questions)
             + 0.30 × (self-confidence / 5)
             + 0.10 × (recency factor)

where recency_factor = max(0, 1 − days_since_review / 30)
```

## Priority Engine (Leitner Logic)

| Last Session Accuracy | New Priority | Description |
|:--|:--|:--|
| < 60% | 🔴 **High** | Immediate attention needed. Drill again within 1-3 days. |
| 60% – 79% | 🟡 **Medium** | Good grasp, but needs reinforcement. Drill again within 1 week. |
| ≥ 80% (1st time) | 🟡 **Medium** | Strong performance. Spaced repetition kicks in. Drill in ~2 weeks. |
| ≥ 80% (2nd time) | 🟢 **Low** | Very strong. Promote to long-term review cycle. Drill in ~1 month. |
| Graduated (⭐) | 🟢 **Low** | Mastered. Review quarterly to prevent decay. |

---

## Aggregate Snapshot

| Metric | Value |
|:--|:--:|
| LOs tracked | 15 |
| 🔴 High priority | 10 |
| 🟡 Medium priority | 4 |
| 🟢 Low priority | 1 |
| ⭐ Graduated | 0 |
| **Avg LO Readiness** | **~0.54** (R30 avg 0.65; R31 baseline 0.45) |
| Target (week 28) | **≥ 0.75** |

*Updated after every drill session (Step 4 of `/drill` close-out). Avg LO Readiness ≠ Exam Readiness — see `_READINESS_DASHBOARD.md` for the weighted exam score (currently 1.2%).*

---

## LO Table

**Columns:** LO ID · Reading · Topic · First Studied · Last Reviewed · Confidence (0-5) · Qs Correct/Attempted · Accuracy · Readiness · Priority

### Book 2 — Credit Risk (20% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Priority |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 30.a | R30 | ISDA event of default & unsecured creditor situations (P3) | 2026-04-18 | 2026-04-20 | 3 | 2/3 | 67% | 0.68 | � Medium |
| 30.b | R30 | CVA & DVA; wrong-way / right-way risk (P4) | 2026-04-18 | 2026-04-21 | 2 | 5/8 | 63% | 0.60 | � Medium |
| 30.c | R30 | PD from credit spreads; risk-neutral vs real-world PD (P1, P2) | 2026-04-18 | 2026-04-20 | 4 | 2/2 | 100% | 0.94 | � Low |
| 30.d | R30 | Credit risk mitigants: netting, collateral, downgrade triggers (P5) | 2026-04-18 | 2026-04-21 | 3 | 6/12 | 50% | 0.58 | 🔴 High |
| 30.e | R30 | Default correlation: reduced-form vs structural models (P6) | 2026-04-18 | 2026-04-20 | 2 | 2/3 | 67% | 0.62 | � Medium |
| 30.f | R30 | Gaussian copula for time-to-default; one-factor model (P7) | 2026-04-18 | 2026-04-20 | 2 | 2/3 | 67% | 0.62 | � Medium |
| 30.g | R30 | Credit VaR via Gaussian copula; CreditMetrics (P8) | 2026-04-18 | 2026-04-21 | 3 | 8/21 | 38% | 0.51 | 🔴 High |
| 31.a | R31 | CDS structure, TRS, CDO; CDS-bond basis; CTD bond (P1, P2) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.b | R31 | CDS valuation: hazard rate, PS/PD, spread calculation (P3) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.c | R31 | Risk-neutral vs real-world PD; RR impact on implied PD (P4) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.d | R31 | Credit indices (CDX/iTraxx), fixed coupons, up-front payments (P5) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.e | R31 | CDS forwards and CDS options (P6) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.f | R31 | Synthetic CDO valuation: spread payments & Gaussian copula (P7) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.g | R31 | Compound (tranche) vs base correlation; smile vs skew (P8) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |
| 31.h | R31 | Alternative approaches to default correlation estimation (P9) | 2026-04-21 | 2026-04-21 | 3 | 0/0 | — | 0.45 | � High |

### Book 1 — Market Risk (20% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Priority |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _To be populated as Book 1 readings are re-converted via /new-reading_ | | | | | | | | | |

### Book 3 — Operational Risk (20% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Priority |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _Pending_ | | | | | | | | | |

### Book 4 — Liquidity Risk (15% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Priority |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _Pending_ | | | | | | | | | |

### Book 5 — Investment Risk + Current Issues (25% exam weight)

| LO | Reading | Topic | First | Last Rev | Conf | Q C/A | Acc | Readiness | Priority |
|:--|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| _Pending_ | | | | | | | | | |

---


## Process Per Drill Session (the "guaranteed-success" loop)

1. **Pick top 3 LOs** by urgency: sort by Priority (🔴 High first), then by Readiness (lowest first within same Priority).
2. **Read the proposition** in the linked Schema B file (5 min each).
3. **Answer 3 questions** (AnalystPrep filtered to that LO, or Schweser Module Quiz).
4. **For each wrong answer:** log the archetype in `_ERROR_ARCHETYPES.md`.
5. **Update this file's row** for the LO: `Last Reviewed = today`, `Confidence`, `Q C/A`, `Accuracy`, new `Readiness`, new `Priority` per Leitner.
6. **Add to _ANKI-style self-quiz** in §5 of the Schema B file if a new trap is discovered.
7. **Close session** — 5 min passive: NotebookLM audio on today's LOs for tomorrow's commute.

## Dashboard Link

See `@c:\Users\user\Documents\FRM 2\wiki\_READINESS_DASHBOARD.md` for the rolled-up exam-readiness score updated from this tracker.
