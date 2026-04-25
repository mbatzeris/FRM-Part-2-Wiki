# Extraction Audit — R31

**Generated:** 2026-04-25 22:06
**Source:** `C:/Users/user/Documents/FRM 2/wiki/Book 2 - Credit Risk/Book2.txt`
**Slice:** lines 6726–7408
**Result:** 6 blocker(s), 1 warning(s)

---

## 🔴 Blockers (must fix before LLM call)

| Code | Line | Issue | Snippet |
|:--|:--:|:--|:--|
| B1 | 6877 | Sentence ends with 'is computed as:' but no formula follows within 3 non-blank lines. | `The expected payoff for the protection seller is computed as:` |
| B1 | 6931 | Sentence ends with 'is computed as:' but no formula follows within 3 non-blank lines. | `MtM value of the swap to the protection seller is computed as:` |
| B1 | 7026 | Sentence ends with 'is computed as:' but no formula follows within 3 non-blank lines. | `pays to the buyer is computed as:` |
| B1 | 7144 | Sentence ends with 'is computed as:' but no formula follows within 3 non-blank lines. | `The expected loss at time t is computed as:` |
| B1 | 7191 | Sentence ends with 'is computed as:' but no formula follows within 3 non-blank lines. | `price, the unconditional PD is computed as:` |
| B2 | 7081 | Caption with no numeric/formula payload in next 8 lines (likely table/figure dropped). | `Figure 31.7: Total Return Swap Structure` |

## 🟡 Warnings (review recommended)

| Code | Line | Issue | Snippet |
|:--|:--:|:--|:--|
| W2 | — | Hyphenated line-breaks detected (1× pattern '[a-z]-\n[a-z]'). Recommend rejoin pre-LLM. | `1 occurrences` |

---

## Check legend

- **B1** — Orphan 'defined-as:' sentence (formula vanished)
- **B2** — Figure/Table caption without numeric payload
- **W1** — Subscript/superscript collapse (e.g., `E_0` → `E0`)
- **W2** — Hyphenation broken at line wrap
- **W3** — Greek-letter expectation violated
- **W4** — Page-density below 1500 chars/page