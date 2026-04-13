# The Boole Scaffold: Reading 19 - Fundamentals of Credit Risk

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:*
*Related Readings: [R21 — Credit Risk Management](R21_Credit_Risk_Management.md), [R23 — Credit Risk Modeling](R23_Intro_to_Credit_Risk_Modeling.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Credit Risk vs Default vs Insolvency:** Credit risk is the probability of loss from failure to honor obligations. Insolvency means liabilities > assets (negative equity). Default is failure to meet contractual obligations. Bankruptcy is a legal protection procedure. | `[THE]` | High — Distinguishing between these states is heavily tested conceptually. | "company continues to operate despite negative equity" |
| P2 | **Derivative Credit Risk:** The largest global source of credit exposure by notional value is OTC derivatives. | `[ECO]` | Medium — Used as background context for CVA/DVA risk pricing. | "source of credit exposure," "notional amounts" |
| P3 | **Hedge Fund Risk Tolerance:** Unlike asset managers, hedge funds may actively short-sell or buy distressed debt, viewing default as an investment opportunity rather than a risk to avoid. | `[OPS]` | Low — Tests the difference in operational mandates between counterparties. | "long/short distressed debt," "hedge fund mandate" |
| P4 | **Corporate Credit Risk Mitigation:** Corporations mitigate receivables risk via factoring, insurance, or documentary credit. They do *not* manage this natively through statistical provisioning like banks do. | `[OPS]` | Medium — Focuses on non-financial firm risk transfer. | "mitigate accounts receivable," "corporate credit policy" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (Insolvency/Default) | The vignette states: "A firm has $320M in debt, $280M in assets, but continues paying its coupons on time." | The firm is **insolvent** but **NOT in default**. The trap is assuming negative equity automatically triggers a legal default. |
| P2 (Derivatives) | The question asks for the primary source of credit exposure for *domestic U.S. financial companies* rather than global markets. | Shifts from Derivatives to **Loans/Corporate Obligations**. |
| P4 (Corporate Receivables) | The stem asks about mitigating credit risk for an *unverifiable, small* corporate customer rather than a large blue-chip. | The corporation must use **factoring or documentary credit (guarantees)** rather than relying on internal credit scores. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Distinguishing between Insolvency (balance sheet math) and Default (cash flow action).
- identifying the types of transactions generating credit risk (Lending, Leases, Receivables, Prepayments, Derivatives, Contingent claims).
- The *motivation* for managing credit risk (Survival, Profitability, Return on Equity optimization).

**Noise (distractors):**
- Asset size or complexity when the core question is about willingness/ability to pay.
- Short-term stock market fluctuations in a question strictly about insolvency (which requires evaluating the balance sheet liabilities vs assets).

**Tensions:**
- **[THE] vs [REG]**: A firm can be theoretically bankrupt (insolvent) but continue to operate perfectly under regulatory and operational dimensions until a cash flow failure (default) forces legal bankruptcy.



## 4. Directional Intuition
- **Leverage (Debt/Equity) ↑ → Insolvency Probability ↑ → Credit Risk ↑:** Higher leverage means a smaller equity cushion, making the balance sheet more fragile to asset value drops.
- **Cash Flow Volatility ↑ → Default Probability ↑:** Even a solvent firm can default if its cash flows are too erratic to meet scheduled payments.
- **Credit Risk Mitigation (Factoring/Insurance) ↑ → Residual Receivables Risk ↓:** Transferring receivables to a factor eliminates the idiosyncratic risk of individual customers.

## 5. Ambiguity Traps (Anti-Decoder)
- **Insolvency ≠ Default:** A company with negative equity (Liabilities > Assets) can continue operating and paying coupons for years. Insolvency is a balance sheet state; default is a cash flow event. GARP loves this distinction.
- **Bankruptcy ≠ Default:** Bankruptcy is a legal court process — a company may default without filing for bankruptcy, and may file for bankruptcy protection while still current on payments (Chapter 11).
- **"Largest source of credit exposure":** Globally = OTC Derivatives (by notional). For a typical US commercial bank = Loans. The scope qualifier in the stem flips the answer.
- **Hedge Funds as Creditors:** Don't assume all creditors want to avoid default. Distressed debt hedge funds actively buy defaulted obligations at a discount, hoping for recovery > purchase price.


## 4. Directional Intuition
- **Leverage (Debt/Equity) ↑ → Insolvency Probability ↑ → Credit Risk ↑:** Higher leverage means a smaller equity cushion, making the balance sheet more fragile to asset value drops.
- **Cash Flow Volatility ↑ → Default Probability ↑:** Even a solvent firm can default if its cash flows are too erratic to meet scheduled payments.
- **Credit Risk Mitigation (Factoring/Insurance) ↑ → Residual Receivables Risk ↓:** Transferring receivables to a factor eliminates the idiosyncratic risk of individual customers.

## 5. Ambiguity Traps (Anti-Decoder)
- **Insolvency ≠ Default:** A company with negative equity (Liabilities > Assets) can continue operating and paying coupons for years. Insolvency is a balance sheet state; default is a cash flow event. GARP loves this distinction.
- **Bankruptcy ≠ Default:** Bankruptcy is a legal court process — a company may default without filing for bankruptcy, and may file for bankruptcy protection while still current on payments (Chapter 11).
- **"Largest source of credit exposure":** Globally = OTC Derivatives (by notional). For a typical US commercial bank = Loans. The scope qualifier in the stem flips the answer.
- **Hedge Funds as Creditors:** Don't assume all creditors want to avoid default. Distressed debt hedge funds actively buy defaulted obligations at a discount, hoping for recovery > purchase price.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
