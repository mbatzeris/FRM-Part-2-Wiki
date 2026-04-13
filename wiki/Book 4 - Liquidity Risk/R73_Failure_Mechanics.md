# R73 — The Failure Mechanics of Dealer Banks

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.73.1` | **The Dealer Bank Run:** Unlike a retail bank run (depositors at the window), a dealer bank run is a "Flight of Counterparties": Prime brokerage clients pulling cash, repo lenders refusing to roll, and derivate counterparties exiting positions. | `[THE/OPS]` | It’s a "Wholesale Run." The bank doesn't die because Grandma took her $1,000 out; it dies because Hedge Funds and other banks won't answer its phone calls. |
| `P.73.2` | **Novation Drain:** When a counterparty exits a derivative trade via **Novation** (transferring the trade to a third party), it often forces the original dealer to settle collateral or pay out cash, accelerating the liquidity collapse. | `[OPS]` | A novation is a "Legal Exit." Every time a counterparty "Novates" away from a shaky bank, they are taking their collateral with them, leaving the bank with an empty vault. |
| `P.73.3` | **PPIP and Adverse Selection:** The Public-Private Investment Program (TARP) was designed to combat **Adverse Selection** in "toxic" assets by subsidizing bidders and absorbing losses above a pre-set level. | `[REG/ECO]` | Buyers are afraid of "Lemons" (Toxic Assets). The government acts as a "Warranty Provider" to convince investors to start buying again and clear the bank's balance sheet. |
| `P.73.4` | **Central Clearing as a Solution:** Moving OTC derivatives to a Central Counterparty (CCP) reduces the risk of a "run" because the counterparties are exposed to the CCP, not the individual dealer bank. | `[REG/OPS]` | If you trade through a "Middleman" (CCP), you don't care if the original dealer bank is dying, as long as the Middleman is safe. Note: Only works for **Standardized** contracts. |
| `P.73.5` | **The "Final Collapse" Trigger:** The terminal stage of a dealer bank failure is the **loss of cash settlement privileges** with its tri-party clearing banks. | `[OPS]` | If the clearing bank stops processing your payments, you can't settle anything. You are effectively "disconnected" from the global financial grid. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a dealer bank has 100% "Committed" repo lines:** Then it is much safer from a "Run on Repo." Most dealer banks rely on **Overnight Uncommitted** repo, which clearing banks can refuse to roll over at any second without legal penalty.
- **Variable Flip: If all OTC derivatives were "Bespoke/Non-standardized":** Then **Central Clearing** would be impossible to implement. Central clearing requires standardized terms to allow the CCP to manage and net the risk.
- **Variable Flip: If a bank is "Too-Big-To-Fail":** The government might provide a **Bridge Bank** to ensure an orderly unwind. This prevents a "Fire Sale" that would destroy the valuations of other banks' assets (Systemic Spillover).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Novation:** Accelerates the liquidity crisis. | **Diversification:** Is used to *reduce* risk, not as a crisis exit mechanism. |
| **Adverse Selection:** Buyers demand deep discounts due to "Information Asymmetry." | **Moral Hazard:** Is about taking more risk because you are insured (distinct from adverse selection). |
| **Tri-party Repo:** Clearing banks (like JPM/BNY) have the "discretion" to kill a dealer. | **Bilateral Repo:** Is directly between two peers (less systemic clearing risk). |

## 4. Directional Intuition
- **Solvency Rumors $\uparrow \rightarrow$ Prime Brokerage Withdrawals $\uparrow \rightarrow$ Dealer Cash $\downarrow \downarrow$:** The reaction is non-linear and near-instant.
- **Collateral Haircuts $\uparrow \rightarrow$ Repo Funding $\downarrow \rightarrow$ Asset Sales $\uparrow$:** Higher haircuts force the bank to sell assets to raise the missing cash, which drives prices down further (The Death Spiral).
- **Toxic Asset Subsidies (PPIP) $\uparrow \rightarrow$ Market Liquidity $\uparrow$:** By floor-protecting losses, the government "restarts" the engine of the frozen asset markets.

## 5. Ambiguity Traps (Anti-Decoder)
- **Novation Trap:** Does a novation *help* a dealer bank? **NO.** It often drains their liquidity as they lose the offset and must post more collateral elsewhere.
- **TARP Objective:** Was TARP designed to "Force the sale" of assets to find their true value? **NO.** It was designed to **Mitigate Adverse Selection** and provide a floor for prices.
- **TBTF Bridge Bank:** Is a bridge bank for small local banks? **NO.** It's a resolution tool for **Large Dealer Banks** (Systemic).
- **The "Scope" of Clearing:** Does central clearing fix everything? **NO.** It only works for **Standardized** contracts, leaving bespoke trades as a source of "Run" risk.
- **The "Death" of a dealer:** Is it usually an "Equity" failure? **NO.** It is almost always a **Liquidity** failure (inability to settle cash).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
