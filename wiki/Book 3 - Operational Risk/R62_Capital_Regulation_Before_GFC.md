# R62 — Capital Regulation Before the GFC

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.62.1` | **Basel I Risk Weights:** Introduced the 8% minimum capital rule with crude risk weights: 0% (Sovereigns), 20% (OECD Banks), 50% (Mortgages), and 100% (Corporates). | `[REG/Basel I]` | It was the "First Draft." It was simple, but it treated a AAA-rated company and a junk-rated company the same (both 100%). |
| `P.62.2` | **The 1996 Market Risk Amendment:** Introduced the use of internal VaR models for trading book capital: `Capital = Mult * VaR(10-day, 99%)`. | `[REG]` | Regulators let banks use their own "Quants" to decide capital, but added a "Multiplier" ($m_c$) to keep things safe. |
| `P.62.3` | **Market Risk Multiplier ($m_c$):** The multiplier starts at 3.0 but increases (up to 4.0) if backtesting reveals too many "exceptions" (losses exceeding VaR) over the prior 250 days. | `[REG/MTH]` | If your model lies to you, the regulator punishes you by making you hold more capital. $\text{Exceptions} \uparrow \rightarrow \text{Capital} \uparrow$. |
| `P.62.4` | **Basel II — The Three Pillars:** Established (1) Minimum Capital Requirements, (2) Supervisory Review, and (3) Market Discipline (Disclosure). | `[REG/Basel II]` | It’s a three-legged stool: The math (P1), the human oversight (P2), and the public scrutiny (P3). If one leg breaks, the stool falls. |
| `P.62.5` | **Solvency II (Insurance):** Similar to Basel II but for insurers. Uses a **Solvency Capital Requirement (SCR)** and a **Minimum Capital Requirement (MCR)**, calibrated to a 99.5% 1-year VaR. | `[REG/SOL]` | Insurers are slightly less risky than banks, so their "Confidence Level" (99.5%) is lower than the Basel 99.9% target. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank has 12 backtesting exceptions over 250 days:** Then the Market Risk multiplier ($m_c$) **MUST** be set at the maximum of **4.0**. High exceptions prove the model is structurally failing to capture risk.
- **Variable Flip: If Basel I treated an unrated corporate as 100% risk weight:** This was the default. Basel II (Standardized) refined this, but the "crude" nature of Basel I led to **Regulatory Arbitrage**, where banks moved low-weight assets off-balance sheet to hide risk.
- **Variable Flip: If an insurance company falls below its MCR (Minimum Capital Requirement):** Then the regulator may move to **Liquidation** or prohibit new business. Falling below SCR only requires a plan to remedy; falling below MCR is a "Red Alert."

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Basel II Pillar 1:** Credit, Market, and **Operational** risk. | **Basel I:** Did not include Operational Risk. |
| **A-IRB (Advanced):** Bank estimates PD, LGD, and EAD. | **F-IRB (Foundation):** Bank estimates PD; Regulator provides LGD/EAD. |
| **Market Risk VaR:** 10-day horizon, 99% confidence. | **Economic Capital:** Often uses a 1-year horizon, 99.9% confidence. |

## 4. Directional Intuition
- **Backtesting Exceptions $\uparrow \rightarrow$ Model Multiplier $\uparrow \rightarrow$ Capital Required $\uparrow$:** Poor model performance has a direct, formulaic financial penalty.
- **Method Complexity $\uparrow \rightarrow$ Capital Precision $\uparrow$ BUT $\rightarrow$ Implementation Risk $\uparrow$:** Moving from Basic Indicator to AMA (OpRisk) or Standardized to A-IRB (Credit) saves capital but adds massive operational risk.
- **Unrated Corporate Risk Weight (Hinge):** In Basel II Standardized, an unrated corporate is **100%**. Don't guess—it's the same 100% shell as Basel I.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Solvency II" Confidence Level:** Is it 99.9% like Basel? **NO. 99.5%.**
- **The "Exception" Thresholds:** How many exceptions trigger a 4.0 multiplier? **10 or more.**
- **A-IRB vs. F-IRB:** Who provides LGD in Foundation? **The Regulator.** In Advanced? **The Bank.**
- **Basel I vs. II:** Which one introduced "Operational Risk"? **Basel II.**
- **The "Market Discipline" Pillar:** Pillar 3 is about **Public Disclosure**, not "Trading Rules."


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
