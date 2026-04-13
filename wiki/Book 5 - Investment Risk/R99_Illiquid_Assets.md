# R99 — Illiquid Assets

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.99.1` | **The Triad of Illiquidity Biases:** Reported returns for illiquid assets are chronically "too good" due to (1) **Survivorship Bias** (losers disappear), (2) **Selection Bias** (only winners sell and report), and (3) **Infrequent Trading** (smooths the volatility). | `[MTH/THE]` | It’s the "Beauty Filter" of finance. It hides the wrinkles (volatility) and only shows the best angles (successful sales). |
| `P.99.2` | **Return Smoothing & Autocorrelation:** Because illiquid assets trade infrequently, today's price is often heavily influenced by "stale" prices from weeks or months ago. This creates high **Autocorrelation** and makes volatility and Beta appear much lower than they truly are. | `[MTH]` | If you only weigh yourself once a month, you look like you have "Zero Volatility," but you're just ignoring the daily ups and downs. |
| `P.99.3` | **Unsmoothing Returns:** To see the true risk, analysts must "Unsmooth" the returns by removing the autocorrelation. This process reveals that the true volatility of private equity or real estate is often 2-3x higher than the reported version. | `[MTH/OPS]` | It’s like "Turning up the contrast" on a blurry photo. Suddenly, all the sharp edges and noise (real risk) become visible. |
| `P.99.4` | **Search Frictions:** Unlike liquid markets where you just "hit a button," illiquid markets suffer from **Search Frictions**—the difficulty of finding a counterparty who understands the asset and has the cash to buy it, regardless of the price. | `[MKT/OPS]` | Selling a specialized $50M office building isn't just about price; it's about finding that one specific billionaire who wants that exact building today. |
| `P.99.5` | **Harvesting the Premium:** The most effective way to capture the illiquidity premium is through **Dynamic Factor Strategies**: going Long the illiquid factor and Short the liquid equivalent. This isolates the "Premium" for being stuck. | `[MTH/THE]` | You are betting on the "Wait." You get paid extra not for being smart, but for being willing to have your money "locked in the cage" with the asset. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If an illiquid asset class has an $R^2$ of 1.0 with a liquid benchmark:** Then the "Alpha" is fake, and any extra return is likely just a **Leverage Effect** or a mismatch in timing.
- **Variable Flip: If there is a massive market crash:** Liquidity "Dries Up" even for assets that are normally liquid. The correlation between all assets tends toward **1.0**, and the "Illiquidity Premium" can turn into an "Illiquidity Discount" as everyone tries to exit at the same door.
- **Variable Flip: If a manager uses "Mark-to-Model" valuations:** They have an incentive to **Smooth** returns to ensure steady management fees and avoid upsetting investors. This creates an agency problem between the GP and the LP.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Stale Pricing:** Leads to **Underestimated** volatility. | **Stale Pricing:** Leads to **Overestimated** return (NO: that's choice/selection bias). |
| **Search Frictions:** Counterparty search + Information asymmetry. | **Search Frictions:** High brokerage commissions (NO: those are transaction costs). |
| **Unsmoothing:** Increases volatility and Beta estimates. | **Unsmoothing:** Increases expected return (NO: it usually doesn't change the mean). |

## 4. Directional Intuition
- **Asset Unique-ness $\uparrow \rightarrow$ Search Frictions $\uparrow$:** The more "weird" the asset, the harder it is to find a buyer.
- **Reporting Frequency $\downarrow \rightarrow$ Return Autocorrelation $\uparrow$:** The longer the gap between prices, the more "smooth" the return stream appears to be.
- **Institutional Competition $\uparrow \rightarrow$ Illiquidity Premium $\downarrow$:** As everyone tries to "Harvest" the premium (e.g., by piling into Private Equity), the extra return for being illiquid disappears.

## 5. Ambiguity Traps (Anti-Decoder)
- **Survivorship vs. Selection Bias:**
    - **Survivorship:** The fund is **Dead**. 
    - **Selection:** The price is **Cherry-picked** from a successful sale.
- **The "Zero Returns" Metric:** Why is it a proxy for illiquidity? Because in a liquid market, prices move every day. If a price stays the same for 10 days, it means no one is trading.
- **Unsmoothing Math:** It doesn't change the *mean* return, only the *variance* and *covariances*.
- **The "Alpha" Trap:** Is illiquid asset performance real? Much of it is just **Stale-priced Beta** or **Leverage**.
- **Agency Problem:** Managers love illiquidity because it hides their bad months and lets them "game" the timing of fees.
- **Market Making:** One way to harvest the premium is by **Providing Liquidity** to those desperate to exit.
- **Information Asymmetry:** The seller often knows much more about the "Hidden flaws" of an illiquid asset (like a building) than the buyer.
- **Funding Constraints:** You might know an asset is cheap, but if you can't borrow money to buy it, the price stays low (Illiquidity).
- **Clientele Effects:** Only certain investors (like endowments) can afford to wait 10 years for a payout.
- **Volatility underestimation:** Reported $\sigma_{PE}$ might be 10%, but unsmoothed $\sigma_{PE}$ might be 25%.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
