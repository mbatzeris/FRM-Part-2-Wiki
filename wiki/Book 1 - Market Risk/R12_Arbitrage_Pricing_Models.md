# R12 — Arbitrage Pricing Models

**Exam Priority:** 🟡 Medium (1-2 questions) with Term Structure Models

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.12.1` | **Backward Induction:** The process of valuing a bond by starting at the maturity nodes (where value is known/Par) and working backward through the binomial tree to "Today," discounting at each node using the one-period rate. | `[MTH/THE]` | It’s like tracing your ancestry. You know where you are now, but to find out "how much you’re worth," you look at the potential of your descendants and bring it back to yourself. |
| `P.12.2` | **Risk-Neutral Valuation:** Using adjusted probabilities (where investors are assumed to be risk-neutral) and the risk-free rate for discounting to ensure the tree-generated price exactly matches the current market price. | `[MTH/THE]` | We assume everyone is "chill" about risk so that the math doesn't get cluttered with human emotions. This "chill" price should equal the real market price. |
| `P.12.3` | **Negative Convexity (Callable Bonds):** As yields fall, the issuer is more likely to call the bond. This "caps" the price gains for the investor. The price-yield curve flattens and bends the "wrong" way. | `[MKT/THE]` | Usually, as rates drop, bond prices "jump" up. But if the issuer can take the bond away at $102, the price won't go above $102 no matter how much rates drop. It’s like a ceiling on your profit. |
| `P.12.4` | **Option-Adjusted Spread (OAS):** The constant spread added to every node in the interest rate tree to make the model price equal the market price. It represents the "True" extra yield of the bond after removing the noise of the embedded option. | `[MTH/REG]` | It’s the "Purity Filter." It strips away the value of the "Call" or "Put" to show you if the bond itself is a good deal compared to a Treasury. |
| `P.12.5` | **BSM Limitations for Bonds:** The Black-Scholes-Merton model fails for bonds because it assumes constant interest rates and infinite price bounds, while bonds have changing rates and "Pull to Par" (they must equal 100 at maturity). | `[THE/MTH]` | BSM is like a "Space Rocket" (goes anywhere). A bond is like a "Train" (it has to arrive at the station at 100 on a specific date). You can't use rocket math for a train. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Option-Adjusted Spread (OAS) is ZERO:** The bond is priced perfectly relative to the benchmark according to the tree.
- **Variable Flip: If a bond is "Putable":** It exhibits **Enhanced Positive Convexity**. As yields rise, the price won't fall below the put floor, protecting the investor.
- **Variable Flip: If you use a very large time step (e.g., 1 year) in a tree:** The model becomes **Less Accurate**. Smaller steps (e.g., daily) better capture the continuous nature of interest rate movements but increase computational "grunt work."

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Callable Bond:** Negative convexity at low yields. | **Callable Bond:** Negative convexity at high yields (NO: behaves like normal bond at high yields). |
| **OAS:** Spread after stripping the option. | **OAS:** Spread including the option (NO: that's the Z-spread). |
| **Backward Induction:** Calculates value Today. | **Forward Induction:** Calculates value Today (NO: that's for calibration). |

## 4. Directional Intuition
- **Interest Rate Volatility $\uparrow \rightarrow$ Call Option Value $\uparrow \rightarrow$ Callable Bond Price $\downarrow$:** If rates might swing wildly, the issuer’s right to "buy it back" becomes much more valuable, hurting the investor.
- **Maturity $\downarrow \rightarrow$ Pull to Par $\uparrow \rightarrow$ Bond Price Volatility $\downarrow$:** As the "End Date" approaches, there is less time for things to go wrong, so the price calms down.
- **Market Price < Model Price $\rightarrow$ OAS must be Increased:** You need a higher "extra yield" to drag the model's value down to match the cheap market price.

## 5. Ambiguity Traps (Anti-Decoder)
- **OAS vs. Z-Spread:** 
    - **OAS** = "Option-Free" spread. 
    - **Z-Spread** = Full spread. 
    - For Callable: $Z > OAS$. For Putable: $Z < OAS$.
- **Negative Convexity:** This ONLY happens for callable/prepayable bonds when rates are low. At high rates, they have positive convexity just like normal bonds.
- **Price Compression:** The official term for the "leveling off" of the price-yield curve for callable bonds.
- **Risk-Neutral Probabilities:** Usually 0.5 for "Up" and 0.5 for "Down" in FRM tree problems, but real-world trees require specific calculations to match the term structure.
- **The "Belly" of the Tree:** Remember that in a **Recombining** tree, an "Up-Down" move results in the same rate as a "Down-Up" move. In a **Non-Recombining** tree, they are different (exploding complexity).
- **Embedded Options:**
    - Issuer holds the Call (Bad for you).
    - Investor holds the Put (Good for you).
- **Reinvestment Risk:** Callable bonds have HIGHER reinvestment risk because the issuer calls them exactly when rates are low and you don't want your money back.
- **BSM Volatility Assumption:** BSM assumes $\sigma$ is constant. Bonds have "Volatility Decay"—the further from maturity, the more volatile the price.
- **Backward Induction Step:** $Value = \frac{0.5 \times (V_{up} + C) + 0.5 \times (V_{down} + C)}{1 + r}$. Don't forget to **Add the Coupon** $(C)$ at each node before discounting.
- **OAS and Credit Risk:** OAS captures liquidity risk and credit risk. It doesn't mean the bond has "zero spread" over LIBOR/Treasury.
- **Constant Maturity Swap (CMS):** Swapping a standard floating rate (SOFR) for a long-term Treasury rate.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
