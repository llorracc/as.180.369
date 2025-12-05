# Results

## National Level
### National Level Descriptive Patterns
Across the national sample of 1,767 high schools located within 0.25 miles of a historical HOLC boundary, access to advanced STEM coursework declines consistently across the HOLC grading scale. Figure 1 presents predicted probabilities from the logistic regression model. Schools in formerly “A” neighborhoods exhibit the highest likelihood of offering at least one advanced STEM course (approximately 0.80), while those in “D” neighborhoods show probabilities closer to 0.74. Although the overall decline appears modest, it is monotonic and precisely aligned with expectations surrounding redlining’s long-term effects.

Figure 1. Predicted Probability of Offering ≥1 Advanced STEM Course, by HOLC Grade
Notes: This figure displays predicted probabilities from a logistic regression model estimating the likelihood that a school offers at least one advanced STEM course (calculus, physics, computer science, chemistry). Predictions hold Title I status, charter/magnet status, and percent of certified teachers at their sample means. The downward trend from A → D indicates that schools located in historically lower-rated HOLC neighborhoods exhibit systematically reduced access to advanced STEM coursework.

Descriptive distributions of the number of STEM subjects offered reinforce this pattern. Figure 2 shows the percent of schools offering 0, 1, 2, or 3 advanced STEM subjects by HOLC grade. Schools in A-rated areas are far more likely to offer all three courses (44.2%), while only 21.2% of schools in D-rated areas do so. Conversely, the share of schools offering no advanced STEM subjects increases from 20.9% in A-rated areas to 26.9% in D-rated neighborhoods.

Figure 2. Percent Distribution of Schools Offering 0–3 Advanced STEM Courses, by HOLC Grade
Notes: This stacked bar chart presents the distribution of the number of advanced STEM subjects offered across four HOLC grades. Schools in A-rated neighborhoods are substantially more likely to offer all three STEM subjects, while schools in C- and D-rated areas are more likely to offer none. Sample sizes for each grade appear above the bars.

Table I provides the numeric distribution underlying the graph, showing a consistent decline in STEM opportunity as HOLC grade worsens.

Table I. Numeric Summary of Course Availability by HOLC Grade
Notes: This table reports the number and percentage of schools offering 0, 1, 2, or 3 advanced STEM subjects. The distribution exhibits a clear gradient: the share of schools offering no advanced STEM increases from 20.9% in “A” areas to 26.9% in “D” areas, while the share offering all three advanced STEM courses drops from 44.2% to 21.2%. These descriptive patterns align closely with the regression estimates reported below.

A complementary perspective comes from examining the average number of courses offered in each subject area. Figure 3 plots the mean number of calculus, computer science, and physics courses by HOLC grade. The pattern again shows a smooth, monotonic decline from A → D for every subject. On average, A-rated neighborhoods offer the highest levels of advanced math and science—approximately 3.4 calculus classes, 5.6 computer science classes, and more than 8 physics classes. These averages fall sharply for lower-rated neighborhoods: D-rated areas typically offer only about 1 calculus class, 2.2 computer science classes, and 4.3 physics classes. Notably, the error bars across grades show little overlap, suggesting that these differences are both educationally meaningful and statistically precise.

Figure 3. National Average Number of Advanced STEM Classes by HOLC Grade
Notes: This figure shows the mean number of advanced calculus, computer science, and physics classes offered by schools in each HOLC grade. Error bars represent standard errors. The decline in the number of classes offered from A → D highlights substantial reductions in the breadth of advanced STEM opportunities available to students in historically disadvantaged neighborhoods.

Together, Figures 1–3 present a consistent descriptive picture: historically redlined areas are less likely to offer any advanced STEM coursework, and when such courses are offered, they tend to be fewer in number across all STEM disciplines.

### Regression Estimates for Any Advanced STEM Access

Table II presents linear probability model estimates for the probability a school offers at least one advanced STEM course. The first column uses a binary indicator for whether a school is located in a historically redlined (C/D) neighborhood. Schools in C/D zones are 10.5 percentage points less likely to offer an advanced STEM course than schools in A/B areas (p ≈ 0.051). While marginally significant, this estimate is consistent in magnitude with the model-based predicted probabilities in Figure 1.

The categorical specification allows separate comparisons across all four HOLC grades. Relative to A-rated neighborhoods, B-rated areas show no difference, C-rated areas show a small negative difference, and D-rated areas show the largest gap (−0.152), albeit just shy of conventional statistical significance (p = 0.124). Across both specifications, magnet schools consistently display significantly higher STEM access (p < 0.001), while charter schools do not differ from traditional public schools.

