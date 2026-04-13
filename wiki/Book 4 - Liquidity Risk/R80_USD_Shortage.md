# R80 — The US Dollar Shortage in Global Banking

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.80.1` | **The USD Funding Gap:** Occurs when a non-US bank has more long-term USD assets than long-term USD liabilities. This exposes the bank to the risk that it cannot "roll over" its short-term USD funding (Interbank or FX Swaps). | `[THE/MKT]` | If you buy a 30-year US mortgage but pay for it by borrowing USD for only 1 day at a time, you have a massive "Gap." If the lender says "No" tomorrow, you're stuck. |
| `P.80.2` | **Implicit Funding via FX Swaps:** Banks often fund USD assets by borrowing their home currency (e.g., EUR) and swapping it for USD in the FX swap market. During the GFC, this market "Broke," creating the USD shortage. | `[MKT/ECO]` | You can't find a direct USD loan, so you take a EUR loan and "Trade" for USD. But if no one wants your EUR anymore, you can't get the USD you need to stay alive. |
| `P.80.3` | **Upper vs. Lower Bound of the Gap:** If USD liabilities are short-term, the gap's **Upper Bound** is the *Gross* position to nonbanks; if liabilities are long-term (stable), the **Lower Bound** is the *Net* position. | `[MTH]` | The "Gross" number is the disaster scenario (everyone leaves); the "Net" number is the more stable reality (only the gap itself needs rolling). |
| `P.80.4` | **Factor of the Shortage (2008):** Key contributors were the drawing of prearranged credit commitments by customers and the "re-boarding" of off-balance sheet vehicles (SIVs) back onto the bank's own books. | `[OPS]` | The bank's "Basement" (Off-balance sheet) flooded, and it had to bring all that wet furniture (toxic assets) back up into the main living room (the Balance Sheet). |
| `P.80.5` | **The Fed as Global Lender of Last Resort:** Through **Unlimited Swap Lines**, the Fed provided USD to foreign central banks (collateralized by their local currencies), which then auctioned the USD to their local banks. | `[REG/POL]` | The world ran out of "Fuel" (USD). The Fed, as the only "Refinery" in the world, piped unlimited fuel to other countries to keep the global engine from seizing up. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Fed’s Swap Lines were "Uncollateralized":** Then the Fed would have faced massive counterparty credit risk. In reality, the lines were **Collateralized** by the foreign central bank's currency, protecting the US taxpayer.
- **Variable Flip: If a European bank has perfectly matched USD assets and USD liabilities (Maturity & Amount):** Then its USD Funding Gap is **Zero**. It has no need to roll over short-term funds or use the FX swap market, making it immune to a USD shortage.
- **Variable Flip: If foreign central banks could print USD themselves:** Then the USD shortage wouldn't have happened. Only the **Federal Reserve** has the power to create US Dollars; foreign central banks can only create their own domestic currency.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Upper Bound:** Gross USD position (Short-term liabilities). | **Upper Bound:** Net USD position (No: that's the lower bound). |
| **FX Swap:** Borrowing base currency $\rightarrow$ Swapping for USD. | **Spot Trade:** Simple currency exchange without a forward agreement. |
| **Fed Swap Lines:** Mitigate interbank rate volatility. | **Fed Swap Lines:** Increase moral hazard (NO: they are collateralized). |

## 4. Directional Intuition
- **Market Panic $\uparrow \rightarrow$ FX Swap counterparty trust $\downarrow \rightarrow$ USD Funding Gap Risk $\uparrow$:** When banks stop trusting each other, the "Synthetic" way to get USD (Swaps) is the first to fail.
- **USD Asset Write-downs $\uparrow \rightarrow$ Maturing Assets $\downarrow \rightarrow$ Funding Gap (Underestimation) $\uparrow$:** If you think your assets are worth $100 but they are only worth $80, you have a bigger "Survival" problem than the numbers suggest.
- **Fed Swap Line Extension $\uparrow \rightarrow$ USD Appreciation Pressure $\downarrow$:** By providing USD directly, the Fed reduced the "Desperation Buying" of Dollars that was driving the USD price to extreme levels.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Unlimited" Trap:** Were the swap lines limited? Originally yes, but in late 2008 for major central banks, they became **Unlimited**.
- **Credit Risk:** Does the Fed take credit risk on the foreign *commercial* banks? **NO.** The Fed only deals with the foreign *Central Bank*. The Central Bank takes the risk on its local commercial banks.
- **FX Swap vs. Interbank:** Is an FX swap a loan? **Functionally yes**, but legally it’s two exchange contracts (Spot + Forward).
- **The "Non-Fed" Central Banks:** Can the ECB fix a USD shortage on its own? **NO.** It can only swap its EUR for USD *with* the Fed or use its limited reserves. It cannot print USD.
- **Gap Bounds:** 
    - Short-term liabilities = **Gross** (Upper).
    - Long-term liabilities = **Net** (Lower).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
