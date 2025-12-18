# Methodology

## Research Design

This study evaluates whether California's Film and Television Tax Credit Program 2.0 (effective FY2015–16) and Program 3.0 (credit allocations beginning July 1, 2020) produced measurable employment or wage effects in motion picture production (NAICS 512110). I use difference-in-differences (DiD) on a state-by-quarter panel (2010–2025), complemented by Synthetic Control Methods (SCM) for robustness.

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
- Standard errors clustered at state level to account for serial correlation within states and the small number of treatment units (Bertrand, Duflo, & Mullainathan 2004)

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

Descriptive analysis of proximity between legislative enactments and gubernatorial elections, following Owens and Rennhoff (2023).

**Sources:** California Legislative Information (LegInfo), Secretary of State election records

## Robustness Checks

- Alternative control groups (secondary states: FL, IL, PA, NC)
- Alternative time windows (1, 2, 3-year post-treatment)
- Placebo tests (false treatment dates: 2013, 2017)
- NAICS 5121 aggregation for broader industry coverage

## Identification Challenges

### COVID-19 Confounding

The Program 3.0 treatment (July 2020) coincides with COVID-19 pandemic disruptions that severely affected film production nationwide. Production shutdowns, social distancing requirements, and delayed projects created unprecedented employment volatility across all states. This presents a critical identification challenge: observed post-2020 employment changes may reflect pandemic recovery rather than tax credit effects.

I address this concern through several approaches:
1. **SCM matching:** The synthetic control incorporates pandemic-period data from donor states, constructing a counterfactual that partially accounts for common COVID shocks
2. **Control group exposure:** Georgia and New York experienced similar production disruptions, providing a reasonable comparison
3. **Cautious interpretation:** Results for the 2020 treatment should be interpreted with appropriate caution given this confounding

Despite these mitigations, the 2020 estimates remain less reliable than the 2015 estimates, and readers should weight the Program 2.0 findings more heavily.

### Industry Disruptions

Beyond COVID-19, the film industry experienced significant labor disruptions during the study period. The 2007-2008 Writers Guild of America strike affected the pre-treatment baseline, while the 2023 WGA and SAG-AFTRA strikes severely curtailed production in the post-2020 period. These industry-specific shocks compound the challenge of isolating tax credit effects from broader labor market volatility.

### Sample Size Considerations

The three-state DiD panel (192 observations) and six-state SCM donor pool raise statistical power concerns. With limited cross-sectional variation, detecting small effects becomes difficult. The 3-4% employment point estimates from SCM, while not statistically significant, represent approximately 3,300-4,300 jobs at California's employment levels—a potentially meaningful economic effect that this study may lack power to detect. This limitation should inform interpretation: failure to reject the null hypothesis does not establish that the programs had zero effect.

## Methodological Contribution

This approach extends Thom (2018) and Rickman & Wang (2020) by:
1. Extending temporal scope to capture 2015 and 2020 California expansions
2. Integrating ACS migration data to validate employment changes
3. Embedding political-timing analysis to connect economic outcomes with electoral incentives
