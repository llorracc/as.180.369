# Results

## Preliminary Findings from Exploratory Analysis (2013-2018)

### Basic Employment Trends

Initial exploration of BLS QCEW data for NAICS 512110 (Motion Picture and Video Production) reveals the following rudimentary patterns for California:

**Raw Employment Changes:**
- California's quarterly employment in motion picture production showed growth from 2013Q4 to 2018Q4
- Pre-tax credit average (2013-2014): ~110,000 employees
- Post-tax credit average (2015-2018): ~115,000 employees  
- Overall change: approximately +4-5% over the period
- Peak employment occurred in 2018Q3-Q4

**Quarterly Growth Patterns:**
- Notable positive growth in 2015Q2 and 2015Q3 (shortly after the July 2015 tax credit expansion)
- More volatile quarterly growth rates in 2016-2017
- Stabilization at higher employment levels in 2018

### Multi-State Comparison

Exploratory comparison across California, Georgia, and New York (2013-2018):

- **California:** Modest growth (~4-5%)
- **Georgia:** Substantial growth with consistent upward trajectory
- **New York:** Relatively stable employment with slight fluctuations
- **National aggregate:** Positive growth trend across all states combined

### Rudimentary Difference-in-Differences (California vs. New York)

Using New York as a control group (percentage-based approach to account for different baseline employment levels):

- **California percentage change (Pre vs. Post-2015):** +4.5%
- **New York percentage change (Pre vs. Post-2015):** -2.3%
- **Simple DiD estimate:** ~+6.8 percentage points

This preliminary calculation suggests California's employment growth rate was approximately 6.8 percentage points higher than New York's after the 2015 tax credit expansion. However, this rudimentary analysis:
- Does not control for economic conditions (GDP, unemployment)
- Does not include state and time fixed effects
- Uses only a single control state
- Lacks statistical significance testing
- Does not address parallel trends assumption
- Does not extend to the 2020 policy expansion

---

## What Still Needs to Be Done

To complete this Results section according to the methodology outlined in Section 4, the following analyses must be conducted:

### 1. **Formal Difference-in-Differences Regression Models**
   - Estimate two-way fixed effects regression: $Y_{st} = \alpha + \beta_{2015}(CA_s \times Post2015_t) + \beta_{2020}(CA_s \times Post2020_t) + \gamma_s + \delta_t + X_{st} + \varepsilon_{st}$
   - Run for full 2009-2022 panel (not just 2013-2018)
   - Include both Program 2.0 (2015) and Program 3.0 (2020) treatment effects
   - Add state and quarter fixed effects
   - Control for GDP growth and unemployment rates
   - Cluster standard errors at state level
   - Report coefficients with standard errors, t-statistics, and p-values
   - Test both log employment and average wages as dependent variables

### 2. **Parallel Trends Testing & Event Study**
   - Generate event-study graphs showing quarter-by-quarter treatment effects relative to policy implementation
   - Estimate leads (pre-treatment quarters) to test parallel trends assumption
   - Visualize confidence intervals for all lead/lag coefficients
   - Conduct formal statistical test of joint significance of pre-treatment leads

### 3. **Synthetic Control Method Analysis**
   - Construct synthetic California using Georgia, New York, and secondary control states as donor pool
   - Report optimal weights assigned to each donor state
   - Calculate treatment effects as gap between actual CA and synthetic CA
   - Generate time series plots comparing actual vs. synthetic trends
   - Conduct placebo tests assigning pseudo-treatments to donor states
   - Calculate p-values from placebo distribution

### 4. **Migration Data Validation (ACS)**
   - Obtain U.S. Census ACS migration data for film industry occupations (SOC 27-2012, 27-4031, 27-4032)
   - Calculate in-migration rates to California before/after 2015 and 2020
   - Identify source states of migrants (competitor states vs. non-competitor states)
   - Compare migration patterns for film workers vs. other professional occupations (placebo)
   - Analyze occupation-specific effects (creative vs. support staff)
   - Report with 3-year moving averages and margins of error

### 5. **Robustness Checks**
   - **Alternative control groups:** 
     - Georgia + New York only (primary specification)
     - Secondary controls only (FL, IL, PA, NC)
     - All controls combined
   - **Alternative time windows:** Test 1-year, 2-year, and 3-year post-treatment effects
   - **Placebo tests:** Assign false treatment dates (2013, 2017) to detect spurious effects
   - **Industry definition:** Repeat analysis using NAICS 5121 (broader Motion Picture and Sound Recording)
   - **Alternative standard errors:** Wild bootstrap (Cameron et al.) for single-treated-state inference
   - **Staggered treatment:** Test whether 2020 effects differ from 2015 effects

### 6. **Statistical Tables to Generate**
   - **Table 1:** Summary statistics (employment, wages, controls) by state and treatment period
   - **Table 2:** Main DiD regression results with multiple specifications
   - **Table 3:** Event study coefficients for leads/lags
   - **Table 4:** Synthetic control weights and pre-treatment fit metrics (RMSPE)
   - **Table 5:** Placebo test results and permutation p-values
   - **Table 6:** Migration analysis summary statistics
   - **Table 7:** Robustness checks across alternative specifications

### 7. **Figures to Generate**
   - **Figure 1:** Raw employment trends for California, control states, and national aggregate (2009-2022)
   - **Figure 2:** Event study plot with 95% confidence intervals
   - **Figure 3:** Synthetic control time series (actual vs. synthetic California)
   - **Figure 4:** Placebo distribution from permutation tests
   - **Figure 5:** Migration inflow rates by year and source state
   - **Figure 6:** Robustness visualization across alternative specifications

### 8. **Cost-Per-Job Calculation (Optional)**
   - Obtain California Film Commission expenditure data for Program 2.0 and 3.0
   - Divide total tax credits allocated by DiD-estimated net employment gain
   - Report implied cost per job created
   - Compare to Thom (2018) and other states' estimates

### 9. **Political Timing Analysis (Descriptive)**
   - Document exact dates of AB 1839 (2015 expansion) and Program 3.0 approval (2020)
   - Calculate months between each expansion and nearest gubernatorial election
   - Present timeline visualization showing policy enactments relative to election cycles
   - Contextualize alongside findings from Owens & Rennhoff (2024)

---

**Note:** Current exploratory analysis only covers 2013-2018 and uses simplified calculations. The methodology requires extending the dataset to 2009-2022 to capture both pre-treatment baseline (2009-2014) and both policy expansions (2015 and 2020), while implementing formal econometric specifications with proper controls, fixed effects, and statistical inference.

