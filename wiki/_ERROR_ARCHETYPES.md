# Error Archetypes — Personal Distractor Decoder

**Purpose:** A running catalog of the specific error patterns YOU make on FRM Part 2 questions. Over time, this becomes the most valuable file in the repo — the decoder for your own brain's blind spots.

**How to use:**
1. After every wrong question, tag the error with an archetype from the table below (or add a new one).
2. Once per week, scan the top 3 archetypes by frequency — those are your distractor vulnerabilities.
3. In the last 6 weeks before exam, read this file end-to-end daily. It's your personal cheat sheet.

---

## Archetype Taxonomy (seed)

| Code | Archetype | Description | Count | Last Seen | Highest Risk Books |
|:--:|:--|:--|:--:|:--:|:--|
| **A1** | **Sign Flip** | Got the magnitude right but direction wrong (e.g., CVA decreases instead of increases when correlation rises) | 9 | 2026-04-20 | 2 (Credit), 4 (Liquidity) |
| **A2** | **Swapped Definitions** | Confused paired concepts (CVA↔DVA, WWR↔RWR, netting↔close-out, Q↔P probability, PD↔WCDR) | 8 | 2026-04-21 | 2 |
| **A3** | **Formula Component Drop** | Forgot a multiplier (e.g., dropped (1-RR) in Credit VaR, ignored recovery rate in hazard) | 3 | 2026-04-20 | All |
| **A4** | **Wrong Regulator / Framework** | Attributed a rule to the wrong body (e.g., OCC vs BCBS, ISDA vs SFTR) | 0 | — | 3 (OpRisk), 4 |
| **A5** | **Q vs P confusion** | Used real-world PD for pricing, or risk-neutral for stress losses | 0 | — | 2 |
| **A6** | **Unit Confusion** | bp vs %, annual vs monthly, % vs fraction | 0 | — | All |
| **A7** | **Basel Threshold Miss** | Wrong trigger number (e.g., 2.5% buffer vs 2% countercyclical; 4.5% vs 6% CET1) | 0 | — | 3 |
| **A8** | **Model Choice Mismatch** | Picked wrong model for task (reduced-form for high correlation, historical sim for fat tails) | 0 | — | 1, 2, 5 |
| **A9** | **Time-Horizon Error** | Confused 10-day vs 1-year VaR, or conditional vs unconditional default over N years | 0 | — | 1, 2 |
| **A10** | **Distractor Plausibility Trap** | Picked a "textbook-sounding" wrong answer over the correct one because it recited canonical language | 1 | 2026-04-19 | All |
| **A11** | **Vignette Constraint Miss** | Ignored a specific constraint in the question stem (e.g., "assume zero recovery", exposure floor at zero, CSA threshold) | 2 | 2026-04-21 | All |
| **A12** | **Stale Regulation Trap** | Picked the pre-Basel-III answer when Basel III/IV applies, or vice versa | 0 | — | 3 |

---

## Specific Instance Log

Format: date · question source · LO · your-answer → correct-answer · **archetype** · lesson.

### 2026-04-19 · Drill Session A, Q1
- **LO:** 30.g
- **Question summary:** Calculate Credit VaR from L, RR, and WCDR.
- **You answered:** Mixed up formula with Unexpected Loss.
- **Correct:** Credit VaR = L × (1 - RR) × WCDR
- **Archetype:** A3 · Formula Component Drop
- **Lesson:** Credit VaR formula is distinct from UL; it requires the LGD `(1-RR)` component.

### 2026-04-19 · Drill Session A, Q3
- **LO:** 30.d
- **Question summary:** Calculate net exposure with two trades (+30M, -10M).
- **You answered:** -20M
- **Correct:** +20M
- **Archetype:** A1 · Sign Flip
- **Lesson:** Positive net exposure means the bank is a creditor. The sign matters.

