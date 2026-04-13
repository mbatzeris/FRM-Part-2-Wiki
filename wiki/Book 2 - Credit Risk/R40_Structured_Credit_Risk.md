# The Boole Scaffold: Reading 40 - Structured Credit Risk

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R29 — Portfolio Credit Risk](R29_Portfolio_Credit_Risk.md), [R41 — Intro to Securitization](R41_Intro_to_Securitization.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **CDO Tranching:** Pooling assets and slicing the liabilities into tranches (Equity, Mezzanine, Senior) based on priority of cash flows and loss absorption. | `[ECO]` | Foundation — Basic structural mechanics. | "attachment point," "detachment point," "waterfall" |
| P2 | **Correlation and Default Risk:** High correlation shifts risk upward in the capital structure. Uncorrelated defaults hit the equity tranche predictably; correlated defaults cause systemic wipeouts that reach the senior tranche. | `[THE]` | Absolute Dominance — The defining mathematical reality of structured credit. | "implied correlation," "tranche sensitivity" |
| P3 | **Mezzanine Tranche Squeeze:** The mezzanine tranche is short correlation against the equity tranche, but long correlation against the senior tranche. Its sensitivity is non-linear and depends heavily on the overall macro environment. | `[THE]` | High — Usually tested graphically or via directional logic. | "mezzanine tranche," "intermediate attachment" |
| P4 | **Synthetic CDOs:** Constructed using CDS portfolios rather than physical cash bonds. Allows slicing of credit risk without needing funding or the physical assets. | `[OPS]` | Low/Medium — Mechanism definition. | "funded vs unfunded," "synthetic CDO" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P2 (Correlation) | Given an existing CDO, the general correlation of the economy drops to near-zero. | The **Equity tranche loses value (becomes riskier)** because it is long correlation. The **Senior tranche gains value (becomes safer)** because it relies on correlation to be breached. |
| P1 (Attachment Points) | The underlying portfolio suffers defaults exactly equal to the Equity detachment point (e.g., 5%). | The Equity tranche is **completely wiped out**. The Mezzanine tranche (attaching at 5%) now acts as the new first-loss (Equity) tranche for all future defaults. |
| P2 (Idiosyncratic Risk) | A bank specifically selects a portfolio of loans with zero correlation across different industries worldwide. | This heavily protects the Senior tranche but guarantees a steady stream of random idiosyncratic defaults that will quickly **devour the Equity tranche**. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Attachment and Detachment points (the boundaries of loss for a specific tranche).
- Base correlation vs Implied correlation.
- The distinction between the underlying collateral correlation and the tranche's sensitivity to it.

**Noise (distractors):**
- The credit rating of the originator/sponsor bank. (CDOs are bankrupt-remote SPVs).
- Interest rate volatility in a pure default-mode synthetic CDO (unless discussing cash-flow reinvestment risk in physical CDOs).

**Tensions:**
- **[THE] vs [REG]:** `[REG]`ulatory ratings (AAA) on senior tranches rely on historical data that heavily penalizes idiosyncratic risk while underestimating `[THE]`oretical tail dependence (correlation spikes during crises). This caused the 2008 downgrade avalanche.

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| Equity Tranche (0% - X%) | Correlation ↑ → Value ↑ (Risk ↓) | "Correlation is bad" heuristic. Equity holders WANT high correlation because it preserves their yield (they only get wiped out once). |
| Senior Tranche (Y% - 100%) | Correlation ↑ → Value ↓ (Risk ↑) | Assuming AAA means risk-free. A highly correlated portfolio acts like a single massive bond—if it fails, the senior tranche fails with it. |


## 5. Ambiguity Traps (Anti-Decoder)
- **Equity vs. Senior Correlation Sensitivity:** Equity tranche is LONG correlation (benefits from ρ↑). Senior tranche is SHORT correlation (hurt by ρ↑). Mezzanine sensitivity is non-monotonic.
- **Subordination ≠ Safety:** Just because a tranche has 30% subordination doesn't mean it's safe. If default correlation is high, losses can bypass the equity tranche and directly hit mezzanine/senior.
- **Gaussian Copula Limitation:** The Gaussian copula underestimates tail dependence — it assumes extreme co-defaults are rarer than they actually are. This was the core model failure of the 2008 crisis.
- **Attachment/Detachment Points:** Know how to read them. A 3-7% mezzanine tranche means it starts absorbing losses after the first 3% of the pool defaults and is wiped out at 7%.

## 5. Ambiguity Traps (Anti-Decoder)
- **Equity vs. Senior Correlation Sensitivity:** Equity tranche is LONG correlation (benefits from ρ↑). Senior tranche is SHORT correlation (hurt by ρ↑). Mezzanine sensitivity is non-monotonic.
- **Subordination ≠ Safety:** Just because a tranche has 30% subordination doesn't mean it's safe. If default correlation is high, losses can bypass the equity tranche and directly hit mezzanine/senior.
- **Gaussian Copula Limitation:** The Gaussian copula underestimates tail dependence — it assumes extreme co-defaults are rarer than they actually are. This was the core model failure of the 2008 crisis.
- **Attachment/Detachment Points:** Know how to read them. A 3-7% mezzanine tranche means it starts absorbing losses after the first 3% of the pool defaults and is wiped out at 7%.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
