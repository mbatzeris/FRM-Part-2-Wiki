# R61 — Capital Planning at Large Bank Holding Companies

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.61.1` | **The $50B Threshold:** The Capital Plan Rule explicitly targets Bank Holding Companies (BHCs) with total consolidated assets of **$50 Billion** or greater. | `[REG]` | This is the "Major League" threshold. If you're this big, your failure is systemic, so the Fed demands a formal, annual capital plan. |
| `P.61.2` | **Capital Policy Contingencies:** A robust capital policy must include clear triggers for **Capital Contingency Actions**, such as the suspension of dividends or share repurchases during financial stress. | `[OPS/REG]` | You must have a "Break glass in case of emergency" plan for your cash. If capital gets low, the first thing to stop is the payout to owners. |
| `P.61.3` | **Net Interest Income (NII) Complexity:** Stressed NII projections must incorporate "secondary" effects like changes in **prepayment rates**, embedded options, and loan repricing lags. | `[THE/ECO]` | In a crisis, people don't just stop paying; they also stop refinancing, or they exercise options that hurt the bank's margin. The model must capture these "Hidden Levers." |
| `P.61.4` | **"Other Risks" Integration:** Hard-to-quantify risks like **Reputational, Strategic, and Compliance** risks must still be part of the capital adequacy process, even if they require more qualitative estimation methods. | `[THE/OPS]` | "Too hard to measure" is not a valid excuse for ignoring a risk. If it can break the bank, it needs a capital cushion, even if that cushion is based on expert judgment. |
| `P.61.5` | **Governance vs. Internal Control:** Governance is about Board-level oversight and setting the strategy; Internal Control is about the plumbing—audit, model validation, and process integrity. | `[OPS]` | The Board decides the destination (Governance); the Internal Controls ensure the engine doesn't explode and the map is accurate. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a BHC has $40B in assets:** Then it is not strictly subject to the Capital Plan Rule's $50B threshold requirements (though it may still be subject to other supervisory expectations).
- **Variable Flip: If a Capital Plan assumed "Constant Dividends" during a severe stress scenario:** Then the Fed would likely reject the plan. A realistic plan must show that the bank *will* cut dividends to preserve capital when the "Severely Adverse" scenario hits.
- **Variable Flip: If a bank ignored "Embedded Options" in its NII projections:** Then its interest income would be grossly overestimated in a falling-rate environment (as customers exercise their "prepayment" option to refinance).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Capital Policy:** Contains dividend triggers and contingency plans. | **Peer BHC Oversight:** Not a requirement of the Seven Principles. |
| **Capital Plan Rule:** Applies to BHCs $\ge$ $50B. | **$10B Threshold:** Is for smaller DFAST requirements, not the full Capital Plan Rule. |
| **NII Projections:** Must include prepayments and embedded options. | **Market Cap:** Is not used to determine the threshold; it's based on **Assets**. |

## 4. Directional Intuition
- **Asset Size $\uparrow \rightarrow$ Systemic Importance $\uparrow \rightarrow$ Capital Planning Rigor $\uparrow$:** The bigger the bank, the less "wiggle room" the regulator allows in the capital adequacy process.
- **Interest Rate Volatility $\uparrow \rightarrow$ NII Projection Difficulty $\uparrow$:** When rates move fast, customer behavior (prepayments) becomes erratic and hard to model.
- **Internal Control Strength $\uparrow \rightarrow$ Model Validation Reliability $\uparrow \rightarrow$ Capital Plan Credibility $\uparrow$:** If the Fed doesn't trust your audit/validation process, they won't trust the numbers in your plan.

## 5. Ambiguity Traps (Anti-Decoder)
- **The $50B Asset Rule:** Is it $50B in Market Cap? **NO. Assets.**
- **Hard-to-Quantify Risks:** Can you exclude Reputational Risk because it's hard to model? **NO.** It must be included in the comprehensive assessment.
- **Governance vs. Policy:** Does the "Governance Policy" mandate dividend cuts? **NO.** That is part of the **Capital Policy**. Governance is the oversight *of* that policy.
- **The Principles Count:** Remember there are **Seven** core principles for a sound capital adequacy process.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
