# R86 — Portfolio Construction

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.86.1` | **The Only Observable Input:** In the portfolio construction process, the **Current Portfolio** is the only input that is actually observable. Alphas, covariances, and transaction costs are all estimated and subject to bias. | `[OPS]` | You know what's in your wallet right now. Everything else—how much you'll make, how much you might lose, and how much the broker will charge—is just a guess. |
| `P.86.2` | **Refining Alphas vs. Constraints:** Instead of using hard constraints (like "no short selling"), a manager can **Refine Alphas** to reflect these limitations before performing an unconstrained optimization. | `[THE/OPS]` | Instead of a rule saying "Don't touch that hot stove," you just assign that stove an "Alpha" of negative one million. The math will automatically tell you to stay away. |
| `P.86.3` | **Neutralization Types:** To remove undesirable risks, a manager can use **Benchmark Neutralization** (match beta), **Cash Neutralization** (remove active cash), or **Risk-Factor Neutralization** (match specific factors like Size or Value). | `[THE/OPS]` | It’s about "Ceteris Paribus." You want to bet on your skill in picking stocks, not on whether the whole market or the "Small Cap" index goes up. |
| `P.86.4` | **The No-Trade Region:** Transaction costs create a region where it is optimal **not to trade** because the cost of rebalancing exceeds the expected benefit. This region grows with **Risk Aversion** and **Marginal Contribution to Active Risk**. | `[MTH/ECO]` | If the gas to drive to the store costs $5, you won't go just to save $2 on milk. The more you "hate losing gas money" (Risk Aversion), the more likely you are to stay home. |
| `P.86.5` | **Hierarchy of Optimization:** Quadratic Programming is theoretically the best method as it considers Alpha, Risk, and Costs simultaneously, but it is highly sensitive to errors in **Covariance** estimates. | `[MTH/THE]` | It’s a "Formula 1 Car." If everything is tuned perfectly, it’s the fastest. But if the balance is off by an inch (covariance error), it crashes into the wall. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a manager has a forecast for Stock C but it is NOT in the benchmark:** To minimize active risk, the manager should assign Stock C a tracking weight of **Zero**. 
- **Variable Flip: If transaction costs are Zero:** Then the **No-Trade Region disappears**. The manager would rebalance the portfolio constantly for even the tiniest change in expected Alpha.
- **Variable Flip: If a manager increases "Active Risk":** Optimal **Dispersion** across client accounts will **Increase**. Higher active risk means the manager is taking bigger bets, which are harder to replicate exactly across multiple portfolios with different entry times and cash flows.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Quadratic Programming:** Considers Alpha, Risk, and Costs together. | **Linear Programming:** Considers Alpha, Risk, and Costs together (NO: it ignores risk). |
| **No-Trade Region:** Determined by Transaction Costs and Risk Aversion. | **No-Trade Region:** Determined by Alpha coverage (NO: that's about benchmark tracking). |
| **Amortization:** Transaction costs must be spread over the investment horizon. | **Rebalancing:** Transaction costs are ignored in short-term rebalancing (NO: they define it). |

## 4. Directional Intuition
- **Transaction Costs $\uparrow \rightarrow$ No-Trade Region $\uparrow \rightarrow$ Portfolio Turnover $\downarrow$:** High fees make the manager "Stickier" and less likely to chase small Alpha signals.
- **Risk Aversion $\uparrow \rightarrow$ No-Trade Region $\uparrow$:** The more paranoid the manager is, the more certain they must be about an Alpha boost to justify spending the transaction fee.
- **Active Risk $\uparrow \rightarrow$ Client Account Dispersion $\uparrow$:** The more aggressive the strategy, the harder it is to keep all clients' returns identical.

## 5. Ambiguity Traps (Anti-Decoder)
- **The Best Method:** If asked for the most robust *theoretically*, pick **Quadratic Programming**. If asked which is sensitive to input errors, it's also **Quadratic**.
- **Alpha Coverage:** If you have an alpha for a stock NOT in the index, should you buy it? **For a tracking portfolio, NO.** Its weight should be zero.
- **Neutralization:** Benchmark neutralization is about matching the **Beta**, not the specific stocks.
- **Amortization:** Why is it hard to value trades? Because you pay the cost **Today** but get the alpha **Over Time**. You have to "guess" how long you will hold the stock to know if the trade was worth it.
- **Dispersion:** What's the main cause? **History.** (When did the client give you money and what have they bought since?)
- **Screening vs. Stratification:**
    - Screening: "Buy the Top 10." 
    - Stratification: "Buy the Top 2 in each of these 5 industries."


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
