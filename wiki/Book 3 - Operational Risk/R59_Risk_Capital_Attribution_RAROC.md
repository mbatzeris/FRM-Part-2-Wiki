# R59 — Risk Capital Attribution and RAROC

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.59.1` | **The RAROC Formula:** `(Revenue - Expenses - Expected Loss + Income from Capital) / Economic Capital`. | `[ECO/THE]` | It’s the "Purity Test" for profit. It subtracts the "cost of risk" (EL) and divides by the "cushion" (EC) needed to take that risk. |
| `P.59.2` | **Unexpected Loss (UL) Focus:** Economic Capital is designed to cover UL at a specific confidence level (e.g., 99.9%), while Expected Loss (EL) is treated as a cost of doing business and subtracted from revenue. | `[THE]` | You pay for your lunch (EL); you keep a credit card in case the car breaks down (EC/UL). |
| `P.59.3` | **Point-in-Time (PIT) vs. Through-the-Cycle (TTC):** PIT models capture current default probabilities (volatile); TTC models average risk across economic cycles (stable). | `[THE]` | PIT is a "Snapshot" of the storm; TTC is a "Climate Map" of the region. |
| `P.59.4` | **Confidence Level Sensitivity:** For heavy-tailed risks (like OpRisk), a small decrease in the target confidence level (e.g., 99.9% to 99.5%) results in a massive reduction in required Economic Capital. | `[THE/MTH]` | The "Tail" of operational risk is where all the capital lives. If you ignore the last 0.4% of extreme events, your required cushion collapses. |
| `P.59.5` | **Strategic Use of RAROC:** RAROC is used to optimize scarce capital by allocating it to business units that generate the highest risk-adjusted returns, rather than just the highest raw profits. | `[OPS]` | A unit making $10M profit with $1M risk capital is "Better" than a unit making $50M profit with $100M risk capital. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a firm used "Point-in-Time" (PIT) for Economic Capital:** Then the bank’s capital requirements would swing wildly every month based on market sentiment, leading to strategic instability. TTC is the standard for capital because it provides the "Stable Anchor."
- **Variable Flip: If a RAROC calculation ignored the "Income from Capital":** Then the return would be underestimated. The capital being held isn't just sitting in a vault; it's invested in risk-free assets, and that interest belongs in the numerator.
- **Variable Flip: If Expected Loss (EL) was included in the Denominator (EC):** This is a categorical error. EC covers **Unexpected Loss**. EL should already be covered by pricing and reserves (the numerator).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Numerator:** Revenue - Expenses - EL + Income from Capital. | **Denominator:** Economic Capital (covers UNEXPECTED loss). |
| **Through-the-Cycle (TTC):** Best for strategic/EC decisions. | **Standard Deviation:** Is a measure of volatility, not the capital itself. |
| **Risk Attribution:** Assigning capital based on the marginal contribution to firm-wide risk. | **Asset Allocation:** Is a market risk/portfolio term, not a capital attribution term. |

## 4. Directional Intuition
- **Confidence Level $\downarrow \rightarrow$ Economic Capital $\downarrow \downarrow$ (for OpRisk):** Because OpRisk is fat-tailed, the "Tail" holds an exponential amount of the risk.
- **Economic Volatility $\uparrow \rightarrow$ PIT/TTC Divergence $\uparrow$:** In a crisis, PIT default rates spike immediately, while TTC rates move slowly, creating a massive gap in required capital estimates.
- **Diversification $\uparrow \rightarrow$ Required Economic Capital $\downarrow$:** At the firm level, risks across units often cancel out, allowing the total "Firm EC" to be less than the sum of "Unit ECs."

## 5. Ambiguity Traps (Anti-Decoder)
- **EL placement:** Where does Expected Loss go in RAROC? **The Numerator** (subtracted from the profit). NEVER the denominator.
- **PIT vs. TTC for Pricing:** Which is better for pricing a loan today? **PIT**. Which is better for long-term capital? **TTC**.
- **The "Income from Capital" piece:** Why is it there? Because the capital held to support a desk is earning interest in a treasury account. That interest is part of the desk's return.
- **Subjectivity in OpRisk:** RAROC for OpRisk is much more subjective than for Market/Credit risk due to the lack of frequent loss data.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
