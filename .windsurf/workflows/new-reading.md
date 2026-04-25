---
description: Convert an FRM reading chapter (from Schweser PDF) into a Schema B markdown file
---

# /new-reading — Reading Conversion Pipeline

Use this workflow every time you start a new reading. The output is a single `.md` file in the same format as `@c:\Users\user\Documents\FRM 2\wiki\Book 2 - Credit Risk\R30_Credit_Risk.md` (the gold standard).

---

## Inputs Required

1. **Reading number** (e.g., `R30`, `R42`).
2. **Book number** (1-5) and the corresponding PDF at `wiki/Book N - {Name}/FRM 2026 Part II Book N.pdf`.
3. **Target output path** — `wiki/Book N - {Name}/R{N}_{short_title}.md`.

---

## Step 1 — Extract the reading via Gemini direct-PDF

Gemini reads the PDF as a vision-aware LLM, preserving formulas as LaTeX. This is the single source of truth for chapter content.

```powershell
.venv-gemini\Scripts\python.exe scripts\extract_via_gemini.py --book {B} --reading {N} --output raw
```

Output: `wiki/Book {B} - {Name}/R{N}.raw.gemini.md` (gitignored). Contains:
- All section headings (MODULE N.X, LO N.x)
- Display formulas as `$$...$$` LaTeX blocks
- Inline formulas as `$...$`
- Tables as Markdown tables
- Figure captions + faithful descriptions
- Module Quiz questions + answer key

Record from the raw output:
- **Module headers** and **learning objectives** order
- **Formulas** — every `$$...$$` block is a candidate proposition source
- **Tables and figures** — quote numerical data verbatim into the Schema B
- **Module Quiz** — verbatim, including answer key

## Step 2 — Build propositions

**Rule:** one proposition per LO (minimum). If an LO contains two dense sub-concepts, split into two.

For each proposition:
- Start with **bold topic name + `(LO {N}.{x})`**.
- One paragraph of the core statement, including any formula in Unicode math (`λ ≈ s / (1 − R)`, not LaTeX).
- Append `*Intuition: {vivid one-sentence analogy}.*`
- Pick the canonical tag: `[THE]` / `[REG]` / `[OPS]` / `[ECO]`.
- Exam Dominance: rate Very High / High / Medium / Low with a one-phrase reason.
- Trigger Phrase: 2-5 quoted keywords or phrases the exam would use.

## Step 3 — Constraint stress-test

