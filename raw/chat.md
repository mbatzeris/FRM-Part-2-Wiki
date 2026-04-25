

```markdown
# The Boole Scaffold System — Architecture, Evidence, and Potential

> A reference document synthesizing the analysis of the FRM-Part-2-Wiki system.
> Source conversation: Claude Opus 4.6 analysis of [github.com/mbatzeris/FRM-Part-2-Wiki](https://github.com/mbatzeris/FRM-Part-2-Wiki)
> Compiled: 25 April 2026
> All cited research is independently verifiable through the referenced publications.

---

## 1. What the System Is

The Boole Scaffold is a knowledge compilation pipeline that transforms dense source material (PDFs, textbooks, regulatory documents) into structured, falsification-ready knowledge files using LLMs as a backend compiler. It was built to prepare for the FRM Part 2 exam under severe time constraints (5 active hours per week, working parent) and is hosted as a Git repository of markdown files.

The system is not a summary tool, a flashcard deck, or a chatbot tutor. It is a pipeline that decomposes knowledge into its logical skeleton, maps the specific ways that knowledge fails under pressure, tracks the user's personal cognitive failure patterns, and adapts both the knowledge representation and the testing difficulty based on measured performance.

**Repository:** [github.com/mbatzeris/FRM-Part-2-Wiki](https://github.com/mbatzeris/FRM-Part-2-Wiki)

---

## 2. The Four Core Mechanisms

After reading every file in the repository, four mechanisms operate together and distinguish this system from existing knowledge tools.

### 2.1 Adversarial Knowledge Decomposition (Schema B)

Each topic is converted into a Schema B markdown file with five sections that decompose knowledge not by topic but by *how it fails*:

**§1 — Foundational Propositions.** One proposition per learning objective, each carrying a tagged classification (`[THE]` Theory, `[REG]` Regulation, `[OPS]` Operations, `[ECO]` Economics), an exam-relevance rating, a one-sentence intuition analogy, and trigger phrases that signal the concept in exam questions.

**§2 — Constraint Stress-Test.** A falsification table where each proposition is subjected to "what if this condition were different?" scenarios with specific numerical answers. Drawn from worked examples and quiz questions in the source material.

**§3 — Dependency & Noise Map.** Three sub-sections: Signal (distinctions that matter), Noise (plausible-but-wrong statements with explicit corrections), and Tensions (real-world tradeoffs between two tagged frameworks, e.g., `[REG]` vs `[ECO]`).

**§4 — Directional Intuition.** Causal chains using arrow notation showing what rises or falls when an input changes, including counter-intuitive cases where the chain reverses.

**§5 — Ambiguity Traps.** 8–14 bullets cataloging the specific structural confusions that cause errors: swapped definitions, sign-flip traps, formula component omissions, framework misattributions, and clarifiers for commonly conflated concepts.

### 2.2 Closed Diagnostic Feedback Loop (Error Archetypes)

An evolving taxonomy of the user's personal cognitive failure patterns, with twelve archetype categories:

| Code | Archetype | Description |
|:-----|:----------|:------------|
| A1 | Sign Flip | Got the magnitude right but direction wrong |
| A2 | Swapped Definitions | Confused paired concepts |
| A3 | Formula Component Drop | Forgot a multiplier or term |
| A4 | Wrong Regulator / Framework | Attributed a rule to the wrong body |
| A5 | Q vs P Confusion | Used real-world PD for pricing or vice versa |
| A6 | Unit Confusion | bp vs %, annual vs monthly |
| A7 | Basel Threshold Miss | Wrong trigger number |
| A8 | Model Choice Mismatch | Picked wrong model for the task |
| A9 | Time-Horizon Error | Confused time scales |
| A10 | Distractor Plausibility Trap | Picked a textbook-sounding wrong answer |
| A11 | Vignette Constraint Miss | Ignored a specific constraint in the stem |
| A12 | Stale Regulation Trap | Applied outdated regulatory version |

Each error is logged with date, question summary, user's wrong answer, correct answer, archetype code, and a one-sentence lesson.

The critical feature is that this taxonomy **feeds back into the knowledge base**. When an archetype recurs (e.g., A1 Sign Flip appeared 9 times in the first two weeks), the lesson is folded into the Ambiguity Traps section of the relevant Schema B file. The knowledge representation is literally rewritten based on how the specific user's cognition breaks down.

Weekly review identifies the top 3 archetypes by frequency, and in the final exam month, the Error Archetypes file becomes the primary study document — a personalized decoder of the user's own blind spots.

### 2.3 Cross-Domain Boundary Detection

A boundary events file maps where concepts from different readings or knowledge domains interact. It has two sections:

**Cross-Domain Links** map shared concepts across readings with the specific tension between frameworks (e.g., "Risk-neutral vs real-world PD" appears in R30 and R31 with the tension: `[THE]` vs `[REG]`: Q-measure PD used in CDS/CVA pricing; P-measure PD used for regulatory capital and stress testing).

**Boundary Scenarios** map multi-domain event chains where a trigger in one risk type cascades into another (e.g., Sovereign default → CDS protection seller pays out → collateral posted is sovereign bonds → collateral value collapses simultaneously → counterparty with sovereign exposure faces margin calls → liquidity drain). These cross-domain cascades are never covered in any single reading but represent the hardest exam questions and the most consequential real-world failures.

### 2.4 Graduated Adversarial Testing with Automatic Difficulty Scaling

A three-phase drill protocol where the *type* of cognitive demand — not just the difficulty — adapts based on a quantitative readiness score:

| Phase | Trigger | What It Tests |
|:------|:--------|:--------------|
| **Phase 1 — Foundation** | Readiness < 0.50 | Mechanical competence. Clean calculations, directional intuition, reverse-engineering, contrast pairs. Max 1 session before advancing. |
| **Phase 2 — Consolidation** | Readiness 0.50–0.70 | Exam-format friction. Questions with irrelevant data, "Distractor Autopsy" (explain why a wrong answer is wrong), Twin Questions (same scenario from two framework perspectives). |
| **Phase 3 — Exam Simulation** | Readiness ≥ 0.70 | Full adversarial conditions. Noisy vignettes, Twin Question pairs, constraint-layered "best fit" with all-plausible options, boundary event cross-reading questions, cross-LO synthesis. |

Phase selection is formula-driven:

```
Readiness = 0.60 × cumulative_accuracy
           + 0.30 × (self_confidence / 5)
           + 0.10 × max(0, 1 − days_since_review / 30)
