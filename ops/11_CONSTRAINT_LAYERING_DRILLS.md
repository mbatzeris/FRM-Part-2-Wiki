# FRM Part 2 — Constraint Layering Drills

> **Purpose:** High-yield exam simulation. Each vignette layers 2-3 conflicting constraints. Apply the Constraint Hierarchy: `[REG]` > `[APP]` > `[ECO]` > `[THE]`.  
> **How to use:** Read the vignette, identify all constraints, apply hierarchy, then answer. Compare with solution to check your framework application.

---

## BE-1: FRTB Liquidity Shocks → CVA

**Vignette:** A trading desk holds a large OTC interest rate swap portfolio with a BBB-rated counterparty. The desk's FRTB Internal Models Approach (IMA) calculates a 10-day VaR of $50M. The desk also calculates CVA at $12M. During a market stress event, liquidity dries up, and the desk cannot hedge its CVA exposure for 5 days. The CRO considers reducing the CVA capital charge by adjusting the margin period of risk (MPoR) assumption from 10 days to 5 days to reflect the desk's improved collateralization process. The risk manager argues this is inappropriate because the actual market conditions show hedge execution taking longer than 5 days.

**Question:** From a **regulatory** perspective, the CRO's proposed MPoR adjustment is:
- A) Appropriate — the desk's improved collateralization process justifies a lower MPoR
- B) Inappropriate — MPoR is a supervisory parameter that cannot be adjusted downward based on internal process improvements
- C) Appropriate — the stress event is temporary and the desk should reflect its normal operating conditions
- D) Inappropriate — CVA capital should be calculated using the longer of (a) contractual margin period and (b) actual market conditions

**Answer:** D — Under Basel, MPoR should reflect actual market conditions, not just contractual terms or internal processes. If market stress shows hedge execution takes longer than 5 days, using a 5-day MPoR understates CVA capital. The CRO's focus on "improved process" is `[ECO]` (efficiency), but the binding constraint is `[REG]` (supervisory requirement to reflect actual market liquidity). Option A is `[ECO]`-only reasoning. Option B is partially correct but overly rigid — MPoR can be adjusted, but must reflect reality, not wishful thinking.

---

## BE-2: Margin Spirals → Funding Liquidity

**Vignette:** A bank's derivatives portfolio with a central clearing member (CCP) has a negative MTM of -$200M. Under SA-CCR, the PFE multiplier is calculated based on the ratio of current exposure to margin period of risk. The bank's model suggests using a 10-day MPoR, which yields a multiplier of 1.2 and EAD of $240M. The bank's treasury department, facing a funding shortage, argues for using a 20-day MPoR to increase the multiplier to 1.4 and EAD to $280M, which would justify holding more capital and requesting additional funding from the board. The model validation team objects, stating that 20 days exceeds the standard supervisory assumption and would be rejected by the regulator.

**Question:** From a **risk management** perspective, the treasury's request is:
- A) Appropriate — conservative assumptions strengthen the bank's capital position
- B) Inappropriate — supervisory MPoR floors cannot be exceeded without explicit regulatory approval
- C) Appropriate — the bank's funding stress justifies a longer margin period
- D) Inappropriate — capital requirements should be minimized to preserve funding flexibility

**Answer:** B — While conservative assumptions are generally `[ECO]`-sound, Basel sets **floors** on MPoR (typically 10 days) for standardized calculations. Exceeding these floors without regulatory approval would be `[REG]` non-compliant. The treasury's funding concern is `[APP]` (business constraint), but `[REG]` dominates. Option A is the common "conservatism trap" — you can't be more conservative than the regulatory floor without approval. Option C confuses internal stress with supervisory parameters.

---

## BE-3: CCP Concentration → Systemic Risk

**Vignette:** A bank clears 80% of its derivatives through a single CCP. The CCP's skin-in-the-game is 1% of total default fund contributions. The bank's risk committee considers reducing its concentration by shifting 20% of volume to a second CCP. However, the second CCP has higher margin requirements, which would increase the bank's funding costs by $15M annually. The CFO argues against the shift, citing the economic cost and the fact that the first CCP has never defaulted. The CRO argues for the shift, citing concentration risk and the potential for a CCP failure to trigger a domino effect.

