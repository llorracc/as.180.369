# Results

## 4.1 Model 1: Baseline Specification

![Figure 1: Model 1 - Baseline](figures/model1.png)

The baseline regression yields the following estimates:

$$\widehat{GDP}_i = 7663.03 + 80.56 \times TrainingCost_i$$

| Parameter | Estimate | Std. Error | t-statistic | p-value | 95% CI |
|-----------|----------|------------|-------------|---------|--------|
| Intercept ($\beta_0$) | 7,663.03 | 3,995.80 | 1.918 | 0.066 | [-535.68, 15,861.74] |
| Training Cost ($\beta_1$) | 80.56 | 11.90 | 6.767 | <0.001 | [56.14, 104.99] |

**Model Fit:** R² = 0.629, Adjusted R² = 0.615, F-statistic = 45.80 (p < 0.001), N = 29

The coefficient on training cost ($\beta_1$ = 80.56) is statistically significant at conventional levels (t = 6.77, p < 0.001). The point estimate suggests that a €1 increase in average training expenditure per employee is associated with approximately €80.56 higher GDP per capita. The model explains approximately 62.9% of the cross-national variation in GDP per capita. However, this coefficient should not be interpreted causally. The substantial explanatory power in a bivariate model is itself suggestive of omitted variables that correlate with both training investment and GDP.

---

## 4.2 Model 2: Controlling for Educational Attainment

![Figure 2: Model 2 - Education Control](figures/model2.png)

$$\widehat{GDP}_i = -11,380 + 69.33 \times TrainingCost_i + 561.90 \times Education_i$$

| Parameter | Estimate | Std. Error | t-statistic | p-value | 95% CI |
|-----------|----------|------------|-------------|---------|--------|
| Intercept ($\beta_0$) | -11,380 | 11,400 | -0.996 | 0.329 | [-34,900, 12,100] |
| Training Cost ($\beta_1$) | 69.33 | 13.39 | 5.176 | <0.001 | [41.80, 96.86] |
| Tertiary Education ($\beta_2$) | 561.90 | 306.39 | 1.834 | 0.078 | [-67.90, 1,191.69] |

**Model Fit:** R² = 0.638, Adjusted R² = 0.610, F-statistic = 22.89 (p < 0.001), N = 29

After controlling for tertiary educational attainment, the association between training investment and GDP per capita remains positive and highly statistically significant. The estimated coefficient on training expenditure declines from 80.56 in the baseline model to 69.33, an attenuation of approximately 14 percent. The coefficient on tertiary education itself is positive but only marginally statistically significant (p = 0.078). The comparison between Models 1 and 2 suggests that training investment is not merely a proxy for education, but captures complementary aspects of productive capacity such as skill upgrading and organizational learning.

---

## 4.3 Model 3: Region Fixed Effects

![Figure 3: Model 3 - Region Fixed Effects](figures/model3.png)

$$\widehat{GDP}_i = 9396.40 + 33.81 \times VCT_i + 24070 \times Nordic_i + 3662.56 \times Southern_i + 23970 \times Western_i$$

Relative to the baseline model, the estimated slope on training cost declines sharply—from 81.67 to 33.81 once region fixed effects are included—indicating that a substantial portion of the raw training–GDP gradient reflects cross-region income differences. Model 3 explains a substantial share of cross-country variation (R² = 0.707, Adjusted R² = 0.653).

The key result: even after controlling for region, the VCT coefficient stays positive ($\hat\beta_1$ = 33.81). Countries spending more on vocational training tend to have higher GDP per capita *within regions*, not just because richer regions spend more overall. The estimate is not statistically tight in this small sample (N = 27), and multicollinearity inflates standard errors, but the magnitude remains economically meaningful (about €3.4k higher GDP per capita for a €100 increase in VCT per employee).

---

## 4.4 Model 4: Region-Heterogeneous Effects

![Figure 4: Model 4 - Region Interactions](figures/model4.png)

Model 4 allows the VCT–GDP slope to vary by region through interaction terms. Holding education constant, $\hat\beta_1$ measures how GDP per capita co-moves with VCT within Western Europe. For other regions, interaction terms $\hat\delta_k$ indicate whether the VCT–GDP slope is steeper or flatter than Western Europe.

