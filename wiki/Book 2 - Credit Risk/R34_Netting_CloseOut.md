# R34 — Netting, Close-Out, and Related Aspects

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.34.1` | **The Netting Principle:** Credit exposure with netting is the "Max of the Sum" ($\max[\sum MtM_i, 0]$), whereas exposure without netting is the "Sum of the Maxes" ($\sum \max[MtM_i, 0]$). | `[MTH/THE]` | Without netting, you lose on every bet you win and still have to pay on every bet you lose. With netting, you only care about the "Bottom Line" of all your bets together. |
| `P.34.2` | **Close-out Netting (Default):** Unlike "Payment Netting," which only happens on payday, "Close-out" happens when someone dies. All contracts are instantly stopped and squashed into one single number. | `[REG/OPS]` | It’s the "Emergency Stop" button. Instead of managing 1,000 separate trades, you just write one check (or receive one check) for the net value and walk away. |
| `P.34.3` | **Netting Benefit & MtM Signs:** Netting is most powerful when you have some trades that are "Winners" ($MtM > 0$) and some that are "Losers" ($MtM < 0$) with the same counterparty. | `[MTH/MKT]` | You want your "Losses" to act as a shield for your "Gains." If you have no "Loser" trades, netting does absolutely nothing to help you. |
| `P.34.4` | **Break Clauses:** Specific survival tools that allow a bank to "pull the plug" on a trade at certain times (before maturity) at its current fair value. | `[THE/MKT]` | It’s a "Pre-nup" for a swap. If things start looking shaky in the future, you have a legal right to get out early with your money intact. |
| `P.34.5` | **Banker’s Paradox:** The idea that you only want to use a break clause when a client is in trouble, but that’s exactly when using it would destroy your relationship with them. | `[ECO/THE]` | It’s like firing a friend. It’s the right business move, but it has a high social/reputational cost, so you wait too long and lose money instead. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a firm only buys OPTIONS from a counterparty:** **Netting is useless**. Options always have a positive or zero value. You never have a "negative" position to offset your gains.
- **Variable Flip: If there is no "Master Agreement" (ISDA) in place:** The liquidators of a failed bank can "Cherry Pick"—they will take the trades you owe them money on and walk away from the trades they owe you money on.
- **Variable Flip: If you implement Payment Netting but NOT Close-out Netting:** You have reduced your **Settlement Risk** (cash transfer stress), but your **Credit Risk** remains 100% higher should the counterparty suddenly fail.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Close-out Netting:** Reduces Pre-settlement Risk. | **Payment Netting:** Reduces Pre-settlement Risk (NO: only settlement risk). |
| **Max of Sum:** Exposure with netting. | **Sum of Max:** Exposure with netting (NO: that’s without netting). |
| **Break Clause:** Exercised at replacement value. | **Break Clause:** Exercised at Par value (NO). |

## 4. Directional Intuition
- **Number of Offsetting Trades $\uparrow \rightarrow$ Netting Benefit $\uparrow$:** The more balanced your "book" is (longs and shorts with the same guy), the safer you are.
- **Correlation $\uparrow \rightarrow$ Netting Benefit $\downarrow$:** If all your trades move in the same direction (all win together or all lose together), they can't protect each other.
- **Complexity of Master Agreement $\uparrow \rightarrow$ Operational Risk $\uparrow$:** The more "special rules" and clauses you add, the easier it is for a lawyer to find a loophole in court.

## 5. Ambiguity Traps (Anti-Decoder)
- **Netting vs. Set-off:** These are essentially the same thing in the FRM context—the right to combine multiple obligations into one.
- **The "Winner's Loss":** Remember that netting only helps if *you* are overall positive. If you are net negative, your exposure is always zero anyway.
- **Options and Netting:** Options are the "Enemy" of netting. This is a common exam trick. If a portfolio is 100% long options, the "Net exposure" = "Gross exposure."
- **Close-out Amount:** This is NOT just the MtM. It often includes unpaid amounts, interest, and costs of replacing the trade.
- **Walkaway Clauses:** These are now mostly illegal/discouraged. They allowed a solvent party to simply stop paying if the other party defaulted, even if they were net negative.
- **Bilateral vs. Multilateral:** 
    - **Bilateral** = 2 parties. 
    - **Multilateral** = 3+ parties (requires a Clearing House/CCP).
- **Herstatt Risk vs. Netting:** Netting reduces the gross size of the payments, so it *indirectly* reduces Herstatt risk, but its primary job is credit protection.
- **The ISDAs:** The industry standard master agreement that makes netting legally enforceable across borders.
- **The Banker's Paradox Logic:** Exercising a break clause is a "Negative Signal" to the market. If you quit, everyone else gets scared and quits too, causing the default you were afraid of.
- **Trade Compression:** Often compared to netting. Compression actually *deletes* the underlying trades, whereas netting just *maths* them together at the end.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
