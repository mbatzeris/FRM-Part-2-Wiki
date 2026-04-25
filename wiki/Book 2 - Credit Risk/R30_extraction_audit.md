# Extraction Audit — R30

**Generated:** 2026-04-25 22:05
**Source:** `C:/Users/user/Documents/FRM 2/wiki/Book 2 - Credit Risk/Book2.txt`
**Slice:** lines 6202–6725
**Result:** 3 blocker(s), 1 warning(s)

---

## 🔴 Blockers (must fix before LLM call)

| Code | Line | Issue | Snippet |
|:--|:--:|:--|:--|
| B1 | 6330 | Sentence ends with 'is equal to:' but no formula follows within 3 non-blank lines. | `ased on the Black-Scholes-Merton formula, the value of equity today is equal to:` |
| B1 | 6446 | Sentence ends with 'is equal to:' but no formula follows within 3 non-blank lines. | `default situation, the value of the bond is equal to:` |
| B1 | 6530 | Sentence ends with 'is equal to:' but no formula follows within 3 non-blank lines. | `Conditioned on the common factor (F), the default probability, Qi, is equal to:` |

## 🟡 Warnings (review recommended)

| Code | Line | Issue | Snippet |
|:--|:--:|:--|:--|
| W2 | — | Hyphenated line-breaks detected (6× pattern '[a-z]-\n[a-z]'). Recommend rejoin pre-LLM. | `6 occurrences` |

---

## Check legend

- **B1** — Orphan 'defined-as:' sentence (formula vanished)
- **B2** — Figure/Table caption without numeric payload
- **W1** — Subscript/superscript collapse (e.g., `E_0` → `E0`)
- **W2** — Hyphenation broken at line wrap
- **W3** — Greek-letter expectation violated
- **W4** — Page-density below 1500 chars/page