# R36 — Central Clearing

**Exam Priority:** 🔴 High (3-4 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.36.1` | **Novation:** The legal process where a bilateral contract between A and B is torn up and replaced by two new contracts: A-CCP and CCP-B. The CCP becomes the counterparty to everyone. | `[REG/OPS]` | It’s like a group of friends wanting to swap gifts. Instead of everyone mailing packages to each other (messy), they all send their gifts to a "Christmas Elf" (CCP), and the Elf sends them back out correctly. |
| `P.36.2` | **The Default Waterfall:** A strict prioritised sequence of funds used to cover losses if a member fails. It starts with the "Sinner's" money before touching the "Saints'" money. | `[REG/OPS]` | It’s the "Crumple Zone" of a car. Each layer absorbs some of the "Default Crash" until the energy is gone. Only in a massive accident does it reach the non-faulty members. |
| `P.36.3` | **Loss Mutualization:** The defining feature of CCPs. All members contribute to a shared Default Fund. If one fails and their own margin isn't enough, everyone else's contribution is used to save the system. | `[THE/REG]` | It’s an "All-for-One" insurance policy. You pay a small fee to make sure that if your neighbor's house burns down, the whole neighborhood doesn't catch fire. |
| `P.36.14` | **CCP Netting (Multilateral):** A CCP allows you to net positions across dozens of different counterparties into a single net exposure to the CCP. | `[MTH/MKT]` | If you owe Bob $10, and Alice owes you $10, you are net zero. In a bilateral world, you still have credit risk to Alice. In a CCP, those two trades cancel out completely. |
| `P.36.5` | **Skin in the Game:** The CCP must put its own capital (equity) into the waterfall (usually before using the non-defaulter's money) to ensure it has an incentive to manage risk properly. | `[REG/OPS]` | The Elf (CCP) has to put some of its own "Christmas Cookies" at risk. This makes the Elf very careful about which gifts it accepts into its workshop. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a derivative is highly ILLIQUID or CUSTOMIZED:** It is **Ineligible** for central clearing. The CCP cannot value it accurately or hedge it quickly if a member defaults.
- **Variable Flip: If a CCP only accepts Bonds as Variation Margin:** It faces **Liquidity Risk**. If the market crashes, the CCP needs cash *instantly* to pay the "winners." Selling bonds takes time and their price might be dropping. (This is why VM is usually **Cash-only**).
- **Variable Flip: If a CCP fails all its waterfall layers:** It must move to **Rights of Assessment**, effectively hitting its members with an "Emergency Tax." If that fails, the CCP itself is insolvent.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Novation:** Replaces A-B with A-CCP & CCP-B. | **Novation:** Guarantees no one ever loses money (NO: it just manages the loss). |
| **Waterfall:** Defaulter's IM is used first. | **Waterfall:** CCP Equity is used first (NO: "Sinners before Saints"). |
| **VM:** Usually Cash only. | **VM:** Usually Stocks and Bonds (NO: too illiquid for daily pays). |

## 4. Directional Intuition
- **Market Standardization $\uparrow \rightarrow$ CCP Compatibility $\uparrow$:** The more uniform the "Widgets" are, the easier it is for the factory (CCP) to process them.
- **Number of Members $\uparrow \rightarrow$ Loss Mutualization Strength $\uparrow$:** More people sharing the risk means each individual "hit" is smaller.
- **Concentration Risk $\uparrow \rightarrow$ Systemic Risk $\uparrow$:** By making everyone trade through one CCP, we’ve created a "Behemoth" that could potentially destroy the global economy if it ever failed.

## 5. Ambiguity Traps (Anti-Decoder)
- **Netting Benefit:** CCPs provide **Multilateral Netting**. Bilateral markets only provide **Bilateral Netting**. This is a massive capital efficiency win for banks.
- **Skin in the Game position:** Usually, CCP Equity sits between the Defaulter's contributions and the Non-defaulters' fund.
- **Initial Margin (IM) vs Default Fund (DF):** 
    - **IM** covers "Normal" market moves (the MPoR). 
    - **DF** covers "Extreme but Plausible" (Stressed) tail events.
- **Access:** Not everyone can join a CCP directly. "Tier 1" banks are **Clearing Members**. Smaller firms are **Clients** who clear *through* those members.
- **Macro-hedging:** The CCP’s first goal after a default is to get "Market Neutral." It will enter a large index trade to cancel out the defaulter's exposure before auctioning the specific trades.
- **Governance:** CCPs are often run by the big banks that use them, leading to potential conflicts of interest regarding how high margins should be.
- **Margin Period of Risk (MPoR):** Typically 5 days for OTC derivatives in a CCP.
- **Standardization:** Before a CCP accepts a product, it must have a reliable "Price Feed" and a "Liquidation Strategy."
- **Wrong-Way Risk:** If a member is long a contract that pays off when the member fails, the CCP will charge an extra margin penalty.
- **The "Butterfly" effect:** A default at one small member could trigger margin calls at other members, leading to a liquidity spiral.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
