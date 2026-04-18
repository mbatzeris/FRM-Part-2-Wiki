# FRM Part 2 — Quantitative Formula Engine

> **Purpose:** Domain-organized formula reference with directional intuition and common exam traps.  
> **How to use:** After reading a topic, use this as a quick-reference. For each formula, practice the "Directional Drill" — cover the intuition column and test yourself.

---

## Domain 1: Market Risk

### 1.1 Value-at-Risk (VaR)

**Parametric (Variance-Covariance)**
```
VaR_α = μ - z_α × σ × √t
```
| Variable | Meaning | Direction |
|----------|---------|-----------|
| `z_α` | Standard normal quantile at confidence α | α↑ → z↑ → VaR↑ |
| `σ` | Portfolio volatility | σ↑ → VaR↑ |
| `t` | Holding period | t↑ → VaR↑ (√t scaling) |

> **Exam Trap:** √t scaling assumes i.i.d. returns. If autocorrelation exists (illiquid markets), √t *understates* multi-day VaR. GARP tests this assumption violation.

**Portfolio VaR (2 assets)**
```
VaR_p = √(VaR₁² + VaR₂² + 2ρ × VaR₁ × VaR₂)
```
> **Directional:** ρ↑ → Diversification benefit↓ → VaR_p↑. At ρ=1, VaR_p = VaR₁ + VaR₂ (no benefit).

### 1.2 Expected Shortfall (ES)
```
ES_α = E[Loss | Loss > VaR_α]
```
- ES is always ≥ VaR at the same confidence level
- ES is a **coherent** risk measure (satisfies subadditivity); VaR is **not**
- Under Basel FRTB: ES replaces VaR at **97.5%** confidence

> **Exam Trap:** ES at 97.5% ≈ VaR at 99% for normal distributions, but ES captures tail shape.

### 1.3 Marginal / Component / Incremental VaR

| Measure | Formula | What It Answers |
|---------|---------|-----------------|
| **Marginal VaR** | `∂VaR_p / ∂w_i = β_i × VaR_p / Value` | Per-unit VaR sensitivity |
| **Component VaR** | `CVaR_i = w_i × MVaR_i × Value` | Position i's VaR contribution |
| **Incremental VaR** | `VaR(with) - VaR(without)` | Full position add/remove impact |

> **Key Identity:** Σ CVaR_i = Total Portfolio VaR

### 1.4 EWMA Volatility
```
σ²_t = λ × σ²_{t-1} + (1 - λ) × r²_{t-1}
```
> **Trap:** EWMA has **no mean reversion**. GARCH(1,1) adds it via the ω term. If question says "revert to long-run average" → EWMA is wrong.

### 1.5 GARCH(1,1)
```
σ²_t = ω + α × r²_{t-1} + β × σ²_{t-1}
Long-run variance = ω / (1 - α - β)
```
Stationarity requires α + β < 1.

### 1.6 Backtesting — Basel Traffic Light

| Zone | Exceptions (99%, 250 days) | Multiplier |
|------|---------------------------|-----------|
| **Green** | 0–4 | k = 3.0 |
| **Yellow** | 5–9 | +0.40 to +0.85 |
| **Red** | ≥ 10 | k + 1.0 |

### 1.7 Extreme Value Theory (EVT)

**Generalized Extreme Value (GEV) Distribution**
```
F(x) = exp[-(1 + ξ × (x - μ)/σ)^{-1/ξ}]   for ξ ≠ 0
F(x) = exp[-exp(-(x - μ)/σ)]             for ξ = 0 (Gumbel)
```
| Parameter | Distribution | Tail Behavior |
|-----------|--------------|---------------|
| ξ > 0 | Fréchet | Heavy-tailed (fat tails) |
| ξ = 0 | Gumbel | Exponential tails |
| ξ < 0 | Weibull | Bounded upper tail |

