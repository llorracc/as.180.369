# Discussion

## Interpretation in Context of Existing Literature

This study finds no statistically significant evidence that California's Film and Television Tax Credit Program increased employment. The SCM results (p = 0.286 for Program 2.0 and p = 0.143 for Program 3.0) fail to reject the null hypothesis, consistent with the broader literature's finding that film incentives produce limited measurable effects (Thom 2018; Button 2019; Bradbury 2020).

The significant wage premium (9.1% for 2015, p = 0.003) represents a notable exception and warrants economic interpretation. At California's average weekly wage of $2,338, a 9.1% increase translates to approximately $213 additional weekly earnings per worker, or roughly $11,000 annually. Applied to California's ~110,000 motion picture workers, this implies aggregate wage gains of approximately $1.2 billion annually—comparable to the program's $330 million annual allocation. This suggests the wage benefits may provide substantial returns to existing workers, even absent employment growth. However, this finding must be interpreted cautiously given DiD's parallel trends violations. Several alternative explanations merit consideration: (1) **composition effects**—the expanded credits may have attracted higher-budget productions requiring more experienced (and higher-paid) workers; (2) **selection into treatment**—productions seeking credits may differ systematically from those that don't apply; (3) **union bargaining**—credit availability may have strengthened unions' negotiating position on wages. Without production-level data, I cannot distinguish these mechanisms from genuine wage increases for incumbent workers.

The ACS migration evidence reveals persistent net inflow throughout 2009-2023, averaging +2,029 workers annually. However, this baseline pattern did not strengthen after tax credit expansions—net inflow actually declined from +2,058 in 2015 to just +58 in 2021. This addresses Rickman and Wang's (2020) concern about distinguishing genuine job creation from administrative reclassification.

## Robustness and Method Selection

A key contribution of this study is the explicit comparison of DiD and SCM methods, where robustness checks determined method selection. Initial DiD analysis produced concerning diagnostics:

1. **Parallel Trends Violations:** Pre-treatment trend differences between California and Georgia (0.153 log points/year) substantially exceeded acceptable thresholds. California vs. New York showed smaller divergence (0.020 log points/year), but the three-state control group was dominated by Georgia's rapid growth trajectory.

2. **Placebo Test Failures:** A placebo treatment at 2013 Q2—two years before Program 2.0—produced a significant spurious coefficient (−0.300, p = 0.005). Significant effects at false treatment dates indicate that DiD estimates may reflect pre-existing differential trends rather than causal policy effects.

These violations motivated the transition to SCM, which addresses parallel trends concerns by optimally weighting donor states based on pre-treatment predictor matching rather than assuming identical trends. The algorithm assigned 100% weight to New York for both treatments, reflecting its superior trajectory match to California.

SCM's permutation-based placebo tests provide more credible inference: California's post-treatment deviation ranked 2nd of 7 states (2015) and 1st of 7 (2020), but neither achieved statistical significance. The 2020 effect (p = 0.143) approaches marginal significance, suggesting potentially meaningful impacts that warrant further investigation with expanded donor pools.

### COVID-19 Confounding

The Program 3.0 analysis faces a fundamental identification challenge: the July 2020 treatment onset coincides with COVID-19 pandemic disruptions. Film production nationwide experienced unprecedented shutdowns, delayed projects, and workforce displacement during 2020-2021. While SCM partially addresses this by incorporating pandemic-period donor state data, separating tax credit effects from pandemic recovery remains difficult. The 2015 estimates, uncontaminated by pandemic effects, should receive greater interpretive weight. The 2020 estimates are best understood as upper bounds on potential effects, acknowledging that observed post-treatment patterns may partially reflect differential pandemic recovery rather than policy impacts.

## Policy Implications

The evidence suggests California's tax credits did not generate detectable employment growth. The wage premium indicates improved compensation for existing workers, but the failure to enhance baseline migration patterns suggests the programs functioned as defensive policy—maintaining California's existing industry advantages—rather than expanding production capacity.

The political timing analysis reveals both Program 2.0 and 3.0 were enacted within months of gubernatorial elections. To formalize: assuming legislation timing is uniformly distributed across the four-year gubernatorial cycle, the probability of a single bill falling within 6 months of an election is 6/48 ≈ 12.5%. The probability of both independent expansions falling in this window is (0.125)² ≈ 1.6%. While this calculation assumes independence and uniform distribution—simplifying assumptions that may not hold—the pattern is suggestive. This aligns with Owens and Rennhoff's (2023) finding that film tax credits persist for political rather than purely economic reasons. Visible benefits to existing workers—higher wages, industry goodwill, production announcements—may provide sufficient political justification even absent broader development goals.

## Limitations

1. **Statistical Power:** The limited donor pool (n = 6 states) constrains SCM inference. Expanding to include additional states with film industries could improve power to detect smaller effects.

2. **Cost-Effectiveness:** Lack of program expenditure data prevents cost-per-job calculations. Future research should obtain allocation data to assess whether observed effects (if any) justify program costs.

3. **Migration Measurement:** ACS captures permanent residential moves but may miss temporary project-based relocations common in film production, potentially understating production activity effects.

4. **Aggregate Analysis:** This study examines aggregate motion picture employment. Heterogeneous effects across production types (independent vs. studio), occupations (above-line vs. below-line), or firm sizes remain unexplored.

Future research should expand donor pools, incorporate program expenditure data for cost-effectiveness analysis, and explore alternative data sources capturing temporary migration patterns.
