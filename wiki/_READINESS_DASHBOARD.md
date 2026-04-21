# Readiness Dashboard

**Target:** Exam Readiness ≥ 0.75 by **Week 28** (week of 2 November 2026)
**Exam:** Saturday 21 November 2026
**Historical pass rate:** ~52% · **Personal target:** 75%+ on mocks = >90% estimated pass probability

---

## Current Overall Readiness

```
Overall Exam Readiness:  0.010 / 1.00
                         [░░░░░░░░░░░░░░░░░░░░]   1.0%
Target (Week 28):        0.75 / 1.00
                         [███████████████░░░░░]  75%
Gap to close:            74.0 pp  ·  Weeks remaining: 31
Required weekly gain:    +2.4 pp / week
```

> Week 1 baseline: R30 (7 LOs, avg 0.65) + R31 (8 LOs, formula-baseline 0.28) = 15 LOs tracked → Avg LO Readiness 0.45 × 10.7% coverage × 20% book weight ≈ 0.010 overall. Rises rapidly as Book 2 fills in and R31 is drilled.

---

## Formula

```
Book_Readiness = Σ( LO_Readiness × Reading_exam_share_within_book × ...
                  × Book_coverage_of_tracked_LOs )

Exam_Readiness = Σ( Book_Readiness × Book_exam_weight )

where Book_exam_weights = {
    Book 1 Market:       0.20,
    Book 2 Credit:       0.20,
    Book 3 OpRisk:       0.20,
    Book 4 Liquidity:    0.15,
    Book 5 Inv + Issues: 0.25
}
```

> **Coverage caveat:** A book that has only 1/24 readings tracked contributes a tiny signal regardless of how well you know that 1 reading. The dashboard discounts untracked LOs as `Readiness = 0`, which is the honest representation. As you complete readings, the score climbs naturally.

---

## Per-Book Breakdown

| Book | Weight | LOs tracked | Avg LO Readiness | Book Coverage | **Book Readiness** |
|:--|:--:|:--:|:--:|:--:|:--:|
| Book 1 — Market Risk | 20% | 0 | — | 0% | **0.00** |
| Book 2 — Credit Risk | 20% | 15 (of ~140) | 0.45 | 10.7% | **0.048** |
| Book 3 — Operational Risk | 20% | 0 | — | 0% | **0.00** |
| Book 4 — Liquidity Risk | 15% | 0 | — | 0% | **0.00** |
| Book 5 — Investment Risk + Current Issues | 25% | 0 | — | 0% | **0.00** |
| **TOTAL WEIGHTED** | **100%** | | | | **0.010** (1.0%) |

---

## Trajectory Forecast (if you hit 2.5 readings/week)

```
Week  1  (20 Apr)  ████░░░░░░░░░░░░░░░░  0.05
Week  5  (18 May)  ████████░░░░░░░░░░░░  0.15  — Book 2 complete
Week 13 (13 Jul)   ████████████░░░░░░░░  0.35  — Book 3 complete
Week 18 (17 Aug)   ██████████████░░░░░░  0.50  — Book 4 complete
Week 22 (14 Sep)   ████████████████░░░░  0.65  — Book 5 (R83-R99) complete
Week 23 (21 Sep)   █████████████████░░░  0.70  — Current Issues complete
Week 24 (28 Sep)   █████████████████░░░  0.68  — Mock 1 (dips after honest grading)
Week 28 ( 2 Nov)   ██████████████████░░  0.75  ← TARGET
Week 30 (16 Nov)   ███████████████████░  0.80  — Mock 4 week
```

Minor dip around Week 24 is **expected and healthy** — your first real mock will expose overconfident self-ratings, and honest recalibration drops the score ~5 pp. That's the system working correctly.

---

## Warning Thresholds

| If by... | Readiness is below... | Escalate by... |
|:--|:--:|:--|
| Week 10 | 0.25 | Cutting passive time → active drills; drop 1 reading/week target; schedule family-care buddy weekend |
| Week 18 | 0.45 | Skip Current Issues reading depth (accept 10% weight loss); focus Books 1-4 |
| Week 24 | Mock 1 < 55% | Deep error-archetype review in Week 25; do Mock 1b (different seed) Week 26 |
| Week 28 | < 0.65 | Consider deferring to May 2027 — only if sustained drop is systemic, not a one-week dip |

---

## Update Cadence

- **Per drill session:** individual LO row in `_LO_TRACKER.md`
- **Per Sunday:** roll-up of this dashboard (overall %, book breakdown)
- **Per mock:** overlay mock score onto forecast line
- **Per month-end:** full trajectory recompute

## See Also

- `@c:\Users\user\Documents\FRM 2\wiki\_LO_TRACKER.md` — source data
- `@c:\Users\user\Documents\FRM 2\wiki\_WEEKLY_LOG.md` — Sunday check-ins
- `@c:\Users\user\Documents\FRM 2\wiki\_ERROR_ARCHETYPES.md` — error taxonomy