### 2026-04-19 · Drill Session A, Q4
- **LO:** 30.e
- **Question summary:** Compare structural vs. reduced-form models.
- **You answered:** B (Reduced-form uses hazard rates).
- **Correct:** D (CreditMetrics uses equity correlation).
- **Archetype:** A2 · Swapped Definitions
- **Lesson:** Structural = Asset Value. Reduced-form = Hazard Rate. The definitions were swapped in the options.

### 2026-04-19 · Drill Session A, Q5
- **LO:** 30.b
- **Question summary:** Identify a situation of high exposure when PD is low.
- **You answered:** Wrong-Way Risk
- **Correct:** Right-Way Risk
- **Archetype:** A2 · Swapped Definitions
- **Lesson:** Right-way risk is "good" (high exposure aligns with low PD) and reduces CVA.

### 2026-04-21 · Drill Session J, Q5
- **LO:** 30.d
- **Question summary:** CSA threshold=$10M, MTA=$1M, net MtM=$13M. Collateral posted and residual uncollateralised exposure?
- **You answered:** Collateral $3M ✓, uncollateralised $2M ✗.
- **Correct:** Collateral $3M; uncollateralised = threshold = $10M.
- **Archetype:** A11 · Vignette Constraint Miss
- **Lesson:** Residual uncollateralised exposure always equals the threshold (the band of exposure never covered by collateral). Formula: uncollateralised = min(exposure, threshold).

### 2026-04-21 · Drill Session I, Q2
- **LO:** 30.d
- **Question summary:** Bank claims in bankruptcy under netting: gross positive MtM ($55M) or net ($37M)?
- **You answered:** $55M (sum of positive trades only).
- **Correct:** $37M — under netting, bank files one net claim, not the sum of winning trades.
- **Archetype:** A2 · Swapped Definitions (gross vs net claim)
- **Lesson:** Netting means ONE claim = net MtM. The administrator cannot cherry-pick trades. No netting = $55M claim; with netting = $37M claim.

### 2026-04-20 · Drill Session H, Q2
- **LO:** 30.g
- **Question summary:** Recover WCL from Credit VaR=$22M, EL=$2.2M.
- **You answered:** $19.8M (subtracted EL instead of adding).
- **Correct:** WCL = $22M + $2.2M = $24.2M
- **Archetype:** A1 · Sign Flip (recurring — 4th instance of this exact error)
- **Lesson:** WCL = Credit VaR + EL. Always ADD. WCL is always the largest number — self-check: answer must be > Credit VaR.

### 2026-04-20 · Drill Session H, Q4
- **LO:** 30.g
- **Question summary:** Recovery rate rises from 30% to 50%. What happens to EL, WCL, Credit VaR?
- **You answered:** EL↓, WCL↑, CVaR unchanged.
- **Correct:** All three decrease. LGD = 1−RR appears in all three formulas.
- **Archetype:** A1 · Sign Flip
- **Lesson:** LGD is a common multiplier. RR↑ → LGD↓ → EL↓, WCL↓, Credit VaR↓ all together.

### 2026-04-20 · Drill Session H, Q8
- **LO:** 30.b
- **Question summary:** Oil producer swap (receives fixed, pays floating). Oil collapses. WWR or RWR?
- **You answered:** Wrong-Way Risk; bank exposure rises; producer PD falls.
- **Correct:** Right-Way Risk; bank exposure falls to zero; producer PD rises.
- **Archetype:** A1 + A2 · Sign Flip + Swapped Definitions
- **Lesson:** Bank pays fixed/receives floating. Oil falls → bank MtM negative → zero exposure. Producer PD rises (less revenue). Zero exposure + rising PD = Right-Way (favorable).

### 2026-04-20 · Drill Session H, Q10
- **LO:** 30.g
- **Question summary:** Same WCDR, Portfolio X PD=2% vs Portfolio Y PD=5%. Which has higher Credit VaR?
- **You answered:** Portfolio Y (higher PD = higher Credit VaR).
- **Correct:** Portfolio X. Credit VaR = EAD × LGD × (WCDR − PD). Higher PD → larger subtraction → lower Credit VaR.
- **Archetype:** A1 · Sign Flip
- **Lesson:** PD has a NEGATIVE sign in the Credit VaR formula. Higher PD → lower Credit VaR (holding WCDR constant).