The results imply that the VCT–GDP relationship is not uniform across regions, consistent with region-specific institutions (training systems, labor market structure, sector mix) shaping how training expenditure relates to income. A negative regional slope should be read as a conditional correlation—potentially reflecting reverse causality or omitted factors—rather than evidence that training causally reduces GDP.

---

## 4.5 Model 5: Firm Size Composition Controls

![Figure 5: Training Investment by Firm Size](figures/model5.png)

$$\text{GDP per capita} = 43,409.5 + 71.1 \times \text{TrainingCost} + 343.3 \times \text{Education} - 53,021.9 \times \text{MidFirm} - 64,278.8 \times \text{LargeFirm} + \varepsilon$$

Training investment varies systematically by firm size: large firms (250+ employees) invest approximately €580 per employee compared to €310 for medium firms and €200 for small firms. This raises the concern that the training-GDP relationship could be spurious if wealthier countries simply have more large firms that invest heavily in training.

The results alleviate this concern. After controlling for tertiary education and firm size composition, the training coefficient remains highly significant (β = 71.08, p < 0.001) and decreases only 4.8% from Model 2 (β = 74.68). Neither the MidFirm nor LargeFirm variables achieve significance (p = 0.623 and p = 0.302), though the high condition number (18,600) suggests multicollinearity may affect these estimates. The model maintains strong explanatory power (R² = 0.679, Adjusted R² = 0.620).

The stability of the training coefficient across specifications provides evidence that firm size composition does not drive the training-GDP relationship. Each additional euro invested in training per employee is associated with approximately €71 higher GDP per capita, independent of industrial structure.

---

## 4.6 Model 6: Stratified Regressions by Firm Size

![Figure 6: Stratified Regression by Firm Size](figures/model6.png)

**Small Firms (10-49 employees):**
$$\text{GDP per capita} = -2,162.7 + 117.8 \times \text{TrainingCost}_{small} + 263.1 \times \text{Education} + \varepsilon$$

**Medium Firms (50-249 employees):**
$$\text{GDP per capita} = -8,361.0 + 80.2 \times \text{TrainingCost}_{mid} + 443.8 \times \text{Education} + \varepsilon$$

**Large Firms (≥250 employees):**
$$\text{GDP per capita} = -13,509.0 + 40.9 \times \text{TrainingCost}_{large} + 694.8 \times \text{Education} + \varepsilon$$

| Firm Size | Training β | Education β | R² | p-value (Training) |
|-----------|------------|-------------|-----|-------------------|
| Small (10-49) | 117.75 | 263.09 | 0.694 | <0.001 |
| Mid (50-249) | 80.21 | 443.77 | 0.669 | <0.001 |
| Large (≥250) | 40.88 | 694.80 | 0.553 | 0.001 |

The stratified analysis reveals diminishing marginal returns as firm size increases. Small firm training yields the highest coefficient (β = 117.8), nearly three times larger than large firms (β = 40.9), with medium firms falling in between (β = 80.2). All three coefficients are statistically significant (p < 0.001 for small and medium; p = 0.001 for large), confirming that training is productive across all firm sizes. However, model fit weakens for larger firms (R² = 0.553) compared to small firms (R² = 0.694), suggesting greater heterogeneity in how large firms translate training into economic output.

This pattern may reflect several mechanisms. Small firms likely target training more precisely to immediate skill gaps, while large firms may invest in broader programs with more diffuse returns. Additionally, small firm training investments represent a larger proportional commitment, potentially signaling stronger organizational investment in human capital.

---

## 4.7 Summary: Coefficient Stability Across Specifications

| Model | Specification | Training β | p-value | R² |
|-------|--------------|------------|---------|-----|
| 1 | Baseline | 80.56 | <0.001 | 0.629 |
| 2 | + Education | 69.33 | <0.001 | 0.638 |
| 3 | + Region FE | 33.81 | 0.114 | 0.707 |
| 5 | + Firm Size | 71.08 | <0.001 | 0.679 |

The training coefficient remains positive across all specifications, though magnitude and significance vary. The largest attenuation occurs with region fixed effects (Model 3), suggesting regional factors account for a substantial portion of the training-GDP association. However, controlling for firm size composition (Model 5) produces minimal attenuation from Model 2, indicating industrial structure does not confound the relationship.
