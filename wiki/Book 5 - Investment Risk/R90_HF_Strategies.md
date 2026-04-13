# R90 — Hedge Fund Investment Strategies

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.90.1` | **Equity Long/Short & Rebates:** Returns come from (1) Alpha on both legs, (2) Interest earned on cash buffers, and (3) The **Interest Rebate** on the cash proceeds from short sales. | `[OPS/MKT]` | You don't just win on the price move; the broker pays you interest on the cash you "borrowed" from the person who bought your shorted shares. |
| `P.90.2` | **Convertible Arbitrage & Volatility:** Managers buy the convertible bond and short the stock. This creates a position that is "Equity Neutral" but "Long Volatility," allowing them to profit from **Dynamic Delta Hedging**. | `[MTH/THE]` | You are "Gamma Long." The more the stock price oscillates, the more you make from rebalancing your hedge, regardless of which way the stock goes. |
| `P.90.3` | **Merger Arbitrage (Risk Arb):** Involves capturing the "Spread" between the current price and the offer price. The primary risk is **Deal Failure**, which causes the target's stock to crash back to its pre-announcement level. | `[MKT/OPS]` | It's "Selling Insurance." You collect a small premium (the spread) most of the time, but you lose big if the "Accident" (Deal collapse) happens. |
| `P.90.4` | **Distressed Investing Prioritization:** Success depends on calculating **Recovery Values** and understanding capital structure priority. Shorting the equity is often a hedge against the bankruptcy failing to restructure. | `[THE/OPS]` | You're a "Vulture." You buy the debt when it's $0.30 on the dollar, betting that the judge will give you $0.40 worth of assets at the end. |
| `P.90.5` | **Global Macro:** One of the few strategies that avoids "Market Neutrality" by design. It seeks large, directional, leveraged exposure to tectonic shifts in policy, interest rates, and geopolitics. | `[ECO/MTH]` | These are the "Tsunami Surfers." They don't care about individual stock mispricing; they care about whether the USD is going to collapse or if oil is going to double. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a Merger Deal has a 100% Probability of closing:** Then the target stock should trade exactly at the **Offer Price**. Any spread remaining is a "Risk Premium" for the possibility of the deal falling through.
- **Variable Flip: If an investor is "Short Biased" in a bull market:** They will face **Margin Calls and Short Squeezes**. Rising prices are a triple-threat: they lower the value of the short position, increase the collateral requirement, and force "covering" which pushes prices higher still.
- **Variable Flip: If a convertible bond is "Deep In-The-Money":** It behaves like the **Stock**. The arbitrageur must short more shares to stay delta-neutral, and the volatility (gamma) profits become smaller.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Convertible Arb:** Long Bond, Short Stock. | **Convertible Arb:** Long Stock, Short Bond (NO: that's selling vol). |
| **Merger Arb Risk:** Deal Failure (Gap Down). | **Merger Arb Risk:** Market Risk (NO: it's usually market-neutralized). |
| **Pairs Trading:** Relative Value / Convergence. | **Pairs Trading:** Fundamental Long only (NO: it requires a short). |

## 4. Directional Intuition
- **Deal Closing Probability $\uparrow \rightarrow$ Target Stock Price $\rightarrow$ Offer Price:** As uncertainty disappears, the "Arb Spread" narrows.
- **Market Volatility $\uparrow \rightarrow$ Convertible Arbitrage Returns $\uparrow$:** "Gamma" profits from delta-hedging increase when the underlying stock moves more.
- **Bankruptcy Timeline $\uparrow \rightarrow$ Distressed Debt Return $\downarrow$:** Time-value of money and legal costs erode the recovery value.

## 5. Ambiguity Traps (Anti-Decoder)
- **Interest Rebate:** Does the short-seller keep all the interest? **NO.** The broker takes a "Spread," and the short-seller gets the "Rebate."
- **Delta Hedging:** Is it static? **NO.** It’s **Dynamic**. As the stock goes up, you must short *more* shares to stay neutral.
- **Short Squeeze:** Who is squeezed? The **Short seller**. Why? Because they are forced to buy at high prices to cover, which creates more buying pressure.
- **Merger Arb (Share-for-Share):** You must short the **Acquirer's** stock in the specified exchange ratio.
- **Activist vs. Distressed:**
    - Activist: "I want to change the Board."
    - Distressed: "I want to survive the Bankruptcy."
- **Hedge Fund Crisis Sensitivity:** Remember that correlations go to **1** during a systemic crisis, breaking many "Market Neutral" hedges.
- **Merger Calculation:** $ \text{Expected Return} = (P_{success} \times \text{Spread}) - (P_{fail} \times \text{Loss}) $. (Don't forget to annualize if the deal is 3 months away).
- **Distressed:** Active investors take a seat on the **Creditor Committee**.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