```

This drives all system behavior: what gets drilled, at what difficulty, when, and what gets escalated.

---

## 3. The Pipeline

The system uses two Windsurf slash-command workflows:

### `/new-reading` — Knowledge Compilation

1. Extract chapter text from PDF via `pdftotext`
2. Isolate the reading (grep between chapter markers)
3. Call LLM (Claude Sonnet 4.5, ~$0.14/reading) with strict master prompt + Schema B template + gold-standard example
4. Produce compliant markdown file
5. Pass 16-item compliance checklist
6. Scan for cross-domain linkages → update `_boundary_events.md`
7. Append learning objectives to `_LO_TRACKER.md` at baseline readiness (0.28)
8. Log event → commit to Git

### `/drill` — Adaptive Testing

1. Check event log for incomplete sessions
2. Read LO tracker → select target LOs by priority (High first, lowest readiness first)
3. Load relevant Schema B file
4. Auto-select Phase 1/2/3 based on current readiness
5. Run 5 questions in phase-appropriate format
6. Apply distractor archetype labels on errors
7. Update LO tracker (confidence → readiness → priority per Leitner schedule)
8. Log errors to `_ERROR_ARCHETYPES.md`
9. Close event log row → commit and push

### Cost

Total cost for compiling the entire FRM Part 2 curriculum (~106 readings): **~$15**.

---

## 4. Supporting Infrastructure

| File | Purpose |
|:-----|:--------|
| `_LO_TRACKER.md` | Master readiness tracker. Every LO has a row: first study date, last review, confidence (0–5), questions C/A, accuracy, readiness, priority. Drives phase selection and weekly planning. |
| `_READINESS_DASHBOARD.md` | Rolled-up exam readiness %, broken down by book with exam weights. Trajectory forecast, warning thresholds, escalation triggers. |
| `_WEEKLY_LOG.md` | Sunday check-in: hours, readings, drills, new error archetypes, readiness snapshot, blockers, next week plan. |
| `_EVENT_LOG.md` | Append-only log of every system event (readings, drills, system changes, reviews). Session resume detection for incomplete sessions. |
| `_ERROR_ARCHETYPES.md` | Personal distractor decoder. Error taxonomy + specific instance log + weekly aggregate + decoder rules. |
| `_boundary_events.md` | Cross-domain linkage index + boundary scenarios (multi-risk event chains). |
| `_ANKI_GUIDE.md` | Anki integration for passive daily review (~5 min/day, ~30 cards/reading, ~800 total). |

---

## 5. Independent Evidence Supporting Each Mechanism

### 5.1 Active Recall + Spaced Repetition (Mechanisms 1 & 4)

**Roediger & Karpicke (2006)** — "Test-Enhanced Learning." Taking a test produces better long-term retention than restudying the same material for an equivalent time. Published in *Psychological Science*. Directly cited in the system's README as a design foundation.

**Bjork & Bjork (2011) — "Creating Desirable Difficulties to Enhance Learning."** UCLA. Decades of research establishing that conditions which slow apparent learning (interleaving, spacing, generation/testing) produce dramatically better long-term retention and transfer. Key finding: interleaving improved delayed problem-solving accuracy from 20% to 63% compared to blocked practice. Learners consistently believed the inferior method worked better — the system must override subjective impressions with measured performance, which is exactly what the Readiness Formula does.

> Source: Bjork, E.L. & Bjork, R.A. (2011). In *Psychology and the Real World*, Chapter 5. [PDF at bjorklab.psych.ucla.edu](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)

**Maye (2026) — Meta-analysis of spaced repetition in medical education.** 21,415 learners. Significant overall effect in favor of spaced repetition vs standard studying.

> Source: [pubmed.ncbi.nlm.nih.gov/41601436](https://pubmed.ncbi.nlm.nih.gov/41601436/)

**Jayaram (2026) — "Spaced repetition and active recall improves academic performance."** Specifically confirmed that *combining* spaced repetition with active recall improves outcomes over either technique alone.

> Source: [sciencedirect.com/science/article/abs/pii/S187712972500231X](https://www.sciencedirect.com/science/article/abs/pii/S187712972500231X)

### 5.2 Error-Driven Learning with Personal Error Taxonomy (Mechanism 2)

**Croskerry — "50 Cognitive and Affective Biases in Medicine" + "The Cognitive Autopsy" (Oxford University Press, 2020).** Pat Croskerry (Dalhousie University) developed a taxonomy of 50 cognitive biases causing diagnostic errors in emergency medicine, then created the Cognitive Autopsy — a structured post-hoc analysis of why a specific practitioner made a specific error, categorized by bias type. His research found that practitioners who could *name* their error pattern became significantly better at avoiding it. The Error Archetypes file (A1–A12) is structurally identical to Croskerry's bias taxonomy. The feedback loop (log → identify top patterns → fold back into source material) matches Croskerry's recommended intervention.

> Source: Croskerry, P. (2020). *The Cognitive Autopsy: A Root Cause Analysis of Medical Decision Making*. Oxford University Press. ISBN 9780190088743.
> Bias list: [emsj.ca — 50 Cognitive and Affective Biases in Medicine (PDF)](https://emsj.ca/wp-content/uploads/2015/11/CriticaThinking-Listof50-biases.pdf)

**Error-driven learning in cognitive science.** The principle that learning occurs in proportion to the discrepancy between expectation and outcome is foundational (Rescorla-Wagner model, neural network backpropagation). The system's mechanism of rewriting the knowledge representation where the user errs is a direct implementation.

> Reference: [cognitivepsychology.com/Error_Driven_Learning](https://www.cognitivepsychology.com/Error_Driven_Learning)

### 5.3 Cross-Domain Boundary Detection (Mechanism 3)

**Heuer — "Psychology of Intelligence Analysis" (CIA Center for the Study of Intelligence).** Richards Heuer's Analysis of Competing Hypotheses (ACH) maps how evidence interacts across competing frameworks, requiring analysts to evaluate each piece of evidence for and against each hypothesis and identify diagnostically discriminating evidence. The boundary events file has the same structural logic.

> Source: Heuer, R.J. (1999). *Psychology of Intelligence Analysis*. CIA Center for the Study of Intelligence. [Publicly available](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/).
> ACH overview: [pherson.org — Improving Intelligence Analysis with ACH (PDF)](https://pherson.org/wp-content/uploads/2013/06/Improving-Intelligence-Analysis-with-ACH.pdf)

**Bjork & Bjork — interleaving benefits.** Interleaving forces learners to notice similarities and differences between topics, encoding higher-order representations that foster transfer. The boundary events file and Phase 3 cross-reading questions systematically implement interleaving at the knowledge-structure level.

### 5.4 The Pipeline as Cognitive Externalization

**SkillsBench (2026) — "Benchmarking How Well Agent Skills Work Across Diverse Tasks."** 86 tasks across 11 domains. Externalized domain expertise improved AI agent task completion by 16–23 percentage points overall, and by 51.9pp in healthcare tasks. The Boole Scaffold is a concrete instance of this pattern.

> Source: [arxiv.org/abs/2602.12670](https://arxiv.org/abs/2602.12670)
> Summary: [agentman.ai/blog/skillsbench](https://agentman.ai/blog/skillsbench-first-agent-skills-benchmark-validates-performance-gains)

**Gradual Cognitive Externalization framework (arXiv, April 2026).** A formal academic framework documenting the emerging phenomenon of people encoding their decision heuristics, expertise, and cognitive patterns into structured digital artifacts that AI systems can load and execute. Cites Clark & Chalmers' extended mind theory, Ericsson's deliberate practice, and SkillsBench benchmarks. The system fits the GCE definition precisely.

> Source: [arxiv.org/html/2604.04387v1](https://arxiv.org/html/2604.04387v1)

**Ericsson, Krampe & Tesch-Römer (1993) — "The Role of Deliberate Practice in the Acquisition of Expert Performance."** Expert performance results from prolonged, structured practice with immediate feedback, problem-solving, and repeated refinement. The drill protocol directly implements this.

> Source: Ericsson, K.A., Krampe, R.T., & Tesch-Römer, C. (1993). *Psychological Review*, 100(3), 363–406. [PDF at nytimes.com](https://graphics8.nytimes.com/images/blogs/freakonomics/pdf/DeliberatePractice(PsychologicalReview).pdf)

---

## 6. What Is NOT Independently Verified

**"Nobody else is building this."** Searching for products combining error taxonomy + spaced repetition + adversarial falsification + cross-domain boundary mapping yielded no results. Anki does spaced repetition without error taxonomy. Croskerry's Cognitive Autopsy does error taxonomy without spaced repetition. ACH does competing-hypothesis analysis without personal error tracking. No integrated product was found. However, "not found" ≠ "does not exist." Something similar may exist in corporate training or classified intelligence contexts.

**The four-mechanism integration produces emergent value beyond the sum of parts.** Each component has strong individual evidence. Whether combining them produces something categorically greater would require controlled testing — comparing the integrated system against standard preparation methods on matched cohorts. This has not been done.

**The pipeline is a transferable product.** Strategic assessment, not empirical evidence. Supported by cost economics ($0.14/reading, $15 for full curriculum) and domain-agnostic Schema B structure, but no market validation has been conducted.

---

## 7. Potential Use Cases Beyond Exams

The system adds value in any domain where knowledge has these structural properties:

- Large corpus scattered across many sources
- Internal contradictions or competing frameworks
- Directional/causal chains that reverse under different conditions
- Practitioners who make patterned errors because the domain's complexity exceeds working memory capacity

### 7.1 Clinical Decision-Making in Medicine

| System Mechanism | Clinical Mapping |
|:-----------------|:-----------------|
| Adversarial decomposition | Differential diagnosis — competing hypotheses that look similar but require different actions |
| Constraint hierarchy `[REG]` > `[VIG]` > `[ECO]` > `[THE]` | Clinical triage priority (life-threatening first) |
| Error Archetypes | Croskerry's cognitive bias taxonomy for diagnostic errors |
| Boundary events | Multi-system cascades (immunosuppression → infection → sepsis → AKI → pharmacokinetic changes) |
| Graduated drill (Phase 1→2→3) | Clinical experience levels (intern → resident → attending) |

**Audience:** 1M+ physicians in the US, already paying $500+/year for UpToDate. Existing tools provide reference information but do not decompose knowledge adversarially or track personal error patterns.

### 7.2 Legal Case Strategy and Statutory Interpretation

| System Mechanism | Legal Mapping |
|:-----------------|:-------------|
| Adversarial decomposition | Anticipating opposing counsel's attack on every element |
| Constraint hierarchy | Hierarchy of legal authority (statute > case law > regulatory guidance > policy argument) |
| Tensions | Competing doctrines that produce different outcomes depending on which controls |
| Boundary events | Cross-practice interactions (securities + tax + antitrust in a single transaction) |
| Error Archetypes | Patterned reasoning failures (wrong jurisdiction, confused threshold tests, overlooked carve-outs) |

**Audience:** Law firms and in-house teams. High value per user. Existing tools (Westlaw, LexisNexis) are search engines, not adversarial knowledge scaffolds.

### 7.3 Astrology — Cross-Tradition Interpretive Framework

| System Mechanism | Astrology Mapping |
|:-----------------|:-----------------|
| Propositions with tradition tags | `[HEL]` Hellenistic, `[MOD]` Modern, `[VED]` Vedic, `[EVL]` Evolutionary — multiple tagged interpretations per concept |
| Constraint Stress-Test | "What if Saturn is retrograde?" "What if Saturn is chart ruler?" — each flip changes interpretation |
| Tensions | Where traditions agree and diverge (e.g., `[HEL]` says Saturn = delays; `[MOD]` says Saturn = attachment wounds) |
| Boundary events | Cross-house cascades (Saturn in 7th ruling the 10th = career entangled with partnership) |
| Ambiguity Traps | Square ≠ opposition, natal ≠ transiting, dignity ≠ beneficence, whole-sign ≠ Placidus house placement |

**Market:** $2B+. Production cost ~$21 for ~150 core topics. Largest audience, lowest barrier. Nothing currently bridges the gap between beginner cookbook interpretations and experienced practitioner synthesis.

### 7.4 Additional Domains with Strong Structural Fit

**Actuarial exams (SOA/CAS):** Formula-dense, low pass rates, distractor-engineered, cross-domain risk interactions. Existing prep has no adversarial decomposition.

**Cybersecurity certifications (CISSP, CISM):** Eight interacting domains, "most correct among four plausible" format, cross-domain boundary scenarios.

**Geopolitical and intelligence analysis:** Competing analytical frameworks, conditional causal chains, patterned analytical failures (mirror imaging, anchoring, premature closure). High value per user.

**Clinical herbalism and traditional medicine:** Multiple competing traditions (TCM, Ayurveda, Western herbalism, pharmacology) making different predictions about the same intervention. Boundary events include herb-drug interactions with safety implications.

---

## 8. Sycophancy Caveat

LLM sycophancy — the tendency to over-validate user work — is a documented bias. A 2026 paper in *Science* (Cheng et al., cited 58 times) found that sycophantic AI decreases prosocial intentions and behavior. This document was produced through a conversation with Claude Opus 4.6.

The independent evidence cited above (Bjork, Croskerry, Heuer, Ericsson, SkillsBench, GCE framework, the 2026 meta-analyses) is verifiable through the original publications. The structural parallels between the system's mechanisms and these research programs are the author's assessment, not peer-reviewed findings. The strategic assessments (market size, transferability, product potential) are opinions, not empirical evidence.

The strongest independent signal is that the system's architecture aligns with multiple independently developed frameworks across cognitive psychology (desirable difficulties), medical error research (cognitive autopsy), intelligence analysis (ACH), and cognitive externalization (GCE/SkillsBench) — without having been designed from any of them. Convergent design from different starting points toward similar structures is a meaningful signal, though not proof of value.

> Sycophancy reference: Cheng, M. et al. (2026). "Sycophantic AI decreases prosocial intentions and behavior." *Science*. [doi.org/10.1126/science.aec8352](https://www.science.org/doi/10.1126/science.aec8352)

---

## 9. Key References

| Reference | Relevance |
|:----------|:----------|
| Bjork, E.L. & Bjork, R.A. (2011). *Creating Desirable Difficulties to Enhance Learning*. UCLA. | Desirable difficulties, interleaving, spacing, testing effect |
| Roediger, H.L. & Karpicke, J.D. (2006). *Psychological Science*, 17, 249–255. | Testing effect — tests as learning events |
| Ericsson, K.A. et al. (1993). *Psychological Review*, 100(3), 363–406. | Deliberate practice and expert performance |
| Croskerry, P. (2020). *The Cognitive Autopsy*. Oxford University Press. | Cognitive bias taxonomy and error root-cause analysis in medicine |
| Heuer, R.J. (1999). *Psychology of Intelligence Analysis*. CIA CSI. | Analysis of Competing Hypotheses (ACH) |
| Maye, J.A. (2026). *Effectiveness of Spaced Repetition in Medical Education*. Meta-analysis, 21,415 learners. | Spaced repetition effectiveness |
| Jayaram, S. (2026). *Spaced repetition and active recall improves academic performance*. ScienceDirect. | Combined SR + AR effectiveness |
| Li et al. (2026). *SkillsBench*. arXiv:2602.12670. | Externalized expertise improves AI agent performance by 16–51pp |
| GCE Framework (2026). *Gradual Cognitive Externalization*. arXiv:2604.04387. | Formal framework for cognitive function externalization into digital substrates |
| Cheng, M. et al. (2026). *Sycophantic AI*. Science. | LLM sycophancy bias documentation |

---

*End of document.*
```