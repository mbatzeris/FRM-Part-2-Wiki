# R66 — Liquidity Risk

**Exam Priority:** 🔴 High (3-4 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.66.1` | **Funding vs. Market Liquidity:** Funding liquidity is the ability to meet immediate cash obligations (liabilities); Market liquidity is the ability to sell assets quickly without a large price hit (assets). | `[THE]` | Funding is "Can I pay my rent today?"; Market is "Can I sell my car today at a fair price?" They are two sides of the same coin. |
| `P.66.2` | **The Liquidity Coverage Ratio (LCR):** A 30-day survival metric. Requires `HQLA / Net Cash Outflows >= 100%` under a stress scenario involving a **3-notch downgrade** and total loss of wholesale funding. | `[REG/Basel III]` | It’s a 30-day "Oxygen Tank." It ensures the bank can breathe even if the wholesale funding market (the "air") is completely cut off. |
| `P.66.3` | **Positive vs. Negative Feedback Traders:** Positive feedback traders buy as prices rise (destabilizing); Negative feedback traders buy as prices fall (stabilizing/providing liquidity). | `[THE/MKT]` | Positive feedback traders "Chase the Trend" and create bubbles/crashes. Negative feedback traders "Buy the Dip" and act as the shock absorbers of the market. |
| `P.66.4` | **Liquidity Black Holes & Positive Feedback:** Occur when everyone wants to sell at once. Driven by **Positive Feedback Trading** (stop-loss rules, trend/breakout trading, predatory trading, and unmet margin calls). | `[THE]` | It’s a theater fire where everyone runs for the same tiny door. The "door" (liquidity) effectively closes to zero as the panic increases. |
| `P.66.5` | **Cost of Liquidation:** In a normal market, cost is $\frac{\alpha}{2} \times s$, where $\alpha$ is the mid-market position value and $s$ is the proportional spread. In a **Stressed Market**, the cost is $\frac{\alpha}{2} \times (\mu + z \times \sigma)$ where $\mu$ and $\sigma$ are mean/std dev of the spread. | `[MTH/MKT]` | You lose half the spread when you trade. In a stressed market, you must adjust the expected spread upward by a $z$-score because liquidity dries up precisely when you need it. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank has a 2-notch downgrade in its LCR stress test:** This is **Incorrect**. Basel III mandates a **3-notch** downgrade assumption to ensure the stress is severe enough to represent a true crisis.
- **Variable Flip: If a market is dominated by "Negative Feedback Traders":** Then the market will be highly stable. Price drops will be met with immediate buying interest, preventing "Liquidity Black Holes."
- **Variable Flip: If a bank relies purely on "Trading Book Liquidation" for LCR:** In a stress scenario, this may fail. Markets for even "liquid" stocks can freeze (Black Hole), which is why the LCR focuses on **HQLA** (Cash/Treasuries) which stay liquid.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **LCR Horizon:** 30 days. | **NSFR Horizon:** 1 year. |
| **Wholesale Funding:** Assumed 100% loss in LCR stress. | **Retail Deposits:** Assumed only partial loss in LCR stress. |
| **Negative Feedback:** Stabilizes markets. | **Positive Feedback:** Destabilizes markets (bubbles). |

## 4. Directional Intuition
- **Market Volatility $\uparrow \rightarrow$ Bid-Offer Spread $\uparrow \rightarrow$ Liquidation Cost $\uparrow$:** In a crisis, the "Exit Tax" increases exactly when you need to exit the most.
- **Credit Rating Downgrade $\uparrow \rightarrow$ Required Collateral $\uparrow \rightarrow$ Funding Liquidity $\downarrow$:** A lower rating triggers "Collateral Calls" in derivatives, draining the bank's cash reserves.
- **Crowdedness of Trade $\uparrow \rightarrow$ Liquidity Black Hole Probability $\uparrow$:** The more people in the same "Momentum" trade, the more violent the eventual exit will be.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "30-Day" Metric:** Which Basel ratio? **LCR.** (Don't confuse with NSFR's 1-year horizon).
- **Cost of Liquidation Math:** In stressed markets, you add $z \times \sigma$ to the *mean of the proportional spread* ($\mu$) because liquidity adjustment *increases* the VaR. The formula relies on a strong positive correlation assumption.
- **Stabilization Trap:** Does buying when prices rise help liquidity? **NO.** That is **Positive Feedback** and it increases volatility.
- **Ashanti Goldfields:** Sold gold forwards to hedge against drops. When prices *soared* >25% (due to central banks limiting sales), they faced devastating margin calls they couldn't meet.
- **Metallgesellschaft:** Sold 5-10 year fixed-price oil contracts, hedged with short-term long futures. When prices *dropped*, immediate margin calls misaligned with their illiquid long-term contracts.
- **Northern Rock:** They used short-term debt, but the fatal blow was when the **BBC leaked** their emergency request to the Bank of England, triggering a massive £2B retail bank run in one week.
- **The 3-Notch Rule:** Note the specific LCR stress test rule: **Three** notches downgrade. Not two, not one.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
