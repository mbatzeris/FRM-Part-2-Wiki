# The Boole Scaffold: Reading 21 - Credit Risk Management

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:*
*Related Readings: [R19 — Fundamentals](R19_Fundamentals_of_Credit_Risk.md), [R22 — Capital Structure](R22_Capital_Structure_in_Banks.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Expected vs Unexpected Loss:** Expected Loss (EL) = PD × LGD × EAD. It is provisioned for. Unexpected Loss (UL) is the variation in expected loss (tail risk) and requires Economic Capital buffers. | `[THE]` / `[ECO]` | Absolute Dominance — The defining math of credit risk. | "capital allocated for default," "provisioning" |
| P2 | **IFRS 9 Expected Loss Model:** Stage 1 (Performing) = 12-month expected loss. Stage 2 (Delinquent/Watch) = Lifetime expected loss. Stage 3 (Non-Performing) = Lifetime expected loss on net amount. | `[REG]` | High — Regulatory reporting mandate. | "International Financial Reporting Standards," "12-month EL" |
| P3 | **Asset Classification Spectrum:** Standard $\rightarrow$ Specially Mentioned $\rightarrow$ Substandard $\rightarrow$ Doubtful $\rightarrow$ Loss. | `[OPS]` | Medium — Triggers provisioning buckets. | "non-performing loan," "delinquent > 90 days" |
| P4 | **Concentration & Related Parties:** Regulators limit exposure to single clients and related parties (directors, subsidiaries) to prevent bias and systemic risk from single failures. | `[REG]` | High — Tests the boundary of acceptable risk thresholds. | "aggregate exposure," "board member loan" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (EL vs UL) | A bank experiences a high frequency of small defaults exactly in line with its historical PD modeling. | This is covered by **Expected Loss (Provisions/Reserves)**, not Economic Capital! If they tap Economic Capital, they failed their provisioning models. |
| P2 (IFRS 9) | An asset shows early signs of weakness but still pays coupons. | It moves from Stage 1 to Stage 2. Provisioning jumps from **12-month EL** to **Lifetime EL**, destroying near-term P&L visually on the balance sheet. |
| P3 (Classification) | A loan is delinquent for 105 days, but the bank begins tapping secondary collateral sources with hope of recovery. | The loan is **Substandard**, not a "Loss." "Loss" means write-off is unavoidable. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Time horizons: 12-month vs Lifetime EL.
- Distinguishing Provisioning (Expected) from Capital (Unexpected).
- The strict 90-day threshold for non-performing loans (NPL).

**Noise (distractors):**
- Intraday market volatility of related equities is noise when assessing the strict IFRS 9 stage of a non-traded loan.
- The use of "British vs US models" of accounting (Retention vs Write-off) is conceptual noise unless the question asks about the visual size of the loan loss reserves on the balance sheet.

**Tensions:**
- **[REG] vs [ECO]**: IFRS 9 `[REG]` forces banks to book Lifetime Expected Losses the moment an asset hits Stage 2, heavily depressing `[ECO]` profitability immediately rather than spreading it out as incurred.



## 4. Directional Intuition
- **Credit Quality ↓ (Stage 1 → Stage 2) → Provisioning ↑↑:** The jump from 12-month EL to Lifetime EL under IFRS 9 creates a P&L cliff — even a small downgrade triggers massive provisioning increases.
- **Portfolio Diversification ↑ → Unexpected Loss (UL) ↓:** Spreading exposure across industries reduces concentration, lowering the variance of the loss distribution.
- **Delinquency Days ↑ → Asset Classification ↓:** Each threshold (30, 60, 90 days) moves the loan down the classification spectrum, triggering progressively heavier provisioning.

## 5. Ambiguity Traps (Anti-Decoder)
- **EL vs. UL Placement:** Expected Loss goes in *provisions* (numerator of RAROC). Unexpected Loss goes in *Economic Capital* (denominator). Mixing them up is the #1 credit risk exam error.
- **IFRS 9 Stage 2 Trigger:** The move from Stage 1 to Stage 2 does NOT require a default or a specific number of delinquency days — it requires a "significant increase in credit risk" (SICR), which is a judgment call.
- **90-Day Rule:** Loans delinquent > 90 days are classified as non-performing (Stage 3). But a loan can be Stage 2 at 30 days if the bank judges the risk has "significantly increased."
- **"Loss" Classification:** A loan classified as "Loss" is fully written off. Don't confuse with "Doubtful" — which means the bank expects a loss but hasn't confirmed the amount.


## 4. Directional Intuition
- **Credit Quality ↓ (Stage 1 → Stage 2) → Provisioning ↑↑:** The jump from 12-month EL to Lifetime EL under IFRS 9 creates a P&L cliff — even a small downgrade triggers massive provisioning increases.
- **Portfolio Diversification ↑ → Unexpected Loss (UL) ↓:** Spreading exposure across industries reduces concentration, lowering the variance of the loss distribution.
- **Delinquency Days ↑ → Asset Classification ↓:** Each threshold (30, 60, 90 days) moves the loan down the classification spectrum, triggering progressively heavier provisioning.

## 5. Ambiguity Traps (Anti-Decoder)
- **EL vs. UL Placement:** Expected Loss goes in *provisions* (numerator of RAROC). Unexpected Loss goes in *Economic Capital* (denominator). Mixing them up is the #1 credit risk exam error.
- **IFRS 9 Stage 2 Trigger:** The move from Stage 1 to Stage 2 does NOT require a default or a specific number of delinquency days — it requires a "significant increase in credit risk" (SICR), which is a judgment call.
- **90-Day Rule:** Loans delinquent > 90 days are classified as non-performing (Stage 3). But a loan can be Stage 2 at 30 days if the bank judges the risk has "significantly increased."
- **"Loss" Classification:** A loan classified as "Loss" is fully written off. Don't confuse with "Doubtful" — which means the bank expects a loss but hasn't confirmed the amount.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
