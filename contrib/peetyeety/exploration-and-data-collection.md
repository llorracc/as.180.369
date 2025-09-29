# Film Tax Credits as Location-Based Subsidies: An Analysis of Georgia and California Programs

## Abstract

In this paper, I evaluate film tax credits as location-based subsidies by examining two contrasting state programs: Georgia and California. My analysis addresses three questions: (1) How efficient are film tax credits compared to people-based subsidies when measured in cost per job, using Georgia as a case study? (2) Do film tax credits generate sustained employment or wage gains in the motion-picture industry, tested through a difference-in-differences framework in California following major program expansions in 2015 and 2020? (3) To what extent are credit expansions driven by political incentives, particularly their alignment with gubernatorial election cycles, rather than solely by economic goals? 

To answer these questions, I use Georgia audit reports to calculate cost-per-job and benchmark efficiency against alternative subsidies such as state EITC supplements and job training programs. For California, I build a panel of motion-picture employment and wage data from 2009–2022 and estimate policy impacts using difference-in-differences models with appropriate control states, supplemented by synthetic control methods to ensure robustness to alternative control group construction. Finally, I map the timing of program changes in both states against electoral calendars to assess political motivations. My preliminary findings suggest that while film tax credits deliver short-term production spikes and visible political wins, they are less efficient than people-based subsidies, generate limited long-term industry gains, and reflect political as much as economic logic.

## Literature Review

### 1. Lights, Camera, but No Action? Tax and Economic Development Lessons from State Motion Picture Incentive Programs (Michael Thom, 2018)

#### Summary

Thom provides a national, longitudinal evaluation (1998–2013) of motion picture incentive (MPI) programs across U.S. states. Using state-level panel data, the paper examines employment, wages, gross state product (GSP), and industry concentration. Results show that most incentives—like sales and lodging tax waivers—had no measurable effect. Transferable tax credits modestly increased employment over time but had no impact on wages, while refundable credits temporarily boosted wages but not jobs. Neither type of credit influenced GSP or industry concentration. The study highlights program inefficiencies, risks of rent-seeking, and poor oversight (including fraud cases), and argues that incentives largely benefitted existing workers and producers rather than generating sustained state-level growth.

#### Connection to Your Paper

This study provides a broad, empirical baseline against which I can contextualize my Georgia and California case studies. Thom's findings—that MPI programs yield short-term, limited labor market gains and no long-term structural benefits—mirror my preliminary claim that credits are less efficient than people-based subsidies. Importantly, Thom does not deeply explore cost-per-job efficiency relative to alternative subsidies, nor does he examine the political timing of expansions. I can thus build on his evidence by:

- Extending the efficiency analysis (Georgia audits vs. EITC/job training benchmarks)
- Testing for sustained employment/wage effects in a more recent time frame (California post-2015/2020 expansions)
- Investigating the political cycle dimension that Thom only alludes to

In other words, I can frame my study as both a deep dive into state-level mechanisms and a bridge between efficiency and political economy analyses.

### 2. Political Behavior and Voting for Tax Incentives (Owens & Rennhoff, 2024)

#### Summary

Owens and Rennhoff analyze the determinants of state legislators' votes on movie production tax incentives. Using roll-call data, election results, district characteristics, and political donations, they find that political affiliation (Republicans being less supportive), governor's party alignment and donations, margin of electoral victory, unemployment rates, and neighboring states' policies significantly shape support. Interestingly, local film activity or industry donations to individual legislators were not strong predictors. Districts that voted in favor did see more production afterwards, suggesting some payoff to legislators. Their results also align with the median voter theorem: legislators' votes reflect the ideological leanings of their districts. Overall, the paper highlights that politics and electoral incentives—rather than purely economic logic—are central in sustaining film tax credits.

#### Connection to Your Paper

This study directly complements my third research question on whether credit expansions are politically motivated. Owens and Rennhoff provide micro-level evidence that votes follow political incentives (party alignment, electoral security, inter-state competition, voter ideology). I can build on this by:

