# R79 — Liquidity Transfer Pricing

**Exam Priority:** 🟡 Medium (1-2 questions) (LTP)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.79.1` | **The LTP Goal:** To ensure that liquidity costs, benefits, and risks are properly reflected in the pricing of products and the performance measurement (remuneration) of business units. | `[OPS]` | If a department borrows money from the bank "vault," they should pay a fair "rent" for it. If they provide deposits, they should get a "credit" for it. |
| `P.79.2` | **Matched-Maturity Marginal Cost (Best Practice):** The gold standard for LTP. It attributes funding rates based on the *marginal cost of funds* matched to the product maturity. Historically referenced to the LIBOR/swap curve; going forward, **SOFR (Secured Overnight Financing Rate)** is applied. | `[THE/OPS]` | You don't charge a 30-year mortgage and a 1-day loan the same interest rate. You look at the current market "Price List" for each time-bucket and charge accordingly. |
| `P.79.3` | **Contingent Liquidity Charge Formula:** The cost attributed to a business line for carrying a liquidity cushion (for potential drawdowns) is: `Probability of Drawdown * Cost of Liquidity Cushion`. | `[MTH/OPS]` | If you have a $10M line of credit, and there's a 50% chance the customer uses it, you charge the unit for $5M worth of "Emergency Cash" (the cushion). |
| `P.79.4` | **Zero-Cost & Average-Cost Failures:** Methods used pre-GFC. Zero-cost treats liquidity as free; Average-cost uses historical data. Both significantly underpriced liquidity for illiquid long-term assets and failed to credit liquidity providers. | `[THE]` | Average cost is like using last year's gas price to plan this year's road trip. You'll likely underestimate the cost and drive too much. |
| `P.79.5` | **Centralized Treasury Oversight:** The LTP process should be managed centrally to prevent business units from "arbitraging" internal rates. Decentralized structures with manual adjustments were identified as a major GFC failure. | `[OPS]` | If every department sets its own "Rent" price, they will just move money around to make themselves look profitable on paper without actually creating value. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank uses "Overnight Rates" to charge for "Long-term Assets":** This is a failure of Matched-Maturity. It makes long-term loans look artificially profitable and long-term funding look artificially expensive, leading to a massive maturity mismatch.
- **Variable Flip: If the cost of the "Liquidity Cushion" is only charged to Assets:** This is **Incorrect**. Liabilities also create liquidity risk (Runoff risk); LTP must capture the costs of both outflows and the benefits of stable funding.
- **Variable Flip: If a credit line has a 0% "Probability of Drawdown":** Then the contingent liquidity charge is zero. However, in stress tests, regulators assume drawdowns WILL occur, making the "0%" assumption unrealistic for a prudent bank.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Matched-Maturity Marginal Cost:** Best practice for LTP. | **Historical Average Cost:** Lags market rates; significantly underprices illiquid long-term assets. |
| **Probability-weighted Charge:** For contingent liquidity. | **Total Line Charge:** (NO: you weight it by the probability or the stressed drawdown rate). |
| **New Benchmark:** SOFR (Secured Overnight Financing Rate). | **Old Benchmark:** LIBOR. |
| **Group Treasury:** Centralized management of LTP. | **Business Unit Treasuries:** Decentralized (leads to internal arbitrage and manual errors). |

## 4. Directional Intuition
- **Liquidity Cushion Cost $\uparrow \rightarrow$ Contingent Charge Rate $\uparrow \rightarrow$ BU Profit $\downarrow$:** As it becomes more expensive for the bank to hold "Emergency Cash" (HQLA), the departments using those buffers become less profitable.
- **Probability of Drawdown $\uparrow$ (e.g., in a crisis) $\rightarrow$ Contingent Liquidity Needs $\uparrow$:** When customers are scared, they draw on their lines. The bank must charge more to cover the increased likelihood of needing that cash.
- **Maturity $\uparrow \rightarrow$ Maturity Premium $\uparrow \rightarrow$ LTP Funding Cost $\uparrow$:** It's always more expensive to borrow for 10 years than for 1 day; LTP captures this "Term Premium."

- **The "Winner":** When asked for the best LTP method, pick **Matched-Maturity Marginal Cost**.
- **Margin Calls:** Prior to the GFC, the liquidity cost of potential margin calls in trading books was *never priced* into the LTP process, which was a fatal flaw.
- **The Calculation:**
    - Level = `(Total Line) * (Prob of Drawdown) * (Cushion Cost)`.
    - **Trap:** They might use the *total* line, not just the *undrawn* part, to reflect the cost of the whole service/commitment (depends on specific bank methodology).
- **Remuneration (Moral Hazard):** Should bankers be paid based on profits *before* or *after* LTP charges? **AFTER.** Tying bonuses to raw profit without subtracting LTP funding costs rewards extreme risk-taking (funding illiquid assets with overnight cash).
- **Internal Arbitrage:** What prevents it? **Centralized Group Treasury** doing granular Liquidity Management Information Systems (LMIS) reporting.
- **Average Cost:** Why is it bad? Because it's **Backward-looking**, significantly underprices liquidity for illiquid assets, and ignores contingent liquidity risks of specific business units.

## 5. Ambiguity Traps (Anti-Decoder)
- **FTP != Market Rate:** FTP is an internally set transfer rate, not an external market rate. It should reflect the bank's marginal cost of funds for a specific tenor, not the SOFR/LIBOR rate directly.
- **Behavioral vs. Contractual Maturity:** Demand deposits are contractually overnight but behaviorally multi-year. FTP should use the behavioral maturity, or the bank will undervalue deposit funding.
- **Profit Center Trap:** If a branch shows high profit in the FTP system, it may just mean FTP credits are set too generously -- not that the branch is genuinely profitable. FTP distortions create illusory performance.
- **Liquidity Premium in FTP:** FTP should include a liquidity premium component for illiquid assets. If it doesn't, business units will originate long-dated illiquid loans because they appear cheap to fund internally.

## 5. Ambiguity Traps (Anti-Decoder)
- **FTP != Market Rate:** FTP is an internally set transfer rate, not an external market rate. It should reflect the bank's marginal cost of funds for a specific tenor, not the SOFR/LIBOR rate directly.
- **Behavioral vs. Contractual Maturity:** Demand deposits are contractually overnight but behaviorally multi-year. FTP should use the behavioral maturity, or the bank will undervalue deposit funding.
- **Profit Center Trap:** If a branch shows high profit in the FTP system, it may just mean FTP credits are set too generously -- not that the branch is genuinely profitable. FTP distortions create illusory performance.
- **Liquidity Premium in FTP:** FTP should include a liquidity premium component for illiquid assets. If it doesn't, business units will originate long-dated illiquid loans because they appear cheap to fund internally.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
