# Event Log

Append-only. One row per major system event. **Never edit existing rows — only append.**

**Types:** `READING` · `DRILL` · `SYSTEM` · `REVIEW`
**Status:** `✅ Complete` · `⚠️ In Progress` (no close-out written = resume trigger)

---

| # | Date | Type | Subject | Detail | Status |
|:--|:--|:--|:--|:--|:--|
| 001 | 2026-04-18 | READING | R30 — Credit Risk Models | 7 LOs added to tracker (30.a–30.g) | ✅ Complete |
| 002 | 2026-04-19 | DRILL | Session A · R30 · Phase 1 | LOs: 30.g, 30.d, 30.e, 30.b · 4 errors (A1, A2×2, A3) | ✅ Complete |
| 003 | 2026-04-19 | DRILL | Session B · R30 · Phase 1 | LOs: 30.b (P1 Quant crossover) · 1 error (A1) | ✅ Complete |
| 004 | 2026-04-19 | DRILL | Session C · R30 · Phase 1 | LOs: 30.g, 30.b, 30.f · 3 errors (A2, A3, A10) | ✅ Complete |
| 005 | 2026-04-20 | DRILL | Session E · R30 · Phase 1 | LOs: 30.g, 30.d · 2 errors (A2, A3) | ✅ Complete |
| 006 | 2026-04-20 | DRILL | 30.g Deep Dive · R30 · Phase 1 | LO: 30.g (targeted remediation) · 3 errors (A1, A2×2) | ✅ Complete |
| 007 | 2026-04-20 | DRILL | Session G · R30 · Phase 1→2 | LOs: 30.g, 30.d · 3 errors (A1×2, A11) | ✅ Complete |
| 008 | 2026-04-20 | DRILL | Session H · R30 · Phase 2 | LOs: 30.g, 30.b · 4 errors (A1×4, A2) | ✅ Complete |
| 009 | 2026-04-21 | DRILL | Session I · R30 · Phase 2 | LO: 30.d · 1 error (A2) | ✅ Complete |
| 010 | 2026-04-21 | DRILL | Session J · R30 · Phase 2 | LO: 30.d · 1 error (A11) | ✅ Complete |
| 011 | 2026-04-21 | READING | R31 — Credit Derivatives | 8 LOs added (31.a–31.h) · boundary events updated | ✅ Complete |
| 012 | 2026-04-21 | SYSTEM | Review fixes (B1–B8) | A10 count, LO tracker snapshot, Priority/column format, dashboard refresh, Phase 3 boundary | ✅ Complete |
| 013 | 2026-04-21 | SYSTEM | Structural fixes (S1–S8) | Status legend removed · Priority unified · drill formula · step renumber · R38/R32 pending links | ✅ Complete |
| 014 | 2026-04-21 | SYSTEM | Event log + commit format | _EVENT_LOG.md created · drill.md + new-reading.md updated · R38 boundary annotation | ✅ Complete |
| 015 | 2026-04-21 | SYSTEM | Exhaustive review fixes (12 items) | C1–C5 + L1–L5 + L7, A3, A5 · 3 commits · R31 readiness 0.45→0.28, dashboard recomputed | ✅ Complete |
| 016 | 2026-04-25 | SYSTEM | Tag rename [APP]→[VIG] | Eliminate proposition-tag collision; 4 files touched (00_SYSTEM_PROMPT, drill.md, system/README, raw/chat) | ✅ Complete |
| 017 | 2026-04-25 | SYSTEM | Extraction verifier added | scripts/verify_extraction.py · 6 checks (B1–B2 blockers, W1–W4 warnings) · /new-reading Step 2.5 hook | ✅ Complete |
| 018 | 2026-04-25 | SYSTEM | R30/R31 retroactive audit | R30: 3 blockers (B1×3 dropped formulas), 1 warning · R31: 6 blockers (B1×5 + B2×1 dropped figure), 1 warning · audits saved as R{N}_extraction_audit.md | ✅ Complete |
| 019 | 2026-04-26 | SYSTEM | Migrated extraction to Gemini direct-PDF | scripts/extract_via_gemini.py + slice_pdf.py · .venv-gemini (50 MB, replaces .venv-marker 2 GB) · /new-reading Step 2 rewritten · verifier downgraded to non-blocking safety net · Marker pipeline abandoned (CPU too slow) | ✅ Complete |
| 020 | 2026-04-26 | FIX | R30 P7 corrected via Gemini-extracted PDF | F1 (one-factor copula factor decomposition) was wrong: Schema B showed only common-correlation form; PDF presents general form first (xᵢ = aᵢF + √(1−aᵢ²)Zᵢ). Both forms now in P7 + Trap. F2/F3/F4 confirmed correct. Source Fidelity footer added. | ✅ Complete |
| 021 | 2026-04-26 | FIX | R31 spot-checked via Gemini-extracted PDF | All 7 key formulas (CDS-bond basis, PS=e^−λt, expected payoff, MtM, Q(t\|F), EL_t, CDO C) confirmed match. Figure 31.7 now captured in raw markdown. Source Fidelity footer added. | ✅ Complete |

---

*Next session appends row #022. At close-out, update the row's Status from `⚠️ In Progress` to `✅ Complete`.*

> **Note:** Sessions D and F (alphabetical sequence) had no errors logged in `_ERROR_ARCHETYPES.md` and pre-dated this log — they are not reconstructed here. All sessions from #014 onward are fully tracked. Session numbering converts to numeric from #016: **next DRILL is Session 10** (9 prior DRILL rows in this log: #002–#010, per the drill.md counting rule).
