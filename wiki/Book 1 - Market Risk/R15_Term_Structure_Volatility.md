# R15 — The Art of Term Structure Models: Volatility

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.15.1` | **Time-Dependent Volatility:** Models where $\sigma$ changes over time ($\sigma_t$). This is used to calibrate the model to match the prices of liquid interest rate options like Caps and Floors. | `[MTH/THE]` | It’s like a weather forecast that predicts the wind will be "extra gusty" only between 2 PM and 4 PM. |
| `P.15.2` | **The CIR Model (Level-Dependent Vol):** The Cox-Ingersoll-Ross model makes volatility proportional to the square root of the interest rate ($\sigma \sqrt{r}$). | `[MTH/THE]` | When the "Market Temperature" is high, the "Fever" (Fluctuations) gets worse. When rates are near zero, reality stays very calm. |
| `P.15.3` | **The Zero-Bound (CIR vs. Vasicek):** Because $\sigma \sqrt{r}$ goes to zero as $r \rightarrow 0$, the CIR model (combined with mean reversion) theoretically prevents interest rates from becoming negative. | `[THE/MTH]` | There is a "Gravity Field" at 0%. As you get closer, your speed drops to zero, and the mean-reversion pull eventually drags you back up. You can't cross the line. |
| `P.15.4` | **Lognormal Models (Black-Derman-Toy):** Models the natural log of rates ($d \ln r$). This also prevents negative rates and ensures that rates move "multiplicatively" rather than additively. | `[MTH/THE]` | Instead of saying "Rates went up by 1%", you say "Rates went up by a factor of 1.1x." You can never reach zero by multiplying by positive numbers. |
| `P.15.5` | **Basis Point Volatility vs. Yield Volatility:** 
- **Normal Models:** Basis point vol is constant; Yield vol decreases as $r \uparrow$.
- **Lognormal Models:** Yield vol is constant; Basis point vol increases as $r \uparrow$. | `[MTH/THE]` | In a lognormal world, a "10% move" when rates are 1% is tiny (0.1%). A "10% move" when rates are 10% is huge (1%). |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a model uses a Lognormal distribution:** It will **Never** produce negative interest rates.
- **Variable Flip: If interest rates are very HIGH in a CIR model:** The absolute volatility $(\sigma \sqrt{r})$ will be **High**, making the model's simulations much wider than at low rates.
- **Variable Flip: If a model is "Additive" (like Ho-Lee):** The effect of different shocks simply adds up $(r + \Delta r_1 + \Delta r_2)$.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **CIR Vol:** $\sigma \sqrt{r}$. | **Vasicek Vol:** $\sigma \sqrt{r}$ (NO: Vasicek vol is just $\sigma$). |
| **Lognormal:** Base for Black-Derman-Toy. | **Normal:** Base for Black-Derman-Toy (NO). |
| **Time-Dependent Vol:** Calibrated to Caps/Floors. | **Time-Dependent Drift:** Calibrated to Caps/Floors (NO: drift fits the yield curve). |

## 4. Directional Intuition
- **Interest Rate ($r$) $\uparrow \rightarrow$ CIR Basis Point Vol $\uparrow$ (at a decreasing rate):** As rates go up, the absolute shaking increases, but less and less for every extra 1%.
- **Interest Rate ($r$) $\uparrow \rightarrow$ Lognormal Basis Point Vol $\uparrow$ (linearly):** In lognormal math, the "shaking" is perfectly proportional to the level of the rate.
- **Step size ($dt$) $\downarrow \rightarrow$ Accuracy of Multiplicative Models $\uparrow$:** Lognormal approximations work best when the intervals are tiny.

## 5. Ambiguity Traps (Anti-Decoder)
- **CIR vs. Vasicek:** 
    - Both have mean reversion. 
    - Only **CIR** has level-dependent volatility ($\sqrt{r}$). 
    - Only **CIR** has a hard floor at zero.
- **Ho-Lee vs. Lognormal Drift:**
    - Ho-Lee is **Additive**.
    - Lognormal Drift is **Multiplicative**.
- **Recombining Trees again:** Lognormal models with mean reversion **do not** naturally recombine. You have to "Stitch" them back together by adjusting the time intervals.
- **The "Multiplicative" Trap:** $r_{up} = r_{down} \times e^{2\sigma \sqrt{dt}}$.
- **Variance Persistence:** Note that "Time-Dependent Volatility" means $\sigma$ is a function of *terminal time* $T$, not just the current rate.
- **Standard Deviation of Shocks:** In CIR, the variance of the change is $\sigma^2 r dt$.
- **Out-of-the-Money Options:** The choice between Normal and Lognormal models changes OTM option prices the most.
- **Short-term vs Long-term Vol:** Time-dependent vol is used when the market thinks the "next month" will be wilder than "next year."
- **Black-Derman-Toy (BDT):** A very common lognormal tree model used for options.
- **Basis Point (BP) Volatility:** In many exam questions, they will say "The model has a volatility of 80 bps." This implies a **Normal** distribution (constant BP vol).
- **Yield Volatility:** In others, they say "The model has a 20% volatility." This implies a **Lognormal** distribution (constant relative vol).
- **The "Sqrt(r)" effect:** In CIR, basis point volatility increases, but it increases *less than* in a lognormal model (where it's proportional to $r$, not $\sqrt{r}$).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