**Generalized Pareto Distribution (GPD)**
```
F(x) = 1 - (1 + ξ × x/σ̄)^{-1/ξ}   for ξ ≠ 0
F(x) = 1 - exp(-x/σ̄)             for ξ = 0 (Exponential)
```
> **Exam Trap:** EVT models tail behavior, not the entire distribution. Use only for losses exceeding a threshold u (POT method). ξ parameter determines tail thickness — ξ > 0 means infinite variance (fat tail).

### 1.8 Copula Functions

**Gaussian Copula**
```
C_ρ(u₁, u₂, ..., u_n) = Φ_ρ(Φ⁻¹(u₁), Φ⁻¹(u₂), ..., Φ⁻¹(u_n))
```
- Φ = standard normal CDF
- Φ_ρ = multivariate normal CDF with correlation matrix ρ
- **Limitation:** Underestimates tail dependence (assumes extreme co-defaults are rare)

**Student-t Copula**
```
C_ν,ρ(u₁, u₂, ..., u_n) = t_ν,ρ(t_ν⁻¹(u₁), t_ν⁻¹(u₂), ..., t_ν⁻¹(u_n))
```
- ν = degrees of freedom (lower ν = fatter tails)
- **Advantage:** Captures tail dependence (joint extreme events)
- **Exam Trap:** Student-t copula has "tail dependence" parameter — extreme events cluster together. Gaussian does not.

### 1.9 Term Structure Models

**Vasicek Model (Mean-Reverting)**
```
dr = κ(θ - r)dt + σdW
```
| Parameter | Meaning | Direction |
|-----------|---------|-----------|
| κ | Speed of mean reversion | κ↑ → faster reversion to θ |
| θ | Long-term mean rate | — |
| σ | Volatility | σ↑ → rate volatility ↑ |

**Ho-Lee Model (No Mean Reversion)**
```
dr = θ(t)dt + σdW
```
- Time-dependent drift θ(t) fits initial yield curve exactly
- **Limitation:** Negative rates possible (no mean reversion)

**Black-Derman-Toy (BDT) Model**
```
ln(r_{t+1}/r_t) = μ(t) + σ(t)ε
```
- Log-normal rates (r ≥ 0 always)
- Time-dependent volatility σ(t)
- **Use case:** Pricing interest rate derivatives with volatility smile

> **Exam Trap:** Vasicek has analytical bond pricing formula. Ho-Lee and BDT require lattice/tree methods. Vasicek allows negative rates; BDT does not.

---

## Domain 2: Credit Risk

### 2.1 Expected & Unexpected Loss
```
EL = PD × LGD × EAD
UL = LGD × EAD × √(PD × (1 - PD))     [single obligor]
```

### 2.2 Vasicek Single-Factor Model (Credit VaR)
```
WCDR = N[ (N⁻¹(PD) + √ρ × N⁻¹(X)) / √(1 - ρ) ]
Credit VaR = EAD × LGD × [WCDR(99.9%) - PD]
```
| Variable | Direction |
|----------|-----------|
| ρ↑ | WCDR↑ → Credit VaR↑ |
| PD↑ | WCDR↑ (but Basel IRB: regulatory ρ *decreases* with PD) |

### 2.3 CVA & DVA
```
CVA ≈ LGD_cpty × Σ [EE(t_i) × PD_cpty(t_{i-1}, t_i)]
DVA ≈ LGD_own  × Σ [NEE(t_i) × PD_own(t_{i-1}, t_i)]
```
| Event | CVA | DVA | P&L |
|-------|-----|-----|-----|
| Counterparty spread ↑ | ↑ | — | ↓ |
| Own spread ↑ | — | ↑ | ↑ (accounting) |

> **DVA Paradox:** Profit from own deterioration. Regulators exclude DVA from CET1.

### 2.4 Correlation & Tranche Impact

| Correlation | Equity Tranche | Senior Tranche |
|-------------|---------------|----------------|
| Low ρ | High risk | Very safe |
| High ρ | Lower risk | Higher risk |

