# The Boole Scaffold: Reading 29 - Portfolio Credit Risk

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R28 — Credit VaR](R28_Credit_VaR.md), [R30 — Credit Risk](R30_Credit_Risk.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Default Correlation Impact:** In a portfolio, higher default correlation increases the probability of extreme events (tail risk/Credit VaR) while decreasing the probability of suffering exactly zero defaults. | `[THE]` | Absolute Dominance — The central tension of portfolio credit modeling. | "joint default," "increase in default correlation" |
| P2 | **Copulas (Gaussian vs Student-t):** Copulas separate the marginal distributions of single assets from their joint correlation structure. The Student-t copula features "tail dependence" (assets crash together). | `[THE]` | High — The mathematical engine for modeling joint defaults. | "Gaussian copula," "tail dependence," "Student's t" |
| P3 | **Idiosyncratic vs Systematic Risk:** As a portfolio approaches infinite granularity ($N \to \infty$), idiosyncratic risk diversifies to zero; only systematic risk (macro shocks) remains. | `[ECO]` | High — Drives the Vasicek model used in Basel IRB. | "infinitely granular," "systematic factor" |
| P4 | **Default Mode vs Mark-to-Market:** Default Mode only recognizes losses if an obligor defaults. MtM (CreditMetrics) recognizes losses for credit downgrades even without default. | `[OPS]` | Medium — Defining model boundaries. | "credit migration," "rating transition matrix" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (Correlation) | The economy enters a deep systemic crisis, driving the correlation between a portfolio of SME loans from 0.1 to 0.8. | The variance (Unexpected Loss) **explodes**. The EL remains unchanged, but the right tail (Credit VaR) thickens massively, requiring substantially more Economic Capital. |
| P2 (Gaussian Copula) | A bank switches its CDO pricing model from a Gaussian copula to a Student-t copula with low degrees of freedom, holding correlation constant. | The **probability of joint extreme defaults increases**. Student-t captures tail dependence (black swans) that the bell-curve Gaussian copula fatally ignores. |
| P3 (Granularity) | A bank holds 5 massive corporate loans instead of 10,000 small mortgage loans, but total EAD is identical. | The portfolio is **not granular**. Idiosyncratic risk dominates. Regulatory Capital formulas (Vasicek) will critically *underestimate* risk without a Granularity Adjustment. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Asset correlation vs Default correlation (they are related but not identical; asset correlation drives default correlation in threshold models).
- The shape of the copula (Tail dependence = Yes/No).
- Number of names in the portfolio (Granularity).

**Noise (distractors):**
- Expected Loss changes when purely discussing correlation shifts. (Correlation moves UL and VaR, but *EL is independent of correlation*).
- Equity market beta when the model uses pure statistical copulas.

**Tensions:**
- **[THE] vs [OPS]:** The Gaussian copula `[THE]`oretically assumes extreme joint defaults are impossibly rare. `[OPS]`erationally (as seen in 2008), housing markets crash together, heavily punishing models that lack tail dependence.

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| Copula Tail Dependence | Gaussian → Student-t → Joint Extreme Loss ↑ | Assuming Gaussian copulas are conservative. They are precisely the opposite; they under-price tail risk. |
| Portfolio variance | Correlation ($\rho$) ↑ → Portfolio Variance ↑ | Thinking correlation increases Expected Loss. EL is the sum of individual ELs and entirely ignores correlation. |


## 5. Ambiguity Traps (Anti-Decoder)
- **Granularity Adjustment:** Corrects the Vasicek single-factor model for finite portfolio size. The adjustment INCREASES capital requirements because smaller portfolios retain more idiosyncratic risk.
- **Vasicek Formula Inputs:** WCDR requires PD, ρ (asset correlation), and the confidence level. It does NOT require LGD — LGD is multiplied AFTER computing WCDR to get Credit VaR.
- **Single-Factor Limitation:** The Vasicek model assumes a single systematic factor drives all correlations. In reality, sector-specific factors exist, which is why portfolio-specific adjustments are needed.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
