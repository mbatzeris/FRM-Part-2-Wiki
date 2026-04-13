# R56 — Supervisory Guidance on Model Risk Management (SR 11-7)

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.56.1` | **Definition of Model Risk:** Risk resulting from (1) improper decisions based on inaccurate model outputs (Faulty Design) or (2) misuse of the model (Inappropriate Application). | `[REG/SR 11-7]` | You can fail by building a bad map (Design) or by using a good map of New York to navigate London (Usage). |
| `P.56.2` | **The Validation Triad:** Effective validation requires three elements: (1) **Evaluation of Conceptual Soundness**, (2) **Ongoing Monitoring**, and (3) **Outcomes Analysis**. | `[REG]` | First, check the logic (Soundness); second, check the daily performance (Monitoring); third, check if the predictions actually came true (Outcomes). |
| `P.56.3` | **Effective Challenge:** Validation must be performed by parties independent of the model development process, providing a critical "challenge" to the developers' assumptions. | `[OPS]` | You can't grade your own exam. Independence ensures the validator isn't blinded by "Confirmation Bias" from the developer. |
| `P.45.4` | **Benchmarking vs. Backtesting:** Benchmarking compares model inputs/outputs to other data sources; Backtesting compares model estimates to actual realized outcomes. | `[THE]` | Benchmarking is "How do I look compared to others?"; Backtesting is "Did I predict what actually happened?" |
| `P.56.5` | **Vendor Model Accountability:** Using a third-party "Black Box" model does not exempt the bank from validation. Focus shifts to sensitivity analysis and benchmarking due to limited code access. | `[REG/OPS]` | "The Vendor told me it works" is not a defense. The bank owns the risk and must prove the outputs are appropriate for its specific use case. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a validator used the "Development" dataset for Backtesting:** Then the backtest is mathematically invalid. Backtesting requires a **different time period** than the one used to build the model to ensure the model isn't "Overfitted" to past data.
- **Variable Flip: If a bank automated its "Process Verification" perfectly but ignored "Conceptual Soundness":** Then the bank would have a high-speed machine producing perfectly formatted but logically meaningless garbage. Monitoring only checks the *operation*; Soundness checks the *essence*.
- **Variable Flip: If the reporting component of a model was flawless but the processing component failed:** THEN you would have a beautiful, clear report of a totally incorrect estimate. Processing creates the number; Reporting explains it.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Outcomes Analysis** contains **Backtesting**. | **Ongoing Monitoring** is the umbrella for **Benchmarking**. |
| **Conceptual Soundness** includes **Sensitivity Analysis**. | **Process Verification** checks data inputs, not model logic. |
| **Effective Challenge** requires segregation of duties. | **Peer Review** is not a formal part of the 3-element validation framework. |

## 4. Directional Intuition
- **Model Complexity $\uparrow \rightarrow$ Model Risk $\uparrow \rightarrow$ Validation Depth $\uparrow$:** The more "Black Box" and non-linear the model (e.g., Deep Learning), the more aggressive the independent challenge must be.
- **Data Uncertainty $\uparrow \rightarrow$ Sensitivity Analysis Importance $\uparrow$:** If you aren't sure about the inputs, you must "Stress Test" them by flipping variables to see if the model's output explodes.
- **Target Confidence Level $\uparrow \rightarrow$ Required Backtesting Rigor $\uparrow$:** If you are using a 99.9% VaR model for capital, your backtesting must be far more surgical than for a simple budget-forecasting tool.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Benchmarking" Label:** Is comparing your model to a competitor's model part of "Outcomes Analysis"? **NO.** It is **Ongoing Monitoring/Benchmarking**.
- **Backtesting Horizon:** Does the backtesting period need to match the forecast horizon? **YES.** But the *time dates* must be different from the development set.
- **The Vendor Trap:** GARP asks "Does a vendor model's proprietary nature excuse the bank from full validation?" **NEVER.** The bank must increase sensitivity analysis to compensate for the "Black Box" nature.
- **Processing vs. Reporting:** Which one transforms inputs into estimates? **PROCESSING.** Which one transforms estimates into business info? **REPORTING.**


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
