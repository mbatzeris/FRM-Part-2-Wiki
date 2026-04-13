# FRM Part 2 Wiki — Project Evaluation & Recommendations

> Full audit of methodology, implementation quality, structural integrity, and gaps.  
> **Date:** 2026-04-13 · **Scope:** All 107 scaffolds, 4-layer architecture, ops tooling, cross-domain linking.

---

## 1. Architecture Grade: A-

The 4-directory design (`raw/ → system/ → wiki/ → ops/`) is clean and correctly separates concerns:

| Layer | Purpose | Status | Verdict |
|:------|:--------|:-------|:--------|
| `raw/` | Immutable source PDFs + extracted text | 5 books (PDF + MD) present | ✅ Complete |
| `system/` | Prompts, templates, workflow docs | 5 files | ✅ Complete |
| `wiki/` | 107 Boole Scaffolds + 5 book indexes + 1 wiki index + boundary events | 114 files | ✅ Complete |
| `ops/` | Tracker, formulas, drills, error log, calendar, boundary templates | 6 files | ✅ Complete |

**What works well:**
- Clear separation of "engine" (system/) from "output" (wiki/) from "operations" (ops/)
- The `raw/` layer is correctly marked immutable — no editing contamination risk
- The `index.md` root serves as a genuine sitemap with quick-commands

---

## 2. Scaffold Methodology Grade: A

The Boole Scaffold framework is genuinely novel and well-suited for FRM exam preparation. It goes beyond passive summarization by forcing:

1. **Falsification** (Constraint Stress-Tests) — "What flips the answer?" is the single most valuable study drill for GARP-style questions
2. **Signal/Noise separation** (Dependency & Noise Map) — trains the brain to filter vignette distractors
3. **Directional Intuition** — ↑/↓ chains build rapid qualitative reasoning without calculation
4. **Ambiguity Traps** — pre-loading anti-patterns against GARP's specific distractor style

The constraint hierarchy (`[REG] > [APP] > [ECO] > [THE]`) is a legitimate decision-tree for resolving ambiguous multi-framework questions.

---

## 3. Implementation Issues Found

### 3.1 Structural Schema Drift (Severity: HIGH)

> [!WARNING]
> The 107 scaffolds use **two different schemas** depending on when they were built. This is the single biggest problem in the wiki.

The section audit reveals a clear split:

| Schema | Sections Present | Files |
|:-------|:----------------|:------|
| **Schema A** (Early Book 2: R19–R31, R40–R41) | FP, CS, DN, **Exam Dominance**, **Trigger Phrase** | ~13 files |
| **Schema B** (Everything else) | FP, CS, DN, **Directional Intuition**, **Ambiguity Traps** | ~94 files |

**Problem:** Schema A files (R19–R31, R40–R41) are **missing** the `Directional Intuition` section AND the `Ambiguity Traps` section. They have `Exam Dominance` and `Trigger Phrase` columns inside the propositions table instead — which is from the *old* template (`01_BOOLE_SCAFFOLD_TEMPLATE.md`).

Meanwhile, Schema B files have the *evolved* structure with 5 sections (adding Sections 4 and 5) but **lack** the `Exam Dominance` and `Trigger Phrase` columns that the original template specified.

**Implication:** The early Book 2 scaffolds (R19–R31) are weaker study tools — they cannot support directional sensitivity drills or ambiguity pre-loading. The later scaffolds are stronger but lost the trigger-phrase capability.

**One outlier:** R79 (Liquidity Transfer Pricing) is missing the Ambiguity Traps section entirely. It has `[FP,CS,DN,DI]` — the only file in the whole wiki with only 4 sections.

### 3.2 Duplicate / Stale Boundary Events File (Severity: MEDIUM)

> [!IMPORTANT]
> There are now **two** boundary events files:
> - `wiki/_boundary_events.md` — The **new** comprehensive 10-cascade version (164 lines, just built)
> - `ops/09_BOUNDARY_EVENTS.md` — The **older** 5-template version (127 lines, built earlier)

These serve different purposes:
- `wiki/_boundary_events.md` maps *reading-level* cross-silo linkages (structural, reference-grade)
- `ops/09_BOUNDARY_EVENTS.md` provides *vignette-style drill templates* (operational, practice-grade)

But the `index.md` root only references the `ops/` version. The 107 scaffold tags all point to the `wiki/` version. There's no cross-link between them, creating a navigation dead-end.

### 3.3 LO Tracker is Stale (Severity: MEDIUM)

The `ops/04_LO_TRACKER.md` shows **0/60 LOs covered, 0% readiness** across all domains, despite all 107 scaffolds being marked `[✓]` in the book indexes. The tracker has never been updated since creation. This breaks the feedback loop the methodology depends on.

