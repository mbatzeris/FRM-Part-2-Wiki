# R106 — Tokenization and Market Inefficiencies

**Exam Priority:** 🔴 High (3-4 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.106.1` | **The Core Triad:** Digital ledgers offer three fundamental benefits: (1) **Trust** (Verified records), (2) **Sharedness** (Single source of truth), and (3) **Programmability** (Smart contracts). | `[THE/OPS]` | It’s a "Living Spreadsheet." Imagine a shared Google Sheet (Sharedness) that only lets you enter valid numbers (Trust) and automatically pays your bills when a cell changes (Programmability). |
| `P.106.2` | **Native vs. Non-native Tokens:** Native tokens (like Bitcoin) exist only on the blockchain. Non-native tokens are "Digital Wrappers" for real-world assets like gold, stocks, or real estate. | `[THE/MKT]` | Native tokens are "Digital Gold." Non-native tokens are "Digital Receipts" for physical gold sitting in a real-world vault. |
| `P.106.3` | **Mitigating Frictions:** Tokenization reduces **Internalities** (like search costs and information asymmetry) and **Externalities** (by improving coordination through network effects). | `[ECO/MKT]` | It’s like "The Uber-ization of Assets." It makes finding a buyer (Search) and checking the asset's history (Information) as easy as clicking a button on an app. |
| `P.106.4` | **The Automation Trap:** Programmability (Smart Contracts) can lead to faster **Shock Propagation**. Automated liquidation triggers can create "Flash Crashes" where models sell off assets instantly without human judgment to "hit the brakes." | `[OPS/MKT]` | If every robot is programmed to "Jump out the window if the price hits $90," and the price hits $90, they all jump together in one millisecond, crashing the market. |
| `P.106.5` | **Monopoly Rents:** While tokenization aims to reduce middlemen, a private ledger that gains market dominance can become a "New Middleman," charging high fees (Monopoly Rents) once users are locked into their platform. | `[ECO/REG]` | You replaced the "Bank" with a "System," but if one company owns the "System," they just become the new Bank with even more power. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If ledgers are Non-interoperable (Fragmented):** The benefit of tokenization is **lost**. Users are stuck in "Digital Silos," and liquidity is split across many different platforms that can't talk to each other.
- **Variable Flip: If a Permissioned Ledger suffers from "Collusion":** Then the **Trust** feature fails. If the certified validators decide to "cheat" together, they can alter the records for their own benefit.
- **Variable Flip: If tokenization leads to higher Leverage:** It creates **Systemic Vulnerability**. Lower costs make borrowing easier, but a small drop in asset value can trigger a massive, automated deleveraging event.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Programmability:** Enabled by Smart Contracts. | **Programmability:** Enabled by high liquidity (NO: that's an effect). |
| **Non-native Tokens:** Requires a link to off-chain assets. | **Non-native Tokens:** Exist only on the ledger (NO: that's Native). |
| **Trust Failure:** Collusion in permissioned ledgers. | **Trust Failure:** Use of VPNs (NO: that's a bypass, not a trust failure). |

## 4. Directional Intuition
- **Asset Transparency $\uparrow \rightarrow$ Information Asymmetry $\downarrow$:** If the ledger shows every previous owner and repair on a building, a buyer can’t be easily "tricked."
- **Settlement Speed $\uparrow \rightarrow$ Counterparty Risk $\downarrow$:** Transferring a token and payment at the same time (Atomic Settlement) means no one is "waiting for the check to clear."
- **Ledger Fragmentation $\uparrow \rightarrow$ Transaction Costs $\uparrow$:** The more "Walls" there are between systems, the more "Tolls" you have to pay to move money across.

## 5. Ambiguity Traps (Anti-Decoder)
- **Sharedness:** It’s about a "Consensus" on what the truth is.
- **Internalities vs Externalities:** 
    - **Internalities** = Costs to the people *inside* the trade (Search/Asymmetry). 
    - **Externalities** = Costs to people *outside* (Network effects/Stability).
- **Atomic Settlement:** The "All or Nothing" nature of a blockchain trade.
- **Lock-in Effect:** When it's too expensive to move your tokens to a different ledger, you are vulnerable to "Monopoly Rents."
- **Smart Contracts:** They are "Self-Executing" code. They don't need lawyers to enforce the handshake.
- **Flash Crashes:** A key risk of **Programmability**.
- **Permissioned vs Permissionless:** 
    - **Permissioned** = Like a Private Club (Banks). 
    - **Permissionless** = Like a Public Park (Bitcoin).
- **Consensus Mechanism:** How the ledger decides which block is "True."
- **Tokenization's Goal:** Not just "Making it digital," but making it "Programmable and Shared."
- **Interoperability:** The "Bridge" between different digital islands.
- **Search Friction:** The Difficulty of finding a buyer. Tokenization turns a "Manual search" into a "Digital match."


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
