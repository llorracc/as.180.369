# Data and Methods

## 3.1 Data Sources

### 3.1.1 Vocational Training Investment

This study draws on the Eurostat Continuing Vocational Training Survey (CVTS), specifically the dataset *trng_cvt_17s*, which reports the cost of CVT courses by type and firm size class, measured as cost per person employed in all enterprises. The CVTS is conducted every five years across European Union member states and select partner countries, providing standardized cross-national data on employer-sponsored training activities.

The selection of this particular dataset (trng_cvt_17s) over alternative Eurostat training cost measures was deliberate. While Eurostat provides several related indicators—including training costs as a percentage of total labor costs (trng_cvt_16s), costs per participant (trng_cvt_19s), and costs per training hour (trng_cvt_20s)—the cost per person employed metric offers distinct analytical advantages:

1. It captures training investment intensity at the enterprise level without conditioning on training participation, thereby reflecting the overall commitment to workforce development across all employees rather than just training recipients.
2. It enables direct comparison across countries with varying training participation rates, as the denominator (total employment) is standardized.
3. This measure aligns most closely with policy-relevant questions about aggregate training investment and its macroeconomic correlates.

The dataset provides training cost figures denominated in Euros (EUR) for survey years 2005, 2010, 2015, and 2020, disaggregated by firm size categories: small enterprises (10-49 employees), medium enterprises (50-249 employees), and large enterprises (250+ employees). For the baseline analysis, I focus on the 2015 survey year to ensure temporal alignment with complementary economic indicators and to avoid potential confounding from the COVID-19 pandemic's effects on the 2020 data.

### 3.1.2 Economic Output

GDP per capita data are sourced from Eurostat's National Accounts dataset (*tec00001*), which reports gross domestic product at current market prices per inhabitant, denominated in Euros. This indicator serves as the primary dependent variable, capturing cross-national variation in economic productivity and living standards.

### 3.1.3 Sample Construction

The analytical sample comprises 29 European countries for which complete data on training investment and GDP per capita are available for 2015. This sample size represents a significant limitation of the study, as the small number of observations constrains statistical power and limits the number of control variables that can be simultaneously included in regression models without risking overfitting. The countries span considerable heterogeneity in economic development, institutional configurations, and training systems, ranging from Nordic welfare states with extensive employer-sponsored training traditions to Southern and Eastern European economies with more varied vocational training landscapes.

---

## 3.2 Empirical Strategy

### 3.2.1 Model Specifications

**Model 1: Baseline Specification**

The baseline model estimates the bivariate relationship between vocational training investment and economic output:

$$GDP_i = \beta_0 + \beta_1 \cdot TrainingCost_i + \varepsilon_i$$

where $GDP_i$ denotes GDP per capita in country $i$ (measured in Euros for 2015), $TrainingCost_i$ represents average vocational training expenditure per employee across all firm size categories, and $\varepsilon_i$ is the error term.

**Model 2: Education Control**

$$GDP_i = \beta_0 + \beta_1 \cdot TrainingCost_i + \beta_2 \cdot Education_i + \varepsilon_i$$

where $Education_i$ denotes the share of the population with tertiary education.

**Model 3: Region Fixed Effects**

$$GDP_i = \beta_0 + \beta_1 \cdot VCT_i + \sum_{k \neq W} \gamma_k \cdot \mathbf{1}\{Region_i = k\} + \varepsilon_i$$

where region indicators absorb level differences across Nordic, Western, Southern, and Central/Eastern Europe (with Central & Eastern Europe as reference).

**Model 4: Region-Heterogeneous Effects**

$$GDP_i = \beta_0 + \beta_1 VCT_i + \beta_2 Edu_i + \sum_{k \neq W} \gamma_k \mathbf{1}\{Region_i = k\} + \sum_{k \neq W} \delta_k (VCT_i \cdot \mathbf{1}\{Region_i = k\}) + \varepsilon_i$$

where interaction terms allow the VCT–GDP slope to vary by region.

**Model 5: Firm Size Composition Controls**

$$GDP_i = \beta_0 + \beta_1 \cdot TrainingCost_i + \beta_2 \cdot Education_i + \beta_3 \cdot MidFirm_i + \beta_4 \cdot LargeFirm_i + \varepsilon_i$$

where $MidFirm_i$ and $LargeFirm_i$ represent the share of training costs attributable to medium and large firms.

**Model 6: Stratified Regressions by Firm Size**

Separate regressions estimated for small, medium, and large firm training costs:

$$GDP_i = \beta_0 + \beta_1 \cdot TrainingCost_{size} + \beta_2 \cdot Education_i + \varepsilon_i$$

### 3.2.2 Analytical Approach

This parsimonious specification serves as a deliberate starting point for a sequential modeling approach. The primary objective is not to estimate the causal effect of training on GDP—which would require addressing substantial endogeneity concerns—but rather to establish a baseline coefficient ($\beta_1$) that can be tracked across progressively richer specifications. By observing how the training coefficient changes as additional covariates are introduced, we can assess the extent to which the baseline association is attributable to omitted variables versus a more robust relationship.

### 3.2.3 Limitations

Several important limitations warrant acknowledgment:

**Limited sample size.** The cross-sectional design with only 29 observations severely constrains the analysis. With limited degrees of freedom, adding multiple control variables risks overfitting and produces unstable coefficient estimates. This necessitates a parsimonious approach to model specification and caution in interpreting results from more complex models.

**Omitted variable bias.** The baseline model almost certainly suffers from omitted variable bias. Countries with higher GDP per capita may invest more in training due to greater available resources (reverse causality), or both training investment and GDP may be driven by unobserved factors such as institutional quality, technological sophistication, or cultural attitudes toward human capital development. The coefficient $\beta_1$ should therefore be interpreted as a conditional correlation rather than a causal effect.

**Analytical focus on coefficient stability.** Given these concerns, the analytical strategy explicitly prioritizes tracking coefficient stability across specifications over interpreting the magnitude of any single estimate. A coefficient that remains statistically significant and relatively stable as controls are added provides suggestive evidence of a robust relationship, whereas substantial attenuation would indicate that the baseline association largely reflects confounding.
