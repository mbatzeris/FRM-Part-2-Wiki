# R93 — Private Markets

**Exam Priority:** 🟡 Medium (1-2 questions) Investing

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.93.1` | **The J-Curve Effect:** Private market funds typically exhibit negative returns in the early years as management fees and start-up costs outweigh the value of young investments. Value is only "unlocked" in the later years of the fund's life. | `[THE/OPS]` | It’s like planting a fruit tree. The first few years are just digging holes (costs) and watering. You only get the fruit (harvest) at the very end. |
| `P.93.2` | **Gaming the IRR:** Fund managers can artificially boost IRRs by using **Subscription Credit Lines** to delay capital calls from investors. This shortens the "measured" time capital is at risk, inflating the percentage return without increasing the actual dollar profit. | `[MTH/OPS]` | If you borrow $10 today to buy a $12 item tomorrow, your "IRR" is huge because you only used your own money for one day. But you still only made $2. |
| `P.93.3` | **MOIC vs. IRR:** The Multiple of Invested Capital (MOIC) provides an absolute measure of value creation ($2x, $3x) that is immune to timing manipulation. IRR measures the *speed* of capital growth. | `[MTH]` | IRR is the "Speedometer" (how fast are we going?); MOIC is the "Odometer" (how far did we actually travel?). |
| `P.93.4` | **Performance Dispersion:** The gap between "Top Quartile" and "Bottom Quartile" managers is far wider in private markets than in public markets. This makes **Manager Selection** the primary driver of success. | `[MKT/THE]` | In the stock market, most "Large Cap" managers perform similarly. In Private Equity, the best manager is a genius and the worst is a disaster. |
| `P.93.5` | **Co-Investing Benefits:** Co-investment allows LPs to invest directly alongside the GP in a specific deal. This typically features **Reduced Fees** and no "Carried Interest" on the co-invest portion, boosting the investor's net return. | `[OPS/ECO]` | It’s like getting a "VIP discount." You pay full price for the buffet (The Fund), but the chef lets you buy an extra steak (Co-invest) at cost. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a fund manager returns all capital early but has zero dollar profit:** The **IRR** would be mathematically high (or infinite if instantaneous), but the **MOIC** would be precisely **1.0x**. This highlights the danger of relying on IRR alone.
- **Variable Flip: If an investor is "Liquidity Constrained":** They should avoid Private Markets. The J-curve and long lock-up periods mean capital is inaccessible exactly when the investor might need it most (e.g., during a market crash).
- **Variable Flip: If a Fund of Funds (FoF) has high fees on both layers:** The manager must generate massive gross alpha just to break even for the investor. The **"Double Fee" burden** is the primary hurdle for FoF performance.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **DPI:** Distribution to Paid-In (Realized cash). | **TVPI:** Distribution to Paid-In (NO: TVPI includes *unrealized* value). |
| **TVPI:** Total Value to Paid-In (Realized + Unrealized). | **TVPI:** The same as MOIC (NO: MOIC is relative to *invested*, TVPI is relative to *paid-in*). |
| **J-Curve:** Caused by initial fees and slow harvesting. | **J-Curve:** Caused by market volatility (NO). |

## 4. Directional Intuition
- **Subscription Credit Lines $\uparrow \rightarrow$ Fund IRR $\uparrow$:** Delaying the "Start Clock" on investor capital makes the return look faster.
- **Market Volatility $\uparrow \rightarrow$ Private Market Valuation Lag $\uparrow$:** Because private assets are valued quarterly (or less), they appear smoother and less volatile than public comps during a crisis.
- **GP Skill Dispersion $\uparrow \rightarrow$ Importance of Due Diligence $\uparrow$:** You cannot just "buy the index" in Private Equity; picking a bad manager is a permanent loss of capital.

## 5. Ambiguity Traps (Anti-Decoder)
- **DPI (Realized) vs. RVPI (Unrealized):** 
    - DPI is "Cash in your pocket." 
    - RVPI is "Value on the paper." 
    - TVPI is the **SUM** of both.
- **Paid-In vs. Invested:** 
    - **Paid-In** includes fees and expenses. 
    - **Invested** is just the capital put into the companies. 
    - Multiples calculated against "Invested" look better than those against "Paid-In."
- **Co-investing:** Does it have fees? **Usually lower or zero.** 
- **The "Carry":** Usually 20%. Remember that it is calculated on the **Net Profit** after fees.
- **J-Curve Navigation:** Some secondary funds try to "buy" old funds to skip the bottom of the J-curve.
- **Intermediated Vehicles:** They solve the "Access" problem but create a "Fee" problem.
- **Subscription Lines:** Are they bad? They provide liquidity for the GP, but they can **Distort** performance reporting for the LP.
- **Dry Powder:** Committed capital that has not yet been "Called" or invested.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
