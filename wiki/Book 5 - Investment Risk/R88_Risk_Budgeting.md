# R88 — VaR and Risk Budgeting in Investment Management

**Exam Priority:** 🟡 Medium (1-2 questions) in Investment Management

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.88.1` | **Risk Budgeting:** A top-down process where the total risk appetite of an institution is decomposed and allocated across asset classes, factors, or managers. | `[OPS]` | You decide how much "Risk" (not just money) to spend. If you have $100 of risk, you give $50 to Equities, $30 to Bonds, and $20 to Alternatives. |
| `P.88.2` | **Buy Side vs. Sell Side:** Buy-side firms (Insurers, Pensions) have historically focused on **Tracking Error** and **Notional Limits**. Recently, they have moved toward the Sell-side (Banks) model of using **Forward-looking VaR** and **VaR Limits**. | `[THE/OPS]` | Banks are "Sprint Runners" (Short term); Pensions are "Marathon Runners" (Long term). But the marathon runners have realized they still need a "Heart Rate Monitor" (VaR) to avoid collapsing mid-race. |
| `P.88.3` | **Surplus VaR (Pension Focus):** Funding risk is the possibility that assets will not cover liabilities. Surplus VaR measures the potential drop in the **Asset-Liability Surplus**. | `[MTH/THE]` | If you owe $100 and have $110, you have a $10 "buffer." Surplus VaR tells you: "There is a 5% chance your buffer will disappear or become negative next month." |
| `P.8.4` | **Guidelines — Beyond Notionals:** Modern risk management replaces cumbersome **Notional Limits** (e.g., "$10M in Oil") with more effective **VaR Limits**, which capture the actual risk/volatility interactions of the position. | `[OPS]` | A $10M bet on "Cash" is safe; a $10M bet on "Bitcoin" is a heart attack. Notional limits treat them the same; VaR correctly sees the difference. |
| `P.88.5` | **Optimal Manager Allocation:** The optimal weight assigned to an active manager $i$ is proportional to their Skill (IR) and the Portfolio's desired risk level: $ w_i = \frac{IR_i}{IR_p} \frac{\sigma_p}{\sigma_i} $. | `[MTH]` | You give the most "Risk Budget" to the manager with the best "Sharpshooter" record (High IR). If they are a "High-Volatility" shooter, you give them less money to keep the risk stable. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If multiple managers take on the SAME trade:** This is a **Concentration Failure**. Centralized VaR monitoring is required to detect when three different "Independent" managers have all secretly bet on the same stock, increasing portfolio-level risk.
- **Variable Flip: If a manager manages a "Passive" portfolio:** They still need **Risk Monitoring**. The benchmark's own risk characteristics (volatility/sector weights) can change over time, requiring the manager to adapt.
- **Variable Flip: If "Low Liquidity" assets are in the fund:** Their volatility and correlation measures will be **Downfolded (Biased Lower)**. VaR systems must adjust for "stale prices" to avoid underestimating true risk.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Absolute Risk:** Total potential dollar loss of the assets. | **Active Risk:** Risk of the benchmark (NO: it's the risk relative to benchmark). |
| **Funding Risk:** Assets < Liabilities. | **Financial Risk:** Market/Credit risk (NO: Funding risk is the ALM mismatch). |
| **Rogue Traders:** Detected via centralized VaR monitoring. | **Rogue Traders:** Prevented by notional limits (NO: they can circumvent notionals). |

## 4. Directional Intuition
- **Information Ratio$_i \uparrow \rightarrow$ Optimal Weight $w_i \uparrow$:** Efficient allocation puts more capital in the hands of the most skilled managers.
- **Asset-Liability Correlation $\uparrow \rightarrow$ Surplus VaR $\downarrow$:** If your assets (bonds) move exactly like your liabilities (pension obligations), your "Surplus" is safe even if the market crashes.
- **Global Custodians $\uparrow$ (Use of) $\rightarrow$ Risk Transparency $\uparrow$:** Centralizing data makes it easier to track "Factor Concentration" across many sub-funds.

## 5. Ambiguity Traps (Anti-Decoder)
- **Weight Sum:** Do active manager weights have to sum to 100%? **NO.** Any leftover weight goes into the **Passive Benchmark**.
- **Information Ratio of Benchmark:** What is it? **ZERO.** (There is no alpha/active return relative to itself).
- **Hedge Funds:** Are they "Buy Side"? Nominally yes, but their **High Turnover** and **Leverage** make them behave like "Sell Side" bank desks.
- **Shortfall Math:** `(Expected Surplus) - (Surplus VaR)`. This is the "Worst-Case Surplus" at the given confidence level.
- **Notionals:** Why are they bad? Because they are "Ad Hoc" and "Easily Circumvented" (e.g., using derivatives to hide a position).
- **Sponsor Risk:** 
    - **Cash Flow:** Will the company have the money to pay into the plan? 
    - **Economic:** Will the plan's earnings be stable?
- **Global Custodian:** Why use them? For **Consolidated Reporting** across many different managers with different styles.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
