# R81 — Covered Interest Parity Lost

**Exam Priority:** 🟡 Medium (1-2 questions) Covered Interest Parity Lost

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.81.1` | **Covered Interest Parity (CIP):** The classic no-arbitrage condition where the forward exchange rate is determined solely by the interest rate differential. $F = S \times \frac{1+r_{usd}}{1+r_{fc}}$. | `[THE/MTH]` | It’s the "Law of One Price" for money. You shouldn't be able to make a risk-free profit by borrowing in one currency, swapping to another, and hedging back. |
| `P.81.2` | **The Cross-Currency Basis (b):** The "Error Term" in the CIP equation post-2008. It represents the *extra* cost of borrowing USD via a swap. `USD_Rate + Basis`. | `[MTH/MKT]` | It’s a "USD Premium." Everyone wants Dollars so badly through the swap market that they are willing to pay more than the traditional interest rate differential would suggest. |
| `P.81.3` | **FX Swap vs. Cross-Currency Swap:** FX swaps are short-term (<1yr) and use the **Forward Rate** at maturity. Cross-currency swaps are long-term (>1yr) and use the **Original Spot Rate** at maturity with periodic interest exchanges. | `[THE/OPS]` | FX Swaps are for "Quick Cash"; Cross-Currency Swaps are for "Long-Term Funding." They use different exit prices (Forward vs Spot) to handle the different time horizons. |
| `P.81.4` | **Demand Drivers (Why Basis Opens):** Hedging pressure from three main sources: (1) Banks managing currency gaps, (2) Insurers/Pensions hedging foreign assets, and (3) US firms issuing cheap foreign debt ("Reverse Yankees") and swapping to USD. | `[ECO/MKT]` | Everyone is trying to "Buy USD Protection" at the same time. This one-sided demand pushes the price (the basis) away from its fair value. |
| `P.81.5` | **Limits to Arbitrage (Why Basis Stays Open):** Post-crisis regulations (like Basel III Leverage Ratios) make expanding the balance sheet expensive. Arbitrage requires taking on debt and assets, which consumes scarce capital. | `[REG/ECO]` | In the old days, banks would "Close the Gap" to make a quick buck. Now, the regulator charges so much for "Balance Sheet Space" that the profit from the gap isn't worth the capital cost of the trade. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Cross-Currency Basis (b) is Zero:** Then **Covered Interest Parity holds**. There is no "Premium" for borrowing USD through swaps, and the forward rate is perfectly predicted by interest rates.
- **Variable Flip: If a USD-payer in a swap pays `USD_Rate - Basis`:** This would mean the USD is at a **Discount**, not a premium. Since the GFC, the USD has consistently commanded a **Premium** (positive basis).
- **Variable Flip: If regulators lowered capital requirements for FX arbitrage:** Then the basis would likely **Shrink**. More banks could enter the trade without a heavy capital penalty, "Arbitraging away" the violation and returning the market to CIP.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Cross-Currency Basis (b):** The amount the USD rate is *adjusted* to satisfy the identity. | **Forward Points:** (F - S). These are a part of the identity, but not the "Basis" itself. |
| **XCCY Swap Maturity:** Original Spot Rate. | **FX Swap Maturity:** Forward Rate. |
| **USD Premium:** Basis is positive (Payer pays USD_Rate + b). | **USD Discount:** Basis is negative. |

## 4. Directional Intuition
- **Hedging Demand for USD $\uparrow \rightarrow$ Basis (b) $\uparrow$:** The more people "Panic Buy" USD through the swap market, the higher the "Tax" (Basis) becomes.
- **Bank Capital Scarcity $\uparrow \rightarrow$ Limits to Arbitrage $\uparrow \rightarrow$ CIP Violation Persistence $\uparrow$:** If banks are "Balance Sheet Constrained," the basis can stay irrational for a long time.
- **Counterparty Risk $\uparrow \rightarrow$ Transaction Costs $\uparrow \rightarrow$ Basis $\uparrow$:** The more dangerous the trade, the more "Profit" (the deviation from CIP) the arbitrageur needs to justify the risk.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Forward" vs. "Spot" exit:** 
    - Short-term (FX Swap) = **Forward Rate**. 
    - Long-term (XCCY Swap) = **Original Spot**.
- **The Basis Side:** Does the EUR payer pay the basis? **NO.** In the standard notation, the **USD Payer** pays the `USD_Rate + Basis`. The foreign currency payer often pays the `FC_Rate` (sometimes with the basis subtracted).
- **Why it won't close:** Is it just because banks are mean? **NO.** It’s because of **Limits to Arbitrage** (Capital costs and Regulation).
- **Reverse Yankees:** Why do US firms issue debt in EUR? Because the EUR credit spreads are narrow. Then they swap to USD, contributing to the demand that keeps the basis alive.
- **CIP Formula:** Keep the currencies in original units ($F$ and $S$ as USD/FC) to avoid flipping errors.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
