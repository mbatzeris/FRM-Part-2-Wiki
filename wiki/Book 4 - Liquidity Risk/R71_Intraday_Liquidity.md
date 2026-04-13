# R71 — Intraday Liquidity

**Exam Priority:** 🟡 Medium (1-2 questions) Risk Management

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.71.1` | **Intraday Liquidity Purpose:** The primary and most significant use of intraday liquidity is managing **Outgoing Wire Transfers** to ensure timely settlement of obligations throughout the operating day. | `[OPS]` | It’s about the "Plumbing." A bank needs cash flowing through the pipes every second to pay its customers' bills, even if those customers haven't paid them back yet today. |
| `P.71.2` | **The Systemic Risk Metric:** A bank's contribution to systemic risk is best measured by its **Intraday Credit relative to Tier 1 Capital**. | `[THE/REG]` | If your intraday "Credit Tab" is huge compared to your actual equity (Tier 1), your failure during the business day could freeze the entire global payment system. |
| `P.71.3` | **Cost of Intraday Credit:** Intraday credit can have **Explicit Costs** (interest charged by the clearing bank) or **Implicit/Opportunity Costs** (the need to pledge high-quality collateral to secure the line). | `[ECO]` | Nothing is free. Either you pay rent for the cash (Interest) or you lock up your best assets as a security deposit (Collateral), preventing you from using them for anything else. |
| `P.71.4` | **Governance and 3LoD:** Intraday liquidity should be managed via the Three Lines of Defense, with the **Second Line (Corporate Risk Management)** providing the necessary expertise and "Effective Challenge" to the First Line (Treasury). | `[OPS]` | Treasury wants to move money fast; Risk Management wants to make sure there's enough gas in the tank. The Second Line acts as the "Brake" and "Auditor" of the Treasury's speed. |
| `P.71.5` | **Daily Maximum Usage:** A backwards-looking metric that takes the "Most Negative" balance during the day and divides it by the total credit limit. It helps banks size their needed intraday cushions. | `[MTH/OPS]` | It’s the "Deepest Point" in your account during the day. If you regularly dip to 90% of your limit at 11:00 AM, you need a bigger limit or better-timed incoming flows. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank relies purely on "Incoming Funds" to pay its "Outgoing Wires":** Then the bank is exposed to extreme **Settlement Risk**. If one customer is late with a payment, the bank won't be able to pay its own bills, potentially triggering a cascade of defaults.
- **Variable Flip: If a bank has no "Uncommitted" intraday credit lines:** Then its liquidity is more certain. "Uncommitted" lines are the first to be yanked in a crisis, making a bank that relies on them extremely vulnerable to sudden withdrawal.
- **Variable Flip: If an FMU (Financial Market Utility) has no deadlines for payments:** Then there would be no "Time-sensitive" obligation risk. In reality, FMUs have strict windows; missing a window results in penalties and reputational "Noise."

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Systemic Risk:** Intraday Credit / Tier 1 Capital. | **Systemic Risk:** Total Assets or Number of Customers. |
| **Nostro account:** A foreign currency account held at another bank to facilitate intraday transfers. | **Vostro account:** The account your peers hold *with you*. |
| **Explicit Cost:** Interest on the intraday line. | **Implicit Cost:** Credit quality of the bank's own HQLA (usually noise as HQLA quality is high). |

## 4. Directional Intuition
- **Payment Throughput Speed $\uparrow \rightarrow$ Intraday Liquidity Need $\downarrow$:** The faster you can circulate money (sending out only after receiving in), the less "Static Cash" you need to keep in your accounts.
- **FMU Deadlines $\uparrow$ (Strictness) $\rightarrow$ Settlement Risk $\uparrow \rightarrow$ Intraday Cushion $\uparrow$:** When the "Penalty" for being a minute late increases, banks hold more cash to ensure they never miss a slot.
- **Tier 1 Capital $\downarrow \rightarrow$ Intraday Coverage Ratio $\uparrow \rightarrow$ Systemic Danger $\uparrow$:** As a bank’s equity erodes, its ability to support its own daily settlement activities becomes more precarious for the whole market.

## 5. Ambiguity Traps (Anti-Decoder)
- **Outgoing Wires vs. Deposits:** Which is the bigger intraday liquidity user? **Outgoing Wires.** Deposits are a source/use at the end of the day; Wires are the core business *during* the day.
- **Is IT a Line of Defense?** **NO.** IT supports the process, but the "Lines" are Treasury (1st), Risk Mgt (2nd), and Audit (3rd).
- **The "Real-Time" Myth:** Does "monitoring maximum usage" require real-time data? **NO.** It can be done at the end of the day by looking back at the day's transaction log.
- **Explicit vs. Implicit:** If the clearing bank doesn't charge interest, is the intraday credit free? **NO.** You likely had to pledge collateral, which has an **Opportunity Cost**.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
