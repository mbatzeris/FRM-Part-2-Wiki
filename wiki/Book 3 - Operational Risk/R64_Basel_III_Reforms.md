# R64 — High-Level Summary of Basel III Reforms (Basel III Finalization)

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.64.1` | **The Output Floor:** Banks using internal models must ensure their total Risk-Weighted Assets (RWA) are at least **72.5%** of the RWA calculated using the Standardized Approach (SA). | `[REG/Basel III]` | It’s a "Reality Check." Even if your genius quant model says you need $0 capital, the regulator says "No bank can be more than 27.5% more efficient than the standard." |
| `P.64.2` | **The Death of AMA:** Basel III reforms remove the Advanced Measurement Approach (AMA) for Operational Risk, replacing it with a single, simplified **Standardized Approach (SMA)**. | `[REG/OpRisk]` | The complex "Monte Carlo" OpRisk models of the past were inconsistent and prone to gaming. The new system uses a simple formula based on income and loss history. |
| `P.64.3` | **Restrictions on A-IRB:** Banks are no longer allowed to use the **Advanced IRB** approach for exposures to large/mid-size corporates and financial institutions; they must use **Foundation IRB (F-IRB)**. | `[REG/Credit]` | For complex counterparties, regulators don't trust banks to estimate their own LGD and EAD. You can estimate the probability of default (PD), but the regulator provides fixed values for LGD and EAD. |
| `P.64.4` | **G-SIB Leverage Buffer:** Global Systemically Important Banks (G-SIBs) are required to hold an additional leverage ratio buffer that **must be met with Tier 1 capital**. | `[REG]` | If you are "Too Big To Fail," the tax is higher. You need an even larger "Equity Anchor" to prevent a systemic collapse. |
| `P.64.5` | **Granular Standardized Approach:** The new SA for Credit Risk is more granular and relies less on external ratings, using specific risk-weight tables for different asset classes (e.g., LTV for mortgages instead of a flat rate). | `[REG/Credit]` | Making the "Default" approach more accurate reduces the incentive for banks to spend millions on complex internal models just to "save" capital. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank's Internal Model RWA is 50% of the Standardized RWA:** Then the **Output Floor** kicks in. The bank's reported RWA will be forced upward to **72.5%** of the Standardized value.
- **Variable Flip: If a bank wanted to use an internal model for CVA (Credit Valuation Adjustment) risk:** This is no longer allowed under the Basel III finalization rules. CVA must use the standardized approach.
- **Variable Flip: If a large bank estimated its own LGD for a loan to another bank:** This is a violation of the A-IRB restrictions. For bank exposures, only F-IRB (Regulator-provided LGD) is permitted.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Output Floor:** 72.5%. | **Output Floor:** 80% or 50% are distractors. |
| **Operational Risk:** No more AMA; now only SA (SMA). | **Operational Risk:** IRB was never the primary term; it was AMA. |
| **G-SIB Buffer:** Applies to both the risk-based ratio AND the leverage ratio. | **LCR/NSFR:** Are liquidity ratios; the Output Floor is a capital ratio limit. |

## 4. Directional Intuition
- **Internal Model RWA Variability $\uparrow \rightarrow$ Regulatory Skepticism $\uparrow \rightarrow$ Output Floor Stringency $\uparrow$:** The 72.5% floor exists because different banks were calculating wildly different capital levels for the exact same assets.
- **Reliance on External Ratings $\downarrow \rightarrow$ SA Complexity $\uparrow$:** By providing more "Built-in" risk weights, Basel reduces the power of ratings agencies like Moody's or S&P over bank capital.
- **Income & Loss History $\uparrow \rightarrow$ Operational Risk Capital $\uparrow$:** The new SMA formula treats a bank's income (positive correlation with risk) and a history of big losses as direct indicators of high future operational risk, removing the "Smoothing" allowed by old AMA models.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Finalization" Name:** Note that "Basel III Finalization" is often colloquially called **Basel IV**, though the BCBS officially calls it an update to Basel III.
- **A-IRB vs. F-IRB for Corporates:** Can you use A-IRB for a small local business? **YES** (some exceptions apply). Can you use it for a large or mid-size corporate? **NO (Must use F-IRB).**
- **The Floor Math:** Higher of (Approved Internal Model calculated RWA) or (72.5% of Standardized RWA).
- **CVA Risk:** Is there an internal model option left for CVA? **NO.** Only Standardized (SA-CVA) or Basic (BA-CVA), or applying 100% of the counterparty credit risk capital requirement.
- **F-IRB Parameters:** F-IRB requires fixed values for both Loss Given Default (LGD) and Exposure at Default (EAD). These were the two parameters causing the most variability under A-IRB.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
