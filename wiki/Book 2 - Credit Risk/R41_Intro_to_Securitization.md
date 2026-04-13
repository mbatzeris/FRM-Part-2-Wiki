# The Boole Scaffold: Reading 41 - An Introduction to Securitization

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R25 — Retail Credit Risk](R25_Retail_Credit_Risk.md), [R40 — Structured Credit Risk](R40_Structured_Credit_Risk.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **The Securitization Motive:** Banks securitize assets to achieve regulatory capital relief, access cheaper funding, manage concentrations, and transfer risk to third parties via an SPV (Special Purpose Vehicle). | `[ECO]` | High — The fundamental "why" of securitization. | "regulatory arbitrage," "funding costs," "SPV" |
| P2 | **True Sale & Bankruptcy Remoteness:** The transfer of assets to the SPV must be a "true sale." If the originating bank goes bankrupt, its creditors cannot seize the SPV's assets. | `[REG]` | Very High — The legal backbone of securitization safety. | "bankruptcy remote," "true sale," "originator default" |
| P3 | **Credit Enhancement:** Internal (subordination, overcollateralization, excess spread) and External (monoline insurance, letter of credit) methods used to support the high credit ratings of senior tranches. | `[OPS]` | High — Distinguishing between mechanical structures and third-party guarantees. | "internal credit enhancement," "overcollateralization" |
| P4 | **Prepayment Risk vs Default Risk:** MBS (Mortgage-Backed Securities) face prepayments (interest rates down) and defaults (house prices down). Both disrupt expected cash flows. | `[THE]` | Medium — Distinguishes retail ABS from corporate CDOs. | "contraction risk," "extension risk," "WALA" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P2 (True Sale) | The originator retains a legal right to repurchase troubled assets from the SPV at par. | This violates the **True Sale** criteria. Regulators will declare it a secured loan, denying capital relief and exposing investors to the originator's bankruptcy risk. |
| P3 (Overcollateralization) | The pool generated $1M in interest, paid $800k in coupons, and absorbed $300k in default losses in month one. | The **Excess Spread** ($200k) is insufficient to cover the losses. The structure must now trap cash flows (hyper-amortization) or begin writing down the lowest subordinated tranche. |
| P4 (Prepayment) | Interest rates plummet across the economy. | Investors suffer **Contraction Risk**. Underlying borrowers refinance, returning principal early when reinvestment rates are terrible, lowering the SPV's yield. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Whether credit enhancement is Internal (structural rules) or External (third-party counterparty risk).
- The legal isolation of the SPV.
- The difference between Excess Spread (interest difference) and Overcollateralization (principal difference).

**Noise (distractors):**
- The original loan-to-value (LTV) ratios of the mortgages when the question focuses purely on the SPV's legal structure.
- Details of the originator's overall corporate capital structure.

**Tensions:**
- **[REG] vs [ECO]:** Originators use securitization for `[REG]` capital relief, but they often retain the equity tranche or provide liquidity lines to the SPV. `[ECO]`nomically, the originating bank still holds the most volatile tail risk (the "skin in the game" tension).

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| Excess Spread | Asset Yields ↑ / Tranche Coupons ↓ → Excess Spread ↑ | Confusing Excess Spread (Yield mismatch) with Overcollateralization (Principal amount mismatch). |
| Prepayment Speeds (CPR/PSA) | Interest Rates ↓ → Prepayments ↑ | Assuming prepayments behave linearly. They exhibit burnout (people who want to refinance do it early, then the pool rate slows down regardless of rates). |


## 5. Ambiguity Traps (Anti-Decoder)
- **SPV Bankruptcy Remoteness:** The SPV is legally isolated from the originator. If the originator goes bankrupt, the SPV's assets are NOT part of the bankruptcy estate. This is the entire point of securitization.
- **True Sale vs. Synthetic:** In a true sale, the originator transfers ownership of the assets. In a synthetic, the originator retains the assets but transfers credit risk via CDS. The balance sheet treatment differs dramatically.
- **Overcollateralization vs. Subordination:** Both provide credit enhancement. OC = more assets than liabilities in the SPV. Subordination = junior tranches absorb losses first. They can coexist.
- **FRTB Treatment:** Under FRTB, securitized products MUST use the Standardized Approach — internal models are prohibited. This is a bright-line regulatory rule.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
