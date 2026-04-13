# FRM Part 2 — Learning Objective → Reading Mapping

> **Purpose:** Maps each Learning Objective (LO) to the specific reading(s) that cover it.  
> **How to use:** When a specific LO is weak, use this table to identify exactly which scaffolds to review. LOs spanning multiple readings are natural cross-domain boundary targets.

---

## Domain 1: Market Risk Measurement & Management (20%)

| LO # | Learning Objective | Primary Reading(s) | Secondary Reading(s) | Cross-Domain Notes |
|------|-------------------|-------------------|---------------------|-------------------|
| 1.1 | VaR estimation methods: Parametric, Historical Simulation, Monte Carlo | R1 (Market Risk Measures) | R18 (FRTB) | — |
| 1.2 | Expected Shortfall (ES) — definition, coherence, regulatory preference | R1 (Market Risk Measures) | R18 (FRTB) | — |
| 1.3 | Backtesting VaR models — exception counting, Basel traffic-light zones | R4 (Backtesting VaR) | R18 (FRTB) | — |
| 1.4 | Stress testing — scenario design, reverse stress testing, regulatory expectations | R5 (Stress Testing) | R58 (Stress Testing Banks) | Crosses to OpRisk (Domain 3) |
| 1.5 | Risk measures for non-linear portfolios — Delta-Gamma, full revaluation | R2 (Non-Linear Risk) | R18 (FRTB) | — |
| 1.6 | Correlation risk — breakdown in crisis, copulas, tail dependence | R8 (Correlation Basics) | R10 (Copulas), R29 (Portfolio Credit) | Crosses to Credit (Domain 2) |
| 1.7 | Volatility modeling — EWMA, GARCH, term structure of volatility | R6 (Volatility) | R12–R16 (Term Structure Models) | — |
| 1.8 | FRTB framework — IMA vs Standardized Approach, desk-level approval, P&L attribution | R18 (FRTB) | R64 (Basel III) | Crosses to OpRisk (Domain 3) |
| 1.9 | Sensitivity-based measures (SbM) — Delta, Vega, Curvature risk charges | R18 (FRTB) | — | — |
| 1.10 | Default Risk Charge (DRC) and Residual Risk Add-On (RRAO) | R18 (FRTB) | R28 (Credit VaR) | Crosses to Credit (Domain 2) |
| 1.11 | Market risk for options — Greeks, exotic option risks | R7 (Options) | R2 (Non-Linear Risk) | — |
| 1.12 | Model risk management — validation, governance, limitations | R56 (Model Risk) | — | Crosses to OpRisk (Domain 3) |
| 1.13 | Marginal VaR, Component VaR, Incremental VaR — portfolio decomposition | R1 (Market Risk Measures) | — | — |
| 1.14 | Parametric approaches — mapping positions, cash-flow mapping | R1 (Market Risk Measures) | — | — |

---

## Domain 2: Credit Risk Measurement & Management (20%)

| LO # | Learning Objective | Primary Reading(s) | Secondary Reading(s) | Cross-Domain Notes |
|------|-------------------|-------------------|---------------------|-------------------|
| 2.1 | Credit VaR — portfolio unexpected loss, single-factor Vasicek, granularity adjustment | R28 (Credit VaR) | R22 (Capital Structure), R29 (Portfolio Credit) | — |
| 2.2 | Default probability estimation — structural models (Merton), reduced-form (hazard rates), transition matrices | R23 (Credit Risk Modeling) | R27 (Estimating Default Probabilities) | — |
| 2.3 | Credit exposure — EAD, PFE, EPE, loan equivalents | R37 (Future Value Exposure) | R35 (Margin & Settlement) | — |
| 2.4 | Loss Given Default (LGD) — recovery rates, seniority, collateral | R21 (Credit Risk Management) | R41 (Securitization) | — |
| 2.5 | Counterparty credit risk (CCR) — netting, margining, wrong-way risk, right-way risk | R33 (Counterparty Risk Beyond) | R34 (Netting, Close-Out), R35 (Margin), R38 (CVA) | Crosses to Liquidity (Domain 4) |
| 2.6 | CVA & DVA — formulas, accounting vs risk management perspectives, CVA hedging | R38 (CVA) | R39 (Stress Testing CCR) | Crosses to Market (Domain 1) |
| 2.7 | Credit derivatives — CDS pricing, basis risk, index products | R31 (Credit Derivatives) | R30 (Credit Risk - Derivatives) | — |
| 2.8 | Securitization — CDO tranching, correlation effects on equity/mezzanine/senior, waterfall structures | R40 (Structured Credit) | R41 (Securitization) | — |
| 2.9 | SA-CCR — replacement cost, PFE add-on, aggregation across asset classes | R37 (Future Value Exposure) | — | — |
| 2.10 | Central Counterparties (CCPs) — default waterfall, skin-in-the-game, systemic risk implications | R36 (Central Clearing) | R78 (Repo Markets) | Crosses to Liquidity (Domain 4) |
| 2.11 | Credit scoring & rating models — PD estimation, discriminatory power (Gini, AR), calibration | R24 (Credit Scoring) | R25 (Retail Credit) | — |

