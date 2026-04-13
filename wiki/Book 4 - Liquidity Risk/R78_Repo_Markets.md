# R78 — Repo Markets

**Exam Priority:** 🟡 Medium (1-2 questions) and Financing

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.78.1` | **The Repo Equation:** A Repo is a collateralized loan. The borrower sells an asset for cash today and buys it back later at the **Repo Price**, which is `Cash * (1 + Repo Rate * days/360)`. | `[MTH/OPS]` | It’s a "Pawn Shop" for big banks. You give the lender your Treasury bond, they give you cash, and you pay them "Rent" (the Repo Rate) until you buy your bond back. |
| `P.78.2` | **GC vs. Specials:** The **General Collateral (GC)** rate applies to any acceptable bond in a class. A **Special** rate applies to a specific, highly-demanded bond and is always **lower** than the GC rate. | `[THE/MKT]` | GC is like "Any 4-door sedan." A Special is like "The one specific 1964 Ferrari everyone wants to rent." Because people want that *exact* bond, they are willing to accept a much lower interest rate on the cash they lend to get it. |
| `P.78.3` | **The Special Spread:** Defined as `GC Rate - Special Rate`. A larger spread indicates higher demand for that specific security in the market. | `[MTH/MKT]` | If the GC rate is 5% but the Special rate for a 10-year Treasury is 2%, the "Special Spread" is 3%. Investors are paying a 3% "Luxury Tax" to hold that specific bond. |
| `P.78.4` | **Counterparty vs. Liquidity Risk:** In a Repo, **Collateral** mitigates counterparty credit risk (the borrower dying), while **Haircuts** mitigate liquidity risk (the collateral price dropping before it can be sold). | `[THE]` | Performance is guaranteed by the bond (Credit fix); the "Extra Space" in the haircut ensures you get your full cash back even if the bond's price falls 2% (Liquidity fix). |
| `P.78.5` | **Crisis Spread Behavior:** During financial crises, the **Fed Funds-GC Spread** (`Fed Funds - GC Rate`) widens. This is because the demand for "Safe Harbor" collateral (GC) spikes, driving the GC interest rate down. | `[MKT/ECO]` | In a panic, everyone wants Treasuries as collateral. The more people want to "Lend Cash to get Treasuries," the lower the interest rate (GC) drops, pushing it far away from the Fed Funds rate. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a borrower defaults but the collateral value has dropped by 10% and the haircut was only 2%:** Then the lender incurs a loss. The **Haircut** must be large enough to cover the maximum potential price drop of the collateral during the liquidation window.
- **Variable Flip: If a security goes "On Special":** Its repo rate **Decreases**. This is counter-intuitive: High demand for a security makes its interest rate (the repo rate) go **Down**, potentially even to 0% (or negative).
- **Variable Flip: If a bank uses "Tri-Party Repo":** It reduces operational risk. A neutral third-party (Clearing Bank) handles the exchange of cash and collateral, ensuring that neither party can "cheat" during the settlement process.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Special Spread:** (GC Rate - Special Rate). | **Special Spread:** (Fed Funds - Special Rate) (NO: GC is the baseline). |
| **Haircut:** Mitigates Liquidity/Market Risk of collateral. | **Haircut:** Mitigates Counterparty Default Risk (NO: the collateral *itself* does that). |
| **Repo Seller:** The borrower of cash (provides collateral). | **Repo Buyer:** The lender of cash (receives collateral). |

## 4. Directional Intuition
- **Security Demand $\uparrow \rightarrow$ Special Rate $\downarrow \rightarrow$ Special Spread $\uparrow$:** The more "Desirable" a bond is, the cheaper the cash becomes for the person who owns it.
- **Market Volatility $\uparrow \rightarrow$ Repo Haircuts $\uparrow$:** Lenders demand more "Safety Margin" as the fear of asset price crashes increases.
- **Crises $\uparrow \rightarrow$ GC Rate $\downarrow \rightarrow$ Fed Funds-GC Spread $\uparrow$:** The "Flight to Quality" drives the cost of borrowing against Treasuries toward 0%.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Lower Rate" Trap:** Does "On Special" mean a higher rate? **NO.** It means a **LOWER** rate (the bond owner pays less interest to borrow cash).
- **Repo Price Math:** Don't forget the **360-day** convention (standard in US money markets).
- **Haircut vs. Margin:** They are functionally similar, but in Repo, the haircut is a discount to the market value of the bond.
- **Tri-Party Clearing:** Who are the players? Borrower, Lender, and **Clearing Bank** (The middleman).
- **Special Spread baseline:** The baseline is always the **GC Rate**, not Fed Funds or LIBOR.
- **Repo Buyer is the Lender:** In repo terminology, the "Buyer" is the one who *buys* the bond (lends the cash). The "Seller" is the borrower.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
