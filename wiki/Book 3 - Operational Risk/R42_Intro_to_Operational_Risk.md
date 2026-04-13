# R42 — Introduction to Operational Risk

**Exam Priority:** 🟡 Medium (1-2 questions) and Resilience

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.42.1` | **Definition of Operational Risk:** The risk of loss resulting from inadequate or failed internal processes, people, systems, or external events. | `[REG/BCBS]` | Operational risk is about *execution failure*—it’s what happens when the machines (systems), the pilots (people), or the environment (external) break down. |
| `P.42.2` | **The Four-Step Iterative Cycle:** Operational risk must be managed through (1) Identification, (2) Assessment, (3) Mitigation, and (4) Monitoring. | `[OPS]` | You can't manage what you don't identify; you can't prioritize what you don't assess. |
| `P.42.3` | **The Seven Basel II Event Categories:** Operational risk is taxonomized into IF, EF, EPWS, CPBP, DPA, BDSF, and EDPM. | `[REG]` | These categories capture the *origin* of the failure, from fraud to legal compliance (CPBP) to physical asset damage. |
| `P.42.4` | **Attributes of OpRisk Exposures:** Operational risk is (1) Heterogeneous, (2) Idiosyncratic, (3) Heavy-tailed (Fat-tailed), (4) Interconnected, and (5) Dynamic. | `[THE]` | Unlike market risk, OpRisk has no single driver; it is highly firm-specific, prone to "Black Swan" catastrophes, and constantly evolving. |
| `P.42.5` | **Operational Resilience Pivot:** The focus has shifted from solely *preventing* incidents to *managing* them as they happen, acknowledging that extreme disruptions will occur. | `[ECO/REG]` | Resilience assumes you *will* be hit; it measures how well you bounce back rather than how thick your shield is. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If OpRisk were Homogeneous (like Market Risk):** Then we could use universal correlations and global factors to hedge it. In reality, it is **Heterogeneous**, meaning a system failure at Bank A tells you nothing about the probability of a fraud at Bank B.
- **Variable Flip: If OpRisk were Light-Tailed:** Then standard normal distributions would suffice. In reality, it is **Heavy-tailed**, meaning the "mean" loss is irrelevant; it is the 99.9% probability catastrophic loss that bankrupts the firm.
- **Variable Flip: If Operational Resilience focused only on "Prevention":** Then a single successful breach would mean a total failure of the resilience framework. In reality, it focuses on **Impact Tolerance**—how long can you survive the breach before the system fails?

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **CPBP (Clients, Products, & Business Practices)** usually accounts for the highest *severity* (e.g., massive regulatory fines). | **EDPM** is high *frequency* but often lower severity than peak CPBP events. |
| **Legal/Compliance Risk** is explicitly included in the OpRisk definition. | **Strategic and Reputational Risk** are often excluded from standard *regulatory capital* buckets but are managed within the broader ORM framework. |
| **Idiosyncratic Nature:** OpRisk cannot be fully eliminated through traditional hedging. | **Dynamic Nature:** OpRisk is *not* static; as technology evolves (AI/Remote work), the risk surface changes instantly. |

## 4. Directional Intuition
- **Complexity $\uparrow \rightarrow$ Interconnectedness $\uparrow \rightarrow$ OpRisk $\uparrow$:** As systems become more linked, a single point of failure (e.g., a shared third-party cloud provider) creates systemic operational vulnerability.
- **Remote Work $\uparrow \rightarrow$ Cyber/Fraud Surface $\uparrow$:** Pandemic-driven remote work shifted processing to less secure external environments, increasing the surveillance burden.
- **Regulatory Pressure $\uparrow \rightarrow$ CPBP Severity $\uparrow$:** Increasing focus on investor protection (MiFID II/Dodd-Frank) makes "Business Practices" a primary driver of heavy-tailed losses.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Prevention" Trap:** GARP will suggest that a resilient firm is one that *prevents* all cyber intrusions. **FALSE.** A resilient firm is one that maintains *Impact Tolerance* during and after the inevitable intrusion.
- **The "Strategic Risk" Boundary:** Is Strategic Risk part of Operational Risk? **NUANCE.** While related to "people/processes," standard BCBS capital rules often separate Strategic and Reputational risk from the primary Capital charge, though they fall under the ORM *framework*.
- **Frequency vs. Severity:** "Execution and Process Management (EDPM)" has more *incidents*, but "Clients, Products and Business Practices (CPBP)" has the *biggest* checks. Don't confuse bulk loss with peak loss.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
