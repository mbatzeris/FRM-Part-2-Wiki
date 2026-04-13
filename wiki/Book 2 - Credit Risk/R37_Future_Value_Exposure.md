# R37 — Future Value Exposure

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.37.1` | **Expected Exposure (EE):** The average of the positive outcomes of a trade’s value at a specific future date. It ignores the cases where you owe money (negative values). | `[MTH/THE]` | It’s your "Expected Perk." If there's a 50% chance you win $100 and a 50% chance you lose $100, your EE is $50 (Average of 100 and 0). |
| `P.37.2` | **Expected Positive Exposure (EPE):** The average of all the EE values over the entire life of the transaction. It is the "Global Average" exposure. | `[MTH/THE]` | If EE is the "Average Weather" for one day, EPE is the "Average Climate" for the whole year. |
| `P.37.3` | **Potential Future Exposure (PFE):** A "worst-case" scenario (usually 95% or 99% confidence) of what the exposure could look like at a future date. | `[MTH/REG]` | It’s the "Maximum Splash Zone." You want to know if the pipe bursts, how much water (loss) could potentially hit you in the face. |
| `P.37.4` | **The "Peaked" Swap Profile:** Interest rate swap exposure follows a "Hump" shape. Early on, uncertainty grows (Diffusion), but later, the remaining payments decrease (Amortization), eventually dragging exposure back to zero. | `[MKT/MTH]` | It’s like a "Mountain Hike." The further you go, the more lost you could get (Uncertainty). But as you get close to the destination (Maturity), you know exactly where you are and how much is left. |
| `P.37.5` | **Margin Period of Risk (MPoR):** The time gap from the last successful margin call until the counterparty defaults and you finally close out the trade. This is where most "hidden" exposure lives. | `[OPS/REG]` | It’s the "Dead Air" time. It’s the period after the phone line goes quiet but before you realize the other person has hung up. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a portfolio has 100% PERFECT POSITIVE correlation:** Netting provides **Zero Benefit**. If one trade is a winner, they are all winners; you never have a "loser" to offset the "gains."
- **Variable Flip: If the Margin Period of Risk (MPoR) is set to ZERO:** The firm would have **Zero Exposure** (assuming a zero threshold and MTA). This is impossible in reality as it takes time to process defaults.
- **Variable Flip: If you add more Initial Margin (IM) to a trade:** The EE and EPE will **Decrease**. You’ve basically pre-paid for the potential losses, lowering the average amount you still have at risk.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **EPE:** Average of EE over time. | **EPE:** Worst case exposure (NO: that’s PFE). |
| **Swaps Profile:** Peaked/Hump-shaped. | **Options Profile:** Peaked/Hump-shaped (NO: uncertainty grows linearly). |
| **MTA:** Increases exposure. | **MTA:** Decreases exposure (NO: it’s a delay in collecting collateral). |

## 4. Directional Intuition
- **Volatility ($\sigma$) $\uparrow \rightarrow$ Potential Future Exposure (PFE) $\uparrow$:** Higher waves mean the "Maximum Splash Zone" reaches further up the beach.
- **Maturity ($T$) $\downarrow \rightarrow$ Amortization Effect $\uparrow \rightarrow$ Exposure $\downarrow$:** As the clock runs out, there’s no time left for the market to move against you.
- **Threshold $\uparrow \rightarrow$ Expected Exposure $\uparrow$:** If you allow the other guy to owe you $1M before asking for cash, you are literally asking for more risk.

## 5. Ambiguity Traps (Anti-Decoder)
- **EE vs PFE:** 
    - **EE** = Average (for pricing CVA). 
    - **PFE** = Worst Case (for setting limits/VaR).
- **The Swap "Roll-off":** Remember that a swap at $T-1$ only has one payment left! No matter how much rates move, the exposure is tiny.
- **Exposure vs. MtM:** 
    - MtM can be negative. 
    - Exposure is **ALWAYS** $\geq 0$. This is the $\max(MtM, 0)$ rule.
- **MPoR Components:** It includes:
    1.  Time to realize the default.
    2.  Time to call for margin.
    3.  Grace periods.
    4.  Time to liquidate/hedge.
- **Rounding Effect:** Rounding *up* collateral calls (collecting more) reduces your exposure. Rounding *down* increases it.
- **Netting Factor:** A specific number (always $\leq 1$) used to multiply the gross exposure to find the net exposure.
- **The "Diffusion" Effect:** For forwards, the PFE is usually highest at the very end ($T$). For swaps, it's usually at 1/3 to 1/2 way through the life.
- **CVA and EE:** You cannot calculate CVA without knowing the EE at every point in the future.
- **Wrong-Way Risk (WWR):** Exposure increases when the probability of default increases. (e.g., an oil company being short oil).
- **MTA vs Threshold:** 
    - You "Accept" exposure up to the **Threshold**. 
    - You "Ignore" exposure chunks smaller than the **MTA**. Both add to your risk.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
