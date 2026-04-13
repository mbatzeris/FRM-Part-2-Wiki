# The Boole Scaffold: Reading 24 - Credit Scoring and Rating

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R23 — Credit Risk Modeling](R23_Intro_to_Credit_Risk_Modeling.md), [R27 — Estimating Default Probabilities](R27_Estimating_Default_Probabilities.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Rating Systems:** Point-in-Time (PiT) ratings estimate current default risk over a short horizon. Through-the-Cycle (TTC) ratings estimate risk over a full economic cycle, remaining stable during short-term fluctuations. | `[THE]` | Absolute Dominance — The defining difference in rating agency methodologies. | "Through-the-cycle," "Point-in-time," "cycle fluctuations" |
| P2 | **Agency Ratings vs Internal Models:** External rating agencies (Moody's, S&P) heavily use TTC to prioritize stability and avoid procyclicality. Bank internal models often tilt PiT for accurate current pricing. | `[OPS]` | High — Explains the tension between internal risk and external ratings. | "External rating agency," "upgrade/downgrade stability" |
| P3 | **Altman Z-Score:** A classic multiple-discriminant analysis model. Higher score = lower probability of default. Z < 1.8 indicates distress; Z > 3.0 indicates safe zone. | `[THE]` | Medium — Historical significance but often tested on what factors it ignores (e.g., market volatility). | "Altman Z-score," "discriminant analysis" |
| P4 | **Type I vs Type II Errors:** Type I error = failing to identify a default (classifying a bad borrower as good). Type II error = falsely identifying a default (classifying a good borrower as bad). | `[THE]` | High — The fundamental trade-off in credit scoring models. | "false positive," "Type I error" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P1 (PiT vs TTC) | A mild recession hits, but a firm's long-term competitive position is unchanged. | A **PiT rating gets downgraded**, while a **TTC rating remains unchanged**, providing stability but lagging the economic reality. |
| P2 (Agency Ratings) | The stem asks about calculating short-term Economic Capital for a trading desk. | Using TTC external ratings will **underestimate** current risk in a downturn. The desk should use **PiT models**. |
| P4 (Type I vs II) | The bank's risk appetite becomes extremely conservative and rejects almost all marginal borrowers. | **Type II errors skyrocket (lost revenue)** while Type I errors drop. The bank loses profitable business to avoid defaults. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Whether the model/rating is explicitly PiT or TTC.
- The tradeoff between Type I errors (capital loss) and Type II errors (opportunity cost).
- Objective inputs (financial ratios) vs subjective inputs (management quality in rating agency committees).

**Noise (distractors):**
- Exact formulae for Altman Z-score weights (you rarely calculate it, you just apply the threshold or critique the inputs).
- Short-term stock price fluctuations for a TTC rating — rating agencies filter this out.

**Tensions:**
- **[THE] vs [OPS]:** `[THE]`oretically, PiT is the most accurate reflection of current PD. In `[OPS]` practice, rating agencies use TTC because investors detest rating volatility (downgrading forces fire sales).

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| Type I vs Type II Tradeoff | Model strictness ↑ → Type I ↓ but Type II ↑ | Confusing which error causes capital loss (Type I) vs revenue loss (Type II). |
| Altman Z-score | Score ↑ → PD ↓ | Assuming the Z-score maps directly to a continuous true probability rather than a categorical safe/distress bin. |


## 5. Ambiguity Traps (Anti-Decoder)
- **Accuracy Ratio (AR) = 2 × AUC - 1:** A perfect model has AR = 1; a random model has AR = 0. Don't confuse AR with the ROC curve itself.
- **Through-the-Cycle (TTC) vs. Point-in-Time (PIT):** Rating agencies use TTC (stable but slow). Internal bank models often use PIT (volatile but accurate). GARP tests which is appropriate for pricing (PIT) vs. capital (TTC).
- **Type I vs. Type II Errors:** Type I = Rejecting a good borrower (lost revenue). Type II = Accepting a bad borrower (credit loss). Banks generally care more about Type II.

## 5. Ambiguity Traps (Anti-Decoder)
- **Accuracy Ratio (AR) = 2 × AUC - 1:** A perfect model has AR = 1; a random model has AR = 0. Don't confuse AR with the ROC curve itself.
- **Through-the-Cycle (TTC) vs. Point-in-Time (PIT):** Rating agencies use TTC (stable but slow). Internal bank models often use PIT (volatile but accurate). GARP tests which is appropriate for pricing (PIT) vs. capital (TTC).
- **Type I vs. Type II Errors:** Type I = Rejecting a good borrower (lost revenue). Type II = Accepting a bad borrower (credit loss). Banks generally care more about Type II.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
