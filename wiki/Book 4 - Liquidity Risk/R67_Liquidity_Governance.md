# R67 — Liquidity Governance

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.67.1` | **The Governance Split:** Senior Management is responsible for the *daily management* of liquidity; the Board of Directors is responsible for *approving* the strategy and setting the **Liquidity Risk Tolerance**. | `[OPS]` | The Board decides how much risk is "too much" (Strategy); Senior Management makes sure the bank stays within those lines every day (Tactics). |
| `P.67.2` | **SEC Rule 2a-7 (Amortized Cost):** Money Market Mutual Funds (MMMFs) often use amortized cost accounting, which allows them to maintain a stable Net Asset Value (NAV) of $1.00 even if the market value of assets fluctuates slightly. | `[REG]` | It’s like a "Magic Mirror." It shows a perfectly stable $1.00 as long as the underlying assets don't deviate by more than 0.5%. If they do, the fund "Breaks the Buck." |
| `P.67.3` | **Liquidity Cost of Trading:** Liquidity risk in trading manifests as **Slippage** (price move while trying to trade), **Adverse Price Impact** (you move the market), and bid-ask spreads. | `[MKT]` | Trading isn't free. The more you "rush" or the larger you trade, the more the market "taxes" you through worse prices. |
| `P.67.4` | **Leverage vs. Haircut Relation:** The leverage ratio is the reciprocal of the haircut (if 100% financed by equity). `Leverage = 1 / Haircut`. | `[MTH]` | If you have to put up 10% cash (haircut), you can buy 10 times your equity ($1 / 0.10$). If the haircut is 50%, your leverage is 2.0. |
| `P.67.5` | **Risk Appetite Statement (RAS):** A formal document that defines the specific types and levels of liquidity risk a bank is willing to accept to achieve its business objectives. | `[OPS]` | It’s the bank's "Dietary Plan." It says: "We are willing to take some market risk, but we will NEVER let our 30-day survival buffer fall below 110%." |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank uses Mark-to-Market (MTM) instead of Amortized Cost for a MMMF:** Then the NAV would fluctuate every day (e.g., $0.9998 or $1.0002). While more "accurate," this would remove the "Stable $1.00" illusion that investors value, potentially leading to more frequent redemptions.
- **Variable Flip: If the Fed Initial Margin requirement was 20% instead of 50%:** Then the maximum allowed leverage would increase from **2.0** ($1/0.5$) to **5.0** ($1/0.2$). Lower margins = higher systemic leverage.
- **Variable Flip: If a Board "managed" liquidity directly instead of "oversight":** This would be a failure of governance. Boards are for **Direction**; management is for **Execution**. A Board doing daily liquidity checks is "micromanaging" and loses its objective perspective.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Slippage:** Price deterioration over the duration of the trade. | **Standard Deviation:** A measure of price *volatility*, not liquidity cost. |
| **Board:** Approves Risk Tolerance / RAS. | **Senior Management:** Manages daily liquidity / develops strategies. |
| **Amortized Cost:** SEC Rule 2a-7 for MMMFs. | **Fair Value Accounting:** Is for traditional mutual funds, not stable NAV MMMCs. |

## 4. Directional Intuition
- **Haircut $\uparrow \rightarrow$ Maximum Leverage $\downarrow$:** Higher collateral requirements act as a natural brake on systemic leverage.
- **Trade Size $\uparrow \rightarrow$ Adverse Price Impact $\uparrow$:** The larger your "Footprint," the more the market moves against you before you can finish.
- **Board Engagement $\uparrow \rightarrow$ Risk Transparency $\uparrow$:** When the Board actively challenges management's assumptions, hidden liquidity gaps are more likely to be found.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Breaking the Buck" Trap:** Does a MMMF "break the buck" every time an asset loses $0.01 value? **NO.** Because of **Amortized Cost** accounting, they can hide small fluctuations up to a threshold.
- **Leverage Math:** GARP gives you a 50% margin and asks for the leverage. **Answer: 2.0.** (Don't overcomplicate).
- **Slippage vs. Impact:** Slippage is the market moving *anyway* while you wait; Impact is the market moving *because of you*.
- **The "17 Principles":** Don't memorize all 17, but remember the core split: **Board (Strategy/Tolerance)** vs. **Management (Daily Operations)**.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
