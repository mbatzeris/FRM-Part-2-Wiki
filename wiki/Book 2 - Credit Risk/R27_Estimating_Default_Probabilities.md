# The Boole Scaffold: Reading 27 - Estimating Default Probabilities

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R23 — Credit Risk Modeling](R23_Intro_to_Credit_Risk_Modeling.md), [R29 — Portfolio Credit Risk](R29_Portfolio_Credit_Risk.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Historical vs Risk-Neutral PD:** Historical (Real-world) PD is derived from rating agencies and default statistics. Risk-Neutral PD is inferred from market prices (bonds/CDS) and includes the risk premium. | `[THE]` | Absolute Dominance — The most heavily tested PD concept. | "risk-neutral probability," "historical default rate," "credit spread" |
| P2 | **The Spread-to-PD Formula:** Risk-Neutral PD ≈ Credit Spread / LGD. Therefore, Credit Spread ≈ PD_{RN} × LGD. | `[THE]` | Very High — The core quantitative approximation for backing out PD from a CDS or bond spread. | "spread of X bps," "implied probability of default" |
| P3 | **Risk Premium Wedge:** Risk-Neutral PD is ALWAYS greater than Historical PD because investors demand a premium for bearing default risk (which is historically right-tailed and systematic). | `[ECO]` | High — Tests directional understanding without calculation. | "compare the risk-neutral and real-world," "default risk premium" |
| P4 | **Hazard Rates:** The continuous-time probability of default given survival up to time $t$. Survival probability $S(t) = e^{-\lambda t}$, where $\lambda$ is the hazard rate. | `[THE]` | Medium — Used for multi-year survival math. | "constant hazard rate," "survival probability" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1/P3 (RN vs Hist) | An analyst uses historical default rates from Moody's to price a new Credit Default Swap. | The CDS will be **mispriced (too cheap)**. Historical PD lacks the risk premium. Pricing MUST use Risk-Neutral PD inferred from the market. |
| P2 (Spread Calc) | The recovery rate (1 - LGD) drops from 40% to 20%, but the bond spread remains unchanged. | If LGD increases but the spread is static, the **implied Risk-Neutral PD must have decreased**. (Spread = PD × LGD. If LGD↑, PD must ↓ to keep the spread constant). |
| P4 (Hazard Rates) | The stem gives a 1-year PD of 5% and asks for the 2-year survival probability, assuming a constant hazard rate. | Candidates who use $(1-0.05)^2$ are using discrete math. For continuous hazard rates, you must find $\lambda$ where $e^{-\lambda} = 0.95$, then calculate $e^{-\lambda \times 2}$. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Which PD metric is requested (Historical for capital/provisions, Risk-Neutral for pricing/trading).
- Recovery Rate vs LGD (LGD = 1 - Recovery Rate).
- Whether the interest rates are compounding continuously or discretely.

**Noise (distractors):**
- Risk-free rate fluctuations in simple Spread approximations (the approximation Spread ≈ PD × LGD ignores the risk-free rate entirely).
- Firm-specific equity volatility when the question strictly provides bond spreads (Merton uses equity; reduced-form uses spreads).

**Tensions:**
- **[ECO] vs [OPS]:** `[ECO]`nomically, risk premiums make Risk-Neutral PD higher. In `[OPS]`, banks must reconcile the two: they use Historical PD for Basel `[REG]` capital (Expected Loss) but Risk-Neutral PD for CVA `[OPS]` (Mark-to-Market).

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| $PD_{RN} \approx Spread / LGD$ | Spread ↑ → Implied PD ↑; Recovery Rate ↑ (so LGD ↓) → Implied PD ↑ | Forgetting that LGD = 1 - Recovery, and applying the Recovery Rate as the denominator instead of LGD. |
| Survival Rate $S(t) = e^{-\lambda t}$ | Hazard rate ($\lambda$) ↑ → Survival ↓, Cumulative PD ↑ | Adding discrete yearly PDs instead of compounding survival probabilities (e.g., $PD_{cumulative} = 1 - S(t)$). |


## 5. Ambiguity Traps (Anti-Decoder)
- **Hazard Rate vs. PD:** The hazard rate is the instantaneous conditional default rate. PD over a period T = 1 - e^(-λT) where λ is the hazard rate. They're related but not identical.
- **Risk-Neutral vs. Real-World PD:** Market-implied PDs (from CDS/bonds) are risk-neutral and typically HIGHER than historical PDs because they include a risk premium. Use risk-neutral for pricing (CVA), historical for capital.
- **Rating Migration Matrices:** These are Markov chains — the probability of moving from BBB to BB next year is independent of whether the firm was AA two years ago. This "memoryless" property is an assumption, not a fact.
- **The "Term Structure of PD":** Cumulative PD rises with time. Marginal (forward) PD can rise or fall depending on the credit curve shape. An inverted credit curve implies high near-term risk.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
