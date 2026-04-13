# R98 — Liquidity Risk Management

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.98.1` | **The Four Pillars of Liquidity:** A robust framework requires (1) Measurement (quantifying needs), (2) Management (maintaining buffers), (3) PM Awareness (aligning trades with liquidity), and (4) Extraordinary Tools (gates/borrowing). | `[OPS/REG]` | It’s "Financial Plumbing." You need to know how much water you need, keep a tank ready, make sure the gardener doesn't waste water, and have a "Shut-off valve" for emergencies. |
| `P.98.2` | **Fixed-Income Illiquidity:** Managing bond liquidity is harder than stocks because bonds trade OTC (less transparency), have millions of different CUSIPs, and many trade "infrequently." TRACE and MiFID II provide some "smoke" but not the "fire" of real-time depth. | `[MKT/OPS]` | In stocks, there’s a crowded marketplace (Exchange). In bonds, it’s a series of "Private Garage Sales." Finding a buyer for a specific junk bond is much harder than selling Apple stock. |
| `P.98.3` | **Days-to-Liquidate & Participation:** A simple model to estimate exit time: $\text{Days} = \frac{\text{Position Size}}{\text{ADV} \times \text{Participation Rate}}$. A 10% participation rate means you try to be only 1/10th of the daily volume to avoid "crashing" the price. | `[MTH/OPS]` | If you have 1000 apples to sell and the market only buys 100 a day, but you don't want to look desperate, you sell 10 a day. It will take you 100 days to exit. |
| `P.98.4` | **US vs. EU Regulatory Tools:** US mutual funds rely on **Borrowing** and **In-kind redemptions** but are generally **Forbidden** from using Gates or Swing Pricing. European (UCITS) funds **Cannot Borrow** but **Can** use Gates, Swing Pricing, and Suspensions. | `[REG/OPS]` | The US says: "Keep the doors open, just borrow money to pay people." Europe says: "Close the doors (Gates) or make the people who leave pay a tax (Swing Pricing)." |
| `P.98.5` | **The Redemption Waterfall:** A prioritized sequence for meeting outflows: (1) Use Cash/Liquid assets first, then (2) Pro-rata sales of the whole portfolio, then (3) Borrowing from a bank facility. | `[OPS]` | First use the "Change in your pocket," then sell a little bit of "Everything you own," and if that’s not enough, take out a "Payday loan." |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a manager uses "End-of-Day" (EOD) prices for transaction cost benchmarks:** The implementation shortfall measure will be **Noisy and Inaccurate**. Intraday, pre-trade benchmarks are required to isolate the actual cost of the manager's execution.
- **Variable Flip: If a fund is "High-Growth" or "New":** **Historical Redemption-at-Risk (HRaR)** will be **Useless**. There is no history of stress to model. You must use peer analysis or "Factor-based" liquidity stress tests.
- **Variable Flip: If "Latent Liquidity" is ignored:** You will **Underestimate** the market's true capacity. Traded volume (ADV) only shows what *did* happen, not what *could* have happened if the price were slightly different.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Swing Pricing:** Adjusts NAV to charge leavers for costs. | **Swing Pricing:** Available for US Mutual Funds (NO: Forbidden). |
| **Gates:** Limits redemptions to a \% of AUM. | **Gates:** Available for US Mutual Funds (NO: Forbidden). |
| **TRACE:** US system for reporting bond trades. | **TRACE:** US system for reporting equity trades (NO). |

## 4. Directional Intuition
- **Asset Fragmentation $\uparrow \rightarrow$ Price Discovery $\downarrow$:** The more different types of bonds there are, the harder it is to know what a "fair" price is.
- **Participation Rate $\uparrow \rightarrow$ Market Impact $\uparrow$:** The "hurrieder" you are to sell (taking up more of the daily volume), the more you will push the price against yourself.
- **Market Stress $\uparrow \rightarrow$ Bid-Ask Spread $\uparrow$:** In a panic, dealers won't commit capital, making it much more expensive to exit.

## 5. Ambiguity Traps (Anti-Decoder)
- **LVaR:** Liquidity-Adjusted VaR. Formulas:
    - **Exogenous (Constant Spread):** $ VaR_{adj} = VaR + 0.5 \times \text{Spread} \times \text{Position} $.
    - **Endogenous (Variable Spread):** Accounts for market impact (position size matters).
- **US vs EU (CRITICAL):** 
    - US = **Borrowing** (Yes), **Gates** (No). 
    - EU = **Borrowing** (No), **Gates** (Yes).
- **In-Kind Redemptions:** Giving the investor the "Actual Bonds" instead of cash. Usually only for big institutions.
- **Implementation Shortfall:** $ \text{Execution Price} - \text{Benchmark Price} $.
- **ADV:** Average Daily Volume. Remember that this is a **Backward-looking** measure.
- **Swing Pricing:** It protects the **Remaining** investors by making the **Redeeming** investors pay the spread they "caused" by forcing a sale.
- **Suspensions:** The "Nuclear Option." Halting all withdrawals. Requires massive regulatory approval in the US.
- **Participation Rate:** Usually assumed to be **10% to 25%**. 
- **Wait Time:** Total exit time = position / (ADV * participation).
- **Interfund Lending:** Big fund families (like Vanguard/BlackRock) letting their "Cash" funds lend to their "Equity" funds to meet redemptions. (US tool).
- **CTFs (Collective Trust Funds):** In the US, these **DO** allow more flexible price mechanisms than mutual funds.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
