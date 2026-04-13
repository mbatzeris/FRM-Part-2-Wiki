"""
Schema Drift Fix: Upgrade Schema A files to include Directional Intuition + Ambiguity Traps.
Also fix R79 (missing Ambiguity Traps only).
"""
import os

wiki_dir = r"c:\Users\user\Documents\FRM 2\wiki\Book 2 - Credit Risk"

# ─── Files needing BOTH Directional Intuition + Ambiguity Traps ───
upgrades_full = {
    "R19_Fundamentals_of_Credit_Risk.md": {
        "di": [
            "- **Leverage (Debt/Equity) ↑ → Insolvency Probability ↑ → Credit Risk ↑:** Higher leverage means a smaller equity cushion, making the balance sheet more fragile to asset value drops.",
            "- **Cash Flow Volatility ↑ → Default Probability ↑:** Even a solvent firm can default if its cash flows are too erratic to meet scheduled payments.",
            "- **Credit Risk Mitigation (Factoring/Insurance) ↑ → Residual Receivables Risk ↓:** Transferring receivables to a factor eliminates the idiosyncratic risk of individual customers.",
        ],
        "at": [
            "- **Insolvency ≠ Default:** A company with negative equity (Liabilities > Assets) can continue operating and paying coupons for years. Insolvency is a balance sheet state; default is a cash flow event. GARP loves this distinction.",
            "- **Bankruptcy ≠ Default:** Bankruptcy is a legal court process — a company may default without filing for bankruptcy, and may file for bankruptcy protection while still current on payments (Chapter 11).",
            "- **\"Largest source of credit exposure\":** Globally = OTC Derivatives (by notional). For a typical US commercial bank = Loans. The scope qualifier in the stem flips the answer.",
            "- **Hedge Funds as Creditors:** Don't assume all creditors want to avoid default. Distressed debt hedge funds actively buy defaulted obligations at a discount, hoping for recovery > purchase price.",
        ],
    },
    "R20_Governance.md": {
        "di": [
            "- **Reporting Line Independence ↑ → Governance Quality ↑ → Regulatory Approval ↑:** The more direct the CRO-to-Board reporting path, the stronger the 2nd Line's integrity.",
            "- **Compensation Tied to Desk P&L ↑ → Risk Manager Independence ↓:** If risk managers are paid bonuses from the trading desk's profits, their \"monitoring\" becomes compromised.",
            "- **Carve-Out Specificity ↑ → Limit Breach Ambiguity ↓:** Well-defined carve-outs prevent endless debates about whether a breach was \"external\" or \"intentional.\"",
        ],
        "at": [
            "- **\"Advisory\" vs. \"Veto\":** Risk managers advise and escalate; they do NOT have veto power over transactions. If a question says a risk manager \"blocks\" a trade, that is a governance violation — the risk manager should escalate to the credit committee.",
            "- **2nd Line Executing Trades:** The 2nd Line (Risk) NEVER executes trades. Even if they spot a VaR breach, the 1st Line (Business) must execute the offsetting trade. This is the most tested governance boundary.",
            "- **\"Dotted-Line\" Trap:** If the stem mentions risk managers reporting to a desk head (even partly), independence is compromised. The CRO must report to the CEO/Board, period.",
            "- **Carve-Out Confusion:** A carve-out does NOT mean the breach is forgiven. It means the breach is explained by an external factor (e.g., FX move) and triggers investigation, not immediate termination.",
        ],
    },
    "R21_Credit_Risk_Management.md": {
        "di": [
            "- **Credit Quality ↓ (Stage 1 → Stage 2) → Provisioning ↑↑:** The jump from 12-month EL to Lifetime EL under IFRS 9 creates a P&L cliff — even a small downgrade triggers massive provisioning increases.",
            "- **Portfolio Diversification ↑ → Unexpected Loss (UL) ↓:** Spreading exposure across industries reduces concentration, lowering the variance of the loss distribution.",
            "- **Delinquency Days ↑ → Asset Classification ↓:** Each threshold (30, 60, 90 days) moves the loan down the classification spectrum, triggering progressively heavier provisioning.",
        ],
        "at": [
            "- **EL vs. UL Placement:** Expected Loss goes in *provisions* (numerator of RAROC). Unexpected Loss goes in *Economic Capital* (denominator). Mixing them up is the #1 credit risk exam error.",
            "- **IFRS 9 Stage 2 Trigger:** The move from Stage 1 to Stage 2 does NOT require a default or a specific number of delinquency days — it requires a \"significant increase in credit risk\" (SICR), which is a judgment call.",
            "- **90-Day Rule:** Loans delinquent > 90 days are classified as non-performing (Stage 3). But a loan can be Stage 2 at 30 days if the bank judges the risk has \"significantly increased.\"",
            "- **\"Loss\" Classification:** A loan classified as \"Loss\" is fully written off. Don't confuse with \"Doubtful\" — which means the bank expects a loss but hasn't confirmed the amount.",
        ],
    },
    "R22_Capital_Structure_in_Banks.md": {
        "di": [
            "- **Default Correlation (ρ) ↑ → Portfolio UL ↑ → Economic Capital ↑:** Clustering of defaults destroys diversification and pushes the tail of the loss distribution outward.",
            "- **Confidence Interval ↑ → Economic Capital ↑ (exponentially for fat tails):** Moving from 99.5% to 99.9% can more than double the required capital for credit portfolios.",
            "- **Number of Obligors ↑ → Idiosyncratic Risk ↓ → Portfolio UL ↓ (if correlation is low):** Diversification works only when defaults are not perfectly correlated.",
        ],
        "at": [
            "- **EL in Capital:** Does Expected Loss belong in Economic Capital? **NO.** EL is priced into the loan spread and covered by reserves. EC covers only UL.",
            "- **Sum of ULs ≠ Portfolio UL:** Individual ULs are NOT additive. Portfolio UL < Sum(Individual ULs) due to diversification unless ρ = 1.",
            "- **\"99.97% confidence\":** This is the typical A-rated bank target. Don't confuse with 99.9% (Basel IRB) or 99.5% (Solvency II). The confidence level determines which quantile of the loss distribution you must capitalize.",
            "- **Beta Distribution:** The loss rate is modeled using a Beta distribution (bounded 0-1), NOT a Normal distribution (which can go negative).",
        ],
    },
    "R23_Intro_to_Credit_Risk_Modeling.md": {
        "di": [
            "- **PD ↑ → Basel IRB ρ ↓:** Counter-intuitive but critical. High-PD obligors fail for idiosyncratic reasons (micro), so the systemic correlation factor is reduced. Low-PD (AAA) obligors only fail in macro crises → high ρ.",
            "- **Asset Volatility (σ_V) ↑ → Distance to Default ↓ → PD ↑:** Higher volatility makes it easier for the asset value to breach the debt barrier in the Merton model.",
            "- **Debt/Asset Ratio ↑ → Default Barrier ↑ → Distance to Default ↓:** Higher leverage raises the \"trip wire\" closer to the current asset value.",
        ],
        "at": [
            "- **Basel IRB ρ vs. PD:** GARP's most tested tension. High-PD bonds get LOWER correlation under Basel, not higher. The reasoning: junk bonds default due to company-specific problems, not macro events.",
            "- **Merton vs. KMV:** Merton uses N(d2) for PD (standard normal). KMV maps Distance to Default to an empirical default frequency (EDF), which is more accurate for real-world tails.",
            "- **CreditRisk+ vs. CreditMetrics:** CreditRisk+ = Default-mode only (Poisson). CreditMetrics = Mark-to-Market (rating transitions, copulas). If the question mentions \"downgrade losses\" → CreditMetrics. If \"actuarial\" → CreditRisk+.",
            "- **Private Firms & Merton:** Structural models REQUIRE observable equity prices. For private firms with no public equity, Merton cannot be used directly — KMV or reduced-form models must substitute.",
            "- **CAMEL vs. CAMELS:** The S stands for \"Sensitivity to Market Risk\" — added later. If the question says \"CAMEL\" (5 letters), it's the original. \"CAMELS\" (6) is the expanded version.",
        ],
    },
}

