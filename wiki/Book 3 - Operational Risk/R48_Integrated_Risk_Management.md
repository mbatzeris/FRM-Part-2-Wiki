# R48 — Integrated Risk Management

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.48.1` | **Economic Capital (EC) Calibration:** Firms set EC to cover unexpected losses at a confidence interval matching the target credit rating (e.g., a bank targeting an 'A' rating with a 0.07% PD sets EC at the 99.93% confidence level). | `[THE/REG]` | EC is your "Self-Insurance." You decide how much of a cushion you want based on the probability of ruin you're willing to accept. |
| `P.48.2` | **Reverse Stress Testing:** A qualitative approach that starts with a hypothetical institution *failure* and works backward to identify the specific circumstances that caused it. | `[OPS]` | Instead of asking "What if X happens?", you ask "If we go bankrupt tomorrow, how did it happen?" This catches blind spots. |
| `P.48.3` | **Operational Stress Modeling Modules:** OpRisk stress tests typically consist of a **Legal Loss** module, a **Non-Legal Loss** module, and an **Idiosyncratic Scenario Add-on**. | `[REG/BCBS]` | Legal losses (litigation) behave differently than routine IT failures and must be modeled separately due to massive timing lags. |
| `P.48.4` | **Legal Loss Lag Time:** There is a significant time delay between a macroeconomic shock (e.g., a financial crisis) and the incurring of legal operational losses (e.g., years of lawsuits). | `[THE]` | The market crashes in Year 0; the heavy-tailed legal fines don't hit the balance sheet until Year 3-5. Stress tests must account for this "Long Tail." |
| `P.48.5` | **RAROC in Integration:** `Risk-Adjusted Income / Economic Capital`. While standard for credit, it is difficult to apply to OpRisk due to the challenge of quantifying the numerator and EC precisely. | `[ECO]` | It’s the "Efficiency Metric" for risk. It tells you if the profit you're making is worth the economic cushion you're burning. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If Economic Capital was set at the 100% confidence level:** Then the bank would need infinite capital to cover the most extreme, unimaginable events. EC is always a trade-off between safety and capital efficiency.
- **Variable Flip: If a Stress Test ignored "Lag Time" for legal losses:** Then the model would fundamentally underestimate the capital needed during a multi-year crisis. It would assume the "blow" happens instantly, rather than being a sustained financial bleed.
- **Variable Flip: If a Reverse Stress Test only used "Quantitative" data:** Then it would likely miss the governance and cultural failures (e.g., fraud or senior management bypass) that are most likely to cause a total institutional collapse.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Reverse Stress Testing** is primarily qualitative/scenario-driven. | **Standard Stress Testing** is often quantitative/factor-driven. |
| **Idiosyncratic Scenario Add-on** captures risks unique to the bank. | **General Macro Scenarios** capture risks common to the industry. |
| **Probability of Default (PD)** defines the confidence interval for Economic Capital (EC = 1 - PD). | **Expected Loss (EL)** is priced in; EC covers **Unexpected Loss (UL)**. |

## 4. Directional Intuition
- **Target Credit Rating $\uparrow \rightarrow$ Required Confidence Level $\uparrow \rightarrow$ Economic Capital $\uparrow$:** To be "Triple-A" safe, you must hold many more standard-deviations of capital than to be "B-rated" safe.
- **Transparency $\downarrow \rightarrow$ Reverse Stress Test Effectiveness $\uparrow$:** The more secretive a culture is, the more important it is to perform reverse stress tests to uncover hidden "taboo" failure paths.
- **Macroeconomic Volatility $\uparrow \rightarrow$ Legal Loss Uncertainty $\uparrow$:** Highly volatile markets create more "unhappy customers," which eventually translates into higher litigation (OpRisk) losses years later.

## 5. Ambiguity Traps (Anti-Decoder)
- **The Confidence Level Math:** GARP says "A bank wants an A-rated PD of 0.05%." What is the EC confidence level? Answer: **99.95%**. Don't forget to subtract the PD from 100%.
- **Reverse Stress Starting Point:** Does a reverse stress test start with a scenario like "Interest rates rise 2%?" **NO.** It starts with **"The bank has failed and is insolvent."** Then it works backward.
- **RAROC's Weakness in OpRisk:** Why isn't RAROC used for OpRisk? Answer: **Difficulty in risk-adjusting income and the lack of precision in OpRisk EC.** It works much better for Credit/Market risks.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
