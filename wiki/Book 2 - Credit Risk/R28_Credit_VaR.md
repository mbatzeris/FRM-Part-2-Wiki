# The Boole Scaffold: Reading 28 — Credit Value at Risk

*Source Material: FRM 2026 Part II Book 2 (Hull, Ch. 19)*
*Learning Objectives Covered: 28.a – 28.f*

## 1. Foundational Propositions (Tagged)

| # | Proposition | Tag | Exam Dominance | Trigger Phrase |
|:---|:---|:---:|:---|:---|
| P1 | **Time Horizon:** Market VaR typically uses a 1-day horizon; Credit VaR uses a 1-year horizon. This reflects the relative illiquidity of credit positions and the slow-moving nature of credit events. | `[REG]` | High — A common qualitative differentiator between risk types. | "primary difference in horizon," "regulatory capital period" |
| P2 | **Transition Matrix Logic:** Ratings are assumed independent across periods. A 3-year matrix is the 1-year matrix raised to the 3rd power ($M^3$). Sub-year periods (e.g., 3 months) require the $n$-th root (e.g., $M^{1/4}$). | `[THE]` | Very High — Tests the mathematical mechanics of ratings migration. | "ratings momentum," "independence criteria," "n-year transition" |
| P3 | **Vasicek WCDR:** The Worst-Case Default Rate at confidence $X$ is modeled via a Gaussian copula. The key input is asset/credit correlation ($\rho$), which is proxied by equity return correlation. | `[THE]` / `[REG]` | Absolute — The engine of Basel II IRB capital calculations. | "Gaussian copula model," "equity return proxy," "WCDR" |
| P4 | **CreditRisk+ vs. CreditMetrics:** CreditRisk+ is an actuarial, default-only model (Poisson/Negative Binomial). CreditMetrics is a MTM model accounting for both defaults and rating downgrades. | `[OPS]` | High — Distinguishing between "Default Mode" and "MTM Mode" models. | "actuarial approach," "rating migration," "downgrade loss" |
| P5 | **Spread Risk Strategies:** Constant Level of Risk (sell downgrades, buy original rating) vs. Buy-and-Hold. Buy-and-Hold typically produces higher losses in stress due to downgrade exposure. | `[ECO]` | Medium — Focuses on the behavioral impact of risk management policy. | "rebalancing," "constant risk profile," "buy-and-hold" |

## 2. Constraint Stress-Test (Falsification)

| Proposition | Constraint Flip | Answer Shift |
|:---|:---|:---|
| P2 (Matrix Independence) | The stem mentions "Ratings Momentum" (a recently downgraded firm is more likely to be downgraded again). | The independence assumption fails. Simple matrix multiplication will **underestimate** the probability of extreme downgrade/default. |
| P3 (Vasicek $\rho$) | The credit correlation $\rho$ increases during a slowing economic growth cycle. | WCDR increases sharply. Financial institution risk and required capital jump even if individual PDs remain stable. |
| P4 (Model Mode) | The CRO wants to measure the loss in portfolio value if a counterparty drops from AA to A, but doesn't default. | **CreditRisk+ is invalid** (Default-mode only). The bank MUST use **CreditMetrics** to capture the credit spread impact of the downgrade. |
| P5 (Strategy Choice) | A bank switches from a "Buy-and-Hold" to a "Constant Level of Risk" strategy in a downward-trending credit cycle. | **Credit VaR decreases.** The bank "cuts losses" on downgrades by selling early, avoiding the extreme left-tail of a total default loss. |

## 3. Dependency & Noise Map

**Signal (these matter):**
- **$\rho$ (Correlation):** The "hidden" driver of WCDR. ROE/ROA correlation is the standard Basel proxy.
- **WCDR formula components:** $N[\frac{N^{-1}(PD) + \sqrt{\rho}N^{-1}(X)}{\sqrt{1-\rho}}]$. Note the positive relationship between $\rho$ and WCDR.
- **$\sigma$ in CreditRisk+:** As volatility of the default rate ($\sigma$) increases, the Poisson distribution moves toward Negative Binomial, increasing the likelihood of large numbers of defaults.

**Noise (distractors):**
- **Daily spread updates:** This is mentioned as a "problem" with historical simulation for credit, but is often noise in a question about structural model choice (CreditMetrics vs. CreditRisk+).
- **Notional amounts:** Used for total loss calculation, but irrelevant for determining the *rate* (WCDR) or the model type selection.

**Tensions:**
- **[REG] vs [ECO]**: Basel `[REG]` uses standardized $\rho$ for the IRB approach, while `[ECO]` capital might use internal equity-correlation proxies that are much more reactive to market cycles.

## 4. Directional Intuition
- **Time Horizon $T$ ↑ → Default Probability ↑ → Odds of keeping rating ↓:** Time allows more room for "drift" toward the absorbing state of default.
- **Credit Correlation $\rho$ ↑ → WCDR ↑ → Credit VaR ↑:** Higher correlation destroys the diversification of "independent" default risks.
- **Default Rate Volatility $\sigma$ ↑ → Positive Skew of Loss ↑ → Tail Risk ↑:** Higher $\sigma$ in CreditRisk+ makes extreme clustering of defaults more probable.
- **Constant Risk Strategy → Credit VaR ↓ (relative to Buy-and-Hold):** Active rebalancing (selling losers) truncates the tail of the loss distribution.

## 5. Ambiguity Traps (Anti-Decoder)
- **"Market VaR vs Credit VaR":** Check the horizon. If it's one day, it's market. If it's one year, it's credit. If the tool is "Historical Simulation," it's likely market; if it's "Monte Carlo," it's likely credit.
- **The Matrix Power Rule:** Remember: $M^n$ for extension; $M^{1/n}$ for root. GARP often tests the 3-month (4th root) or 4-year (4th power).
- **CreditRisk+ Skew:** Be careful—CreditRisk+ produces a **positively skewed** distribution (fat tail on the right/loss side) when default correlation increases.
- **Vasicek Proxy:** Remember that Basel's $\rho$ is a proxy for the correlation between **asset returns** (ROA/ROE), not just a binary default correlation.


## 4. Directional Intuition
- **Default Correlation (ρ) ↑ → Credit VaR ↑:** Higher systematic risk pushes the WCDR upward, fattening the tail of the portfolio loss distribution.
- **PD ↑ → EL ↑, but Credit VaR (UL) effect depends on ρ:** Higher individual PD increases EL linearly, but the marginal impact on UL depends on the correlation structure.
- **Portfolio Granularity ↑ → Idiosyncratic Risk ↓ → Closer to Vasicek Asymptote:** The larger and more diversified the portfolio, the closer it converges to the single-factor model prediction.
- **Confidence Level ↑ → WCDR ↑ → Credit VaR ↑ (exponentially):** Moving from 99% to 99.9% dramatically increases the capital charge because the tail is fat.

---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