Pull 3-8 rows from:
- Numerical examples inside the reading (e.g., Schweser's worked examples).
- Module Quiz problems (the answer key tells you the "Answer Shift").
- The "if-this-were-different" thought experiments in the narrative.

Format each row: `P{n} ({topic}) | {flip} | {answer}`.

## Step 4 — Dependency & Noise Map

- **Signal:** 3-5 bullets capturing the *distinctions* that matter (X vs Y pairs, directional rules, formula components).
- **Noise:** 3-8 bullets of plausible-but-wrong statements with explicit corrections (these become exam distractors).
- **Tensions:** 1-2 bullets with two canonical tags on either side. Draw from the reading's real-world tradeoffs (e.g., `[REG] vs [OPS]`).

## Step 5 — Directional Intuition

5-8 bulleted arrows showing what rises/falls when an input changes. Always use Unicode arrows (↑ ↓ →), never LaTeX.

## Step 6 — Ambiguity Traps

8-14 bullets covering:
- Swapped definitions (A vs B) with a clarifying tell.
- Formula mnemonics.
- Sign-flip traps.
- Regulator/framework mappings.
- "{A} ≠ {B}" clarifications.

## Step 7 — §9 Checklist Verification

Before committing, verify all 16 items:

1. Title uses em-dash `—` (not hyphen `-`).
2. Exam Priority has emoji (🔴 / 🟡 / 🟢).
3. Metadata block includes `*Source Material*`, `*Learning Objectives Covered*`, `*Related Readings*`.
4. §1 has the 5-column header.
5. §1 alignment row is exactly `|:---|:---|:---:|:---|:---|`.
6. Proposition IDs are `P1`, `P2`, ... (sequential, no gaps).
7. Every proposition has `*Intuition: ...*` inlined at the end.
8. Tags are canonical only (`[THE]`, `[REG]`, `[OPS]`, `[ECO]`).
9. Exam Dominance format: `{rating} — {reason}`.
10. Trigger Phrase format: comma-separated `"quoted keywords"`.
11. §2 heading + 3-column table + `|:---|:---|:---|` alignment.
12. §3 has Signal / Noise / **Tensions** (Tensions is mandatory).
13. §4 uses Unicode arrows, no LaTeX.
14. §5 has 8+ bullets.
15. Footer contains `**Cross-Domain Linkage:** [Boundary Events](../_boundary_events.md)`.
16. No LaTeX rendering errors — all formulas in Unicode or plain text.

## Step 8 — Update `_boundary_events.md`

After the §9 checklist passes, scan the completed Schema B file for cross-domain linkages:

1. Read **§3 Tensions** — every tension bullet names two canonical tags and a real-world tradeoff. If it references a concept from another reading, it's a boundary link.
2. Read **§5 Ambiguity Traps** — any "A ≠ B" clarifier that involves a concept from a different reading is a boundary link.
3. For each boundary link found, open `wiki/_boundary_events.md` and:
   - **If the concept row already exists:** add R{N} to the Readings column.
   - **If it's new:** append a row to the Cross-Domain Links table:
     ```
     | {Concept} | R{N}[, R{prev}] | [{Tag1}] vs [{Tag2}]: {one-sentence tension} |
     ```
4. Check **§Boundary Scenarios** — if the reading introduces a cross-domain event chain (e.g., credit event → collateral collapse → liquidity drain), add a row to that section.

**Mandatory linkage checks per reading:**
- Does the reading reuse a formula or model from a prior reading? → Link them.
- Does the reading take a different REG or ECO position on a shared concept? → Link them with the tension.
- Does the reading contain a scenario where two risk types interact (Market + Credit, Credit + Liquidity, Ops + Liquidity)? → Add to Boundary Scenarios.

After updating, add `wiki/_boundary_events.md` to the git staging in Step 10.

---

## Step 9 — Append LOs to `_LO_TRACKER.md`

For each LO covered in the new reading, append a row to the appropriate Book section of `@c:\Users\user\Documents\FRM 2\wiki\_LO_TRACKER.md`.

Row template:
```
| {LO id} | R{N} | {topic, linked to prop Px} | {YYYY-MM-DD} | {YYYY-MM-DD} | 3 | 0/0 | — | 0.28 | 🔴 High |
```

Defaults for new LOs:
- **First Studied / Last Reviewed** = today's date
- **Confidence** = 3 (neutral baseline — user recalibrates in first drill)
- **Qs** = 0/0 until first drill
- **Readiness** = 0.28 (formula-derived baseline: 0.60×0 + 0.30×(3/5) + 0.10×1 = 0.28 — Acc=0, Conf=3, recency=1)
- **Priority** = 🔴 High (per Priority Engine rule "new LO with 0 questions"; needs first drill within 3 days). Note: Phase will also be 1 because 0.28 < 0.50, but that's a separate determination (Priority = when to drill; Phase = how to drill).

After appending: update the aggregate snapshot at the top of `_LO_TRACKER.md` (LOs tracked count).

## Step 10 — Append to event log and commit

Append a row to `wiki/_EVENT_LOG.md`:
```
| {next #} | {YYYY-MM-DD} | READING | R{N} — {Short Title} | {n} LOs added ({LO id list}) · boundary events updated | ✅ Complete |
```

```powershell
git add "wiki/Book N - {Name}/R{N}_{short_title}.md" "wiki/_LO_TRACKER.md" "wiki/_boundary_events.md" "wiki/_EVENT_LOG.md"
git commit -m "[READING] R{N} converted; {n} LOs added; boundary events updated"
git push
```

> **Commit format:** `[TYPE] Description` where TYPE = `READING` / `DRILL` / `SYSTEM` / `REVIEW` / `FIX`

---

# LLM Master Prompt (Copy-Paste)

Use the prompt below when calling an external LLM (Claude Sonnet 4.5 recommended). Paste it along with:
1. The extracted chapter text (from Step 2).
2. The contents of `wiki/_TEMPLATE_Reading.md` as a reference.
3. The contents of `wiki/Book 2 - Credit Risk/R30_Credit_Risk.md` as a gold-standard example.

```
You are converting an FRM Part II Schweser reading into a Boole Scaffold Schema B markdown file.

RULES (non-negotiable):
1. One proposition per Learning Objective. If an LO has two dense sub-concepts (e.g., a formula + a Q-vs-P distinction), split into two propositions.
2. Every proposition MUST include: bold topic name + LO tag, one-paragraph content with Unicode-math formulas, an *Intuition: ...* one-liner, a canonical tag ([THE] / [REG] / [OPS] / [ECO]), Exam Dominance rating + reason, and 2-5 Trigger Phrases.
3. Section 2 (Constraint Stress-Test) MUST contain 3-8 rows drawn from the reading's worked examples, Module Quiz questions, and answer key. Include the numerical answer in the "Answer Shift" column.
4. Section 3 MUST have three sub-sections in order: Signal, Noise (with explicit "wrong" corrections), Tensions (using two canonical tags).
5. Section 4 uses Unicode arrows (↑ ↓ →) only — never LaTeX `\uparrow`.
6. Section 5 contains 8-14 bullets: at least one mnemonic, one sign-trap, one "A ≠ B" clarifier.
7. All math formulas in Unicode or plain text. Never use `\frac`, `\sqrt`, `\Rightarrow`, `$...$`, or `$$...$$`. Acceptable: λ ≈ s / (1 − R), √ρ, N⁻¹, etc.
8. Title format: `# The Boole Scaffold: Reading {N} — {Title}` (em-dash, not hyphen).
9. Exam Priority with emoji: 🔴 High (3-4 questions) / 🟡 Medium (1-2 questions) / 🟢 Low (0-1 questions).
10. Zero hallucination: every formula, number, and claim must be traceable to the provided chapter text.

INPUTS:
- Chapter text: {paste extracted text between READING N and READING N+1 here}
- Template skeleton: {paste contents of wiki/_TEMPLATE_Reading.md here}
- Gold-standard example: {paste contents of wiki/Book 2 - Credit Risk/R30_Credit_Risk.md here}

OUTPUT:
- A single markdown file that passes all 16 checklist items in the template's §9 verification.
- No preamble, no explanation — just the .md content, starting with `# The Boole Scaffold: Reading ...`.
```

---

# LLM Recommendations (cost × quality for this task)

| Rank | Model | Approx cost/reading | Why |
|:--:|:--|:--:|:--|
| 🥇 | **Claude Sonnet 4.5** | ~$0.14 | Strictest schema adherence, zero hallucination in tests, faithful to source finance text. Best for production. |
| 🥈 | **Gemini 2.5 Pro** | ~$0.05 | 1M-token context lets you paste whole PDF. Cheapest top-tier. Occasionally paraphrases — needs stricter prompt. |
| 🥉 | GPT-5 (reasoning) | ~$0.10 | Strong LO decomposition but cost spikes with reasoning tokens. |
| 4 | DeepSeek V3.2 | ~$0.01 | 10× cheaper; first-draft only — needs human formula verification. |
| 5 | Claude Haiku 4.5 | ~$0.03 | Schema-compliant but shallower intuitions. |

**Production recommendation:** Claude Sonnet 4.5. Total cost for the remaining ~106 readings ≈ $15.

**Verification step regardless of model:** Run the §9 checklist (Step 8 above) manually on every output. The checklist catches the ~5% of cases where any model drifts.
