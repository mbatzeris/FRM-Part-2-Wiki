# FRM Part 2 — Practice Drill Bank

> **Format:** Each question tagged with `[Domain]`, `[Distractor Archetype]`, `[Constraint Tested]`.  
> Use the Strict Output Template from `00_SYSTEM_PROMPT.md` to answer before checking solutions.

---

## Domain 1: Market Risk (Questions 1–10)

### Q1 [Market Risk] [REG-ECO FLIP] [REG > ECO]
**Vignette:** A trading desk runs a Monte Carlo VaR model producing 3 exceptions over 250 days (99% confidence). The desk head argues the model is conservative and requests reducing the multiplier from 3.0 to 2.5 to free up capital for new strategies. The CRO notes the bank is in the Basel Green Zone.

**The desk head's request is most likely:**
- A) Appropriate — the model is demonstrably conservative with only 3 exceptions
- B) Inappropriate — the multiplier is a regulatory floor, not a bank-discretionary input
- C) Appropriate — Green Zone status confirms the model overstates risk
- D) Inappropriate — 3 exceptions suggest the model may still understate tail risk

**Answer:** B  
**Why:** `[REG]` dominates. The Basel multiplier floor of 3.0 is not negotiable downward by the bank. Green Zone means the *supervisor* does not add a penalty — it does not grant the bank permission to reduce below 3.0. Option A is `[TRUE-IRRELEVANT]` — model conservatism is real but doesn't change the regulatory constraint. Option C is `[REG-ECO FLIP]` — conflating supervisory assessment with capital optimization.

---

### Q2 [Market Risk] [INVERSE INTUITION] [ECO]
**Vignette:** A portfolio manager holds a portfolio of emerging market bonds. During a stress period, the manager observes that the correlation between asset classes in the portfolio increases from 0.3 to 0.85. The portfolio's Historical Simulation VaR (using 500 days of data, equally weighted) shows only a modest increase.

**The most likely explanation is:**
- A) The portfolio has natural hedges that offset the correlation increase
- B) Historical Simulation is slow to reflect regime changes because it equally weights old, calm-period data
- C) The correlation increase is within the model's assumptions
- D) Emerging market bonds have low sensitivity to correlation changes

**Answer:** B  
**Why:** Historical Simulation with equal weighting is slow to react — the 500-day window still contains ~400 days of low-correlation data, diluting the recent stress. This is the "ghosting" effect. Option A is possible but the vignette gives no evidence of hedges — it's `[TRUE-IRRELEVANT]`. Option D is factually wrong.

---

### Q3 [Market Risk] [TRUE-IRRELEVANT] [REG]
**Vignette:** Under FRTB, a bank's trading desk fails the P&L Attribution Test. The desk currently uses the Internal Models Approach (IMA). The desk's ES model has strong backtesting results (1 exception in 250 days).

**The most likely regulatory consequence is:**
- A) The desk retains IMA status due to strong backtesting performance
- B) The desk must fall back to the Standardized Approach (SA)
- C) The supervisor increases the ES multiplier as a penalty
- D) The desk is placed on a 12-month remediation plan before any action

**Answer:** B  
**Why:** FRTB requires desks to pass **both** backtesting **and** P&L Attribution to retain IMA. Failing either triggers SA fallback. The strong backtesting result (Option A) is `[TRUE-IRRELEVANT]` — it's a real fact that doesn't save the desk. The P&L Attribution test is a separate, binding gate.

---

### Q4 [Market Risk] [ABSOLUTE] [ECO]
**Vignette:** A risk analyst states: "Expected Shortfall always provides a more accurate risk estimate than VaR because it is a coherent risk measure."

**This statement is:**
- A) Correct — coherence guarantees accuracy
- B) Incorrect — coherence addresses mathematical properties (subadditivity), not estimation accuracy
- C) Correct — ES captures tail risk that VaR ignores
- D) Incorrect — VaR is more accurate for normally distributed returns

**Answer:** B  
**Why:** The word "always" is the `[ABSOLUTE]` flag. Coherence (subadditivity, monotonicity, etc.) is about the *mathematical behavior* of the measure, not its empirical accuracy. ES can have **higher estimation error** than VaR because it averages over fewer tail observations. Option C is partially true but doesn't address the "always more accurate" claim.

