# R97 — Market-Driven Scenarios

**Exam Priority:** 🟡 Medium (1-2 questions) (MDS)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.97.1` | **The Market-Driven Scenario (MDS):** A structured framework that translates subjective expert views into precise market shocks by using a **Covariance Matrix** to ensure that the shocks to all factors are statistically consistent with each other. | `[MTH/OPS]` | It’s a "Reality Check" for your nightmare scenarios. If you say "Stocks crash 20%," the MDS math tells you exactly how much "Gold" and "Bonds" should move to keep the scenario plausible. |
| `P.97.2` | **Policy Variables Necessity:** MDS relies on a **small set** of "Policy Variables" (e.g., Oil price, Fed rate) as the anchors. Having too many policy variables causes **Multicollinearity**, making the scenario unstable and arbitrary. | `[MTH]` | Don't try to control every single dial on the dashboard. Just pick the 2 or 3 most important ones, and let the statistical engine calculate the rest based on how they usually move together. |
| `P.97.3` | **Mahalanobis Distance (MD):** The primary metric for identifying the "Plausibility" of a scenario. it measures how many standard deviations a scenario vector lies from the historical center, accounting for the correlations between variables. | `[MTH]` | Simple Z-scores look at one variable at a time. MD looks at the "Whole Picture." A scenario where "Oil goes to $200 AND Inflation goes to 0%" would have a massive MD because those things almost never happen together. |
| `P.97.4` | **Scenario z-score:** A normalized measure of a scenario's severity. It allows risk managers to rank hypothetical "what-if" outcomes on a single "Risk Ruler," comparing them to historical events like the GFC. | `[MTH/OPS]` | It’s the "Richter Scale" for stress tests. A z-score of 3 is a bad day; a z-score of 8 is a once-in-a-century apocalypse. |
| `P.97.5` | **Conditional Stress Testing:** MDS is a form of conditional stress testing. Once you "condition" (fix) the policy variables, the shocks to all other variables are determined by their conditional expectations given the covariance structure. | `[MTH/THE]` | "If A happens, what is the most likely value for B?" You use the known relationships to fill in the blanks of your disaster plan. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If you use a "Stagnant" (low vol) period for the covariance matrix:** Your MDS response will **Understate** the risk of a market crash. To model a crash, you MUST use a covariance matrix derived from a period of high volatility/stress.
- **Variable Flip: If a scenario has a Very High z-score but a Low Correlation z-score:** This means the scenario is **Extreme in Magnitude** but **Statistically Coherent**. The moves are big, but they are all "moving in the right direction" together.
- **Variable Flip: If you select 20 Policy Variables for a portfolio of 50 assets:** You will likely encounter **Inversion Problems** in the math. The "Perturbation Vector" becomes highly sensitive to tiny changes, making the test useless.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Mahalanobis Distance:** Primary tool for plausibility (multivariate). | **Euclidean Distance:** (NO: ignores correlations). |
| **Policy Variables:** Should be a **Small** set. | **Policy Variables:** Should include every asset in the portfolio (NO). |
| **MDS Goal:** Aggregate independent views into a collective scenario. | **MDS Goal:** Eliminate all subjectivity from stress testing (NO: it quantifies it). |

## 4. Directional Intuition
- **Policy Variable Correlation $\uparrow \rightarrow$ Scenario Instability $\uparrow$:** If your "Anchors" are moving too much like each other, the math can't find a unique solution.
- **Scenario z-score $\uparrow \rightarrow$ Plausibility $\downarrow$:** The further you get from the "Normal" center of the universe, the less likely it is that your scenario will ever actually happen.
- **Volatility z-score $\uparrow \rightarrow$ Absolute Shock Magntiude $\uparrow$:** Higher vol z-scores mean the scenario is "Bigger" in terms of raw movement.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Small Set" Requirement:** Why not use 100 variables? Because of **Multicollinearity**. Stick to a few "Key Shocks."
- **MD vs. Z-score:** Z-score is 1D. MD is **Multi-dimensional**.
- **The "Forward-Looking" Aspect:** MDS is not just historical. It uses **Expert Views** as inputs, which is why it avoided the "Historical Bias" that failed during the GFC.
- **Five Steps:** 
    1. Define Event. 
    2. Pick Policy Vars. 
    3. Calibrate Shocks. 
    4. Generate Non-Policy Shocks. 
    5. Est. P&L.
- **Risk Ruler:** Using z-scores to compare "COVID-19" to "2008 GFC" to a "Hypothetical Cyber Attack."
- **Subjectivity:** MDS does **not** get rid of subjectivity. It makes it "Transparent and Open to Critique" by putting it into a statistical box.
- **S-plus vs. S-minus:** These are often used to define "Bull" vs "Bear" versions of the same macro shock.
- **The "Conditional" Trick:** MDS finds the **Most Likely** outcome for the rest of the market given your specific policy shocks.
- **Plausibility:** Does a low z-score mean it's a "Good" scenario? **YES**, it means it’s plausible. Extreme scenarios have high z-scores.
- **Risk Attribution:** You can use MD to see which specific assets are contributing most to the "implausibility" of a scenario.
- **The Mahalanobis formula:** $ \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)} $. (Notice the inverse covariance matrix $\Sigma^{-1}$—this is what "removes" the correlations).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
