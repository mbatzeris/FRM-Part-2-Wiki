# R51 — Sound Management of Risks Related to Money Laundering and Financing of Terrorism

**Exam Priority:** 🟢 Low (0-1 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|
| `P.51.1` | **3LoD in AML/CFT:** Layer 1 (Front Office) is the primary line for identifying and controlling ML/FT risks; Layer 2 (AML Officer) provides oversight; Layer 3 (Audit) ensures framework integrity. | `[REG/OPS]` | The teller (L1) is the first filter; the Compliance officer (L2) sets the rules; the Auditor (L3) checks if the rules are being followed. |
| `P.51.2` | **Customer Risk Profiling:** Banks must assess customers based on Source of Wealth, Occupation, Country of Origin, and Account Purpose to determine the required level of due diligence. | `[REG]` | A local teacher with a savings account is low risk; a foreign "consultant" moving millions across borders is high risk. |
| `P.51.3` | **Politically Exposed Persons (PEPs):** Individuals with prominent public functions present higher ML/FT risks and always require **Enhanced Due Diligence (EDD)**. | `[REG]` | Power attracts corruption. Even if they seem clean, the "Title" mandates a deeper investigation (EDD). |
| `P.51.4` | **Cross-Border Stricter Rule:** In cases of cross-border operations, banks and supervisors must apply the stricter of the two jurisdictions' AML/CFT requirements. | `[REG/BCBS]` | When in two countries, follow the highest bar. You can't "jurisdiction-shop" for a weaker regulator. |
| `P.51.5` | **AML Officer Reporting:** It is a regulatory best practice for the Chief AML/CFT Officer to have a direct reporting line to the Board or Senior Management. | `[OPS]` | The compliance lead needs enough "OOMPH" (authority) to stop a lucrative but illegal transaction without fear of being silenced by the business line. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank applied "Simplified Due Diligence" to a Foreign PEP:** Then the bank would be in material breach of BCBS/FATF standards. Foreign PEPs are categorically high-risk and must never be "simplified," regardless of their account balance.
- **Variable Flip: If a bank followed the "Local" rule instead of the "Stricter" rule in a cross-border scenario:** Then the bank would expose itself to regulatory arbitrage risks. The global standard requires the **Stricter** rule to prevent money from flowing toward the weakest link in the chain.
- **Variable Flip: If the Chief AML Officer (L2) reported to the Business Unit Head (L1):** Then the independence of the second line would be compromised. The officer would have a conflict of interest that could lead to "blind-eye" approvals of high-risk business.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Enhanced Due Diligence (EDD)** is for PEPs and large cross-border flows. | **Standard Due Diligence** is not sufficient for high-risk occupations. |
| **Supervisor's Role:** Ensure the stricter rule is applied in cross-border contexts. | **Supervisor's Noise:** They do *not* require banks to use the same payment systems or see daily logs of every transfer. |
| **Source of Wealth (SOW)** is a critical factor for high-risk clients. | **Revenue from Client** is a business factor, not an AML risk factor. |

## 4. Directional Intuition
- **Cross-Border Complexity $\uparrow \rightarrow$ AML Monitoring Burden $\uparrow \rightarrow$ Potential for "Shadow" Transactions $\uparrow$:** The more jurisdictions involved, the easier it is for criminals to hide the "audit trail" through layering.
- **Political Instability in Origin Country $\uparrow \rightarrow$ PEP Risk $\uparrow \rightarrow$ EDD Frequency $\uparrow$:** If a customer comes from a high-corruption region, the bank must assume higher risk even if the individual seems legitimate.
- **L1 Policy Communication $\downarrow \rightarrow$ ML/FT Identification Failures $\uparrow$:** If the front-line staff don't understand the policy, they will skip the "Identification" step, making the L2 and L3 oversight useless.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Stricter Rule" Hinge:** GARP will ask: "In a cross-border transfer between Country A (Strict) and Country B (Lax), which rules apply?" Answer: **Country A (The Stricter one)**.
- **The "High Balance" Logic:** Is a high balance alone enough for EDD? **NO.** But high balances *combined* with regular cross-border transfers or suspicious activity triggers it.
- **Who is the First Line?** GARP might suggest the AML Officer is the first line. **FALSE.** The **Business Unit/Front Office** is the first line of defense.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