---

### Q5 [Market Risk] [REG-ECO FLIP] [REG]
**Vignette:** A bank calculates its ES for a trading portfolio at the 97.5% confidence level using the FRTB IMA. The risk manager also calculates VaR at 99% for internal capital allocation.

**Under FRTB, the capital charge is based on:**
- A) The higher of ES(97.5%) and VaR(99%)
- B) ES(97.5%) only — VaR is no longer used for regulatory capital under FRTB
- C) VaR(99%) with an ES adjustment factor
- D) ES(97.5%) for market risk, VaR(99%) for default risk

**Answer:** B  
**Why:** FRTB replaced VaR with ES for market risk capital. The internal VaR(99%) is the bank's choice for economic capital — irrelevant to regulatory capital. `[REG-ECO FLIP]`: candidates who remember "VaR at 99%" from Basel 2.5 select C or D.

---

### Q6–Q10: Twin-Question Format

### Q6–Q7 [Market Risk] [REG-ECO FLIP] — Twin Pair
**Vignette:** A bank's 10-day VaR model produces 7 exceptions over 250 trading days at the 99% confidence level. The CRO is evaluating next steps.

**Q6 (REG):** From a **regulatory** perspective, the supervisor will most likely:
- A) Take no action — 7 exceptions is within tolerance
- B) Increase the VaR multiplier by a penalty add-on
- C) Require immediate transition to the Standardized Approach
- D) Request the bank conduct a fundamental model review within 30 days

**Q6 Answer:** B — Yellow Zone (5–9 exceptions) triggers a progressive multiplier add-on (+0.40 to +0.65 for 7 exceptions). Not severe enough for SA fallback (Red Zone ≥ 10).

**Q7 (ECO):** From an **internal risk management** perspective, the CRO should most likely:
- A) Accept the model performance and focus on the capital impact
- B) Investigate whether the exceptions are clustered or driven by a specific risk factor
- C) Immediately increase position limits across all desks
- D) Replace Historical Simulation with Monte Carlo

**Q7 Answer:** B — Internally, the *pattern* of exceptions matters more than the count. Clustered exceptions suggest regime change or model weakness in a specific factor. Option C is disproportionate. Option D is not justified without diagnosis.

---

### Q8–Q9 [Market Risk] [INVERSE INTUITION] — Twin Pair
**Vignette:** A portfolio contains long positions in both equity index futures and deep out-of-the-money put options on the same index. Implied volatility increases sharply.

**Q8 (Quantitative):** The portfolio's overall VaR will most likely:
- A) Increase — higher volatility means higher risk
- B) Decrease — the put options gain value, offsetting equity losses
- C) Remain unchanged — the hedge is delta-neutral
- D) Decrease initially, then increase as gamma effects dominate

**Q8 Answer:** B — The puts are a tail hedge. Vol↑ → put values↑ significantly (high vega for OTM puts), partially offsetting equity exposure. The portfolio VaR decreases because the hedge kicks in during stress.

**Q9 (Qualitative):** The risk manager should be most concerned that:
- A) The hedge may create a false sense of security if not dynamically managed
- B) The puts will expire worthless in a low-volatility environment
- C) Implied volatility may not accurately predict realized volatility
- D) The put position creates unlimited downside exposure

**Q9 Answer:** A — `[OPS]` concern. Static hedges decay (theta) and their effectiveness depends on continuous recalibration. Option D is factually wrong (long puts have limited loss = premium paid). Option B is true but answers a different question (cost, not risk management concern).

---

### Q10 [Market Risk] [TRUE-IRRELEVANT] [REG > ECO]
**Vignette:** A bank uses FRTB Sensitivity-Based Method (SbM) under the Standardized Approach. The risk analyst computes Delta, Vega, and Curvature risk charges. A junior analyst asks whether the bank should also compute DRC.

**The correct response is:**
- A) No — DRC only applies under IMA
- B) Yes — DRC is computed separately under both IMA and SA
- C) No — DRC is embedded within the Curvature risk charge
- D) Yes — but only for securitization positions

**Answer:** B — Default Risk Charge applies under **both** approaches. It captures jump-to-default risk not covered by the sensitivity-based charges. Option A is incorrect. Option C confuses curvature (non-linear market risk) with default risk.