---

## Domain 3: Operational Risk & Resilience (20%)

| LO # | Learning Objective | Primary Reading(s) | Secondary Reading(s) | Cross-Domain Notes |
|------|-------------------|-------------------|---------------------|-------------------|
| 3.1 | Operational risk framework — definition (Basel), loss event categories, business line mapping | R43 (Op Risk Framework) | — | — |
| 3.2 | Three Lines of Defense — roles, independence requirements, common violations | R20 (Governance) | R48 (Integrated Risk) | — |
| 3.3 | Op Risk measurement — Basic Indicator, Standardized, AMA (legacy), new SMA | R44 (Op Risk Measurement) | R64 (Basel III) | — |
| 3.4 | Loss data collection — internal loss data, external data, scenario analysis, BEICFs | R45 (Loss Data) | — | — |
| 3.5 | Risk and Control Self-Assessments (RCSA) — design, scoring, limitations | R46 (RCSA) | — | — |
| 3.6 | Key Risk Indicators (KRIs) vs Key Performance Indicators (KPIs) — design, thresholds, escalation | R47 (KRIs) | — | — |
| 3.7 | Cyber risk — threat landscape, controls, NIST framework, regulatory expectations | R49 (Cyber Resilience) | R53 (Outsourcing), R107 (Cyber Threats) | Crosses to Current Issues (Domain 6) |
| 3.8 | Operational resilience — impact tolerances, important business services, mapping dependencies | R50 (Operational Resilience) | R71 (Intraday Liquidity) | Crosses to Liquidity (Domain 4) |
| 3.9 | Model risk management — SR 11-7 / SS1/23, validation, governance | R56 (Model Risk) | R4 (Backtesting) | Crosses to Market (Domain 1) |
| 3.10 | Risk appetite & risk culture — board oversight, tone from the top, compensation alignment | R48 (Integrated Risk) | R59 (RAROC) | — |

---

## Domain 4: Liquidity & Treasury Risk Management (15%)

| LO # | Learning Objective | Primary Reading(s) | Secondary Reading(s) | Cross-Domain Notes |
|------|-------------------|-------------------|---------------------|-------------------|
| 4.1 | Liquidity risk types — funding liquidity, market liquidity, settlement/payment risk | R66 (Liquidity Risk) | R71 (Intraday Liquidity) | — |
| 4.2 | Liquidity Coverage Ratio (LCR) — HQLA classification (Level 1/2A/2B), total net cash outflows, 30-day horizon | R66 (Liquidity Risk) | — | — |
| 4.3 | Net Stable Funding Ratio (NSFR) — Available Stable Funding (ASF), Required Stable Funding (RSF), ≥100% requirement | R67 (NSFR) | — | — |
| 4.4 | Funds Transfer Pricing (FTP) — behavioral incentives, matched-maturity FTP, impact on business unit decisions | R79 (Liquidity Transfer Pricing) | — | — |
| 4.5 | Intraday liquidity management — real-time monitoring, nostro account management | R71 (Intraday Liquidity) | R73 (Failure Mechanics) | — |
| 4.6 | Contingency Funding Plans (CFPs) — triggers, stress scenarios, governance | R68 (CFP) | — | — |
| 4.7 | Liquidity stress testing — scenario design, behavioral assumptions, management actions | R69 (Liquidity Stress Testing) | — | — |
| 4.8 | Interest rate risk in the banking book (IRRBB) — EVE vs NII sensitivity, Basel standards | R82 (ALM Duration) | R83 (IRRBB) | — |

---

## Domain 5: Risk Management & Investment Management (15%)

| LO # | Learning Objective | Primary Reading(s) | Secondary Reading(s) | Cross-Domain Notes |
|------|-------------------|-------------------|---------------------|-------------------|
| 5.1 | Portfolio construction — mean-variance, risk budgeting, factor models | R84 (Portfolio Theory) | R85 (Factor Models) | — |
| 5.2 | Alpha vs Beta — factor decomposition, risk-adjusted performance (Sharpe, IR, Sortino) | R86 (Performance Attribution) | R87 (Risk-Adjusted Performance) | — |
| 5.3 | Hedge fund risk — strategy-specific risks, due diligence, style drift, illiquidity | R91 (HF Risk) | R92 (HF Due Diligence) | — |
| 5.4 | Pension fund risk — asset-liability mismatch, surplus at risk, discount rate sensitivity | R93 (Pension Risk) | R94 (ALM for Pensions) | — |
| 5.5 | Risk budgeting & allocation — marginal contribution to risk, risk parity | R85 (Factor Models) | R88 (Risk Budgeting) | — |
| 5.6 | VaR & risk measures for investment portfolios — parametric vs simulation-based | R84 (Portfolio Theory) | — | Crosses to Market (Domain 1) |
| 5.7 | Performance attribution — Brinson model (allocation, selection, interaction effects) | R86 (Performance Attribution) | — | — |
| 5.8 | Illiquid asset valuation — smoothing bias, unsmoothing techniques, J-curves in PE | R95 (Illiquid Assets) | R96 (Private Equity) | — |
| 5.9 | Tail risk management — portfolio insurance, options-based strategies, drawdown control | R98 (Tail Risk) | — | — |