Additionally:
- The tracker lists **60 LOs** across 6 domains, but the wiki has **107 readings**. The LOs are aggregated at a higher level than the scaffolds, but there's no explicit mapping from LO → Reading(s).
- Domain 6 (Current Issues) is listed at 10% weight in the tracker but the wiki `_index.md` doesn't break it out — current issues are embedded inside Book 5.
- The Error Log link in the tracker's weekly checklist points to `file:///c:/Users/user/Documents/credit%20var/07_ERROR_LOG.md` — a **dead path** from an older project directory.

### 3.4 Book 2 Index Says "In Progress" (Severity: LOW)

`wiki/Book 2/_index.md` line 3 reads `## Status: In Progress` — but all 23 readings are marked `[✓]`. Stale status label.

### 3.5 Book 2 Folder Name Inconsistency (Severity: LOW)

All other book folders use the pattern `Book N - Topic Name`:
- `Book 1 - Market Risk`
- `Book 3 - Operational Risk`
- `Book 4 - Liquidity Risk`  
- `Book 5 - Investment Risk`

But Book 2 is just `Book 2` — missing the ` - Credit Risk` suffix. This breaks pattern-matching for any automation or navigation.

### 3.6 Template vs. Reality Mismatch (Severity: LOW)

`system/01_BOOLE_SCAFFOLD_TEMPLATE.md` defines a 3-section template (FP, CS, DN). The actual scaffolds have evolved to 5 sections. The template was never updated to reflect the final schema. Anyone using the template to create new scaffolds would produce incomplete output.

### 3.7 The `system/README.md` File (Severity: LOW)

There's a `README.md` in `system/` (3.3 KB) that I didn't audit in detail, but its existence alongside `03_ANTIGRAVITY_WORKFLOW.md` suggests potential content overlap.

---

## 4. Methodology Gaps

### 4.1 No Learning Objective → Reading Mapping

The LO Tracker (`04_LO_TRACKER.md`) uses 60 aggregated LOs, but there's no explicit table showing which LO maps to which reading(s). For example:
- LO 2.6 "CVA & DVA" presumably maps to R38, but also partially to R33, R37, R39. 
- LO 1.8 "FRTB framework" maps to R18, but FRTB concepts also appear in R1 (ES definition) and R4 (backtesting).

Without this mapping, the tracker can't accurately reflect partial coverage.

### 4.2 No Intra-Book Cross-References

The scaffolds have `Related Readings` links in the early Schema A files (e.g., R19 links to R21 and R23), but Schema B files **do not** include intra-book cross-references. The boundary events file handles *cross-book* links, but within a book (e.g., R35 Margin → R36 Central Clearing → R38 CVA), the dependency chain is invisible.

### 4.3 No Difficulty/Priority Weighting

All 107 readings are treated equally. There's no "exam weight" or "question frequency" annotation on individual scaffolds. GARP's historical exam distribution is uneven — some readings generate 3–4 questions while others generate 0–1. A priority tag would optimize time allocation.

### 4.4 Drill Bank is Thin for the Curriculum Size

45 questions for 107 readings = 0.42 questions per reading. The cross-domain boundary questions (Q41–Q45) are excellent, but the main body only covers ~10 questions per domain. Given the exam is 80 questions, the drill bank should ideally be 2–3x its current size for meaningful coverage.

### 4.5 Formula Engine Covers ~60% of Quantitative Material

The Formula Engine (`05_FORMULA_ENGINE.md`) covers Market Risk, Credit Risk, OpRisk, Liquidity, and Investment Management well, but is missing formulas for:
- EVT (GEV/GPD distributions from R3)
- Copula functions (R10)
- Term structure models (R12–R16) — Vasicek, Ho-Lee, BDT
- SA-CCR PFE add-on detail (R37)
- Mahalanobis distance (R97)
- MPoR scaling for CVA (R38)

---

## 5. Recommendations (Prioritized)

### Priority 1 — Fix Schema Drift (HIGH IMPACT)

Upgrade the 13 Schema A files (R19–R31, R40–R41) to include:
- **Section 4: Directional Intuition** (↑/↓ chains)
- **Section 5: Ambiguity Traps** (Anti-Decoder tips)

Also fix R79 (missing Ambiguity Traps).

Do NOT remove `Exam Dominance` and `Trigger Phrase` from the Schema A proposition tables — these are valuable. Instead, add them to the Schema B files. The ideal "Schema C" scaffold would have all 5 sections AND the two extra columns in the proposition table.

### Priority 2 — Reconcile Boundary Events Files (MEDIUM IMPACT)

Options:
- **Option A (Recommended):** Keep both files but cross-link them. Add a "See also: [Drill Templates](../ops/09_BOUNDARY_EVENTS.md)" link at the bottom of `wiki/_boundary_events.md`, and a "See also: [Structural Linkage Map](../wiki/_boundary_events.md)" link at the top of `ops/09_BOUNDARY_EVENTS.md`. Update `index.md` to reference both.
- **Option B:** Merge them into a single file. Risk: the file becomes very long and mixes structural reference with drill practice.

