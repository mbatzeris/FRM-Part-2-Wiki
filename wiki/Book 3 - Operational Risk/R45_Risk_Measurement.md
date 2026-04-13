# R45 — Risk Measurement

**Exam Priority:** 🟢 Low (0-1 questions) and Assessment

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.45.1` | **The Indicator Triad:** Firms use KRIs (Exposure), KCIs (Control effectiveness), and KPIs (Business efficiency) to monitor the operational environment. | `[OPS]` | KRIs tell you how many people are trying to hack you; KCIs tell you if your firewall is actually on; KPIs tell you if you're still making money. |
| `P.45.2` | **RCSA Bias Analysis:** When backtesting qualitatively assessments (RCSAs), human experts tend to underestimate the *frequency* (likelihood) but overestimate the *severity* (impact). | `[THE]` | Humans are "Black Swan" obsessed but "Day-to-day" blind. We ignore the leaky faucet but panic about the flood. |
| `P.45.3` | **Loss Event Chronology:** The time between **Occurrence** and **Reporting** is typically the longest interval, as discovery can be delayed for years (e.g., hidden fraud). | `[REG]` | A loss that happened in 2020 but was found in 2024 is still a 2020 event for data modeling, even if the check is written in 2024. |
| `P.45.4` | **Fault Tree Calculation:** The probability of a top-level event is the product of the probabilities of independent sequential failures in an "AND" gate. | `[THE]` | For a heist to succeed, the alarm AND the guard AND the safe must fail. If any one works, the heist fails. |
| `P.45.5` | **Capital Modeling Techniques:** Firms use **Filtering** (data cleaning), **Cut-off Mix** (using external data for tails), and **Scaling** (adjusting for bank size) to build loss distributions. | `[REG/BCBS]` | Internal data is never enough for the "big one." You have to borrow (external) and adjust (scale) to see the true tail. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a KCI (Control Indicator) showed 100% success but a KRI (Risk Indicator) was red:** Then the controls are ineffective against the *specific* threat, or the controls are measuring the wrong thing. This creates a "False Sense of Security" where the wall is strong but the gate is open.
- **Variable Flip: If you scaled a $1M loss from a small bank to a global bank without adjustment:** Then you would likely underestimate the potential loss. Scaling must account for the fact that larger banks have larger transaction volumes and higher potential for catastrophic "tail" events.
- **Variable Flip: If a "Near Miss" was excluded from a Fault Tree model:** Then the calculated probability of failure would be artificially low. Near misses provide the data points needed to estimate the frequency of the "gates" failing before a total system collapse.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **KCIs** measure *controls* (e.g., "percentage of staff trained"). | **KRIs** measure *risk surface* (e.g., "number of hacking attempts"). |
| **Swiss Cheese Model:** Multi-layered failures lead to a loss. | **Bowtie Tool:** Visualizing the relationship between causes, the event, and the consequences. |
| **Backtesting RCSAs:** Reveals underestimation of frequency. | **Scenario Analysis** is for *extreme* events; RCSAs are for *known* process risks. |

## 4. Directional Intuition
- **Reporting Delay $\uparrow \rightarrow$ Capital Adequacy Uncertainty $\uparrow$:** The longer it takes to discover and report losses, the more likely the bank's current capital reserves are based on stale or incomplete data.
- **Interconnectedness $\uparrow \rightarrow$ Fault Tree Complexity $\uparrow \rightarrow$ Hidden Vulnerability $\uparrow$:** The more "AND" gates you have in a system, the harder it is to spot a single point of failure that bypasses multiple layers.
- **External Data Inclusion $\uparrow \rightarrow$ Tail Sensitivity $\uparrow \rightarrow$ Economic Capital Requirement $\uparrow$:** Using industry-wide "catastrophe" data usually pushes the 99.9% VaR further out than using only friendly internal data.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "KCI vs KRI" Mix-up:** Question: "A bank's IT system has a 10% failure rate in weekly maintenance checks. What is this?" Options: A) KRI. B) KCI. C) KPI. **Correct: B.** It is measuring the effectiveness of a *control* process (maintenance).
- **The RCSA Illusion:** "RCSAs are reliable because they are performed by the people closest to the risk." **FALSE.** RCSAs are notorious for bias (underestimating the likelihood of boring, frequent failures).
- **AND vs OR Gates:** In a Fault Tree, an **AND** gate *multiplies* probabilities (lowers total risk); an **OR** gate *adds* probabilities (increases total risk). Don't let GARP flip the math on you.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
