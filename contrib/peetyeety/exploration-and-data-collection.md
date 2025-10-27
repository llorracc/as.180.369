# Film Tax Credits and Motion Picture Employment: A Contemporary Analysis of California's Program Expansions

## Abstract

In this paper, I evaluate the employment and wage effects of California's film tax credit expansions in 2015 and 2020 using contemporary data that extends beyond previous studies. Building directly on Thom's (2018) national analysis which ended in 2013, I examine whether more recent program expansions generated sustained employment or wage gains in the motion picture industry. I construct a panel of motion picture employment and wage data from 2009-2022 using Bureau of Labor Statistics Quarterly Census of Employment and Wages (QCEW) data and estimate policy impacts through difference-in-differences models with appropriate control states, supplemented by synthetic control methods for robustness.

Recognizing that QCEW data has important limitations—particularly the risk of capturing employee reclassification across state lines rather than genuine job creation—I supplement my analysis with American Community Survey (ACS) migration data to distinguish between actual worker relocation to California and potential strategic firm reporting. Additionally, I provide descriptive analysis of the political timing of these expansions relative to gubernatorial election cycles, exploring whether policy changes align with electoral incentives as suggested by recent political economy research. My approach addresses a critical gap in the literature: understanding whether film tax credits continue to show employment effects in the post-2013 period, and whether these effects represent genuine economic gains or statistical artifacts of firm behavior.

## Literature Review

The academic literature on film tax credits reveals a consistent pattern: while these programs are politically popular and widely adopted, empirical evidence for their economic effectiveness is weak. Four recent papers establish the foundation for my research, covering national panel studies (Thom 2018), methodological approaches (Rickman & Wang 2020), aggregate economic impacts (Bradbury 2020), and political incentives (Owens & Rennhoff 2024). Together, these studies highlight both a temporal gap—most data end before 2015—and a methodological challenge—distinguishing genuine job creation from statistical artifacts. My research addresses both gaps.

### 1. Lights, Camera, but No Action? Tax and Economic Development Lessons from State Motion Picture Incentive Programs (Michael Thom, 2018)

#### Summary

Thom provides the most comprehensive national evaluation of motion picture incentive (MPI) programs to date, analyzing state-level panel data from 1998–2013. Using difference-in-differences estimation, he examines the effects of various incentive types on employment, wages, gross state product (GSP), and industry concentration across all U.S. states. His key findings reveal mixed and modest results: transferable tax credits modestly increased employment over time but had no measurable impact on wages, while refundable credits temporarily boosted wages without affecting employment levels. Critically, neither credit type influenced GSP or industry concentration, suggesting that job gains did not translate into broader economic development. Thom attributes these limited effects to program inefficiencies, rent-seeking behavior by existing industry participants, and weak oversight mechanisms.

#### How My Research Extends Thom (2018)

**Temporal Extension Beyond 2013**: My research directly continues Thom's work by analyzing the period from 2014-2022, a critical gap in the literature. This nine-year extension is particularly important because:

1. **California's major program expansions occurred after Thom's study period**: The 2015 Film and Television Tax Credit Program (AB 1839) tripled the annual cap from $100 million to $330 million, and the 2020 expansion (AB 2021) extended the program through 2025 with expanded eligibility. Thom's analysis could not capture these substantial policy changes.

2. **The film production landscape changed dramatically post-2013**: The rise of streaming platforms (Netflix, Amazon Prime, Apple TV+, Disney+) fundamentally altered production economics and location decisions. My analysis captures these structural industry changes that Thom's period could not address.

3. **Testing whether Thom's null findings persist**: Thom found limited employment effects and no wage effects for transferable credits during 1998-2013. California's aggressive post-2013 expansions provide a natural experiment to test whether larger, more generous programs can overcome the limitations Thom documented.

**Addressing the "What Happens Next?" Question**: Thom's study leaves open the question of whether his findings represent fundamental limitations of film tax credits or whether they reflect the specific programs and time period he analyzed. By examining California's substantially larger and more recent program expansions, I can distinguish between these interpretations and assess whether policy design improvements addressed earlier program shortcomings.

### 2. Political Behavior and Voting for Tax Incentives (Owens & Rennhoff, 2024)

#### Summary

Owens and Rennhoff provide micro-level evidence that political incentives—rather than economic rationale—drive legislative support for film tax credits. Analyzing roll-call votes, they find that party affiliation, gubernatorial alignment, electoral margins, and inter-state competition significantly predict legislator voting patterns, while local film industry presence and direct industry donations do not. Their findings suggest that film tax credits persist due to electoral calculations and political visibility rather than demonstrated economic effectiveness.

