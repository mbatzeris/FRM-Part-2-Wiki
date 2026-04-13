# R87 — Portfolio Risk: Analytical Methods

**Exam Priority:** 🟡 Medium (1-2 questions) Methods

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.87.1` | **Individual vs. Diversified VaR:** Individual VaR treats a position in a vacuum; Diversified VaR accounts for the correlations between positions. The sum of Individual VaRs will always be $\geq$ Diversified VaR. | `[MTH/THE]` | Individual VaR is "The risk if this is the only thing I house." Diversified VaR is "The risk of this item as part of the whole collection." |
| `P.87.2` | **Marginal VaR (MVaR):** The sensitivity of the total portfolio VaR to a tiny ($1) change in a specific position's size. It is proportional to the position's **Beta** relative to the portfolio. | `[MTH]` | It’s the "Risk Derivative." If I add $1 more of Stock A, by how many pennies does my total portfolio VaR move? |
| `P.87.3` | **Component VaR (CVaR):** An additive measure that approximates how much the total portfolio VaR would drop if the position were completely removed. $CVaR_i = MVaR_i \times W_i$. | `[MTH/OPS]` | It’s a "Risk Attribution" tool. If the total VaR is $100 and CVaR for Apple is $10, Apple is "responsible" for 10% of the risk. |
| `P.87.4` | **Rule for Global Minimum Variance:** A portfolio is at its minimum risk level when the **Marginal VaRs of all positions are equal** ($MVaR_i = MVaR_j$). | `[MTH]` | If adding $1 of A adds 5 cents of risk, but adding $1 of B adds 3 cents, you should move money from A to B until they both add the same "marginal" risk. |
| `P.87.5` | **Rule for Optimal (Tangent) Portfolio:** A portfolio is optimal when the ratio of **Excess Return to Marginal VaR** is equal across all positions: $\frac{R_i - R_f}{MVaR_i} = \text{Constant}$. | `[MTH/THE]` | It’s the "Risk Efficiency" rule. You shouldn't just equalize risk (MVaR); you should equalize the "Return per unit of marginal risk" across every single bet you take. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a position has a Negative Marginal VaR:** Adding more of this position actually **Reduces** the total portfolio VaR. This typically happens with strong hedges or negatively correlated assets.
- **Variable Flip: If two assets have equal Marginal VaRs but Asset A has a higher expected return:** Then the portfolio is **Not Optimal**. You should move capital from Asset B to Asset A to increase the overall reward-to-MVaR ratio.
- **Variable Flip: If returns are NOT elliptical (Normal):** The simple MVaR and CVaR identities might break. You must use historical simulation and identify the "VaR-equivalent" losses for each position to attribute risk.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Marginal VaR:** Derivative of VaR (change for $1). | **Incremental VaR:** Change for a *large* step or new position. |
| **Component VaR:** Approximate loss from *deleting* a position. | **Individual VaR:** VaR of the position *in isolation*. |
| **Tangency Condition:** Equal Return-to-MVaR ratios. | **Min Variance Condition:** Equal MVaRs (NO: that only minimizes risk). |

## 4. Directional Intuition
- **Correlation $\uparrow \rightarrow$ Diversified VaR $\uparrow$:** As assets start moving together, the "Diversification Benefit" evaporates and the portfolio VaR approaches the sum of individual VaRs.
- **Position Beta (to portfolio) $\uparrow \rightarrow$ Marginal VaR $\uparrow$:** High-beta assets "push" the portfolio risk harder than low-beta assets.
- **Excess Return / MVaR $\uparrow \rightarrow$ Weight in Portfolio $\uparrow$:** You want to give the most money to the assets that give you the most "bang" for your marginal risk "buck."

## 5. Ambiguity Traps (Anti-Decoder)
- **Incremental vs. Marginal:** Marginal is for $1 (think calculus). Incremental is for a whole new trade (think "Before vs. After").
- **Beta Context:** In this reading, **Beta** is the regression of the *position* on the *portfolio*, not the market. 
- **The "Equal MVaR" Trap:** If the question asks for the **Optimal** portfolio, don't just equalize MVaR. You must look at the **Return** as well. Equal MVaR only gives the **Minimum Variance** portfolio.
- **VaR Calculation:** For uncorrelated assets ($ \rho=0 $), $ VaR_p = \sqrt{VaR_1^2 + VaR_2^2} $. 
- **VaR Calculation:** For perfectly correlated assets ($ \rho=1 $), $ VaR_p = VaR_1 + VaR_2 $.
- **CVaR Additivity:** In a linear (delta-normal) VaR model, the sum of Component VaRs equals the **Total Portfolio VaR**.
- **The "1.65" Factor:** Standard for 95% confidence. Don't confuse it with 1.96 (95% two-tailed) or 2.33 (99% one-tailed).
- **MVaR and Diversification:** Can MVaR be negative? **YES.** Can Individual VaR be negative? **NO.** (Risk management is about the *amount* of potential loss).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
