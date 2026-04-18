# FRM Part 2 — Cross-Domain Boundary Event Templates

> **See also:** [Structural Linkage Map](../wiki/_boundary_events.md) — 10 comprehensive cross-domain event cascades covering all 5 books.
>
> **Purpose:** Train for 2026-trend questions where risks cross domain boundaries.
> **How to use:** Read the vignette, then answer: (1) What is the **root cause** domain? (2) What is the **impact** domain? (3) Where is capital held? (4) What is the Board's first action?

---

## Template 1: Cyber → Liquidity → Reputational

**Vignette:** A Tier-2 bank's cloud-hosted payment processing system suffers a ransomware attack at 09:00 on a business day. The system is offline for 8 hours. During the outage:
- 2,400 corporate payment instructions are queued but unprocessed
- The bank cannot settle its obligations in the real-time gross settlement (RTGS) system
- Social media reports of the outage trigger retail deposit withdrawals of $180M by 16:00
- The bank's LCR drops from 115% to 94%

**Domain Mapping:**

| Layer | Domain | Specific Risk |
|-------|--------|--------------|
| Root Cause | **Operational Risk** | Cyber attack / third-party cloud dependency |
| 1st Impact | **Liquidity Risk** | Settlement failure + deposit outflows |
| 2nd Impact | **Reputational Risk** | Social media amplification |
| Capital Treatment | OpRisk (SMA) | The coding bug / cyber event is the loss event |
| Liquidity Treatment | LCR buffer draw-down | Contingency Funding Plan activation |

**Key Question:** "Which risk should the CRO report to the Board as the *primary* risk event?"  
**Answer:** Operational Risk. The liquidity stress is a *consequence*, not the cause. Misclassifying it as a liquidity event would result in the wrong remediation (adding HQLA vs. fixing cyber controls).

---

## Template 2: Model Risk → Credit Loss → Regulatory Breach

**Vignette:** An AI-based credit scoring model deployed 18 months ago has been systematically underestimating PD for commercial real estate (CRE) loans originated in secondary markets. The model validation team discovers:
- The training data excluded the 2008–2010 period (survivorship bias)
- 340 CRE loans totaling $2.1B are potentially under-provisioned
- If PDs are corrected, the bank's CET1 ratio falls from 11.2% to 10.4% (regulatory minimum: 10.5% including buffers)

**Domain Mapping:**

| Layer | Domain | Specific Risk |
|-------|--------|--------------|
| Root Cause | **Operational Risk** | Model risk — validation failure (SR 11-7 breach) |
| 1st Impact | **Credit Risk** | Understated EL → insufficient provisions |
| 2nd Impact | **Regulatory / Capital** | CET1 breach triggers supervisory action |
| Governance | Three Lines of Defense | 1st Line (lending) relied on flawed model; 2nd Line (validation) failed to catch bias; 3rd Line (audit) should have flagged data exclusion |

**Key Questions:**
1. "Who bears primary accountability?" → **2nd Line** — model validation is their explicit mandate
2. "What is the most immediate action?" → **Regulatory notification** of potential capital breach (not fixing the model — that's important but not *first*)

---

## Template 3: Geopolitical → Credit + Liquidity + Compliance

**Vignette:** New sanctions are announced against Country X at 14:00 UTC. The bank has:
- $450M in trade finance exposure to 12 entities in Country X
- A correspondent banking relationship with Bank X (Country X's largest bank) carrying $85M in nostro balances
- 3 swap positions with Country X sovereign entities (MTM: +$62M for the bank)
- A compliance screening system that requires 48 hours to process full portfolio re-screening

**Domain Mapping:**

| Layer | Domain | Immediate Action |
|-------|--------|-----------------|
| **Priority 1** | **Compliance / Legal** | Freeze all transactions with designated entities — criminal liability risk |
| Priority 2 | **Liquidity** | Assess nostro balance recoverability — $85M potentially trapped |
| Priority 3 | **Credit** | Crystallize swap exposures — counterparties may become restricted |
| Priority 4 | **Operational** | Emergency screening of full portfolio within regulatory timeline |

**The Trap:** Candidates prioritize credit or market risk (the $450M or $62M) over compliance. But **sanctions violations carry criminal penalties** — legal compliance always trumps capital optimization. This tests the constraint hierarchy: `[REG] > [APP] > [ECO]`.

---

## Template 4: Climate Transition → Market + Credit + Strategic

**Vignette:** A government announces a $75/ton carbon tax effective in 18 months. The bank's portfolio includes:
- $3.2B in loans to coal-fired power plants (20-year maturities)
- $800M in green bonds (various renewable energy issuers)
- A proprietary commodity trading desk with natural gas futures positions
- The bank's own operations rely on a coal-powered data center

**Multi-Domain Impact:**

| Domain | Impact | Horizon |
|--------|--------|---------|
| **Credit Risk** | Coal plant loans face stranded asset risk → PD↑, LGD↑ | 6–18 months |
| **Market Risk** | Energy commodity prices reprice → trading book MTM shifts | Immediate |
| **Operational Risk** | Own data center costs increase → OpEx↑ | 12+ months |
| **Strategic Risk** | Reputational pressure to divest vs. contractual obligations to existing borrowers | Ongoing |

**Key Question:** "Which risk is most *immediate*?"  
**Answer:** Market Risk — commodity prices reprice on announcement day. Credit deterioration in the loan book takes months to manifest. The temporal dimension determines the answer.

---

## Template 5: Interest Rate Shock → ALM + Credit + Liquidity (SVB Pattern)

**Vignette:** Interest rates rise 300bps over 12 months. A regional bank holds:
- $18B in HTM securities (agency MBS, average duration 6.2 years)
- Unrealized losses of $2.8B (not reflected in CET1 under HTM accounting)
- A deposit base that is 65% uninsured, concentrated in tech-sector operating accounts
- A social media-driven deposit run begins after unrealized losses are disclosed in a quarterly filing

**Domain Cascade:**

| Sequence | Event | Domain |
|----------|-------|--------|
| 1 | Rates↑ → HTM securities lose value | **Market Risk** (IRRBB) |
| 2 | Unrealized losses disclosed → depositor confidence drops | **Reputational Risk** |
| 3 | Uninsured deposits flee ($4B in 48 hours) | **Liquidity Risk** |
| 4 | Forced sale of HTM securities at loss → losses become realized | **Market Risk** → crystallized |
| 5 | CET1 falls below minimum → FDIC intervention | **Regulatory / Solvency** |

**The Deep Trap:** "The securities are high quality (Treasuries/Agency MBS) so credit risk is minimal."  
This is `[TRUE-IRRELEVANT]`. Credit quality is irrelevant — the loss is **interest rate risk** (duration mismatch). Candidates conditioned to associate "loss" with "credit" miss this entirely.

**Governance Question:** "What should the Board have done *before* the crisis?"  
**Answer:** Established IRRBB limits and hedged duration risk (interest rate swaps). The failure was in ALM governance, not in credit selection.

---

## How to Use These Templates with Antigravity

**Prompt:** *"I'm studying [Template N — topic]. Run a Constraint Layering drill. Add one more conflicting constraint that I haven't considered and ask me to prioritize the Board's response."*

This forces Antigravity to extend the scenario beyond what's written here, keeping the drills fresh and preventing memorization.