#### Connection to My Research

While my primary focus is the employment impact analysis (Research Question 2), Owens and Rennhoff's political economy framework motivates an important supplementary descriptive analysis. If film tax credits are adopted and expanded for political reasons rather than economic evidence, this could explain why programs persist despite mixed empirical results (as documented by Thom 2018 and Bradbury 2020). 

I incorporate their insights by conducting descriptive analysis of California's 2015 and 2020 expansion timing relative to gubernatorial election cycles. This political context helps interpret my employment findings: if I detect positive employment effects, are they economically meaningful or politically timed? If I find null effects, do programs persist anyway due to electoral incentives? This descriptive component enriches my analysis without requiring a full political economy model, positioning my work as primarily an employment study with political awareness.

### 3. The Economics of State Film Incentives (Rickman & Wang, 2020)

#### Summary

Rickman and Wang provide critical methodological guidance for evaluating film incentives, systematically applying synthetic control methods (SCM) to multiple states using Bureau of Labor Statistics QCEW data for the motion picture industry (NAICS 512110). They find that while film incentives often increase sector employment and wages in early-adopter states, the effects vary substantially by state context and program design. Importantly, they critique earlier industry-sponsored impact studies that overstated benefits by assuming all production was caused by incentives, establishing the need for rigorous counterfactual methods.

#### Methodological Justification and Data Limitations

**Why I Use QCEW Data (Following Rickman & Wang)**: Rickman and Wang establish QCEW as the standard administrative data source for film industry employment analysis, providing comprehensive, quarterly coverage of employment and wages by industry and state. This justifies my use of the same data source (NAICS 512110) for consistency with the established literature and to ensure comparability with prior findings.

**Critical Limitation—The Reclassification Problem**: However, QCEW data has a fundamental limitation that Rickman and Wang do not fully address: **employment increases may reflect strategic firm reclassification rather than genuine job creation**. Specifically:

1. **Cross-state reclassification**: Multi-state production companies could reclassify employees from Texas or other locations to California for reporting purposes to maximize tax credit eligibility, showing increased California QCEW employment without actual worker migration or new hires.

2. **NAICS code gaming**: Firms might reclassify workers from related industries (advertising, post-production, digital media) into NAICS 512110 to demonstrate program participation, creating statistical employment gains without real industry growth.

3. **Temporary vs. permanent effects**: QCEW captures project-based employment that may disappear immediately after credit eligibility periods end, making it difficult to distinguish between sustained industry growth and temporary statistical artifacts.

**My Solution—American Community Survey Validation**: To address this critical gap, I supplement QCEW analysis with American Community Survey (ACS) migration data examining whether individuals actually moved to California for motion picture occupations during the post-2015 and post-2020 expansion periods. ACS migration data tracks actual residential moves and occupation codes, providing a validity check on QCEW employment trends. If QCEW shows employment increases but ACS shows no corresponding in-migration of film workers, this suggests reclassification rather than genuine job creation. This dual-data approach strengthens causal inference beyond what Rickman and Wang accomplished.

**Synthetic Control Method for Robustness**: Following Rickman and Wang's methodological innovation, I implement synthetic control methods as a robustness check on my difference-in-differences estimates. This addresses concerns about control group selection and parallel trends assumptions that could bias standard DiD results.

### 4. Do State Movie Production Incentives Promote Economic Development? (Bradbury, 2020)

#### Summary

Bradbury addresses the fundamental policy question: do film tax credits generate broader economic development benefits beyond the motion picture industry itself? Using instrumental variable methods and panel data from 2000-2015, he examines whether film incentives increase state per capita income and gross state product. His findings are decisively negative—film tax credits show no measurable impact on aggregate state economic outcomes. Even when industry-level employment gains exist, they do not translate into broader prosperity or spillover effects.

#### Why Industry-Level Analysis Still Matters

Bradbury's null macro findings might suggest that studying California's employment effects is pointless if they don't improve overall state welfare. However, my research addresses three critical questions that Bradbury's aggregate analysis cannot answer:

1. **Do modern, large-scale programs work differently?** Bradbury's period ends in 2015, missing California's tripled program cap and the streaming era transformation. If even California's massive post-2015 expansions show limited industry employment effects, this strengthens the case against film incentives. Conversely, if they do show effects, we need to understand why they don't translate to aggregate gains (zero-sum competition? displacement of other sectors? pure redistribution?).

2. **Distinguishing real vs. statistical effects**: My ACS migration analysis addresses whether observed employment changes represent genuine economic activity or statistical artifacts (reclassification, gaming). Bradbury's aggregate nulls could reflect either ineffective programs or poor measurement—my micro-level analysis helps distinguish these interpretations.

