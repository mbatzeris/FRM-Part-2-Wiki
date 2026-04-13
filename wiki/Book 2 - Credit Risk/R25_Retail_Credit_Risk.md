# The Boole Scaffold: Reading 25 - Retail Credit Risk Management

**Exam Priority:** 🟡 Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R24 — Credit Scoring](R24_Credit_Scoring_and_Rating.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Retail vs Corporate:** Retail credit uses automated scoring (statistical models) due to high volume/low value. Corporate credit uses bespoke expert judgment. | `[OPS]` | Low/Medium — Foundational distinction. | "retail portfolio," "consumer loans" |
| P2 | **Retail Model Predictability:** Retail portfolios are highly granular, making overall expected loss highly predictable (Law of Large Numbers), but severely exposed to macro-systemic shocks. | `[ECO]` | High — Explains why retail unexpected loss volatility is often driven entirely by macro factors. | "granularity," "consumer macro sensitivity" |
| P3 | **Retail Basel IRB Correlation:** Under regulatory capital, retail portfolios (like mortgages or credit cards) have lower prescribed asset correlations ($\rho$) than corporate loans. | `[REG]` | Very High — Heavily tested Basel constraint. | "Retail IRB," "prescribed asset correlation" |
| P4 | **Cutoff Score Optimization:** The bank maximizes profit by setting the cutoff score where Marginal Revenue of accepting the next borrower = Marginal Cost (Expected Loss). | `[ECO]` | High — The core logic of consumer credit approval. | "cutoff score," "marginal cost of default" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (Scoring) | The bank attempts to manually underwrite a batch of 100,000 credit card applications. | The **operational cost** destroys the margin. Retail relies strictly on statistical automation. |
| P3 (Retail vs Corp $\rho$) | The CRO wants to apply internal corporate correlations (e.g., 0.15) to a retail credit card portfolio. | Under `[REG]`, retail correlations are prescribed significantly lower (often 0.04) because retail defaults are highly idiosyncratic globally. |
| P4 (Cutoff Score) | The economy enters a boom phase, decreasing the generic PD across all consumers. | The bank should **lower its cutoff score**. Because EL dropped, the Marginal Cost intersecting Marginal Revenue shifted downward, allowing more approvals. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- High granularity (large number of small exposures).
- Trade-off between approval rates and default rates.
- Basel IRB treatment specifying lower risk weights and correlations for retail vs wholesale.

**Noise (distractors):**
- Complex single-name structural models (like Merton) — retail credit never uses structural models because consumers do not have traded equity.
- Individual borrower analysis in a purely portfolio-level question.

**Tensions:**
- **[THE] vs [OPS]:** Theoretical models might suggest precise individual behavioral modeling. Operationally, banks bin consumers into large risk buckets (scorecards) and apply uniform pricing.

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| Expected Profit (Retail Loan) | Cutoff Model Strictness ↑ → Approval Rate ↓, Profit margin per loan ↑ but Total Volume ↓ | Setting cutoff too high leaves profitable (high margin, moderate risk) borrowers unserved. |
| Law of Large Numbers (Retail) | Number of loans ($N$) ↑ → Portfolio Variance (relative to Mean) ↓ | Assuming adding more retail loans increases absolute portfolio risk linearly — granularity reduces the *relative* unexpected loss. |


## 5. Ambiguity Traps (Anti-Decoder)
- **Pool-Level vs. Individual Modeling:** Retail credit risk is modeled at the pool level (segments of similar borrowers), not individual obligor level like corporate credit. This is because individual retail exposures are too small.
- **Behavioral Scoring vs. Application Scoring:** Application scoring is at origination (static). Behavioral scoring uses post-origination data (dynamic) and is more predictive of actual default.
- **Loss Forecasting Horizon:** Retail models typically use a 12-month horizon for EL estimation, aligning with IFRS 9 Stage 1.

## 5. Ambiguity Traps (Anti-Decoder)
- **Pool-Level vs. Individual Modeling:** Retail credit risk is modeled at the pool level (segments of similar borrowers), not individual obligor level like corporate credit. This is because individual retail exposures are too small.
- **Behavioral Scoring vs. Application Scoring:** Application scoring is at origination (static). Behavioral scoring uses post-origination data (dynamic) and is more predictive of actual default.
- **Loss Forecasting Horizon:** Retail models typically use a 12-month horizon for EL estimation, aligning with IFRS 9 Stage 1.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
