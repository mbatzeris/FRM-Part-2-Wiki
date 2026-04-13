# R100 — AI and Machine Learning in Financial Services

**Exam Priority:** 🔴 High (3-4 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.100.1` | **The Triad of Learning:** ML is categorized into **Supervised** (labeled data), **Unsupervised** (unlabeled patterns/clusters), and **Reinforcement Learning** (optimization through rewards/punishments). | `[THE/MTH]` | Supervised is like a student with a teacher (Answer Key). Unsupervised is a student exploring a library on their own. Reinforcement is a student playing a video game until they win. |
| `P.100.2` | **The Explainability Gap:** Advanced models (like Deep Learning) provide high accuracy but low **Interpretability**. In finance, this "Black Box" nature creates Model Risk, as managers may not understand why a model is suddenly making huge losing trades. | `[OPS/THE]` | You have a genie that gives the right answer 99% of the time, but it won't tell you *how* it knows. When it finally gives a wrong answer, you won't know it's wrong until the money is gone. |
| `P.100.3` | **Concentration Risk (Big Tech):** Financial stability is increasingly dependent on a very small number of AI service providers (e.g., Cloud giants). A failure at one of these providers could trigger a systemic collapse across the entire "AI-driven" financial sector. | `[ECO/MKT]` | Everyone is using the same "Brain" (Cloud Provider). If that brain gets a headache, the whole world's financial system trips over. |
| `P.100.4` | **Market Fragility:** AI-driven trading can lead to "Flash Crashes" or sudden liquidity evaporate. If many models use the same data and logic, they might all "run for the exit" simultaneously during a stress event. | `[MKT/ECO]` | It’s "Digital Groupthink." If every AI robot is programmed to sell when a certain line is crossed, they all sell at the same microsecond, and the market price disappears. |
| `P.100.5` | **Governance and Human-in-the-Loop:** Regulators emphasize that AI should not be fully autonomous; "Human Oversight" is required to ensure ethical use, bias mitigation, and data quality. | `[REG/OPS]` | Don't let the car drive itself without a driver in the seat. The AI does the work, but a human must be there to "Hit the Brakes" if things go weird. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a model is "Overfitted" to historical data:** It will perform perfectly on the training set but **Fail miserably** on new, unseen data. It has "memorized" the past instead of "learning" the underlying rules.
- **Variable Flip: If the underlying "Concept" in the market changes (Concept Drift):** A model trained on a low-interest-rate environment will become **Inaccurate** when rates rise, as the old relationships no longer hold.
- **Variable Flip: If training data is Biased (e.g., historical lending bias):** The AI will **Automate and Accelerate** that bias, potentially leading to legal and reputational disaster for the firm.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Explainability:** Understanding *why* a model made a choice. | **Accuracy:** How often the model is "correct" (NO: high accuracy can hide low explainability). |
| **Concept Drift:** Change in statistical properties of the target. | **Data Leakage:** Information from the future in training data (NO: that's a training error). |
| **Model Transparency:** Disclosing how the model works. | **Model Opacity:** The "Black Box" nature (NO: this is the risk, not the solution). |

## 4. Directional Intuition
- **Model Complexity $\uparrow \rightarrow$ Explainability $\downarrow$:** The more "Neurons" and layers you add, the harder it is for a human auditor to understand the logic.
- **Data Quality $\downarrow \rightarrow$ Algorithmic Bias $\uparrow$:** "Garbage In, Garbage Out." If you give the AI trash data, its "rational" conclusions will be trash.
- **Regulatory Scrutiny $\uparrow \rightarrow$ Deployment Time $\uparrow$:** Strict oversight on fairness and transparency slows down the launch of new AI tools.

## 5. Ambiguity Traps (Anti-Decoder)
- **Explainability vs. Interpretability:** 
    - **Interpretability** is about the model's *structure* (e.g., a simple tree). 
    - **Explainability** is about *post-hoc* techniques to figure out what a complex model was thinking.
- **Concentration Risk:** It's not just about "Many banks using AI"; it's about "Many banks using the **SAME** AI provider."
- **Deepfakes:** A new form of **Market Manipulation**. Using AI to fake a CEO's voice to crash a stock.
- **Margin Calls:** AI can speed up the "Death Spiral" of margin calls by calculating and demanding collateral faster than humans can react.
- **Model Risk Management:** Always treat AI models as "Assets with potential liabilities," requiring constant validation and stress testing.
- **Supervised vs. Unsupervised:** Look for the **Labels**. If there across "No Labels," it's Unsupervised (Clustering).
- **Reinforcement Learning:** Keywords: "Agent," "Environment," "Reward," "Policy."
- **The "Black Box" Problem:** It's the #1 reason regulators are nervous about AI in systemic banking.
- **NBFI (Non-Bank Financial Intermediaries):** High heavy users of AI, often with less regulation than traditional banks.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
