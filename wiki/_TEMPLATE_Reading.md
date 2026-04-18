# The Boole Scaffold: Reading {N} — {Title}

**Exam Priority:** {🔴 High / 🟡 Medium / 🟢 Low} ({X-Y} questions)

*Source Material: FRM 2026 Part II Book {B} · {Primary Author/Source Chapter}*
*Learning Objectives Covered: {N}.a, {N}.b, {N}.c, ...*
*Related Readings: [R{prev} — {prev title}](R{prev}_Xxx.md), [R{next} — {next title}](R{next}_Xxx.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|:---|:---|:---:|:---|:---|
| P1 | **{Concept name} (LO {N}.{x}):** {One-paragraph statement. Include the key formula in Unicode math (e.g., λ ≈ s / (1 − R)), any numerical thresholds, and the canonical definitions.} *Intuition: {One-sentence plain-language gloss using a vivid analogy.}* | `[THE]` / `[REG]` / `[OPS]` / `[ECO]` | {Very High / High / Medium / Low} — {one-phrase rationale}. | "{keyword 1}," "{keyword 2}," "{formula name}" |
| P2 | **{Concept}:** ... *Intuition: ...* | `[...]` | ... | "..." |
| P3 | ... | ... | ... | ... |
| P4 | ... | ... | ... | ... |
| P5 | ... | ... | ... | ... |
| P6 | ... | ... | ... | ... |
| P7 | ... | ... | ... | ... |
| P8 | ... | ... | ... | ... |

> **Proposition count rule:** One proposition per LO (minimum). If an LO has two dense sub-concepts, split into two propositions (e.g., PD formula + Q-vs-P → P1 and P2).

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|:---|:---|:---|
| P{n} ({topic}) | {Concrete scenario with specific numbers, e.g., "A 2-year bond yields 190 bp with R=35%"} | {Definite answer with computation shown, e.g., "Hazard rate = 0.0190/0.65 = 2.92%"} |
| P{n} ({topic}) | {What-if phrased as a violation of the rule} | {Consequence of violating it} |
| P{n} ({topic}) | ... | ... |

> **Source for this section:** Schweser "Module Quiz" questions + numerical examples. Use 3-8 rows.

## 3. Dependency & Noise Map

**Signal (these matter):**
- **{Key distinction 1}** → {consequence}.
- **{Formula pair}** — both inputs matter; ignoring {X} is a classic error.
- **{Directional rule}** — {when it holds, when it breaks}.

**Noise (distractors):**
- "{Plausible-but-wrong statement}" — wrong ({correction}).
- "{Swapped definitions}" — wrong ({correction}).
- "{Sign flip}" — wrong ({correction}).

**Tensions:**
- **[{Tag1}] vs [{Tag2}]:** {One-sentence description of the real-world tradeoff between these two lenses, with a concrete example of where the tension shows up.}

> **Tags canonical set:** `[THE]` Theory · `[REG]` Regulation · `[OPS]` Operations · `[ECO]` Economics. Tension rows MUST use two canonical tags on either side (no free-form labels).

## 4. Directional Intuition

- **{Input} ↑ → {Intermediate} ↑ → {Output} ↑:** {One-line mechanism.}
- **{Input} ↑ → {Output} ↓ (counter-intuitive case):** {Why this surprises people.}
- **{Formula sensitivity}:** {What happens at the extremes.}
- ...

> **Format:** 5-8 bullet arrows. Prefer Unicode arrows (↑ ↓ →) over LaTeX.

## 5. Ambiguity Traps (Anti-Decoder)

- **{Trap name}:** {Concept A} vs {Concept B} — {how to tell them apart}.
- **{Formula memorization mnemonic}:** {The phrase to recite, e.g., "portfolio × LGD × default-rate percentile"}.
- **{Sign-flip trap}:** {Which sign goes where and why}.
- **{Regulator/framework mapping}:** {Who cares about what — e.g., "OCC → embedded options; BCBS 2012 → intraday"}.
- ...

> **Target:** 8-14 bullets. Include at least one mnemonic, one sign-trap, and one "{A} ≠ {B}" clarification.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
