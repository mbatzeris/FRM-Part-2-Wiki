# R70 — Liquidity and Reserves Management: Strategies and Policies

**Exam Priority:** 🟡 Medium (1-2 questions): Strategies and Policies

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.70.1` | **Net Liquidity Position (L):** The fundamental liquidity equation: `Supply of Liquidity - Demand for Liquidity`. A negative value indicates a deficit that must be covered by borrowing or asset sales. | `[MTH]` | It’s your "Cash Flow" statement for the bank. If you have more money leaving (loans/withdrawals) than coming in (deposits/sales), you have a hole to fill. |
| `P.70.2` | **Asset vs. Liability Management:** Asset Management relies on selling liquid assets (Stored Liquidity); Liability Management relies on borrowing (Purchased Liquidity). | `[THE]` | Asset management is "Selling your jewelry to pay rent"; Liability management is "Taking out a new credit card to pay rent." |
| `P.70.3` | **Structure of Funds Method:** Liabilities are categorized into **Hot Money** (very volatile), **Vulnerable Funds**, and **Core Deposits** based on their probability of withdrawal. | `[OPS]` | You treat every dollar differently. You know your "Core" customers stay forever, but "Hot Money" investors will leave the second they find a better rate elsewhere. |
| `P.70.4` | **Expected Liquidity Requirement:** A probabilistic approach where the manager assigns probabilities to "Best," "Most Likely," and "Worst Case" liquidity scenarios to calculate an expected funding need. | `[MTH/OPS]` | Instead of guessing one number, you prepare for three futures and take the weighted average of the "Liquidity Holes" you might face. |
| `P.70.5` | **The Market Discipline Approach:** Using external signals like the bank's stock price, the interest premium on its CDs, and the frequency of central bank borrowing to gauge liquidity adequacy. | `[MKT/OPS]` | The market tells you if you're in trouble. If investors demand a "Risk Premium" just to lend you money, your liquidity position is already compromised in their eyes. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank's "Deposit Composition Ratio" (Demand/Time) increases:** Then the bank’s liquidity risk **increases**. Demand deposits can be withdrawn at any second (volatile); Time deposits (CDs) have set maturities and penalties for early exit (stable).
- **Variable Flip: If a bank uses "Asset Conversion" during a market-wide liquidity black hole:** Then the strategy fails. In a "Black Hole," the market price of even "liquid" assets drops, and transaction costs explode, making "Stored Liquidity" impossible to harvest fairly.
- **Variable Flip: If a bank relies purely on "Purchased Liquidity" (Liability Management) during a credit rating downgrade:** Then its funding costs will spike or its credit lines will be yanked. Dependency on borrowing is highly sensitive to the bank's own creditworthiness.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Hot Money Ratio:** Higher means more liquid assets relative to volatile liabilities (Good). | **Capacity Ratio:** Higher (Loans/Assets) means **LOWER** liquidity. |
| **Sources and Uses:** Based on $\Delta\text{Deposits}$ and $\Delta\text{Loans}$. | **Structure of Funds:** Based on the *type* of liability, not just the change in volume. |
| **Reverse Repo:** Represents an asset / supply of liquidity (Lending cash). | **Repo:** Represents a liability / demand for funds (Borrowing cash). |

## 4. Directional Intuition
- **Loan Demand $\uparrow \rightarrow$ Capacity Ratio $\uparrow \rightarrow$ Liquidity $\downarrow$:** As the bank ties up more cash in long-term loans, it has fewer "immediately spendable" resources left.
- **Economic Sluggishness $\uparrow \rightarrow$ Loan Demand $\downarrow \rightarrow$ Liquidity $\uparrow$:** When nobody wants to borrow, banks get "stuffed" with cash, often resulting in a liquidity surplus.
- **Central Bank Borrowing $\uparrow \rightarrow$ Market Confidence $\downarrow$:** Using the "Discount Window" frequently is a signal that private lenders don't trust the bank anymore.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Composition Ratio" Trap:** Which way is bad? **Higher Demand / Lower Time = BAD.** Demand is "Hot"; Time is "Cool."
- **Asset Management Cost:** Don't forget **Opportunity cost**. While you're holding a 0%-yield T-bill for liquidity, you're missing out on the 6%-yield loan you could have made.
- **Fed Funds:** If you are a **Net Seller** of Fed Funds, you have high liquidity (you are lending out your excess). If you are a **Net Buyer**, you have low liquidity (you are scrambling for cash).
- **Liability Reserve:** In the "Structure of Funds" method, do you hold reserves against loans too? **YES.** A smart manager holds "Liquidity Reserves" to fund the loans they expect to make in the future.
- **Brokered Deposits:** Higher "Deposit Brokerage Index" = **Lower Liquidity Quality.** Brokered deposits are "Mercenary Money" and will vanish instantly for a better rate.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
