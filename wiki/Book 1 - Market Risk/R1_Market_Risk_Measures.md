# R1 — Estimating Market Risk Measures

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.1.1` | **Historical Simulation (HS):** The simplest VaR method. It assumes the future will look exactly like the past by re-ordering historical P/L observations from worst to best and picking the $k^{th}$ percentile. | `[MTH/THE]` | It’s like looking at your last 100 days of spending to guess how much you might lose tomorrow. No fancy math, just counting "Bad Days." |
| `P.1.2` | **Parametric VaR (Normal):** Calculates VaR using mean ($\mu$) and standard deviation ($\sigma$). Formula: $VaR = -(\mu - z \sigma) \times W$. It assumes the bell curve is a perfect fit for market returns. | `[MTH]` | You assume market movements follow a predictable shape. If you know the average and the "spread," you can find the "danger zone" at the edge. |
| `P.1.3` | **Lognormal VaR:** Assumes that *log-returns* are normal. This prevents the "negative price" absurdity in traditional normal distributions and is better for long horizons. | `[MTH/THE]` | Stocks can't go below zero. Lognormal math respects this physical floor, whereas normal math thinks a stock price could technically be -$50. |
| `P.1.4` | **Expected Shortfall (ES):** Unlike VaR, which only gives the *threshold* of pain, ES calculates the *average* loss once that threshold is breached. It is the average of all tail VaRs. | `[MTH/OPS]` | VaR tells you: "You might lose at least $10M." ES tells you: "On the days you lose $10M, you actually lose an average of $15M." |
| `P.1.5` | **Coherence Criteria:** A "Coherent" risk measure must satisfy: (1) Monotonicity, (2) **Subadditivity**, (3) Positive Homogeneity, and (4) Translational Invariance. VaR fails subadditivity; ES passes. | `[THE/REG]` | Subadditivity means $Risk(A+B) \leq Risk(A) + Risk(B)$. VaR can sometimes say two safe things together are more dangerous than they are apart, which makes no sense for diversification. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a distribution has Fat Tails (Kurtosis > 3):** A Normal VaR will **Underestimate** the true risk. The "z-score" won't reach far enough into the tail to capture the extreme "Black Swan" events.
- **Variable Flip: If you merge two portfolios (A and B):** If using VaR, the total VaR might be greater than the sum of the individual VaRs (Violation of Subadditivity). If using ES, the total ES will ALWAYS be less than or equal to the sum.
- **Variable Flip: If arithmetic returns are used for long-term modeling:** The model will become **Biased** because it fails to account for the compounding effect (Geometric returns are mandatory for multi-period analysis).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **VaR:** Threshold loss at a confidence level. | **VaR:** Maximum possible loss (NO: losses can be much higher). |
| **ES:** Average loss in the tail. | **ES:** Maximum loss in the tail (NO). |
| **QQ Plot:** Linear line = Good fit. | **QQ Plot:** Vertical line = Fat tails (NO: curved ends indicate fat/thin tails). |

## 4. Directional Intuition
- **Confidence Level $\uparrow \rightarrow$ VaR $\uparrow$:** The more "sure" you want to be, the bigger the potential loss you must prepare for.
- **Sample Size ($n$) $\downarrow \rightarrow$ Standard Error $\uparrow$:** The less data you have, the "fuzzier" your risk estimate becomes.
- **Volatility ($\sigma$) $\uparrow \rightarrow$ VaR $\uparrow$:** More "market noise" pushes the edge of the bell curve further out.

## 5. Ambiguity Traps (Anti-Decoder)
- **VaR Interpetation:** "VaR is $10M at 95% confidence" means there is a **5% probability** of losing **$10M or MORE**.
- **Coherence - Subadditivity:** This is the #1 exam trap. VaR is NOT coherent because it can discourage diversification mathematically (though rarely in practice).
- **Geometric vs. Arithmetic:** Remember: $R_{log} = \ln(1 + R_{arith})$. Arithmetic returns are simple but "dangerous" for long time horizons.
- **Normal vs. Lognormal VaR:**
    - Normal VaR can be $ > 100\% $ (meaning you lose more than you own).
    - Lognormal VaR is capped at the total value of the investment.
- **Spectral Risk Measures:** This is the most general class. ES is a spectral measure where all tail quantiles have equal weight. A risk-averse person would give *more* weight to the worst outcomes.
- **QQ Plot Ends:**
    - If the empirical line is **Above** the diagonal at the far ends: **Fat Tails**.
    - If it's **Below**: **Thin Tails**.
- **Standard Error of Quantiles:** $ SE(q) = \sqrt{\frac{p(1-p)}{n \cdot f(q)^2}} $. Note that $SE$ increases as sample size $n$ decreases.
- **Tail Slicing:** ES is estimated by "slicing" the tail into $n$ pieces and averaging the VaR of each piece.
- **Risk Reporting:** We usually quote losses as **Positive values** (e.g., "The loss is $5M") to keep the numbers cleaner.
- **HS Bias:** Historical simulation is only as good as the look-back period. If the last 100 days were "calm," HS will be "blind" to an upcoming storm.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
