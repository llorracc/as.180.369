# Methodology

## Research Objective and Design

This study evaluates whether California's Film and Television Tax Credit Program 2.0 (FY2015–16 launch) and Program 3.0 (credit allocations from July 1, 2020 onward) produced measurable employment or wage effects in the motion picture and video production industry (NAICS 512110).

Following Thom (2018), I use a difference-in-differences (DiD) design on a state-by-quarter panel (2009–2022), comparing California against a control group of states with stable film incentive policies and similar pre-treatment industry trends. For robustness and improved counterfactual validity, I complement DiD with a Synthetic Control Method (SCM) following Rickman and Wang (2020).

## Data Sources

### Employment and Wages:

**Source:** Bureau of Labor Statistics QCEW, quarterly data (2009–2022).

**Industry:** Motion Picture and Video Production (NAICS 512110), consistent with Rickman & Wang's specification.

**Alternative specification:** Robustness check using NAICS 5121 (Motion Picture and Sound Recording Industries) to capture post-production spillovers.

### Migration Validation Data:

**Source:** U.S. Census Bureau American Community Survey (ACS) 1-Year Estimates (2010–2022).

**Variables:** State-to-state migration flows by occupation (SOC 27-2012, 27-4031, 27-4032).

**Purpose:** Identify whether post-2015 or post-2020 employment increases in QCEW correspond to actual inflows of film workers into California.

**Approach:** Use 3-year moving averages and report margins of error to address ACS sampling noise.

### Economic Controls:

State GDP growth, unemployment rate, and population from the Bureau of Economic Analysis (BEA).

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

The baseline specification follows Thom's (2018) framework, extended through 2022 and with two treatment onsets:

$$Y_{st} = \alpha + \beta_{2015}(CA_s \times Post2015_t) + \beta_{2020}(CA_s \times Post2020_t) + \gamma_s + \delta_t + X_{st} + \varepsilon_{st}$$

Where:

- $Y_{st}$ = log of employment or average wages in NAICS 512110 for state $s$ in quarter $t$
- $\alpha$ = constant term (intercept)
- $\beta_{2015}$ = **treatment effect of Program 2.0** (the primary coefficient of interest)
- $\beta_{2020}$ = **treatment effect of Program 3.0** (the secondary coefficient of interest)
- $CA_s$ = indicator variable equal to 1 for California, 0 for control states
- $Post2015_t$ = indicator variable equal to 1 for quarters after 2015 Q2, 0 otherwise
- $Post2020_t$ = indicator variable equal to 1 for quarters after 2020 Q3, 0 otherwise
- $\gamma_s$ = **state fixed effects** (a set of state-specific dummy variables controlling for time-invariant differences across states, such as CA's historically larger industry scale)
- $\delta_t$ = **quarter fixed effects** (a set of quarter-specific dummy variables controlling for national time trends and seasonal patterns affecting all states equally, such as COVID-19 or holiday production cycles)
- $X_{st}$ = time-varying state-level controls (GDP growth rate, unemployment rate)
- $\varepsilon_{st}$ = error term, clustered at the state level to account for within-state correlation

The coefficients $\beta_{2015}$ and $\beta_{2020}$ represent the DiD estimates—the difference in employment or wage growth between California and control states after each policy implementation, net of pre-existing trends and state-specific characteristics. Fixed effects are not separate datasets but rather dummy variables constructed directly from the panel structure during regression estimation.

Event-study versions of this model will estimate coefficients for each quarter relative to treatment to test parallel pre-trends and visualize dynamic effects. Standard errors are clustered at the state level. I also implement wild bootstrap standard errors as robustness for the single-treated-state case.

### 2. Synthetic Control Method (SCM)

To corroborate DiD estimates, I construct a Synthetic California from the donor pool of control states identified above, following Rickman & Wang (2020). The SCM algorithm optimally weights donor states based on pre-treatment fit, naturally down-weighting states with divergent trends.

**Pre-treatment window:** 2009 Q1–2015 Q1 for the 2015 treatment, and 2012 Q1–2020 Q2 for the 2020 treatment.

**Predictor variables:** Quarterly employment, average wages, GDP growth, and unemployment rate.

**Evaluation:** The treatment effect is the post-period difference between actual California and the synthetic counterfactual. I further conduct placebo tests assigning "pseudo-treatments" to donor states to confirm that California's estimated gap is statistically distinct from noise.

### 3. Migration-Based Validation (ACS)

To determine whether observed QCEW job gains reflect real labor inflows, I analyze ACS migration data across three dimensions:

**Inflow Analysis:**
- Measure annual in-migration of film workers into California before and after 2015 and 2020.
- Compare to migration trends for other professional occupations (placebo).

**Source-State Composition:**
- Identify whether inflows originate from high-incentive competitor states (e.g., Georgia, Louisiana) or from non-competitor states.
- A shift away from competitor states supports genuine industry relocation.

**Occupation-Specific Effects:**
- Examine changes in inflow composition between creative/high-skill occupations (e.g., directors, cinematographers) and support staff (e.g., post-production, clerical).
- Divergent occupation patterns help distinguish real production relocation from administrative headquarter reclassification.

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