# ─── Files needing ONLY Ambiguity Traps (already have DI) ───
upgrades_at_only = {
    "R24_Credit_Scoring_and_Rating.md": [
        "- **Accuracy Ratio (AR) = 2 × AUC - 1:** A perfect model has AR = 1; a random model has AR = 0. Don't confuse AR with the ROC curve itself.",
        "- **Through-the-Cycle (TTC) vs. Point-in-Time (PIT):** Rating agencies use TTC (stable but slow). Internal bank models often use PIT (volatile but accurate). GARP tests which is appropriate for pricing (PIT) vs. capital (TTC).",
        "- **Type I vs. Type II Errors:** Type I = Rejecting a good borrower (lost revenue). Type II = Accepting a bad borrower (credit loss). Banks generally care more about Type II.",
    ],
    "R25_Retail_Credit_Risk.md": [
        "- **Pool-Level vs. Individual Modeling:** Retail credit risk is modeled at the pool level (segments of similar borrowers), not individual obligor level like corporate credit. This is because individual retail exposures are too small.",
        "- **Behavioral Scoring vs. Application Scoring:** Application scoring is at origination (static). Behavioral scoring uses post-origination data (dynamic) and is more predictive of actual default.",
        "- **Loss Forecasting Horizon:** Retail models typically use a 12-month horizon for EL estimation, aligning with IFRS 9 Stage 1.",
    ],
    "R26_Country_Risk.md": [
        "- **Sovereign Default ≠ Country Risk:** Sovereign default is the government failing to pay. Country risk includes transfer risk (capital controls), political risk, and macroeconomic risk — it's broader than just sovereign default.",
        "- **Transfer Risk:** Even if a borrower is willing and able to pay in local currency, capital controls may prevent conversion to the lender's currency. This is transfer risk, not credit risk.",
        "- **Composite Risk Ratings:** Country risk scores blend quantitative (GDP, debt/GDP) and qualitative (political stability) measures. Don't assume the quantitative score alone determines the rating.",
    ],
    "R27_Estimating_Default_Probabilities.md": [
        "- **Hazard Rate vs. PD:** The hazard rate is the instantaneous conditional default rate. PD over a period T = 1 - e^(-λT) where λ is the hazard rate. They're related but not identical.",
        "- **Risk-Neutral vs. Real-World PD:** Market-implied PDs (from CDS/bonds) are risk-neutral and typically HIGHER than historical PDs because they include a risk premium. Use risk-neutral for pricing (CVA), historical for capital.",
        "- **Rating Migration Matrices:** These are Markov chains — the probability of moving from BBB to BB next year is independent of whether the firm was AA two years ago. This \"memoryless\" property is an assumption, not a fact.",
        "- **The \"Term Structure of PD\":** Cumulative PD rises with time. Marginal (forward) PD can rise or fall depending on the credit curve shape. An inverted credit curve implies high near-term risk.",
    ],
    "R29_Portfolio_Credit_Risk.md": [
        "- **Granularity Adjustment:** Corrects the Vasicek single-factor model for finite portfolio size. The adjustment INCREASES capital requirements because smaller portfolios retain more idiosyncratic risk.",
        "- **Vasicek Formula Inputs:** WCDR requires PD, ρ (asset correlation), and the confidence level. It does NOT require LGD — LGD is multiplied AFTER computing WCDR to get Credit VaR.",
        "- **Single-Factor Limitation:** The Vasicek model assumes a single systematic factor drives all correlations. In reality, sector-specific factors exist, which is why portfolio-specific adjustments are needed.",
    ],
    "R30_Credit_Risk.md": [
        "- **Spread Risk vs. Default Risk:** Credit spread movements cause MTM losses even without default. Under FRTB, spread risk is captured in the ES model while jump-to-default is captured by the DRC.",
        "- **Credit Migration Risk:** A downgrade from A to BBB is a credit event that causes MTM losses, even though no default occurred. CreditMetrics captures this; CreditRisk+ does not.",
        "- **Recovery Rate Uncertainty:** LGD is not fixed — recovery rates vary by seniority, collateral, and economic conditions. Stressed LGD in a downturn can be 20-30% lower than historical average.",
    ],
    "R31_Credit_Derivatives.md": [
        "- **CDS Buyer = Protection Buyer = Short Credit:** Buying a CDS is equivalent to shorting the reference entity's credit. The CDS buyer pays a premium and profits if spreads widen or default occurs.",
        "- **Cheapest-to-Deliver (CTD) Option:** In physically settled CDS, the protection buyer can deliver the cheapest eligible bond. This CTD option makes CDS slightly more valuable than implied by a single bond's spread.",
        "- **CDS-Bond Basis:** Basis = CDS Spread - Bond Spread. A negative basis means the CDS is \"cheap\" relative to the bond — potential arbitrage. During the GFC, basis went massively negative due to liquidity.",
        "- **Index CDS vs. Single-Name CDS:** Index CDS (CDX, iTraxx) are standardized and more liquid. Single-name CDS are customized and less liquid but more precise for hedging specific exposures.",
    ],
    "R40_Structured_Credit_Risk.md": [
        "- **Equity vs. Senior Correlation Sensitivity:** Equity tranche is LONG correlation (benefits from ρ↑). Senior tranche is SHORT correlation (hurt by ρ↑). Mezzanine sensitivity is non-monotonic.",
        "- **Subordination ≠ Safety:** Just because a tranche has 30% subordination doesn't mean it's safe. If default correlation is high, losses can bypass the equity tranche and directly hit mezzanine/senior.",
        "- **Gaussian Copula Limitation:** The Gaussian copula underestimates tail dependence — it assumes extreme co-defaults are rarer than they actually are. This was the core model failure of the 2008 crisis.",
        "- **Attachment/Detachment Points:** Know how to read them. A 3-7% mezzanine tranche means it starts absorbing losses after the first 3% of the pool defaults and is wiped out at 7%.",
    ],
    "R41_Intro_to_Securitization.md": [
        "- **SPV Bankruptcy Remoteness:** The SPV is legally isolated from the originator. If the originator goes bankrupt, the SPV's assets are NOT part of the bankruptcy estate. This is the entire point of securitization.",
        "- **True Sale vs. Synthetic:** In a true sale, the originator transfers ownership of the assets. In a synthetic, the originator retains the assets but transfers credit risk via CDS. The balance sheet treatment differs dramatically.",
        "- **Overcollateralization vs. Subordination:** Both provide credit enhancement. OC = more assets than liabilities in the SPV. Subordination = junior tranches absorb losses first. They can coexist.",
        "- **FRTB Treatment:** Under FRTB, securitized products MUST use the Standardized Approach — internal models are prohibited. This is a bright-line regulatory rule.",
    ],
}

