# Abstract and Literature Review: Film Tax Credits and California Employment Effects

## Abstract

In this paper, I evaluate the employment and wage effects of California's film tax credit expansions in 2015 and 2020 using contemporary data that extends beyond previous studies. Building directly on Thom's (2018) national analysis which ended in 2013, I examine whether more recent program expansions generated sustained employment or wage gains in the motion picture industry. I construct a panel of motion picture employment and wage data from 2009-2022 using Bureau of Labor Statistics Quarterly Census of Employment and Wages (QCEW) data and estimate policy impacts through difference-in-differences models with appropriate control states, supplemented by synthetic control methods for robustness.

Recognizing that QCEW data has important limitations—particularly the risk of capturing employee reclassification across state lines rather than genuine job creation—I supplement my analysis with American Community Survey (ACS) migration data to distinguish between actual worker relocation to California and potential strategic firm reporting. Additionally, I provide descriptive analysis of the political timing of these expansions relative to gubernatorial election cycles, exploring whether policy changes align with electoral incentives as suggested by recent political economy research. My approach addresses a critical gap in the literature: understanding whether film tax credits continue to show employment effects in the post-2013 period, and whether these effects represent genuine economic gains or statistical artifacts of firm behavior.

## Literature Review

The academic literature on film tax credits reveals a persistent puzzle: despite weak empirical evidence of economic benefits, these programs remain politically popular and continue to expand. This review examines four foundational papers that establish what we know about effects (Thom 2018), how to measure them rigorously (Rickman & Wang 2020), why industry-level analysis matters despite aggregate nulls (Bradbury 2020), and why ineffective programs persist (Owens & Rennhoff 2024). Together, these studies reveal two critical gaps: a **temporal gap** (most data end before California's major 2015 expansion) and a **methodological gap** (distinguishing genuine job creation from statistical artifacts). My research addresses both.

### 1. Lights, Camera, but No Action? Tax and Economic Development Lessons from State Motion Picture Incentive Programs (Michael Thom, 2018)

#### Summary

Thom provides the most comprehensive national evaluation of motion picture incentive (MPI) programs to date, analyzing state-level panel data from 1998–2013. Using difference-in-differences estimation, he examines the effects of various incentive types on employment, wages, gross state product (GSP), and industry concentration across all U.S. states. His key findings reveal mixed and modest results: transferable tax credits modestly increased employment over time but had no measurable impact on wages, while refundable credits temporarily boosted wages without affecting employment levels. Critically, neither credit type influenced GSP or industry concentration, suggesting that job gains did not translate into broader economic development. Thom attributes these limited effects to program inefficiencies, rent-seeking behavior by existing industry participants, and weak oversight mechanisms.

#### How My Research Extends Thom (2018)

**Temporal Extension Beyond 2013**: My research directly continues Thom's work by analyzing the period from 2014-2022, a critical gap in the literature. This nine-year extension is particularly important because:

1. **California's major program expansions occurred after Thom's study period**: The 2015 Film and Television Tax Credit Program (AB 1839) tripled the annual cap from $100 million to $330 million, and the 2020 expansion (AB 2021) extended the program through 2025 with expanded eligibility. Thom's analysis could not capture these substantial policy changes.

2. **The film production landscape changed dramatically post-2013**: The rise of streaming platforms (Netflix, Amazon Prime, Apple TV+, Disney+) fundamentally altered production economics and location decisions. My analysis captures these structural industry changes that Thom's period could not address.

3. **Testing whether Thom's null findings persist**: Thom found limited employment effects and no wage effects for transferable credits during 1998-2013. California's aggressive post-2013 expansions provide a natural experiment to test whether larger, more generous programs can overcome the limitations Thom documented.

**Addressing the "What Happens Next?" Question**: Thom's study leaves open whether his findings represent fundamental limitations of film tax credits or artifacts of his specific time period. By examining California's substantially larger post-2013 expansions, I test whether bigger programs overcome earlier limitations or whether Thom's modest findings persist even with tripled funding and streaming-era industry dynamics.

### 2. The Economics of State Film Incentives (Rickman & Wang, 2020)

#### Summary

Rickman and Wang provide critical methodological guidance for evaluating film incentives, systematically applying synthetic control methods (SCM) to multiple states using Bureau of Labor Statistics QCEW data for the motion picture industry (NAICS 512110). They find that while film incentives often increase sector employment and wages in early-adopter states, the effects vary substantially by state context and program design. Importantly, they critique earlier industry-sponsored impact studies that overstated benefits by assuming all production was caused by incentives, establishing the need for rigorous counterfactual methods.

#### How This Informs My Methodology

Rickman and Wang establish QCEW (NAICS 512110) as the standard data source for film industry employment analysis, which I adopt for consistency and comparability. Their synthetic control methodology provides a crucial robustness check for my difference-in-differences estimates, addressing concerns about parallel trends and control group selection.

**The Reclassification Problem**: However, Rickman and Wang leave unresolved a critical data limitation: **QCEW employment increases may reflect strategic firm behavior rather than genuine job creation**. Three mechanisms could produce spurious employment gains:

1. **Cross-state reclassification**: Multi-state production companies could reclassify employees from Texas or other locations to California for reporting purposes to maximize tax credit eligibility, showing increased California QCEW employment without actual worker migration or new hires.

2. **NAICS code gaming**: Firms might reclassify workers from related industries (advertising, post-production, digital media) into NAICS 512110 to demonstrate program participation, creating statistical employment gains without real industry growth.

3. **Temporary project-based employment**: Credits may simply shift production timing within California, creating temporary employment spikes without sustained industry growth.

**My Methodological Innovation**: I address this gap through dual-data validation—supplementing QCEW analysis with American Community Survey (ACS) migration data that tracks actual residential moves by occupation. If QCEW shows employment gains but ACS shows no corresponding in-migration of film workers, this reveals reclassification rather than genuine job creation. This approach provides stronger causal inference than existing studies relying solely on administrative employment data.

### 3. Do State Movie Production Incentives Promote Economic Development? (Bradbury, 2020)

#### Summary

Bradbury addresses the fundamental policy question: do film tax credits generate broader economic development benefits beyond the motion picture industry itself? Using instrumental variable methods and panel data from 2000-2015, he examines whether film incentives increase state per capita income and gross state product. His findings are decisively negative—film tax credits show no measurable impact on aggregate state economic outcomes. Even when industry-level employment gains exist, they do not translate into broader prosperity or spillover effects.

#### Why Industry-Level Analysis Matters Despite Aggregate Nulls

Bradbury establishes that film tax credits fail the ultimate policy test—they don't improve aggregate state welfare. This might suggest studying California's employment effects is pointless. However, his aggregate null findings make my industry-level analysis more important, not less, for three reasons:

**First, testing modern program design**: Bradbury's data end in 2015, missing California's tripled program cap. If even this massive expansion shows limited industry effects, it strengthens the case against film credits. If it does show industry gains that don't translate to aggregate benefits, we need to understand why—zero-sum competition, sectoral displacement, or pure redistribution?

**Second, distinguishing measurement from reality**: Bradbury's nulls could reflect either genuinely ineffective programs or measurement problems in administrative data. My ACS migration validation helps distinguish these interpretations by testing whether observed QCEW employment gains represent real economic activity or statistical artifacts.

**Third, explaining political persistence**: Bradbury's findings create a puzzle—if these programs don't work, why do they persist and expand? Understanding whether they produce even narrow industry gains (real or illusory) is essential for explaining their continued political support, which the next paper addresses.

### 4. Political Behavior and Voting for Tax Incentives (Owens & Rennhoff, 2024)

#### Summary

Owens and Rennhoff solve the persistence puzzle by showing that film tax credits are driven by political incentives rather than economic evidence. Analyzing legislative roll-call votes, they find that party affiliation, gubernatorial alignment, electoral margins, and inter-state competition predict legislator support—while local film industry presence and industry donations do not. Film tax credits persist because they offer visible political wins and electoral advantages, not because they deliver demonstrated economic benefits.

#### How This Contextualizes My Research

This political economy finding reframes how we should interpret employment effects. Even if California's expansions show positive QCEW employment gains, we must ask: are these economically meaningful or politically timed? Even if I find null employment effects, Owens and Rennhoff explain why programs expand anyway—electoral incentives override empirical evidence.

I incorporate this insight through supplementary descriptive analysis of California's 2015 and 2020 expansion timing relative to gubernatorial elections. This positions my research correctly: I'm primarily testing employment effects (extending Thom 2018), but with awareness that political logic may dominate economic logic in program design and persistence.

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
