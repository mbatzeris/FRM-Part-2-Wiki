# R50 — Case Study: Cyberthreats

**Exam Priority:** 🟢 Low (0-1 questions) and Information Security Risks

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.50.1` | **The Four-Quadrant Risk Matrix:** Data incidents are categorized across two axes: **Internal vs. External** and **Intentional vs. Unintentional**. | `[OPS]` | To defend, you must know if the threat is a hacker (External/Intentional), a rogue employee (Internal/Intentional), or a clumsy clerk (Internal/Unintentional). |
| `P.45.2` | **IT Security vs. InfoSec Risk Management:** Modern frameworks shift the focus from purely technical prevention (IT Security) to viewing data security as a business-led risk management discipline. | `[THE]` | Cyber is no longer "an IT problem"; it's a Board-level business continuity problem. |
| `P.50.3` | **Equifax Weakness: IT Inventory:** Equifax failed because it did not have a comprehensive, centralized inventory of its IT assets and systems. | `[OPS]` | You can't patch a server you don't know exists. Shadow IT is a fatal vulnerability. |
| `P.50.4` | **Equifax Weakness: Patch Management:** The breach was caused by a failure to apply a critical, known security patch (Apache Struts) despite a policy requiring it. | `[REG/OPS]` | A policy without enforcement is just a piece of paper. The gap between "Policy" and "Execution" is where hackers live. |
| `P.50.5` | **Equifax Weakness: Certificate Management:** An expired SSL certificate prevented Equifax from detecting data being exfiltrated from their network for months. | `[OPS]` | Your "Alarms" (detection tools) only work if their batteries (certificates) are charged. Expired certificates create visibility "blind spots." |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If Equifax had a perfect Patch Management policy but NO IT Inventory:** Then they would have patched all *known* servers, but the attackers would have simply used the *uninventoried* servers to enter. Inventory is the prerequisite for all other security controls.
- **Variable Flip: If a data breach was caused by an employee sending an email to the wrong person:** This would be classified as **Internal/Unintentional**. Even without "malice," the operational impact (data leak) is the same.
- **Variable Flip: If Equifax's SSL certificate had not expired:** Then their intrusion detection systems (IDS) would have likely flagged the unusual volume of data leaving the network, significantly reducing the "discovery lag" from months to days.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Equifax Failures:** Inventory, Patching, SSL Certs, Communication. | **Phishing Exercises:** Were *not* cited as a primary failure in the Equifax case study. |
| **Internal/Unintentional:** Sending documents to the wrong recipient. | **External/Unintentional:** Disasters, third-party system disruptions. |
| **Intentional/Internal:** Employee theft or data corruption. | **Intentional/External:** External hackers and cyber-espionage. |

## 4. Directional Intuition
- **IT Complexity $\uparrow \rightarrow$ Inventory Accuracy $\downarrow \rightarrow$ Patch Management Failure $\uparrow$:** The more complex the network, the higher the chance of "orphaned" or unpatched systems existing.
- **Detection Lag $\uparrow \rightarrow$ Breach Severity $\uparrow$:** The longer a hacker is inside your network (due to expired certs or poor monitoring), the more data they can find and steal.
- **Communication Inconsistency $\uparrow \rightarrow$ Reputational Damage $\uparrow$:** Conflicting messages to the public during a breach destroy customer trust faster than the breach itself.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Internal/Unintentional" Label:** GARP asks about a clerk misaddressing a sensitive file. Is this "Fraud"? **NO.** It is **Internal/Unintentional**. It is a process failure, not a crime.
- **Equifax's Fatal Blow:** Was it a "Zero-Day" attack (unknown vulnerability)? **NO.** It was a **known** vulnerability with an available patch that was simply not applied.
- **The Role of the SSL Certificate:** In the Equifax case, the expired cert didn't *allow* the entry—it *prevented the detection* of the exit (exfiltration).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
