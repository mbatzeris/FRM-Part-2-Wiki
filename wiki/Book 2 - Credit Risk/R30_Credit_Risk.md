# The Boole Scaffold: Reading 30 - Credit Risk (Derivatives & Default Correlation)

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R29 — Portfolio Credit Risk](R29_Portfolio_Credit_Risk.md), [R31 — Credit Derivatives](R31_Credit_Derivatives.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Default Correlation (Binomial):** For two firms, default correlation $\rho_{1,2}$ is defined via joint probability: $P(1,2) = PD_1 PD_2 + \rho_{1,2} \sqrt{PD_1(1-PD_1)PD_2(1-PD_2)}$. | `[THE]` | High — The mechanical link between marginal PD and joint PD. | "joint probability of default," "pairwise correlation" |
| P2 | **First-to-Default (FtD) Basket:** A credit derivative that pays out on the *first* default in a basket of names, then terminates. It is highly sensitive to correlation. | `[ECO]` | Very High — Heavily tested because its correlation sensitivity inverts standard intuition. | "first-to-default swap," "basket default swap" |
| P3 | **Correlation Sensitivity in FtD:** As default correlation approaches 1, the FtD swap acts like a single-name CDS on the safest name. As correlation approaches 0, it acts like the sum of all individual CDS spreads. | `[THE]` | Absolute Dominance — The defining trick of basket products. | "correlation increases," "spread of a first-to-default" |
| P4 | **Seniority in Basket Swaps:** Nth-to-default swaps have different risk profiles. The First-to-Default is the equity tranche. The Last-to-Default is the super-senior tranche. | `[OPS]` | Medium — Connects derivatives to securitization logic. | "second-to-default," "Nth-to-default" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P2/P3 (FtD Corr) | An investor is long protection on a First-to-Default basket. The default correlation between the names spikes from 0.2 to 0.8. | The value of the protection **drops massively**. High correlation means they survive or die together. If they die together, you only get paid once! High correlation ruins the "multiple chances to win" feature of the FtD. |
| P1 (Joint PD) | Correlation is zero (independent events). | The joint probability of default is simply **$PD_1 \times PD_2$**. |
| P4 (Nth-to-Default) | An investor buys protection on a Last-to-Default basket. Correlation spikes. | The value of this protection **increases**. High correlation is required to wipe out every single name in the basket to trigger the payout. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- The type of basket (First-to-default vs Second-to-default vs Last-to-default).
- Direction of correlation shift (↑ or ↓).
- Whether the position is buying protection (short risk) or selling protection (long risk).

**Noise (distractors):**
- Recovery rate assumptions when determining the pure *directional* impact of correlation.
- The underlying physical bond coupons (derivatives trade on spreads).

**Tensions:**
- **[ECO] vs Intuition:** Naive intuition says "Correlation ↑ = Risk ↑". This is **FALSE** for First-to-Default protection buyers. Correlation ↑ mathematically means they cluster, reducing the chance of an isolated first default. FtD protection buyers want zero correlation (independent sniper shots).

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| First-to-Default Spread | Correlation ↑ → FtD Spread ↓ | Thinking that systemic risk makes the FtD payout *more* likely. It doesn't; it makes them all default *simultaneously*, wasting your coverage since you only get paid once. |
| Last-to-Default Spread | Correlation ↑ → LtD Spread ↑ | Confusing Nth-to-default ordering. LtD requires joint wipeout, so it **loves** high correlation. |
| Joint Default Max/Min | Correlation = 1 → P(Joint) = min(PD1, PD2) | Assuming P(Joint) can exceed the PD of the safest entity. |


## 5. Ambiguity Traps (Anti-Decoder)
- **Spread Risk vs. Default Risk:** Credit spread movements cause MTM losses even without default. Under FRTB, spread risk is captured in the ES model while jump-to-default is captured by the DRC.
- **Credit Migration Risk:** A downgrade from A to BBB is a credit event that causes MTM losses, even though no default occurred. CreditMetrics captures this; CreditRisk+ does not.
- **Recovery Rate Uncertainty:** LGD is not fixed — recovery rates vary by seniority, collateral, and economic conditions. Stressed LGD in a downturn can be 20-30% lower than historical average.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
