# R68 — Early Warning Indicators

**Exam Priority:** 🟡 Medium (1-2 questions)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.68.1` | **EWI Definition:** Forward-looking, leading metrics that act as "warning lights" on a bank's liquidity dashboard to signal a pending crisis before it occurs. | `[OPS]` | It’s the "Check Engine" light. You want it to turn on *before* the smoke starts coming out of the hood. |
| `P.68.2` | **The Purpose is Escalation:** The ultimate desired outcome of a suggesting EWI is the timely **Escalation** to relevant personnel to initiate remedial action. | `[OPS]` | A warning light is useless if no one looks at it. The indicator must be tied to a definitive "Who do I call?" plan. |
| `P.68.3` | **OCC (2012) — Embedded Options:** A specific regulatory requirement for EWIs to track securities and derivatives with **embedded options** (like callable debt) to flag when these might increase cash outflows. | `[REG/OCC]` | If your debt is "Callable," you need a light that turns on when interest rates drop, signaling the lender is about to take their money back. |
| `P.68.4` | **BCBS (2012) — Intraday Focus:** These guidelines specifically target **Intraday Liquidity** indicators, such as payment timing and daily maximum liquidity availability. | `[REG/BCBS]` | It’s about the "hour-by-hour" plumbing. If slow payments from customers are draining your cash before noon, you need an indicator for that. |
| `P.68.5` | **Threshold Color Coding:** EWIs utilize a stoplight approach: **Green** (Steady State), **Amber** (Increased monitoring/Investigation), and **Red** (Immediate Remediation). | `[OPS]` | This creates a common language for risk levels across the bank. Everyone knows that "Red" means "Act now." |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If a bank focused purely on "Lagging" indicators:** Then the bank would only find out it had a liquidity problem *after* it defaulted on a payment. Lagging indicators tell you "What happened," not "What's about to happen."
- **Variable Flip: If a bank increased "Granularity" without an Escalation Plan:** Then the bank would have a high-resolution view of its own collapse. More data (granularity) does not equal better accuracy or safety without the **Escalation** mechanism.
- **Variable Flip: If a bank used only "External" metrics:** The bank would miss internal signals like a sudden sharp increase in assets or a breach of internal concentration limits (BCBS 2008). A balanced framework requires both Internal and External measurements.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **Leading Indicators:** Forward-looking signals of future trouble. | **Lagging Indicators:** Past data that reports on what already occurred. |
| **Escalation:** The core goal of the EWI framework. | **Granularity:** Sharpens the focus but doesn't guarantee accuracy. |
| **BCBS (2012):** Intraday liquidity guidelines. | **OCC (2012):** Embedded options / advance notice. |

## 4. Directional Intuition
- **Market Spreads $\uparrow \rightarrow$ External EWI Status $\rightarrow$ Amber/Red:** Wide fixed-income spreads suggest the market is losing confidence in the bank's name.
- **Payment Delay $\uparrow \rightarrow$ Intraday EWI Status $\rightarrow$ Red:** If major customers are lagging their transfers, the bank’s intraday buffer might hit zero before EOD.
- **Internal Concentration $\uparrow \rightarrow$ BCBS 2008 EWI $\rightarrow$ Alert:** Too many bets on one sector or one funding source increases the risk that one "Bad Event" will trigger a total liquidity collapse.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Accuracy" Trap:** Does more granularity (more detailed data) make an EWI more accurate? **NO.** It makes it "sharper" and harder to ignore, but accuracy depends on the data quality and model logic.
- **Leading vs. Lagging:** Which is better for LikRisk? **LEADING.** Lagging is for reporting; Leading is for surviving.
- **Regulator Mapping:**
    - Who cares about "Embedded Options"? **OCC.**
    - Who cares about "Intraday"? **BCBS (2012).**
    - Who cares about "CAMELS" ratings? **OCC.**
- **Internal vs. External:** If GARP asks if one is more reliable than the other, the answer is **NO.** You need a balance of both.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