**Question:** From a **regulatory** perspective, the CRO's position is:
- A) Appropriate — concentration risk to a single CCP is a systemic concern
- B) Inappropriate — the economic cost outweighs the theoretical risk
- C) Appropriate — the bank should diversify across at least 3 CCPs
- D) Inappropriate — the first CCP's track record justifies continued concentration

**Answer:** A — Basel III explicitly addresses CCP concentration risk as a systemic concern. While the CFO's cost argument is `[ECO]`-valid, the `[REG]` requirement to manage systemic risk through diversification dominates. The "never defaulted" argument (Option D) is `[TRUE-IRRELEVANT]` — past performance does not guarantee future solvency. Option C is too prescriptive (regulation doesn't mandate 3 CCPs specifically), but the principle of diversification is correct.

---

## BE-4: Model Risk → VaR Underestimation

**Vignette:** A bank's market risk VaR model uses Historical Simulation with 500 days of data. During a period of low volatility, the model produces a 1-day 99% VaR of $10M. The model validation team discovers a coding error that caused the model to exclude the most volatile 10 days of data. Correcting the error would increase VaR to $15M. The desk head argues against the correction, stating that (a) the current market conditions are calm, (b) the error has existed for 2 years without issues, and (c) correcting it would trigger a capital increase and reduce the desk's P&L. The CRO insists on immediate correction.

**Question:** From a **regulatory** perspective, the CRO's insistence is:
- A) Appropriate — model errors must be corrected regardless of market conditions
- B) Inappropriate — the error's history suggests it's material only in stress, which is not current
- C) Appropriate — the bank should apply the corrected model prospectively only
- D) Inappropriate — the desk should be allowed to phase in the correction over 6 months

**Answer:** A — Model validation (SR 11-7) requires errors to be corrected immediately. The desk head's arguments are all `[ECO]` (current calm, history, P&L impact) or `[APP]` (business pressure), but `[REG]` (model integrity) dominates. Option B is the "history trap" — past luck doesn't justify future risk. Option C is partially correct but insufficient — retrospective correction may also be required depending on materiality. Option D is not a regulatory option.

---

## BE-5: Cyber → Payment Freeze

**Vignette:** A bank's payment processing system suffers a ransomware attack at 9:00 AM. The system is offline, preventing the bank from processing €500M in customer payments. The bank has a Contingency Funding Plan (CFP) that requires activating a backup line of credit when payment processing is disrupted for more than 4 hours. However, the backup line requires Board approval, which cannot be obtained until 2:00 PM. The CFO argues for waiting until 2:00 PM to avoid unnecessary borrowing costs. The CRO argues for activating the line immediately at 1:00 PM (4 hours after the attack), citing the CFP's trigger and the risk of reputational damage if payments are missed.

**Question:** From an **operational resilience** perspective, the CRO's position is:
- A) Appropriate — CFP triggers must be followed regardless of cost
- B) Inappropriate — the Board approval requirement is a binding constraint
- C) Appropriate — reputational risk outweighs borrowing costs
- D) Inappropriate — 4 hours is too short a threshold for payment disruption

**Answer:** A — CFP triggers are `[OPS]` governance requirements designed to ensure resilience. The CFO's cost argument is `[ECO]`, the Board approval is `[APP]` (process constraint), but the CFP's 4-hour trigger is `[OPS]` and must be followed. Option B is the "process trap" — governance exists to enable action, not block it. The CFP should have pre-approved activation authority. Option C is `[ECO]`-only reasoning that happens to align with the right conclusion.

---

## BE-6: Stress Testing Incoherence

**Vignette:** A bank runs its annual stress test using a severe but plausible scenario: 30% equity market decline, 200bps rate increase, and 20% corporate spread widening. The results show the bank's CET1 ratio falling from 12% to 8.5%, still above the 7% minimum. The CEO argues the bank is well-capitalized and can continue its dividend policy. The CRO points out that the stress test assumes the bank can sell all assets at modeled prices, but in a real crisis, market liquidity would be severely impaired, making actual losses higher. The CFO argues that including liquidity effects would double-count risk since the bank already holds a liquidity buffer.

