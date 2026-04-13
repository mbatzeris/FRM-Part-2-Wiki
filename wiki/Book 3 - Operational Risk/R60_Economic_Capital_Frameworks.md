# R60 — Practices and Issues in Economic Capital Frameworks

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.60.1` | **Eclectic Risk Measures:** Every measure has a flaw. **VaR** is not coherent (violates *subadditivity*). **Standard Deviation** is not coherent (violates *monotonicity*). **Expected Shortfall (ES)** is coherent and stable, but hard to link to a target rating. **Spectral/Distorted** measures are academically coherent but rarely used. | `[THE/MTH]` | Industry sticks to what it can explain to a Board. ES tells you the "average disaster"; VaR tells you the "minimum disaster." The rest is math for math's sake. |
| `P.60.1b` | **Point-in-Time (PIT) vs Through-the-Cycle (TTC):** **PIT** is used to price financial instruments and compute *short-term* expected losses. **TTC** is used for economic capital and strategic decisions because it results in a *lower volatility* of capital requirements over time. | `[ECO/REG]` | You use PIT to trade today, but you use TTC to decide how much buffer cash to lock in the vault for the next five years. |
| `P.60.2` | **The Copula Challenge:** Copulas are superior for modeling joint distributions of different risks, but they suffer from extreme difficulty in **parameterization** and **validation**. | `[MTH]` | Copulas are the "Glue" of risk aggregation. The problem is that the glue behaves differently during a crisis (correlations spike), and we don't have enough data to prove the glue will hold. |
| `P.60.3` | **Benchmarking vs. Reality:** Benchmarking against peers only proves your model is "normal," not that it is "correct." It provides broad comfort but doesn't guarantee the model reflects real-world risk. | `[OPS]` | If everyone is driving toward a cliff at the same speed, benchmarking will tell you your speed is "Optimal." It won't tell you about the cliff. |
| `P.60.4` | **Economic Capital (EC) is Not Enough:** EC must be supplemented with **Stress Testing** to cover the "Gaps" in statistical models, particularly for tail events where historical data is sparse. | `[REG/BCBS]` | EC is your "Daily Shield"; Stress Testing is your "Bunker." You need both because the shield can't stop a meteor. |
| `P.60.5` | **Strategic Applications:** EC is used for **Risk-Based Pricing** (to ensure the price covers the cost of capital), **Credit Portfolio Management** (to hedge deteriorating risks), and **Management Incentives** (to align pay with risk-taking). | `[ECO/OPS]` | EC turns "Risk" into a "Dollar Cost." This allows management to compare the return of a high-risk trade with a low-risk one on an even playing field. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank used simple "Summation" $\sum \text{VaR}_i$ for Economic Capital:** Then the bank would ignore all **Diversification Benefits**. The capital requirement would be overly conservative, as it assumes all risks (Credit, Market, Op) fail at the exact same moment.
- **Variable Flip: If a bank relied 100% on Benchmarking for model validation:** Then the bank would be vulnerable to **Systemic Model Risk**. If the "Industry Standard" model has a flaw, the bank's benchmarking will never find it. Benchmarking only proves the model matches peers, it offers **little comfort that the model reflects reality**.
- **Variable Flip: If a bank tries to use a standard Market Risk VaR model to measure Counterparty Credit Risk:** It will **FAIL**. Market VaR models combine all portfolio positions allowing full cross-offsetting. Counterparty Credit Risk *prohibits* netting across different counterparties and must be computed strictly at the *netting set* level.
- **Variable Flip: If senior management was not committed to the EC framework:** Then EC would become a "compliance exercise" rather than a decision-making tool. Strategic decisions would continue to be made based on "Raw Profit," leading to hidden risk accumulation.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Benchmarking:** Comparing your model inputs/outputs to others. | **Backtesting:** Comparing your model estimates to actual outcomes. |
| **Copulas:** Used for complex joint distribution modeling. | **Spectral Measures:** Academically interesting but practically "Noise." |
| **Risk-Based Pricing:** Maximizing profit relative to capital used. | **Credit Portfolio Management:** Aimed at protecting against risk deterioration. |

## 4. Directional Intuition
- **Model Complexity $\uparrow \rightarrow$ Parameterization Difficulty $\uparrow \rightarrow$ Validation Error Risk $\uparrow$:** The more complex the copula, the more likely you are to "Overfit" it to the wrong data.
- **Senior Management Commitment $\uparrow \rightarrow$ EC Integrity $\uparrow \rightarrow$ Capital Efficiency $\uparrow$:** When the Board uses EC to set limits, the business units are forced to optimize their risk-taking.
- **Economic Integration $\uparrow \rightarrow$ Cross-Risk Correlation $\uparrow \rightarrow$ Diversification $\downarrow$:** In a globalized crisis, the benefit of having "different" risks disappears as everything correlates to 1.0.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Reality" Trap:** Does benchmarking prove a model is accurate? **NO.** It only proves the model is **comparable to peers** and provides broad comparisons, offering *little comfort* that it reflects reality.
- **Model Replication Trap:** Simply re-running a set of algorithms to produce the same set of results is *not considered enough* model validation.
- **Coherent Risk Measure Violations:** 
    - **Standard Deviation** violates *Monotonicity*.
    - **VaR** violates *Subadditivity*.
- **Time Horizon Selection:** Selecting a multi-period RAROC > 1 year might capture a full business cycle, but examiner trap: **risk and return data beyond 1 year is of questionable reliability**.
- **Copula Disadvantage:** What is the main problem with Copulas? Answer: **Difficult validation of parameters and building a joint distribution.**
- **Price vs. Protection:** Is Credit Portfolio Management used to maximize profit? **NO.** It is used to **protect against risk deterioration**. Risk-based pricing is what maximizes profit.
- **Banking Book Interest Rate Risk:** Long-term fixed-income obligations make cash flows indeterminate due to embedded optionality (borrower prepayment option, depositor withdrawal option). 


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
