# R82 — Risk Management for Changing Interest Rates (ALM)

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.82.1` | **The ALM Philosophy:** Asset-Liability Management (ALM) is an integrated approach where the bank manages both sides of the balance sheet as a unified whole, rather than in isolation. | `[THE/OPS]` | You don't manage your "Credit Card debt" and "Savings account" in separate rooms. You look at both to see if you're actually getting richer or poorer as interest rates move. |
| `P.82.2` | **Interest-Sensitive (IS) Gap:** Measures the impact of interest rate changes on **Net Interest Income (NII)**. `IS Gap = Sensi_Assets - Sensi_Liabilities`. | `[MTH/ECO]` | If you have $100M of loans that reset today (Assets) but only $40M of deposits that reset today (Liabilities), your gap is +$60M. You are "Asset Sensitive." |
| `P.82.3` | **Asset vs. Liability Sensitivity:** If IS Gap is **Positive**, NII rises when rates rise. If IS Gap is **Negative**, NII falls when rates rise. | `[MKT/ECO]` | **Positive Gap:** You're a "Lender" waiting for higher rates. **Negative Gap:** You're a "Borrower" afraid of higher rates. |
| `P.82.4` | **Leverage-Adjusted Duration Gap:** Measures the impact of interest rate changes on the **Net Worth (Capital)** or market value of the bank. `Dur_Gap = DA - (L/A * DL)`. | `[MTH]` | This is the "Equity Protection" metric. It tells you how much your bank's "Fair Value" will drop if the whole yield curve shifts up by 1%. |
| `P.82.5` | **Dual-Hedge Challenge:** It is often impossible to perfectly hedge both NII (IS Gap) and Net Worth (Duration Gap) simultaneously. Managers must choose which "Volatility" to tolerate. | `[OPS]` | You can lock in your "Income" (Short term) or protect your "Inheritance" (Long term), but trying to do both perfectly often leaves you with a messy, expensive hedge. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank has a Positive Duration Gap and rates rise:** Its Net Worth **Falls**. This is because the assets (long duration) lose more value than the liabilities (short duration), shrinking the equity "cushion."
- **Variable Flip: If a bank has a Negative IS Gap and rates rise:** Its **Net Interest Margin (NIM) is squeezed**. The cost of funds (liabilities) resets to the new higher rates faster than the yield on the assets, reducing the bank's profit "spread."
- **Variable Flip: If a bank matches $DA = DL$ but has $L/A = 0.90$:** The duration gap is NOT zero. It is `DA - (0.9 * DL)`. To have a zero duration gap, the bank must have `DA = (L/A) * DL`. Because banks are leveraged (Assets > Liabilities), the Asset duration must be *shorter* than the Liability duration to be immune.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **IS Gap:** Focuses on Net Interest Income (Short-term / Cash flow). | **Duration Gap:** Focuses on Net Interest Income (NO: it's for Net Worth / Value). |
| **Asset Sensitive (+ Gap):** Benefits from rising rates. | **Liability Sensitive (+ Gap):** (NO: negative gap is liability sensitive). |
| **Duration Limitations:** Assumes small, parallel shifts in yield curve. | **Duration Limitations:** Only works for floating-rate instruments (NO: it's for fixed-rate). |

## 4. Directional Intuition
- **Interest Rates $\uparrow \rightarrow$ (+ IS Gap) $\rightarrow$ NII $\uparrow$:** The bank "wins" on income as its loans reprice higher while its debts stay locked in.
- **Interest Rates $\uparrow \rightarrow$ (+ Dur Gap) $\rightarrow$ Net Worth $\downarrow$:** The bank "loses" on valuation as the present value of its long-term assets collapses.
- **Asset Duration $\uparrow$ (e.g., buying 30yr mortgages) $\rightarrow$ Duration Gap $\uparrow \rightarrow$ Interest Rate Risk $\uparrow \uparrow$:** Small moves in rates cause massive swings in the bank's capital.

## 5. Ambiguity Traps (Anti-Decoder)
- **Income vs. Value:** Does IS Gap protect the bank's "Stock Price"? **NO.** It protects the "Quarterly Income." Duration Gap is closer to "Stock Price" (Value).
- **The "Leverage" in Duration:** Don't forget the **`(L/A)`** term. `DA - (L/A) * DL`. If you ignore this, you'll calculate the wrong gap.
- **Repricing Timing:** Can you perfectly time a checking account's repricing? **NO.** That's a major limitation of IS Gap. Use **Behavioral assumptions**.
- **Liability Sensitive:** If a bank is funded by overnight CDs and has 5-year fixed mortgages, it is **Liability Sensitive**. (Rates UP = Profit DOWN).
- **Zero Gap:** If `Dur_Gap = 0`, is the bank "Safe"? **Partially.** It is immune to parallel shifts, but not to **Slope** (Twist) or **Convexity** changes.
- **NII squeeze:** Look for a **Negative IS Gap** in a **Rising Rate** environment.
- **Capital decline:** Look for a **Positive Duration Gap** in a **Rising Rate** environment.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
