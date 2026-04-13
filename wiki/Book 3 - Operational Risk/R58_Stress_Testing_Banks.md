# R58 — Stress Testing Banks

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.58.1` | **Scenario Coherence:** A critical challenge in stress test design is ensuring that the extreme scenario is "Coherent"—meaning its multiple factors (Interest rates, GDP, Unemployment) are logically and economically possible together. | `[THE/OPS]` | You can't have a "Deep Depression" scenario with "Record High Interest Rates" without a very coherent economic explanation. If the story doesn't make sense, the bank won't believe the results. |
| `P.58.2` | **Credit Card/Unemployment Sensitivity:** Credit card loss rates are the most sensitive asset class to changes in the unemployment rate, often serving as a leading indicator of household distress. | `[THE]` | When money gets tight, families choose. They usually stop paying the "Credit Card" (Unsecured) before they stop paying the "Rent/Mortgage" (Secured/Shelter). |
| `P.58.3` | **Recursive Balance Sheet Modeling:** Stress tests are dynamic; the losses in Q1 reduce the capital for Q2, which limits the bank's ability to originate new loans or pay dividends in future quarters. | `[OPS]` | It’s a "Financial Bleed." The model must account for the bank's own reactive behaviors (e.g., cutting dividends or selling assets) as the stress horizon progresses. |
| `P.58.4` | **CCAR Internal Scenarios:** Unlike many other frameworks, the US Comprehensive Capital Analysis and Review (CCAR) requires banks to develop and run their own internal stress scenarios in addition to the regulator's. | `[REG/CCAR]` | The Fed says: "Don't just pass MY test; prove to me that YOU know where your specific body is most vulnerable." |
| `P.58.5` | **Capital Plan Rule:** Stress testing is not just a math exercise; it is integrated into a formal "Capital Plan" that determines if a bank is allowed to return capital to shareholders via dividends/buybacks. | `[REG]` | The result of the stress test is a "Pass/Fail" for your dividend check. If you fail the "Severely Adverse" test, you can't pay your owners. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a stress test scenario was "Extreme but Incoherent":** Then the bank's management would likely ignore the results, branding them as "economically impossible." Coherence is necessary for the **Credibility** and **Utility** of the test.
- **Variable Flip: If a bank assumed static "Asset Origination" during a crisis:** Then the stress test would likely be inaccurate. In a real crisis, banks tighten credit standards and originate fewer loans to preserve capital. A "Static" balance sheet is a common model failure.
- **Variable Flip: If Unemployment stayed low but Interest Rates spiked:** This would hit commercial loans and mortgages (repayment ability) but might not spike credit card defaults as severely as an unemployment crisis would. Different stressors hit different asset classes.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Unemployment:** The primary driver of credit card losses in stress models. | **Inflation:** Often a secondary factor in retail stress models compared to jobless rates. |
| **CCAR/DFAST:** Names of US stress testing frameworks. | **MiFID:** Is for investor protection, not capital stress testing. |
| **Coherence:** Logical consistency of scenario variables. | **Precision:** Stress tests are about "Broad Impacts," not penny-accurate predictions. |

## 4. Directional Intuition
- **Economic Downturn $\uparrow \rightarrow$ Unemployment $\uparrow \rightarrow$ Credit Card Defaults $\uparrow$:** The relationship is near-linear and high-velocity.
- **Scenario Severity $\uparrow \rightarrow$ Bank Corrective Actions $\uparrow \rightarrow$ Model Complexity $\uparrow$:** The deeper the stress, the more "heroic" the management actions (asset sales/capital raises) the model must simulate.
- **Internal Scenario Quality $\uparrow \rightarrow$ Management Risk Awareness $\uparrow \rightarrow$ Regulatory Approval $\uparrow$:** Banks that truly understand their own idiosyncratic risks get more leeway from the Fed in CCAR.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Mortgage vs. Credit Card" Trap:** Which one defaults first? **Credit Cards.** People protect their home as a last resort.
- **Who provides the CCAR scenarios?** Answer: **Both.** The Fed provides scenarios (Baseline, Adverse, Severely Adverse), AND the bank must provide its own.
- **Coherence vs. Severity:** Can a scenario be too severe? No. But it can be **Incoherent** (the variables don't fit together logically).
- **The 9-Quarter Horizon:** Note that CCAR/DFAST typically uses a **9-quarter** (2.25 years) projection horizon.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
