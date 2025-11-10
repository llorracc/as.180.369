# Methodology

## Research Objective and Design

This study evaluates whether California's Film and Television Tax Credit Program 2.0 (FY2015–16 launch) and Program 3.0 (credit allocations from July 1, 2020 onward) produced measurable employment or wage effects in the motion picture and video production industry (NAICS 512110).

Following Thom (2018), I use a difference-in-differences (DiD) design on a state-by-quarter panel (2010–2025), comparing California against a control group of states with stable film incentive policies and similar pre-treatment industry trends. For robustness and improved counterfactual validity, I complement DiD with a Synthetic Control Method (SCM) following Rickman and Wang (2020).

## Data Sources

### Employment and Wages:

**Source:** Bureau of Labor Statistics QCEW, quarterly data (2010–2025).

**Industry:** Motion Picture and Video Production (NAICS 512110), consistent with Rickman & Wang's specification.

**Variables Extracted from QCEW:**
- `area_fips`: State FIPS code (filtered for California: 06000, New York: 36000, Georgia: 13000)
- `agglvl_code`: Aggregation level code (filtered to 58 for state-level totals)
- `year`: Year (2010-2025)
- `qtr`: Quarter (1-4)
- `month1_emplvl`, `month2_emplvl`, `month3_emplvl`: Monthly employment levels for each month in the quarter
- `avg_wkly_wage`: Average weekly wage
- `total_qtrly_wages`: Total quarterly wages
- `qtrly_estabs_count`: Quarterly establishment count

**Derived Variables:**
- `employment`: Average quarterly employment, calculated as the mean of `month1_emplvl`, `month2_emplvl`, and `month3_emplvl`
- `avg_weekly_wage`: Directly from `avg_wkly_wage`
- `log_employment`: Natural logarithm of employment (used in regression models)
- `log_wage`: Natural logarithm of average weekly wage (used in regression models)

**Data Processing:** The analysis filters for state-level data (agglvl_code = 58) and focuses on the three primary states (California, New York, Georgia). Missing values in employment and wages are excluded from the analysis.

**Alternative specification:** Robustness check using NAICS 5121 (Motion Picture and Sound Recording Industries) to capture post-production spillovers.

### Migration Validation Data:

**Source:** IPUMS (Integrated Public Use Microdata Series) American Community Survey (ACS) microdata, accessed through the IPUMS USA database. The analysis uses annual ACS microdata from 2009-2023.

**Data Processing:** The analysis processes IPUMS ACS microdata in chunks to handle the large file size, filtering for film industry workers using NAICS industry codes.

**Variables Extracted:**
- `YEAR`: Survey year (2009-2023)
- `STATEFIP`: State FIPS code (current state of residence)
- `GQ`: Group quarters indicator (filtered to GQ = 1 for household population only)
- `PERWT`: Person weight (survey weights for population estimates)
- `INDNAICS`: Industry code (filtered for NAICS 512110 and codes starting with 5121 to capture Motion Picture and Video Production)
- `MIGPLAC1`: State of residence one year prior to survey (used to identify interstate movers)
- `MIGRATE1`: Migration status indicator

**Data Cleaning:** The analysis applies several filters:
- Industry filter: NAICS 512110 or codes starting with 5121
- Excludes invalid industry codes (0, missing, or empty)
- Excludes observations with zero or missing person weights
- Restricts to household population (GQ = 1)

**Purpose:** Identify whether post-2015 or post-2020 employment increases in QCEW correspond to actual inflows of film workers into California. The analysis calculates net migration as the difference between inflows (workers moving TO California from other states) and outflows (workers moving FROM California to other states).

**Approach:** Migration is measured using the `MIGPLAC1` variable, which indicates the state of residence one year prior to the survey. Interstate movers are identified as individuals where `MIGPLAC1` is a valid state code and differs from `STATEFIP`. All counts are weighted using `PERWT` to represent population estimates.

### Economic Controls:

**GDP Growth:**
- **Source:** Bureau of Economic Analysis (BEA) quarterly GDP by state data
- **Variable:** Year-over-year percentage change in quarterly GDP, calculated as `pct_change(periods=4) * 100` (comparing each quarter to the same quarter in the previous year)
- **Usage:** Included as a control variable in both DiD and SCM models

**Unemployment Rate:**
- **Source:** Bureau of Labor Statistics (BLS) state unemployment data (monthly)
- **Variable:** Quarterly average unemployment rate, calculated as the mean of three monthly unemployment rates per quarter (e.g., Q1 = average of January, February, March)
- **Usage:** Included as a control variable in both DiD and SCM models

**Population Growth:**
- **Source:** Bureau of Labor Statistics (BLS) state population data
- **Variable:** Year-over-year percentage change in quarterly population, calculated as `pct_change(periods=4) * 100`
- **Usage:** Included as a control variable in DiD models only (not used in SCM)

### Control Group Selection:

Proper control group selection requires balancing two competing concerns: policy stability (to avoid confounding) and industry comparability (to satisfy parallel trends). I prioritize the latter, as DiD validity depends fundamentally on common pre-treatment trajectories, not on the absence of incentives per se.