---

## Domain 2: Credit Risk (Questions 11–20)

### Q11 [Credit Risk] [INVERSE INTUITION] [ECO]
**Vignette:** A CDO portfolio manager observes that default correlation among the underlying assets has increased from 0.15 to 0.45.

**The equity tranche holder's risk has most likely:**
- A) Increased — higher correlation means more defaults
- B) Decreased — higher correlation means defaults are more "all-or-nothing," improving the equity tranche's expected survival
- C) Remained unchanged — correlation affects mezzanine tranches, not equity
- D) Increased — the equity tranche absorbs first losses regardless of correlation

**Answer:** B — Counter-intuitive. High correlation → binary outcome (all survive or all default). The "all survive" scenario becomes more likely, benefiting equity. Equity tranche is **long correlation**. Option A applies the wrong intuition. Option D is `[TRUE-IRRELEVANT]` — first-loss status is true but doesn't address the *change* in risk.

---

### Q12 [Credit Risk] [REG-ECO FLIP] [REG]
**Vignette:** A bank calculates CVA for a large OTC derivative exposure. The bank's own credit spread has widened by 150bps. The CFO notes this produces a DVA gain of $45M.

**For regulatory capital purposes, this DVA gain:**
- A) Can be included in CET1 as realized P&L
- B) Must be excluded from CET1 — Basel III requires full deduction of DVA gains
- C) Is included at 50% of face value as a prudential filter
- D) Can be included only if the bank has a CVA desk that actively hedges DVA

**Answer:** B — Basel III mandates full exclusion of DVA from CET1. The $45M accounting profit does **not** strengthen the bank's regulatory capital position. The `[REG-ECO FLIP]`: under IFRS 13, the gain is real; under Basel, it's stripped out.

---

### Q13 [Credit Risk] [TRUE-IRRELEVANT] [ECO]
**Vignette:** A bank enters an interest rate swap with a BBB-rated counterparty. The swap has a 5-year maturity, is uncollateralized, and the bank is the fixed-rate receiver. Current MTM is +$12M for the bank. The risk analyst provides the counterparty's CDS spread (180bps), recovery rate (40%), and a correlation matrix of interest rates and credit spreads.

**To estimate CVA, the analyst needs the correlation matrix primarily to assess:**
- A) The diversification benefit of the bank's overall derivative portfolio
- B) The presence of wrong-way risk — whether the exposure increases when counterparty creditworthiness declines
- C) The expected future positive exposure under risk-neutral pricing
- D) The appropriate discount rate for future cash flows

**Answer:** B — The correlation between the exposure driver (interest rates) and the counterparty's credit spread determines whether WWR exists. If rates move in a direction that increases the bank's MTM *and* the counterparty's PD rises simultaneously, CVA is understated. The correlation matrix is the tool for detecting this. Options A and D are `[TRUE-IRRELEVANT]` — valid concepts but not what the correlation matrix diagnoses here.

---

### Q14 [Credit Risk] [ABSOLUTE] [ECO]
**Vignette:** A credit analyst states: "Netting agreements always reduce counterparty credit exposure."

**This statement is:**
- A) Correct — netting legally offsets positive and negative MTM positions
- B) Incorrect — netting reduces exposure only when the bank has both positive and negative MTM positions with the same counterparty
- C) Correct — ISDA Master Agreements enforce bilateral netting in all jurisdictions
- D) Incorrect — netting increases exposure due to legal uncertainty

**Answer:** B — `[ABSOLUTE]` flag on "always." If all positions with a counterparty are in-the-money (all positive MTM), netting provides **zero** benefit — the net is the same as the gross. Netting only helps when positive and negative values offset. Option C is wrong — enforceability varies by jurisdiction.

---

### Q15 [Credit Risk] [REG-ECO FLIP] [REG > ECO]
**Vignette:** Under Basel IRB, a bank estimates PD = 8% for a corporate obligor. The Basel regulatory asset correlation formula assigns ρ = 0.13 for this PD level. The bank's internal model estimates ρ = 0.25 based on the obligor's industry concentration.

**For regulatory capital, the bank must use:**
- A) ρ = 0.25 — the bank's internal estimate is more risk-sensitive
- B) ρ = 0.13 — Basel IRB prescribes the asset correlation; banks cannot override
- C) The average of both: ρ = 0.19
- D) ρ = 0.25 for economic capital, ρ = 0.13 for regulatory capital — and report both

