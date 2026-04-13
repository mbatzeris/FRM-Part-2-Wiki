# R4 — Backtesting VaR Models

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.4.1` | **The Backtest Goal:** To verify a VaR model's accuracy by comparing the number of "Exceptions" (actual loss > VaR) against the expected number ($p \cdot T$). | `[OPS/REG]` | It’s a "Report Card" for your risk model. If you say you’ll only be late to work 5% of the time, and you’re late every Monday, your model is wrong. |
| `P.4.2` | **Unconditional Coverage (Kupiec):** Tests only the **Frequency** of exceptions. It uses a binomial distribution to see if the total number of breaches is statistically consistent with the confidence level. | `[MTH/REG]` | You don't care *when* the rain happens, just if it rained as many inches as the weather man predicted over the whole month. |
| `P.4.3` | **Independence Test (Christoffersen):** A good model should not have "Clusters" of exceptions. If one breach happens today, the probability of one tomorrow should not change. | `[MTH/THE]` | Exceptions should be like "stray raindrops," not a "hurricane." If losses come in streaks, your model isn't updating fast enough for market stress. |
| `P.4.4` | **Type I vs. Type II Errors:** Type I is rejecting a "True" model (Bad Luck). Type II is accepting a "False" model (A failure of integrity). In risk management, **Type II is the deadly error**. | `[MTH/OPS]` | Type I: Firing a good employee because they had one bad day. Type II: Keeping a thief because they haven't been caught yet. The thief is more dangerous. |
| `P.4.5` | **The Basel Traffic Light:** A regulatory rule for a 250-day window (99% VaR). Green (0-4), Yellow (5-9), and Red (10+ exceptions). This determines the capital multiplier $k$ (3.0 to 4.0). | `[REG/OPS]` | It’s the "Regulatory Speed Limit." If you get too many tickets (Exceptions), the policeman (Regulator) makes you pay more to stay on the road. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a model has zero exceptions in 250 days at 95% confidence:** The model is actually **Too Conservative**. It is wasting capital by over-estimating the risk. (Kupiec would reject it for having *too few* exceptions).
- **Variable Flip: If all 5 exceptions in a year happen in the SAME WEEK:** The **Christoffersen Test** will fail (Independence breach), even if the **Kupiec Test** passes (Frequency is fine). The model is failing to capture volatility clustering.
- **Variable Flip: If backtesting uses "Actual P&L" instead of "Hypothetical P&L":** Results are **Noisy** due to intraday trading, fees, and commissions. Hypothetical P&L (holding today's portfolio frozen) is preferred for verifying model integrity.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Basel Window:** 250 days / 99% VaR. | **Basel Window:** 100 days / 95% VaR (NO). |
| **Yellow Zone Causes:** Bad Luck, Model Integrity, Intraday trading. | **Yellow Zone Causes:** High Interest Rates (NO). |
| **Conditional Coverage:** Frequency + Independence. | **Unconditional Coverage:** Frequency + Independence (NO: just Frequency). |

## 4. Directional Intuition
- **Confidence Level $\uparrow$ (99% vs 95%) $\rightarrow$ Statistical Power of Backtest $\downarrow$:** At high confidence, you have very few expected exceptions, making it harder to prove a model is "bad" vs "unlucky."
- **Number of Exceptions $\uparrow \rightarrow$ Capital Multiplier $k \uparrow$:** More failures mean the regulator forces you to hold more "safety" cash.
- **Sample Size ($T$) $\uparrow \rightarrow$ Type II Error Probability $\downarrow$:** The longer the history you check, the harder it is for a "bad" model to hide.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Deadly" Error:** Always remember **Type II** (Failed to reject a bad model) is the one that sinks banks.
- **Kupiec's Null Hypothesis:** $H_0: \text{The model is correct}$. If you "Reject $H_0$," you are saying the model is bad.
- **Intraday Trading:** This is a #1 cause of "Fake" exceptions. The trader made/lost money *after* the VaR was calculated.
- **The Multiplier $k$:** The minimum is **3.0**. The maximum is **4.0** (when exceptions hit 10+).
- **Lopez & Blanco-Ihle:** These are **Magnitude** tests. Kupiec/Christoffersen only care *if* you breached; Lopez cares by *how much*.
- **Backtesting 95% vs. 99%:** Note that 95% has more "power" because it generates 12.5 exceptions/year vs 2.5 for 99%. Small samples are the enemy of backtesting.
- **Ghosting / Bad Luck:** Basel Category 1. It happens. If you are in the Yellow zone due to "Bad Luck," the penalty is lower than for "Model Failure."
- **The 4 Basel Categories of Failure:**
    1.  Model Integrity (Formula is wrong).
    2.  Model Accuracy (Formula is okay, but parameters are stale).
    3.  Intraday Trading (The "Noise").
    4.  Bad Luck (Statistical outlier).
- **Independence Test:** Uses a $2 \times 2$ contingency table ($0 \rightarrow 0, 0 \rightarrow 1, 1 \rightarrow 0, 1 \rightarrow 1$).
- **Sample Period:** Standard is **250 days** (approx. 1 business year).
- **The multiplier k:** $ k = 3 + \text{plus factor} $. The plus factor goes from 0 to 1.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