- Moving from vote-level analysis to policy-cycle analysis, linking expansions in Georgia and California to gubernatorial election calendars
- Testing whether the timing of expansions (e.g., clustered around elections) aligns with the behaviors documented by Owens & Rennhoff
- Bridging legislative behavior with policy outcomes: their study shows why legislators vote for incentives, while mine examines whether those incentives actually improve efficiency or deliver sustained economic benefits

In short, their paper supplies the political mechanism, while mine evaluates policy efficiency and outcomes, letting me position my work as an integrative extension.

### 3. The Economics of State Film Incentives (Rickman & Wang, 2020)

#### Summary

Rickman and Wang review the academic literature on U.S. state film incentives and highlight the weaknesses of many economic impact studies. They note that most early analyses assumed all production was caused by incentives, overstating benefits. Their key contribution is applying the synthetic control method (SCM) to evaluate both the adoption and elimination of incentives across states. Using QCEW data (employment and wages in NAICS 51211), they find that incentives often raise sector employment and wages in early-adopter states like Louisiana and New Mexico. However, incentives rarely "pay for themselves," with ROI usually below 1, though sometimes more favorable than general business tax incentives. They also show that repealing or capping incentives tends to reduce industry activity. Ultimately, they argue outcomes depend on program size, design, and state context.

#### Connection to Your Paper

Rickman is directly relevant because it builds on the same methodological debates I've been considering (DiD vs. SCM). Their application of SCM makes a strong case for supplementing standard DiD estimates with case-study counterfactuals, aligning with my idea of running DiD first and then SCM for robustness. Moreover, Rickman highlights the distinction between short-term production effects (more measurable) and broader economic spillovers (harder to detect), which dovetails with my concern about identifying causal impacts of incentives. Their discussion of eliminations and caps is also a useful contrast to Thom (who focuses more on adoption), allowing me to position my work in that middle ground—using both methodologies while acknowledging limits.

### 4. Do State Movie Production Incentives Promote Economic Development? (Bradbury, 2020)

#### Summary

Bradbury evaluates whether state movie production incentives (MPIs) stimulate overall state economic development, rather than just film industry activity. Using panel data from 2000–2015 and an instrumental variable fixed-effects strategy, he exploits the staggered adoption, suspension, and repeal of MPIs across 44 states. Instruments include the age of a state's film commission and adoption by neighboring states. The outcome variables are broad macroeconomic indicators: per capita income and per capita gross state product. Bradbury finds no statistically significant evidence that MPIs increase state economic growth or income levels. At best, some estimates suggest limited boosts to the film industry itself, but these gains do not spill over into the wider economy. In many cases, effects are negative or negligible, echoing state agency audits that show low or negative returns on investment. His conclusion: MPIs represent a costly and ineffective economic development strategy.

#### Connection to My Paper