**Answer:** B — For regulatory capital computation, Basel IRB **prescribes** the correlation formula. Banks estimate PD, LGD, EAD, and maturity — not ρ. Option D correctly describes reality (banks do use two numbers) but the question asks what the bank "must use" for regulatory capital, which is the prescribed formula.

---

### Q16–Q20: Abbreviated Format

### Q16 [Credit Risk] [INVERSE INTUITION]
A bank has wrong-way risk on an interest rate swap with a sovereign counterparty. Interest rates rise sharply while the sovereign's fiscal position deteriorates. The bank's exposure most likely **increases** because the MTM moves in its favor precisely when the counterparty's PD rises. **Trap:** candidates think "rising rates hurt the bank" — but the bank is the *fixed receiver*, so rates↑ = MTM↑ for the bank.

### Q17 [Credit Risk] [TRUE-IRRELEVANT]
The Merton model derives PD from equity price and volatility. **Trap question:** "What is the main limitation?" Option A says "It assumes normally distributed asset returns" (TRUE — but this applies to most models). The correct answer is "It assumes the firm has a single zero-coupon debt instrument," which is structurally unrealistic.

### Q18 [Credit Risk] [REG-ECO FLIP]
SA-CCR vs CEM: SA-CCR allows a **PFE multiplier < 1** when the portfolio has negative MTM (risk-reducing). CEM did not. If the question asks "Under SA-CCR, what happens when portfolio MTM is deeply negative?" → PFE is reduced. Under CEM → no reduction.

### Q19 [Credit Risk] [INVERSE INTUITION]
Credit VaR **increases** with asset correlation because the tail of the loss distribution becomes fatter (more systematic risk). But Basel IRB sets correlation **inversely** to PD — higher PD → lower ρ. This means very risky obligors get *less* correlation amplification. **Trap:** thinking high-PD obligors generate the highest Credit VaR. They contribute high EL, but their *unexpected* loss increment may be lower per unit due to lower ρ.

### Q20 [Credit Risk] [REG]
CCP default waterfall: (1) Defaulting member's initial margin → (2) Defaulting member's default fund contribution → (3) CCP's skin-in-the-game → (4) Non-defaulting members' default fund contributions → (5) Further assessments. **Trap:** candidates put CCP's capital before the defaulter's default fund contribution, or confuse the order of steps 3 and 4.

---

## Domain 3: Operational Risk (Questions 21–25)

### Q21 [OpRisk] [REG-ECO FLIP] [OPS]
**Vignette:** The Risk Management team (2nd Line) identifies that a trading desk has breached its VaR limit. The head of risk immediately instructs the desk to unwind the position.

**This action is most likely:**
- A) Appropriate — the 2nd Line is responsible for enforcing risk limits
- B) Inappropriate — the 2nd Line should notify and recommend; the 1st Line (business) executes trades
- C) Appropriate — limit breaches require immediate remediation regardless of governance structure
- D) Inappropriate — only the 3rd Line (Audit) can mandate position changes

**Answer:** B — 2nd Line monitors, challenges, and advises. **Executing trades** crosses into 1st Line territory and violates segregation of duties. The distinction is Influence (appropriate) vs Execution (inappropriate). Option A is the most common trap — "enforcing" sounds right but means different things at each line.

---

### Q22 [OpRisk] [TRUE-IRRELEVANT] [OPS]
A bank faces **high-frequency, low-severity** transaction processing errors. The correct strategy is **Treat** (improve controls), not **Transfer** (insurance). Insurance is for low-frequency/high-severity events where premiums are economically sensible. Frequent small losses eat premiums and make insurance cost-prohibitive.

### Q23 [OpRisk] [ABSOLUTE]
"KRIs are always leading indicators of operational risk." **Incorrect.** KRIs can be leading (staff turnover↑, suggesting future errors), lagging (number of incidents last quarter), or current (system downtime today). The word "always" is the trap.

### Q24 [OpRisk] [REG]
Under SMA, the Internal Loss Multiplier (ILM) scales BIC using historical loss data. **National discretion** allows supervisors to set ILM = 1 for all banks. This means in some jurisdictions, historical losses don't affect the Op Risk capital charge at all. **Trap:** assuming ILM always > 1 for banks with high losses.

