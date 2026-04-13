# R14 — The Art of Term Structure Models: Drift

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.14.1` | **Model 1 (No Drift):** The simplest model ($dr = \sigma dw$). It assumes interest rates are just a random walk with no direction. | `[MTH/THE]` | It’s like a drunk person walking in a straight line. They might step left or right, but they aren't trying to go anywhere specific. |
| `P.14.2` | **Ho-Lee Model (Time-Dependent Drift):** A model that allows the "direction" of rates ($\lambda$) to change at every point in time. This allows the model to perfectly fit the current yield curve. | `[MTH/THE]` | You can "program" the drunk person to follow a specific path on the ground, but they still wobble with the same intensity $(\sigma)$ the whole way. |
| `P.14.3` | **Vasicek Model (Mean Reversion):** Assumes that interest rates are pulled toward a long-run equilibrium level ($r_l$). The further away the rate is, the stronger the pull. | `[MTH/THE]` | The drunk person is now attached to a "Bungee Cord" anchored at 5%. If they wander too far, the cord pulls them back. |
| `P.14.4` | **Half-Life ($\tau$):** The time it takes for an interest rate shock to get halfway back to its long-run mean. It is calculated as $\ln(2) / k$. | `[MTH]` | If you pour cold water into a hot bath, how many minutes before the bath is back to a "lukewarm" midpoint? |
| `P.14.5` | **Volatility Term Structure:** Model 1 and Ho-Lee predict "Flat Volatility" (all maturities are equally risky). The Vasicek model correctly predicts that long-term volatility should be lower than short-term volatility. | `[MKT/THE]` | In a mean-reverting world, the long-term is "predictable" (it's the mean). The short-term is "chaotic" (where the shocks happen). |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Mean Reversion Speed ($k$) is VERY HIGH:** Any economic shock (like a sudden inflation spike) will be **Short-lived**. Rates will snap back to normal almost immediately.
- **Variable Flip: If a model assumes Normal distribution (Models 1, 2, Ho-Lee, Vasicek):** There is always a statistical probability of **Negative Interest Rates**. This is a major theoretical limitation (though less of a concern in the NIRP era).
- **Variable Flip: If you use Model 1 to predict the yield curve:** Every change in the short rate will result in a **Perfectly Parallel Shift**. The model cannot handle "Twists" or "Butterfly" spreads.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Ho-Lee:** Arbitrage-free (fits current prices). | **Vasicek:** Arbitrage-free (NO: it’s an equilibrium model). |
| **PC1 (Level):** Only shift allowed in Model 1. | **Twist:** Allowed in Model 1 (NO). |
| **Short-lived News:** High $k$ (Mean Reversion). | **Long-lived News:** High $k$ (NO: it’s Low $k$). |

## 4. Directional Intuition
- **Distance from Mean $\uparrow \rightarrow$ Drift Velocity $\uparrow$:** The further you are from the bungee anchor, the faster you get pulled back.
- **Mean Reversion $k \uparrow \rightarrow$ Forward Rate Sensitivity to Short Rate $\downarrow$:** If the "Pull" is strong, a jump in the 1-month rate doesn't change the 30-year rate much (because it'll be back to normal by then).
- **Volatility ($\sigma$) $\uparrow \rightarrow$ Expected Price (Convexity) $\uparrow$:** (Reviewing R13—this applies to the trees in R14 too).

## 5. Ambiguity Traps (Anti-Decoder)
- **Recombining Trees:** 
    - Model 1, Model 2, and Ho-Lee **recombine**. 
    - Vasicek theoretically **does NOT** (because the drift depends on the *level* of the rate, making "Up-Down" different from "Down-Up").
- **Arbitrage-free vs. Equilibrium:** 
    - **Ho-Lee** is Arbitrage-free (Starts with market prices). 
    - **Vasicek** is Equilibrium (Starts with economic assumptions).
- **Ho-Lee at Time 2:** The middle node is $r_0 + (\lambda_1 + \lambda_2)dt$. Note that it's the *sum* of the drifts of the previous periods.
- **The "Half-Life" Formula:** $\tau = \frac{0.693}{k}$. If $k=0.4$, then $\tau = 1.73$ years.
- **Volatility Decay:** This is the hallmark of Vasicek. Short rate vol > Long rate vol.
- **Negative Rates:** Normal models (like Model 1) allow them. One fix is to use a "Floor" at 0.0, but this makes the math messy.
- **Exogenous Shocks:** In Model 1, a shock to $r$ affects the entire curve. In Vasicek, it mainly affects the "Front End."
- **Calibration:** Ho-Lee is calibrated to the **Forward Curve**. Vasicek is calibrated to **Long-run history**.
- **Model 2 Drift:** $\lambda$ is constant. It can move the whole curve up/down over time like an escalator.
- **Ho-Lee "Generalization":** Model 1 and Model 2 are just Ho-Lee models where $\lambda(t)$ is set to zero or a constant.
- **Economic Interpretation:** Why use Vasicek? Because central banks usually have a "Target Rate" they want to return to (Standard behavior).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
