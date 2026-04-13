# R39 — Stress Testing Counterparty Exposures

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.39.1` | **Macro Stress Testing:** The process of identifying how large, extreme moves in market variables (like a massive interest rate spike) impact the total counterparty exposure of a bank. | `[REG/MKT]` | It’s a "Stress Test for the Pipes." You’re pumping 10x the normal pressure through the plumbing to see which joints (counterparties) burst first. |
| `P.39.2` | **The Derivative Difference:** Unlike loans (where exposure is fixed), the exposure of a derivative is a function of market prices. Stress testing CCR requires stressing the **Exposure Profile (EE/EPE)**, not just the current value. | `[MTH/THE]` | A loan is a "Solid Object" (its weight doesn't change). A derivative is a "Balloon." If the temperature (market) rises, the balloon expands, and your risk of it popping (defaulting) grows. |
| `P.39.3` | **Linearization Risk (Delta Trap):** Simplistic models that use only "Delta" to estimate how exposure changes in a stress test will fail during extreme moves because they ignore "Gamma" (curvature). | `[MTH]` | If you assume a road is perfectly flat (Linear), you’ll be in big trouble when you hit a 90-degree cliff (Curvature). |
| `P.39.4` | **Aggregation Complexity:** You cannot simply add up the stressed exposures of all counterparties. This would assume a "Global Apocalypse" where everyone dies at the same time, which is statistically unrealistic and overly capital-intensive. | `[THE/REG]` | It’s the "Sinking Ship" problem. One or two people might fall overboard in a storm, but assuming the *entire* world's population sinks at the same second is bad math. |
| `P.39.5` | **Bilateral CVA (BCVA):** A more advanced CVA measure that accounts for the fact that you might default *before* your counterparty does. It uses **Expected Negative Exposure (ENE)**. | `[MTH/REG]` | It’s "Mutual Ghosting." It considers the chance that you disappear before they have a chance to not pay you. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If you stress "Current Exposure" instead of "Expected Exposure":** You will **Underestimate** the risk of at-the-money options. Since they currently have little value, their current exposure is near zero, but their *future* exposure in a stress scenario could be massive.
- **Variable Flip: If a firm hedges its CCR as "Market Risk":** It is protected against price swings (e.g., interest rate moves), but it remains **Exposed** to its counterparty’s credit rating dropping (Spread Risk).
- **Variable Flip: If correlations "Break" during a stress test (go to 1.0):** Netting benefits will **Disappear**. Your "Loser" trades might stop offsetting your "Winner" trades, causing your total credit exposure to explode.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Stress EPE:** Correct method for CCR. | **Stress Current Exposure:** Correct method for CCR (NO: too static). |
| **BCVA:** Includes your own survival risk. | **BCVA:** Includes only the counterparty's survival risk (NO: that’s CVA). |
| **Linearization:** Works for small moves. | **Linearization:** Works for stress tests (NO: too much curvature). |

## 4. Directional Intuition
- **Market Volatility ($\sigma$) $\uparrow \rightarrow$ Model Error Sensitivity $\uparrow$:** The wilder the market moves, the more your "simple" internal models will lie to you about the true exposure.
- **Concentration $\uparrow \rightarrow$ Aggregation Error $\uparrow$:** If you are heavily exposed to one industry, a sector-specific stress test will hit all your counterparties simultaneously, making simple sums more "real."
- **Wrong-Way Risk Presence $\rightarrow$ Stressed CVA $\uparrow \uparrow$:** If your exposure grows exactly when the world burns, your stress test results will be much more catastrophic than a "Neutral" model.

## 5. Ambiguity Traps (Anti-Decoder)
- **EPE vs ENE:** 
    - **EPE** (Positive) = Your risk. 
    - **ENE** (Negative) = Their risk (your DVA).
- **Macro vs Micro:** 
    - **Micro** stress tests look at one specific counterparty. 
    - **Macro** look at the whole world/portfolio.
- **The "Sum of Sums" Trap:** Remember that exposure is $\max(V, 0)$. You can't just add them up across counterparties because of diversifying defaults.
- **Wrong-Way Risk in Stressing:** A good stress test *forces* the correlation to be high. It asks: "What if the dollar crashes AND the company goes bankrupt?"
- **Static vs. Dynamic:** Statically stressing current MtM is an "Operational shortcut" that leads to bad risk management.
- **Funding Value Adjustment (FVA):** Often discussed alongside CVA stress testing. It's the cost of borrowing the cash to post as collateral in a stressed market.
- **Jump Diffusion:** Standard CCR models often assume smooth moves. Stress tests should assume "Jumps" (gaps in pricing).
- **The "Amber Zone":** If a desk's stressed exposure exceeds its limits too often, it may be forced to reduce its trading volume or move to a more conservative clearing model.
- **Interpreting Results:** Does a high stressed exposure mean the bank is failing? Not necessarily. It means the bank needs to have a **Contingency Funding Plan** for that specific scenario.
- **Linearization again:** If you see "Delta-Normal" in a stress testing context, it is almost certainly a **BAD** sign. Full revaluation of the portfolio is the gold standard.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
