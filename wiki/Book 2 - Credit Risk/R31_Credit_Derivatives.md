# The Boole Scaffold: Reading 31 — Credit Derivatives

**Exam Priority:** 🔴 High (3–4 questions)

*Source Material: FRM 2026 Part II Book 2 · Schweser Study Session 5*
*Learning Objectives Covered: 31.a, 31.b, 31.c, 31.d, 31.e, 31.f, 31.g, 31.h*
*Related Readings: [R30 — Credit Risk Models](R30_Credit_Risk.md), R32 — Spread Risk and Credit Migrations (pending)*

---

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|:---|:---|:---:|:---|:---|
| P1 | **CDS Structure & Credit Derivative Definition (LO 31.a):** A credit derivative transfers credit risk from a protection buyer to a protection seller without transferring ownership of the underlying asset. In a credit default swap (CDS), the protection buyer pays a periodic CDS spread (in arrears) until maturity or default, whichever comes first. Upon default, the protection seller pays (1 − RR) × Notional, and the protection buyer delivers the cheapest-to-deliver (CTD) bond. No-arbitrage condition: CDS-bond basis = CDS spread − bond yield spread ≈ 0. CDS contracts are standardised under ISDA with common maturities (1, 3, 7, 10 years) and quarterly settlement on 20 Mar/Jun/Sep/Dec. *Intuition: Buying a CDS is like buying fire insurance on someone else's house — you pay premiums and collect if it burns down, without owning it.* | `[ECO]` | High — CDS structure mechanics appear on every sitting. | "protection buyer," "protection seller," "CDS spread," "cheapest-to-deliver," "reference obligation," "CDS-bond basis" |
| P2 | **Total Return Swap & CDO Structure (LO 31.a):** A total return swap (TRS) has one party paying the total return (coupon + price change) on a reference asset and receiving a floating rate (MRR + spread). Unlike a CDS, a TRS hedges both credit risk and market risk (price risk). A collateralized debt obligation (CDO) pools risky debt and issues claims divided into tranches via a distribution waterfall: the equity tranche absorbs first losses (highest spread), the mezzanine tranche absorbs intermediate losses, and the senior tranche absorbs last losses (lowest spread, highest rating). *Intuition: A CDO is like a building where equity investors occupy the ground floor — they feel any flood first, but earn the highest rent for that risk.* | `[ECO]` | Medium — TRS and CDO structure tested conceptually; structure questions, not calculations. | "total return swap," "distribution waterfall," "equity tranche," "mezzanine," "senior tranche," "total return" |
| P3 | **CDS Valuation: Hazard Rate and Spread Calculation (LO 31.b):** CDS spread s is set so that PV(expected payments) = PV(expected payoff). With constant hazard rate λ: PS(t) = e^(−λ × t); PD in year t = PS(t−1) − PS(t). The protection buyer pays s each period only if no default occurred, plus an accrual payment of s/2 upon default (since default assumed mid-period). The protection seller pays (1 − RR) upon default. Example (λ = 3%, RR = 35%, r = 4%, 3-year annual settlement): PS1 = 0.9705, PS2 = 0.9418, PS3 = 0.9139; PV(payments) = 2.6529s; PV(payoff) = 0.0528; breakeven s = 0.0528 / 2.6529 ≈ 1.99%. *Intuition: The CDS spread is the insurance premium that makes the insurer indifferent at inception — expected premiums exactly equal expected claims.* | `[THE]` | Very High — CDS spread calculation is the single most-tested item in this reading. | "hazard rate," "probability of survival," "PV of expected payments," "PV of expected payoff," "CDS spread calculation," "accrual payment" |
| P4 | **Risk-Neutral vs Real-World PD in CDS (LO 31.c):** CDS valuation uses risk-neutral (Q-measure) default probabilities, not real-world (P-measure). The risk-neutral hazard rate is implied iteratively from the market CDS spread. Approximate relationship: λ_Q ≈ s / (1 − RR). Critically, if market-implied (risk-neutral) PD is used, the assumed RR does not affect the implied CDS spread (the model self-adjusts). However, a higher assumed RR implies a higher risk-neutral PD for the same market spread: PD_Q ∝ 1 / (1 − RR). *Intuition: Risk-neutral PD is what the market prices in — it is higher than the actuarial PD because it includes a credit risk premium, just as risk-neutral probabilities in option pricing overweight bad outcomes.* | `[THE]` | High — Q vs P PD distinction recurs across Readings 30, 31, and 38. | "risk-neutral probability of default," "real-world PD," "hazard rate implied by market," "recovery rate assumption," "Q-measure" |
| P5 | **Credit Indices and Fixed Coupons (LO 31.d):** Credit indices (CDX NA IG: 125 North American IG companies; iTraxx Europe: 125 European IG companies) provide equally-weighted exposure. Upon one default: the contract continues with 124 entities, the protection seller pays (1 − RR) on that entity's notional, and future annual payments decline by 1/125. Standardised contracts use a fixed coupon (e.g., 100 bps) instead of the actual CDS spread. Up-front settlement: Up-front payment = −(coupon − spread) × Duration × Notional. If coupon > spread, protection seller pays the buyer upfront. Example: coupon = 100 bps, spread = 65 bps, duration = 4.125, NP = $100,000 → seller pays buyer (100 − 65) / 10000 × 4.125 × 100,000 = $1,443.75. *Intuition: Fixed coupons turn bespoke swaps into standardised bonds — everyone pays the same coupon, and the opening price adjusts to reflect whether the coupon is above or below the market spread.* | `[OPS]` | Medium — index mechanics and fixed coupon calculations are directly tested. | "CDX NA IG," "iTraxx Europe," "fixed coupon," "up-front premium," "125 investment-grade companies," "duration of CDS" |
| P6 | **CDS Forwards and CDS Options (LO 31.e):** A CDS forward locks a party into a specific CDS at a fixed spread starting at a future date. If the reference entity defaults before the forward's start date, the forward ceases to exist. CDS forwards entered at market rates require no up-front premium. A CDS option gives the holder the right (not obligation) to enter a CDS at a strike spread, in exchange for an up-front option premium. Because the option holder can walk away, CDS options always require a premium while CDS forwards do not. *Intuition: A CDS forward is an obligation — a handshake sealing a future deal; a CDS option is a ticket — you pay now for the right to decide later.* | `[ECO]` | Low — tested at definition level; distinguish forward vs option mechanics. | "CDS forward," "CDS option," "strike spread," "option premium," "forward ceases upon default," "no up-front for forward" |
| P7 | **Synthetic CDO Valuation (LO 31.f):** A synthetic CDO replicates cash CDO credit risk via CDS contracts (no bond purchases; unfunded). Valuation uses two approaches. (1) Spread payments approach: set PV(inflows from tranche spread) = PV(outflows from credit losses). Breakeven: s = C / (A + B), where A = PV-weighted surviving notional, B = PV-weighted accrual on loss amount, C = PV of expected credit losses. For non-par coupons s*: up-front payment NP = (s* − s) × (A + B). (2) Gaussian copula approach: model correlated time-to-default using copula correlation ρ; compute conditional PD Q(t|F) = N([N⁻¹(Q(t)) − √ρ · F] / √(1−ρ)); apply binomial distribution to estimate expected tranche losses. *Intuition: A synthetic CDO is a credit risk factory assembled entirely from derivatives — no real bonds change hands, only the cashflows from insuring them.* | `[THE]` | High — synthetic CDO valuation mechanics and tranche structure are frequently tested. | "synthetic CDO," "spread payments approach," "Gaussian copula," "tranche expected loss," "conditional PD," "breakeven spread" |
| P8 | **Implied Correlation: Compound vs Base Correlation (LO 31.g):** Two measures of implied correlation are derived from CDO tranche market spreads (analogous to implied volatility from option prices). Compound (tranche) correlation: the single ρ value per tranche q such that the model spread equals the market spread (found iteratively). Problem: compound correlations exhibit a correlation smile — equity and senior tranches imply high ρ, mezzanine implies low ρ — making the measure internally inconsistent across tranches. Base correlation: derived iteratively by pricing each synthetic tranche as [0%, Kh]; produces a monotonically increasing correlation skew from junior to senior and is the market standard. *Intuition: Base correlation is like using a consistent implied volatility surface across all strikes — it produces a coherent picture rather than an ad-hoc number per tranche.* | `[THE]` | Medium — compound vs base distinction is directly exam-testable as a definition question. | "compound correlation," "base correlation," "correlation smile," "correlation skew," "iterative search," "tranche correlation" |
| P9 | **Alternative Approaches to Default Correlation (LO 31.h):** Three main alternatives to the Gaussian copula for estimating default correlation: (1) Historical estimation — infer joint default frequency from observed defaults; limited by sparse data and regime changes. (2) Structural models — correlate the asset values of firms (Merton framework); require firm-specific asset return correlation assumptions. (3) Implied correlation — back out from market tranche prices as in P8; model-dependent and circular. Each approach has distinct data requirements and model limitations; no single method dominates in practice. *Intuition: Estimating joint default probability is like forecasting simultaneous earthquakes — history is too sparse, models require assumptions, and markets price fear differently from actuaries.* | `[THE]` | Low — tested conceptually; rarely requires numerical work; compare and contrast questions only. | "historical default correlation," "structural model," "implied correlation," "joint default," "alternative approaches" |

