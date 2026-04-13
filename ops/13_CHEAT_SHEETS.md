# FRM Part 2 — Pre-Exam Cheat Sheets

> **Purpose:** One-page rapid review per domain. Use during final week (Phase 3, Week 16) for confidence reinforcement.  
> **Per Domain:** Top 5 formulas + Top 5 traps + Top 3 directional intuitions.

---

## Domain 1: Market Risk (20%)

### Top 5 Formulas
1. **VaR (Parametric):** `VaR_α = μ - z_α × σ × √t` — √t assumes i.i.d. returns
2. **Expected Shortfall:** `ES_α = E[Loss | Loss > VaR_α]` — ES ≥ VaR, coherent measure
3. **Backtesting Zones:** Green (0-4), Yellow (5-9), Red (≥10) at 99%/250 days
4. **EWMA:** `σ²_t = λ × σ²_{t-1} + (1-λ) × r²_{t-1}` — no mean reversion
5. **GARCH(1,1):** `σ²_t = ω + α × r²_{t-1} + β × σ²_{t-1}` — long-run variance = ω/(1-α-β)

### Top 5 Traps
1. **√t scaling:** Assumes i.i.d. returns. Illiquid markets with autocorrelation → √t understates multi-day VaR
2. **ES vs VaR:** ES at 97.5% ≈ VaR at 99% for normal distributions, but ES captures tail shape
3. **EWMA vs GARCH:** EWMA has no mean reversion. If question says "revert to long-run average" → EWMA is wrong
4. **Gaussian vs Student-t Copula:** Student-t has tail dependence (joint extremes cluster). Gaussian underestimates tail dependence
5. **FRTB ES vs VaR:** FRTB replaced VaR with ES for market risk capital. ES at 97.5% confidence.

### Top 3 Directional Intuitions
1. Correlation ↑ → Portfolio VaR ↑, Equity tranche risk ↓, Senior tranche risk ↑
2. Volatility ↑ → VaR ↑, ES ↑, Option value ↑
3. λ ↑ (EWMA) → Slower vol response; GARCH α ↑ → More reactive, β ↑ → More persistent

---

## Domain 2: Credit Risk (20%)

### Top 5 Formulas
1. **EL:** `EL = PD × LGD × EAD`
2. **UL (single obligor):** `UL = LGD × EAD × √(PD × (1-PD))`
3. **Vasicek WCDR:** `WCDR = N[(N⁻¹(PD) + √ρ × N⁻¹(X)) / √(1-ρ)]`
4. **CVA:** `CVA ≈ LGD_cpty × Σ[EE(t_i) × PD_cpty(t_{i-1}, t_i)]`
5. **SA-CCR:** `EAD = 1.4 × (RC + PFE)` — PFE multiplier depends on MPoR

### Top 5 Traps
1. **Correlation & Tranches:** Low ρ → Equity high risk, Senior very safe. High ρ → Equity lower risk, Senior higher risk. Equity = long correlation, Senior = short correlation
2. **CVA DVA Paradox:** Own spread ↑ → DVA ↑ → Accounting P&L ↑ → CET1 unchanged (Basel excludes DVA)
3. **Wrong-Way Risk:** Correlation between exposure and counterparty PD → CVA understated. Check correlation matrix
4. **Basel IRB ρ formula:** Banks estimate PD, LGD, EAD — but ρ is prescribed by formula based on PD. Cannot override with internal estimate
5. **Netting:** Netting reduces exposure only when positive and negative MTM positions offset. If all positions are in-the-money, netting = 0 benefit

### Top 3 Directional Intuitions
1. PD ↑ (Basel IRB) → Regulatory ρ ↓, UL ↑, EL ↑
2. Own spread ↑ → DVA ↑, Acct P&L ↑, CET1 unchanged
3. Cpty spread ↑ → CVA ↑, P&L ↓

---

## Domain 3: Operational Risk (20%)

