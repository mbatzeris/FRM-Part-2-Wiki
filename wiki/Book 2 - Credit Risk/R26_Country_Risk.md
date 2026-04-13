# The Boole Scaffold: Reading 26 - Country Risk

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R27 — Estimating Default Probabilities](R27_Estimating_Default_Probabilities.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Sovereign Default Risk:** The risk that a foreign government refuses or is unable to service its debt. Unlike corporate debt, there is no international bankruptcy court to enforce asset seizure. | `[THE]` | High — The fundamental distinction between sovereign and corporate risk. | "sovereign debt," "willingness to pay" |
| P2 | **Country Risk vs Sovereign Risk:** Country Risk is broader—it includes sovereign default, but also transfer/convertibility risk (capital controls) and macro shocks affecting private corporate debt in that country. | `[ECO]` | High — Distinguishing the umbrella term from the specific government default. | "transfer risk," "capital controls," "expropriation" |
| P3 | **Local vs Hard Currency Debt:** Governments rarely default on local currency debt (they can print money, causing inflation). Defaults occur primarily on hard currency debt (e.g., USD, EUR). | `[ECO]` | Very High — A classic GARP distractor test. | "hard currency," "domestic currency bond" |
| P4 | **Sovereign CDS:** The primary market instrument reflecting sovereign default probabilities. Widening spreads indicate deteriorating creditworthiness. | `[OPS]` | Medium — Traded indicator of stress. | "sovereign spread," "CDS premium" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (Sovereign vs Corp) | The country defaults. A foreign bank attempts to liquidate the country's domestic infrastructure assets to recover funds. | This is **impossible**. Sovereigns have immunity; recovery relies entirely on geopolitical renegotiations (e.g., Paris Club), not liquidation. |
| P2 (Country vs Sovereign) | A corporate entity in Country X is highly profitable with zero debt, but its host government blocks foreign exchange transfers. | The corporation **defaults on foreign obligations** due to Transfer Risk (a subset of Country Risk), despite having no underlying corporate credit risk! |
| P3 (Local vs Hard) | A country faces a massive deficit but issues debt solely in its own sovereign currency. | The probability of nominal default is **near zero**. The risk is absorbed via **inflation/currency devaluation**, destroying real investor returns without a formal default event. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Denomination of the debt (Local vs Hard/Foreign currency).
- Ability to pay (reserves, tax base) vs Willingness to pay (political regime).
- The difference between Sovereign Default (Gov't fails) and Transfer Risk (Gov't blocks private capital).

**Noise (distractors):**
- Strict corporate bankruptcy procedures (Chapter 11 equivalents) when discussing sovereign recovery rates.
- Domestic inflation rates when the question specifically asks about the probability of a formal default on local debt.

**Tensions:**
- **[ECO] vs [REG]:** In `[REG]` (Basel), domestic sovereign debt is often assigned a 0% risk weight. In `[ECO]`, history shows sovereigns can and do default (or drastically devalue), making the 0% weight a fiction that encourages bank concentration in sovereign bonds (the "doom loop").

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| Sovereign CDS Spread | Sovereign Distress ↑ → Spread ↑ | Confusing country risk (macro) with sovereign risk (government specifically). |
| Debt-to-GDP | Debt/GDP ↑ → Default Probability (usually) ↑ | Assuming a strict theoretical cutoff (e.g., >100% means default) — willingness to pay and reserve currency status (like US/Japan) override mechanical rules. |


## 5. Ambiguity Traps (Anti-Decoder)
- **Sovereign Default ≠ Country Risk:** Sovereign default is the government failing to pay. Country risk includes transfer risk (capital controls), political risk, and macroeconomic risk — it's broader than just sovereign default.
- **Transfer Risk:** Even if a borrower is willing and able to pay in local currency, capital controls may prevent conversion to the lender's currency. This is transfer risk, not credit risk.
- **Composite Risk Ratings:** Country risk scores blend quantitative (GDP, debt/GDP) and qualitative (political stability) measures. Don't assume the quantitative score alone determines the rating.

## 5. Ambiguity Traps (Anti-Decoder)
- **Sovereign Default ≠ Country Risk:** Sovereign default is the government failing to pay. Country risk includes transfer risk (capital controls), political risk, and macroeconomic risk — it's broader than just sovereign default.
- **Transfer Risk:** Even if a borrower is willing and able to pay in local currency, capital controls may prevent conversion to the lender's currency. This is transfer risk, not credit risk.
- **Composite Risk Ratings:** Country risk scores blend quantitative (GDP, debt/GDP) and qualitative (political stability) measures. Don't assume the quantitative score alone determines the rating.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