---

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|:---|:---|:---|
| P3 (CDS valuation) | λ = 2%, 5-year CDS. What is the probability of default in Year 2 (annual settlement)? | PS1 = e^(−0.02×1) = 0.9802; PS2 = e^(−0.02×2) = 0.9608; PD Year 2 = 0.9802 − 0.9608 = 0.0194 = **1.94%**. |
| P3 (CDS valuation) | Same 3-year CDS (λ=3%, RR=35%, r=4%) but actual market spread = 2.75%, not 1.99%. What adjustment is required? | Model hazard rate of 3% is too low. Iterate λ upward (trial-and-error or Solver) until model spread matches 2.75%; solution is λ ≈ **4.15%**. |
| P4 (risk-neutral PD) | Market CDS spread = 2%. Calculate risk-neutral PD under RR = 35% vs RR = 60%. | RR=35%: PD_Q ≈ 2%/(1−0.35) = **3.08%**. RR=60%: PD_Q ≈ 2%/(1−0.60) = **5.00%**. Higher RR → higher risk-neutral PD for the same market spread. |
| P5 (credit indices) | CDX NA IG (125 companies), fixed coupon = 100 bps, market spread = 65 bps, duration = 4.125, notional = $100,000/company. One company defaults (RR=40%). Describe the outcome. | Protection seller pays (1−0.40)×$100,000 = $60,000 for the defaulted entity. Contract continues with 124 entities. Up-front: seller pays buyer (100−65)/10,000 × 4.125 × $100,000 = **$1,443.75** per company at inception. |
| P6 (CDS forwards vs options) | Which requires an up-front premium: a CDS forward entered at market rates, or a CDS option? | CDS forward at market rates: **no premium**. CDS option: **always requires a premium** (right to walk away has option value). |
| P7 (synthetic CDO) | $100M synthetic CDO: equity 0–5% ($5M), mezzanine 5–25% ($20M), senior 25–100% ($75M). Credit losses total $7M. Which tranches are affected and by how much? | Equity tranche: **fully wiped out** (absorbs first $5M). Mezzanine: absorbs remaining **$2M** loss (principal reduced to $18M). Senior: **unaffected**. |
| P8 (implied correlation) | A CDO shows compound correlations: equity = 28%, mezzanine = 12%, senior = 25%. Is this a smile or a skew? Why is it problematic? | This is a **correlation smile** (U-shape: equity high, mezzanine low, senior high). It is internally inconsistent — different tranches of the same CDO imply different models. Base correlation resolves this. |