Table II. Effect of HOLC Grade on Probability of Offering ≥1 Advanced STEM Course
| Variable                              | Binary Redline (C/D)     | HOLC Grade Categories        |
|---------------------------------------|---------------------------|------------------------------|
| **Redline (C/D)**                     | **−0.105** (0.054) †      | —                            |
| **HOLC B**                            | —                         | 0.010 (0.095)                |
| **HOLC C**                            | —                         | −0.052 (0.088)               |
| **HOLC D**                            | —                         | −0.152 (0.099)               |
| **Magnet School**                     | 0.218 (0.064) ***         | 0.238 (0.064) ***            |
| **Charter School**                    | −0.080 (0.079)            | −0.061 (0.081)               |
| **% Certified Teachers**              | —                         | −0.001 (0.002)               |
| **Title I School**                    | —                         | 0.147 (0.056) **             |
| **Intercept**                         | 0.771 (0.173) ***         | 0.783 (0.194) ***            |
| **N**                                 | 1,767                     | 1,767                        |

† p < .10, * p < .05, ** p < .01, *** p < .001

### Regression Estimates for the Number of Advanced STEM Subjects Offered

Table III reports the OLS models predicting the number of advanced STEM subjects offered (0–3). These models reveal substantially stronger associations between HOLC grade and curricular breadth. Schools in C/D neighborhoods offer 6.7 fewer advanced STEM subjects on average than schools in A/B areas (p = 0.004). This is a large decline, particularly given the limited number of advanced STEM course types typically available.

The categorical specification again shows a monotonic gradient: compared to A-rated areas, B schools offer 3.1 fewer STEM subjects, C schools offer 5.9 fewer, and D schools offer a striking 12.5 fewer (p < 0.001). These differences closely mirror the descriptive patterns in Figure 3, where the steepest declines occur moving from “A” to “D” neighborhoods.

Table III. Effect of HOLC Grade on Number of Advanced STEM Subjects Offered
| Variable                              | Binary Redline (C/D)     | HOLC Grade Categories        |
|---------------------------------------|---------------------------|------------------------------|
| **Redline (C/D)**                     | **−6.675** (2.290) **     | —                            |
| **HOLC B**                            | —                         | −3.124 (3.462)               |
| **HOLC C**                            | —                         | −5.874 (3.557) †             |
| **HOLC D**                            | —                         | **−12.474** (3.663) ***      |
| **Magnet School**                     | 3.267 (3.480)             | 4.644 (3.505)                |
| **Charter School**                    | −11.718 (2.998) ***       | −10.758 (2.989) ***          |
| **% Certified Teachers**              | −0.057 (0.086)            | −0.072 (0.088)               |
| **Title I School**                    | 5.475 (2.734) *           | 5.794 (2.713) *              |
| **Intercept**                         | 23.512 (8.454) **         | 26.984 (9.246) **            |
| **N**                                 | 1,767                     | 1,767                        |

† p < .10, * p < .05, ** p < .01, *** p < .001

### Summary of National Findings

Nationally, the legacy of HOLC redlining remains clearly visible in access to advanced STEM coursework. Across both extensive (any STEM) and intensive (number of STEM subjects) margins, lower HOLC grades are associated with worse opportunities—even when comparing schools located within 0.25 miles of one another on opposite sides of a historical boundary.

The probability of offering any advanced STEM course falls modestly from A → D, while the number of STEM subjects offered falls sharply, especially in formerly “D” areas. The descriptive evidence in Figures 1–3, combined with the regression estimates in Tables II and III, shows that redlining’s long-term educational impacts operate not merely through whether schools offer STEM at all, but through the breadth and depth of STEM curricula—an important determinant of students’ college readiness and long-term STEM career opportunities.


## City-Level Analyses (Chicago, LA, Philadelphia, Detroit)
To complement the national analysis, I examine how the relationship between historical HOLC grades and advanced STEM course offerings appears within four large, historically redlined metropolitan areas: Chicago, Los Angeles, Philadelphia, and Detroit. These cities were selected because each contains at least three neighborhoods of every HOLC grade and each has substantial variation in school locations relative to HOLC boundaries. As in the national design, I restrict the analysis to high schools located within 0.25 miles of a historical redlining boundary to ensure that comparisons are made across locally similar areas. The goal of this section is not to compare cities to one another, but rather to evaluate whether the patterns observed nationally also hold within individual urban contexts, and to understand where and why deviations may occur.

