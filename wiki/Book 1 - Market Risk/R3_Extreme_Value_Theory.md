# R3 — Parametric Approaches (II): Extreme Value Theory (EVT)
**Exam Priority:** 🟡 Medium (1-2 questions) (EVT)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.3.1` | **The Limit Law of Extremes:** Just as the CLT says sums of variables converge to a Normal distribution, the **Fisher-Tippett Theorem** says the *maximums* of variables converge to a **Generalized Extreme Value (GEV)** distribution. | `[MTH/THE]` | Normal math is for "Typical" days. EVT is the math of "The Worst Possible Days." It’s the physics of the crash, not the driving. |
| `P.3.2` | **Block Maxima vs. POT:** Block Maxima (GEV) takes the worst day of each year. **Peaks Over Threshold (POT)** models every day that is worse than a set level $u$. POT is usually more efficient because it uses more of the extreme data. | `[MTH/OPS]` | Block Maxima is like only looking at the biggest wave of each year. POT is like looking at *every* wave bigger than 20 feet. You get more data on how big waves behave. |
| `P.3.3` | **Generalized Pareto Distribution (GPD):** The specific distribution used in POT to model the "Tail." It is defined by the **Scale ($\beta$)** and **Shape ($\xi$)** parameters. | `[MTH]` | GPD is the "magnifying glass" used to study only the far right edge of the chart. |
| `P.3.4` | **The Shape Parameter ($\xi$):** The most critical value. If $\xi > 0$, the distribution has "Fat Tails" (Fréchet). If $\xi = 0$, it's the Gumbel (Thinner tails). If $\xi < 0$, it's bounded (Weibull). Financial data is almost always $\xi > 0$. | `[MTH/THE]` | It’s the "Curvature" of the disaster. A positive $\xi$ means that "Extreme" events are much more likely than a bell curve would suggest. |
| `P.3.5` | **The Hill Estimator:** A simple, non-parametric formula to estimate the tail index ($1/\xi$) by using the log-distance of the $k$ most extreme observations from the threshold. | `[MTH]` | You look at the "distance" between the 100th worst day and the 1st worst day to guess how steep the "cliff" is. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Threshold ($u$) is set too LOW:** The data will contain "Normal" observations, and the GPD logic will **Fail** because you aren't just looking at the extremes anymore.
- **Variable Flip: If the Threshold ($u$) is set too HIGH:** You will have so few data points ($n_u$) that the **Standard Error** of your estimate will skyrocket, making the result meaningless.
- **Variable Flip: If $\xi = 1$:** The distribution has an "infinite mean." This means the tail is so fat that the average of the losses could literally be anything. (Extreme market chaos).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **POT:** Uses the Generalized Pareto Distribution (GPD). | **POT:** Uses the GEV distribution (NO: GEV is for Block Maxima). |
| **Tail Index ($\alpha$):** Equal to $1/\xi$. | **Tail Index ($\alpha$):** Equal to $\xi$ (NO: it’s the reciprocal). |
| **Multivariate EVT:** Requires Copulas. | **Multivariate EVT:** Requires Correlation coefficients (NO: correlation fails at the tails). |

## 4. Directional Intuition
- **Sample Size ($n$) $\uparrow \rightarrow$ Convergence to GEV $\uparrow$:** The more years of data you have, the more you can trust the Fisher-Tippett limit.
- **Threshold ($u$) $\uparrow \rightarrow$ Model Bias $\downarrow$ (but Estimation Variance $\uparrow$):** A higher threshold is more "Pure" to the theory but "Messier" for the calculator.
- **Shape Parameter ($\xi$) $\uparrow \rightarrow$ Tail Fatness $\uparrow$:** The larger the $\xi$, the more likely you are to see "Impossible" huge losses.

## 5. Ambiguity Traps (Anti-Decoder)
- **Extreme VaR Formula:** $VaR_p = u + \frac{\beta}{\xi} \left[ \left( \frac{n}{n_u}(1-p) \right)^{-\xi} - 1 \right]$. 
    - $n$ = total observations.
    - $n_u$ = observations > threshold.
- **EVT vs. Normal:** EVT **always** results in a higher VaR for high confidence levels (99.9%) because it respects the fat tails that the Normal distribution ignores.
- **The "Tail Index":** Pay attention to whether the question asks for the **Shape Parameter ($\xi$)** or the **Tail Index ($\alpha$)**. $ \alpha = 1/\xi $.
- **GEV Types:**
    - **Fréchet ($\xi > 0$):** Heavy tail (Finance).
    - **Gumbel ($\xi = 0$):** Light tail (Normal-ish).
    - **Weibull ($\xi < 0$):** Short/Finite tail (Doesn't happen in finance).
- **Copulas in EVT:** Why? Because during a crash, correlations "break." Copulas allow us to model how assets "crash together" without assuming they move together on normal days.
- **Hill Estimator Usage:** It is **Conditional** on the chosen threshold $k$.
- **Standard Error:** High $u$ = High SE. Low $u$ = High Bias. This is the "Goldilocks problem" of EVT.
- **Fisher-Tippett Theorem:** This is the "CLT for Extremes."
- **Pickands-Balkema-de Haan Theorem:** This is the theorem that proves the **GPD** is the correct limit for POT.
- **Convergence:** Note that convergence to GEV is **slow**. You need a lot of "Blocks" or "Exceedances" to get it right.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