### Q25 [OpRisk] [REG-ECO FLIP]
SR 11-7 requires model validation to be **independent** of model development. If the same team that builds a model also validates it, this violates the standard. **Trap:** "The team has deep expertise in the model" — expertise is `[TRUE-IRRELEVANT]` when independence is the binding constraint.

### Q26 [OpRisk] [TRUE-IRRELEVANT] [REG]
Under SMA, the Business Indicator Component (BIC) is calculated using a tiered structure. A bank with BI = €5bn falls in the second tier (€1bn < BI ≤ €30bn). The BIC calculation uses 0.12 × €1bn + 0.15 × (BI - €1bn). **Trap:** Candidates mistakenly apply the 0.15 rate to the entire BI, not just the excess over €1bn. The tiered structure is the binding constraint.

### Q27 [OpRisk] [INVERSE INTUITION] [OPS]
A bank has high-frequency, low-severity transaction processing errors (average loss $500 per incident, 200 incidents/month). The correct strategy is **Treat** (improve controls), not Transfer (insurance). Insurance is for low-frequency/high-severity events. **Trap:** Candidates think "we should insure against all losses" — but frequent small losses make insurance premiums uneconomical. The cost of insurance exceeds the expected loss for high-frequency events.

### Q28 [OpRisk] [REG-ECO FLIP] [REG]
The Internal Loss Multiplier (ILM) under SMA scales the BIC based on the bank's loss experience: ILM = log(1 + min(α × Loss_10y, 15)) / log(2). National discretion allows supervisors to set ILM = 1 for all banks. If a jurisdiction uses this discretion, historical losses have **zero impact** on the Op Risk capital charge. **Trap:** Assuming ILM always > 1 for banks with high losses — national discretion overrides the formula.

### Q29 [OpRisk] [ABSOLUTE] [ECO]
"Scenario analysis always produces more reliable loss estimates than historical loss data." **Incorrect.** Scenario analysis is forward-looking and captures tail events not in historical data, but it is subjective and depends on expert judgment. Historical data is objective but backward-looking. Neither is "always" more reliable — the exam rewards nuance over absolutes.

### Q30 [OpRisk] [REG-ECO FLIP] [OPS]
A bank's risk appetite statement sets a maximum acceptable operational loss of €10M per incident. A cyberattack causes €8M in losses. The CRO approves the incident response without escalation because it's within appetite. **This is inappropriate** — operational risk appetite applies to the **aggregate** risk profile, not individual incidents. Even if €8M < €10M, the pattern or frequency of incidents may exceed aggregate tolerance. **Trap:** Confusing per-incident threshold with aggregate risk profile.

---

## Domain 4: Liquidity Risk (Questions 26–30)

### Q26 [Liquidity] [TRUE-IRRELEVANT] [REG]
A corporate bond rated A+ with "proven liquidity during the 2008 crisis" is classified as HQLA Level **2B** (not 2A). Level 2A requires **AA- or higher**. The narrative about crisis performance is noise — the rating rule is the signal.

### Q27 [Liquidity] [INVERSE INTUITION] [ECO]
FTP credit for deposits set below market rate → branch managers stop gathering deposits (unprofitable for their P&L) → bank's funding liquidity deteriorates. **Trap:** candidates analyze the direct accounting impact instead of the behavioral incentive (second-order effect).

### Q28 [Liquidity] [REG] [REG > ECO]
NSFR: Wholesale funding from financial institutions with residual maturity < 6 months receives **0% ASF factor** — assumed to completely vanish in stress. Even if the counterparty relationship is "strong and long-standing" (noise), the regulatory factor is 0%.

### Q29 [Liquidity] [REG-ECO FLIP]
LCR net cash outflows use **prescribed run-off rates**, not bank-estimated rates. Stable retail deposits = 5% outflow (regulatory), even if the bank's internal model estimates 2%. **Trap:** using the bank's "more accurate" estimate instead of the regulatory floor.

### Q30 [Liquidity] [ABSOLUTE]
"A bank with LCR > 100% will never face a liquidity crisis." **Incorrect.** LCR is a 30-day stress metric. Intraday liquidity crunches, reputational runs exceeding modeled outflows, or collateral value drops can create liquidity stress even with LCR compliance.

