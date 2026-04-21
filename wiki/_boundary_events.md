# Boundary Events — Cross-Domain Linkage Index

**Purpose:** This file maps concepts that span multiple readings or books. When a Schema B file links to `[Boundary Events](../_boundary_events.md)`, it points here. Use this index to find which readings share overlapping concepts, competing frameworks, or regulatory tensions.

---

## Cross-Domain Links

| Concept | Readings | Tension / Overlap |
|:--|:--|:--|
| Risk-neutral vs real-world PD | R30, R31 | [THE] vs [REG]: Q-measure PD used in CDS/CVA pricing; P-measure PD used for regulatory capital and stress testing |
| CVA / DVA accounting | R30, R38 | [REG] vs [ECO]: Basel disallows DVA benefit in regulatory capital; accounting standards (IFRS 13) permit it |
| Netting & close-out | R30, R31 | [OPS] vs [REG]: legal enforceability of netting varies by jurisdiction; close-out netting under ISDA Master Agreement reduces gross exposure |
| Default correlation models | R30, R29 | [THE]: reduced-form hazard rate models (tractable, low correlation) vs structural asset-value models (flexible, computationally slow) |
| Gaussian copula for correlated defaults | R30, R31 | [THE]: R30 uses copula for Credit VaR portfolio; R31 applies the same one-factor Gaussian copula to synthetic CDO tranche pricing — same model, different output |
| CDS spread and hazard rate | R31, R38 | [THE] vs [OPS]: R31 derives CDS spread from hazard rate under constant λ assumption; R38 extends to CVA incorporating CDS-implied PD as the market-standard input |
| CDO tranche correlation | R31 | [THE]: compound correlation produces smile (inconsistent); base correlation produces skew (consistent, market standard) — both implied from market tranche prices |
| Synthetic CDO vs cash CDO | R31 | [ECO] vs [REG]: economically equivalent credit exposure; post-2008 Basel III/IV imposes punitive re-securitisation capital charges on synthetic positions at regulated banks |

---

## Boundary Scenarios

Cross-domain event chains where a trigger in one risk type causes downstream effects in another. These are high-priority 2026 exam scenarios per the Ambiguity Training Roadmap (Section 7).

| Trigger | Chain | Risk Types Involved | Readings |
|:--|:--|:--|:--|
| Sovereign default | CDS protection seller pays out → collateral posted is sovereign bonds → collateral value collapses simultaneously → counterparty with sovereign exposure faces margin calls → liquidity drain | Credit → Collateral (Credit) → Liquidity | R30, R31 |
| Correlation spike in crisis | CDO senior tranche losses breach attachment point → forced selling of "safe" assets → market liquidity evaporates → fire-sale losses exceed VaR estimates | Credit (CDO) → Market → Liquidity | R31 |
| Reference entity defaults mid-CDS-forward | CDS forward ceases to exist before start date → hedged position becomes unhedged → residual credit exposure unmitigated | Credit → OPS (contract termination) | R31 |
| Wrong-Way Risk materialises | Counterparty PD rises as bank's exposure rises → CVA increases rapidly → bank's own credit spread widens (DVA rises) → P&L distortion masks true credit deterioration | Credit (CVA/DVA) → Accounting | R30, R38 |

---

*Add rows to Cross-Domain Links when a new reading's §3 Tensions or §5 Ambiguity Traps reference a concept from another reading. Add rows to Boundary Scenarios when a reading introduces a multi-domain event chain (Step 8b of /new-reading workflow).*
