# Cross-Domain Boundary Events

> **Purpose:** The 2026 FRM Part II exam tests cascading, multi-book risks that traditional siloed study hides. This node maps every identified cross-domain boundary event—the exact point where a shock originating in one Book's domain spills into another. Use this as a falsification layer *on top of* the individual Boole Scaffolds.

---

## BE-1 · FRTB Liquidity Shocks → CVA Blow-Up → Operational Resilience Failure

**The Canonical 3-Book Cascade**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 1 (Market) | [R18 — FRTB](Book%201%20-%20Market%20Risk/R18_Fundamental_Review_Trading_Book.md) | FRTB assigns 120-day liquidity horizons to illiquid credit positions. In stress, these positions cannot be exited → mark-to-market losses spike. |
| **Amplifier** | Book 2 (Credit) | [R38 — CVA](Book 2 - Credit Risk/R38_CVA.md) | Market volatility ↑ → Expected Exposure (EE) ↑ → CVA charges explode. If Wrong-Way Risk (R38 P.38.4) is present, exposure and default probability spike simultaneously. |
| **Breaker** | Book 3 (OpRisk) | [R49 — Cyber-Resilience](Book%203%20-%20Operational%20Risk/R49_Cyber_Resilience.md) + [R48 — Integrated Risk](Book%203%20-%20Operational%20Risk/R48_Integrated_Risk_Management.md) | The resulting collateral disputes, intraday margin calls, and system overload test operational resilience. If the bank's incident response framework (R49 P.49.1: "Anticipate → Withstand → Recover → Adapt") fails, the operational arm collapses under the market/credit cascade. |

**Exam Trap:** A vignette describes a bank holding illiquid corporate credit derivatives. The question asks which risk domain the *primary* capital charge falls under. Siloed thinking says "Market Risk (FRTB)." The boundary answer: the CVA capital charge (K-CVA, R38) may dominate because the credit spread movement is both a market event *and* a counterparty event, and Basel III finalization (R64) forces CVA to the Standardized Approach.

---

## BE-2 · Margin Spirals → Funding Liquidity Drain → Dealer Bank Death

**The Collateral ↔ Liquidity Death Loop**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 2 (Credit) | [R35 — Margin & Settlement](Book 2 - Credit Risk/R35_Margin_Settlement.md) | Market volatility ↑ → haircuts ↑ (R35 P.35.2) → variation margin calls spike. If rehypothecation chains break (R35 P.35.4), posted collateral vanishes. |
| **Amplifier** | Book 4 (Liquidity) | [R66 — Liquidity Risk](Book%204%20-%20Liquidity%20Risk/R66_Liquidity_Risk.md) + [R71 — Intraday Liquidity](Book%204%20-%20Liquidity%20Risk/R71_Intraday_Liquidity.md) | Funding liquidity collapses (R66 P.66.1). Credit rating downgrade → required collateral ↑ → cash reserves ↓ (R66 directional intuition). Intraday settlement fails (R71 P.71.1). |
| **Terminal** | Book 4 (Liquidity) | [R73 — Failure Mechanics](Book%204%20-%20Liquidity%20Risk/R73_Failure_Mechanics.md) | Loss of cash settlement privileges with tri-party clearing banks (R73 P.73.5). Novation drain accelerates the collapse (R73 P.73.2). The dealer dies from *liquidity*, not *insolvency*. |

**Exam Trap:** "A dealer bank is solvent (positive equity) but has failed. What is the most likely cause?" Siloed Book 2 thinking says "credit default." The boundary answer: liquidity failure (R73 P.73.5)—consistent with the R19 distinction that insolvency ≠ default.

---

## BE-3 · CCP Concentration → Systemic Risk → Regulatory Capital Shock

**The "Too-Central-to-Fail" Problem**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 2 (Credit) | [R36 — Central Clearing](Book 2 - Credit Risk/R36_Central_Clearing.md) + [R33 — CCR Beyond](Book 2 - Credit Risk/R33_Counterparty_Risk_Beyond.md) | Mitigation of bilateral CCR through CCPs (R33 P.33.5) transforms counterparty risk into *systemic concentration risk*. If the CCP exhausts its default waterfall (R36 P.36.2), Rights of Assessment hit all members. |
| **Amplifier** | Book 4 (Liquidity) | [R78 — Repo Markets](Book%204%20-%20Liquidity%20Risk/R78_Repo_Markets.md) | CCP stress → repo haircuts spike (R78 directional intuition) → Fed Funds-GC spread widens (R78 P.78.5). The "flight to quality" starves non-government collateral of funding. |
| **Regulatory** | Book 3 (OpRisk) | [R64 — Basel III](Book%203%20-%20Operational%20Risk/R64_Basel_III_Reforms.md) | The output floor (72.5%, R64 P.64.1) prevents banks from using internal models to minimize the capital hit. CVA must now use standardized approaches only (R64 constraint flip). Capital buffers erode system-wide. |

