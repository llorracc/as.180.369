# Methodology

## Research Design

This study evaluates whether California's Film Tax Credit Program 2.0 (FY2015–16) and Program 3.0 (2020) produced measurable employment or wage effects in motion picture production (NAICS 512110). I use difference-in-differences (DiD) on a state-by-quarter panel (2010–2025), complemented by Synthetic Control Methods (SCM) for robustness.

## Data Sources

### Employment and Wages (QCEW)
- **Source:** BLS Quarterly Census of Employment and Wages (2010–2025)
- **Industry:** NAICS 512110 (Motion Picture and Video Production)
- **Key Variables:** Monthly employment levels (averaged to quarterly), average weekly wages
- **Derived:** Log employment and log wages for regression models

### Migration Validation (ACS)
- **Source:** IPUMS American Community Survey (2009–2023)
- **Variables:** State of current residence (STATEFIP), prior-year residence (MIGPLAC1), person weights (PERWT)
- **Purpose:** Test whether employment changes correspond to actual worker inflows

### Economic Controls
- **GDP Growth:** BEA quarterly GDP by state (year-over-year % change)
- **Unemployment:** BLS state unemployment (quarterly average)
- **Population Growth:** BLS state population (year-over-year % change)

### Control Group Selection

**Primary controls:** Georgia and New York—the only states with motion picture industries comparable in scale to California's. Both maintained stable incentive structures during the study period:
- **Georgia:** 30% credit (20% base + 10% logo bonus) from 2008–2022
- **New York:** 30% base credit from 2009–2022

**SCM donor pool:** New York, Georgia, Louisiana, Florida, Illinois, Pennsylvania

## Empirical Strategy

### 1. Difference-in-Differences

$$Y_{st} = \alpha + \beta_{2015}(CA_s \times Post2015_t) + \beta_{2020}(CA_s \times Post2020_t) + \gamma_s + \delta_t + X_{st} + \varepsilon_{st}$$

Where:
- $Y_{st}$ = log employment or log wages for state $s$ in quarter $t$
- $\beta_{2015}$, $\beta_{2020}$ = treatment effects (coefficients of interest)
- $\gamma_s$ = state fixed effects
- $\delta_t$ = quarter fixed effects
- $X_{st}$ = time-varying controls (GDP growth, unemployment, population growth)
- Standard errors clustered at state level

### 2. Synthetic Control Method

SCM constructs a synthetic California by optimally weighting donor states to minimize pre-treatment distance across predictors (employment, wages, GDP growth, unemployment).

**Pre-treatment windows:**
- 2015 treatment: 2010 Q1 to 2015 Q1 (21 quarters)
- 2020 treatment: 2012 Q1 to 2020 Q2 (34 quarters)

**Inference:** Permutation-based placebo tests rank California's post-treatment deviation against donor states.

### 3. Migration Validation

Net migration = Inflows (workers moving TO California) − Outflows (workers moving FROM California)

This addresses Rickman and Wang's (2020) concern that QCEW employment gains may reflect reclassification rather than genuine job creation.

### 4. Political Timing

Descriptive analysis of proximity between legislative enactments and gubernatorial elections, following Owens and Rennhoff (2024).

**Sources:** California Legislative Information (LegInfo), Secretary of State election records

## Robustness Checks

- Alternative control groups (secondary states: FL, IL, PA, NC)
- Alternative time windows (1, 2, 3-year post-treatment)
- Placebo tests (false treatment dates: 2013, 2017)
- NAICS 5121 aggregation for broader industry coverage

## Methodological Contribution

This approach extends Thom (2018) and Rickman & Wang (2020) by:
1. Extending temporal scope to capture 2015 and 2020 California expansions
2. Integrating ACS migration data to validate employment changes
3. Embedding political-timing analysis to connect economic outcomes with electoral incentives