> Equity = **long** correlation. Senior = **short** correlation.

### 2.5 SA-CCR
```
EAD = 1.4 × (RC + PFE)
RC = max(V - C, 0)   [unmargined]
PFE = multiplier × AddOn_aggregate
```

**PFE Add-On by Asset Class**
```
AddOn = Σ (AddOn_factor × Effective_Notional × Supervisory_Factor)
```
| Asset Class | Supervisory Factor (SF) | Notes |
|-------------|------------------------|-------|
| Interest Rate | 0.50% | Same across all tenors |
| FX | 4.0% | Single factor |
| Credit (single-name) | 0.38% (AAA–AA) → 6.00% (CCC and below) | Increases with credit grade deterioration |
| Credit (index) | 0.38% (IG) / 1.06% (speculative) | Two-bucket structure |
| Equity (single-name) | **32%** | — |
| Equity (index) | 20% | — |
| Commodity — electricity | 40% | Highest SF across all asset classes |
| Commodity — energy / metals / agricultural | 18% | All other commodities |

**Multiplier Calculation**
```
multiplier = min(1, floor[(RC + AddOn_aggregate) / (2 × MPR)] + 1)
MPR = 10-day netting set exposure (if > 0)
```
> **Exam Trap:** SA-CCR uses a 1.4 multiplier on (RC + PFE). The PFE multiplier depends on the ratio of current exposure to margin period of risk (MPR). High netting set exposure → lower multiplier → lower EAD.

### 2.6 MPoR Scaling for CVA
```
CVA_MPoR = CVA × (1 + e^(-a × MPoR))
```
| Variable | Meaning | Direction |
|----------|---------|-----------|
| MPoR | Margin Period of Risk (typically 10-20 days) | MPoR↑ → CVA_MPoR↑ |
| a | Scaling parameter (typically 0.05) | a↑ → faster decay |

> **Exam Trap:** CVA charges scale with margin period. Longer MPoR (uncollateralized trades) → higher CVA capital. Collateralization reduces MPoR and thus CVA capital requirement.

---

## Domain 3: Operational Risk

### 3.1 SMA Capital
```
BIC:  BI ≤ €1bn → 0.12 × BI
      €1bn < BI ≤ €30bn → ... + 0.15 × (BI - €1bn)
      BI > €30bn → ... + 0.18 × (BI - €30bn)
```

### 3.2 Risk Decision Matrix

| Frequency | Severity | Strategy |
|-----------|----------|----------|
| Low | Low | **Tolerate** |
| Low | High | **Transfer** (Insure) |
| High | Low | **Treat** (Mitigate) |
| High | High | **Terminate** (Exit) |

---

## Domain 4: Liquidity & Treasury Risk

### 4.1 LCR
```
LCR = HQLA / Net Cash Outflows (30-day) ≥ 100%
```
| Level | Assets | Haircut | Cap |
|-------|--------|---------|-----|
| 1 | Cash, sovereign (0% RW) | 0% | None |
| 2A | Corp bonds (AA-), covered bonds | 15% | ≤40% |
| 2B | Corp bonds (BBB- to A+), equities | 25-50% | ≤15% |

> **Trap:** A+ rated bond = Level **2B** (not 2A). 2A requires AA-.

### 4.2 NSFR
```
NSFR = ASF / RSF ≥ 100%
```
| Source | ASF Factor |
|--------|-----------|
| CET1 | 100% |
| Stable retail deposits | 95% |
| Wholesale < 1yr | 50% |
| FI wholesale < 6mo | 0% |

### 4.3 FTP Behavioral Incentives
> FTP credit for deposits ↓ → branches stop gathering deposits → liquidity ↓

---

## Domain 5: Investment Management