**Exam Trap:** "Central clearing eliminates counterparty risk." FALSE. It *transforms* it (R33 P.33.5). The risk shifts from "my counterparty defaults" to "the CCP itself fails" — a low-probability, extinction-level systemic event.

---

## BE-4 · Model Risk → VaR Underestimation → Stressed Capital Shortfall

**The Model Blindness Chain**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 3 (OpRisk) | [R56 — Model Risk Management](Book%203%20-%20Operational%20Risk/R56_Model_Risk_Management.md) | A VaR model passes backtesting but has a conceptual flaw (R56 P.56.1 — "faulty design"). Vendor models treated as "Black Boxes" without sensitivity analysis (R56 P.56.5). |
| **Amplifier** | Book 1 (Market) | [R1 — Market Risk Measures](Book%201%20-%20Market%20Risk/R1_Market_Risk_Measures.md) + [R18 — FRTB](Book%201%20-%20Market%20Risk/R18_Fundamental_Review_Trading_Book.md) | Normal VaR underestimates fat-tail risk (R1 constraint flip). FRTB P&L Attribution test (R18 P.18.4) fails → desk forced to Standardized Approach → capital charge jumps. |
| **Cascade** | Book 2 (Credit) | [R39 — Stress Testing CCR](Book 2 - Credit Risk/R39_Stress_Testing_Counterparty.md) | Linearization (Delta-only) models understate derivative exposure during extreme moves (R39 P.39.3). Aggregation assumes independence (R39 P.39.4), but stressed correlations → 1.0 → netting benefits vanish. |

**Exam Trap:** "A bank's VaR model has zero backtesting exceptions. Is it reliable?" Not necessarily. Model risk includes *misuse* (R56 P.56.1). The model may be predicting normal days perfectly while being structurally incapable of capturing tail events (ES vs. VaR distinction, R1 P.1.4).

---

## BE-5 · Cyber Attack → Payment System Freeze → Liquidity Crisis → Market Contagion

**The Digital-Physical Cascade**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 5 (Current) | [R107 — Cyber Threats](Book%205%20-%20Investment%20Risk/R107_Cyber_Resilience.md) + [R101 — AI & Stability](Book%205%20-%20Investment%20Risk/R101_AI_Stability.md) | An integrity attack (R107 P.107.2) corrupts payment ledger data. AI-generated deepfake triggers social-media bank run (R101 P.101.4). Cloud concentration means one outage → multiple banks dark (R101 P.101.3). |
| **Amplifier** | Book 3 (OpRisk) | [R49 — Cyber-Resilience](Book%203%20-%20Operational%20Risk/R49_Cyber_Resilience.md) + [R53 — Outsourcing Risk](Book%203%20-%20Operational%20Risk/R53_Outsourcing_Risk.md) | Third-party cloud vendor failure (R53 P.53.5 — exit strategy) compounds the attack. Sub-contracting chains (R53 P.53.3) create hidden dependencies. Bank-to-bank information sharing (R49 P.49.3) is the primary defense. |
| **Terminal** | Book 4 (Liquidity) | [R71 — Intraday Liquidity](Book%204%20-%20Liquidity%20Risk/R71_Intraday_Liquidity.md) + [R73 — Failure Mechanics](Book%204%20-%20Liquidity%20Risk/R73_Failure_Mechanics.md) | Payment systems freeze → intraday settlement fails (R71 P.71.1) → wholesale "run" on the dealer bank (R73 P.73.1). The bank hasn't lost money; it simply can't *move* money. |

**Exam Trap:** "A cyber attack is an operational risk event." TRUE, but incomplete. The *second-order* effects are liquidity (payment freeze) and market (contagion/fire sales). The exam tests whether you recognize the *cascade*, not just the *origin*.

---

## BE-6 · Stress Testing Incoherence → Capital Plan Failure → Dividend Block

