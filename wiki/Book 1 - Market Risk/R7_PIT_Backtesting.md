# R7 — Beyond Exceedance-Based Backtesting (PIT)
**Exam Priority:** 🟡 Medium (1-2 questions) (PIT)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.7.1` | **The Probability Integral Transform (PIT):** A method to validate the **entire** forecasted distribution, not just the tail. It converts actual outcomes into a probability value ($0$ to $1$) based on the model’s predicted distribution. | `[MTH/THE]` | Instead of just saying "Did I crash?", PIT asks "Exactly where on the map was I today?" If your map is right, your positions over time should be evenly spread across the whole world. |
| `P.7.2` | **The i.i.d. Uniform Requirement:** If a VaR model is perfectly calibrated, the resulting PIT values must be **Independent and Identically Distributed (i.i.d.) Uniform[0,1]**. | `[MTH]` | If you predict 10% chance of rain, 10% chance of sun, etc., and your model is perfect, you should see those outcomes happen exactly 10% of the time each. |
| `P.7.3` | **The Berkowitz Test:** A "Super-Test" that converts Uniform PIT values into Normal values ($z$-scores). This allows the use of powerful Likelihood Ratio (LR) tests to check for Mean=0, Variance=1, and zero autocorrelation all at once. | `[MTH/OPS]` | It’s easier to check if a pile of sand is a "perfect cone" (Normal) than if it’s a "perfect flat square" (Uniform). Berkowitz reshapes the sand so we can use our standard tools. |
| `P.7.4` | **Anderson-Darling (AD) vs. KS Test:** While the Kolmogorov-Smirnov (KS) test looks for the biggest single error, the **Anderson-Darling** test puts more weight on the **Tails** of the distribution. | `[MTH/REG]` | In risk management, we don't care if the model is slightly off in the "middle" (normal days). We care if it's wrong at the "edges" (crash days). AD is the better "Tail-Sensing" tool. |
| `P.7.5` | **Rosenblatt Transform:** The mathematical engine behind PIT. It ensures that the transformation is valid even for non-normal, complex distributions. | `[MTH]` | The "Universal Translator." It can take any language (distribution type) and turn it into the "Standard Code" (Uniform 0-1). |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a model captures the tail perfectly but fails the "Middle" of the distribution:** Simple backtesting (Kupiec) will **Pass** it, but **PIT/Berkowitz** will **Reject** it. Simple backtesting is "blind" to non-extreme errors.
- **Variable Flip: If PIT values are clustered (e.g., all high values happen in January):** The **Independence** part of the Berkowitz test will fail. This indicates that the model is failing to handle volatility regimes correctly.
- **Variable Flip: If the QQ plot of PITs is curved AWAY from the diagonal:** The model’s distribution is **Mis-specified**. A curve toward the bottom-left indicates the model thinks the distribution is thinner-tailed than it actually is.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Berkowitz:** Uses the Inverse Normal Transform. | **Berkowitz:** Uses the Lognormal Transform (NO). |
| **PIT Score = 0.95:** Outcome was in the 95th percentile. | **PIT Score = 0.95:** 95% chance of exceedance (NO: it’s the *actual* percentile). |
| **Anderson-Darling:** Sensitive to tails. | **KS Test:** Sensitive to tails (NO: it’s sensitive to the maximum distance). |

## 4. Directional Intuition
- **Model Accuracy $\uparrow \rightarrow$ PIT Histogram Flatness $\uparrow$:** A perfect model produces a perfectly flat (Uniform) histogram of results.
- **Model Bias $\uparrow \rightarrow$ Berkowitz Mean $\neq 0$:** If the model consistently under-predicts losses, the $z$-scores will have a non-zero average.
- **Tail Index Fit $\uparrow \rightarrow$ AD Statistic $\downarrow$:** The lower the AD value, the "tighter" the fit in the danger zone.

## 5. Ambiguity Traps (Anti-Decoder)
- **Kupiec vs. Berkowitz:** Kupiec = 1 Point (VaR). Berkowitz = The Whole Shape.
- **PIT Formula:** $u_t = \int_{-\infty}^{y_t} f(x) dx $. (It's just the area to the left of the outcome).
- **Independence:** Berkowitz tests this by checking the $\rho$ (autocorrelation) coefficient of the $z$-scores. If $\rho \neq 0$, the model is "lagging."
- **Uniformity:** A "U-shaped" PIT histogram means the model is **Over-stating** volatility (too many results in the middle, too few in the ends).
- **Humped PIT Histogram:** Means the model is **Under-stating** volatility (too many outliers).
- **Crusty PITs:** PIT values are usually calculated using "Realized" P/L.
- **LR Test Degrees of Freedom:** 
    - Testing Mean/Vol only = 2 d.f.
    - Testing Mean/Vol/Independence = 3 d.f.
- **The "Transformation" sequence:**
    1.  Outcome ($y_t$) $\rightarrow$ PIT ($u_t$) via Model CDF.
    2.  PIT ($u_t$) $\rightarrow$ Z-score ($z_t$) via Inverse Normal CDF ($\Phi^{-1}$).
- **Why inverse normal?** Because we have 100 years of math built for testing if things are Normal.
- **Sample Size:** PIT tests require **More Data** than simple backtesting because they are trying to prove the shape of a curve, not just count dots.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
