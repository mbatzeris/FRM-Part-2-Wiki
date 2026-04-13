# R49 — Cyber-Resilience: Range of Practices

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.49.1` | **Definition of Cyber-Resilience:** The ability to anticipate, withstand, recover from, and adapt to cyber-shocks, rather than just preventing them. | `[REG/BCBS]` | It’s about "Bouncing Back." Preventing the hack is security; surviving the hack and staying open is resilience. |
| `P.49.2` | **Sector-Specific vs. Cross-Sectoral:** Regulators in emerging/homogeneous markets often use sector-specific rules, while advanced markets use cross-sectoral frameworks. | `[REG]` | Small pond, specific rules; big ocean, universal rules. |
| `P.49.3` | **Cyber Information Sharing Types:** Sharing occurs between banks, regulators, and security agencies. Bank-to-bank and Bank-to-Security-Agencies are the most common flows. | `[OPS]` | If Bank A gets hit, telling Bank B helps the whole system defend. Information is the primary ammo in cyber-warfare. |
| `P.49.4` | **Third-Party/Outsourcing Risks:** Outsourcing introduces Vendor Lock-in, Security Risk, and Access Risk, but notably *not* Liquidity Risk (in this context). | `[REG]` | When you hire a cloud provider, you trade "Internal Control" for "Vendor Counterparty Risk." |
| `P.49.5` | **Resilience Metrics:** Effective management requires tracking supervision, security controls, incident response, and specific resilience KPIs. | `[OPS]` | You can't improve what you don't measure. Metrics provide the "DASHBOARD" for the cyber-defense posture. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank focused 100% of its budget on "Information Security Controls" (Prevention):** Then it would have zero capacity for "Incident Response and Recovery." This is the "Thin Glass Shield" failure—impossible to break, but total collapse if it does. Resilience requires balance across all four management areas.
- **Variable Flip: If Information Sharing was "Regulator-to-Bank" only:** Then the system would be too slow. Real-time defense requires "Bank-to-Bank" sharing to capture the speed of a spreading malware strain.
- **Variable Flip: If an Outsourcing Risk Analysis included "Liquidity Risk":** Then it would be misaligned with the BCBS range of practices for cyber-resilience. While a cloud failure might *eventually* cause liquidity issues, it is not a primary risk category within the cyber-outsourcing framework (Strategic/Security/Compliance are).

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Incident Response and Recovery** is a core management area. | **Asset Allocation** is not related to cyber-resilience frameworks. |
| **Vendor Lock-in** is a specific risk of third-party outsourcing. | **Liquidity Risk** is a distractor in cyber-outsourcing questions. |
| **Red Teaming (TIBER-EU)** is an ethical hacking tool used for testing. | **Scenario Analysis** is a broader ORM tool used for capital, not just cyber-testing. |

## 4. Directional Intuition
- **Market Homogeneity $\uparrow \rightarrow$ Sector-Specific Regulation $\uparrow$:** When all banks look the same, regulators can issue one "manual" for all of them.
- **Information Sharing $\uparrow \rightarrow$ Systemic Cyber Risk $\downarrow$:** The faster the industry shares "Signs of Compromise," the less likely a single malware strain can take down multiple institutions.
- **Outsourcing $\uparrow \rightarrow$ Vendor Lock-in Risk $\uparrow \rightarrow$ Exit Strategy Importance $\uparrow$:** The more you rely on one cloud provider (AWS/Azure), the harder it is to leave if they fail or raise prices.

## 5. Ambiguity Traps (Anti-Decoder)
- **Common vs. Rare Flows:** Which sharing flow is *less* common? Answer: **Regulator-to-Bank** or **Regulator-to-Regulator**. Most sharing is driven by the banks themselves or sent to security agencies.
- **The "Liquidity" Red Herring:** GARP loves to list "Liquidity Risk" as an outsourcing risk. **DON'T FALL FOR IT.** Stick to Strategic, Security, Compliance, and BCP.
- **Resilience vs. Security:** Is "Anticipating" an attack part of resilience? **YES.** Resilience is the complete lifecycle: Anticipate $\rightarrow$ Withstand $\rightarrow$ Recover $\rightarrow$ Adapt.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
