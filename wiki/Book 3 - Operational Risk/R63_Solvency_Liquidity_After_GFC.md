# R63 — Solvency, Liquidity, and Regulation After the GFC

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.63.1` | **The Capital Conservation Buffer (CCB):** A 2.5% Tier 1 equity buffer built during normal times to be absorbed during stress, bringing the effective CET1 minimum from 4.5% to **7.0%**. | `[REG/Basel III]` | It’s a "Rainy Day Fund." You aren't allowed to pay dividends or bonuses unless you've filled this extra bucket first. |
| `P.63.2` | **Liquidity Coverage Ratio (LCR):** Designed for a **30-day** stress period. Formula: `High-Quality Liquid Assets (HQLA) / Net Cash Outflows >= 100%`. | `[REG/LIQ]` | Can the bank survive a "Bank Run" for exactly one month? This ensures you have enough "Fast Cash" to handle the panic. |
| `P.63.3` | **Net Stable Funding Ratio (NSFR):** A longer-term (1-year) measure ensuring long-term assets are funded by stable, long-term liabilities. | `[REG/LIQ]` | Prevents "Maturity Mismatch." You shouldn't fund a 30-year mortgage with 1-day deposits (Hot Money). |
| `P.63.4` | **Leverage Ratio:** A simple, non-risk-based backstop: `Tier 1 Capital / Total Exposure >= 3%`. | `[REG]` | The "Reality Check." Risk-weights (Basel II) can be manipulated; the leverage ratio looks at the raw size of the bank's footprint. |
| `P.63.5` | **Contingent Convertibles (CoCos):** Debt instruments that automatically convert to equity when a bank's capital falls below a specific trigger. | `[THE/FIN]` | CoCos are "Emergency Equity." They act like debt in good times (cheap) and like a "Lifejacket" in bad times (loss-absorbing). |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank has HQLA of $90M and Outflows of $100M:** Then the LCR is **90%**, which is a regulatory failure ($\text{Min} = 100\%$). The bank must either raise more cash or reduce its short-term liabilities.
- **Variable Flip: If a bank is "Solvent" but has an LCR of 0%:** Then the bank will still collapse. Solvency means your assets are worth more than your debts *long-term*, but without liquidity (LCR), you can't pay the bill that's due *today*.
- **Variable Flip: If the Capital Conservation Buffer (CCB) was discretionary by local regulators:** This is **FALSE**. The CCB is a fixed Basel III requirement meant for all economic cycles (though the *Counter-Cyclical* buffer is discretionary).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **LCR Horizon:** 30 days. | **NSFR Horizon:** 1 year. |
| **Common Equity Tier 1 (CET1):** The purest form of capital (common stock/retained earnings). | **Tier 2 Capital:** Lower quality (subordinated debt). |
| **Leverage Ratio:** Uses **Total Exposure** (non-risk-weighted). | **Capital Ratios:** Use **Risk-Weighted Assets** (RWA). |

## 4. Directional Intuition
- **Economic Stress $\uparrow \rightarrow$ CCB Usage $\uparrow \rightarrow$ Dividend Restrictions $\uparrow$:** The buffer is designed to be eaten in a crisis, but doing so triggers a "penalty" where you can't give money back to shareholders.
- **Stable Funding (NSFR) $\uparrow \rightarrow$ Liquidity Risk $\downarrow$ BUT $\rightarrow$ Profitability $\downarrow$:** Long-term funding is more expensive than short-term funding. Basel III forces banks to trade profit for safety.
- **G-SIB Surcharge $\uparrow \rightarrow$ Systemic Risk $\downarrow$:** The "Too Big to Fail" surcharge makes it more expensive to be a giant bank, encouraging firms to shrink and simplify.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "7% CET1" Rule:** Where does 7 come from? Answer: **4.5% (Min) + 2.5% (CCB).**
- **Solvency vs. Liquidity:** Which is the "Bank Run" risk? **Liquidity (LCR).** Which is the "Bankruptcy" risk? **Solvency.**
- **CoCos drag on ROE:** Do CoCos hurt ROE in good times? **NO.** They are debt, which is cheaper than equity. They only "dilute" and hurt ROE if they convert during a crisis.
- **The LCR Calculation:** GARP loves to give you HQLA and Net Outflows and ask for the ratio. **Rule: Must be >= 100%.**
- **Deductions:** Does a pension *surplus* add to capital? **NO.** Only a *deficit* subtracts from it. Surpluses are ignored ("Prudence").


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
