# R89 — Portfolio Performance Evaluation

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.89.1` | **Time-Weighted vs. Dollar-Weighted:** Time-weighted returns remove the impact of cash flows (deposits/withdrawals) and are the industry standard for evaluating **Manager skill**. Dollar-weighted returns (IRR) reflect the **Investor's experience**. | `[MTH/THE]` | Manager: "I grew the money by 10% per year." Investor: "But I put all my money in right before the crash, so I'm down 5 points." Both are right. |
| `P.89.2` | **The M2 Measure:** A variation of the Sharpe ratio that translates "Risk-adjusted performance" into a return number that can be directly compared to the market. It shows what the portfolio *would* have returned if its volatility were matched to the market. | `[MTH]` | It "Normalizes" the playing field. If you were as volatile as the S&P 500, how much extra performance would you have delivered? |
| `P.89.3` | **Sharpe Style Analysis:** A regression-based method to uncover a manager's "Actual" asset allocation. The $R^2$ represents the return due to **Style (Asset Allocation)**, while $1-R^2$ represents the return due to **Selection (Skill)**. | `[MTH/THE]` | Most managers (97%+) are just riding a style (e.g., "Tech Stocks"). Very few are actually "picking winners" within that style. |
| `P.89.4` | **Performance Attribution (Brinson Model):** Total excess return is decomposed into **Asset Allocation** (overweighting the right sectors) and **Security Selection** (picking the right stocks within sectors). | `[MTH/OPS]` | Did you win because you bet on "Tech" (Allocation), or because the specific tech stock you picked, "NVIDIA," went to the moon (Selection)? |
| `P.89.5` | **Hedge Fund Performance Hazards:** Hedge fund returns are often "Smoothed" due to illiquid holdings, making their volatility and correlations appear artificially low. They also exhibit nonlinear (option-like) risks that increase during crises. | `[MKT/OPS]` | A hedge fund is the "Hidden Iceberg." On the surface (stale prices), it looks calm. Underneath (crisis), it has massive, non-linear exposure that can sink the ship instantly. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If an investor adds capital right before a period of POOR performance:** The **Dollar-Weighted** return will be **Lower** than the Time-Weighted return. 
- **Variable Flip: If a manager matches the benchmark beta perfectly but underperforms the benchmark return:** **Jensen's Alpha** will be **Negative**. The manager failed to deliver the "Required" return for that level of systematic risk.
- **Variable Flip: If a manager has "Perfect Foresight":** Their performance profile will look like a **Call Option**. They switch to the risky asset when it's going up and stay in cash when it's going down. The "Value" of their skill is equal to the price of that option.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Sharpe Ratio:** Uses Standard Deviation (Total Risk). | **Treynor Ratio:** Uses Standard Deviation (NO: it uses Beta). |
| **Information Ratio:** Alpha / Tracking Error. | **Jensen's Alpha:** Alpha / Beta (NO: Alpha is the *result* of the regression). |
| **Style Attribution (R^2):** Return from Asset Allocation. | **Selection Attribution (1-R^2):** Return from Market Timing + Selection. |

## 4. Directional Intuition
- **Tracking Error $\uparrow \rightarrow$ Information Ratio $\downarrow$:** (Assuming Alpha stays same). The more you "wobble" away from the benchmark without extra reward, the less efficient you are as a manager.
- **Illiquidity $\uparrow \rightarrow$ Volatility (Measured) $\downarrow$:** Stale pricing makes assets look "Stable" even when they aren't.
- **Market Timing Skill $\uparrow \rightarrow$ Portfolio Convexity $\uparrow$:** A good timer creates an "Up-captured" curve where they participate in gains but miss out on losses.

## 5. Ambiguity Traps (Anti-Decoder)
- **Time vs. Dollar:** If you didn't control when the money arrived, use **Time-Weighted**.
- **Sharpe vs. Treynor:**
    - Use **Sharpe** if the portfolio is the **Entire** investment (Total risk matters).
    - Use **Treynor/Jensen** if the portfolio is just **One piece** of a larger diversified fund (Systematic risk matters).
- **Jensen's Alpha:** It’s a measure of **Absolute Skill** ($y$-intercept of the regression).
- **Information Ratio:** It’s a measure of **Relative Efficiency** (How well you take "Tracking Error" risk).
- **Style Analysis Constraints:** Slopes must sum to **1** and be **$\geq 0$** (No shorting).
- **Market Timing:** Look for "Beta shifting" or "Option-like" payoffs.
- **M2 interpretation:** Units are **Returns** (e.g., 12%). It’s the return after adjusting the portfolio to have the same vol as the market.
- **Aggregate Contribution:** Asset Allocation + Selection. 
- **Selection Attribution Math:** $W_p \times (R_p - R_b)$. (Common trap: using $W_b$ instead).
- **Hedge Fund Risk:** Does it stay constant? **NO.** It increases significantly in market crises.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