### 2026-04-20 · Drill Session G, Q1
- **LO:** 30.g
- **Question summary:** Full chain EL/Credit VaR/WCL for $400M portfolio. Recover WCL from Credit VaR.
- **You answered:** WCL = Credit VaR − EL (subtracted instead of added, gave $18M).
- **Correct:** WCL = Credit VaR + EL = $23.4M + $5.4M = $28.8M
- **Archetype:** A1 · Sign Flip (recurring — 3rd instance of this exact error)
- **Lesson:** Rearranging Credit VaR = WCL − EL gives WCL = Credit VaR + EL. Always ADD EL back.

### 2026-04-20 · Drill Session G, Q2
- **LO:** 30.d
- **Question summary:** Net exposure under netting: Equity Swap −30M, FX −12M, IRS +8M.
- **You answered:** −34M (correct arithmetic, but missed exposure floor).
- **Correct:** max(−34M, 0) = $0. Bank owes counterparty; credit exposure is zero.
- **Archetype:** A11 · Vignette Constraint Miss
- **Lesson:** Credit exposure = max(Net MtM, 0). Negative net = bank is a debtor = zero credit exposure.

### 2026-04-20 · Drill Session G, Q5
- **LO:** 30.g
- **Question summary:** Which portfolio has higher Credit VaR — LGD=40% or LGD=60%?
- **You answered:** Portfolio X (LGD=40%) — said smaller LGD = higher Credit VaR.
- **Correct:** Portfolio Y (LGD=60%) — higher LGD = more loss per default = higher Credit VaR.
- **Archetype:** A1 · Sign Flip
- **Lesson:** LGD ↑ → Credit VaR ↑. Higher LGD = lower recovery = more loss. Direction: LGD and Credit VaR move together.

### 2026-04-20 · 30.g Deep Dive, Q1
- **LO:** 30.g
- **Question summary:** Recall formulas for WCL, Credit VaR, and EL.
- **You answered:** WCL = LGD × PD × WCL (circular, used PD instead of WCDR).
- **Correct:** WCL = EAD × WCDR × LGD
- **Archetype:** A2 · Swapped Definitions
- **Lesson:** WCL and EL are identical formulas — the ONLY difference is PD (EL) vs WCDR (WCL).

### 2026-04-20 · 30.g Deep Dive, Q3
- **LO:** 30.g
- **Question summary:** Which metric determines capital requirement — WCL or Credit VaR?
- **You answered:** WCL ($35M).
- **Correct:** Credit VaR ($30M) — the unexpected portion above EL.
- **Archetype:** A2 · Swapped Definitions
- **Lesson:** EL is covered by pricing/provisions. Capital covers Credit VaR (= WCL − EL) only.

### 2026-04-20 · 30.g Deep Dive, Q4
- **LO:** 30.g
- **Question summary:** Reverse-engineer EAD from Credit VaR=$18M, EL=$2M, LGD=60%, WCDR=10%.
- **You answered:** $266.67M (subtracted EL from Credit VaR instead of adding).
- **Correct:** WCL = Credit VaR + EL = $20M → EAD = $20M / 0.06 = $333.33M
- **Archetype:** A1 · Sign Flip
- **Lesson:** To recover WCL from Credit VaR, always ADD EL back. Credit VaR = WCL − EL ⇒ WCL = Credit VaR + EL.

### 2026-04-20 · Drill Session E, Q1
- **LO:** 30.g
- **Question summary:** Calculate Credit VaR (unexpected portion) from L=200M, LGD=55%, WCDR=15%, EL=3M.
- **You answered:** $16.5M (WCL only, did not subtract EL).
- **Correct:** $16.5M − $3M = $13.5M
- **Archetype:** A3 · Formula Component Drop
- **Lesson:** When the question asks for Credit VaR as the ‘unexpected’ portion, always subtract EL from WCL.