### 5.1 Key Ratios
```
Sharpe = (R_p - R_f) / σ_p
IR = (R_p - R_b) / TE
Sortino = (R_p - R_f) / Downside_σ
```

### 5.2 Illiquid Asset Bias

| Reported | True | Bias Direction |
|----------|------|---------------|
| Volatility | Higher | Understated |
| Correlation | Higher | Understated |
| Sharpe | Lower | Overstated |

### 5.3 Mahalanobis Distance (Scenario Plausibility)
```
D_M = √[(x - μ)ᵀ × Σ⁻¹ × (x - μ)]
```
| Variable | Meaning |
|----------|---------|
| x | Proposed scenario vector |
| μ | Historical mean vector |
| Σ⁻¹ | Inverse covariance matrix |
| D_M | Mahalanobis distance |

> **Exam Trap:** Mahalanobis distance measures how many standard deviations a scenario is from the historical mean, accounting for correlation. D_M² > χ² threshold indicates implausible scenario. Used in Market-Driven Scenarios (MDS) to filter out impossible stress tests.

### 5.4 Pension Fund Surplus-at-Risk
```
Surplus = Assets - Liabilities
Surplus_at_Risk = Surplus - Confidence_Level(Surplus)
```
| Variable | Direction |
|----------|-----------|
| Discount rate ↓ | Liabilities PV ↑ (more than Assets PV ↑) → Surplus ↓ |
| Asset volatility ↑ | Surplus_at_Risk ↑ |
| Duration mismatch ↑ | Surplus volatility ↑ |

> **Exam Trap:** Pension liabilities typically have longer duration than assets. When rates fall, liability PV rises faster than asset PV → surplus shrinks. Counter-intuitive for candidates who think "lower rates = good for bonds."

### 5.5 Risk Parity Allocation
```
w_i = (1/σ_i) / Σ(1/σ_j)  [equal risk contribution]
```
| Asset Class | Risk Contribution | Capital Weight |
|-------------|-------------------|----------------|
| Low-vol (bonds) | Equal | Higher |
| High-vol (equities) | Equal | Lower |

> **Exam Trap:** Risk parity allocates based on equal **risk contribution**, not equal capital. Bonds get higher capital weight because they're lower volatility.

### 5.6 J-Curve in Private Equity
```
J-Curve: Returns negative in early years (fees, capital calls) → positive in later years (exits)
```
| Year | Cash Flow | Net IRR |
|------|-----------|---------|
| 1-3 | Negative (fees, investments) | Negative |
| 4-7 | Mixed (some exits) | Approaching break-even |
| 8+ | Positive (exits) | Positive |

> **Exam Trap:** PE funds show negative returns in early years. This is normal, not a failure. The J-Curve reflects the illiquid, long-term nature of PE investments.

---

## Domain 6: Current Issues in Financial Markets (10%)

### 6.1 SMA Internal Loss Multiplier (ILM)
```
ILM = ln[exp(1) − 1 + (LC / BIC)^0.8]
LC  = 15 × average annual operational losses over the prior 10 years
Op Risk Capital = BIC × ILM
```
| Variable | Direction |
|----------|-----------|
| LC / BIC ratio ↑ | ILM ↑ (above 1) |
| LC / BIC = 0 | ILM = 1 (no historical-loss penalty) |
| National discretion | ILM = 1 (override regardless of LC) |

> **Exam Trap:** National discretion allows supervisors to set ILM = 1, meaning historical losses have zero impact on Op Risk capital. Don't assume ILM always > 1 for banks with high losses. Also: when LC/BIC = 1, ILM = ln(e) = 1 exactly — the formula is anchored so that "average bank" has ILM ≈ 1.

### 6.2 Climate Risk Transition Scenarios
```
Transition Risk Impact = Policy_Severity × Carbon_Intensity × Asset_Exposure
Physical Risk Impact = Probability(Physical_Event) × Asset_Value × Vulnerability
```
| Risk Type | Temporal Priority | Key Drivers |
|-----------|------------------|-------------|
| Transition | Immediate (policy/tax) | Carbon taxes, phase-out deadlines, technology shifts |
| Physical | Longer-term (decades) | Sea-level rise, extreme weather, agricultural loss |