**The Regulatory Cascade**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 3 (OpRisk) | [R58 — Stress Testing Banks](Book%203%20-%20Operational%20Risk/R58_Stress_Testing_Banks.md) | CCAR stress scenario must be *coherent* (R58 P.58.1). Bank's internal scenario misses OpRisk legal-loss lag (R48 P.48.4: losses arrive 3-5 years after the crisis). |
| **Amplifier** | Book 5 (Current) | [R97 — Market-Driven Scenarios](Book%205%20-%20Investment%20Risk/R97_Market_Driven_Scenarios.md) | MDS framework requires plausibility (Mahalanobis Distance, R97 P.97.3). Too many policy variables → multicollinearity → unstable results (R97 P.97.2). Stressed covariance matrix must come from a *crisis* period, not calm markets (R97 constraint flip). |
| **Regulatory** | Book 3 (OpRisk) | [R59 — RAROC](Book%203%20-%20Operational%20Risk/R59_Risk_Capital_Attribution_RAROC.md) + [R58](Book%203%20-%20Operational%20Risk/R58_Stress_Testing_Banks.md) | If the stress test fails, the Capital Plan Rule blocks dividends/buybacks (R58 P.58.5). RAROC collapses for the stressed unit because Economic Capital ↑↑ while income ↓ (R59 P.59.1). |

**Exam Trap:** "A stress test shows the bank survives with 5% CET1. Has it passed?" Depends on whether the scenario was *coherent* (R58 P.58.1) and whether it captured the legal-loss lag (R48 P.48.4). A "passing" number from a flawed scenario is not a pass.

---

## BE-7 · Wrong-Way Risk → CVA Mispricing → Securitization Contagion

**The Correlation Bomb**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 2 (Credit) | [R38 — CVA](Book 2 - Credit Risk/R38_CVA.md) | Wrong-Way Risk (R38 P.38.4): exposure peaks precisely when the counterparty is most likely to default. Currency swaps with EM counterparties are the classic case (R38, Brazil/BRL example). |
| **Amplifier** | Book 2 (Credit) | [R40 — Structured Credit Risk](Book 2 - Credit Risk/R40_Structured_Credit_Risk.md) + [R41 — Securitization](Book 2 - Credit Risk/R41_Intro_to_Securitization.md) | Correlated defaults in the underlying pool → junior tranches wiped → mezzanine tranches hit. The "correlation smile" means small changes in default correlation → massive shifts in tranche valuation. |
| **Market** | Book 1 (Market) | [R10 — Copulas](Book%201%20-%20Market%20Risk/R10_Copulas.md) + [R8 — Correlation Basics](Book%201%20-%20Market%20Risk/R8_Correlation_Basics.md) | Gaussian copula underestimates tail dependence (R10). In stress, correlations → 1.0 (R8), destroying diversification benefits. The *same* correlation assumption error hits both CVA pricing and portfolio VaR. |

**Exam Trap:** "A Gaussian copula is used for both CVA and CDO pricing. In stress conditions, which is more dangerous?" Both fail, but CDO tranching amplifies the error — the mezzanine tranche is the most sensitive to correlation assumptions.

---

## BE-8 · HF Leverage → Fire Sales → Liquidity Black Hole → Repo Market Freeze

**The Hedge Fund Contagion Path**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 5 (Investment) | [R91 — HF Risk & Regulation](Book%205%20-%20Investment%20Risk/R91_HF_Risk_Regulation.md) | Leveraged HF faces margin calls → forced fire sales (R91 P.91.2). In stress, "market neutral" correlations → 1.0 (R91 directional intuition). |
| **Amplifier** | Book 4 (Liquidity) | [R66 — Liquidity Risk](Book%204%20-%20Liquidity%20Risk/R66_Liquidity_Risk.md) | Positive feedback traders accelerate the crash (R66 P.66.3). Liquidity Black Hole forms (R66 P.66.4): everyone sells, no one buys. Bid-offer spreads explode → liquidation cost formula shifts to stressed mode (R66 P.66.5). |
| **Systemic** | Book 4 (Liquidity) | [R78 — Repo Markets](Book%204%20-%20Liquidity%20Risk/R78_Repo_Markets.md) | Repo haircuts spike (R78 directional intuition). Overnight uncommitted repo lines are refused (R73 constraint flip). The HF's prime broker (a dealer bank) faces contagion spillover (R91 P.91.2). |

**Exam Trap:** "A hedge fund's failure is contained to its investors." FALSE. Through prime brokerage linkages (R91 P.91.2), fire-sale externalities (R66 P.66.4), and repo market contagion (R78), a single HF failure can freeze dealer bank funding.

---

## BE-9 · AI Herding → Flash Crash → FRTB Backtesting Failure → Capital Surge

