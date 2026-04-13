# R33 — Counterparty Risk and Beyond

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.33.1` | **Counterparty Credit Risk (CCR):** The risk that a counterparty defaults *prior* to the final settlement of a transaction. It is "unilateral" in lending but "bilateral" in derivatives. | `[THE/MTH]` | In a loan, only the bank is scared. In a swap, both people are looking at each other nervously because who "owes" whom depends on the market price tomorrow. |
| `P.33.2` | **The Bilateral Nature:** Derivatives are two-way risks. If the contract is an asset for you (Positive Mark-to-Market), you have credit risk. If it's a liability (Negative MtM), the other person has credit risk. | `[MKT/THE]` | It’s a "See-Saw." One side is always "Up" (has the exposure) and the other is "Down" (owes the money). As market prices change, the see-saw flips. |
| `P.33.3` | **Pre-settlement Risk vs. Settlement Risk:** Pre-settlement is the risk over the life of the trade. Settlement risk (Herstatt risk) is the small window of hours where you've sent your cash but haven't received theirs yet. | `[OPS/THE]` | Pre-settlement is the "Engagement" (years of wondering if they'll show up). Settlement is the "Wedding Ceremony" (the 5 minutes where you've said "I do" and are waiting for them to say it back). |
| `P.33.4` | **Risk-Neutral ($Q$) vs. Real ($P$) Measures:** Use **Risk-Neutral** probabilities (market prices) for CVA and pricing; use **Real/Physical** probabilities (history) for VaR and capital. | `[MTH/REG]` | Pricing is about "What the market thinks today" (Q). Risk measurement is about "What history says could actually happen" (P). |
| `P.33.5` | **Mitigation Trade-offs:** Reducing CCR through collateral or CCPs doesn't make risk disappear; it transforms it into **Liquidity Risk** (getting margin calls) or **Systemic Risk** (the CCP itself failing). | `[THE/ECO]` | You’ve traded a "Possible Heart Attack" (Default) for "Constant Stress" (Margin Calls). You’re safer, but you need to keep a lot of cash ready at all times. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a firm has a NEGATIVE Mark-to-Market (MtM) value:** It has **ZERO** exposure to the counterparty's default. From its perspective, the contract is a liability; if the counterparty dies, the firm still owes money, but it doesn't "lose" anything.
- **Variable Flip: If you use the Real-World ($P$) probability for CVA pricing:** You will **Misprice** the derivative. CVA is a market-available charge and must be calculated using market-implied (risk-neutral) defaults.
- **Variable Flip: If the probability of default ($PD$) decreases over time:** This is common in the very distant future. Why? Because if the firm was going to die, it would likely have died *already* by year 10, making the surviving "future" self mathematically less likely to surprise you with a default.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **CCR:** Always pre-maturely focused. | **CCR:** Focused on the final payment only (NO: that’s settlement risk). |
| **Bilateral:** Both parties at risk. | **Bilateral:** Only the weaker party is at risk (NO: both are, at different times). |
| **Risk-Neutral (Q):** Used for CVA. | **Real-World (P):** Used for CVA (NO: used for VaR). |

## 4. Directional Intuition
- **Market Volatility $\uparrow \rightarrow$ Potential Future Exposure (PFE) $\uparrow \rightarrow$ CCR $\uparrow$:** If the price "shaking" gets wilder, the see-saw could tip much higher in your favor, meaning you have more to lose if they quit.
- **Maturity $\downarrow \rightarrow$ Time to Default $\downarrow \rightarrow$ CCR $\downarrow$:** As the trade approaches the "Finish Line," there is less time for the counterparty to go bankrupt.
- **Collateral $\uparrow \rightarrow$ Counterparty Risk $\downarrow$:** If they give you their "Watch" as a deposit, you don't care if they walk away—you keep the watch.

## 5. Ambiguity Traps (Anti-Decoder)
- **CVA Calculation:** CVA is an **Expectation**. It’s the average loss, not the "worst case."
- **Herstatt Risk:** This is the specific name for **Settlement Risk**. Common in FX trades (different time zones).
- **MtM Thresholds:** Note that exposure only exists when $MtM > 0$. If $MtM < 0$, exposure is zero (you are the one owing them).
- **OTC vs. Exchange:** OTC (Private) is the home of CCR. Exchanges (CME, ICE) use CCPs to virtually eliminate it for individual traders.
- **"Risk-Neutral" is not "Objective":** It’s a mathematical tool. It reflects the prices people are willing to pay for insurance, not necessarily the actual stats of bankruptcies.
- **Replacement Cost:** The fundamental concept of CCR. If they default, you have to go to the market and buy the same trade at "Current Prices." The loss is the cost of doing that.
- **Sovereign Counterparties:** They often don't provide collateral (because they're the government), creating huge unmitigated CCR for banks.
- **Waterfall of Risk:** Remember that CCR has its own "EL, UL, VaR" just like traditional credit risk.
- **The Ondine Paradox:** If you owe $1M and your counterparty defaults, you might actually "profit" if you can get out of the trade without paying the full net (though laws usually prevent this).
- **Systemic Fragility:** The more we centralize everything into a few mega-CCPs, the more vulnerable we are to a "Super-Default" that crashes everything at once.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
