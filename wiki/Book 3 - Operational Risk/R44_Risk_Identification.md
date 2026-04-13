# R44 — Risk Identification

**Exam Priority:** 🟢 Low (0-1 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.44.1` | **Top-Down Identification:** Strategic-level identification using workshops, brainstorming, and "Risk Wheels" to find enterprise-wide threats. | `[OPS]` | Looking at the forest from a helicopter; capturing high-level strategic failures that could sink the whole ship. |
| `P.44.2` | **Bottom-Up Identification:** Granular, local identification focusing on day-to-day processes, near misses, and specific failures. | `[OPS]` | Looking at the individual trees; finding the root causes (e.g., data entry errors) before they aggregate into a catastrophe. |
| `P.44.3` | **Near Misses:** Events where an operational failure occurred but resulted in zero or minimal loss (either by luck or quick recovery). | `[THE]` | Near misses are "Free Lessons." They reveal the same vulnerabilities as actual losses but without the price tag. |
| `P.44.4` | **Taxonomy Hierarchy (Basel):** A three-level system for categorizing risk: L1 (Broad Event Category), L2 (Sub-category), L3 (Specific Example). | `[REG/BCBS]` | Standardization allows for benchmarking. Level 1 (Internal Fraud) $\rightarrow$ Level 2 (Unauthorized Activity) $\rightarrow$ Level 3 (Insider Trading). |
| `P.44.5` | **Control Types:** Controls are categorized as **Preventive** (stop it happening), **Detective** (find it after it happened), or **Corrective** (fix the damage). | `[OPS]` | Reconciliations are detective (they show the error); firewalls are preventive; backup servers are corrective. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a firm ignored "Near Misses" because no money was lost:** Then the firm is structurally blind to its own vulnerabilities. Near misses have the same "underlying process" distribution as actual losses; ignoring them leads to a false sense of security (The "Gunslinger Paradigm").
- **Variable Flip: If a facilitator for a Scenario Analysis workshop was an "Internal" manager:** Then the "empirical" nature of the assumptions might be tainted by internal bias or political pressure (Groupthink). Third-party facilitators are preferred to ensure objectivity.
- **Variable Flip: If a detective control (Reconciliation) was perfect:** Then it would still not *prevent* the initial error. A perfect detective control only ensures the loss is *known*, not that the process is *robust*.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Process Mapping** is a bottom-up tool (micro-view). | **Risk Wheel** is a top-down tool (macro-view). |
| **RCSAs (Risk and Control Self-Assessments)** are subjective but provide local ownership. | **Standardized Taxonomies** are objective and allow for industry loss-data sharing. |
| **Detective vs. Corrective:** A reconciliation *is* detective. It is *not* corrective (the manual entry to fix it is the correction). | **External Fraud** is a Basel L1 category; **Theft** is an L2 sub-category. |

## 4. Directional Intuition
- **Granularity $\uparrow \rightarrow$ Identification Accuracy $\uparrow \rightarrow$ Complexity $\uparrow$:** The more detail you want (Bottom-Up), the more resources and data-processing you need.
- **Data Quality $\downarrow \rightarrow$ Scenario Analysis Bias $\uparrow \rightarrow$ Tail Risk Underestimation $\uparrow$:** If scenarios aren't built on empirical evidence, they become "fantasy modeling" that ignores real-world fat tails.
- **Automated Controls $\uparrow \rightarrow$ Human Error $\downarrow \rightarrow$ Process Consistency $\uparrow$:** Moving from manual (people) to automated (systems) reduces frequency but may increase severity if the system itself has a "model risk" bug.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Internal" Assumption:** GARP might suggest that internal managers should facilitate scenario workshops because they "know the business best." **FALSE.** For extreme risk identification, third-party facilitators are needed to reduce subjectivity and bias.
- **Detective vs. Preventive:** Is a "limit check" in a system detective? **NO.** If it blocks the trade, it is **Preventive**. If it sends an email *after* the trade is executed, it is **Detective**.
- **The "Zero Loss" Trap:** Question: "Should a firm record an event that was halted by a manual override before any loss occurred?" **YES.** It is a *Near Miss*, and it identifies an operational breakdown regardless of the zero loss outcome.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
