# The Boole Scaffold: Reading 23 - Introduction to Credit Risk Modeling

**Exam Priority:** 🟡 Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:*
*Related Readings: [R22 — Capital Structure](R22_Capital_Structure_in_Banks.md), [R28 — Credit VaR](R28_Credit_VaR.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **CAMEL Framework:** Regulators evaluate banks on Capital adequacy, Asset quality, Management, Earnings, and Liquidity. | `[REG]` | Medium — Core qualitative classification. | "supervisory assessment," "financial condition of a bank" |
| P2 | **Basel IRB Capital Matrix:** Under the Internal Ratings-Based approach, RWA relies on an asymptotic risk factor model where asset correlation ($\rho$) is prescribed inversely to PD (High PD = Low $\rho$). | `[REG]` | Absolute Dominance — Arguably the most tested tension in the curriculum. | "under Basel II IRB," "prescribed correlation" |
| P3 | **Merton Model (Structural):** Equity is a call option on the firm's assets with strike = Debt. Distance to Default (DD) measures how many standard deviations the asset value must fall to hit the debt barrier. | `[THE]` | Very High — The foundation of modern structural credit pricing. | "option pricing model," "distance to default" |
| P4 | **KMV Expected Default Frequency (EDF):** Improves Merton by using short-term debt + 50% of long-term debt as the default boundary, and maps output to a proprietary historical default database (not standard normal). | `[OPS]` | High — Tested as the practical industry evolution of Merton. | "Moody's KMV," "empirical mapping" |
| P5 | **CreditRisk+ vs CreditMetrics:** CreditRisk+ uses Poisson/Gamma (insurance math, default only, independent). CreditMetrics uses Mark-to-Market rating transition matrices (downgrade losses, copulas). | `[THE]` | High — Core categorization of the Big Three models. | "actuarial approach," "rating transition matrix" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P2 (IRB $\rho$ vs PD) | The analyst claims high-risk (High PD) obligors require the highest correlation multiplier mathematically. | **False.** Basel `[REG]` prescribes that High PD bonds have *lower* correlation multipliers because their default is viewed as idiosyncratic, whereas AAA companies only fail under systemic macro crashes (High $\rho$). |
| P3 (Merton) | A firm wants to evaluate the default risk of a 5-year corporate bond, but the firm's equity is entirely illiquid/private. | The **Merton model fails**. Structural models absolutely require observable equity prices and volatility to infer unobservable asset values. |
| P5 (Risk Models) | The CRO wants a model that tracks the economic loss from a loan dropping from AA to BBB over one year. | **CreditRisk+ is useless**, as it is a default-mode (binary) system. The CRO MUST use **CreditMetrics** (MtM transition model). |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Merton Model inputs: $V_0$ (Asset Value), $\sigma_V$ (Asset Volatility), $D$ (Debt Face Value), $t$ (Time).
- Real-world vs Risk-neutral $\mu$ in Distance to Default.
- Basel III's specific adjustments (liquidity, leverage, stressed VaR additions).

**Noise (distractors):**
- Corporate credit ratings when using the raw Merton model (Merton relies entirely on equity market prices, not agency ratings).
- Historical default recovery rates when using pure structural limits.

**Tensions:**
- **[THE] vs [OPS]**: Merton `[THE]` analytically assumes standard normal distributions and single zero-coupon debt structures. KMV `[OPS]` overrides this elegance with brute-force empirical defaults and messy debt structuring (STD + 0.5 LTD) because the real world is not normally distributed.



## 4. Directional Intuition
- **PD ↑ → Basel IRB ρ ↓:** Counter-intuitive but critical. High-PD obligors fail for idiosyncratic reasons (micro), so the systemic correlation factor is reduced. Low-PD (AAA) obligors only fail in macro crises → high ρ.
- **Asset Volatility (σ_V) ↑ → Distance to Default ↓ → PD ↑:** Higher volatility makes it easier for the asset value to breach the debt barrier in the Merton model.
- **Debt/Asset Ratio ↑ → Default Barrier ↑ → Distance to Default ↓:** Higher leverage raises the "trip wire" closer to the current asset value.

## 5. Ambiguity Traps (Anti-Decoder)
- **Basel IRB ρ vs. PD:** GARP's most tested tension. High-PD bonds get LOWER correlation under Basel, not higher. The reasoning: junk bonds default due to company-specific problems, not macro events.
- **Merton vs. KMV:** Merton uses N(d2) for PD (standard normal). KMV maps Distance to Default to an empirical default frequency (EDF), which is more accurate for real-world tails.
- **CreditRisk+ vs. CreditMetrics:** CreditRisk+ = Default-mode only (Poisson). CreditMetrics = Mark-to-Market (rating transitions, copulas). If the question mentions "downgrade losses" → CreditMetrics. If "actuarial" → CreditRisk+.
- **Private Firms & Merton:** Structural models REQUIRE observable equity prices. For private firms with no public equity, Merton cannot be used directly — KMV or reduced-form models must substitute.
- **CAMEL vs. CAMELS:** The S stands for "Sensitivity to Market Risk" — added later. If the question says "CAMEL" (5 letters), it's the original. "CAMELS" (6) is the expanded version.


## 4. Directional Intuition
- **PD ↑ → Basel IRB ρ ↓:** Counter-intuitive but critical. High-PD obligors fail for idiosyncratic reasons (micro), so the systemic correlation factor is reduced. Low-PD (AAA) obligors only fail in macro crises → high ρ.
- **Asset Volatility (σ_V) ↑ → Distance to Default ↓ → PD ↑:** Higher volatility makes it easier for the asset value to breach the debt barrier in the Merton model.
- **Debt/Asset Ratio ↑ → Default Barrier ↑ → Distance to Default ↓:** Higher leverage raises the "trip wire" closer to the current asset value.

## 5. Ambiguity Traps (Anti-Decoder)
- **Basel IRB ρ vs. PD:** GARP's most tested tension. High-PD bonds get LOWER correlation under Basel, not higher. The reasoning: junk bonds default due to company-specific problems, not macro events.
- **Merton vs. KMV:** Merton uses N(d2) for PD (standard normal). KMV maps Distance to Default to an empirical default frequency (EDF), which is more accurate for real-world tails.
- **CreditRisk+ vs. CreditMetrics:** CreditRisk+ = Default-mode only (Poisson). CreditMetrics = Mark-to-Market (rating transitions, copulas). If the question mentions "downgrade losses" → CreditMetrics. If "actuarial" → CreditRisk+.
- **Private Firms & Merton:** Structural models REQUIRE observable equity prices. For private firms with no public equity, Merton cannot be used directly — KMV or reduced-form models must substitute.
- **CAMEL vs. CAMELS:** The S stands for "Sensitivity to Market Risk" — added later. If the question says "CAMEL" (5 letters), it's the original. "CAMELS" (6) is the expanded version.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
