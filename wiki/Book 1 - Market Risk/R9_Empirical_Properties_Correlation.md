# R9 — Empirical Properties of Correlation

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.9.1` | **Recessionary Correlation Spikes:** Empirical data shows that equity correlations reach their **Highest Levels** during recessions. In a crash, all stocks tend to drop together (the "Nowhere to Hide" effect). | `[MKT/ECO]` | On a sunny day, people in the park go in every direction. When it starts pouring rain, everyone runs toward the exact same shelter at the exact same time. |
| `P.9.2` | **Correlation Volatility:** While correlation peaks in a recession, **Correlation Volatility** is actually highest during **Normal** economic periods. In expansionary periods, correlation volatility is low. | `[MKT/ECO]` | In a crisis, you know correlations will be high (stable high). In an expansion, you know they'll be low (stable low). It's in the "middle" where the relationship is most "fidgety." |
| `P.9.3` | **Mean Reversion of Correlation:** Correlation is not a "random walk." It tends to revert to a long-run mean. The speed of this return is called the **Mean Reversion Rate ($a$)**. | `[MTH/THE]` | It’s like a rubber band. You can stretch correlations apart during a boom, but they eventually snap back to their normal relationship. |
| `P.9.4` | **Correlation Autocorrelation:** The relationship between today's correlation and yesterday's. Mathematically: $\text{Autocorrelation} + \text{Mean Reversion Rate} = 100\%$. | `[MTH]` | If the rubber band is "tight" (High mean reversion), history doesn't matter much. If it's "loose" (High autocorrelation), today will look a lot like yesterday. |
| `P.9.5` | **Best-Fit Distributions:** 
- **Equities/Defaults:** Best fit by the **Johnson SB** distribution.
- **Bonds:** Best fit by the **GEV** (Generalized Extreme Value) distribution. | `[MTH/REG]` | Correlations don't follow a bell curve (Normal). They have their own unique "shapes" that depends on the asset class. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a risk manager assumes a "Normal Distribution" for Equity Correlations:** The VaR model will be **Severely Flawed**. The Johnson SB distribution fits significantly better; using the Normal distribution ignores the "Real World" thickness of correlation tails.
- **Variable Flip: If the Mean Reversion Rate is 0:** Autocorrelation is 100%. This implies that correlation is a **Random Walk**, which contradicts empirical findings that market relationships eventually normalize.
- **Variable Flip: If you are in an Expansionary period $(\text{GDP} > 3.5\%)$:** Expect both correlation levels and correlation volatility to be at their **Lowest**. This is the safest time for diversification.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Recessions:** High $\rho$, High-ish $\rho$-Vol. | **Recessions:** Low $\rho$, High $\rho$-Vol (NO). |
| **Normal Periods:** Highest $\rho$-Vol. | **Expansionary Periods:** Highest $\rho$-Vol (NO: lowest). |
| **Bond Correlations:** Fit by GEV. | **Equity Correlations:** Fit by GEV (NO: Johnson SB). |

## 4. Directional Intuition
- **Market Stress $\uparrow \rightarrow$ Correlation Level $\uparrow$:** Panic breeds "herd behavior" across all asset classes.
- **Time to Mean $\downarrow \rightarrow$ Mean Reversion Rate $a \uparrow$:** A "snap" return to normal means the current deviation is very short-lived.
- **Autocorrelation $\uparrow \rightarrow$ Mean Reversion Rate $a \downarrow$:** If today is a "copy" of yesterday, it takes a long time to get back to the long-run average.

## 5. Ambiguity Traps (Anti-Decoder)
- **The 100% Rule:** $\text{Mean Reversion Rate} + \text{Autocorrelation} = 1.0$. This is a common calculation question. If $a=0.3$, then $\rho_{auto}=0.7$.
- **Johnson SB Distribution:** It's a "Flexible" distribution with 4 parameters. Know that it's the "King" for Equities and Defaults.
- **GEV for Bonds:** Why GEV? Because bond correlations often involve "extremes" (like interest rate pegs or massive flight-to-quality moves).
- **Correlation Volatility:** Don't confuse "High Correlation" with "High Correlation Volatility." They usually peak at different times.
- **Regression Formula:** $\Delta \rho = \text{Intercept} - (\text{Mean Reversion Rate} \times \rho_{t-1})$. The negative sign on the lag is the key.
- **Average Bond Correlation:** Higher (~42%) than Equity (~32%) or Default (~30%). Bonds are more "Macro-driven" and thus more unified.
- **The "Worst" Recession (2007-2009):** Note that correlation volatility actually *dropped* right before most recessions.
- **Survival Bias in Defaults:** Remember from R8—this impacts the empirical correlation of survival across time.
- **Normal Distribution:** It’s actually a "Good Fit" for bonds, even if GEV is the "Best Fit." But it’s "Poor" for equities.
- **GDP Thresholds:** GARP uses specific ranges (Expansion > 3.5%, Normal 0-3.5%, Recession < 0).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