### Q31 [Liquidity] [REG-ECO FLIP] [REG]
Under NSFR, a bank has stable retail deposits of €100M. The ASF factor is 95% → ASF = €95M. If the bank uses these deposits to fund a 30-year mortgage portfolio (RSF factor 65%), the NSFR contribution is: ASF (95% of deposits) vs RSF (65% of assets). The **NSFR ratio** for this funding source is 95% / 65% = 1.46 > 100% → stable funding surplus. **Trap:** Candidates confuse the RSF factor (asset-side) with the ASF factor (liability-side) — deposits are liabilities, so they contribute to Available Stable Funding, not Required Stable Funding.

### Q32 [Liquidity] [TRUE-IRRELEVANT] [REG]
A bank's collateral pool includes Level 2A assets (corporate bonds rated AA-) with a 15% haircut. The bonds have a market value of €50M. The HQLA value is €50M × (1 - 0.15) = €42.5M. If the bonds are downgraded to A+ but remain "proven liquid," they reclassify to Level 2B with a 25% haircut → HQLA value = €37.5M. **Trap:** The "proven liquidity" narrative is `[TRUE-IRRELEVANT]` — the rating rule (AA- vs A+) is the binding constraint for Level 2A classification.

### Q33 [Liquidity] [INVERSE INTUITION] [ECO]
A bank's FTP system gives branches a 5% credit on deposits (below the bank's wholesale funding cost of 6%). Branch managers respond by reducing deposit gathering efforts and focusing on loan origination. **This is rational from the branch P&L perspective** but harmful to the bank's overall funding liquidity. **Trap:** Candidates think "branches should always gather deposits" — but if FTP creates a disincentive, branches will rationally avoid deposits. The second-order effect (funding shortage) is the exam focus.

### Q34 [Liquidity] [REG-ECO FLIP] [REG]
Under LCR, a bank calculates net cash outflows for its deposit base. The regulatory run-off rate for stable retail deposits is 5%. The bank's internal model estimates 2% based on customer stickiness. **For regulatory LCR calculation, the bank must use 5%** — the regulatory floor applies regardless of internal modeling. **Trap:** Using the bank's "more accurate" internal estimate instead of the regulatory prescription.

### Q35 [Liquidity] [ABSOLUTE] [OPS]
"Contingency Funding Plans (CFPs) eliminate all liquidity risk if properly designed." **Incorrect.** CFPs are about **response** to liquidity stress, not prevention. Even with a perfect CFP, a bank can still face liquidity stress from sudden market shocks, operational failures, or counterparty defaults. The word "eliminate" is the `[ABSOLUTE]` trap.

---

## Domain 5: Investment Management (Questions 31–35)

### Q31 [InvMgmt] [TRUE-IRRELEVANT] [ECO]
A hedge fund reports high returns with high correlation to the Momentum factor. The returns represent **factor beta** (momentum premium), **not alpha** (skill). If a factor model explains it, it's compensation for bearing systematic risk. **Trap:** equating "high returns" with "skill."

### Q32 [InvMgmt] [INVERSE INTUITION]
PE fund reports low volatility and low correlation with public markets. This implies **smoothing bias** (stale pricing), not genuine diversification. True risk is higher, true correlation is higher, and Sharpe ratio is overstated. The exam rewards skepticism.

### Q33 [InvMgmt] [REG-ECO FLIP]
Pension fund surplus-at-risk: if the discount rate falls (rates↓), liability PV rises faster than asset PV for most pension funds → surplus shrinks → risk increases. **Trap:** "lower rates are good for bonds" — true for assets but the liability side moves more (longer duration).

### Q34 [InvMgmt] [ABSOLUTE]
"Diversification always reduces portfolio risk." **Incorrect in crisis.** Correlation convergence to 1 in stress eliminates diversification benefits precisely when they're needed most.

### Q35 [InvMgmt] [ECO]
Risk parity allocates based on **equal risk contribution**, not equal capital. Low-vol assets (bonds) get higher capital weight; high-vol assets (equities) get lower weight. **Trap:** confusing equal-weight with risk-parity.

