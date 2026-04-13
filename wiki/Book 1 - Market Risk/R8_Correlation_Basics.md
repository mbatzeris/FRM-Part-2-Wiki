# R8 — Correlation Basics

**Exam Priority:** 🟡 Medium (1-2 questions): Definitions and Applications

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.8.1` | **The Diversification Engine:** Correlation ($\rho$) measures the degree to which assets move together. In a portfolio, as $\rho \rightarrow 1$, diversification benefits vanish and **Portfolio VaR** reaches its maximum (the sum of individual VaRs). | `[MKT/MTH]` | Correlation is the "Glue" between assets. If the glue is too strong (high $\rho$), everything breaks together. If the glue is weak, one part can fall without pulling the rest down. |
| `P.8.2` | **Rank Correlation (Spearman/Kendall):** Unlike Pearson correlation (which assumes a linear relationship), Rank correlation focuses on the *order* of observations. It is more robust to outliers and non-linear (but monotonic) relationships. | `[MTH/THE]` | Pearson asks: "How much did you both move?" Rank asks: "Did you both come in 1st and 2nd place?" It’s about the "Line-up," not the "Score." |
| `P.8.3` | **Correlation Swaps:** A derivative where one party pays a fixed correlation and receives the actual realized correlation of a basket of assets over a period. | `[MKT/OPS]` | You are betting on how "Copycat" the market will be. If you think a crash is coming and everything will drop together, you "Buy Correlation" to profit when $\rho$ spikes. |
| `P.8.4` | **Exotic Correlation Options:** 
- **Quanto Option:** Hedging foreign currency risk; lower $\rho$ between asset and FX = higher price.
- **Exchange Option:** Payoff is max(0, $S_2 - S_1$). $\sigma_E = \sqrt{\sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2}$. Lower $\rho \rightarrow$ higher option price.
- **Best-of / Worst-of:** For 'Worst-of' (min of two assets), lower $\rho$ decreases price (unique!). | `[MKT/MTH]` | Best-of: You want the assets to be different so one can "Win big" (Low correlation). Worst-of: You want them to stay together so the "bad one" doesn't drag you down alone (High correlation). |
| `P.8.5` | **Default Term Structure:** For **Investment Grade** (IG) bonds, the probability of default (PD) increases over time. For **High Yield** (HY) bonds, the PD is highest *now* and decreases over time (Survival Bias). | `[MKT/THE]` | IG bonds are "Healthy" now but might get sick over 30 years. HY bonds are "In the ER" now; if they survive tonight, their chances of living for another 10 years go *up*. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If Correlation jumps from 0.2 to 1.0 during a crisis:** Diversification "breaks." A portfolio that looked safe on paper will suddenly lose value much faster than predicted (Systemic Risk).
- **Variable Flip: If a firm has high Concentration Risk (high Concentration Ratio):** Its **Joint Probability of Default** increases significantly, as its fate is tied to just a few large exposures.
- **Variable Flip: If you are Short a Correlation Swap and realized correlation SPIKES:** You lose money. Being "Short Correlation" means you are betting that components in a index will "do their own thing" rather than following each other.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Pearson Correlation:** Linear relationship. | **Spearman Correlation:** Linear relationship (NO: Monotonic/Rank). |
| **Quanto Option:** Correlation between asset and F/X rate. | **Quanto Option:** Correlation between two stocks (NO). |
| **Portfolio VaR:** Increases as correlation increases. | **Portfolio VaR:** Decreases as correlation increases (NO). |

## 4. Directional Intuition
- **Asset Concentration $\uparrow \rightarrow$ Systemic Sensitivity $\uparrow$:** The more "eggs in one basket" the sector has, the easier it is for one drop to break the whole system.
- **CDS Wrong-Way Risk (WWR):** Correlation (Counterparty, Reference Asset) $\uparrow \rightarrow$ CDS Spread $\downarrow \rightarrow$ WWR $\uparrow$. If you buy protection from Deutsche Bank on France, and their default correlation is high, the spread is cheap but the risk is immense.
- **Realized Correlation > Fixed Correlation $\rightarrow$ Correlation Swap Buyer Profit $\uparrow$:** The "copycat" effect was stronger than the market expected.

## 5. Ambiguity Traps (Anti-Decoder)
- **May 2005 (GM/Ford):** This is a classic case of **Correlation Risk**. Hedge funds were "Long Equity Tranche" (which gains when correlation is high) and "Short Mezzanine" (which gains when correlation is low). When correlation shifted unexpectedly, they lost on **BOTH** legs.
- **Quanto Options:** These are NOT about "Quantity." They are "Quantity-adjusted" options to hedge currency risk.
- **Correlation Sensitivity ($\rho$):** 
    - **Multi-asset options** are highly sensitive to correlation. 
    - **Standard single-asset options** have NO correlation sensitivity.
- **Joint Probability of Default (JPD):** $P(A \cap B) = \pi_A \pi_B + \rho_{default} \sqrt{\pi_A(1-\pi_A)\pi_B(1-\pi_B)}$. 
- **Default Correlation vs. Distance to Default (DtD):** Note that DtD is the "buffer" a firm has before hitting the insolvency wall.
- **Spearman ($\rho_s$) vs Kendall ($\tau$):** Both are rank-based. Kendall is usually more complex to calculate but better for smaller samples.
- **The "Worst-case" for a Creditor:** The joint probability of all loans defaulting simultaneously.
- **Systemic Risk:** Note that during a crisis, correlations of **Everything** (Equities, Bonds, International) tend to converge toward 1.0. This is the "Nowhere to hide" effect.
- **Static vs. Dynamic Correlations:** 
    - **Static:** VaR, CDO copulas, binomial default models.
    - **Dynamic:** Pairs trading, stochastic correlation processes, deterministic correlation.
- **Survival Bias:** Why PD decreases for HY bonds? Because the "weakest" ones fail immediately; those left after 5 years are the "strongest" of the bunch.
- **Concentration Ratio:** A measure of "Lumpiness." High ratio = High risk.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
