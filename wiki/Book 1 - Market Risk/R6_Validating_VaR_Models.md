# R6 — Validating BHC VaR Models

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.6.1` | **Conceptual Soundness:** The first step of validation. It asks: "Are the assumptions behind the model logical and appropriate for the bank's specific portfolio?" | `[THE/REG]` | It’s like checking if you’re using a "Map of New York" to navigate New York. If your map is of Tokyo (wrong assumptions), it doesn't matter how well you follow it; you'll still get lost. |
| `P.6.2` | **Sensitivity Analysis:** A "What-if" exercise where you tweak model inputs (like correlations or volatilities) to see how much the final VaR moves. It identifies which factors the model is most "allergic" to. | `[MTH/OPS]` | You're checking the "Sensitivity" of a patient to a drug. If a tiny dose (small change in correlation) causes a massive reaction (huge VaR jump), you need to watch that factor closely. |
| `P.6.3` | **VaR Model Benchmarking:** Running the "official" model against a simpler "challenger" model. If the results are worlds apart, it suggests the official model might be over-engineered or hiding errors. | `[OPS/REG]` | It’s a "Second Opinion" from another doctor. If the top surgeon says you have a cold but the family doctor says it’s the plague, you need to find out why they disagree. |
| `P.6.4` | **Outcome Analysis:** The final check. It compares predicted values to actual results over time to ensure the model’s "calibration" is holding up in the real world. | `[OPS]` | You predicted you’d finish the race in 10 minutes. You finished in 40. Your "Model" of your own speed is broken. |
| `P.6.5` | **Confidence Intervals are Asymmetric:** Because P/L distributions are skewed and have floors (like zero price), the "error bars" around an estimated VaR are rarely perfectly centered. | `[MTH/THE]` | Your "Plus or Minus" isn't equal. You're more likely to be "Way Off" on the downside than "Way Off" on the upside. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a model is "Conceptually Sound" but has poor "Outcome Analysis":** The implementation is likely flawed (e.g., bad data feeds or coding bugs), even if the math in the textbook was perfect.
- **Variable Flip: If you use more data for a GARCH-VaR model:** The **Confidence Interval** will get **Tighter**. More data + Better model = More precision.
- **Variable Flip: If a bank uses benchmarking as a "Permanent" solution:** It is **Inefficient**. Benchmarking is a temporary tool used for transitions or spot-checks because maintaining two full models is too expensive and resource-heavy.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Sensitivity Analysis:** Validates the model's response to inputs. | **Sensitivity Analysis:** Determines regulatory capital (NO: VaR determines capital). |
| **Conceptual Soundness:** Focuses on the "Logic/Design." | **Conceptual Soundness:** Focuses on "Adjusting inputs" (NO: that's sensitivity). |
| **Benchmarking:** Comparing to a "Challenger" model. | **Benchmarking:** Comparing to a "Competitor bank" (NO: that's peer-analysis). |

## 4. Directional Intuition
- **Model Complexity $\uparrow \rightarrow$ Conceptual Soundness Risk $\uparrow$:** The more "Bells and Whistles" you add, the easier it is to accidentally build a "Black Box" that no one understands.
- **Data Quality $\uparrow \rightarrow$ Outcome Analysis Accuracy $\uparrow$:** "Garbage in, Garbage out." If the historical prices are wrong, the backtest results are lies.
- **Correlation Persistence $\uparrow \rightarrow$ Model Stability $\uparrow$:** If market relationships stay the same, the model stays valid longer.

## 5. Ambiguity Traps (Anti-Decoder)
- **Three Pillars of SR 11-7:** (Guidance on Model Risk Management). You must know **Conceptual Soundness**, **Monitoring**, and **Outcome Analysis**.
- **Internal vs Regulatory:** Note that models for *Internal* risk might be more aggressive/complex than those for *Regulatory* capital, which tend to be more conservative.
- **Ghost Effects vs Model Risk:** A ghost effect is a *known* weakness of HS; failing to account for it or monitor it is **Model Risk**.
- **Sample Error:** Even a "Perfect" model will have a confidence interval because we only have a limited slice of history.
- **The "Challenger" Model:** It doesn't have to be "Better," just "Different" enough to catch logic errors in the main model.
- **Independence of Errors:** Note the "Professor's Note": errors in benchmarking aren't always i.i.d. because trading portfolios change so fast.
- **Dynamic Portfolios:** If the traders are buying and selling all day, a "Static" VaR model will always be slightly "Wrong." Validation must account for this "Noise."
- **Capital Deductions:** Validation *per se* doesn't change capital, but the *results* (like too many exceptions) will trigger the Basel penalty multiplier.
- **Backtesting vs Outcome Analysis:** Backtesting is a *subset* of Outcome Analysis. Analysis is broader and includes Profit Attribution (PAA).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
