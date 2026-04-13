# R46 — Risk Mitigation

**Exam Priority:** 🟢 Low (0-1 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.46.1` | **The 4 T’s of Risk Response:** The standard framework for deciding how to handle an identified risk: **Tolerate**, **Treat**, **Transfer**, or **Terminate**. | `[OPS]` | Do you ignore it (Tolerate), fix it (Treat), buy insurance (Transfer), or quit the business (Terminate)? |
| `P.46.2` | **The Directive Control:** A control that provides guidance, such as policies, procedures, or training. | `[OPS]` | This is the "Instruction Manual." It doesn't physically stop an error, but it tells the employee how to avoid one. |
| `P.46.3` | **Corrective vs. Preventive Controls:** Preventive controls lower the probability of occurrence; Corrective controls (like BCP or cloud backups) lower the impact *after* occurrence. | `[THE]` | A firewall prevents the fire; a sprinkler system corrects the damage. |
| `P.46.4` | **Automation Risks (Type 1 & Type 2 Errors):** Automating controls reduces human error but introduces **False Positives** (Type 1 - blocking valid activity) and **False Negatives** (Type 2 - missing a real threat). | `[THE]` | An over-aggressive fraud scanner (Type 1) annoys customers; a weak one (Type 2) lets the fraud through. |
| `P.46.5` | **Optimistic & Collective Control Failures:** Controls that rely on "good faith" (Optimistic) or split accountability (Collective) are prone to failure. | `[OPS]` | If "everyone" is responsible for checking the trade, then "no one" actually does it. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a firm chose to "Transfer" all risk via insurance:** Then the firm would suffer from **Moral Hazard**, potentially neglecting internal controls because "the insurer will pay." Insurance is a mitigation tool, not a substitute for sound ORM.
- **Variable Flip: If a control was switched from Manual to Automated:** Then the *frequency* of individual errors would drop, but the *severity* of a systematic error (e.g., a bug in the code affecting all transactions) would skyrocket. Automation trades human variance for model risk.
- **Variable Flip: If a "Directive" control (Policy) was the only control in place:** Then the firm would be highly vulnerable to human negligence or malicious intent, as directive controls have the lowest "enforcement" strength compared to preventive or detective system controls.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Transferring risk** includes insurance AND outsourcing/offshoring. | **Termination** is the most extreme response; **Tolerance** is the least. |
| **Detective Controls** are "alarms" (e.g., reconciliations, audit trails). | **Directive Controls** are "rules" (e.g., training, manuals). |
| **Backups/BCP** are **Corrective** controls. | **Corrective** is *not* the same as **Insurance** (which is Transfer). |

## 4. Directional Intuition
- **Control Complexity $\uparrow \rightarrow$ Operational Drag $\uparrow \rightarrow$ Type 1 Errors $\uparrow$:** The more "checks" you add, the slower the business moves and the more legitimate activities get flagged as suspicious.
- **Individual Accountability $\downarrow \rightarrow$ Control Evasion $\uparrow$:** Collective controls (where multiple people sign off) often lead to "rubber-stamping," where no one actually performs the verification.
- **Business Continuity Maturity $\uparrow \rightarrow$ Impact Severity $\downarrow$:** Strong corrective controls don't stop disasters, but they transform a "bankrupting event" into a "minor service disruption."

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Insurance covers all" Trap:** Does insurance mitigate operational risk? **PARTIALLY.** It mitigates the *financial* impact but does nothing to fix the underlying process failure or reputational damage.
- **Detective vs. Directive:** Question: "Is a training manual a detective control?" **NO.** It is **Directive**. It provides guidance. Detective controls find errors *after* they occur.
- **The Automation Fallacy:** "Automated controls are always safer than manual ones." **FALSE.** While more reliable, they introduce **Type 2 errors** (systematic blind spots) and **Model Risk** that humans might have caught through "common sense" intuition.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
