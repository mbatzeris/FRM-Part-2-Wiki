# R18 — Fundamental Review of the Trading Book (FRTB)
**Exam Priority:** 🔴 High (3-4 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.18.1` | **The Shift to Expected Shortfall (ES):** The most significant change. FRTB replaces the 99% VaR with a **97.5% Expected Shortfall**. ES captures the "Tail Risk" (the average loss when you've already crashed), which VaR ignores. | `[REG/OPS]` | VaR tells you: "You might lose more than $1,000." ES tells you: "When you lose more than $1,000, the average loss is $5,000." It’s much more honest about the disaster. |
| `P.18.2` | **The Trading vs. Banking Boundary:** FRTB imposes strict, rules-based criteria for what can be in the "Trading Book" (Mark-to-Market) vs. the "Banking Book" (Accrual). This stops banks from "hiding" risky assets in whichever book requires less capital. | `[REG/OPS]` | It prevents "Accounting Magic." You can't just move a failing asset from your "Short-term Trading" pile to your "Long-term Investment" pile just to avoid showing a loss. |
| `P.18.3` | **Liquidity Horizons (LH):** Instead of assuming everything can be sold in 10 days, FRTB assigns risk factors to buckets of 10, 20, 40, 60, or 120 days. Less liquid assets (like small-cap stocks or credit spreads) require more capital. | `[REG/MKT]` | In a panic, you can sell a US Treasury in an hour, but it might take months to find a buyer for a complex office building loan. The capital check reflects this "Exit Time." |
| `P.18.4` | **P&L Attribution (PLA) Test:** A new requirement for banks using internal models. It compares the P&L predicted by the Risk Management model against the Front Office (Traders') model. If they don't match, the desk loses its model approval. | `[REG/OPS]` | It’s the "Story Check." If the Traders say they made $1M and the Risk Dept says they should only have made $100k, something is wrong with the "Stories" (Models) they are using. |
| `P.18.5` | **Non-Modellable Risk Factors (NMRF):** If a risk factor doesn't have enough "Real Price Observations" (data frequency), it cannot be used in the main ES model. It must have a separate, conservative stressed-capital charge. | `[REG/THE]` | If you only have two data points for an asset all year, you can't build a beautiful "Bell Curve" for it. You have to assume the "Worst Case" because the data is too thin. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a desk fails the PLA Test (P&L Attribution):** It moves to the "Amber zone" (increased capital) or must revert to the **Standardized Approach (SA)**. It loses the "discount" of using its own internal math.
- **Variable Flip: If the Liquidity Horizon for an asset is 120 days:** The capital charge will be significantly **Higher** than a 10-day asset, as the model must "Stochastic-walk" the risk for 4 months instead of 2 weeks.
- **Variable Flip: If a bank uses internal models (IMA) but their backtesting shows too many exceptions:** The multiplier $k$ increases, and they may be forced back to the Standardized Approach (SA).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **FRTB Measure:** 97.5% Expected Shortfall (250-day Stressed period). | **FRTB Measure:** 99% VaR or 10-day period (NO: that was Basel II.5). |
| **Liquidity Horizon:** Minimum is 10 days. | **Liquidity Horizon:** Minimum is 1 day (NO). |
| **PLA Test:** Compares Risk P&L vs. Actual Front-Office P&L. | **PLA Test:** Compares Bank P&L vs. Peer P&L (NO). |
| **Securitizations:** MUST use the Standardized Approach (SA). | **Securitizations:** Can use internal models with high capital charges (NO). |

## 4. Directional Intuition
- **Asset Liquidity $\downarrow \rightarrow$ Liquidity Horizon (LH) $\uparrow \rightarrow$ Capital Charge $\uparrow \uparrow$:** If an asset is "hard to move," the regulator forces you to hold way more safety cash against it.
- **Tail Fatness $\uparrow \rightarrow$ ES Capital vs. VaR Capital $\uparrow$:** The more extreme the outliers, the more ES (which looks at the tail) will penalize you compared to the old VaR.
- **Model Approval $\downarrow$ (Dashed desk) $\rightarrow$ Shift to Standardized Approach (SA):** Regulators are making it harder to use "Internal Black Boxes" unless they are perfectly transparent and accurate.

## 5. Ambiguity Traps (Anti-Decoder)
- **99% VaR vs. 97.5% ES:** Why 97.5%? Because for a Normal distribution, the **99% VaR** is roughly equal to the **97.5% ES**. The change is meant to be "Revenue Neutral" for normal days but "Tail Sensitive" for crash days.
- **Bucketing:** Know the buckets: **10, 20, 40, 60, 120**. (There is no 30 or 50).
- **The Stressed Period:** ES is calculated using a **250-day window (12-month period) of significant stress** (e.g., 2008), not just recent data.
- **Backtesting Exceptions:** Desks are backtested using latest 12 months. If observed exceptions exceed **12 at the 99% level** or **30 at the 97.5% level**, the desk loses internal model approval and reverts to SA.
- **PLA Exceptions:** If PLA ratios fall outside requirements on **four or more occasions during a 12-month period**, capital must be computed using the SA.
- **Jump-to-Default (JTD):** Specifically measures the risk of a sudden issuer default. For JTD, the bank uses **99.9% VaR (1-year horizon)**, not ES. (Odd, but true in the rules).
- **Securitizations:** Under FRTB, any securitized products (ABS, CDO) are strictly forbidden from using internal models; they must use the Standardized Approach.
- **Liquidity-Adjusted ES (IMA):** The framework uses 5 successive shock categories in a nested pairing scheme (ES1 to ES5) scaled by the square root of time horizons.
- **Trading Book vs. Banking Book:** To stay in the Trading Book, a bank must not only have intent to trade, but also **prove ability to trade** and actively manage the risk on a trading desk.
- **Regulatory Arbitrage:** The main motivation for the new Book boundary rules. Reclassification between books is strictly prohibited except under extraordinary structural changes (like a total accounting system shift).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