**Question:** From a **regulatory** perspective, the CRO's concern is:
- A) Appropriate — stress tests should incorporate liquidity effects
- B) Inappropriate — liquidity risk is separate from capital stress testing
- C) Appropriate — the bank should use a more severe scenario
- D) Inappropriate — the modeled CET1 is already above minimum

**Answer:** A — Basel III requires stress tests to incorporate liquidity risk (CCAR, EBA stress tests include funding outflows). The CFO's "double-counting" argument is `[THE]` (theoretical purity) — in practice, liquidity and capital are interdependent. The CEO's conclusion is `[ECO]`-based on the modeled result, but the model's assumptions are flawed. Option B is incorrect — modern stress testing explicitly includes liquidity. Option C is not the core issue.

---

## BE-7: Wrong-Way Risk → Correlation Bomb

**Vignette:** A bank has a large CDS position on a sovereign counterparty. The bank is also the sovereign's primary lender, holding €500M in sovereign bonds. The correlation between the sovereign's credit spread and the bank's exposure is strongly positive (when the sovereign's credit deteriorates, the bank's exposure to the sovereign increases because the bank is more likely to be called on to provide emergency funding). The bank's CVA model assumes zero correlation between exposure and counterparty PD. The model validation team flags this as a material understatement of CVA. The desk argues that (a) the correlation is hard to quantify, (b) the sovereign has never defaulted, and (c) including correlation would increase capital by 40%.

**Question:** From a **risk management** perspective, the validation team's flag is:
- A) Appropriate — wrong-way risk must be modeled even if correlation is uncertain
- B) Inappropriate — without reliable correlation data, the zero assumption is acceptable
- C) Appropriate — the bank should use a conservative correlation assumption of 0.5
- D) Inappropriate — the sovereign's track record justifies the zero-correlation assumption

**Answer:** A — Wrong-way risk is a well-documented CVA understatement source. Basel requires banks to identify and model WWR, even if quantification is imperfect. The desk's arguments are `[ECO]` (hard to quantify, capital cost) and `[TRUE-IRRELEVANT]` (never defaulted). Option B is the "data perfection trap" — you don't need perfect data to apply a conservative adjustment. Option C is too prescriptive (0.5 may not be appropriate for this specific case).

---

## BE-8: HF Leverage → Fire Sales

**Vignette:** A pension fund has allocated 20% of its portfolio to a hedge fund that uses a long/short equity strategy with 3x leverage. During a market downturn, the hedge fund faces margin calls and must sell positions rapidly. The fund's prime broker offers to provide temporary bridge financing to avoid fire sales, but at a 15% interest rate. The hedge fund manager argues for accepting the bridge financing to preserve portfolio value. The pension fund's CRO argues against it, stating that (a) the bridge financing increases the fund's leverage further, (b) the pension fund's investment policy prohibits investments in funds with leverage > 2x, and (c) accepting the bridge would violate the policy.

**Question:** From a **fiduciary** perspective, the CRO's position is:
- A) Appropriate — investment policy constraints must be followed
- B) Inappropriate — bridge financing is a temporary liquidity solution, not a permanent leverage increase
- C) Appropriate — the pension fund should redeem its position instead
- D) Inappropriate — the policy should be interpreted flexibly in crisis

**Answer:** A — Investment policies are `[APP]` (governance constraints) that bind fiduciaries. The hedge fund manager's argument is `[ECO]` (preserve value) and `[TRUE-IRRELEVANT]` (temporary nature doesn't matter for policy compliance). Option B is the "flexibility trap" — policies exist precisely to prevent ad hoc decisions in crisis. Option C is not the core issue. Option D violates fiduciary duty.

---

## BE-9: AI Herding → Flash Crash

