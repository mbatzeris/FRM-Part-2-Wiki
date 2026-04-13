# R65 — Basel III Finalizing Post-Crisis Reforms (The Unified Standardized Approach)

**Exam Priority:** 🟡 Medium (1-2 questions) (The Unified Standardized Approach)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.65.1` | **The Unified Standardized Approach (SMA):** Basel III replaces all previous operational risk methods (Basic, Standardized, AMA) with a single formula: `Capital = BIC * ILM`. | `[REG/OpRisk]` | No more "pick your own adventure" for OpRisk capital. Everyone uses the same calculator now to ensure the industry's numbers are actually comparable. |
| `P.65.2` | **Business Indicator (BI):** A new proxy for exposure that replaces Gross Income. It is the sum of three components: (1) Interest/Lease/Dividends, (2) Services, and (3) Financial (Trading/Banking Book). | `[REG/MTH]` | It’s a broader "Top Line." It captures all the different ways a bank makes money, assuming that the more business you do, the more opportunities you have for an operational failure. |
| `P.65.3` | **The Marginal Coefficients:** The Business Indicator Component (BIC) uses tiered multipliers (12%, 15%, 18%) similar to a progressive tax. As the BI grows, a larger percentage must be held as capital. | `[REG/MTH]` | The "Size Tax." The regulator assumes that a massive global bank is disproportionately riskier and more complex than a small local one. |
| `P.65.4` | **Internal Loss Multiplier (ILM):** A scaling factor that increases (or decreases) capital based on the bank's actual **10-year average annual operational losses**. | `[REG/OPS]` | It’s a "Safety Discount" (or Penalty). If you have a clean 10-year track record, you pay less. If you have been a "Serial Exploder" of operational risk, the regulator forces you to hold more. |
| `P.65.5` | **Data Window:** Pillar 3 requires the disclosure of 10 years of high-quality, aggregate operational loss data to support the ILM calculation. | `[REG]` | You can't hide from your past. The regulator needs a full decade of history to ensure the ILM isn't just reflecting a single "lucky" year. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank's Business Indicator (BI) increases but its Loss History (ILM) decreases:** Then the net effect on capital depends on the math. However, the BIC (the base) will rise due to the progressive tiers. The firm is punished for "Growing" and rewarded for "Safety."
- **Variable Flip: If a regulator set the ILM to 1.0 for all banks (The "Neutral" Case):** Then the capital would be purely determined by the size of the bank (BIC). Some jurisdictions do this to simplify the regime, but it loses the "Risk-Sensitivity" of rewarding safer banks.
- **Variable Flip: If a bank uses only 5 years of data for its ILM:** This is a non-compliance event. Basel III finalization mandates a **10-year** loss data window for the calculation.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **BIC Formula:** Uses BI and marginal coefficients (12%/15%/18%). | **AMA:** Is deleted; anything related to "internal Monte Carlo" is now noise. |
| **ILM:** Based on **10 years** of loss history. | **3 Years:** Is for the old Basic Indicator approach, not the new SMA. |
| **Pillar 3:** Public disclosure of the BI components and loss data. | **Pillar 2:** Is the supervisory review *of* the process, not the formula itself. |

## 4. Directional Intuition
- **Business Complexity $\uparrow \rightarrow$ BI $\uparrow \rightarrow$ BIC $\uparrow \uparrow$:** Due to the progressive multipliers (18% for the top tier), large banks face a steep increase in capital requirements compared to smaller peers.
- **Operational Controls $\uparrow \rightarrow$ Actual Losses $\downarrow \rightarrow$ ILM $\downarrow \rightarrow$ Capital Required $\downarrow$:** The SMA creates a direct financial incentive for banks to invest in better controls (L1/L2/L3) to lower their loss history.
- **Standardization $\uparrow \rightarrow$ RWA Comparability $\uparrow$:** By removing internal models (AMA), the regulator can now look at two banks and know that their "OpRisk Capital" was calculated using the exact same yardstick.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Business Indicator" Components:** Is it just Gross Income? **NO.** It is a sum of three specific components: ILDC (Interest), SC (Service), and FC (Financial).
- **The Magic 10:** How many years of data for ILM? **10 Years.**
- **The Death of AMA:** Can a bank STILL use its internal model if it was really good? **NO.** AMA is officially removed from the global framework.
- **Progressive Tiers:** Do smaller banks pay 18%? **NO.** They start at 12%. The 18% is for the largest, systemically important institutions.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