3. **Political economy puzzle**: If film tax credits don't work at either industry or aggregate levels, why do they persist and expand? Understanding whether programs produce even industry-level gains (and whether these are real or illusory) is essential for explaining the political economy documented by Owens and Rennhoff (2024). My findings contribute to this puzzle regardless of whether they're positive or null.

In essence, Bradbury motivates my research by showing that the "final answer" on welfare effects is negative, making it crucial to understand the micro-mechanisms and political incentives that sustain these programs despite their documented ineffectiveness.

## Data Collection and Methodology

### Primary Research Question: Employment and Wage Impact Analysis (California)

#### Data Sources

**Primary Employment Data:**
- Bureau of Labor Statistics Quarterly Census of Employment and Wages (QCEW) for motion picture and video industries (NAICS 512110, 2009-2022)
- Following Rickman & Wang (2020) data standard for literature comparability

**Migration Validation Data:**
- American Community Survey (ACS) 1-Year Estimates: State-to-state migration flows by occupation
- ACS occupation codes for motion picture occupations (SOC codes 27-2012, 27-4031, 27-4032, and related)
- Annual migration data for California in-migration from other states (2010-2022)
- This addresses the critical reclassification concern by tracking actual worker residential moves

**Control State Selection:**
- National Conference of State Legislatures film incentive database to identify states without major policy changes during treatment period
- Bureau of Economic Analysis state-level economic controls (GDP, unemployment)
- U.S. Census Bureau demographic data for matching

**Political Timing Data (Descriptive Supplement):**
- California Secretary of State gubernatorial election dates and results
- California Legislative Analyst's Office budget documents
- LexisNexis State Capital for policy timeline

#### Methodology

**1. Difference-in-Differences Framework** *(Following Thom 2018, extending to 2022)*

I construct a quarterly panel of employment and wages for California and control states (2009-2022), estimating:

```
Y_st = α + β₁(CA × Post2015) + β₂(CA × Post2020) + γ_s + δ_t + X_st + ε_st
```

Where:
- Y_st = log employment or log average wages in motion picture industry
- CA = California indicator
- Post2015 = indicator for quarters after Q2 2015 (AB 1839 expansion)
- Post2020 = indicator for quarters after Q3 2020 (AB 2021 expansion)
- γ_s = state fixed effects
- δ_t = time fixed effects
- X_st = economic controls (state GDP growth, unemployment rate)

**Control states** will be selected based on: (1) parallel pre-treatment trends in motion picture employment (2009-2014), (2) absence of major film incentive changes during 2015-2022, (3) similar pre-treatment industry size, and (4) economic similarity. Likely candidates include Texas, Florida, Illinois, and Pennsylvania.

**Event study specification** to test parallel trends assumption:
```
Y_st = α + Σ βk(CA × Quarterk) + γ_s + δ_t + X_st + ε_st
```
Where Quarterk indicates periods relative to policy expansion dates.

**2. American Community Survey Migration Analysis** *(Novel contribution addressing reclassification concern)*

To distinguish genuine job creation from statistical reclassification, I analyze ACS migration data:

**Analysis 1—In-migration of Film Workers:**
- Track California in-migration for motion picture occupations before vs. after 2015 and 2020 expansions
- Compare to in-migration trends for other professional occupations (placebo test)
- If QCEW shows employment increases but ACS shows no increase in film worker in-migration, this suggests reclassification rather than genuine job creation

**Analysis 2—Source States:**
- Identify which states saw increased out-migration of film workers to California post-expansion
- Test whether high-tax-credit competitor states (e.g., Georgia, Louisiana) lost workers to California
- If out-migration comes from non-competitor states, this suggests genuine industry attraction rather than zero-sum poaching

**Analysis 3—Occupation-Specific Trends:**
- Examine whether California gained workers in specific high-skill film occupations (directors, cinematographers) vs. general production workers
- Different occupation patterns could distinguish between production location shifts (high-skill migration) vs. administrative reclassification (no skilled worker migration)

**3. Synthetic Control Method** *(Following Rickman & Wang 2020)*

As a robustness check, I implement synthetic control to construct a "Synthetic California" from weighted donor states:

- **Pre-treatment period**: 2009 Q1 - 2015 Q1 (before AB 1839)
- **Donor pool**: States without major incentive changes 2015-2022
- **Matching variables**: Quarterly employment, average wages, state GDP, unemployment
- **Treatment effect**: Difference between actual California and Synthetic California post-2015

This addresses concerns about parallel trends assumptions and control group selection sensitivity in standard DiD.

**4. Robustness and Specification Checks**

