# R47 — Risk Reporting

**Exam Priority:** 🟢 Low (0-1 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.47.1` | **The Reporting Cake:** A tiered approach where depth decreases as altitude (seniority) increases. Tier 1 (Detailed/Daily), Tier 2 (Action-focused), Tier 3 (Strategic/High-level). | `[OPS]` | The plumber needs to know which pipe is leaking (Tier 1); the manager needs to know if we need a new plumber (Tier 2); the owner needs to know if the house is sinking (Tier 3). |
| `P.47.2` | **Misleading Averages:** Due to high skewness and fat tails in operational loss data, the **mean** is a poor measure of central tendency; use median and quartiles instead. | `[THE]` | If 99 days you lose $0 and 1 day you lose $1M, your "average" loss is $10k, but that number describes neither your daily reality nor your catastrophe risk. |
| `P.47.3` | **10-Year Historical Window:** Basel Pillar 3 requires 10 years of aggregate operational loss data for public disclosure. | `[REG/BCBS]` | Operational risk is infrequent but severe. You need a decade of history to capture the rare, catastrophic "tail" events. |
| `P.47.4` | **Combined Assurance:** Aligning oversight across all three lines of defense to provide a holistic view of risk to the Audit Committee. | `[OPS]` | Breaking down silos so that Risk (L2) and Audit (L3) aren't telling two different stories to the Board. |
| `P.47.5` | **Reporting Escalation Criteria:** Events must be reported to regulators based on Reputation, Resilience, Materiality, or Stability triggers. | `[REG]` | If it makes the news (Reputation), stops the ATMs (Resilience), costs a fortune (Materiality), or threatens the market (Stability), call the regulator. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a Board Risk Committee (Tier 3) received Tier 1 reports:** Then "Information Overload" would occur. Executives would get lost in the noise of daily maintenance logs and miss the strategic trend signals. Reporting must be tailored to the audience's decision-making level.
- **Variable Flip: If small, frequent losses were ignored in reporting:** Then the firm would miss the "Structural Flaw" signals that often precede a major collapse. While small losses don't hit the capital budget, they are the primary diagnostic tool for control breaches.
- **Variable Flip: If Qualitative Data was aggregated using only "Addition":** Then the nuances of different risk types (e.g., Fraud vs. IT Failure) would be lost. Categorization or "Worst-Case" reporting is often more informative for qualitative risk than simple summation.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Tier 1 Recipients:** Business Line Managers and Risk Champions. | **Audit Committee:** Receives high-level Tier 3 summaries (3rd line oversight). |
| **Materiality Trigger:** Losses exceeding a specific dollar or percentage threshold. | **Functional Trigger:** Not a recognized regulatory reporting category in the Basel framework. |
| **Heatmaps and Risk Registers** are core internal ORM report components. | **Expected Losses** are for budgeting/pricing, not for "Resilience" reporting. |

## 4. Directional Intuition
- **Data Skewness $\uparrow \rightarrow$ Mean Usefulness $\downarrow$:** As the "tail" of the distribution gets fatter (more extreme outliers), the average becomes a useless number for risk management.
- **Reporting Transparency $\uparrow \rightarrow$ Regulatory Trust $\uparrow \rightarrow$ Intervention Risk $\downarrow$:** Being honest about failures (especially resilience breaches) early often prevents more severe regulatory penalties later.
- **Information Cost > Information Value $\rightarrow$ Reporting Efficiency $\downarrow$:** If it costs more to track the coffee-machine failures than the failures are worth, stop tracking them. Reporting must influence *decisions*.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Who sees what" Trap:** Who needs the most detail? **Line Managers.** Who needs the "Horizon Scanning" (Emerging Risks)? **Board/Executives.** Don't reverse these.
- **The 10-Year Rule:** GARP might suggest 3 or 5 years for historical loss data. **NO.** For Pillar 3, it is **10 years**.
- **Average vs. Median:** Is the "Mean" the best way to describe an OpRisk profile? **FALSE.** The **Median/Quartiles** are superior because they aren't distorted by a single massive tail event.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