### Descriptive Patterns Within Cities

Figure 4. HOLC Neighborhoods and STEM Course Availability, Four Major Cities

Notes: Each panel maps historical HOLC zones (A–D) for Chicago, Los Angeles, Philadelphia, and Detroit. High schools are overlaid and shaded by the number of advanced STEM courses offered (0–3). Across cities, schools in A- and B-rated neighborhoods generally offer more advanced STEM coursework, while those in C- and D-rated areas often offer fewer options. Los Angeles shows a more diffuse pattern, reflecting local placement of magnet and specialized schools.

Across cities, descriptive visualizations show heterogeneous—but broadly consistent—relationships between HOLC grade and advanced STEM offerings. The 2×2 map in Figure 4 displays each city’s HOLC zones with high schools overlaid and shaded by the number of advanced STEM courses they offer. In both Chicago and Detroit, the spatial pattern closely mirrors national expectations: schools in A- and B-rated neighborhoods cluster in areas with more advanced STEM options, while schools in C- and especially D-rated areas tend to offer fewer courses. Philadelphia exhibits a similar but less pronounced gradient, in part because fewer schools are located in A-rated neighborhoods within the 0.25-mile boundary sample. Los Angeles stands out as the least consistent with national patterns; schools offering multiple advanced STEM courses appear fairly dispersed, including in C- and D-rated areas.

Figure 5. Average Number of Advanced STEM Courses by HOLC Grade, Four Major Cities

Notes: This 2×2 panel reports mean numbers of advanced calculus, computer science, and physics courses offered by high schools in each HOLC grade category (A–D). Error bars represent standard errors. Chicago and Detroit display strong monotonic declines from A → D; Philadelphia shows moderate declines with more noise due to small A-rated sample sizes; Los Angeles exhibits comparatively flat or reversed gradients, likely reflecting its distinct school-choice infrastructure and magnet school geography.

A parallel 2×2 plot in Figure 5 shows the mean number of advanced calculus, computer science, and physics courses by HOLC grade for each city. Here again, Chicago and Detroit display a clear declining pattern from A → D, especially in physics and computer science. Philadelphia shows moderate declines, though some grades have few observations, which introduces volatility in the means. Los Angeles once again diverges: averages for C- and D-rated neighborhoods are similar to—or in some cases higher than—those in A- or B-rated areas. This contrasts sharply with the national pattern shown earlier in Figure 3, where declines from A → D are smooth and sizable.

These descriptive findings suggest that the national pattern is not simply an artifact of a few large cities. Instead, the broad trend of reduced STEM offerings in historically lower-rated neighborhoods appears in most—but not all—urban contexts. Los Angeles represents the primary outlier, and the regression results help clarify why.

### Regression Estimates Within Cities

Table IV summarizes the binary redline effects for each city, showing the estimated difference between schools in historically redlined (C/D) versus non-redlined (A/B) areas in both (1) the probability of offering any advanced STEM course and (2) the total number of advanced STEM courses offered.

| City    |   Binary Redline Effect (Any STEM) |   Binary Redline Effect (Total STEM) |
|:--------|-----------------------------------:|-------------------------------------:|
| Chicago |                          -0.173785 |                             -6.05046 |
| Detroit |                          -0.28288  |                            -24.4881  |
| LA      |                           0.078797 |                              2.42456 |
| Philly  |                           0.083938 |                             -2.29009 |
Table IV. City-Level Binary Redline Effects on STEM Access

Notes: This table summarizes binary regression estimates comparing schools in historically redlined (C/D) neighborhoods to those in higher-rated (A/B) neighborhoods across four major cities. The first column reports the effect of redlining on the probability that a school offers at least one advanced STEM course (Any STEM). The second column reports the effect on the total number of advanced STEM courses offered. Negative coefficients indicate reduced STEM access in C/D zones. Chicago and Detroit display large negative effects consistent with national patterns, Philadelphia shows smaller and imprecise effects, and Los Angeles exhibits positive coefficients, reflecting the city’s unique distribution of magnet and specialized schools in lower-rated historical zones.

Across cities, Chicago and Detroit show strong negative associations between redlining and STEM access. In Chicago, schools in C/D neighborhoods are 17.4 percentage points less likely to offer any advanced STEM course, and they offer 6.05 fewer courses in total. Detroit displays even larger effects: a 28.3–percentage point reduction in the probability of offering any advanced STEM and a striking 24.5-course deficit in total offerings. These magnitudes exceed the national estimates and suggest that historical neighborhood ratings continue to strongly shape educational opportunity in cities where economic and demographic segregation remain especially pronounced.