### Q36 [InvMgmt] [REG-ECO FLIP] [REG]
A pension fund reports a surplus (assets > liabilities). The discount rate used to calculate liability PV falls by 100bps. **The surplus decreases** because liability PV is more duration-sensitive than asset PV for most pension funds. **Trap:** "Lower rates are good for bonds" — true for assets but the liability side moves more (longer duration). The net effect is surplus shrinkage.

### Q37 [InvMgmt] [TRUE-IRRELEVANT] [ECO]
A portfolio manager states: "Diversification always reduces portfolio risk." **Incorrect in crisis.** Correlation convergence to 1 in stress eliminates diversification benefits precisely when they're needed most. The word "always" is the `[ABSOLUTE]` trap. Historical average correlation may be 0.3, but stress-period correlation can spike to 0.8+.

### Q38 [InvMgmt] [INVERSE INTUITION] [ECO]
A hedge fund uses a strategy that is long volatility (buys options). When volatility increases sharply, the fund's P&L improves dramatically. However, the fund's **risk increases** because volatility is mean-reverting — the gains can reverse quickly if volatility collapses. **Trap:** Thinking "higher volatility = higher profit always" — for long vol positions, the profit is realized only if volatility stays elevated or increases further.

### Q39 [InvMgmt] [REG-ECO FLIP] [OPS]
A pension fund's investment policy mandates a minimum 60% allocation to "growth assets" (equities, alternatives). The fund's CRO argues for reducing equity exposure due to market volatility concerns. **From a fiduciary perspective**, the CRO's recommendation is inappropriate if it violates the policy — the policy was set by the board to meet long-term return objectives. **Trap:** "Risk management should always reduce risk" — but policy constraints may require maintaining risk exposure to meet return targets.

### Q40 [InvMgmt] [ABSOLUTE] [ECO]
"Private equity returns always outperform public equity over the long term." **Incorrect.** PE may have higher average returns historically, but this includes survivorship bias (failed funds don't report), illiquidity premium, and selection bias. Not all PE funds outperform, and the "always" qualifier makes the statement false.

---

## Domain 6: Current Issues (Questions 41–45)

### Q41 [Current] [REG-ECO FLIP] [OPS > THE]
An ML model predicts default with 99% accuracy but is a black box. The Model Validation committee should most likely **accept with constraints** (human overlay, parallel run, lower limits) — not reject outright (too conservative) or accept fully (too risky). The "middle path" of governance.

### Q42 [Current] [INVERSE INTUITION]
Climate risk: "Which risk is most immediate for a coal-plant lender?" → **Transition risk** (policy/tax) hits valuations before **Physical risk** (floods) destroys assets. Temporal dimension is the key.

### Q43 [Current] [TRUE-IRRELEVANT]
SVB lessons: the bank's securities portfolio had unrealized losses due to rising rates. "The bonds were high quality (Treasuries)." **True but irrelevant** — credit quality doesn't protect against interest rate risk. The loss was duration mismatch, not credit loss.

### Q44 [Current] [ABSOLUTE]
"DeFi eliminates counterparty risk through smart contracts." **Incorrect.** Smart contract bugs, oracle manipulation, governance attacks, and liquidity crunches create different but real counterparty-like risks.

### Q45 [Current] [REG]
NBFI (Non-Bank Financial Intermediation): systemic risk arises from leverage, maturity transformation, and interconnectedness **outside** the regulatory perimeter. The key concern is that NBFI entities are not subject to the same capital/liquidity requirements as banks, creating regulatory arbitrage.

---

## 5 Cross-Domain "Boundary Event" Questions (46–50)

### Q46 [Credit + OpRisk + Liquidity] — Boundary Event
**Vignette:** A bank's CVA model (internally developed) produces a significant pricing error due to a coding bug. The counterparty defaults the following week. The bank's liquidity position is stressed due to unexpected margin calls.

**The loss is classified as:**
- A) Credit risk — the counterparty defaulted
- B) Operational risk — the coding bug is the root cause
- C) Operational risk (root cause: model error) leading to credit loss (impact) and liquidity stress (consequence)
- D) Market risk — the pricing error affected MTM

**Answer:** C — The *cause* is OpRisk (model failure). The *manifestation* is credit loss and liquidity stress. Capital is held for Op Risk; liquidity buffers address the funding impact. Distinguishing cause from consequence is the 2026 exam trend.

