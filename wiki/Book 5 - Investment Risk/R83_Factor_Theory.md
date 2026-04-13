# R83 — Factor Theory

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.83.1` | **Factors as Bad Times:** Factors represent underlying risks that perform poorly during "bad times." Exposure to these factors earns a risk premium as compensation for enduring those periods. | `[THE/ECO]` | You don't get a "free lunch." You get paid to hold stuff that everyone else wants to dump when the economy is crashing. |
| `P.83.2` | **Asset Bundles:** Most assets (Hedge Funds, PE, Corporate Bonds) are not factors themselves but bundles of factors (Equity, Credit, Volatility, Duration). | `[THE]` | An iPhone isn't a "factor"; it's a bundle of silicon, glass, and software. A hedge fund isn't a factor; it's a bundle of leverage, credit, and equity risk. |
| `P.83.3` | **SDF (Stochastic Discount Factor):** Also known as the **Pricing Kernel (m)**. It is an index of "bad times" weighted by marginal utility. Under the SDF model, the price of an asset is $P_i = E[m \times X_i]$, where $X_i$ is the future payoff. | `[MTH/THE]` | $m$ is a "Correction Factor." If an asset pays off when $m$ is high (bad times, meaning an extra dollar is very valuable), it's very valuable, so its price is high and expected return is low. |
| `P.83.3b` | **SDF Risk Premium Formula:** The expected return vs risk-free rate is $E[R_i] - R_F = \beta_{i,m} \times (\text{price of risk})$, where the price of risk is $-\frac{\text{var}(m)}{E[m]}$. Notice the **negative sign** because an asset that pays off when $m$ is high is valuable and commands a *lower* return. | `[MTH/THE]` | It's the inverse. If you co-move strongly with bad times (high $m$), you are a great hedge, so your risk premium goes down (negative price of risk). |
| `P.83.4` | **CAPM Lesson #6:** Valuable assets have **low risk premiums**. This occurs because their payoffs are high (or positive) during bad times, which makes them highly desirable hedges. | `[THE]` | Insurance is expensive and has a negative expected return. Why? Because it pays off exactly when your house is burning down. |
| `P.83.5` | **EMH and Active Management:** The Efficient Market Hypothesis suggests active managers can't beat the market on average. Information is not free; active managers "work" to make the market efficient by finding and closing gaps. | `[ECO/THE]` | If you see a $20 bill on the sidewalk, it's not "Alpha"; it's a reward for the effort of looking down and picking it up in a crowded city. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If an asset pays off 100% when the market drops 50%:** This asset is **High Value** and should have a **Negative Beta** and a **Low (or negative) Risk Premium**.
- **Variable Flip: If all investors have "Homogeneous Expectations" (CAPM assumption):** Then everyone agrees on the risk/return of every asset, and everyone holds the same **Market Portfolio** (the risky portion of their portfolio).
- **Variable Flip: If "Transaction Costs" are introduced to EMH:** Then "Arbitrage" is no longer perfect. Small mispricings will persist because the cost to trade is higher than the expected profit.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Beta:** Measures an asset's covariance with the market (Factor exposure). | **Standard Deviation:** Measures total risk (Not rewarded in factor models). |
| **SDF (m):** Index of "bad times", acts as marginal utility. | **SDF:** Measures volatility (NO: it specifically weights states by marginal utility). |
| **Behavioral Explanation:** Over/Under-reaction to news causes returns. Can persist due to structural/regulatory barriers. | **Rational Explanation:** High returns = compensation for risk during bad times. |
| **CAPM Shortcomings:** Ignores human capital (labor income risk) and multi-period rebalancing. | **CAPM Shortcomings:** Ignores beta (NO: it relies on beta). |

## 4. Directional Intuition
- **Payoff in Bad Times $\uparrow \rightarrow$ Asset Value $\uparrow \rightarrow$ Expected Return $\downarrow$:** The better it protects you, the more you have to pay for it (and the less "extra" profit you get).
- **Information Cost $\downarrow \rightarrow$ Market Efficiency $\uparrow$:** The easier it is to find news, the faster those news items are priced in, leaving no room for Alpha.
- **Diversification $\uparrow \rightarrow$ Idiosyncratic Risk $\downarrow$:** Across all factor models, diversification is the only "Free Lunch" to remove risk that isn't rewarded.

## 5. Ambiguity Traps (Anti-Decoder)
- **Factors vs. Assets:** Is a "Hedge Fund" a factor? **NO.** It’s an asset class that *contains* factors. Is "The Market" a factor? **YES** (it's a tradeable investment factor).
- **m (SDF) Definition:** Remember: High $m$ = **Bad Times** (Marginal utility of an extra dollar is high when you're poor/jobless). $1/R_F = E[m]$.
- **CAPM Lesson #3:** Does every investor hold the same portfolio? **Yes**, if looking at the *risky* portion. They only differ in how much risk-free asset they hold.
- **EMH vs. Reality:** Does EMH say mispricings never exist? **NO.** It says they are expensive to exploit and don't last. The Grossman-Stiglitz paradox notes that if information was truly free and embedded into prices, no one would have an incentive to collect it.
- **Rational vs. Behavioral:** If someone says "I made 20% because I'm smart and saw the news," that's **Behavioral**. If they say "I made 20% because I held during the 2008 crash," that's **Rational** (compensation for bad times).
- **Linear Pricing:** The SDF model $P = E[m \times X]$ is the fundamental link between price and future payoff $X$.
- **Barriers to Capital:** When testing behavioral efficiency, watch for **Structural barriers** (investors can't legally or physically enter trade) and **Regulatory barriers** (minimum credit rating constraints like holding investment grade only), which allow behavioral biases to persist.
- **Lessons of CAPM:** Don't forget that "Valuable assets have low risk premiums" is a key exam point.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
