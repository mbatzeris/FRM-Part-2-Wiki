# R77 — Managing Nondeposit Liabilities

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.77.1` | **Nondeposit Diversity:** Modern banks rely on a mix of Fed Funds (overnight), Repos (collateralized), Discount Window (emergency), and Commercial Paper (large firms) to fill funding gaps. | `[THE/OPS]` | If your "Checking Account" (Deposits) isn't enough to fund your "Shopping Spree" (Loans), you tap your "Credit Lines" (Nondeposit liabilities). |
| `P.77.2` | **Available Funds Gap (AFG):** The amount of nondeposit funding a bank needs to raise in a given period: `(Projected Loans + Investments) - (Expected Deposits + Inflows)`. | `[MTH]` | It’s the "Funding Hole." If you plan to lend $100M but only expect $40M in deposits, your AFG is $60M. |
| `P.77.3` | **The Pooled Funds Approach:** A forward-looking costing method where the bank calculates a **Hurdle Rate** that earning assets must exceed to cover the total costs of all newly raised funds. | `[MTH/ECO]` | You calculate the "All-in Cost." If it costs you 5% to raise new money (including overhead), you must lend it out at >5% just to break even (the Hurdle Rate). |
| `P.77.4` | **Fed Funds — The Immediate Fix:** Fed funds are the most appropriate source for immediate, smaller denomination funding needs (under $1M) for medium-sized banks that lack CP or Eurodollar market access. | `[OPS]` | It’s the bank's "Emergency Cash." It's fast, flexible, and you don't need to be a giant global bank to use it. |
| `P.77.5` | **Negotiable (Jumbo) CDs:** Large-denomination ($100k+) certificates of deposit that are legally deposits but functionally act as money-market instruments used to tap wholesale funding. | `[REG/MKT]` | These are "Mercenary Deposits." They aren't from local families; they are from treasurers and fund managers looking for the best overnight rate. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank needs $800,000 immediately but only has access to "Commercial Paper":** CP usually requires $1M+ denominations and a high credit rating/market presence. For an $800k "Now" need, **Fed Funds** is the correct choice.
- **Variable Flip: If the AFG calculation ignores expected "Drawdowns" on credit lines:** Then the projected "Hole" will be too small. AFG must include both new loans *and* expected usage of existing commitments (Outflows).
- **Variable Flip: If a Hurdle Rate is calculated using "Total Raised Funds" instead of "Earning Assets":** Then the rate will be too low. You must divide the cost by the dollars actually **invested** to ensure the earning assets cover the cost of the "Non-earning" reserves.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Available Funds Gap:** (Loans - Deposits). | **Maturity Gap:** (Assets - Liabilities) in a time bucket. |
| **Pooled Funds Approach:** Forward-looking / Hurdle rate. | **Historical Average Cost:** Backward-looking / Accounting view. |
| **Fed Funds:** Small banks / Immediate / Overnight. | **Eurodollars:** Global banks / Large size / Multiple days. |

## 4. Directional Intuition
- **Loan Demand $\uparrow \rightarrow$ Available Funds Gap $\uparrow \rightarrow$ Nondeposit Funding Need $\uparrow$:** The more aggressive your lending program, the more you have to "Buy" money from the market.
- **Reserve Requirements $\uparrow \rightarrow$ Dollars Invested $\downarrow \rightarrow$ Hurdle Rate $\uparrow$:** If the regulator forces you to keep more cash sitting idle, your active loans have to "Work Harder" to pay the bills.
- **Credit Rating $\downarrow \rightarrow$ Commercial Paper Access $\downarrow \rightarrow$ Dependency on Fed Funds/Repo $\uparrow$:** When you lose access to the "Elite" markets, you fall back on the most basic (and often more expensive) funding sources.

## 5. Ambiguity Traps (Anti-Decoder)
- **Repo vs. Discount Window:** Both need collateral, but Repo is **Market-based**; Discount Window is **Fed-based**.
- **Jumbo CDs:** Are they deposits? **Yes** (legally). Are they core? **No** (they are volatile money-market funds).
- **Hurdle Rate denominator:** Always divide by the money you **actually lent** ($250M), not the money you **raised** ($300M).
- **Available Funds Gap Math:** Be careful with the signs. `(Loans - Deposits)`. A positive gap means you need to *find* money.
- **FHLB:** Who uses it? **Mortgage Lenders**. Why? It was built to stabilize the housing market.
- **Breakeven Cost:** The rate you need just to cover your costs before paying shareholders a single cent.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