### 2026-04-20 · Drill Session E, Q4
- **LO:** 30.d
- **Question summary:** Net exposure under bilateral close-out netting: FX +40M, IRS −15M, CDS −10M.
- **You answered:** +$40M (gross exposure on winning trade only).
- **Correct:** +$40M − $15M − $10M = +$15M
- **Archetype:** A2 · Swapped Definitions
- **Lesson:** Netting collapses all trades into one net claim. Never take only the positive trades.

### 2026-04-19 · Drill Session C, Q1
- **LO:** 30.g
- **Question summary:** Calculate Credit VaR from L, RR, and WCDR.
- **You answered:** 240M
- **Correct:** 36M
- **Archetype:** A3 · Formula Component Drop
- **Lesson:** Reinforces the need to always include the LGD `(1-RR)` term. A large portfolio value can make the error seem bigger.

### 2026-04-19 · Drill Session C, Q4
- **LO:** 30.b
- **Question summary:** Impact of a positively correlated new trade on CVA and DVA.
- **You answered:** CVA increases, DVA decreases.
- **Correct:** Both increase.
- **Archetype:** A2 · Swapped Definitions
- **Lesson:** CVA and DVA move in the same direction with respect to correlation changes.

### 2026-04-19 · Drill Session C, Q5
- **LO:** 30.f
- **Question summary:** Identify the firm-specific shock in the Gaussian copula conditional probability formula.
- **You answered:** A) N⁻¹(Q(T))
- **Correct:** D) The term is not explicitly shown.
- **Archetype:** A10 · Distractor Plausibility Trap
- **Lesson:** The conditional formula integrates out the specific shock `Zᵢ`. N⁻¹(Q(T)) is the unconditional threshold, a common distractor.

### 2026-04-19 · Drill Session B, Q2
- **LO:** Part 1 Quant
- **Question summary:** Calculate 95% VaR for a portfolio with non-zero mean.
- **You answered:** Used `+` instead of `-` in the formula.
- **Correct:** VaR = [μ - (z × σ)] × V
- **Archetype:** A1 · Sign Flip
- **Lesson:** VaR is a loss, so for normal distributions, always move left from the mean (`μ - zσ`).

### Template for new entry

```markdown
### {YYYY-MM-DD} · {AnalystPrep Q# or Schweser Module X.Y}
- **LO:** {e.g., 30.f}
- **Question summary:** {one line}
- **You answered:** {A/B/C/D}
- **Correct:** {A/B/C/D}
- **Archetype:** A{X} · {name}
- **Lesson:** {one-sentence takeaway, e.g., "The copula transforms TIMES-TO-DEFAULT, not PDs."}
- **Added to:** R{N} §5 Ambiguity Traps ✅ / not yet
```

---

## Weekly Aggregate (auto-refresh every Sunday)

| Week | Top Archetype | Count | Action Taken |
|:--:|:--|:--:|:--|
| 1 (14–20 Apr) | A1 · Sign Flip | 9 | Lesson added to R30 §5; formula mnemonic drilled in Sessions G, H |
| 2 (21–27 Apr) | — | — | First R31 drill session pending |

---

## The Decoder Rules (built from your pattern over time)

_(This section becomes your personalised last-mile cheat sheet. Populate as patterns emerge.)_

Examples from past FRM students (will be replaced by your actual patterns):
- "Whenever a question mentions 'market prices already reflect' → risk-neutral PD (Q)."
- "When the stem says 'conservative estimate for capital' → real-world PD (P)."
- "If asked about model computation time → structural is slow, reduced-form is fast."
- "Credit VaR formula: **portfolio × LGD × default-rate percentile** (memorise the phrase, not the letters)."

---

## End-game Use

**Weeks 27-30 (the final month):** Every morning, read the 5 most-recent entries in the Specific Instance Log and the top 3 Archetypes by count. This is faster than re-reading any Schema B file and drills the exact traps you fall for.
