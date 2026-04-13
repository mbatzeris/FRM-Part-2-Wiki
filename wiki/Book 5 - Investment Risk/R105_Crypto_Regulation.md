# R105 — Regulating the Crypto Ecosystem

**Exam Priority:** 🔴 High (3-4 questions) Regulating the Crypto Ecosystem

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.105.1` | **Unbacked Crypto vs. Money:** Unbacked crypto assets (like Bitcoin) do not meet the full definition of "Money" because they fail as a **Store of Value** and **Unit of Account** due to extreme volatility. They are primarily speculative assets. | `[ECO/THE]` | Money is like a ruler—it shouldn't change length every hour. If your "ruler" (Bitcoin) is 12 inches now and 4 inches tomorrow, you can't use it to measure a house (Value) or pay a fixed bill (Account). |
| `P.105.2` | **The IOSCO Exchange Framework:** Regulation for crypto exchanges focus on the "same risk, same regulation" principle: ensuring governance, transparency, integrity, and the mitigation of **Conflicts of Interest** (e.g., when an exchange trades against its own customers). | `[REG/OPS]` | An exchange should be like a neutral referee. If the referee is also playing for one of the teams and betting on the game, the system is broken. |
| `P.105.3` | **Hot vs. Cold Wallets:** Wallets are the primary point of operational risk. "Hot" wallets (connected to the internet) offer convenience but are vulnerable to hacks. "Cold" wallets (offline) are secure but less liquid. | `[OPS/THE]` | A hot wallet is like carrying cash in your hand on a crowded street (Convenient but risky). A cold wallet is like keeping it in a heavy safe at the bottom of a pool (Safe but slow). |
| `P.105.4` | **BCBS Prudential Treatment:** The Basel Committee (BCBS) categorizes bank holdings into **Group 1** (Standard risk) and **Group 2** (High risk). Group 2 assets (unbacked crypto) face a **1,250% risk weight**, effectively requiring banks to hold $1 of capital for every $1 of crypto. | `[REG/MTH]` | The regulator says: "If you want to play with fire (Crypto), you must have a fire extinguisher equal to the size of the house." |
| `P.105.5` | **Regulatory Arbitrage & The BFA:** The **Bali Fintech Agenda (BFA)** emphasizes international cooperation. Without global standards, crypto firms will simply "hop" to the jurisdiction with the weakest rules (Regulatory Arbitrage). | `[REG/ECO]` | If one country bans smoking and the neighbor doesn't, people just walk across the border to smoke. You need a "Global No-Smoking Sign" to be effective. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a country implements a "Broad Ban" on crypto:** It will likely be **Ineffective**. Users will use VPNs, unregulated exchanges, and peer-to-peer transfers to bypass the ban. Targeted regulation of "On-ramps" (Exchanges) is usually more successful.
- **Variable Flip: If a stablecoin has "Algorithmic" backing (no actual assets):** It is much more prone to a **Death Spiral** or "Run" compared to a fully asset-backed stablecoin.
- **Variable Flip: If a blockchain is "Permissionless" (Public):** It offers higher decentralization but poses a massive **Governance and Legal** challenge for regulators, as there is no "Central Entity" to sue or subpoena.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Unbacked Crypto:** Value based solely on Supply/Demand. | **Stablecoins:** Value based on Supply/Demand (NO: based on peg). |
| **BCBS Group 2:** 1,250\% risk weight (High risk). | **BCBS Group 1:** 1,250\% risk weight (NO: standard weights). |
| **Hot Wallets:** Connected to the internet (Hacking risk). | **Cold Wallets:** Connected to the internet (NO: Offline). |

## 4. Directional Intuition
- **International Cooperation $\uparrow \rightarrow$ Regulatory Arbitrage $\downarrow$:** Harmonized rules mean there’s no "Easy" place for bad actors to hide.
- **Tokenization $\uparrow \rightarrow$ Market Efficiency $\uparrow$:** Using DLT for traditional securities (Security Tokens) can speed up settlement and reduce costs.
- **Privacy/Anonymity $\uparrow \rightarrow$ AML/CFT Compliance $\downarrow$:** The harder it is to see who owns a wallet, the easier it is for money launderers to use it.

## 5. Ambiguity Traps (Anti-Decoder)
- **Three Functions of Money:** Medium of Exchange, Store of Value, Unit of Account. Unbacked crypto usually only does #1.
- **NFTs:** They represent **Rights**, not just "images."
- **Validator/Miner Risk:** Note that the "Consensus Mechanism" (Proof of Work/Stake) is a form of operational dependency.
- **Custody vs. Self-Custody:** 
    - **Custody** = Bank/Exchange holds your keys. 
    - **Self-custody** = You hold your keys (Full loss risk if you lose the seed phrase).
- **White Papers:** The crypto version of a "Prospectus." Regulators want these to be standardized to prevent fraud.
- **Interoperability:** The ability for different blockchains to talk to each other. Lack of this creates "Liquidity Silos."
- **The "1,250%" Rule:** It means $8\% \times 1250\% = 100\%$ capital. You must have a full dollar of equity for every dollar of high-risk crypto.
- **Prudential vs. Conduct Regulation:** 
    - **Prudential** = Safety/Capital (Banks). 
    - **Conduct** = Fairness/Disclosures (Customers).
- **Shadow Banking:** Note that decentralized lending (DeFi) is the new form of shadow banking.
- **Immutability:** Records cannot be changed. This is a "Feature" for security but a "Bug" if a mistake is made or a court orders a reversal.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