**Vignette:** A bank's trading desk uses an AI model for algorithmic trading. The model was trained on 5 years of historical data and has a 95% win rate. During a sudden market shock, the model (and similar models at other banks) all simultaneously sell the same positions, creating a flash crash. The bank's model validation team had approved the model without testing for herding behavior with other market participants. After the crash, the CRO argues for immediately disabling the AI model. The desk head argues for keeping it enabled, stating that (a) the model has been profitable, (b) the crash was a one-off event, and (c) competitors will keep their models running, putting the bank at a disadvantage if it disables.

**Question:** From a **model risk** perspective, the CRO's position is:
- A) Appropriate — models showing untested herding behavior must be disabled until validated
- B) Inappropriate — the model's historical profitability justifies continued use
- C) Appropriate — the bank should add herding tests to the model before re-enabling
- D) Inappropriate — disabling the model would put the bank at a competitive disadvantage

**Answer:** C — The immediate action is to disable (A is correct), but the proper governance response is to add herding tests before re-enabling. The desk head's arguments are `[ECO]` (profitability, competitive disadvantage) and `[TRUE-IRRELEVANT]` (one-off event doesn't negate the systemic risk). Option A is the right action but incomplete governance. Option B is the "profitability trap" — past profits don't justify unvalidated risk. Option D is `[ECO]`-only.

---

## BE-10: Climate Transition

**Vignette:** A bank's loan portfolio is 40% concentrated in coal mining companies. The bank's internal credit models show these loans have low PD (2%) based on historical default rates. The bank's climate risk team runs a transition scenario (Net Zero 2050) and projects that policy changes (carbon taxes, phase-out deadlines) will increase PD to 15% over 5 years. The credit risk committee argues that (a) the transition scenario is uncertain, (b) historical data is more reliable than forward-looking scenarios, and (c) reducing exposure to coal would hurt the bank's profitability in the short term. The CRO argues for incorporating climate risk into PD estimates and reducing exposure gradually.

**Question:** From a **regulatory** perspective, the CRO's position is:
- A) Appropriate — climate risk must be incorporated into risk assessments
- B) Inappropriate — forward-looking scenarios are too uncertain for regulatory capital
- C) Appropriate — the bank should use the higher PD (15%) immediately
- D) Inappropriate — historical data should take precedence over scenario analysis

**Answer:** A — Regulators (TCFD, ISSB, Basel climate risk guidance) explicitly require banks to incorporate climate risk into risk management. The credit committee's arguments are `[THE]` (uncertainty), `[ECO]` (historical reliability), and `[ECO]` (profitability). However, `[REG]` (climate risk integration) dominates. Option B is outdated — climate scenario analysis is now a regulatory expectation. Option C is too prescriptive (gradual transition may be appropriate). Option D ignores regulatory direction.

---

## Summary of Constraint Hierarchy Application

| BE # | Conflicting Constraints | Dominant Constraint | Key Takeaway |
|-----|------------------------|---------------------|--------------|
| BE-1 | [ECO] process improvement vs [REG] MPoR reality | [REG] | Supervisory parameters must reflect actual market conditions |
| BE-2 | [APP] funding pressure vs [REG] MPoR floor | [REG] | Cannot exceed supervisory floors without approval |
| BE-3 | [ECO] cost vs [REG] systemic risk | [REG] | Concentration risk trumps economic cost |
| BE-4 | [ECO] P&L impact vs [REG] model integrity | [REG] | Model errors must be corrected immediately |
| BE-5 | [ECO] borrowing cost vs [OPS] CFP trigger | [OPS] | Governance triggers must be followed |
| BE-6 | [THE] double-counting vs [REG] liquidity in stress test | [REG] | Modern stress testing includes liquidity |
| BE-7 | [ECO] quantification difficulty vs [REG] WWR requirement | [REG] | Must model WWR even if imperfect |
| BE-8 | [ECO] preserve value vs [APP] investment policy | [APP] | Policy constraints bind fiduciaries |
| BE-9 | [ECO] profitability vs [OPS] model validation | [OPS] | Unvalidated behavior must be tested before use |
| BE-10 | [THE] uncertainty vs [REG] climate risk | [REG] | Climate scenarios are now regulatory requirement |
