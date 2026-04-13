# FRM Part 2 — Learning Objective Coverage Tracker

> **How to use:** After studying a topic, update its status. Run the Boole Scaffold and Twin-Question Drill before marking anything `[★]`. Your readiness score tells you where you stand.

## Status Legend
| Symbol | Meaning | Criteria to Advance |
|--------|---------|---------------------|
| `[ ]` | Not Started | — |
| `[~]` | Read / Listened (NotebookLM) | You can explain the concept in plain language |
| `[✓]` | Drilled (Boole + Twin-Question) | You've run the Antigravity framework on this topic |
| `[★]` | Combat Tested | You've answered practice questions correctly under timed conditions |

---

## Domain Weights & Readiness

| # | Domain | Weight | LOs Covered | Stars (★) | Domain Score |
|---|--------|--------|-------------|-----------|-------------|
| 1 | Market Risk | 20% | 14 / 14 | 0 / 14 | 0% |
| 2 | Credit Risk | 20% | 6 / 11 | 0 / 11 | 0% |
| 3 | Operational Risk & Resilience | 20% | 0 / 10 | 0 / 10 | 0% |
| 4 | Liquidity & Treasury Risk | 15% | 0 / 8 | 0 / 8 | 0% |
| 5 | Risk Mgmt & Investment Mgmt | 15% | 0 / 9 | 0 / 9 | 0% |
| 6 | Current Issues | 10% | 0 / 8 | 0 / 8 | 0% |
| | **TOTAL** | **100%** | **20 / 60** | **0 / 60** | **0%** |

> **Readiness Formula:** `Σ (domain_star_count / domain_total_LOs × domain_weight × 100)`  
> **Pass Threshold Target:** ≥ 70% weighted readiness before sitting the exam.

---

## Domain 1: Market Risk Measurement & Management (20%)

| # | Learning Objective | Status | Notes |
|---|---|---|---|
| 1.1 | VaR estimation methods: Parametric, Historical Simulation, Monte Carlo — assumptions, strengths, weaknesses | `[✓]` | R1, R2, R3 |
| 1.2 | Expected Shortfall (ES) — definition, coherence, regulatory preference over VaR | `[✓]` | R1 |
| 1.3 | Backtesting VaR models — exception counting, Basel traffic-light zones (Green ≤4, Yellow 5-9, Red ≥10 at 99%/250 days) | `[✓]` | R4, R6, R7 |
| 1.4 | Stress testing — scenario design, reverse stress testing, regulatory expectations | `[✓]` | R1 |
| 1.5 | Risk measures for non-linear portfolios — Delta-Gamma, full revaluation | `[✓]` | R12, R13 |
| 1.6 | Correlation risk — breakdown in crisis, copulas, tail dependence | `[✓]` | R3, R8, R9, R10 |
| 1.7 | Volatility modeling — EWMA, GARCH, term structure of volatility | `[✓]` | R14, R15, R16, R17 |
| 1.8 | FRTB framework — IMA vs Standardized Approach, desk-level approval, P&L attribution test, risk factor eligibility test | `[✓]` | R18 |
| 1.9 | Sensitivity-based measures (SbM) — Delta, Vega, Curvature risk charges | `[✓]` | R18 |
| 1.10 | Default Risk Charge (DRC) and Residual Risk Add-On (RRAO) | `[✓]` | R18 |
| 1.11 | Market risk for options — Greeks, exotic option risks | `[✓]` | R12, R17 |
| 1.12 | Model risk management — validation, governance, limitations | `[✓]` | R6 |
| 1.13 | Marginal VaR, Component VaR, Incremental VaR — portfolio decomposition | `[✓]` | R1, R11 |
| 1.14 | Parametric approaches — mapping positions, cash-flow mapping | `[✓]` | R5, R11 |

---

## Domain 2: Credit Risk Measurement & Management (20%)

| # | Learning Objective | Status | Notes |
|---|---|---|---|
| 2.1 | Credit VaR — portfolio unexpected loss, single-factor Vasicek model, granularity adjustment | `[✓]` | R28 |
| 2.2 | Default probability estimation — structural models (Merton), reduced-form (hazard rates), transition matrices | `[✓]` | R19, R23, R25, R26, R27 |
| 2.3 | Credit exposure — EAD, PFE, EPE, loan equivalents | `[✓]` | R21 |
| 2.4 | Loss Given Default (LGD) — recovery rates, seniority, collateral | `[✓]` | R19, R22 |
| 2.5 | Counterparty credit risk (CCR) — netting, margining, wrong-way risk, right-way risk | `[✓]` | R21 (basics only - netting/margining in R34-R36 pending) |
| 2.6 | CVA & DVA — formulas, accounting vs risk management perspectives, CVA hedging | `[ ]` | R21 |
| 2.7 | Credit derivatives — CDS pricing, basis risk, index products | `[ ]` | R21 |
| 2.8 | Securitization — CDO tranching, correlation effects on equity/mezzanine/senior, waterfall structures | `[ ]` | R40, R41 |
| 2.9 | SA-CCR — replacement cost, PFE add-on, aggregation across asset classes | `[ ]` | R21 |
| 2.10 | Central Counterparties (CCPs) — default waterfall, skin-in-the-game, systemic risk implications | `[ ]` | R21 |
| 2.11 | Credit scoring & rating models — PD estimation, discriminatory power (Gini, AR), calibration | `[✓]` | R20, R23, R24, R25 |