**Primary control states:** Georgia and New York—the only states with motion picture industries comparable in scale to California's. Excluding them would violate the parallel trends assumption by comparing California's established industry (which constituted 23% of national film employment in 2013) to states with minimal film sectors.

**Policy stability justification:**

- **Georgia:** Maintained a stable 30% tax credit structure (20% base + 10% promotional logo bonus) continuously from 2008 through 2022. While Georgia added a postproduction credit in 2018, the core production incentive—the relevant policy for NAICS 512110—remained unchanged during the study period. By 2022, Georgia accounted for 6.3% of national film employment, up from 1.0% pre-incentive, representing the most successful state-level program outside California.

- **New York:** Maintained a consistent 30% base credit throughout 2009–2022. The program saw funding expansions (most notably in 2023, after the study period) and added a 10% upstate county bonus in 2015 with a modest $5 million annual cap—a minor adjustment unlikely to materially affect aggregate state-level trends. New York consistently ranked as the second- or third-largest film production state during the study window.

**Addressing the "high-incentive exclusion" fallacy:** Prior literature sometimes excludes high-incentive states to avoid "spillover bias"—the concern that California's policy might shift production from competitor states, violating SUTVA. However, this concern applies primarily when analyzing aggregate national effects or constructing a donor pool where all states are potential counterfactuals. In a targeted two-way fixed effects framework with state and time controls, what matters is whether control states exhibit parallel pre-trends, not whether they compete for the same projects. Moreover, if California's expansion did pull production from Georgia or New York, observing negative employment effects in those states would strengthen causal inference, not weaken it.

**Secondary controls (robustness):** Florida, Illinois, Pennsylvania, and North Carolina—states with moderate film industries and stable policies during 2015–2022—are included as alternative controls in sensitivity analyses to assess whether results depend on the choice of high-intensity comparators.

**Excluded states:** Louisiana and New Mexico made substantial policy changes during the study period and lack the industry scale for credible comparison.

### Political Timing Data (Descriptive Supplement):

**Sources:** California Legislative Analyst's Office (budget documents), Secretary of State election records, LexisNexis State Capital reports.

**Purpose:** Assess proximity of credit expansions to gubernatorial election cycles.

## Empirical Strategy

### 1. Difference-in-Differences Model

The baseline specification follows Thom's (2018) framework, extended through 2025 and with two treatment onsets. I estimate separate models for **employment** and **wages** as outcome variables, with both Program 2.0 (2015 Q2) and Program 3.0 (2020 Q3) as treatment periods.

**Control Group:** California is compared against Georgia and New York, the two states with motion picture industries comparable in scale to California's and with stable incentive policies during the study period.

The baseline specification is:

$$Y_{st} = \alpha + \beta_{2015}(CA_s \times Post2015_t) + \beta_{2020}(CA_s \times Post2020_t) + \gamma_s + \delta_t + X_{st} + \varepsilon_{st}$$

Where:

