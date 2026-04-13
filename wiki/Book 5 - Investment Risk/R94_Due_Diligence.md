# R94 — Due Diligence

**Exam Priority:** 🟡 Medium (1-2 questions) on Managers and Funds

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.94.1` | **The Pillars of Due Diligence:** Evaluation focuses on four pillars: Strategy (evolution and risk), Ownership (who is in control), Track Record (relative to peers), and Investment Management (key person risk). | `[OPS]` | You're checking the "Driver," the "Engine," the "Past Races," and who actually "Owns the Car." |
| `P.94.2` | **Operational Due Diligence (ODD):** Focuses on the "Plumbing" of the fund—internal controls, compliance, and service providers (Prime Brokers, Administrators). Many fund failures are due to operational breakdowns, not investment skill. | `[OPS/REG]` | The fund might be a great stock picker, but if the back office can't track the cash or if the compliance officer is the manager's cousin, you have a problem. |
| `P.94.3` | **Independent Valuation:** The most critical control for illiquid assets. Valuation must be performed by an independent third party (like an administrator) to prevent managers from "smoothing" returns or hiding losses to keep fees high. | `[OPS/MKT]` | You don't let the student grade their own homework. An outside teacher (Independent Auditor) must mark the score. |
| `P.94.4` | **Business Model Risk:** A fund must have enough AUM to reach its "Break-even" point. If expenses exceed fee income, the manager may take desperate risks or close the shop unexpectedly. | `[OPS/ECO]` | If it costs $1M to run the office but the 2% fee only brings in $500k, the manager is slowly going broke. Desperate people make bad investment decisions. |
| `P.94.5` | **The DDQ (Due Diligence Questionnaire):** A standard tool to gather facts on AML policy, insurance, and disaster recovery. Note: Detailed **Performance Attribution** is usually a separate deep-dive, not a standard DDQ checkbox. | `[OPS/REG]` | The DDQ is the "Standard Form" you fill out at the doctor's office. The "Blood Test" (Attribution) comes later if they find something interesting. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a manager shows "Unreasonably Steady" high returns:** This is a major **Fraud Red Flag**. Real markets are volatile; perfectly smooth lines (like Madoff) suggest the numbers are being fabricated or smoothed.
- **Variable Flip: If a fund has "Stale Prices" on its assets:** Its measured volatility and correlation will be **Biased Downward**. This makes the fund look safer than it is, potentially hiding a "liquidity trap."
- **Variable Flip: If a fund’s decision-making is "Committee-style" but dominated by one person:** This is a **Governance Failure**. The committee is just "window dressing" to hide a dominant personality who might ignore risk warnings.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Independent Valuation:** Required for illiquid assets. | **Internal Valuation:** Safer for proprietary strategies (NO: internal is high risk). |
| **Track Record:** Should be independently verified. | **Track Record:** Should focus on absolute returns (NO: relative returns are better). |
| **Business Model Risk:** Focuses on fund break-even AUM. | **Business Model Risk:** Focuses on stock picking skill (NO: focus is on firm survival). |

## 4. Directional Intuition
- **Transparency $\downarrow \rightarrow$ Fraud Risk $\uparrow$:** If the manager won't show you the books or the service providers, they are hiding something.
- **AUM $\rightarrow$ Break-even Point $\rightarrow$ Manager Stability $\uparrow$:** Once the fund is "In the Black," the manager can focus on long-term strategy rather than short-term survival.
- **Service Provider Independence $\uparrow \rightarrow$ Operational Risk $\downarrow$:** Top-tier prime brokers and auditors provide a "Stamp of Approval" that the fund's assets actually exist.

## 5. Ambiguity Traps (Anti-Decoder)
- **DDQ Content:** Does a DDQ include "Attribution Analysis"? **No, usually not.** It includes AML, Insurance, and Business Continuity.
- **Alpha vs. Returns:** Don't focus on **Absolute Returns**. Focus on **Relative Returns** (v. Peers) and **Verification** by a third party.
- **Operational Failures:** Are they common? **YES.** More funds fail due to back-office errors or fraud than purely bad stock picking.
- **Key Person Risk:** What happens if the lead manager gets hit by a bus? Succession planning is a vital part of due diligence.
- **Related-Party Transactions:** If the fund buys a building from the manager’s wife, that’s a **Conflict of Interest** red flag.
- **Style Drift:** If a "Low Vol" fund suddenly starts buying "Crypto," that's a breach of trust (Style Drift).
- **Lock-up vs. Strategy:** Does the fund let you out in 30 days but holds assets that take 2 years to sell? This is a **Liquidity Mismatch** trap.
- **Succession Planning:** Is there a plan for when the founder retires? (Business Model Risk).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
