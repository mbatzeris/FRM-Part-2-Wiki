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
| **A1** | **Sign Flip** | Got the magnitude right but direction wrong (e.g., CVA decreases instead of increases when correlation rises) | 0 | — | 2 (Credit), 4 (Liquidity) |
| **A2** | **Swapped Definitions** | Confused paired concepts (CVA↔DVA, WWR↔RWR, netting↔close-out, Q↔P probability) | 0 | — | 2 |
| **A3** | **Formula Component Drop** | Forgot a multiplier (e.g., dropped (1-RR) in Credit VaR, ignored recovery rate in hazard) | 0 | — | All |
| **A4** | **Wrong Regulator / Framework** | Attributed a rule to the wrong body (e.g., OCC vs BCBS, ISDA vs SFTR) | 0 | — | 3 (OpRisk), 4 |
| **A5** | **Q vs P confusion** | Used real-world PD for pricing, or risk-neutral for stress losses | 0 | — | 2 |
| **A6** | **Unit Confusion** | bp vs %, annual vs monthly, % vs fraction | 0 | — | All |
| **A7** | **Basel Threshold Miss** | Wrong trigger number (e.g., 2.5% buffer vs 2% countercyclical; 4.5% vs 6% CET1) | 0 | — | 3 |
| **A8** | **Model Choice Mismatch** | Picked wrong model for task (reduced-form for high correlation, historical sim for fat tails) | 0 | — | 1, 2, 5 |
| **A9** | **Time-Horizon Error** | Confused 10-day vs 1-year VaR, or conditional vs unconditional default over N years | 0 | — | 1, 2 |
| **A10** | **Distractor Plausibility Trap** | Picked a "textbook-sounding" wrong answer over the correct one because it recited canonical language | 0 | — | All |
| **A11** | **Vignette Constraint Miss** | Ignored a specific constraint in the question stem (e.g., "assume zero recovery") | 0 | — | All |
| **A12** | **Stale Regulation Trap** | Picked the pre-Basel-III answer when Basel III/IV applies, or vice versa | 0 | — | 3 |

---

## Specific Instance Log

Format: date · question source · LO · your-answer → correct-answer · **archetype** · lesson.

_(No entries yet. Will populate as you drill R30 Module Quiz and subsequent readings.)_

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
| 1 | — | — | Baseline week; no drill yet |

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
