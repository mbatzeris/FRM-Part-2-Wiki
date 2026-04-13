# The Boole Scaffold: Reading 31 - Credit Derivatives

**Exam Priority:** Medium (1-2 questions)

*Source Material: FRM 2026 Part II Book 2*
*Learning Objectives Covered:* 
*Related Readings: [R28 — Credit VaR](R28_Credit_VaR.md), [R30 — Credit Risk](R30_Credit_Risk.md), [R40 — Structured Credit Risk](R40_Structured_Credit_Risk.md)*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|---|------------|-----|---------------|----------------|
| P1 | **Credit Default Swaps (CDS):** The protection buyer pays a periodic premium (spread). If a credit event occurs, the protection seller pays Par minus Recovery (or physical delivery). | `[ECO]` | Foundation — Basic mechanics of credit transfer. | "protection buyer," "credit event" |
| P2 | **Total Return Swaps (TRS):** The payer transfers the *total* economic performance (coupons + capital gains/losses) of a reference asset in exchange for a floating rate (e.g., SOFR + spread). Transfers BOTH credit risk and market risk. | `[ECO]` | High — Distinguishing from CDS which only transfers default risk. | "total return receiver," "market risk and credit risk" |
| P3 | **CDS Basis:** The difference between the CDS spread and the underlying bond's Z-spread (CDS Spread - Bond Spread). It should theoretically be zero (arbitrage). | `[THE]` | High — The most tested pricing relationship. | "negative basis," "CDS spread minus bond spread" |
| P4 | **Negative Basis Trade:** Occurs when CDS Spread < Bond Spread. An arbitrageur buys the bond (earning the high spread) and buys CDS protection (paying the low spread), locking in a risk-free profit. | `[OPS]` | Very High — Actionable trading strategy GARP loves to test. | "negative CDS basis," "arbitrage strategy" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|-------------|----------------|-------------|
| P2 (TRS vs CDS) | An investor wants to hedge against a corporate bond defaulting, but wants to retain the upside if interest rates fall, increasing the bond's price. | The investor MUST use a **CDS**. If they use a TRS, they will pass all capital gains (interest rate upside) to the TRS receiver. |
| P3/P4 (Basis Trade) | The CDS basis is +50 bps (Positive Basis). | The arbitrage reverses: The trader must **Short the Bond** and **Sell CDS Protection**. (Positive basis = CDS is too expensive; sell it). |
| P1 (CDS Settlement) | A credit event occurs, and the cheapest-to-deliver (CTD) bond is trading at 25 cents on the dollar. | The protection seller pays **75% of Par** ($100 - $25) in cash settlement, or pays $100 and receives the $25 bond in physical settlement. Financial outcome is identical. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- Whether the basis is Positive or Negative.
- Whether the instrument isolates credit risk (CDS) or includes market risk (TRS).
- The "Cheapest-to-Deliver" option value granted to the protection buyer in physical settlement.

**Noise (distractors):**
- The underlying firm's equity dividend yield.
- Historical default probabilities when executing a basis arbitrage (arbitrage relies on current market prices, not historical stats).

**Tensions:**
- **[THE] vs [OPS]:** `[THE]`oretically, the CDS basis is exactly zero. `[OPS]`erationally, the basis is often negative because bonds require funding (repo) and use balance sheet, whereas CDS are unfunded synthetic derivatives. The "arbitrage" is not truly risk-free due to funding costs.

## 4. Directional Intuition

| Formula / Concept | Direction When Input ↑ | Exam Trap |
|-------------------|----------------------|-----------|
| CDS Basis = CDS - Bond | Negative Basis Trade: Buy Bond, Buy CDS | Confusing which leg to buy/sell. Always BUY the cheaper asset. If Basis is negative, CDS is cheap → Buy it. |
| TRS Receiver | Asset Price ↑ → Receiver Cash Flow ↑ | Forgetting that the TRS receiver is *long* the asset. If the asset defaults, the receiver owes the payout to the payer. |


## 5. Ambiguity Traps (Anti-Decoder)
- **CDS Buyer = Protection Buyer = Short Credit:** Buying a CDS is equivalent to shorting the reference entity's credit. The CDS buyer pays a premium and profits if spreads widen or default occurs.
- **Cheapest-to-Deliver (CTD) Option:** In physically settled CDS, the protection buyer can deliver the cheapest eligible bond. This CTD option makes CDS slightly more valuable than implied by a single bond's spread.
- **CDS-Bond Basis:** Basis = CDS Spread - Bond Spread. A negative basis means the CDS is "cheap" relative to the bond — potential arbitrage. During the GFC, basis went massively negative due to liquidity.
- **Index CDS vs. Single-Name CDS:** Index CDS (CDX, iTraxx) are standardized and more liquid. Single-name CDS are customized and less liquid but more precise for hedging specific exposures.

## 5. Ambiguity Traps (Anti-Decoder)
- **CDS Buyer = Protection Buyer = Short Credit:** Buying a CDS is equivalent to shorting the reference entity's credit. The CDS buyer pays a premium and profits if spreads widen or default occurs.
- **Cheapest-to-Deliver (CTD) Option:** In physically settled CDS, the protection buyer can deliver the cheapest eligible bond. This CTD option makes CDS slightly more valuable than implied by a single bond's spread.
- **CDS-Bond Basis:** Basis = CDS Spread - Bond Spread. A negative basis means the CDS is "cheap" relative to the bond — potential arbitrage. During the GFC, basis went massively negative due to liquidity.
- **Index CDS vs. Single-Name CDS:** Index CDS (CDX, iTraxx) are standardized and more liquid. Single-name CDS are customized and less liquid but more precise for hedging specific exposures.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
