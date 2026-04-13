# R35 — Margin (Collateral) and Settlement

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.35.1` | **The Credit Support Annex (CSA):** The "Rulebook" for collateral. It defines exactly what counts as "money" (Eligibility), how much it's worth (Haircuts), and when to ask for it (Thresholds). | `[REG/OPS]` | It’s the "Pawn Shop Agreement." It says exactly which items the shop will take as a deposit and how much of a discount they'll apply to them. |
| `P.35.2` | **Haircuts (Valuation Percentage):** A buffer applied to collateral to account for potential price drops. If a bond has a 5% haircut, you only get $95 of credit for every $100 of bond you post. | `[MTH/MKT]` | It’s the "Safety Cushion." If you give me a $1,000 guitar as a deposit, I only value it at $800 because I might have to sell it in a hurry tomorrow for less. |
| `P.35.3` | **One-Way vs. Two-Way Agreements:** In a Two-way, both parties post collateral. In a One-way, only one party (usually the riskier one) posts. | `[THE/REG]` | In a One-way, the "Big Bank" says to the "Small Company": "I trust myself, but I don't trust you. You give me a deposit, but I won't give you anything." |
| `P.35.4` | **Rehypothecation (Reuse):** The right of a bank to take the collateral it received from Client A and use it as collateral for its own trade with Client B. | `[MKT/OPS]` | It’s like a landlord taking your security deposit and using it to pay their own mortgage. It keeps the system liquid, but creates a "Chain of Risk." |
| `P.35.5` | **Initial Margin (IM) vs. Variation Margin (VM):** VM covers the change in market price (today's gain/loss). IM is an extra "Buffer" held to cover potential losses during the time it takes to close the trade (the MPoR). | `[MTH/OPS]` | VM is "Squaring the Bill" every night. IM is the "Security Deposit" you pay upfront just in case you trash the room. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If the Haircut on an asset is 100%:** That asset is **Ineligible**. It provides zero credit for collateral purposes, effectively banning it from the CSA.
- **Variable Flip: If a firm has a "Rehypothecation" right and its own bank fails:** The original client who posted the collateral is now an **Unsecured Creditor**. Their specific asset is gone (it was reused elsewhere), and they just have a claim on the bankrupt estate.
- **Variable Flip: If Volatility $(\sigma)$ in the bond market spikes:** Haircuts in the CSA will likely **Increase**. The receiver demands more "buffer" to protect against the more frequent and larger price swings.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Haircut:** Applied to the collateral. | **Haircut:** Applied to the derivative payout (NO). |
| **Substitution:** Swapping assets of equal value. | **Substitution:** Cancelling the trade (NO: that’s termination). |
| **One-way Agreement:** Common for AAA vs B. | **One-way Agreement:** Illegal under Basel III (NO: still used in some OTC contexts). |

## 4. Directional Intuition
- **Liquidity of Asset $\downarrow \rightarrow$ Haircut $\uparrow$:** If an asset is hard to sell (like a corporate bond), the receiver demands a bigger "discount" to be safe.
- **Counterparty Credit Quality Gap $\uparrow \rightarrow$ Likelihood of One-way CSA $\uparrow$:** The bigger the "Power Dynamic," the more likely the strong party forces the weak party to post alone.
- **Margin Period of Risk (MPoR) $\uparrow \rightarrow$ Initial Margin $\uparrow$:** If it takes 10 days to kill a trade instead of 5, you need a bigger "deposit" to cover the potentially larger price move during those 10 days.

## 5. Ambiguity Traps (Anti-Decoder)
- **Haircut Math:** This is a classic calculation trap. If the call is for $100,000 and the haircut is 5%, you don't post $105,000. You post $100,000 / 0.95 = $105,263. 
- **Threshold vs. Minimum Transfer Amount (MTA):** 
    - **Threshold** = The amount of exposure allowed *before* collateral is needed. 
    - **MTA** = The smallest chunk of cash you're willing to move (to avoid $1 transfers every hour).
- **Interest on Collateral:** The receiver usually pays interest back to the poster (e.g., SOFR).
- **Cash is King:** Cash usually has a **0% Haircut**. It is the gold standard for collateral.
- **Adverse Selection:** A poster will always try to give the "Cheapest to Deliver" (the eligible asset with the highest haircut but lowest real-world value).
- **Dispute Resolution:** If the two parties disagree on the MtM, the CSA has a specific timeline (usually 1-2 days) to resolve it or move to "undisputed" amounts.
- **Legal Entity:** Collateral agreements are usually tied to a specific legal entity, not the whole corporate group.
- **The "Dirty" Price:** Collateral is usually valued at the "Dirty Price" (including accrued interest).
- **Wrong-Way Risk in Collateral:** Don't post the counterparty's own stock as collateral! If they default, the stock becomes worthless exactly when you need it.
- **Title Transfer vs. Pledging:** 
    - **Title Transfer** = Receiver owns it (common in UK/Europe). 
    - **Pledging** = Receiver has a lien but doesn't own it (common in US).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
