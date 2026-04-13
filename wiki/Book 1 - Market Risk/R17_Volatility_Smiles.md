# R17 — Volatility Smiles

**Exam Priority:** 🟡 Medium (1-2 questions) and Volatility Surfaces

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.17.1` | **The Black-Scholes Flaw:** The BSM model assumes volatility is a single fixed number for all strikes. In reality, the market "prices in" different volatilities for different strikes, creating the **Volatility Smile** or **Skew**. | `[MKT/THE]` | BSM assumes the ocean has only one "average wave height" everywhere. Traders know the "shallow end" (OTM) gets much bigger waves during a storm than the "deep end" (ATM). |
| `P.17.2` | **The Equality of Put-Call Vol:** Because of **Put-Call Parity**, any call and put with the same strike ($K$) and expiry ($T$) must have the identical implied volatility. If they didn’t, there would be an arbitrage opportunity. | `[MTH/MKT]` | You can't charge two different "Insurance Premiums" for the same car just because one person calls it a "Collision Policy" and the other calls it "Liability." |
| `P.17.3` | **Financial Currency Smiles:** Currency markets typically show a symmetric "Smile." Implied vol is lowest at-the-money (ATM) and grows as you move toward deep OTM puts or calls. | `[MKT/THE]` | Because currencies have "Fat Tails" (Jump risk), the market charges a premium for protection against massive swings in either direction. |
| `P.17.4` | **Equity Volatility Skew (Smirk):** Equity markets show a "Skew" where low-strike options (OTM Puts) have much higher implied vols than high-strike options. | `[MKT/THE]` | "Crashophobia." Everyone is scared of a 1987-style market meltdown, so they overpay for "Downside Insurance" (Puts). |
| `P.17.5` | **The Leverage Effect:** As a company's stock price falls, its debt remains fixed, causing its **Leverage (D/E ratio)** to spike. This makes the equity more volatile, naturally driving up implied vol as prices drop. | `[THE/ECO]` | If a house has a mortgage, and the house value drops, the owner's "Equity" shrinks and they become more desperate/risky. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If an empirical distribution has THINNER tails than a Normal distribution:** The volatility smile would turn into a **Volatility Frown**, where ATM options are more expensive than OTM options.
- **Variable Flip: If a trder finds a Call with 25% Vol and a Put (same K, T) with 30% Vol:** **Arbitrage is possible**. They should buy the cheap call and sell the expensive put (while adjusting the underlying) to lock in a risk-free profit.
- **Variable Flip: If there is a massive "Jump" risk expected tomorrow:** The volatility surface will show a steep "cliff" or spike for very short maturities.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Equities:** Skew/Smirk (Downside bias). | **Equities:** Symmetric Smile (NO: that's currencies). |
| **Leverage Effect:** Price $\downarrow \rightarrow$ Vol $\uparrow$. | **Leverage Effect:** Price $\uparrow \rightarrow$ Vol $\uparrow$ (NO). |
| **Put-Call Parity:** Same strike = Same vol. | **Put-Call Parity:** Different strike = Same vol (NO: BSM assumes this, but reality doesn't). |

## 4. Directional Intuition
- **Maturity ($T$) $\uparrow \rightarrow$ Slope of Skew $\downarrow$:** The "Skew" is usually steepest for short-term options and "flattens out" as you go out 2 or 5 years.
- **Panic/Fear $\uparrow \rightarrow$ Left-side Skew (Puts) $\uparrow \uparrow$:** When the market expects a crash, the price of the "Insurance" (low-strike puts) skyrockets.
- **Asset Price $\downarrow \rightarrow$ Implied Vol $\uparrow$ (Sticky-Delta):** In an equity market, prices and volatility are typically negatively correlated.

## 5. Ambiguity Traps (Anti-Decoder)
- **Wait—Currencies vs. Equities:**
    - Currencies = Smile (Symmetric Fat Tails).
    - Equities = Skew/Smirk (Asymmetric Crash Risk).
- **Volatility Surface:** This is a 3D map of $(K, T, \sigma)$. It shows how the whole ecosystem of options is priced.
- **Minimum Variance Delta:** Note that if the price goes down, vol usually goes up. This "volatility movement" offsets part of the delta, so you need to adjust your hedge.
- **Black-Scholes is a "Universal Language":** Traders don't believe the BSM assumptions, but they use BSM "Implied Vol" as a way to communicate the *price* of an option without worrying about the units.
- **"Crashophobia":** It’s a psychological term for the left-tail skew in equities since October 1987.
- **Delta-Neutrality:** It is much harder to maintain when there is a steep skew because the "gamma" and "vanna" (vol-sensitivity) are constantly shifting.
- **Sticky-Strike vs Sticky-Delta:**
    - **Sticky-Strike:** Assumes $\sigma_{imp}$ for a specific strike price is constant as the underlying moves.
    - **Sticky-Delta:** Assumes $\sigma_{imp}$ for a specific delta (moneyness) is constant as the underlying moves.
- **Volatility Term Structure:** A 2D slice of the surface showing vol vs. time to maturity only.
- **In-the-Money vs. Out-of-the-Money:** A deep ITM call and a deep OTM put (same strike) must have the same vol.
- **Jump Diffusion:** If you add "Jumps" to BSM, you naturally get a smile.
- **The "Smile" Shape:** Middle is low, ends are high.
- **The "Smirk" Shape:** Left is high, right is low.
- **Put-Call Parity Formula:** $C - P = S_0 - K e^{-rT}$. Use this to prove the vols must be equal!


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