**The Algorithmic Cascade**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 5 (Current) | [R101 — AI & Stability](Book%205%20-%20Investment%20Risk/R101_AI_Stability.md) | Institutions using identical pre-trained models develop identical blind spots (R101 P.101.2). Herding into the same crowded trades → synchronized exit → flash crash. |
| **Amplifier** | Book 1 (Market) | [R18 — FRTB](Book%201%20-%20Market%20Risk/R18_Fundamental_Review_Trading_Book.md) + [R4 — Backtesting VaR](Book%201%20-%20Market%20Risk/R4_Backtesting_VaR.md) | Flash crash triggers backtesting exceptions. If exceptions exceed 12 at 99% level (R18 ambiguity trap), the desk loses IMA approval → forced to SA → capital charge jumps. Non-Modellable Risk Factors (R18 P.18.5) spike because the crash creates "unprecedented" data gaps. |
| **Regulatory** | Book 3 (OpRisk) | [R56 — Model Risk](Book%203%20-%20Operational%20Risk/R56_Model_Risk_Management.md) | Post-crash, the model validation triad (R56 P.56.2) reveals conceptual unsoundness. The "herding" vulnerability was a model design flaw, not just bad luck. Regulators demand increased sensitivity analysis (R56 P.56.5). |

**Exam Trap:** "An AI-driven trading model has excellent in-sample performance. Is it low-risk?" No. In-sample performance masks herding risk (R101) and regime-change vulnerability. The model may be perfectly tuned to current conditions but catastrophically wrong in a tail event.

---

## BE-10 · USD Shortage → CIP Violation → Cross-Border Funding Crisis → ALM Mismatch

**The FX-Liquidity Cascade**

| Stage | Book | Reading | What Happens |
|:------|:-----|:--------|:-------------|
| **Trigger** | Book 4 (Liquidity) | [R80 — USD Shortage](Book%204%20-%20Liquidity%20Risk/R80_USD_Shortage.md) + [R81 — CIP Lost](Book%204%20-%20Liquidity%20Risk/R81_CIP_Lost.md) | Global dollar shortage → Covered Interest Parity breaks down (R81). FX swap basis widens → foreign banks can't roll USD funding. |
| **Amplifier** | Book 2 (Credit) | [R38 — CVA](Book 2 - Credit Risk/R38_CVA.md) | Currency swap WWR (R38 ambiguity trap: Brazil/BRL example). EM counterparty's default probability rises precisely as the bank's USD exposure grows. FVA (Funding Value Adjustment, R39) spikes because the cost of borrowing USD to post collateral explodes. |
| **Terminal** | Book 4 (Liquidity) | [R82 — ALM Duration](Book%204%20-%20Liquidity%20Risk/R82_ALM_Duration.md) + [R79 — Liquidity Transfer Pricing](Book%204%20-%20Liquidity%20Risk/R79_Liquidity_Transfer_Pricing.md) | Asset-liability duration mismatch widens (R82). Internal funds transfer pricing fails to reflect the true cost of USD funding (R79). The bank's LCR (R66 P.66.2) is breached in the USD currency bucket. |

**Exam Trap:** "CIP holds in equilibrium." Technically true, but the 2026 curriculum emphasizes that CIP has been *persistently violated* since 2008 (R81). A question combining FX basis risk with CVA Wrong-Way Risk tests the BE-10 cascade.

---

## Quick-Reference: Book-to-Book Collision Matrix

| | **Book 1 (Market)** | **Book 2 (Credit)** | **Book 3 (OpRisk)** | **Book 4 (Liquidity)** | **Book 5 (Current)** |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Book 1** | — | BE-1, BE-4, BE-7 | BE-4, BE-9 | BE-8 | BE-9 |
| **Book 2** | BE-1, BE-4, BE-7 | — | BE-3 | BE-2, BE-3, BE-10 | BE-7, BE-10 |
| **Book 3** | BE-4, BE-9 | BE-3 | — | BE-5 | BE-5, BE-6, BE-9 |
| **Book 4** | BE-8 | BE-2, BE-3, BE-10 | BE-5 | — | BE-8, BE-10 |
| **Book 5** | BE-9 | BE-7, BE-10 | BE-5, BE-6, BE-9 | BE-8, BE-10 | — |

---

## How to Use This Document

1. **After completing a Boole Scaffold**, check the collision matrix above. If your reading appears in any BE, re-read that BE and trace the full cascade.
2. **During drill sessions**, when a question references a concept in one book, ask: *"Does this shock cascade into another domain?"* If yes, the boundary answer will beat the siloed answer.
3. **For GARP-style vignettes**, look for multi-paragraph stems that describe a *sequence* of events across risk types. These are boundary event questions.
4. **Falsification rule**: If your answer to a multi-book vignette only references one Book's concepts, you have probably been trapped by the silo.

---

> **See also:** [Boundary Event Drill Templates](../ops/09_BOUNDARY_EVENTS.md) — 5 vignette-style practice scenarios for combat simulation of cross-domain events.