### Top 5 Formulas
1. **SMA BIC:** `BIC: BI ≤ €1bn → 0.12 × BI; €1bn < BI ≤ €30bn → 0.12×€1bn + 0.15×(BI-€1bn); BI > €30bn → ... + 0.18×(BI-€30bn)`
2. **ILM:** `ILM = log(1 + min(α × Loss_10y, 15)) / log(2)` — National discretion allows ILM = 1
3. **Risk Decision Matrix:** High freq/High severity → Terminate; High freq/Low severity → Treat; Low freq/High severity → Transfer; Low freq/Low severity → Tolerate
4. **Three Lines of Defense:** 1st Line (business) executes, 2nd Line (risk) monitors/advises, 3rd Line (audit) independent assurance
5. **SR 11-7:** Model validation must be independent of model development

### Top 5 Traps
1. **Three Lines Violation:** 2nd Line monitoring business limit breach and instructing desk to unwind = inappropriate. 2nd Line advises, 1st Line executes
2. **BIC Tier Structure:** Apply tiered rates correctly. For BI = €5bn: 0.12×€1bn + 0.15×(€5bn-€1bn). Don't apply 0.15 to entire BI
3. **ILM National Discretion:** Some jurisdictions set ILM = 1 for all banks → historical losses have zero impact on capital
4. **KRIs:** "KRIs are always leading indicators" — False. KRIs can be leading (staff turnover), lagging (last quarter incidents), or current (system downtime today)
5. **Scenario Analysis:** "Scenario analysis always more reliable than historical data" — False. Neither is "always" more reliable. Scenario is forward-looking but subjective; historical is objective but backward-looking

### Top 3 Directional Intuitions
1. Complexity ↑ → Interconnectedness ↑ → OpRisk ↑
2. Remote Work ↑ → Cyber/Fraud surface ↑
3. Regulatory Pressure ↑ → CPBP Severity ↑

---

## Domain 4: Liquidity & Treasury Risk (15%)

### Top 5 Formulas
1. **LCR:** `LCR = HQLA / Net Cash Outflows (30-day) ≥ 100%`
2. **NSFR:** `NSFR = ASF / RSF ≥ 100%`
3. **HQLA Levels:** Level 1 (0% haircut, no cap), Level 2A (15% haircut, ≤40% cap, AA- or higher), Level 2B (25-50% haircut, ≤15% cap, BBB- to A+)
4. **ASF Factors:** CET1 (100%), Stable retail (95%), Wholesale <1yr (50%), FI wholesale <6mo (0%)
5. **FTP Behavioral:** FTP deposit credit ↓ → Branch deposit gathering ↓ → Bank liquidity ↓

### Top 5 Traps
1. **HQLA Rating Rule:** A+ rated bond = Level 2B (not 2A). Level 2A requires AA- or higher. "Proven liquidity" narrative is noise
2. **NSFR ASF Factor:** Wholesale FI funding < 6 months = 0% ASF factor. Even if relationship is "strong," regulatory factor is 0%
3. **LCR Run-off Rates:** Use prescribed rates, not bank estimates. Stable retail deposits = 5% outflow (regulatory), even if internal model estimates 2%
4. **FTP Incentives:** Analyze behavioral incentive, not direct accounting impact. FTP below market rate → branches stop gathering deposits
5. **LCR ≠ Liquidity Immunity:** LCR > 100% doesn't prevent liquidity crisis. Intraday crunches, reputational runs, collateral value drops can still cause stress

### Top 3 Directional Intuitions
1. FTP deposit credit ↓ → Deposit gathering ↓, liquidity ↓
2. Netting ↑ → Exposure ↓, capital ↓
3. MPoR ↑ → CVA capital ↑ (uncollateralized)

---

## Domain 5: Investment Management (15%)

