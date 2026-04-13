# R72 — Monitoring Liquidity

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.72.1` | **Deterministic vs. Stochastic Flows:** Deterministic flows have fixed time and amount; Stochastic flows have random time and/or amount (e.g., prepayments, defaults, credit lines). | `[THE/MTH]` | A bond coupon is a "clockwork" payment (Deterministic). A mortgage prepayment is a "Maybe" payment (Stochastic). |
| `P.72.2` | **Liquidity Options:** Unlike financial options (exercised for profit), liquidity options are exercised based on a **Need** for cash, even if the exercise is mathematically "Out-of-the-Money." | `[THE]` | If you're starving, you'll sell your gold at a loss just to eat. In liquidity stress, the "Price" is secondary; "Survival" is the trigger. |
| `P.72.3` | **Liquidity Generation Capacity (LGC):** The potential to generate positive cash flows from asset sales, secured (Repo), or unsecured (Credit lines) sources beyond existing contracts. | `[OPS]` | It’s your "Reserve Power." How much cash can you squeeze out of your balance sheet if you *really* have to? |
| `P.72.4` | **TSECCF — The Survival Anchor:** The Term Structure of Expected Cumulated Cash Flows must ideally be **positive at all times** to ensure the bank avoids insolvency/default. | `[OPS/MTH]` | Your "Bank Account Balance" over time. If the cumulative line ever dips below zero, you've run out of cash and the bank stops functioning. |
| `P.72.5` | **TSLaR (Liquidity-at-Risk):** Measures the **Unexpected** cash flows at a given date, representing the difference between the average (expected) and minimum (worst-case) levels of cash flows. | `[MTH]` | It’s the "Cushion Size." How much *extra* cash do you need to hold to handle the gap between what you *expect* to happen and what *could* happen? |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a new bond issuance is scheduled for June 1st but the buyer hasn't signed:** This is **Time-Deterministic but Amount-Stochastic**. You know when it's supposed to happen, but you don't know the exact final cash flow until it settles.
- **Variable Flip: If an investor exercises a "Financial Option" just to get liquidity:** This is a **Liquidity Option** exercise. If the motivation is cash availability rather than profit (ITM), it falls into the liquidity monitoring bucket.
- **Variable Flip: If a Treasury Department only monitors TSECF (Individual flows):** They are blind to the "Cumulative" problem. You can have a positive individual flow on Friday but still be bankrupt if your cumulative balance was -$1B on Thursday. **TSECCF** is the superior anchor.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Quantitative Risk:** Inability to secure funds / lower cash inflows. | **Credit Risk:** Is about the counterparty's ability to pay, not the bank's own cash flows. |
| **Funding Cost Risk:** Widening spread vs. Risk-Free Rate. | **Market Risk:** Is about price volatility, not the cost of accessing the market. |
| **Possession (TSAA):** Drives availability for liquidity purposes. | **Ownership:** Is less important for immediate liquidity than who physically "holds" the asset. |

## 4. Directional Intuition
- **Asset Volatility $\uparrow \rightarrow$ Haircuts $\uparrow \rightarrow$ Liquidity Generation Capacity $\downarrow$:** As the market gets wilder, your "jewelry" is worth less at the pawn shop (Repo market).
- **Cumulative Cash Flow $\downarrow \rightarrow$ Negative TSECCF $\rightarrow$ Bankruptcy Risk $\uparrow$:** The closer the cumulative line gets to zero, the higher the probability of a "Liquidity Default."
- **Liquidity Option Exercise $\uparrow \rightarrow$ Asset Shrinkage/Liability Expansion:** Depending on the side of the trade, the exercise of customer options (like drawing down lines) forces the bank to react immediately.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Bonds" Trap:** Is a new bond issuance deterministic? **Partially.** It is **Time-Deterministic** (you set the date) but **Amount-Stochastic** (the market decides the final fill).
- **Profit vs. Need:** Are liquidity options exercised when profitable? **NO.** They are exercised when **CASH IS NEEDED**.
- **TSLGC vs TSAA:** TSAA is the **Available Assets** (the inventory); TSLGC is the **Capacity** to turn that inventory into cash (the engine).
- **The "Solvency precursor":** A negative cumulative cash flow (TSECCF) is the primary precursor to **Bankruptcy**.
- **Security-linked vs Unlinked:** Repo is linked (securitized); Unsecured bonds are unlinked (general credit).
- **Reverse Repo:** Does it increase TSAA? **YES.** You get the asset in your possession, increasing your ability to generate liquidity elsewhere.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
