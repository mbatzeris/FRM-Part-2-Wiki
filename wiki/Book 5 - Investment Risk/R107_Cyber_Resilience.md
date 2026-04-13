# R107 — Cyber Threats and Digital Resilience

**Exam Priority:** 🔴 High (3-4 questions)ats and Digital Resilience

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.107.1` | **The CIA Triad:** Cyber risk is defined by the loss of **Confidentiality** (Privacy), **Integrity** (Accuracy), or **Availability** (Access) of data/systems due to an attack. | `[OPS/THE]` | It’s the "Lock and Key" of data. Is it a secret (C)? Is the number right (I)? Can you use it (A)? If any one fails, the system is compromised. |
| `P.107.2` | **The Integrity/Availability Priority:** From a financial stability perspective, shocks to **Integrity** (e.g., balances being changed) and **Availability** (e.g., ATM network down) are far more dangerous than shocks to **Confidentiality**. | `[MKT/ECO]` | If someone sees your balance (C), it’s bad. If someone deletes your balance (I) or prevents you from withdrawing it (A), it’s a systemic panic. |
| `P.107.3` | **Cyber vs. ICT Risk:** Cyber risk comes from **Malicious Attacks**. ICT risk comes from **System Failures** (like a server crashing on its own). Cloud computing has reduced "Attack" risk for individual banks but increased the risk of a "Global Outage" (ICT risk). | `[OPS/REG]` | Cyber is a "Burglar." ICT is a "Broken Pipe." Both can flood your house, but you fight them with different tools. |
| `P.107.4` | **Multicloud Systems:** All major banks use multiclouds to manage concentration risk (spreading assets over multiple providers). However, this creates an unintended risk: **weaker stewardship** over distributed computing processes. | `[OPS/THE]` | If you split your gold between three vaults, a thief can't steal it all at once, but it's much harder for you to keep track of exactly what is happening in each vault. |
| `P.107.5` | **Digital Circuit Breakers:** A temporary pause on normal rules during a cyber crisis to minimize the impacts of a bank run. It requires proving the attack is a **force majeure** event, though some argue preventative controls should have stopped it. | `[REG/ECO]` | It’s a "Time-out." If everyone is panicking because they can't log in, you stop all trades so you can fix the system without prices crashing. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank uses only one Cloud Provider (Single-Cloud):** It faces extreme **Concentration Risk**. A single outage at that provider means 100% of the bank's digital functions stop immediately.
- **Variable Flip: If a "Malicious Actor" launches a "Data Integrity" attack on the central bank's payment ledger:** The entire financial system could **Freeze**. Trust would evaporate instantly because no one would know who actually owns which dollar.
- **Variable Flip: If a bank focuses only on "Tick-the-box" compliance:** It becomes **Vulnerable** to new, "Zero-Day" attacks that the regulators haven't documented yet. Resilience requires a "Principles-based," forward-looking approach.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Integrity Shock:** Most severe for stability (alters data). | **Confidentiality Shock:** Most severe for stability (NO: privacy loss is easier to contain). |
| **Agent-Based Models (ABM):** Capture nonlinear contagion and trace systemic risks. | **Linear Models:** Cannot capture contagion effects accuracy. |
| **DORA (EU):** Deals with ICT cloud risks and penetration stress testing. | **Circuit Breaker:** Long-term pause on banking (NO: Temporary pause). |

## 4. Directional Intuition
- **Asset Interconnectivity $\uparrow \rightarrow$ Contagion Speed $\uparrow \uparrow$:** In the digital age, a cyber virus can move through the banking system faster than a human fire-drill can react.
- **Complexity $\uparrow \rightarrow$ Predictability $\downarrow$:** Nonlinear "contagion" effects make it nearly impossible to predict the exact probability of a "Cyber-driven Financial Crisis."
- **Cloud Adoption $\uparrow \rightarrow$ ICT Systemic Risk $\uparrow$:** The more we "Centralize" our data on a Few Cloud providers, the bigger the "Target" for a global-scale failure.

## 5. Ambiguity Traps (Anti-Decoder)
- **Cyber vs ICT:** Did the "Bad Guy" do it (Cyber) or did the "Machine" just break (ICT)?
- **The CIA Trap:** Remember that **Integrity** (data truth) and **Availability** are the most critical for stability. If people think their balance is "fake," the system crashes.
- **Agent-Based Models (ABM):** Why use them? Because contagion is nonlinear. ABMs simulate interactions among agents and can trace systemic sources (e.g., if a cyber incident prevents withdrawals at Bank A, the contagion might manifest at Bank B). Basic principles of ABMs can develop cyber/ICT stress tests.
- **Force Majeure Trap:** To use a circuit breaker, banks often must prove the event is a *force majeure* (unforeseeable act of god), but critics argue cyberattacks are foreseeable and should be prevented.
- **Regulations:** Watch for **DORA** (Digital Operational Resilience Act in the EU), which mandates penetration stress testing and third-party risk management.
- **Cloud Stewardship:** Does Multicloud decrease all risk? **NO.** It reduces concentration risk but increases complexity and leads to *weaker stewardship*.
- **80% Rule:** 80% of cloud customers had an outage in the last 3 years, and 20% had significant disruptions. Cloud is highly vulnerable to physical ICT outages (e.g. from climate/energy issues).
- **Macroprudential vs Microprudential:** Micro deals with general operational guidance for one bank. Macro framework policies deal with the whole system not crashing.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
