# The Boole Scaffold: Reading 30 — Credit Risk

**Exam Priority:** 🟡 Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2 · Hull, Chapter 25*
*Learning Objectives Covered: 30.a, 30.b, 30.c, 30.d, 30.e, 30.f, 30.g*
*Related Readings: [R27 — Estimating Default Probabilities](R27_Estimating_Default_Probabilities.md), [R29 — Portfolio Credit Risk](R29_Portfolio_Credit_Risk.md), [R31 — Credit Derivatives](R31_Credit_Derivatives.md), [R38 — Credit Value Adjustment (CVA)](R38_CVA.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|:---|:---|:---:|:---|:---|
| P1 | **PD from Credit Spreads (LO 30.c):** If $s$ is the bond yield spread over the risk-free rate and $R$ is the recovery rate, the average hazard rate (default intensity) is approximately $\lambda \approx \dfrac{s}{1-R}$. The **conditional PD in year $n$, given survival through year $n-1$**, is $\dfrac{\text{Unconditional PD}_n}{\text{Survival Probability}_{n-1}}$. *Intuition: The spread is the market's "danger pay" for holding risky debt; dividing by $(1-R)$ converts the spread into the per-year probability of the default actually happening.* | `[THE]` | Very High — the $s/(1-R)$ formula is the single most-tested LO 30.c calculation. | "hazard rate," "default intensity," "$s$ divided by $(1-R)$," "conditional default probability" |
| P2 | **Risk-Neutral vs Real-World PD (LO 30.c):** **Risk-neutral** PDs are implied by market prices (bond spreads, CDS) and are used for **pricing instruments** and valuing credit derivatives. **Real-world (physical)** PDs are estimated from historical rating-agency data and are used for **scenario analysis / future-loss estimation**. Risk-neutral PDs are systematically *higher* than real-world PDs. The primary driver of the gap is that defaults are **not independent** — systematic risk cannot be diversified away, so investors demand extra yield. *Intuition: The market charges a "crash insurance premium" on top of the true historical odds. When you price a derivative, use the market's nervous number (Q). When you forecast losses, use history's calmer number (P).* | `[THE]` | Very High — the Q-vs-P distinction and the "pricing vs loss forecasting" mapping is exam gold. | "risk-neutral probability," "real-world probability," "$Q$ vs $P$," "pricing vs scenario analysis," "systematic risk" |
| P3 | **ISDA Master Agreement & Event of Default (LO 30.a):** Bilaterally cleared derivatives are governed by an **ISDA Master Agreement** specifying initial and variation margin. On default, the non-defaulting party becomes an **unsecured creditor** in two situations: (1) their position value is **positive and exceeds** the defaulter's posted collateral (loss = value − collateral), or (2) their position value is **negative but smaller in magnitude** than the collateral *they* posted (loss = collateral − |value|, i.e., the excess collateral trapped in the defaulter's estate). *Intuition: Collateral is a shield, not armor. If your claim overshoots the shield, or your own deposit is stuck inside a bankrupt counterparty's pile, the excess becomes an ordinary claim in bankruptcy court.* | `[REG]` | High — unsecured-creditor situations are a classic exam calculation. | "ISDA Master Agreement," "event of default," "unsecured creditor," "posted collateral" |
| P4 | **CVA & DVA (LO 30.b):** For each counterparty a bank has exactly one **CVA** and one **DVA**. **CVA** = present value of the expected cost to the *bank* if the *counterparty* defaults. **DVA** = present value of the expected cost to the *counterparty* if the *bank* defaults (which is therefore a *benefit* to the bank because bank-default releases it from paying). Derivative value accounting for default = **No-default value − CVA + DVA**. A new trade **positively** correlated with existing trades **increases** both CVA and DVA; a **negatively** correlated trade **decreases** both. **Wrong-way risk**: PD is *positively* correlated with exposure (bad). **Right-way risk**: PD is *negatively* correlated with exposure (good). *Intuition: CVA is the "risk tax" you pay on the value of your winning trades. DVA is the mirror-image tax you owe to the other side on their winners — which, paradoxically, improves *your* balance sheet when *your* own credit worsens.* | `[REG]` | Very High — CVA/DVA definitions and the correlation-impact rule are staple exam content. | "credit value adjustment," "debt value adjustment," "CVA DVA," "wrong-way risk," "right-way risk," "no-default value" |
| P5 | **Credit Risk Mitigants (LO 30.d):** Three standard tools for bilaterally cleared transactions: **(1) Netting** — aggregate positive and negative MtMs into a single net exposure (e.g., +$12M, −$4M, −$3M ⇒ net +$5M, reducing exposure from $12M to $5M, a $7M reduction). **(2) Collateral agreements** — posted cash/securities kept by the non-defaulting party on default. **(3) Downgrade triggers** — contractual rights that activate if the counterparty's rating falls below a threshold, letting the bank close out at market value or demand collateral. Trigger value **erodes** when the counterparty has big downgrades or has triggers with multiple dealers simultaneously. *Intuition: Netting shrinks the wound before it opens. Collateral is the deposit you keep. Downgrade triggers are the "early exit" option that becomes worthless exactly when everyone else is trying to exit at the same time.* | `[OPS]` | High — netting calculations and trigger mechanics are frequently tested. | "netting," "collateral agreements," "downgrade triggers," "exposure reduction" |
| P6 | **Default Correlation — Reduced-Form vs Structural (LO 30.e):** Default correlation exists because (1) external sector/region shocks, (2) economy-wide cycles, and (3) **contagion** — one firm's default triggering another's. **Reduced-form models** assume hazard rates follow correlated stochastic processes driven by macro variables. Mathematically simple, they reflect economic cycles well but produce **low achievable correlations** (two firms defaulting in the same short window is unlikely in the model). **Structural models** (Merton-like, correlated asset processes) produce **arbitrarily high correlations** but are **computationally heavy**. *Intuition: Reduced-form models say "we all dance to the same economic music"; structural models say "our asset values are tethered together and if one firm's assets fall, yours do too." The second model is more flexible but takes much longer to run.* | `[THE]` | Very High — the reduced-form vs structural comparison is a staple LO 30.e distractor set. | "reduced-form model," "structural model," "default contagion," "Merton-type asset correlation" |
| P7 | **Gaussian Copula for Time-to-Default (LO 30.f):** The Gaussian copula transforms each firm's non-normal time-to-default $\tau_i$ into a standard normal variable $x_i$ via percentile-to-percentile mapping, then assumes the $x_i$'s are jointly multivariate-normal. The resulting default correlation is the **copula correlation** $\rho$. In the **one-factor** version, $x_i = \sqrt{\rho}\,F + \sqrt{1-\rho}\,Z_i$, where $F$ is a common market factor and $Z_i$ is the firm-specific shock. Conditional on $F$, default probabilities become independent, enabling the conditional-PD formula $Q_i(T|F) = N\!\left(\dfrac{N^{-1}[Q_i(T)]-\sqrt{\rho}\,F}{\sqrt{1-\rho}}\right)$. Both real-world PDs (rating-agency data) and risk-neutral PDs (bond prices) feed into it. *Intuition: The copula is a universal translator — it takes each firm's own "local language" of default timing and re-expresses them in a shared "standard-normal language" so their correlations can be modelled cleanly.* | `[THE]` | Very High — the one-factor Gaussian copula formula and the "transforms times to default into normal variables" phrase are exam-grade. | "Gaussian copula," "one-factor model," "time to default," "copula correlation," "common factor" |
| P8 | **Credit VaR — Gaussian Copula & CreditMetrics (LO 30.g):** **Credit VaR** is the loss that will not be exceeded over horizon $T$ at confidence $X$%. Using the Gaussian copula with common correlation $\rho$ and marginal PD $Q(T)$, the worst-case default-rate percentile is $V(T,X)=N\!\left(\dfrac{N^{-1}[Q(T)]+\sqrt{\rho}\,N^{-1}(X)}{\sqrt{1-\rho}}\right)$ and **Credit VaR $= L \times (1-RR) \times V(T,X)$**. **CreditMetrics (JPM)** extends this by running Monte Carlo on credit-rating *transitions* (not just defaults) via a transition matrix, with joint rating changes linked by a Gaussian copula where the copula correlations equal **equity-return correlations**. *Intuition: Gaussian-copula Credit VaR answers "how bad can the default rate get?" in a closed form. CreditMetrics answers the same but also captures MtM losses from downgrades short of default — richer picture, higher compute cost.* | `[THE]` | Very High — the Credit VaR formula $L\times(1-RR)\times V(T,X)$ is a direct LO 30.g calculation. | "Credit VaR," "Vasicek formula," "$V(T,X)$," "CreditMetrics," "rating transition matrix," "equity return correlation" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|:---|:---|:---|
| P1 (PD from spreads) | A 2-year corporate bond yields **190 bp** over the risk-free rate; recovery rate is **35%**. | Average hazard rate = $0.0190/(1-0.35) =$ **2.92%** per year. The rate rises as spread widens or recovery falls. |
| P2 (Risk-neutral vs real-world) | You use **real-world** PDs to price a new credit-linked note. | You will **systematically underprice** the default risk — pricing requires **risk-neutral** PDs because market prices already embed the risk premium. |
| P3 (ISDA event of default) | Company B defaults owing Company A $50,000; B had posted only $30,000 collateral. | Company A is an **unsecured creditor for $20,000** (= 50,000 − 30,000). The collateral shield only protects the first $30k. |
| P4 (CVA new-trade impact) | A new trade is **negatively** correlated with the existing portfolio. | Both **CVA and DVA decrease** — the new trade offsets existing exposure, shrinking the expected default cost on both sides. |
| P4 (Wrong-way risk) | Counterparty PD rises with exposure (WWR present). | Standard CVA models that assume *independence* between PD and exposure will **underestimate** CVA — WWR calls for a correlation adjustment. |
| P5 (Netting) | Three trades with a single counterparty: +$12M, −$4M, −$3M. | Gross exposure (ignoring negatives) = $12M. Netted exposure = $5M. **Exposure reduction = $7M.** |
| P6 (Reduced-form vs structural) | A risk manager needs to model a **very high** default correlation between two firms in the same sector. | Use a **structural model** — reduced-form models cannot produce the needed correlation magnitude; accept the computational cost. |
| P8 (Credit VaR formula) | Loan portfolio $L=\$100M$, recovery $RR=40\%$, and $V(T,X)=5\%$. | **Credit VaR = $100M × (1−0.40) × 0.05 = $3M** — the 1-year loss not exceeded at confidence $X$. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- **Risk-neutral PD** → pricing derivatives; **Real-world PD** → scenario analysis (never swap them).
- Hazard rate formula $\lambda \approx s/(1-R)$ — spread and recovery both matter; ignoring $R$ is a classic error.
- **No-default value − CVA + DVA** = accounting-adjusted derivative value; signs must be tracked carefully.
- Credit VaR formula = $L \times (1-RR) \times V(T,X)$ — $(1-RR)$ is LGD, never confuse with $RR$ itself.
- **Structural models** allow high correlation (slow); **reduced-form models** are fast (low correlation ceiling).