Bradbury provides the macro-level counterpart to my more targeted efficiency and employment analysis. While my paper benchmarks cost-per-job (Georgia) and industry wage/employment effects (California), Bradbury tests the "so what?" question: do those sectoral gains translate into overall state economic growth? His null findings suggest they do not, which allows me to frame my paper as filling the middle ground—measuring the narrow efficiency and political economy mechanisms that likely explain why aggregate effects never appear. Methodologically, his IV approach (using diffusion instruments like neighboring states' adoption) can serve as inspiration if I want to address endogeneity in my own DiD setup. Substantively, citing Bradbury lets me argue that even if I find California's 2015/2020 expansions produced measurable industry job gains, those are unlikely to have improved statewide prosperity—reinforcing my efficiency critique and highlighting the political logic of sustaining these credits.

## Data Collection and Methodology

### Research Question 1: Cost-Per-Job Efficiency Analysis (Georgia)

#### Data Sources
- **Primary**: Georgia Department of Audits and Accounts annual reports on entertainment industry investment incentives (2010-2022)
- **Secondary**: 
  - Bureau of Labor Statistics Quarterly Census of Employment and Wages (QCEW) for Georgia motion picture industry (NAICS 512110)
  - Georgia Department of Community Affairs workforce development program reports
  - Tax Foundation state EITC program data
  - National Association of State Workforce Agencies (NASWA) job training expenditure reports
  - U.S. Census Bureau's Annual Survey of State Government Finances

#### Methodology
*Building on Thom's (2018) efficiency concerns and Bradbury's (2020) cost-effectiveness framework*

1. **Cost-Per-Job Calculation**: I will extract total tax credit amounts and reported job creation figures from Georgia audit reports, following the job counting methodology used in official state evaluations
2. **Benchmark Comparison**: I will calculate cost-per-job for alternative programs:
   - State EITC supplements (using IRS Statistics of Income data on participation rates and average credit amounts)
   - Workforce Investment and Opportunity Act (WIOA) programs (using program budgets and documented job placements)
   - Georgia Quick Start job training program (using state budget allocations and placement rates)
3. **Efficiency Metrics**: I will develop comparative cost-per-job ratios with bootstrapped confidence intervals, accounting for different job duration assumptions (temporary vs. permanent positions)
4. **Sensitivity Analysis**: Following Rickman & Wang's (2020) approach, I will test robustness using:
   - Different job counting methodologies (full-time equivalent vs. total positions vs. person-years)
   - Alternative time horizons for job persistence (1-year, 3-year, 5-year)
   - Inclusion/exclusion of indirect job creation claims

### Research Question 2: Employment and Wage Impact Analysis (California)

#### Data Sources
- **Primary**: Bureau of Labor Statistics Quarterly Census of Employment and Wages (QCEW) for motion picture and video industries (NAICS 512110, following Rickman & Wang 2020)
- **Secondary**:
  - California Employment Development Department Labor Market Information Division quarterly data
  - U.S. Census Bureau County Business Patterns for industry establishment counts
  - California Film Commission annual reports and production data
  - National Conference of State Legislatures film incentive database for control state selection

#### Methodology
*Combining Thom's (2018) panel approach with Rickman & Wang's (2020) synthetic control validation*

1. **Panel Construction**: I will build a quarterly panel of employment and wage data (2009-2022) for California and potential control states, using the same NAICS classification (512110) as Rickman & Wang for comparability
2. **Control Group Selection**: Following Bradbury's (2020) approach to identifying comparable states, I will use:
   - Pre-treatment motion picture industry employment levels and growth trends (2009-2014)
   - Economic and demographic similarities (GDP per capita, population, urbanization rates)
   - Absence of major film incentive adoptions, expansions, or eliminations during 2015-2022 treatment periods
   - Geographic and climate considerations relevant to film production
3. **Difference-in-Differences Specification**:
   ```
   Y_st = α + β₁(CA × Post2015) + β₂(CA × Post2020) + γ_s + δ_t + X_st + ε_st
   ```
   Where Y_st is log employment/wages, CA is California indicator, Post periods capture expansions, X_st includes economic controls
4. **Robustness Checks**:
   - Event study plots around expansion dates to test parallel trends assumption
   - Synthetic control method as alternative estimation (following Rickman & Wang's SCM approach)
   - Placebo tests with non-expansion dates and non-treated states
   - Addressing potential endogeneity using Bradbury's instrumental variable approach (neighboring state adoption patterns)

### Research Question 3: Political Timing Analysis (Georgia and California)

#### Data Sources
*Building on Owens & Rennhoff's (2024) political economy framework*

- **Electoral Data**: 
  - Georgia Secretary of State and California Secretary of State websites for gubernatorial election dates, results, and candidate information
  - Federal Election Commission and state campaign finance databases for film industry contributions
  - Ballotpedia for comprehensive electoral timeline data
- **Policy Timeline Data**:
  - State legislative databases (Georgia General Assembly and California Legislature) for bill tracking
  - LexisNexis State Capital for comprehensive policy change documentation
  - National Conference of State Legislatures film incentive program database
  - State budget documents and appropriations bills for program funding changes
- **Economic Control Data**:
  - Bureau of Economic Analysis for state GDP and unemployment rates
  - Tax Foundation for neighboring state policy changes

#### Methodology
*Extending Owens & Rennhoff's (2024) political incentive analysis to policy timing*

1. **Timeline Mapping**: I will create a detailed chronology of:
   - All major film incentive policy changes (2005-2022) including adoptions, expansions, caps, and eliminations
   - Gubernatorial election cycles, primary dates, and campaign periods
   - Key political events, leadership transitions, and budget cycles
2. **Statistical Testing**:
   - Chi-square tests for clustering of policy changes around election periods
   - Logistic regression modeling probability of expansion as function of:
     - Electoral proximity (months to/from election)
     - Governor's party affiliation and approval ratings
     - Legislative control and competitiveness
     - Economic conditions (unemployment, budget surplus/deficit)
3. **Event Analysis**: 
   - I will examine 18-month windows before/after elections for policy activity intensity
   - Control for economic conditions, neighboring state competition (following Bradbury's diffusion approach), and industry lobbying expenditures
4. **Comparative Framework**: I will contrast timing patterns between:
   - Georgia (consistent Republican control, strong incentives) vs. California (Democratic control, variable incentives)
   - Different gubernatorial administrations within each state
   - Policy expansions vs. contractions across electoral cycles

## Alternative Simplified Approach (2-Month Timeline)

*For faster execution while maintaining core insights*

### Research Question 1: Georgia Cost-Per-Job Analysis (Simplified)

#### Data Sources
- **Primary**: Georgia Department of Audits and Accounts annual reports (2015-2022 only)
- **Benchmarks**: 
  - Tax Foundation EITC data (readily available online)
  - Georgia Quick Start program reports (state website)
  - Bureau of Labor Statistics average cost-per-hire data

#### Simplified Methodology with Examples

1. **Basic Cost Calculation for Film Tax Credits**:
   - *Example*: From 2020 Georgia audit report: $800 million in film tax credits awarded, 92,000 jobs reported
   - *Calculation*: $800M ÷ 92,000 jobs = $8,696 per job in film industry
   - *Repeat for 2018, 2019, 2021 reports to get average*

2. **Simple Benchmarking Against Alternative Programs**:
   - *Example 1 - Georgia EITC*: If Georgia had state EITC supplement of $500 per recipient, and 200,000 recipients = $100M total cost ÷ 200,000 jobs supported = $500 per job
   - *Example 2 - Georgia Quick Start*: 2020 program budget $25M, trained 15,000 workers = $1,667 per job
   - *Example 3 - General hiring*: BLS average cost-per-hire in Georgia ≈ $4,000

3. **Descriptive Analysis**:
   - *Comparison*: Film tax credits ($8,696/job) vs. EITC ($500/job) vs. Quick Start ($1,667/job)
   - *Finding*: Film credits cost 17x more per job than EITC, 5x more than job training
   - *Present as simple bar chart with confidence intervals*

### Research Question 2: California Impact Analysis (Simplified)

#### Data Sources
- **Primary**: BLS QCEW data for California motion picture industry (NAICS 512110)
- **Control**: 3-4 obvious control states (Texas, Florida, New York, Illinois) without major incentive changes
- **Timeline**: Focus only on 2015 expansion (drop 2020 for simplicity)

#### Simplified Methodology with Examples

1. **Basic DiD Setup**:
   - *Example*: California film employment 2014: 150,000 jobs → 2016: 180,000 jobs (+20% growth)
   - *Control states average*: 2014: 50,000 jobs → 2016: 52,000 jobs (+4% growth)
   - *DiD estimate*: California grew 20% vs. expected 4% = 16 percentage point effect from 2015 expansion
   - *In jobs*: 16% of 150,000 = 24,000 additional jobs attributable to the policy

2. **Visual Analysis**:
   - *Example*: Create line graph showing California vs. control states employment 2012-2018
   - *Look for*: Parallel trends 2012-2014, then divergence after 2015
   - *Event study*: Plot quarterly employment differences around Q2 2015 expansion date

3. **Synthetic Control (Using Cursor for Easy Implementation)**:
   - *Setup*: Use Python's `synthdid` or R's `Synth` package to create "Synthetic California"
   - *Donor pool*: Texas, Florida, New York, Illinois, Pennsylvania, Michigan (states without major incentive changes)
   - *Pre-treatment fit*: Weight donor states to match California's 2012-2014 employment trends
   - *Example*: Synthetic CA = 0.4×Texas + 0.3×Florida + 0.2×New York + 0.1×Illinois
   - *Validation*: Check that Synthetic CA closely tracks actual CA before 2015

4. **Zero-Sum Check (National Totals)**:
   - *Data*: Total U.S. film employment from BLS (sum of all states)
   - *Test*: Did national film employment increase after CA's 2015 expansion?
   - *Interpretation*: 
     - If national total unchanged → CA just stole jobs from other states
     - If national total increased → CA created new jobs for the industry
   - *Example*: US film jobs 2014: 500K → 2016: 520K (+4%) suggests some job creation, not pure zero-sum

### Research Question 3: Political Timing (Simplified)

#### Data Sources
- **Electoral**: Ballotpedia for election dates (Georgia and California)
- **Policy**: NCSL film incentive database for major changes
- **Simple Timeline**: Wikipedia and news sources for basic chronology

#### Simplified Methodology with Examples

1. **Descriptive Timeline Creation**:
   - *Example*: Georgia timeline showing:
     - 2010: Governor Deal elected → 2012: Film tax credit expansion
     - 2014: Deal re-election campaign → 2015: Credit cap increase
     - 2018: Governor Kemp elected → 2019: Program renewal
   - *Visual*: Create timeline chart with election dates (red) and policy changes (blue)

2. **Basic Statistical Pattern**:
   - *Example calculation*: Out of 8 major Georgia policy changes (2008-2022), how many occurred within 12 months of gubernatorial elections?
   - *Simple test*: If 6 out of 8 changes happened near elections vs. 2 out of 8 expected by chance
   - *Finding*: "75% of major expansions occurred within election cycles vs. 25% expected"

3. **Case Study Examples**:
   - *Case 1*: Georgia 2012 expansion during Deal's first term (campaign promise fulfillment)
   - *Case 2*: California 2015 expansion during Brown's final term (legacy building)
   - *Analysis*: Compare timing, political context, and stated rationales for each case

### Simplified Timeline (8 Weeks)

- **Weeks 1-2**: Data collection (focus on readily available sources)
- **Weeks 3-4**: Georgia efficiency analysis (basic calculations)
- **Weeks 5-6**: California DiD analysis (simple specification)
- **Week 7**: Political timing descriptive analysis
- **Week 8**: Writing and final analysis

### Trade-offs of Simplified Approach

**Advantages:**
- **Feasible timeline**: Realistic for 2-month completion
- **Clear findings**: Simpler analysis often produces clearer results
- **Accessible data**: All sources are publicly available online
- **Core insights preserved**: Still addresses all three research questions

**Limitations:**
- **Less methodological sophistication**: No synthetic control, limited robustness checks
- **Narrower scope**: Fewer years, fewer control states, simpler political analysis
- **Reduced academic rigor**: Less comprehensive literature engagement

## Expected Contributions

My research will contribute to the literature by:

1. **Methodological Innovation**: This will be the first study to systematically compare film tax credit efficiency with people-based alternatives using state audit data, building on the efficiency concerns raised by Thom (2018) and Bradbury (2020)
2. **Temporal Extension**: I will update Thom's (2018) findings with more recent data (through 2022) and longer-term outcome measures, incorporating Rickman & Wang's (2020) synthetic control methodology
3. **Political Economy Integration**: I will bridge the gap between Owens & Rennhoff's (2024) legislative behavior analysis and policy outcome evaluation, extending their political incentive framework to policy timing
4. **Multi-Level Analysis**: I will connect micro-level efficiency analysis (Georgia) with meso-level industry impacts (California) and macro-level political timing, addressing the gap between Bradbury's aggregate null findings and sector-specific effects
5. **Policy Implications**: I will provide concrete efficiency benchmarks and political cycle insights for policymakers considering film incentive programs, informed by the comprehensive literature on program effectiveness

## Preliminary Timeline

- **Months 1-2**: Data collection and cleaning
- **Months 3-4**: Georgia efficiency analysis and benchmarking
- **Months 5-6**: California difference-in-differences estimation
- **Months 7-8**: Political timing analysis and robustness checks
- **Months 9-10**: Writing and revision
