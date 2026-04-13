# R11 — Regression Hedging and Principal Component Analysis (PCA)

**Exam Priority:** 🟡 Medium (1-2 questions) and Principal Component Analysis (PCA)

## 1. Foundational Propositions
| ID | Proposition | Mapping | Intuition |
|:---|:---|:---|:---|
| `P.11.1` | **Beyond DV01 Neutrality:** A standard DV01 hedge assumes that all bond yields move by exactly 1 basis point together (Parallel Shift). A **Regression Hedge** acknowledges that different bonds move by different amounts based on their historical relationship ($\beta$). | `[MTH/THE]` | DV01 is a "1-for-1" trade. Regression is a "Custom-weighted" trade based on who is more "volatile" or "sensitive" in the relationship. |
| `P.11.2` | **The Hedge Adjustment Factor ($\beta$):** The regression slope coefficient ($\beta$) scales the DV01 hedge to minimize the variance of the hedged position. Formula: $Hedge\;Amount = \frac{DV01_{Bond}}{DV01_{Hedge}} \times \beta$. | `[MTH/OPS]` | If Bond A always moves 1.2 bp whenever Bond B moves 1 bp, you need 20% more of the hedge to stay balanced. |
| `P.11.3` | **PCA: The Dimensionality Reducer:** Principal Component Analysis takes a complex system (like 30 different yield maturities) and boils it down to just a few uncorrelated "Factors" that explain most of the movement. | `[MTH/THE]` | It’s like summarizing a person’s health by just their "Height, Weight, and Pulse" instead of measuring every single bone and muscle. |
| `P.11.4` | **The Big Three PCs:** 
1. **Level:** Entire curve moves up/down (~90% variance). 
2. **Twist:** Slope/Slope change (~8% variance). 
3. **Butterfly:** Curvature/Belly change (~2% variance). | `[MTH/MKT]` | Level is the "Elevator" (whole curve up). Twist is the "Seesaw" (long vs short). Butterfly is the "Bird Flap" (ends vs middle). |
| `P.11.5` | **Uncorrelated Risk:** PCA creates "Principal Components" that are perfectly uncorrelated with each other. This allows risk managers to hedge "Level Risk" separately from "Twist Risk." | `[MTH/REG]` | It separates the "Sound" of the market into different instruments. You can turn down the "Bass" (Level) without affecting the "Treble" (Slope). |

## 2. Constraint Stress-Tests (Falsification)
- **Variable Flip: If you use a DV01 hedge on a non-parallel shift:** The hedge will **Fail**. You will be left with large "Residual Risk" because your assumption (1-for-1 move) was wrong.
- **Variable Flip: If it takes 30 PCs to explain 100% of 30 yields:** PCA has **No Benefit**. The whole point of PCA is that the first **3 PCs** should explain ~98% of the risk.
- **Variable Flip: If a regression uses "Level-on-Level" data instead of "Change-on-Change":** The results will suffer from **High Autocorrelation** in the error terms, making the statistical significance $(\text{t-stats})$ unreliable.

## 3. Dependency & Noise Map
| Signal (Exam Core) | Noise (Distractors) |
|:---|:---|
| **PC1 (Level):** Dominant driver (~90%). | **PC3 (Butterfly):** Dominant driver (NO: it’s only ~2%). |
| **Beta ($\beta$):** Minimizes tracking error/variance. | **Beta ($\beta$):** Maximizes yield (NO). |
| **PCA Factors:** Uncorrelated/Orthogonal. | **PCA Factors:** Highly correlated (NO: they are uncorrelated by design). |

## 4. Directional Intuition
- **Yield Correlation $\uparrow \rightarrow$ PC1 Explanation $\uparrow$:** If all rates move perfectly together, you only need 1 factor (Level) to explain everything.
- **Maturity Gap $\uparrow \rightarrow$ Twist Significance $\uparrow$:** The further apart your bonds are on the curve (e.g., 2Y vs 30Y), the more "Twist" risk you have.
- **Hedge Maturity Match $\uparrow \rightarrow$ Regression $\beta \rightarrow 1.0$:** As your hedge becomes a perfect match for the bond, the custom adjustment vanishes.

## 5. Ambiguity Traps (Anti-Decoder)
- **The "Belly" of the Curve:** This refers to the **3rd Component (Butterfly)**. A butterfly trade involves Shorting the wings (Long/Short ends) and Longing the belly (Middle).
- **Sum of Variances:** The total variance of the PCs equals the total variance of the original yields. No information is "lost" mathematically, just "re-organized."
- **Regression Error Terms:** Pay attention to the "Professor's Note": both level-on-level and change-on-change have correlated errors, but level-on-level is usually worse.
- **Reverse Regression:** Switching X and Y. The best choice depends on your objective (Minimizing Treasury risk vs. Minimizing Bond risk).
- **Eigenvectors:** These represent the "Weighting" of each maturity in a factor. For PC1 (Level), all eigenvector values are positive and similar in size.
- **PC2 (Twist):** The eigenvector has negative values for short maturities and positive values for long maturities (or vice-versa).
- **Hedging with PCA:** To hedge Level risk, you need **one** instrument. To hedge Level and Twist, you need **two** instruments with different maturities.
- **DV01 Assumption:** Parallel shifts ONLY.
- **Factor Loadings:** Another name for the eigenvectors. They tell you how much a specific "PC shock" moves each maturity.
- **Orthogonality:** A fancy math word for "Uncorrelated."
- **Standardized PCA:** Sometimes data is scaled to unit variance before PCA. In the FRM context, we usually use the original yield variances.
- **The "Tuckman" Methodology:** This reading is based on the Tuckman & Serrat textbook.


---
**Cross-Domain Linkage:** [[Boundary Events]](../_boundary_events.md)