- $Y_{st}$ = log of employment or log of average wages in NAICS 512110 for state $s$ in quarter $t$ (estimated separately for each outcome)
- $\alpha$ = constant term (intercept)
- $\beta_{2015}$ = **treatment effect of Program 2.0** (the primary coefficient of interest)
- $\beta_{2020}$ = **treatment effect of Program 3.0** (the secondary coefficient of interest)
- $CA_s$ = indicator variable equal to 1 for California, 0 for control states (Georgia and New York)
- $Post2015_t$ = indicator variable equal to 1 for quarters after 2015 Q2, 0 otherwise
- $Post2020_t$ = indicator variable equal to 1 for quarters after 2020 Q3, 0 otherwise
- $\gamma_s$ = **state fixed effects** (a set of state-specific dummy variables controlling for time-invariant differences across states, such as CA's historically larger industry scale)
- $\delta_t$ = **quarter fixed effects** (a set of quarter-specific dummy variables controlling for national time trends and seasonal patterns affecting all states equally, such as COVID-19 or holiday production cycles)
- $X_{st}$ = time-varying state-level controls:
  - **GDP growth rate**: Year-over-year percentage change in quarterly GDP (calculated as `pct_change(periods=4) * 100`), sourced from Bureau of Economic Analysis (BEA) quarterly GDP by state data
  - **Unemployment rate**: Quarterly average of monthly unemployment rates (mean of three months per quarter), sourced from Bureau of Labor Statistics (BLS) state unemployment data
  - **Population growth**: Year-over-year percentage change in quarterly population (calculated as `pct_change(periods=4) * 100`), sourced from BLS state population data
- $\varepsilon_{st}$ = error term, clustered at the state level to account for within-state correlation

The coefficients $\beta_{2015}$ and $\beta_{2020}$ represent the DiD estimates—the difference in employment or wage growth between California and control states (Georgia and New York) after each policy implementation, net of pre-existing trends and state-specific characteristics. Fixed effects are not separate datasets but rather dummy variables constructed directly from the panel structure during regression estimation.

I estimate this model separately for employment and wages, providing treatment effect estimates for both outcomes and both treatment periods (2015 and 2020). Event-study versions of this model estimate coefficients for each quarter relative to treatment to test parallel pre-trends and visualize dynamic effects. Standard errors are clustered at the state level. I also implement wild bootstrap standard errors as robustness for the single-treated-state case.

### 2. Synthetic Control Method (SCM)

To corroborate DiD employment estimates, I construct a Synthetic California from a donor pool of control states, following Rickman & Wang (2020). The SCM algorithm optimally weights donor states based on pre-treatment fit, naturally down-weighting states with divergent trends.

**Outcome Variable:** SCM is applied to **employment** only (not wages), as employment is the primary outcome of interest for evaluating the policy's impact on industry activity.

**Donor Pool:** The donor pool consists of six states: New York, Georgia, Louisiana, Florida, Illinois, and Pennsylvania. These states provide a diverse set of comparators with varying industry scales and policy environments, allowing the SCM algorithm to construct an optimal synthetic counterfactual.

**Pre-treatment windows:**
- **2015 treatment:** 2010 Q1 to 2015 Q1 (21 quarters)
- **2020 treatment:** 2012 Q1 to 2020 Q2 (34 quarters)

**Predictor variables:** The SCM algorithm uses the following pre-treatment predictors to construct the synthetic counterfactual:
- **Log employment**: Natural logarithm of quarterly average employment (from QCEW)
- **Log wage**: Natural logarithm of average weekly wage (from QCEW)
- **GDP growth**: Year-over-year percentage change in quarterly GDP (from BEA quarterly GDP by state data)
- **Unemployment rate**: Quarterly average unemployment rate (from BLS state unemployment data)

These predictors are averaged over the pre-treatment period for each state, and the SCM algorithm finds optimal weights for donor states that minimize the distance between California's predictor values and the weighted combination of donor states' predictor values.

**Evaluation:** The treatment effect is identified from **changes in the gap** between actual California and the synthetic counterfactual following policy implementation, not from the absolute gap itself. I further conduct in-space placebo tests assigning "pseudo-treatments" to donor states to confirm that California's estimated gap is statistically distinct from noise. The placebo tests rank California's post-treatment deviation among all states in the donor pool to assess statistical significance.

### 3. Migration-Based Validation (ACS)

To determine whether observed QCEW job gains reflect real labor inflows, I analyze IPUMS ACS migration data for film industry workers (NAICS 512110 and related codes) from 2009-2023.

**Migration Measurement:**
- **Inflows:** Film workers who moved TO California from other states (identified where `MIGPLAC1` equals California's state code and differs from `STATEFIP`)
- **Outflows:** Film workers who moved FROM California to other states (identified where `STATEFIP` equals California's state code and `MIGPLAC1` is a valid state code different from California)
- **Net Migration:** Calculated as inflows minus outflows (positive values indicate net inflow, negative values indicate net outflow)

**Analysis:**
- Calculate annual weighted counts of inflows, outflows, and net migration for each year from 2009-2023
- Compare migration patterns before and after treatment periods (2015 and 2020)
- Calculate migration rates as net migration divided by total California film workforce
- Assess whether employment increases in QCEW correspond to actual worker inflows or reflect alternative mechanisms (e.g., retention of existing workers, increased hours for existing workers)

This analysis directly addresses the "reclassification problem" identified by Rickman and Wang (2020), testing whether apparent employment gains in administrative data correspond to genuine worker relocation.

### 4. Robustness Checks

- **Alternative control groups:** Test sensitivity to control group composition by comparing (1) Georgia + New York only, (2) secondary controls only (FL, IL, PA, NC), and (3) all controls combined, to assess whether results depend on including high-intensity competitor states.
- **Alternative time windows:** Test 1-year, 2-year, and 3-year post-treatment windows to examine persistence.
- **Placebo tests:** Assign false policy dates (e.g., 2013, 2017) to assess spurious significance.
- **NAICS robustness:** Repeat analysis using 5121 aggregation to capture post-production industries.
- **Cost-per-job estimates (optional):** Compute implied cost per new job using program expenditure data and DiD-estimated employment changes.

### 5. Political Timing Analysis (Descriptive)

Following Owens and Rennhoff (2024), I descriptively examine the proximity of policy enactments to gubernatorial elections:

- 2015 expansion (AB 1839) signed September 2014, months before Governor Brown's re-election.
- 2020 expansion (Program 3.0) approved mid-2020, within Governor Newsom's first term ahead of recall discussions.

By quantifying months between each enactment and the nearest election, I evaluate whether these expansions cluster around politically sensitive periods, contextualizing the persistence of film incentives beyond economic logic.

## Summary of Methodological Contribution

My approach maintains consistency with Thom (2018) and Rickman & Wang (2020) in using QCEW-based DiD and SCM frameworks, but adds three key innovations:

1. Extending temporal scope to capture California's 2015 and 2020 expansions;
2. Integrating ACS migration data to validate whether employment changes reflect real relocation;
3. Embedding political-timing analysis to connect economic outcomes with electoral incentives.

This combined framework allows for a richer interpretation of California's film tax credits—whether they reflect genuine industry revival or politically driven statistical illusions.