# ─── R28: Needs DI only (already has AT) ───
r28_di = [
    "- **Default Correlation (ρ) ↑ → Credit VaR ↑:** Higher systematic risk pushes the WCDR upward, fattening the tail of the portfolio loss distribution.",
    "- **PD ↑ → EL ↑, but Credit VaR (UL) effect depends on ρ:** Higher individual PD increases EL linearly, but the marginal impact on UL depends on the correlation structure.",
    "- **Portfolio Granularity ↑ → Idiosyncratic Risk ↓ → Closer to Vasicek Asymptote:** The larger and more diversified the portfolio, the closer it converges to the single-factor model prediction.",
    "- **Confidence Level ↑ → WCDR ↑ → Credit VaR ↑ (exponentially):** Moving from 99% to 99.9% dramatically increases the capital charge because the tail is fat.",
]


def insert_sections(filepath, di_lines=None, at_lines=None):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the insertion point: before the Cross-Domain Linkage footer
    marker = "---\n**Cross-Domain Linkage:**"
    marker_alt = "---\r\n**Cross-Domain Linkage:**"
    
    if marker_alt in content:
        insert_marker = marker_alt
    elif marker in content:
        insert_marker = marker
    else:
        print(f"  WARNING: No footer marker found in {os.path.basename(filepath)}")
        return False

    insert_text = ""
    if di_lines:
        insert_text += "\n## 4. Directional Intuition\n"
        for line in di_lines:
            insert_text += line + "\n"
        insert_text += "\n"
    if at_lines:
        insert_text += "## 5. Ambiguity Traps (Anti-Decoder)\n"
        for line in at_lines:
            insert_text += line + "\n"
        insert_text += "\n"

    content = content.replace(insert_marker, insert_text + insert_marker)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return True


