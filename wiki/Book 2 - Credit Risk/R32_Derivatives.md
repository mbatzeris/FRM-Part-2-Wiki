# R32 — Derivatives

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.32.1` | **The Lifecycle of a Trade:** Derivatives pass through three distinct phases: (1) **Execution** (the handshake), (2) **Clearing** (the math/risk calculation), and (3) **Settlement** (the final exchange of cash/assets). | `[OPS/THE]` | It’s like buying a car. Execution is signing the papers. Clearing is the bank checking your credit and calculations. Settlement is you driving the car away after the money transfers. |
| `P.32.2` | **Bilateral Markets:** Private trades between two parties. They allow for ultimate flexibility in contract terms and collateral, but carry high individual counterparty risk. | `[MKT/THE]` | It’s a "Back-Alley Deal." You can trade anything (flexibility), but you only have the other person's word that they will pay (high risk). |
| `P.32.3` | **Central Counterparties (CCPs):** A middleman that "interposes" itself between every buyer and seller. It standardizes contracts and uses **Loss Mutualization** to reduce systemic risk. | `[REG/OPS]` | It’s a "Farmer’s Market." A regulator makes sure everyone uses the same weights and measures, and if one stall fails, the market's insurance fund covers the customers. |
| `P.32.4` | **Derivative Product Companies (DPCs):** Highly rated (AAA) subsidiaries created specifically to trade derivatives, protecting the parent company from failure and vice-versa. | `[THE/REG]` | It’s like a "Hazmat Suit" for an investment bank. If the bank gets contaminated (fails), the DPC suit stays clean and keeps trading. |
| `P.32.5` | **Monoline Insurers:** Companies that provide credit enhancement (insurance) for bonds and derivatives. They are highly specialized but create a "Single Point of Failure" risk due to lack of diversification. | `[MKT/ECO]` | They are "One-Trick Ponies." They are great at that one trick, but if that specific trick fails (like subprime mortgages), the whole pony dies. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a CCP fails to collect Initial Margin:** It cannot perform **Loss Mutualization** effectively. The "Default Waterfall" will dry up, leading to a systemic freeze.
- **Variable Flip: If you move from a Standardized to a Bilateral market:** Your ability to hedge complex, specific risks **Increases** (Flexibility), but your liquidity and safety **Decrease**.
- **Variable Flip: If a firm uses an SPV to remove assets:** They have **Securitized** the risk. If the SPV is "off-balance sheet," the firm no longer reports the losses, but they may still have "Reputational Risk" if it blows up.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Clearing:** Calculating obligations. | **Clearing:** Exchanging the final cash (NO: that’s settlement). |
| **DPC:** Protects against originator failure. | **DPC:** Protects against market price moves (NO: it’s about credit). |
| **Bilateral:** Flexible collateral. | **Bilateral:** Standardized collateral (NO: that’s CCP). |

## 4. Directional Intuition
- **Market Standardization $\uparrow \rightarrow$ Systemic Transparency $\uparrow \rightarrow$ Counterparty Risk $\downarrow$:** The more we use CCPs and standard rules, the less "Hidden Rot" there is in the financial system.
- **Collateralization $\uparrow \rightarrow$ Potential Loss at Default $\downarrow$:** If you hold most of the value in "Baggage" (Collateral), you don't care as much if the other person walks away.
- **CDS Spreads $\uparrow \rightarrow$ Perceived Counterparty Risk $\uparrow$:** If it costs more to buy insurance on a bank, the market thinks that bank is more likely to fail.

## 5. Ambiguity Traps (Anti-Decoder)
- **Clearing vs. Settlement:** The #1 trap in this reading. Clearing is the *risk management* of the trade. Settlement is the *logistical completion* of the trade.
- **CCP Zero-Sum:** A CCP never takes a "market position." It is always long one contract and short the same contract. Its only risk is the **Default** of its members.
- **Loss Mutualization:** This is the CCP "Survival Fund." Every member contributes so that one failure doesn't kill the whole system.
- **DPCs vs. Monolines:** 
    - **DPC** = Internal safety barrier (AAA subsidiary). 
    - **Monoline** = External insurance company.
- **Execution:** Don't forget that execution can happen on an **Exchange** (public) or **OTC** (private).
- **The "Waterfall":** The order in which a CCP uses money to cover a default (1. Defaulter's margin $\rightarrow$ 2. Defaulter's contribution $\rightarrow$ 3. CCP equity $\rightarrow$ 4. Survivor's fund).
- **VaR interpretation:** "95% 1-week VaR of $1M" means you expect to lose **no more than** $1M in 95 out of 100 weeks.
- **Trade Compression:** A technique to "tear up" offsetting swaps in a portfolio to reduce the gross amount of risk without changing the net risk. Reduces capital requirements.
- **Novation:** The legal process where the CCP replaces the original bilateral contract between Party A and B with two new contracts (A-CCP and CCP-B).
- **SPVs:** Note that SPVs are often used for "Off-Balance Sheet" accounting. FRM often tests the "Moral Hazard" where a bank supports its SPV even when it's not legally required to.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