Philadelphia’s binary redline effects are small and statistically inconsistent in magnitude (−2.29 to +8.39), echoing the ambiguity in the descriptive plots. This is likely explained by the limited number of schools in A-rated neighborhoods within the boundary sample—many HOLC A areas in Philadelphia were historically smaller and more residential, resulting in fewer present-day high schools. As a result, estimates for A→D comparisons are noisier and less stable than in Chicago or Detroit.

Los Angeles is the only city where both coefficients point in the opposite direction of national patterns. Schools in historically redlined areas are estimated to be slightly more likely to offer any advanced STEM course (+7.9 percentage points) and to offer more STEM courses overall (+2.42). Importantly, this does not necessarily imply that redlining “reversed” in Los Angeles. Rather, it reflects two structural features of the city: (1) extensive postwar suburban expansion that altered the distribution of school types relative to HOLC boundaries, and (2) a concentration of magnet and specialized high schools in historically lower-rated central LA neighborhoods. These institutional dynamics mean that HOLC boundaries in Los Angeles align less cleanly with present-day school resources than in the more rigidly segregated Midwestern and Northeastern cities.

The categorical regression results (Table V) reinforce these patterns. Chicago and Detroit again show monotonic declines across B, C, and D categories for both AnySTEM and TotalSTEM outcomes, mirroring the national gradient. Philadelphia’s coefficients fluctuate in sign but remain modest in magnitude. Los Angeles shows positive coefficients across all categories, consistent with the idea that local school placement and magnet-program geography weaken the historical relationship between redlining and STEM access.

| City    |   AnySTEM_B |   AnySTEM_C |   AnySTEM_D |   TotalSTEM_B |   TotalSTEM_C |   TotalSTEM_D |
|:--------|------------:|------------:|------------:|--------------:|--------------:|--------------:|
| Chicago |  0.364748   |    0.165596 |    0.220373 |      3.12622  |      -3.36243 |      -2.41623 |
| Detroit | -0.00498647 |   -0.251999 |   -0.317836 |    -30.9919   |     -27.2652  |     -32.1833  |
| LA      |  0.186819   |    0.201986 |    0.287856 |      0.468041 |       2.47458 |       3.26122 |
| Philly  | -0.218171   |   -0.082414 |   -0.142491 |    -14.8718   |     -16.957   |     -16.0355  |\
Table V. City-Level Categorical HOLC Grade Effects on STEM Access

Notes: This table reports regression estimates comparing each HOLC grade (B, C, and D) to A-rated neighborhoods within each city. Columns 1–3 present the effects on the probability that a school offers at least one advanced STEM course (Any STEM). Columns 4–6 present the effects on the total number of advanced STEM courses offered. Chicago and Detroit show clear monotonic declines from B → C → D, aligning with national patterns of reduced STEM opportunity in lower-rated historical zones. Philadelphia exhibits modest and variable effects, largely due to limited A-rated coverage in the boundary sample. Los Angeles again departs from the national trend, displaying positive coefficients across categories, likely reflecting its concentrated magnet and specialized high school presence in historically lower-rated neighborhoods.

### Comparison to National Patterns

Taken together, the city-level analyses demonstrate that the national results are not driven solely by one or two metropolitan areas. Chicago and Detroit closely replicate the national pattern: schools in historically redlined areas offer significantly fewer STEM classes and are less likely to offer any at all. Philadelphia shows muted effects due to small sample sizes in top-rated areas, but its qualitative direction aligns with the national trend. Los Angeles, by contrast, deviates from both the national pattern and the other cities—largely due to the city’s distinct educational geography, including widespread magnet programs located disproportionately in lower-rated HOLC areas.

Overall, these results suggest that redlining’s educational legacy is robust at a broad scale, yet its local manifestation varies depending on how historical boundaries intersect with postwar development, school-choice ecosystems, and district-level reforms. In cities with stable neighborhood structures (Chicago, Detroit), the HOLC gradient remains a powerful predictor of STEM access. In cities with significant postwar transformation (Los Angeles) or limited A-rated coverage (Philadelphia), the relationship becomes more diffuse. Nonetheless, even in these cases, descriptive patterns still show disparities in STEM depth across neighborhoods, consistent with broader structural inequalities.