**Noise (distractors):**
- "Real-world PDs are used for pricing credit derivatives" — wrong (risk-neutral are used for pricing).
- "Risk-neutral and real-world PDs are equal in practice" — wrong (risk-neutral is systematically higher because defaults are not independent).
- "CVA is the cost if the bank defaults" — wrong (that's DVA).
- "Wrong-way risk is negative correlation between PD and exposure" — wrong (that's right-way risk).
- "Reduced-form models allow high default correlations" — wrong (structural models do).
- "The Gaussian copula transforms recovery rates into normal variables" — wrong (it transforms **times to default**).
- "Credit VaR = $L \times RR \times V(T,X)$" — wrong (it uses $(1-RR)$, i.e., LGD).
- "CreditMetrics ignores downgrades" — wrong (it captures both downgrades and defaults via rating transition matrix).

**Tensions:**
- **[THE] vs [REG]:** The theoretical attractiveness of risk-neutral PDs for pricing (LO 30.c) vs the regulatory preference for conservative real-world PDs when modelling capital and stress losses. The two numbers can differ by a factor of 2-10× at investment grade.
- **[REG] vs [OPS]:** Regulatory capital assumes independence of defaults (reduced-form / historical data), but operational CVA desks must capture wrong-way risk and systemic co-movement (structural / copula models) — the two risk lenses produce materially different numbers for the same portfolio.

## 4. Directional Intuition

- **Credit spread $\uparrow \rightarrow$ Hazard rate $\uparrow \rightarrow$ PD $\uparrow$:** Direct linear relationship via $s/(1-R)$.
- **Recovery rate $\uparrow \rightarrow$ Hazard rate $\downarrow$ (for given spread):** Higher recovery means the same spread implies fewer defaults because each one hurts less.
- **Bank's own credit spread $\uparrow \rightarrow$ DVA $\uparrow \rightarrow$ Derivative asset value $\uparrow$ (the "DVA paradox"):** As the bank's credit worsens, the market expects it to default more often, releasing it from its obligations — which counter-intuitively inflates accounting profit.
- **Trade correlation with portfolio $\uparrow \rightarrow$ CVA & DVA $\uparrow$:** Correlated trades pile exposure onto the same counterparty at the same time.
- **Copula correlation $\rho \uparrow \rightarrow V(T,X) \uparrow \rightarrow$ Credit VaR $\uparrow$:** Higher co-movement fattens the joint-default tail.
- **Confidence level $X \uparrow \rightarrow V(T,X) \uparrow \rightarrow$ Credit VaR $\uparrow$:** Same mechanics as market VaR — pushing further into the tail demands more capital.
- **Reduced-form parameter choice $\rightarrow$ low correlation ceiling:** No matter how aggressively you calibrate a reduced-form model, two firms rarely default in the same short window.
- **Structural model asset correlation $\uparrow \rightarrow$ default correlation $\uparrow \uparrow$:** Because defaults happen when assets cross a threshold, correlated assets produce correlated crossings.

## 5. Ambiguity Traps (Anti-Decoder)

- **Unconditional vs Conditional PD:** *Unconditional* PD in year $n$ = probability default occurs in that year *as seen today*. *Conditional* PD = probability of default in year $n$ *given survival through year $n-1$* = unconditional PD ÷ survival probability. Exam will give you cumulative figures and ask you to compute either one.
- **The "Ratio" Trap (investment grade):** For investment-grade names, the ratio of bond-implied hazard rate to historical hazard rate is **very high** (e.g., 8×–10× at AAA). The ratio *declines* as ratings fall — counterintuitive.
- **Risk-Neutral ≠ Actuarial:** Risk-neutral probabilities are *not* predictions of what will happen; they are prices for bearing default risk. Don't argue "history disagrees with them" — that's the whole point.
- **CVA Cost vs DVA Benefit:** CVA is *always* a cost to the bank. DVA is *always* a benefit to the bank (because the bank defaulting means it escapes its obligations). Both change in opposite directions when credit spreads move.
- **No-default Value Formula Sign:** $V_{\text{credit-adjusted}} = V_{\text{no-default}} - \text{CVA} + \text{DVA}$. CVA subtracts; DVA adds (from the bank's perspective).
- **Netting vs Close-out Netting:** *Netting* aggregates MtMs for exposure measurement. *Close-out netting* is the legally enforceable termination of all contracts and single-payment settlement under ISDA on default. Often conflated.
- **Downgrade Trigger Failure Mode:** Triggers *lose effectiveness* precisely when you need them most — during a broad credit deterioration when many counterparties hit trigger levels simultaneously (AIG 2008).
- **Gaussian Copula — What Gets Normalized:** The copula transforms **times to default** $\tau_i$ into joint normals, not PDs, not recovery rates, not spreads. This is a favourite distractor.
- **One-Factor Copula Formula — Two Things to Know:**
    1. $x_i = \sqrt{\rho}\,F + \sqrt{1-\rho}\,Z_i$ (the factor decomposition).
    2. $Q_i(T|F) = N\!\left(\dfrac{N^{-1}[Q_i(T)]-\sqrt{\rho}\,F}{\sqrt{1-\rho}}\right)$ (conditional default probability).
- **CreditMetrics Uses Equity Return Correlation:** The copula correlation for rating transitions is set equal to *equity* return correlations between counterparties — not bond return correlation, not asset correlation.
- **Credit VaR Formula Components:** $L \times (1-RR) \times V(T,X)$ — memorize as "portfolio × LGD × default-rate percentile." Dropping the $(1-RR)$ is a classic error.
- **Merton Model Role:** Equity is a call option on firm assets with strike = debt face value. The model produces *relative rankings* of PD that hold up under both risk-neutral and real-world scenarios — useful because equity prices update faster than credit ratings.
- **Default Correlation ≠ Default Probability:** Rising correlation doesn't necessarily raise individual PDs; it concentrates the mass of joint defaults into "all or nothing" outcomes, fattening the tail without shifting the mean.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