---

## 3. Dependency & Noise Map

**Signal (these matter):**
- **Survival vs Default probabilities** — PS(t) = e^(−λt) drives all CDS valuation; PD(t) = PS(t−1) − PS(t). Expected payments use survival probs; expected payoffs use default probs.
- **PV(payments) = PV(payoff)** — the breakeven condition that defines the CDS spread at inception. Any deviation → MtM gain/loss.
- **Risk-neutral PD ∝ 1 / (1 − RR)** — higher assumed recovery inflates implied PD proportionally; this does not change the model-implied CDS spread if using market-implied PD.
- **Compound correlation → smile; Base correlation → skew** — base correlation is the market convention because it is internally consistent across all tranches.
- **Synthetic CDO breakeven: s = C / (A + B)** — equity tranches face higher expected losses (C), hence their spreads are highest; senior tranches have very low C and hence very low spreads.

**Noise (distractors):**
- "A TRS is a pure credit derivative" — wrong (TRS hedges credit risk AND market/interest rate risk; a CDS hedges credit only).
- "CDS premiums are paid at the start of each settlement period" — wrong (CDS premiums paid in arrears; an accrual payment covers the stub period on default).
- "Binary CDS and vanilla CDS have the same spread" — wrong (binary spread = vanilla spread / (1 − RR) because RR = 0% in binary payoff, so protection is more expensive).
- "When one entity in CDX NA IG defaults, the notional per remaining entity increases" — wrong (notional per entity stays the same; total annual payment decreases by 1/125th).
- "CDS forwards require an up-front premium" — wrong (forwards at market rates cost nothing upfront; only options require a premium).
- "Compound and base correlation give the same answer for the same tranche" — wrong only at the aggregate level; they are calibrated differently (compound per-tranche, base to [0,K] buckets).
- "Real-world PD equals risk-neutral PD for CDS pricing" — wrong (risk-neutral PD > real-world PD; includes a risk premium embedded in market credit spreads).

