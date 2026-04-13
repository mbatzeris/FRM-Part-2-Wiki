# R57 — Case Study: Model Risk

**Exam Priority:** 🟢 Low (0-1 questions) and Model Validation

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.57.1` | **Model Risk Tiering:** Models are assigned to risk tiers based on **Materiality** (dollar impact), **Complexity**, **Client-facing** status, and **Regulatory** use. | `[OPS]` | Not all models are equal. A model deciding a $1B capital charge needs more oversight than a model deciding the office lunch budget. |
| `P.57.2` | **The Gaussian Copula Failure:** David X. Li’s model assumed **constant/static correlations** between assets in a pool, ignoring that correlations spike toward 1.0 during a crisis. | `[THE]` | Li’s model assumed the "Gaussian Constant" was, well, constant. In reality, in a crisis, all diversification disappears simultaneously. |
| `P.57.3` | **Implementation Error (Barclays):** The inadvertent purchase of 179 unwanted Lehman contracts due to "hidden cells" in a spreadsheet becoming "visible" during a PDF conversion. | `[OPS]` | This isn't a math error; it's a "User Interface" failure. Spreadsheet risk is a major, hidden operational risk component. |
| `P.57.4` | **Input Measurement Error (NASA):** The loss of a $125M satellite because one team used English units (feet/pounds) while the other used Metric (meters/kilograms). | `[THE/OPS]` | A perfect model with the wrong "Unit of Measurement" produces a perfectly accurate disaster. Data integrity starts with consistent units. |
| `P.57.5` | **Annual vs. Periodic Review:** Regardless of risk tier, all models must undergo an **Annual Review** for environmental changes, while full Validation (Tiers) happens every 2-3 years. | `[REG/SR 11-7]` | Validation is a "Deep Dive"; Annual Review is a "Health Check" to ensure the world hasn't changed enough to break the model. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If David X. Li had used "Stochastc/Dynamic Correlations":** Then the model might have survived 2008. The failure was the **Assumption** of a static constant in a non-static world.
- **Variable Flip: If Barclays had used a "Database" instead of a "Spreadsheet":** Then the "Hidden Row" implementation error would have been impossible. Spreadsheets provide too much flexibility, leading to "Manual Override" errors.
- **Variable Flip: If a model is high-complexity but low-materiality:** It may still be a low-tier model. Tiering is highly weighted by the **Financial Impact** (Materiality) of the model's output failing.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Execution Risk:** Errors in input data (NASA) or coding. | **Precise Outputs:** Models produce *forecasts/estimates*, NEVER precise results. |
| **Model Risk Tiers:** Materiality, Complexity, Client-facing, Regulatory. | **Peer Review:** Useful, but not a driver for formal model tiering. |
| **Gaussian Copula:** Failed due to **Invalid Assumption** (static correlation). | **Gaussian Copula Noise:** It didn't fail due to "Math errors" or "Bad Coding." |

## 4. Directional Intuition
- **Asset Correlation $\uparrow \rightarrow$ Diversification Benefit $\downarrow \rightarrow$ CDO Risk $\uparrow$:** The Gaussian Copula failed because it didn't realize that in a crash, everything goes down together.
- **IT Inventory Clarity $\downarrow \rightarrow$ Shadow Spreadsheet Use $\uparrow \rightarrow$ Implementation Risk $\uparrow$:** When formal IT systems fail to meet user needs, users build "Macro-heavy" spreadsheets, creating unmonitored model risk.
- **Unit Inconsistency $\uparrow \rightarrow$ Input Data Error $\uparrow \rightarrow$ Mission Failure $\uparrow$:** Complex projects with multiple vendors (NASA/Lockheed) are extremely vulnerable to "Siloed" measurement standards.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Model" definition:** Is a spreadsheet with hidden cells a "Bad Model"? **NO.** Technically, it was an **Implementation Error**, not a flaw in a mathematical theory.
- **Li's Mistake:** Did David Li use the wrong math? **NO.** He used the **wrong assumption** (that market-implied correlations were static).
- **Validation Frequency:** How often are high-risk models validated? **Every 2-3 years.** How often are they reviewed? **Annually.** Don't mix these up.
- **Precision Trap:** "A good model provides precise outputs." **FALSE.** Models provide *estimates* with uncertainty.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
