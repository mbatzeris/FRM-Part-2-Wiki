# R75 — Liquidity Risk Reporting and Stress Testing

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.75.1` | **The 1-Day Tenor Rule:** Regulators (e.g., FSA UK) treat all **Callable and Demand Deposits** as having a 1-day tenor, meaning they are assumed to potentially leave the bank in exactly one day. | `[REG]` | Regulators are pessimistic. They assume that if a customer *can* take their money out today, they *will* if things look even slightly bad. |
| `P.75.2` | **The Cash Flow Survival Report:** The most critical stress test for senior management. it tracks the bank's survival horizon by comparing **BAU (Business as Usual)** cash flows against **Adjusted** flows (post-mitigation like asset sales). | `[OPS]` | It’s the "Survival Clock." It tells management: "Without help, we die in 8 days. If we sell the furniture and use our credit lines, we can last 21 days." |
| `P.75.3` | **Reporting Frequency (FSA):** Market-wide stress results are reported **Daily**, while Firm-specific (Idiosyncratic) results are reported **Weekly**. | `[REG/OPS]` | When the whole market is on fire, the regulator wants a status update every morning. When only your bank is on fire, a weekly check-in is the baseline (though usually more frequent in reality). |
| `P.75.4` | **Wholesale Pricing & Volume Report:** A key regulatory tool that compares a bank's own yield curve to its peers' to identify outliers that might be struggling to raise funds at market rates. | `[MKT/REG]` | It’s a "Fever Chart." If everyone else borrows at 3% but you're paying 6%, the regulator knows you're "Sick" before you even tell them. |
| `P.75.5` | **Liability Stickiness (OBF):** Observed Behavioral Forecasting (OBF) metrics are used to estimate the "Stickiness" (resistance to runoff) of different funding sources like corporate or government deposits. | `[THE/MTH]` | "Stickiness" is the opposite of "Hot Money." It measures how loyal (or lazy) your depositors are when the market gets volatile. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank includes "Derivatives Market Value" in its liquidity ratio:** This is generally **Incorrect**. Per FSA guidelines, only **coupons receivable/payable** on their specific pay dates are included. The volatile "Market Value" is too noisy for liquidity ratios.
- **Variable Flip: If a bank's "Survival Horizon" is 21 days after adjustments:** Then the bank **fails** the Basel III 30-day LCR requirement. Mitigation must extend the horizon beyond **30 days** to be regulatory compliant.
- **Variable Flip: If "Undrawn Commitments" are ignored in LST:** Then the report is dangerously incomplete. Regulators require undrawn lines to be included as potential **outflows**, as customers are most likely to draw them down exactly when the bank is stressed.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Demand Deposits:** 1-day tenor assumption. | **Demand Deposits:** Assumed maturity of 1 month or longer. |
| **Wholesale Yield Curve Peer Comparison:** Regulators' early warning tool. | **Bank's Credit Rating:** Important, but peer curve comparison is a faster "market signal." |
| **Weekly Reporting:** For firm-specific stress. | **Daily Reporting:** For firm-specific stress (NO: that's for market-wide). |

## 4. Directional Intuition
- **Market-Wide Stress $\uparrow \rightarrow$ Reporting Frequency $\uparrow \rightarrow$ Daily:** In a systemic crisis, the "Granularity" of time becomes the most important factor.
- **Peer Yield Curve Divergence $\uparrow \rightarrow$ Regulatory Scrutiny $\uparrow$:** The more "Expensive" your money becomes compared to your neighbors, the more the regulator will worry you're hiding a solvency problem.
- **Mitigating Actions (Asset Sales) $\uparrow \rightarrow$ Survival Horizon $\uparrow$:** The bank’s "Burn Rate" slows down as it converts its HQLA buffer into immediate cash.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "30-Day" Target:** Always check if the "Adjusted Survival Horizon" hits the **30-day** mark. if it’s 21, it’s a fail.
- **Derivatives in Ratios:** Remember: **NO** to market value; **YES** to coupons/cash flows on their dates.
- **Market vs. Firm Specific:**
    - Market Fire = **Daily**. 
    - Firm Fire = **Weekly**.
- **Demand Deposits:** Maturity is NOT technical maturity; for liquidity purposes, it is **1 day**.
- **Wholesale Pricing:** Why do regulators look at it? To find the "Weakest Link" in the peer group by looking at who is paying a premium for cash.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
