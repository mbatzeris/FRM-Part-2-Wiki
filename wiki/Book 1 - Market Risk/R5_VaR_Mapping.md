# R5 — VaR Mapping

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.5.1` | **The Purpose of Mapping:** Complex portfolios (with thousands of assets) are simplified by "mapping" them to a small set of **General Risk Factors**. This solves the problem of missing historical data and reduces computational complexity. | `[OPS/THE]` | It’s like describing a complex meal by its main ingredients (Salt, Sugar, Fat). It’s not perfect, but it’s much easier for the computer to digest than a 50-page recipe. |
| `P.5.2` | **Principal Mapping:** Assumes the entire portfolio's value is concentrated in a single zero-coupon bond at the **Average Life** of the cash flows. | `[MTH/THE]` | You treat a 30-year bond ladder as if it were just one giant check coming on the "average" date. Fast, but ignores the "ends" of the ladder. |
| `P.5.3` | **Cash Flow Mapping:** The most accurate method. Every single coupon and principal payment is treated as a separate zero-coupon bond and assigned to "Standard Vertices" (set time points like 1Y, 5Y, 10Y). | `[MTH/OPS]` | You break the bond into every single "Payday" and put each one into the correct "Bucket" on the calendar. Then you model how those buckets move together. |
| `P.5.4` | **Delta Mapping (Derivatives):** For linearizing non-linear assets (options). The VaR of the option is approximated as: $VaR_{opt} = |\Delta| \times VaR_{und}$. | `[MTH]` | If a stock goes down $1, and your option only goes down $0.50 ($\Delta = 0.5$), then the option's risk is half the stock's risk—as long as the move is small. |
| `P.5.5` | **Tracking Error VaR:** Measures the risk of a portfolio *relative* to a benchmark. It is used by fund managers to ensure they don't wander too far from the index they are supposed to follow. | `[OPS/MKT]` | It’s not about "How much can I lose?", but "How much can I lose *compared to my neighbor*?" |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If you use Principal Mapping for a portfolio with high Convexity:** The VaR estimate will be **Significantly Inaccurate**, as it cannot capture the non-linear "bend" of the yield curve.
- **Variable Flip: If Correlations between risk factors are assumed to be 1.0:** The resulting VaR is the **Undiversified VaR** (the simple sum of individual risks). This is almost always an overestimation.
- **Variable Flip: If an option position is mapped using ONLY Delta over a long horizon:** The VaR will be **Useless** because the Delta itself changes (Gamma risk) as the stock price moves. Linear mapping is only valid for "Instantaneous" (1-day) moves.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Cash Flow Mapping:** Maintains the variance and duration of the portfolio. | **Principal Mapping:** Maintains the duration (NO: Duration mapping does that). |
| **Mapping Advantages:** Solving data holes, faster calculation. | **Mapping Advantages:** Increasing specific risk (NO: it decreases specific risk). |
| **Tracking Error VaR:** Smallest when cash flows match exactly. | **Tracking Error VaR:** Smallest when returns are high (NO). |

## 4. Directional Intuition
- **Number of Vertices $\uparrow \rightarrow$ Specific Risk $\downarrow$:** The more detailed your "buckets," the more of the portfolio's unique characteristics are captured by the general factors.
- **Maturity $\uparrow \rightarrow$ Vertex Interest Rate Volatility $\uparrow$:** (Usually) Long-term rates have higher VaR in dollar terms because a small rate change impacts the present value of many future payments.
- **Option Moneyness $\uparrow \rightarrow$ Delta $\uparrow \rightarrow$ Option VaR $\uparrow$:** Deep-in-the-money options behave almost exactly like the underlying stock.

## 5. Ambiguity Traps (Anti-Decoder)
- **Principal vs. Duration Mapping:**
    - **Principal** uses "Average Life."
    - **Duration** uses "Macaulay Duration." (Duration is usually shorter than average life for coupon bonds).
- **Cash Flow Mapping Vertices:** If a cash flow falls between two vertices (e.g., 2.5 years), it is "split" between the 2Y and 3Y vertices to preserve **Duration and Variance**.
- **Forward Mapping:** A Forward on a stock is mapped as: (Long 1 Stock) + (Short Zero-Coupon Bond for the strike).
- **Specific Risk:** This is the risk "lost" during mapping. If your map is too simple, you skip the "unique" wiggles of your specific assets.
- **Undiversified VaR formula:** $VaR = \sum VaR_i$.
- **Diversified VaR formula:** $VaR = \sqrt{\sum \sum VaR_i VaR_j \rho_{ij}}$.
- **Commodity Mapping:** Often mapped to the spot price + basis (spread) risk.
- **Delta-Normal Weakness:** It is "Blind" to **Gamma** (Convexity). If a question asks for the risk of a "Deeply Out-of-the-Money" option, Delta mapping will dangerously underestimate the jump-to-default or volatility risk.
- **Benchmark Matching:** Matching by **Cash Flows** is the best way to minimize tracking error.
- **Standardized Vertices:** These are the "Poles" of the tent. Everything else is just stretched between them.
- **Matrix Notation:** Know that $\mathbf{v}^T \mathbf{R} \mathbf{v}$ refers to the correlation matrix and the vector of individual VaRs.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
