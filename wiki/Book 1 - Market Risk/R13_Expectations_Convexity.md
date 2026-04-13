# R13 — Expectations, Risk Premium, and Convexity

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.13.1` | **The Expectations Component:** In a simple world with no risk or convexity, the forward rate is just the market’s best guess of what the short-term rate will be in the future. | `[THE/MTH]` | It’s the "Plain Vanilla" forecast. If you think rates will be 5% next year, the 1-year forward rate should be 5%. |
| `P.13.2` | **The Risk Premium ($\lambda$):** Risk-averse investors demand extra yield to compensate for the danger of holding long-term bonds (Duration risk). This premium is proportional to duration. | `[MKT/THE]` | It’s the "Danger Pay." The longer you have to wait for your money, the more "Danger Pay" (yield) you demand because more things can go wrong. |
| `P.13.3` | **Jensen’s Inequality & Convexity:** Because bond prices are convex, the average of prices is higher than the price of the average yield ($E[P(y)] > P(E[y])$). This leads to a **Convexity Bias** that lowers forward rates. | `[MTH/THE]` | Imagine you're betting on a coin flip. If it's heads, you win $100. If tails, you lose $50. The average outcome is $25 profit, even if the "average flip" is zero. This "extra profit" from volatility is Convexity. |
| `P.13.4` | **Expected Return Decomposition:** For a risk-averse investor, the expected return is $r_0 + (\lambda \times Duration)$. It skips the convexity benefit because market prices already adjust (lower the rate) to account for it. | `[MTH/REG]` | Your total "paycheck" (Return) is just the basic rate plus your danger pay. You don't get extra for the "Convexity" because the market already "charged" you for it by making the bond's yield lower. |
| `P.13.5` | **Forward Rate Composition:** $f = E(\Delta r) + (\lambda \times Dur) - Convexity\;Effect$. | `[MTH]` | The forward rate is the "Soup." It’s made of expectations and risk premia, but then you "subtract" the value of convexity because everyone wants that "free profit" feature, which drives the yield down. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If investors are Risk-Neutral ($\lambda = 0$):** The expected return on any bond, regardless of duration, is simply the **Short-term Risk-free Rate ($r_0$)**.
- **Variable Flip: If Interest Rate Volatility is ZERO:** The **Convexity Effect** becomes zero. Jensen’s Inequality disappears, and $E[P] = P(E[r])$.
- **Variable Flip: If a bond has a very high Duration and Maturity:** The **Convexity Bias** becomes the dominant factor, significantly dragging the forward rate *below* the expected future spot rate.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Convexity Effect:** Lowers yield/forward rates. | **Convexity Effect:** Raises yield/forward rates (NO: it raises the *price*, which lowers the *yield*). |
| **Risk Premium:** Proportional to Duration. | **Risk Premium:** Proportional to Convexity (NO: it compensates for duration). |
| **Jensen's Inequality:** $E[f(x)] > f(E[x])$ for convex functions. | **Jensen's Inequality:** $E[f(x)] < f(E[x])$ (NO: that’s for concave functions). |

## 4. Directional Intuition
- **Volatility ($\sigma$) $\uparrow \rightarrow$ Convexity Value $\uparrow \rightarrow$ Forward Rate $\downarrow$:** More "market shaking" makes the convexity "free profit" more valuable, driving the forward rate down.
- **Maturity $\uparrow \rightarrow$ Convexity $\uparrow \uparrow$:** Long-term bonds have much deeper "curves" in their price-yield chart, making them highly sensitive to convexity bias.
- **Risk Aversion $\uparrow \rightarrow$ Risk Premium ($\lambda$) $\uparrow \rightarrow$ Forward Rate $\uparrow$:** If investors are more scared, they demand a higher forward rate today to buy the bond.

## 5. Ambiguity Traps (Anti-Decoder)
- **Return vs. Rate:** This is the #1 trap. 
    - Convexity **Increases** the expected **Return** (good for you). 
    - Convexity **Decreases** the **Forward Rate** (the market yield is lower because everyone wants the convexity).
- **Jensen’s Inequality:** $Price = \frac{1}{(1+r)^2}$. Since this function is "U-shaped" (convex), the "Average of Prices" > "Price of Average."
- **Risk Premium Unit:** $\lambda$ is usually expressed as **Basis Points per unit of Duration**.
- **Expectations Hypothesis:** The "Pure" version assumes $\lambda = 0$ and Convexity = 0.
- **The "Belly" of the Curve:** Note how convexity can cause the long-end of the yield curve to "dip" or invert if volatility is high enough (Convexity Bias > Risk Premium).
- **Duration's Role:** It acts as the "Scaling Factor" for the risk premium. $7 \text{ units of duration} \times 15 \text{ bps premium} = 105 \text{ bps total adjustment}$.
- **Forward Rate Components:** 
    1.  Expectation (Direction).
    2.  Risk Premium (Distance/Time).
    3.  Convexity (Noise/Curvature).
- **Price-Yield Function:** $P(y) = \frac{C}{(1+y)} + \dots $. Because $y$ is in the denominator, the second derivative is positive, proving it is convex.
- **Volatility's Two-Faced Nature:** In this reading, volatility *increases* returns (via convexity) but doesn't change the "Risk-Neutral" expected return (which stays at $r_0$).
- **The "Value of Convexity":** The difference between the forward rate and the rate implied by pure expectations. $Value = 0.5 \times \text{Convexity} \times \sigma^2$.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