### Q47 [Market + Liquidity] — Boundary Event
A bank's collateral (corporate bonds) is downgraded from A to BBB during a stress period. This simultaneously triggers: (1) HQLA reclassification from Level 2B to potentially ineligible, (2) higher haircuts in repo markets, (3) margin calls on derivatives. The **most immediate** risk is **liquidity** — the margin calls create a funding gap before market risk crystallizes.

### Q48 [Credit + Current Issues] — Boundary Event
An AI-based credit scoring model systematically underestimates PD for borrowers in regions with limited historical default data. This is both a **model risk** issue (Op Risk) and a **credit risk** issue (understated EL/UL). The governance response must address both: model validation (Op Risk framework) AND credit reserve adequacy (Credit Risk framework).

### Q49 [OpRisk + Current Issues] — Boundary Event
A cloud provider outage disables the bank's real-time risk monitoring for 6 hours. During this window, a trader exceeds position limits undetected. This is **third-party operational risk** (cloud dependency) enabling **market risk limit breach**. The exam tests whether candidates assign the cause (OpRisk) correctly vs the symptom (market risk breach).

### Q50 [All Domains] — Integrated Scenario
A geopolitical sanctions event causes: (1) a counterparty to become a restricted entity → credit exposure must be immediately crystallized, (2) the bank's correspondent banking network is disrupted → settlement/liquidity risk, (3) news coverage triggers reputational risk → deposit outflows, (4) the compliance team must screen all existing exposures → operational burden. **The Board's first priority should be:** ensuring legal compliance with sanctions (avoiding criminal liability) before optimizing capital/liquidity impacts.

---

## Domain 2 Addendum: Reading 28 — Twin Pair

### Q51 [Credit Risk] [REG-ECO FLIP] [REG > ECO]
**Vignette:** A Basel III reporter uses the Internal Ratings-Based (IRB) approach for its corporate credit portfolio. The bank's internal model estimates that during a severe systemic crisis, the asset correlation ($\rho$) for its High-Yield (HY) portfolio will spike to 0.35 due to industry-specific contagion. The Basel IRB prescription for this PD range yields $\rho = 0.12$. 

**For the purposes of calculating regulatory capital, the bank must use:**
- A) $\rho = 0.35$ because it represents the bank's best estimate of tail risk under stress
- B) $\rho = 0.12$ because the asset correlation formula is prescribed by the supervisor and cannot be overridden by internal estimates
- C) An average of internal and prescribed correlation ($\rho = 0.235$) to balance risk sensitivity with regulatory floors
- D) The Standardized Approach (SA) for the Hy portfolio because the IRB model has been invalidated by the internal stress test

**Answer:** **B**
**Why:** [REG-ECO FLIP]. Under Basel IRB, the bank estimates PD, LGD, and EAD, but the **asset correlation ($\rho$) is a formula-prescribed input** based on PD. The bank's internal "economic" view ($\rho = 0.35$) is irrelevant for the regulatory capital charge. Option A is the common "realism" trap. 

### Q52 [Credit Risk] [ABSOLUTE] [ECO]
**Vignette:** A CRO states: "Calculating Credit VaR using a migration-based model (like CreditMetrics) will always yield a higher capital charge than a default-only model (like CreditRisk+) for a diversified investment-grade portfolio."

**This statement is:**
- A) Correct — because CreditMetrics captures downgrade losses that CreditRisk+ ignores
- B) Incorrect — because CreditRisk+ uses a gamma distribution which creates a fatter right tail for defaults
- C) Incorrect — although CreditMetrics captures more "event" types (downgrades), the relative capital charge depends on the chosen confidence interval and credit spread volatility
- D) Correct — because default-only models are inherently more conservative than M2M models

**Answer:** **C**
**Why:** [ABSOLUTE] trap using "always." While CreditMetrics captures the **additional** risk of downgrades (making it conceptually broader), the numerical result isn't "always" higher. For example, if credit spreads are extremely stable or if the CreditRisk+ model is calibrated with high default rate volatility ($\sigma$), the default-only model could produce higher tail losses. Option A is a `[TRUE-IRRELEVANT]` trap—the additional capture is real, but doesn't guarantee a higher result in all calibrations.