---

## Domain 3: Operational Risk & Resilience (20%)

| # | Learning Objective | Status | Notes |
|---|---|---|---|
| 3.1 | Operational risk framework — definition (Basel), loss event categories, business line mapping | `[ ]` | |
| 3.2 | Three Lines of Defense — roles, independence requirements, common violations | `[ ]` | |
| 3.3 | Op Risk measurement — Basic Indicator, Standardized, AMA (legacy), new SMA | `[ ]` | |
| 3.4 | Loss data collection — internal loss data, external data, scenario analysis, BEICFs | `[ ]` | |
| 3.5 | Risk and Control Self-Assessments (RCSA) — design, scoring, limitations | `[ ]` | |
| 3.6 | Key Risk Indicators (KRIs) vs Key Performance Indicators (KPIs) — design, thresholds, escalation | `[ ]` | |
| 3.7 | Cyber risk — threat landscape, controls, NIST framework, regulatory expectations | `[ ]` | |
| 3.8 | Operational resilience — impact tolerances, important business services, mapping dependencies | `[ ]` | |
| 3.9 | Model risk management — SR 11-7 / SS1/23, validation, governance | `[ ]` | |
| 3.10 | Risk appetite & risk culture — board oversight, tone from the top, compensation alignment | `[ ]` | |

---

## Domain 4: Liquidity & Treasury Risk Management (15%)

| # | Learning Objective | Status | Notes |
|---|---|---|---|
| 4.1 | Liquidity risk types — funding liquidity, market liquidity, settlement/payment risk | `[ ]` | |
| 4.2 | Liquidity Coverage Ratio (LCR) — HQLA classification (Level 1/2A/2B), total net cash outflows, 30-day horizon | `[ ]` | |
| 4.3 | Net Stable Funding Ratio (NSFR) — Available Stable Funding (ASF), Required Stable Funding (RSF), ≥100% requirement | `[ ]` | |
| 4.4 | Funds Transfer Pricing (FTP) — behavioral incentives, matched-maturity FTP, impact on business unit decisions | `[ ]` | |
| 4.5 | Intraday liquidity management — real-time monitoring, nostro account management | `[ ]` | |
| 4.6 | Contingency Funding Plans (CFPs) — triggers, stress scenarios, governance | `[ ]` | |
| 4.7 | Liquidity stress testing — scenario design, behavioral assumptions, management actions | `[ ]` | |
| 4.8 | Interest rate risk in the banking book (IRRBB) — EVE vs NII sensitivity, Basel standards | `[ ]` | |

---

## Domain 5: Risk Management & Investment Management (15%)

| # | Learning Objective | Status | Notes |
|---|---|---|---|
| 5.1 | Portfolio construction — mean-variance, risk budgeting, factor models | `[ ]` | |
| 5.2 | Alpha vs Beta — factor decomposition, risk-adjusted performance (Sharpe, IR, Sortino) | `[ ]` | |
| 5.3 | Hedge fund risk — strategy-specific risks, due diligence, style drift, illiquidity | `[ ]` | |
| 5.4 | Pension fund risk — asset-liability mismatch, surplus at risk, discount rate sensitivity | `[ ]` | |
| 5.5 | Risk budgeting & allocation — marginal contribution to risk, risk parity | `[ ]` | |
| 5.6 | VaR & risk measures for investment portfolios — parametric vs simulation-based | `[ ]` | |
| 5.7 | Performance attribution — Brinson model (allocation, selection, interaction effects) | `[ ]` | |
| 5.8 | Illiquid asset valuation — smoothing bias, unsmoothing techniques, J-curves in PE | `[ ]` | |
| 5.9 | Tail risk management — portfolio insurance, options-based strategies, drawdown control | `[ ]` | |

---

## Domain 6: Current Issues in Financial Markets (10%)

> [!NOTE]
> This section changes annually. Verify against the **2026 GARP reading list** before studying. Items below reflect the likely 2026 syllabus based on trends.

| # | Learning Objective | Status | Notes |
|---|---|---|---|
| 6.1 | AI/ML in financial risk management — model governance, explainability, black-box dilemma | `[ ]` | |
| 6.2 | Climate risk — physical vs transition risk, scenario analysis, TCFD/ISSB frameworks | `[ ]` | |
| 6.3 | Digital assets & DeFi — crypto risk, stablecoin mechanics, regulatory responses | `[ ]` | |
| 6.4 | Geopolitical risk — sanctions compliance, supply chain disruption, scenario frameworks | `[ ]` | |
| 6.5 | Cyber resilience — systemic cyber risk, third-party risk, regulatory developments | `[ ]` | |
| 6.6 | Non-bank financial intermediation (NBFI) — systemic risk, leverage, interconnectedness | `[ ]` | |
| 6.7 | Interest rate environment — banking stress (SVB lessons), ALM implications | `[ ]` | |
| 6.8 | Integrated risk management — enterprise risk aggregation, risk appetite frameworks | `[ ]` | |

---

## Weekly Review Checklist

Use this every Sunday to assess progress:

- [ ] Update all LO statuses above
- [ ] Recalculate domain scores in the summary table
- [ ] Identify the 3 weakest domains → prioritize for next week
- [ ] Review [07_ERROR_LOG.md](07_ERROR_LOG.md) for recurring distractor archetypes
- [ ] Adjust study calendar if behind schedule
