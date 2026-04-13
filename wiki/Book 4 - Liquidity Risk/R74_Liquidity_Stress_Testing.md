# R74 — Liquidity Stress Testing

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.74.1` | **The Liquidity Taxonomy:** Funding liquidity is split into **Operational** (day-to-day), **Contingent** (stress buffer), **Strategic** (M&A/expansion), and **Restricted** (set aside for specific uses). | `[THE/OPS]` | Operational is your "Checking Account"; Contingent is your "Emergency Fund"; Strategic is your "House Down-payment Fund"; Restricted is "Auto-pay for Taxes." |
| `P.74.2` | **The Core Threat:** **Deposit Runoff** (both demand and early term withdrawals) is generally considered the **largest threat** to a bank's liquidity position and must be the focus of behavioral modeling. | `[OPS]` | If everyone wants their money back at once, no amount of clever asset management can save a bank without a massive central bank backstop. |
| `P.74.3` | **Reverse Stress Testing:** A methodology where the bank assumes it has already failed (insolvency) and works backward to identify the specific triggers or "Breaking Points" that caused the collapse. | `[MTH]` | "Pre-Mortem" analysis. Instead of asking "What if rates rise?", you ask "What would have to happen for us to die?" and then see if that scenario is plausible. |
| `P.74.4` | **Stressed Asset Buffer Calculation:** `Normal Buffer - Stressed Cash Outflows + Stressed Cash Inflows`. This represents the bank's "Survival Slack" in a crisis scenario. | `[MTH/OPS]` | It’s your net "Oxygen Supply." You start with a full tank, subtract the leaks (Outflows), and add any spare air you find (Inflows). |
| `P.74.5` | **Integration (LST + CST):** Liquidity stress testing (LST) must be integrated with Capital stress testing (CST) because liquidity injections often impact a firm’s overall capital adequacy. | `[OPS]` | If you have to borrow $1B to stay liquid, that new debt changes your leverage ratio and capital buffer. You can't fix one "Hole" without potentially creating another one. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank performs stress tests only for "Idiosyncratic" risk:** Then it is blind to a market-wide "Systemic" event (like the 2008 GFC) where all counterparties freeze simultaneously. A robust framework must test **Idiosyncratic, Systemic, and Combined** scenarios.
- **Variable Flip: If a bank performs LST only "Annually":** This is insufficient. Guidelines recommend at least **Quarterly** updates to allow the Asset-Liability Committee (ALCO) to respond to changing market conditions.
- **Variable Flip: If "Relationship Tenure" is ignored in deposit modeling:** Then the bank’s runoff assumptions are likely wrong. Tenure is a relevant behavioral factor for **all** segments (Retail, Small Biz, and Institutional). Long-time customers are "Stickier" than new "Mercenary" rate-chasers.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Strategic Liquidity:** Used for M&A and investment opportunities. | **Restricted Liquidity:** Used for potential investment opportunities (NO: it’s for predetermined uses). |
| **Deposit Runoff:** Largest threat to bank liquidity. | **Derivative Cash Flows:** Important, but usually second to deposit runoff in total volume threat. |
| **Reverse Stress Test:** Starts from "Failure" and works backward. | **Standard Stress Test:** Starts from "Shocks" and works forward. |

## 4. Directional Intuition
- **Economic Instability $\uparrow \rightarrow$ Deposit Runoff $\uparrow \rightarrow$ Stressed Asset Buffer $\downarrow$:** Panic leads to withdrawals, which drains the emergency tank exactly when it’s hardest to refill.
- **Relationship Tenure $\uparrow \rightarrow$ Deposit Stability $\uparrow \rightarrow$ Outflow Assumptions $\downarrow$:** The more "Loyal" the customer base, the less cash the bank needs to hold in its contingent buffer.
- **Haircuts (Stressed Assumptions) $\uparrow \rightarrow$ Stressed Buffer $\downarrow \downarrow$:** If you assume your "Safe" bonds only sell for 80 cents on the dollar, your perceived liquidity evaporates.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Largest Threat":** When asked for the biggest liquidity risk, look for **Deposit Runoff**.
- **Scenario Types:** Don't forget the **Combined** scenario. Testing only one or the other (Systemic/Idiosyncratic) is an incomplete "Fail."
- **Strategic vs. Restricted:**
    - "I might buy a bank tomorrow": **Strategic.**
    - "This cash is locked by law for taxes": **Restricted.**
- **Frequency Trap:** Is "Annually" enough? **NO.** Think **Quarterly** (at minimum).
- **Behavioral Factors:** Does Relationship Tenure apply only to retail? **NO.** It applies to **Institutional** and **Commercial** clients too.
- **Integration:** Does LST happen in a vacuum? **NO.** It must be linked to **Capital (CST)** and **Funds Transfer Pricing (FTP)**.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
