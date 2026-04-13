# R16 — The Vasicek and Gauss+ Models

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.16.1` | **The Gauss+ Cascade:** A 3-factor model where the short-rate ($r_t$) doesn't just revert to a constant, but to a "Moving Target"—the medium-term factor ($m_t$), which itself reverts to a long-term factor ($l_t$). | `[MTH/THE]` | It’s like a "Parent-Child" relationship. The toddler ($r_t$) follows the teenager ($m_t$), the teenager follows the adult ($l_t$), and the adult follows a fixed "Philosophy" ($\mu$). |
| `P.16.2` | **The Three Economic Shocks:** 
- **Short:** Central bank policy actions. 
- **Medium:** Business cycles. 
- **Long:** Long-term inflation and growth expectations. | `[MKT/ECO]` | The interest rate isn't just one "Wiggle"; it's a combination of a daily "Tic" (Fed), a yearly "Swing" (Economy), and a 20-year "Trend" (Demographics). |
| `P.16.3` | **Hump-Shaped Volatility:** Unlike the simple Vasicek model (which predicts volume always declines with maturity), the Gauss+ model can replicate the "Hump" where volatility is highest in the 1Y-2Y range. | `[MTH/MKT]` | In the real world, next week is unpredictable, and 10 years from now is a guess. But the "Near Future" (1-2 years) is often where the most chaotic "Argument" between the market and the Fed happens. |
| `P.16.4` | **Reversion Speeds ($\alpha$):** Gauss+ assumes $\alpha_r > \alpha_m > \alpha_l$. The short rate moves back to its target much faster than the long-term trend moves. | `[MTH]` | The toddler runs back to the teenager faster than the adult changes their life philosophy. |
| `P.16.5` | **Calibration via Least Squares:** The final target ($\mu$) is found by minimizing the squared errors between the model’s predicted yield curve and the actual market yield curve. | `[MTH/OPS]` | You tweak the knobs on your machine until the output line on the screen perfectly overlaps with the real-world line. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If all Mean Reversion speeds ($\alpha$) are set to ZERO:** The model breaks. It becomes a system of three independent random walks with no connection, losing its cascading nature.
- **Variable Flip: If a surprise inflation report comes out (Long-term shock):** All three factors in the Gauss+ will eventually adjust, but the **Long-term Factor ($l_t$)** will move the most permanently, shifting the entire curve level.
- **Variable Flip: If you use Vasicek for a portfolio of intermediate-maturity options:** Your VaR will be **Wrong**. Vasicek overestimates short vol and underestimates long vol. Only the Gauss+ (or a time-dependent vol model) can correctly price the "Hump."

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Gauss+:** Reverts $r \rightarrow m \rightarrow l \rightarrow \mu$. | **Gauss+:** Reverts $l \rightarrow m \rightarrow r \rightarrow \mu$ (NO: it’s short to long). |
| **Medium-term Factor:** Business cycles. | **Medium-term Factor:** Daily Fed meetings (NO: that's short-term). |
| **Vasicek Volatility:** Always declining. | **Vasicek Volatility:** Hump-shaped (NO: only Gauss+ can do that). |

## 4. Directional Intuition
- **Economic Volatility $\uparrow \rightarrow$ Medium-term Factor ($m_t$) Variance $\uparrow$:** If the business cycle becomes more erratic, the "Target" that short rates follow becomes harder to hit.
- **Mean Reversion Speed ($\alpha_r$) $\uparrow \rightarrow$ Short-term Rate Stability $\uparrow$:** A high alpha means the short rate is "Glued" to the target; it might jump, but it doesn't stay away for long.
- **Hump Positioning:** If $\alpha_r$ and $\alpha_m$ are close together, the volatility "Hump" shifts further out on the maturity spectrum.

## 5. Ambiguity Traps (Anti-Decoder)
- **The Cascade Equation:** $dr_t = \alpha_r(m_t - r_t)dt + \sigma_r dw$. Note that $m_t$ is inside the drift of $r_t$.
- **Hump-Shaped Volatility:** This is the #1 reason to use Gauss+ over Vasicek.
- **Number of Factors:** Don't forget—it's a **3-Factor** model (Short, Medium, Long).
- **Constant Target ($\mu$):** Only the long-term factor ($l_t$) looks at a constant number. Everything else looks at a moving target.
- **Calibration Steps:** 
    1.  Pick Proxies (Fed Funds, 2Y, 10Y).
    2.  Regress to find sensitivities.
    3.  Compute Alphas.
    4.  Minimize Squared Error to find Mu.
- **Vasicek's Failure:** It cannot price interest rate caps/floors accurately across the entire curve because its volatility shape is too rigid.
- **Exogenous Shock vs. Mean Reversion:** Note that a shock to $r_t$ (like a 50 bps Fed hike) "Dissipates" as it filters through the cascade.
- **Correlations:** Gauss+ allows for correlations between the shocks to $r, m, \text{and } l$. Usually, $\rho > 0$ because economic news affects all parts of the curve to some degree.
- **Short-lived News:** Means higher $\alpha$. This reading links "Short-lived" to higher mean reversion (same as R14).
- **Gauss+ as "Arbitrage-Free":** Often used to price illiquid "Off-market" swaps by calibrating to the "On-the-run" Treasury curve.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
