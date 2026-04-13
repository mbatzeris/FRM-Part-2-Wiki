# R101 — AI & Stability

**Exam Priority:** 🔴 High (3-4 questions)nd Financial Stability

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.101.1` | **Transformers and Attention:** The "Transformer" architecture (using the **Attention Mechanism**) is the primary supply-side driver of GenAI. It allows models to process data in **Parallel** and focus on the most relevant parts of the input text. | `[MTH/THE]` | It’s like a super-reader who can read every page of a book at counts (Parallel) and instantly highlight the most important sentence (Attention). |
| `P.101.2` | **The Herding Vulnerability:** If many financial institutions use the same "Pre-trained" base models or the same "Alternative Data" sources, they develop identical blind spots and may all "herd" into the same crowded trades at once. | `[MKT/ECO]` | If every ship in the harbor uses the same GPS and that GPS has a 1-degree error, they all hit the same rock at the same time. |
| `P.101.3` | **Vertical Integration & Concentration:** The AI supply chain is highly concentrated in a few "Critical Nodes" (e.g., NVIDIA for chips, AWS/Azure for cloud). A disruption in one node is no longer an "Individual" failure but a "Systemic" one. | `[OPS/ECO]` | You have 1000 banks, but they all rent their "Brain" from the same two landlords. If a landlord turns off the power, 1000 banks go dark. |
| `P.101.4` | **Cyber surface expansion:** GenAI lowers the "barrier to entry" for hackers. It allows for highly sophisticated, automated, and personalized attacks (vishing/phishing) that can erode trust in the financial system. | `[OPS/THE]` | Before, a hacker needed to be a genius. Now, they just need to ask an AI to write a perfect "CEO-impersonation" script. |
| `P.101.5` | **SupTech (Supervisory Technology):** Regulators are using AI to fight AI. Central banks use LLMs to compile statistics, monitor payment systems, and generate inspection reports more rapidly. | `[REG/OPS]` | The "Police" are getting faster cars and better binoculars to keep up with the "Robbers" who are using the same high-tech tools. |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If many institutions use UNIQUE, internally-developed models:** Then the risk of **Correlation/Herding** decreases. The diversity of logic acts as a "Circuit Breaker" for systemic risk.
- **Variable Flip: If there is a shortage of GPUs/Accelerated chips:** AI adoption slowed down, potentially reducing concentration risk but making the firms that *do* have the chips even more powerful (increasing inequality/monopoly).
- **Variable Flip: If a "Malicious Actor" poisons the training data of a popular base model:** This "Data Poisoning" can create a "Backdoor" that affects thousands of downstream applications that fine-tuned the same poisoned model.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Concentration Risk:** Dependence on few Cloud/Chip providers. | **Market Risk:** Dependence on high interest rates (NO). |
| **Market Fragility:** Flash crashes caused by algorithmic herding. | **Market Fragility:** Lack of trading volume (NO: herding happens *because* everyone trades together). |
| **SupTech:** AI tools used by *Regulators*. | **RegTech:** AI tools used by *Banks* to comply with rules. |

## 4. Directional Intuition
- **Model Efficiency (Parallelization) $\uparrow \rightarrow$ Adoption Speed $\uparrow$:** Transformers made AI fast enough to be useful in real-time finance.
- **Data Unstructured-ness $\uparrow \rightarrow$ Operational Risk $\uparrow$:** Dealing with messy, biased, or "hallucinated" data makes models more unpredictable.
- **Vertical Integration $\uparrow \rightarrow$ Systemic Frailty $\uparrow$:** If the cloud provider also owns the model and the chip, they are a "Single Point of Failure" for the global economy.

## 5. Ambiguity Traps (Anti-Decoder)
- **Transformers vs. Prior Models:** RNNs/LSTMs were **Sequential** (slow). Transformers are **Parallel** (fast).
- **Herding:** It’s not just a choice; it’s a **Vulnerability**. Institutions might not even know they are herding because they don't know who else is using the same "Cloud-hosted" model.
- **Maintenance Margin:** In AI stress testing (margin calls), don't focus on *maintenance* margin; focus on the **Volatility of Margin Calls** and the ability to find collateral.
- **SupTech vs. RegTech:**
    - SupTech = **Supervisors** (The Cop).
    - RegTech = **Regulated firms** (the Driver).
- **Disinformation:** AI can spread rumors at the speed of light, leading to "Social-Media driven Bank Runs."
- **Energy Risk:** The massive power needed for AI is now a "Transition Risk" for financial firms in an ESG world.
- **Algorithm Poisoning:** Manipulating the model's logic vs. **Data Poisoning** (manipulating the inputs).
- **Vertical Integration:** When one firm owns the chips, the software, and the delivery platform.
- **Open Source:** Can *increase* competition (more people have the code) but also *increase* correlation (everyone uses the *same* open code).
- **Deepfakes:** Not just videos; also **Audio** (CEO voice clones for fraudulent wire transfers).


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
