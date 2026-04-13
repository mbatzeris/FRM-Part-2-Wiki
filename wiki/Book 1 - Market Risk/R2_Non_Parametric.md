# R2 — Non-Parametric Approaches

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.2.1` | **Bootstrapping HS:** A technique of re-sampling with replacement from the historical dataset to create many simulated "paths." This allows for the estimation of the **Standard Error** of the VaR, showing how much the estimate might vary. | `[MTH/OPS]` | It’s like drawing names from a hat, putting them back, and drawing again. Doing this 1000 times gives you a "range" of possible outcomes rather than just one single number. |
| `P.2.2` | **Age-Weighting (Boudoukh):** Recognizes that recent data is more relevant than old data. It uses a decay factor ($\lambda$) to give exponential weights to observations. Recent days get more "vote" in the final VaR than days from a year ago. | `[MTH/THE]` | It’s like a "weighted GPA." This semester's grades matter more to your employer than your middle school report card. |
| `P.2.3` | **Volatility-Weighting (Hull-White):** Adjusts historical returns to reflect today's volatility: $r_{adj} = r_{hist} \cdot (\sigma_{today} / \sigma_{hist})$. This "scales up" old calm days if the market is currently crazy, and vice versa. | `[MTH/THE]` | If you are trying to guess how much a car will vibrate at 100mph using data from a 20mph drive, you have to "scale up" the shaking. |
| `P.2.4` | **Filtered Historical Simulation (FHS):** The "Gold Standard" of HS. It uses a volatility model (like GARCH) to remove current trends (standardize), bootstraps the "random noise" residuals, and then re-adds current volatility. | `[MTH/OPS]` | You "clean" the data to get the pure randomness, shuffle it, and then "reactivate" it with today's market temperature. |
| `P.2.5` | **Ghost Effects:** A major flaw of traditional HS where an extreme event "drops out" of the look-back window (e.g., after 250 days), causing the VaR to suddenly plunge even if market risk hasn't changed. | `[THE/MKT]` | If you only remember the last 10 days of weather, then on day 11 after a hurricane, you’ll suddenly think "Hurricanes are impossible!" because it's no longer in your memory. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the decay factor ($\lambda$) is set to 1.0 (Age-Weighting):** The weights become uniform ($1/n$), and the model reverts to **Simple Historical Simulation**.
- **Variable Flip: If Current Volatility is LOWER than Historical Volatility (Hull-White):** The adjusted returns will be **Lower** than the original returns, leading to a smaller VaR than traditional HS.
- **Variable Flip: If a "Permissionless" pair trade is executed (Correlation-Weighting):** Traditional HS ignores the breakdown in correlations. Correlation-weighting is required to capture the risk that assets which used to move together might suddenly diverge.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Age-Weighting:** Adjusts for time decay. | **Volatility-Weighting:** Adjusts for time decay (NO: adjusts for market stress). |
| **Bootstrapping:** Re-sampling *with* replacement. | **Bootstrapping:** Re-sampling *without* replacement (NO: that's just shuffling). |
| **Non-Parametric Advantage:** Handles skew and fat tails. | **Non-Parametric Advantage:** Fast response to new regimes (NO: it's notoriously slow/ghosted). |

## 4. Directional Intuition
- **Decay Factor ($\lambda$) $\downarrow \rightarrow$ Sensitivity to Recent Data $\uparrow$:** A smaller lambda means you discard the past faster.
- **Market Volatility $\uparrow \rightarrow$ Vol-Weighted VaR $\uparrow \uparrow$:** Because it scales all historical data by the new, higher volatility, the VaR jumps immediately.
- **Sample Window Length $\uparrow \rightarrow$ Ghost Effect Sensitivity $\downarrow$:** The longer your "memory," the less impact a single day dropping out has on the final number.

## 5. Ambiguity Traps (Anti-Decoder)
- **Bootstrap sampling:** Why "with replacement"? Because if you don't, you just get the same 250 numbers in a different order, which doesn't change the 5th percentile.
- **The "Max Loss" Trap:** Note that traditional HS can **never** predict a loss larger than the worst day in its historical window.
- **Hull-White Formula:** $r_{t,i} = r_i \cdot \frac{\sigma_t}{\sigma_i}$. Remember: Target ($\sigma_{now}$) is in the **numerator**.
- **FHS Complexity:** It is the combo of GARCH + Bootstrap. It's the most "modern" non-parametric tool.
- **Correlation weighting:** This is more general than Vol-weighting because it handles the **Covariance Matrix** ($\Sigma$), not just individual variances.
- **Decay Factor persistent:** If $\lambda$ is close to 1, the model is "stubborn" and changes slowly.
- **Ghost Effects vs. Regression to the Mean:** Ghost effects are a *methodology error* (the data window moving), not a market phenomenon.
- **Non-Parametric Data:** No covariance matrix estimate is required for *Simple* HS, but it IS required for *Correlation-Weighted* HS.
- **Stationarity:** Non-parametric methods implicitly assume the past is a good guide to the future (Stationarity). If the world changes (Structural Break), HS is useless.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