### Top 5 Formulas
1. **Sharpe:** `Sharpe = (R_p - R_f) / σ_p`
2. **Information Ratio:** `IR = (R_p - R_b) / TE`
3. **Sortino:** `Sortino = (R_p - R_f) / Downside_σ`
4. **Pension Surplus-at-Risk:** `Surplus = Assets - Liabilities`. Discount rate ↓ → Liabilities PV ↑ (more than Assets PV ↑) → Surplus ↓
5. **Risk Parity:** `w_i = (1/σ_i) / Σ(1/σ_j)` — equal risk contribution, not equal capital

### Top 5 Traps
1. **Pension Discount Rate:** Lower rates → Liability PV rises faster than Asset PV → Surplus shrinks. Counter-intuitive for "rates good for bonds" thinking
2. **Risk Parity:** Allocates based on equal risk contribution, not equal capital. Low-vol assets (bonds) get higher capital weight
3. **Illiquid Asset Bias:** Low volatility and low correlation → implies smoothing bias (stale pricing), not genuine diversification. True risk higher, true correlation higher, Sharpe overstated
4. **Private Equity J-Curve:** Negative returns in early years are normal (fees, capital calls). Not a failure. Reflects illiquid, long-term nature
5. **"Diversification always reduces risk":** False. Correlation convergence to 1 in stress eliminates diversification benefits precisely when needed

### Top 3 Directional Intuitions
1. Discount rate ↓ → Pension surplus ↓ (liability duration > asset duration)
2. Volatility ↑ → VaR ↑, ES ↑, Option value ↑
3. Correlation ↑ → Portfolio VaR ↑, diversification benefit ↓

---

## Domain 6: Current Issues (10%)

### Top 5 Formulas
1. **SMA ILM:** `ILM = log(1 + min(α × Loss_10y, 15)) / log(2)` — National discretion allows ILM = 1
2. **Climate Transition:** `Transition Risk Impact = Policy_Severity × Carbon_Intensity × Asset_Exposure`
3. **Climate Physical:** `Physical Risk Impact = Probability(Physical_Event) × Asset_Value × Vulnerability`
4. **Stablecoin Reserve:** `Reserve_Ratio = Reserves / Outstanding_Stablecoins`
5. **NBFI Metrics:** Leverage = Assets/Equity, Maturity = Short-term Liabilities/Long-term Assets, Interconnectedness = Cross-exposures/Total

### Top 5 Traps
1. **Climate Temporal:** Transition risk (policy/tax) hits valuations before Physical risk (floods). For coal-plant lender, transition is immediate
2. **DeFi Counterparty:** "DeFi eliminates counterparty risk" — False. Smart contract bugs, oracle manipulation, governance attacks create real risks
3. **NBFI Regulatory Gap:** Leverage, maturity transformation, interconnectedness exist outside regulatory perimeter. NBFI not subject to same capital/liquidity as banks
4. **AI Governance:** Model with 99% accuracy but no explainability → accept with constraints (human overlay, parallel run), not reject or accept fully
5. **ILM National Discretion:** Some jurisdictions set ILM = 1 → historical losses have zero impact on Op Risk capital

### Top 3 Directional Intuitions
1. Reserve Ratio ↓ → Stablecoin depegging risk ↑
2. Redemption Pressure ↑ → Liquidity crisis risk ↑
3. Carbon Intensity ↑ → Transition risk impact ↑

---

## Final Week Strategy

**Day 1-2:** Review Domain 1 & 2 (40% combined weight) — focus on formulas and traps
**Day 3-4:** Review Domain 3 (20% weight) — focus on SMA, Three Lines, ILM
**Day 5:** Review Domain 4 & 5 (30% combined weight) — focus on LCR/NSFR and Investment ratios
**Day 6:** Review Domain 6 (10% weight) — focus on climate, DeFi, NBFI
**Day 7:** Full refresh — directional intuition drill only (cover right column, test recall)

**Key:** Don't memorize every formula. Master the directional relationships and the linguistic traps. The exam rewards pattern recognition over rote memorization.
