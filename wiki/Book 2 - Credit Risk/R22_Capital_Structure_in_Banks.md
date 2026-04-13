# The Boole Scaffold: Reading 22 - Capital Structure in Banks

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:*
*Related Readings: [R21 — Credit Risk Management](R21_Credit_Risk_Management.md), [R23 — Credit Risk Modeling](R23_Intro_to_Credit_Risk_Modeling.md), [R28 — Credit VaR](R28_Credit_VaR.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Unexpected Loss (UL):** The standard deviation of expected losses. Modeled using a beta distribution. UL = $EA \times \sqrt{PD \times \sigma^2_{LR} + LR^2 \times \sigma^2_{PD}}$. | `[THE]` | High — Understanding the variance drivers of credit portfolios. | "variation of loss," "capital buffer" |
| P2 | **Portfolio UL & Diversification:** The Portfolio UL is significantly less than the sum of individual ULs because idiosyncratic risk diversifies away. | `[ECO]` | Very High — The basis for credit portfolio math. | "subadditivity," "correlation effect" |
| P3 | **Economic Capital Definition:** The excess capital needed to match the bank's estimate of unexpected loss at a specific confidence interval (e.g., 99.97%). | `[ECO]` | High — Often confused with Regulatory Capital (Basel). | "internal capital adequacy," "multiple of unexpected loss" |
| P4 | **Default Correlation Risk:** As correlation increases, defaults cluster. This ruins diversification benefits, drastically increasing the required Economic Capital. | `[THE]` | Very High — The primary driver of portfolio tail risk. | "systematic risk," "concentration risk" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (UL Formula) | The bank's portfolio consists of assets where PD = 0% and Recovery = 100% (Risk-free). | Unexpected Loss = **Zero**. If there is no probability of default, there is no variance. |
| P2 (Portfolio UL) | The correlation ($\rho$) between all assets in the credit portfolio goes to 1.0. | The portfolio acts as a **single magnificent exposure**. The Portfolio UL equals the simple sum of individual ULs. No diversification benefit. |
| P3 (Economic Capital) | The Board decides to lower the internal confidence interval from 99.9% to 95%. | The required **Economic Capital drops massively**. (Conversely, increasing the confidence interval scales up capital requirements exponentially). |

## 3. Dependency & Noise Map

**Signal (these matter):**
- PD, LR (LGD), and EA (EAD).
- Asset return correlation ($\rho$).
- Capital Multiplier (CM) corresponding to the chosen confidence interval.

**Noise (distractors):**
- Expected Loss (EL) metrics when asked *specifically* to calculate the Capital Buffer / Economic Capital. EL is covered by pricing/reserves, NOT capital.
- Market risk variations (like daily spread moves) in a strictly bottom-up default-mode framework.

**Tensions:**
- **[ECO] vs [THE]**: In `[THE]`ory, bottom-up default models require thousands of pairwise correlations to work perfectly. In `[ECO]` practice, this is computationally explosive, so banks often use single-factor models (a macro factor) to simulate correlation.



## 4. Directional Intuition
- **Default Correlation (ρ) ↑ → Portfolio UL ↑ → Economic Capital ↑:** Clustering of defaults destroys diversification and pushes the tail of the loss distribution outward.
- **Confidence Interval ↑ → Economic Capital ↑ (exponentially for fat tails):** Moving from 99.5% to 99.9% can more than double the required capital for credit portfolios.
- **Number of Obligors ↑ → Idiosyncratic Risk ↓ → Portfolio UL ↓ (if correlation is low):** Diversification works only when defaults are not perfectly correlated.

## 5. Ambiguity Traps (Anti-Decoder)
- **EL in Capital:** Does Expected Loss belong in Economic Capital? **NO.** EL is priced into the loan spread and covered by reserves. EC covers only UL.
- **Sum of ULs ≠ Portfolio UL:** Individual ULs are NOT additive. Portfolio UL < Sum(Individual ULs) due to diversification unless ρ = 1.
- **"99.97% confidence":** This is the typical A-rated bank target. Don't confuse with 99.9% (Basel IRB) or 99.5% (Solvency II). The confidence level determines which quantile of the loss distribution you must capitalize.
- **Beta Distribution:** The loss rate is modeled using a Beta distribution (bounded 0-1), NOT a Normal distribution (which can go negative).

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
