# R85 — Alpha (and the Low-Risk Anomaly)

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.85.1` | **The Low-Risk Anomaly:** Empirical evidence shows that low-beta and low-volatility stocks consistently earn higher risk-adjusted returns than high-beta stocks, directly contradicting the CAPM's "Risk-Reward" trade-off. | `[THE/ECO]` | The tortoise beats the hare. Boring, stable stocks grow steadily, while "exciting" high-beta stocks are over-hyped and over-priced, leading to poor future returns. |
| `P.85.2` | **Alpha & Tracking Error:** Alpha ($ \alpha $) is the excess return above a benchmark; Tracking Error is the volatility of that excess return ($ \sigma_{\alpha} $). | `[MTH/OPS]` | Alpha is your "Skill" (the gap from the pack); Tracking Error is how much you "Wobble" relative to that pack. |
| `P.85.3` | **Information Ratio (IR):** The definitive measure of active manager skill, calculated as `Alpha / Tracking Error`. It represents the "bang for buck" for straying from the benchmark. | `[MTH/OPS]` | It’s your "Efficiency." High Alpha with huge Tracking Error is just lucky gambling; High Alpha with low Tracking Error is high-precision skill (High IR). |
| `P.85.4` | **The Fundamental Law (Grinold):** The potential for active return is a function of skill (IC) and opportunity set (Breadth): $ IR \approx IC \times \sqrt{BR} $. | `[MTH/THE]` | To be a great gambler, you either need to be a "Super-Predictor" (High IC) on a few big games, or just "Decently Good" across thousands of small games (High Breadth). |
| `P.85.5` | **The Leverage Proxy Trap:** Retail investors often face "Leverage Constraints" (they can't borrow at the risk-free rate). To get higher returns, they buy high-beta stocks as a "proxy" for leverage, which bids prices up and drives future returns down. | `[ECO/THE]` | If you aren't allowed to "borrow money to buy stocks," you just "buy stocks that move twice as much." This crowded trade makes those stocks expensive "losers." |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If an investor uses the Risk-Free Rate as a benchmark:** Then the **Sharpe Ratio** is the correct risk-adjusted measure (not the Information Ratio).
- **Variable Flip: If a manager increases "Breadth" but the new bets are correlated:** This violates the Fundamental Law. Breadth must be **Independent** bets. If you bet on 100 tech stocks, that's just 1 big "Tech Bet," not 100 small "Breadth" bets.
- **Variable Flip: If a benchmark is NOT replicable or tradeable:** Then the resulting Alpha is "Fake." You can't claim you beat a benchmark that couldn't have been bought in the first place (e.g., an uninvestable index with no fees).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Low-Risk Anomaly:** Low beta = High risk-adjusted return. | **Low-Risk Anomaly:** Higher risk = higher reward (NO: that's CAPM). |
| **Information Ratio:** Alpha / Tracking Error. | **Information Ratio:** Alpha / Beta (NO: that's Treynor). |
| **IC (Information Coefficient):** Correlation between forecast and actual. | **IC:** Number of trades made (NO: that's Breadth). |

## 4. Directional Intuition
- **Breadth $\uparrow \rightarrow$ Information Ratio $\uparrow$:** The more independent shots you take, the more "Luck" averages out, leaving only your "Skill" (IC).
- **Leverage Constraints $\uparrow \rightarrow$ Demand for High-Beta $\uparrow \rightarrow$ High-Beta Alpha $\downarrow$:** The restricted ability to borrow makes "Volatile" assets overpriced.
- **Manager Agreement $\uparrow$ (Homogeneous) $\rightarrow$ CAPM holds best:** When everyone agrees, the anomaly disappears. When everyone **disagrees** (high dispersion), the anomaly gets stronger.

## 5. Ambiguity Traps (Anti-Decoder)
- **The Contradiction:** Does the Low-Risk Anomaly support CAPM? **NO.** It falsifies the central prediction of CAPM.
- **The "Independent" Beta:** Breadth means **Independent** bets. 100 bets on the same industry = Breadth of 1.
- **Nonlinear Hazards:** Be wary of high Alpha in strategies like **Merger Arbitrage** or **Pairs Trading**. This can be "Fake Alpha" (actually just compensation for the risk of a "tail event" crash).
- **The "One-Day" Tenor:** In liquidity/risk reporting, some assets are treated as 1-day regardless of their maturity to model worst-case "Stickiness."
- **IC vs. IR:** 
    - **IC** is how smart you are (accuracy).
    - **IR** is how effective your whole process is.
- **Betting Against Beta (BAB):** Frazzini & Pedersen. The specific trade of going long low-beta and short high-beta to exploit the "Leverage Constraint" bias.
- **Anomalies vs. Data Mining:** Critics argue the anomaly is just a result of looking too hard at past data; supporters argue it’s a systemic behavioral failure.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
