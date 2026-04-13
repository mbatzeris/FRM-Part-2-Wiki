# R38 — Credit Value Adjustment (CVA)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.38.1` | **CVA (Credit Value Adjustment):** The "Market Price" of counterparty credit risk. It is the cost to the counterparty that bears a greater propensity to default. Risky Value = Risk-Free Value - CVA. | `[MTH/MKT]` | It’s the "Risk Tax." If a swap is worth $100 but the guy might default, you only value it at $98. The $2 is the CVA. |
| `P.38.2` | **The CVA Spread Approximation:** For a quick estimate, the CVA running spread $\approx -EPE \times \text{Credit Spread}$. Alternatively, to convert an upfront CVA to a spread, divide by the Risky Duration: $\text{Spread} = \frac{-CVA}{\text{Risky Duration} \times \text{Notional}}$. | `[MTH]` | It’s spreading the "Big Upfront Risk Tax" into a small "Monthly Insurance Premium" tacked onto the swap rate. |
| `P.38.3` | **Debit Value Adjustment (DVA):** The "CVA of yourself." It represents the benefit of *your* own credit risk to your counterparties. (When your credit gets worse, DVA increases, which "helps" your earnings). | `[THE/REG]` | It’s the "Deadbeat Dividend." If you are close to bankruptcy, your debts are worth less, which technically makes your balance sheet look "stronger" (the DVA paradox). |
| `P.38.4` | **Wrong-Way Risk (WWR):** An adverse correlation between exposure and default. Your exposure hits its maximum exactly when the counterparty is most likely to default. | `[MKT/THE]` | It’s "Buying Umbrella Insurance from a guy whose house just flooded." Exactly when you need the money, he can't pay you because the same storm hit both of you. |
| `P.38.5` | **Incremental vs. Marginal CVA:** Incremental CVA is the "before-and-after" impact of a new trade (using $\Delta EE$). Marginal CVA breaks down the total netted portfolio into individual trade contributions ($Marginal EE$). | `[OPS/THE]` | Incremental: "If we do this new deal, how much more risk do we add?" Marginal: "Looking at our existing pie, who is eating the biggest slice?" |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Correlation between your exposure and the counterparty's credit is POSITIVE:** You are facing **Wrong-Way Risk**. Your CVA will be significantly **Underestimated** if you use a standard model that assumes no correlation.
- **Variable Flip: If a firm has a perfectly HEDGED portfolio (Netting = 100%):** The **Incremental CVA** of a new trade that offsets a winning position can be **NEGATIVE**. Adding the trade actually reduces the total risk of the firm.
- **Variable Flip: If the Recovery Rate ($R$) is 100%:** The **CVA is ZERO**. If you get all your money back regardless of default, the risk is free.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **CVA:** Market-implied (Risk-neutral Q). | **CVA:** Historically-based (Real-world P) (NO: used for VaR). |
| **WWR:** Upward-sloping correlation. | **Right-way Risk:** Upward-sloping correlation (NO: that’s WWR). |
| **DVA:** Your default risk. | **DVA:** Your counterparty's default risk (NO: that’s CVA). |

## 4. Directional Intuition
- **Counterparty CDS Spreads $\uparrow \rightarrow$ Default Probability ($q$) $\uparrow \rightarrow$ CVA $\uparrow$:** If the market thinks they are riskier, your "Risk Tax" goes up.
- **Interest Rates $\uparrow \rightarrow$ Future Exposure $\uparrow$ (for fixed-rate receivers) $\rightarrow$ CVA $\uparrow$:** If the value of your trade grows, you have more to lose.
- **Collateralization $\uparrow \rightarrow$ EE $\downarrow \rightarrow$ CVA $\downarrow$:** If they give you cash deposits, your effective exposure drops, making the CVA smaller.

## 5. Ambiguity Traps (Anti-Decoder)
- **Settlement vs Actual Recovery:** If the Actual Recovery rate is higher than the Settled Recovery rate, the CVA is actually **lower** than if both were assumed to be the low settlement amount. 
- **Upward vs Downward Sloping Credit Spreads:** An upward-sloping credit curve generates a **lower** CVA than a downward-sloping curve (because downward means high default risk early on when exposure is heavily discounted).
- **Collateralization's Impact:** Collateral only reduces the Expected Exposure (EE); it has **no impact whatsoever** on the counterparty's Probability of Default.
- **The MPoR Rule:** At an MPoR of 40 days, the CVA is roughly half the size of the uncollateralized CVA. If expanding MPoR (e.g., from 10 to 20 days), the CVA is scaled by the square root of time ($\sqrt{20/10}$).
- **Netting Limitations:** Netting reduces CVA because it nets exposure, but the CVA with netting can **never be higher** than the CVA without netting. The benefits of netting decrease as the transaction size grows.
- **Incremental vs. Marginal CVA:** 
    - **Incremental** = "Before and After" the new trade (Ex-Ante impact). 
    - **Marginal** = "Splitting the Pie" into pieces for each trade (Ex-Post view of the trades).
- **DVA Paradox:** Banks love it when their credit rating drops in the short term because DVA gains boost their accounting profits. Regulators hate it because it’s "fake" money you can't use to pay bills.
- **Risk-Neutrality:** CVA must be calculated using **Market-Implied PD** (from CDS or bonds), not from Moody's/S&P historical tables.
- **BCVA (Bilateral CVA):** $CVA - DVA$. This is the "Fair" amount to charge for the risk in a two-way derivative.
- **Currency Swaps & WWR:** If a company in Brazil owes USD to a New York bank, and the Real (BRL) crashes:
    1.  The bank's exposure grows (they are owed more valuable USD).
    2.  The Brazilian company is more likely to default (it's harder for them to buy USD with cheap BRL).
    3.  This is a massive WWR combo.
- **Wrong-Way Risk vs. Right-Way Risk:** Speculation often creates WWR; Hedging often creates RWR.
- **The "Sum of Losses":** Remember that CVA is not just a point-in-time calculation; it’s an integral over the survival curve.
- **CVA VaR:** Also known as **CVA Volatility**. Banks must hold capital not just for the default itself, but for the *change* in CVA value as spreads move.
- **Credit Value Adjustment vs. Capital Charge:** 
    - **CVA** is a pricing adjustment (P&L). 
    - **K-CVA** is a regulatory capital requirement (Basel III).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