### Priority 3 — Fix Stale References & Labels (LOW EFFORT, HIGH TRUST)

| Item | Fix |
|:-----|:----|
| Book 2 `_index.md` status | Change "In Progress" → "COMPLETE" |
| Book 2 folder name | Rename to `Book 2 - Credit Risk` |
| Error Log dead link in LO Tracker | Fix path from `credit var` to `FRM 2` |
| LO Tracker scores | Either update to reflect scaffold completion or add a note that scores track *drill* completion, not scaffold completion |
| `01_BOOLE_SCAFFOLD_TEMPLATE.md` | Update to reflect the 5-section Schema B (or ideally the merged Schema C) |

### Priority 4 — Add LO → Reading Mapping Table (MEDIUM IMPACT)

Create a mapping table in `04_LO_TRACKER.md` or a new file `ops/10_LO_READING_MAP.md` showing which readings cover each LO. This enables:
- Accurate progress tracking
- Targeted review when a specific LO is weak
- Boundary event awareness (LOs that span multiple readings are natural cross-domain targets)

### Priority 5 — Add Exam-Weight Tags to Scaffolds (MEDIUM IMPACT)

Add a metadata line to each scaffold indicating estimated exam frequency:
```
**Exam Priority:** 🔴 High (3-4 questions) | 🟡 Medium (1-2 questions) | 🟢 Low (0-1 questions)
```
This could be placed right after the title, before the propositions. Sources: GARP practice exams, Schweser weightings, historical pass/fail topic analysis.

### Priority 6 — Expand Drill Bank (MEDIUM IMPACT, HIGH EFFORT)

Target 2 questions per reading for the high-priority topics (≈80 more questions). Focus on:
- Credit Risk (R28 Credit VaR, R38 CVA, R36 Central Clearing) — consistently high-yield exam topics
- FRTB (R18) — the single highest-weight reading in Book 1
- Liquidity ratios (R66 LCR/NSFR) — formula-heavy and trap-heavy
- Current Issues (R100–R107) — guaranteed 8–10 questions on the exam, currently only 5 drill questions

### Priority 7 — Complete the Formula Engine (LOW IMPACT, LOW EFFORT)

Add the missing formulas identified in §4.5. Maintain the existing format (formula → variable table → exam trap note).

### Priority 8 — Add Intra-Book Dependency Links (LOW PRIORITY)

Add a `Prerequisites:` and `Leads to:` metadata tag at the top of each scaffold, creating a directed graph within each book. Example for R38 (CVA):
```
Prerequisites: [R33 — CCR](R33_Counterparty_Risk_Beyond.md), [R37 — Exposure](R37_Future_Value_Exposure.md)
Leads to: [R39 — Stress Testing CCR](R39_Stress_Testing_Counterparty.md)
```

---

## 6. What You Should NOT Change

1. **The Boole Scaffold methodology itself.** It's fundamentally sound. The falsification + signal/noise + directional intuition architecture is more effective than any standard summarization approach.
2. **The constraint hierarchy** (`[REG] > [APP] > [ECO] > [THE]`). It correctly models GARP's answer-selection logic.
3. **The boundary events approach.** The 10-cascade map is the strongest differentiator in this project. Most FRM candidates study in silos and get destroyed by cross-domain vignettes.
4. **The distractor archetype taxonomy** (TRUE-IRRELEVANT, REG-ECO FLIP, INVERSE INTUITION, ABSOLUTE). This is a legitimate psychometric pattern that maps to real GARP question design.
5. **The Error Log structure.** Even though it's empty, the template is correct. It becomes critical during Phase 2/3.

---

## 7. Bottom Line

| Dimension | Grade | Notes |
|:----------|:------|:------|
| **Methodology** | **A** | The Boole + Ambiguity framework is genuinely superior to standard study methods |
| **Coverage** | **A** | 107/107 readings scaffolded. Full curriculum atomicity achieved |
| **Structural Consistency** | **B-** | Schema drift across 13 files. Two competing boundary docs. Stale metadata |
| **Operational Tooling** | **B** | Good templates, but tracker/calendar never activated. Drill bank is thin |
| **Cross-Domain Integration** | **A** | The boundary events map is the crown jewel. Collision matrix is exam-grade |
| **Maintenance Hygiene** | **C+** | Dead links, stale labels, template/reality mismatch |

**Overall: B+/A-** — The intellectual framework is excellent. The implementation needs a cleanup pass to fully realize the architecture's potential. The highest-ROI fix is resolving the schema drift in the 13 Book 2 files, which would bring structural consistency to 100%.