---

## Domain 6: Current Issues in Financial Markets (10%)

| LO # | Learning Objective | Primary Reading(s) | Secondary Reading(s) | Cross-Domain Notes |
|------|-------------------|-------------------|---------------------|-------------------|
| 6.1 | AI/ML in financial risk management — model governance, explainability, black-box dilemma | R100 (AI ML) + R101 (AI Stability) | R56 (Model Risk) | Crosses to OpRisk (Domain 3) |
| 6.2 | Private credit drivers — alternative lending, risk factors, market dynamics | R102 (Private Credit Drivers) | R92 (Private Credit) | Crosses to Credit (Domain 2) |
| 6.3 | Geopolitical stability — sanctions, supply chain risk, scenario frameworks | R103 (Geopolitical Stability) | R26 (Country Risk) | Crosses to Credit (Domain 2) |
| 6.4 | Fiscal & monetary policy — rate environment, central bank actions, banking stress | R104 (Fiscal Monetary Policy) | R82 (ALM Duration) | Crosses to Liquidity (Domain 4) |
| 6.5 | Crypto regulation — DeFi, stablecoin mechanics, regulatory responses | R105 (Crypto Regulation) + R106 (Tokenization Inefficiencies) | — | — |
| 6.6 | Cyber resilience — systemic cyber risk, third-party risk, regulatory developments | R107 (Cyber Resilience) | R49 (Cyber Resilience in Book 3) | Crosses to OpRisk (Domain 3) |
| 6.7 | NBFI — systemic risk, leverage, interconnectedness outside regulatory perimeter | Not covered in Book 5 (use external material) | R78 (Repo Markets in Book 4) | Crosses to Liquidity (Domain 4) |
| 6.8 | Integrated risk management — enterprise risk aggregation, risk appetite frameworks | R48 (Integrated Risk in Book 3) | R58 (Stress Testing in Book 3) | Crosses to OpRisk (Domain 3) |

> **Note:** Domain 6 Current Issues are covered in Book 5 readings R100-R107. R108 (NBFI) and R109 (Rate Environment) referenced in older LO maps do not exist in the current wiki structure. Use external GARP materials for these topics.

---

## Cross-Domain LOs (Boundary Event Targets)

The following LOs span multiple domains and are high-probability candidates for cross-domain vignette questions:

| LO | Primary Domain | Secondary Domain(s) | Boundary Event |
|----|---------------|---------------------|----------------|
| 1.4 | Market Risk | OpRisk | BE-4 (Model Risk → VaR Underestimation) |
| 1.6 | Market Risk | Credit Risk | BE-7 (Wrong-Way Risk → Correlation Bomb) |
| 1.8 | Market Risk | OpRisk | BE-9 (AI Herding → Flash Crash) |
| 1.10 | Market Risk | Credit Risk | BE-1 (FRTB Liquidity Shocks → CVA) |
| 2.5 | Credit Risk | Liquidity Risk | BE-2 (Margin Spirals → Funding Liquidity) |
| 2.6 | Credit Risk | Market Risk | BE-1 (FRTB Liquidity Shocks → CVA) |
| 2.10 | Credit Risk | Liquidity Risk | BE-3 (CCP Concentration → Systemic Risk) |
| 3.7 | OpRisk | Liquidity Risk | BE-5 (Cyber → Payment Freeze) |
| 3.8 | OpRisk | Liquidity Risk | BE-5 (Cyber → Payment Freeze) |
| 3.9 | OpRisk | Market Risk | BE-4 (Model Risk → VaR Underestimation) |
| 4.5 | Liquidity Risk | OpRisk | BE-5 (Cyber → Payment Freeze) |
| 5.6 | Investment Mgmt | Market Risk | BE-8 (HF Leverage → Fire Sales) |
| 6.1 | Current Issues | OpRisk | BE-9 (AI Herding → Flash Crash) |
| 6.2 | Current Issues | Credit Risk | BE-4 (Climate Transition) |
| 6.5 | Current Issues | OpRisk | BE-5 (Cyber → Payment Freeze) |
| 6.6 | Current Issues | Liquidity Risk | BE-8 (HF Leverage → Repo Freeze) |
| 6.7 | Current Issues | Liquidity Risk | BE-5 (SVB Pattern) |
| 6.8 | Current Issues | OpRisk | BE-6 (Stress Testing Incoherence) |

---

## How to Use This Map

1. **When an LO is weak:** Review the Primary Reading scaffold first. If still weak, review Secondary Readings.
2. **For boundary event prep:** Focus on the Cross-Domain LOs listed above. These are the most likely to appear in multi-domain vignettes.
3. **For targeted review:** If you're weak on a specific concept (e.g., CVA), find all LOs mentioning it (2.6, 2.5, 1.10) and review all mapped readings.
4. **For progress tracking:** Use this with the LO Tracker to ensure you're covering all readings that contribute to each LO before marking it `[★]`.