- **Placebo tests**: Assign false treatment dates (e.g., 2013, 2017) to test for spurious effects
- **Alternative control groups**: Test sensitivity to different donor state selections
- **Clustering**: Standard errors clustered at state level
- **Different time windows**: Test effects using 1-year, 2-year, and 3-year post-treatment windows

### Supplementary Analysis: Political Timing (Descriptive)

*Motivated by Owens & Rennhoff (2024)*

As a descriptive supplement to the employment analysis, I will examine whether California's 2015 and 2020 film tax credit expansions align with gubernatorial election cycles, providing political context for interpreting economic findings.

#### Approach

1. **Timeline Documentation**: Map California's policy changes relative to gubernatorial elections:
   - 2015 expansion (AB 1839): signed by Governor Brown during his final term
   - 2020 expansion (AB 2021): timing relative to Governor Newsom's term
   - Compare to pre-election vs. post-election periods

2. **Simple Descriptive Statistics**:
   - Calculate months between policy enactments and nearest elections
   - Note whether expansions occur in election years vs. off-years
   - Document stated political rationales from legislative records and news coverage

3. **Interpretation**: This descriptive analysis helps contextualize employment findings—if expansions align with electoral incentives (as Owens & Rennhoff document for legislative votes), this suggests political rather than economic motivations may drive program design, regardless of whether employment effects materialize.

## Simplified Implementation Plan

*Streamlined approach for feasible completion while maintaining methodological rigor*

**Week 1-2: Data Collection**
- Download BLS QCEW quarterly data for California and control states (Texas, Florida, Illinois, New York)
- Extract motion picture employment and wages (NAICS 512110) for 2009-2022
- Collect state-level economic controls (unemployment, GDP growth)

**Week 3-4: Analysis**
- Basic difference-in-differences estimation focusing on 2015 expansion
- Event study plots to visualize parallel trends and treatment effects
- Simple synthetic control as robustness check

### Phase 2: ACS Migration Validation (Weeks 5-6)

**Week 5: ACS Data**
- Download American Community Survey state-to-state migration flows
- Focus on motion picture occupation codes (SOC 27-XXXX series)
- Extract California in-migration data 2010-2022

**Week 6: Migration Analysis**
- Compare pre/post-2015 trends in film worker migration to California
- Test whether QCEW employment gains correspond to actual worker migration
- Placebo test: compare to other professional occupation migration trends

### Phase 3: Writing and Descriptive Political Analysis (Weeks 7-8)

**Week 7: Political Timing**
- Simple timeline of California's 2015 and 2020 expansions relative to elections
- Document political context from legislative records
- Descriptive statistics on timing patterns

**Week 8: Writing and Integration**
- Synthesize QCEW and ACS findings
- Interpret results in context of Thom (2018) and literature
- Discuss implications for policy effectiveness

## Expected Contributions

My research makes four key contributions to the film tax credit literature:

### 1. Temporal Extension of Thom (2018)

I directly continue Thom's seminal work by analyzing California's post-2013 period, specifically the major 2015 and 2020 expansions that tripled program funding. This addresses a critical gap—testing whether Thom's modest findings persist in the modern streaming era and with substantially larger programs.

### 2. Methodological Innovation: Dual-Data Validation

**Novel contribution:** I am the first to use American Community Survey migration data to validate QCEW employment findings in film tax credit research. This addresses the fundamental "reclassification problem"—distinguishing whether QCEW employment gains reflect:
- Genuine job creation (workers moving to California)
- Statistical artifacts (firms reclassifying existing employees across state lines)
- Administrative gaming (NAICS code manipulation)

This dual-data approach provides stronger causal inference than existing studies that rely solely on administrative employment data.

### 3. Bridging Micro and Macro Findings

I connect Bradbury's (2020) aggregate null findings with industry-level mechanisms. By examining whether California's expansions produce even sector-specific employment gains—and whether these are real or illusory—I help explain why film tax credits show no aggregate economic benefits despite their political persistence.

### 4. Political Economy Context

Following Owens & Rennhoff (2024), I provide descriptive evidence on whether expansion timing aligns with electoral cycles. This political context helps interpret economic findings: programs may persist due to electoral incentives regardless of effectiveness, explaining the puzzle of continued investment despite mixed empirical evidence.

## Research Timeline (8 Weeks)

- **Weeks 1-2**: QCEW data collection and panel construction
- **Weeks 3-4**: Difference-in-differences and synthetic control estimation
- **Weeks 5-6**: ACS migration data analysis and validation
- **Weeks 7**: Political timing descriptive analysis
- **Week 8**: Writing and synthesis