**Tensions:**
- **[THE] vs [OPS]:** Theoretical CDS pricing assumes continuous time, constant hazard rates, and mid-year default timing; operational reality uses standardised quarterly settlement, fixed coupons, and actual ISDA documentation — requiring up-front adjustments and day-count conventions absent from the model.
- **[ECO] vs [REG]:** Economically, synthetic CDOs efficiently redistribute credit risk to investors who want exposure; post-2008 Basel III/IV regulations impose punitive capital charges on re-securitisation exposures, severely limiting synthetic CDO activity at regulated banks.

---

## 4. Directional Intuition

- **λ ↑ → PS(t) ↓ → PD(t) ↑ → CDS spread ↑:** Higher default intensity means more expected defaults; protection costs more.
- **RR ↑ → payoff per default ↓ → CDS spread ↓ (vanilla):** Less is paid out on default, so the protection premium falls.
- **RR ↑ → risk-neutral PD ↑ (holding spread constant):** PD_Q ∝ 1/(1−RR); a higher recovery assumption requires a higher implied PD to reproduce the same market spread.
- **CDS spread widens post-inception → MtM gain for protection buyer, MtM loss for seller:** Spread ↑ → protection more valuable → buyer's position worth more.
- **ρ ↑ (copula correlation) → loss distribution bimodal → senior tranche risk ↑, mezzanine risk may ↓:** At high correlation, losses tend to be all-or-nothing; the senior tranche faces greater risk of being reached.
- **Binary CDS spread > vanilla CDS spread (all else equal):** Binary payoff = full notional (RR = 0%), so protection is more expensive than a vanilla CDS with positive RR.
- **Fixed coupon > market spread → protection seller pays buyer upfront:** Buyer is overpaying on the coupon; seller compensates at inception.

---

## 5. Ambiguity Traps (Anti-Decoder)

- **CDS ≠ TRS:** CDS hedges credit risk only; TRS hedges credit risk + market price risk. Exam trap: calling TRS a "pure credit derivative."
- **Premiums in arrears:** CDS premiums are paid at the END of the settlement period, not the start. A stub accrual payment arises upon default.
- **Binary CDS spread mnemonic:** Binary spread = Vanilla spread / (1 − RR). Binary has NO recovery → spread must be higher to compensate.
- **CDX default mechanics:** One default → 124 entities remain; notional per entity UNCHANGED; total annual payment FALLS by 1/125; protection seller pays (1−RR) for the defaulted entity.
- **Forward ≠ Option — premium rule:** CDS forward at market rates = ZERO up-front. CDS option = ALWAYS positive premium. "Who pays at initiation?" is the exam tell.
- **Risk-neutral PD > real-world PD:** Market credit spreads embed a risk premium above the actuarial default rate. CDS valuation always uses Q-measure PDs.
- **Smile vs Skew — direction:** Compound correlation → U-shaped smile (equity high, mezzanine low, senior high). Base correlation → monotonically increasing skew (junior low, senior high). Base is the market standard.
- **λ constant ≠ PD constant:** The hazard rate λ is constant by assumption; the annual PD(t) declines over time because fewer entities survive to later periods to default.
- **Synthetic CDO ≠ cash CDO — funding:** Synthetic uses CDS (unfunded); cash holds actual bonds (funded). Synthetic CDOs only require cash deposits if default losses materialise.
- **CDS-bond basis ≠ always zero:** No-arbitrage implies basis ≈ 0, but in practice: positive basis (CDS spread > bond spread) arises from CTD optionality, counterparty risk, and repo costs.
- **Mnemonic for CDS valuation:** "Payments on survival, payoffs on default" — PV(payments) sums over survival probabilities; PV(payoff) sums over default probabilities.
- **ρ → 0 vs ρ → 1 in CDO:** ρ = 0: independent defaults → portfolio loss ≈ expected loss, equity takes most risk. ρ = 1: all default together or none do → senior tranche becomes risky, equity tranche may be safer at extremes.
- **Up-front premium sign:** Up-front = −(coupon − spread) × Duration × Notional. If coupon > spread (protection buyer overpays), protection seller compensates buyer → seller pays positive amount.
- **Recovery rate in binary CDS:** Binary CDS effectively assumes RR = 0%. Its spread = vanilla spread / (1−RR). A vanilla CDS with RR = 0% would have the same spread as binary.

---

**Cross-Domain Linkage:** [Boundary Events](../_boundary_events.md)