> **Exam Trap:** For a coal-plant lender, **transition risk** (policy/tax) hits valuations **before** physical risk (floods) destroys assets. The temporal dimension is key.

### 6.3 Stablecoin Mechanics
```
Reserve_Ratio = Reserves / Outstanding_Stablecoins
Redemption_Pressure = (Redemptions / Reserves) × Time_Window
```
| Variable | Direction |
|----------|-----------|
| Reserve_Ratio ↓ | Depegging risk ↑ |
| Redemption_Pressure ↑ | Liquidity crisis risk ↑ |
| Reserve asset volatility ↑ | Depegging risk ↑ |

> **Exam Trap:** "DeFi eliminates counterparty risk through smart contracts" — False. Smart contract bugs, oracle manipulation, governance attacks, and liquidity crunches create different but real counterparty-like risks.

### 6.4 NBFI Systemic Risk Metrics
```
Leverage = Assets / Equity
Maturity_Transformation = (Short-term_Liabilities / Long-term_Assets)
Interconnectedness = Cross-exposures / Total_Exposures
```
| Metric | NBFI Concern | Bank Comparison |
|--------|--------------|-----------------|
| Leverage | High (hedge funds, PE) | Regulated (Basel III) |
| Maturity | High (MMFs, repo) | Regulated (LCR, NSFR) |
| Interconnectedness | High (shadow banking) | Regulated (CCPs) |

> **Exam Trap:** NBFI systemic risk arises from leverage, maturity transformation, and interconnectedness **outside** the regulatory perimeter. The key concern is that NBFI entities are not subject to the same capital/liquidity requirements as banks.

### 6.5 AI Model Governance Metrics
```
Model_Explainer_Score = Feature_Importance_Clarity / Total_Feature_Count
Fairness_Metric = (Protected_Group_Accuracy - Overall_Accuracy) / Overall_Accuracy
```
| Governance Aspect | Regulatory Expectation |
|-------------------|------------------------|
| Explainability | Must be interpretable for high-impact models |
| Fairness | No disparate impact on protected groups |
| Human Oversight | Human-in-the-loop for critical decisions |

> **Exam Trap:** An ML model with 99% accuracy but no explainability should be **accepted with constraints** (human overlay, parallel run, lower limits) — not rejected outright (too conservative) or accepted fully (too risky). The "middle path" of governance.

---

## Directional Intuition Drill — Cover & Test

| Input Change | Impact |
|-------------|--------|
| Correlation ↑ | Portfolio VaR ↑, Equity tranche risk ↓, Senior tranche risk ↑ |
| Volatility ↑ | VaR ↑, ES ↑, Option value ↑ |
| PD ↑ (Basel IRB) | Regulatory ρ ↓, UL ↑, EL ↑ |
| Own spread ↑ | DVA ↑, Acct P&L ↑, CET1 unchanged |
| Cpty spread ↑ | CVA ↑, P&L ↓ |
| λ ↑ (EWMA) | Slower vol response |
| GARCH α ↑ | More reactive |
| GARCH β ↑ | More persistent |
| FTP deposit credit ↓ | Deposit gathering ↓, liquidity ↓ |
| Netting ↑ | Exposure ↓, capital ↓ |
| Wrong-Way Risk | CVA understated |
| EVT ξ ↑ | Tail fatter, extreme losses more likely |
| Copula ν ↓ (Student-t) | Tail dependence ↑, joint defaults ↑ |
| Vasicek κ ↑ | Faster mean reversion, rate volatility ↓ |
| MPoR ↑ | CVA capital ↑ (uncollateralized) |
| Mahalanobis D_M ↑ | Scenario less plausible |