count = 0

# Full upgrades (DI + AT)
for fname, data in upgrades_full.items():
    fpath = os.path.join(wiki_dir, fname)
    if insert_sections(fpath, di_lines=data["di"], at_lines=data["at"]):
        count += 1
        print(f"OK {fname} -- added DI + AT")

# AT-only upgrades
for fname, at_lines in upgrades_at_only.items():
    fpath = os.path.join(wiki_dir, fname)
    if insert_sections(fpath, at_lines=at_lines):
        count += 1
        print(f"OK {fname} -- added AT")

# R28: DI only
r28_path = os.path.join(wiki_dir, "R28_Credit_VaR.md")
if insert_sections(r28_path, di_lines=r28_di):
    count += 1
    print(f"OK R28_Credit_VaR.md -- added DI")

# R79: AT only (in Book 4)
r79_path = r"c:\Users\user\Documents\FRM 2\wiki\Book 4 - Liquidity Risk\R79_Liquidity_Transfer_Pricing.md"
r79_at = [
    "- **FTP != Market Rate:** FTP is an internally set transfer rate, not an external market rate. It should reflect the bank's marginal cost of funds for a specific tenor, not the SOFR/LIBOR rate directly.",
    "- **Behavioral vs. Contractual Maturity:** Demand deposits are contractually overnight but behaviorally multi-year. FTP should use the behavioral maturity, or the bank will undervalue deposit funding.",
    "- **Profit Center Trap:** If a branch shows high profit in the FTP system, it may just mean FTP credits are set too generously -- not that the branch is genuinely profitable. FTP distortions create illusory performance.",
    "- **Liquidity Premium in FTP:** FTP should include a liquidity premium component for illiquid assets. If it doesn't, business units will originate long-dated illiquid loans because they appear cheap to fund internally.",
]
if insert_sections(r79_path, at_lines=r79_at):
    count += 1
    print(f"OK R79_Liquidity_Transfer_Pricing.md -- added AT")

print(f"\n--- Total files upgraded: {count} ---")
