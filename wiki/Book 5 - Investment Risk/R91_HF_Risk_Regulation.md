# R91 — Hedge Fund Risk, Regulation, and Structure

**Exam Priority:** 🟡 Medium (1-2 questions), and Structure

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.91.1` | **Five Incremental Risks:** Hedge funds vary from traditional funds due to (1) High Leverage, (2) Lighter Regulation, (3) Short-selling (unlimited loss), (4) Limited Transparency, and (5) Incentive-driven "Risk Tolerance." | `[THE/OPS]` | They are the "Special Ops" of finance. They have more firepower (leverage) and less oversight, which makes them lethal when right but catastrophic when they fail. |
| `P.91.2` | **Systemic Risk & Contagion:** Hedge funds generate systemic risk through **Contagion** (forced fire sales leading to price drops across uncorrelated assets) and **Banking Spillovers** (banks as prime brokers and counterparties). | `[MKT/ECO]` | If the "Big Whale" (a large HF) is forced to sell to pay its debts, it crashes the price for everyone else, even people holding "safe" assets. |
| `P.91.3` | **Regulatory Avoidance (The 1940 Act):** To avoid the strict rules for mutual funds, HFs use exemptions: **3(c)(1)** for <100 investors and **3(c)(7)** for "Qualified Purchasers" (>$5M in assets). | `[REG/OPS]` | It’s a "Private Club" rule. If you only let in a few people, or only let in very rich people, the regulator assumes you don't need the same "nanny" rules as a public fund. |
| `P.91.4` | **Master-Feeder Structure:** Capital from multiple "Feeder" funds (e.g., Onshore US vs. Offshore Cayman) is pooled into a single "Master" fund. This allows for unified trading and centralized risk management. | `[OPS]` | Two "Buses" (Feeders) carrying different types of passengers (Tax statuses) go to the same "Airport" (Master Fund) to board the same "Plane" (The actual trades). |
| `P.91.5` | **The Carried Interest Loophole:** Performance fees (usually 20%) are often taxed at lower **Capital Gains** rates rather than ordinary income rates, provided the underlying assets are held for more than one year. | `[REG/OPS]` | The manager claims their profit isn't a "Salary" for work, but a "Return" on an investment, which the tax man treats much more favorably. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a hedge fund manager advises more than 15 funds:** Under the **Dodd-Frank Act**, they MUST register with the SEC. The old "Private Adviser Exemption" (which allowed them to hide if they had few clients) was eliminated.
- **Variable Flip: If an investor has $3M in assets but is NOT an institution:** They are an **Accredited Investor** (Net worth > $2.5M) but NOT a **Qualified Purchaser** (requires > $5M). They can join 3(c)(1) funds but not 3(c)(7) funds.
- **Variable Flip: If regulators impose overly strict leverage limits:** This might **Increase** systemic risk by reducing market liquidity. Reasonable regulation is a balance; "Too much" can cause market "dry up" during a crisis.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Dodd-Frank Title IV:** Requires HF registration with SEC. | **Hedge Fund Registration:** Required by the 1940 Act (NO: they are exempt from the 1940 act). |
| **Section 3(c)(7):** High asset threshold ($5M) / High investor limit. | **Section 3(c)(1):** High asset threshold (NO: 3(c)(1) focuses on *number* of investors <100). |
| **Carried Interest:** Taxed as Capital Gains (if >1yr). | **Management Fees:** Taxed as Capital Gains (NO: always Ordinary Income). |

## 4. Directional Intuition
- **Market Stress $\uparrow \rightarrow$ Correlation between Hedges/Assets $\rightarrow$ 1.0:** In a panic, everything "Market Neutral" becomes "Market Correlated," leading to massive losses.
- **AUM $\uparrow \rightarrow$ Reporting Frequency (Form PF) $\uparrow$:** The bigger the fund, the more the government wants to see its books (Stability surveillance).
- **China Short Selling $\uparrow \rightarrow$ Arbitrage Cost $\downarrow$:** Currently, China's heavy restrictions on shorting (high costs + limited tickers) make market-neutral strategies nearly impossible to execute cheaply.

## 5. Ambiguity Traps (Anti-Decoder)
- **Registration vs. Regulation:** Are HFs "Regulated" like mutual funds? **NO.** But their **Managers** are now registered with the SEC.
- **3(c)(1) vs. 3(c)(7):**
    - 3(c)(1) = **100** limit. (Focus on "The Crowd").
    - 3(c)(7) = **No numeric limit** (nearly), but everyone must be **Rich** ($5M).
- **Regulation D:** Focuses on **Private Placements**. It’s the "Gatekeeper" that prevents HFs from advertising on TV.
- **Accredited Investor Thresholds:** 
    - Net Worth: **$2.5M** 
    - Annual Income: **$250k**.
- **The "2008" Turning Point:** Management fees can no longer be **Deferred** (loophole closed).
- **Master Fund:** Where does the **Trading** happen? Always in the **Master Fund**.
- **Survivorship Bias:** Why does it matter? Because it makes the "Average" hedge fund look much better than it is by ignoring the ones that blew up.
- **UBTI (Unrelated Business Taxable Income):** A tax trap for non-profits (pension funds/endowments) if the HF uses leverage. Often solved by using "Offshore" feeders.
- **Dodd-Frank and FSOC:** The FSOC monitors HFs for "Systemic" threats to the whole US financial system.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
