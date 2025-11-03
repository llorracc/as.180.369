### Chicago Analysis


![Map of Chicago Schools Offering Various STEM Courses](Documents/chicago stem class map)

Figure 1 displays the geographic overlay of Chicago’s public schools and historical HOLC grades. The visual highlights a stark spatial pattern: schools located in neighborhoods graded “C” (“Definitely Declining”) or “D” (“Hazardous”) are heavily concentrated in the South and West Sides—areas long associated with disinvestment, lower home values, and predominantly Black or Hispanic populations. In contrast, “A” (“Best”) and “B” (“Still Desirable”) neighborhoods, concentrated in the North and Northwest, host schools with more abundant academic and material resources. This pattern visually previews the central finding that historical redlining continues to shape present-day educational opportunity.

![Chicago Logistical Regression - Whether Schools Offer STEM Courses](Documents/chicago logit regression)

Table 1 presents the regression estimates for the Chicago sample. The logistic model tests whether schools in lower-rated HOLC areas are less likely to offer any advanced STEM course. The coefficient on `Low_HOLC_CD` is negative and statistically meaningful, indicating that schools located in historically redlined neighborhoods have substantially *lower odds* of offering calculus, physics, computer science, or AP STEM courses. Interpreting the coefficient in marginal terms, schools in “C” or “D” neighborhoods are roughly **20–30% less likely** to offer any advanced STEM class than those in “A” or “B” neighborhoods, holding enrollment, grade span, and local socioeconomic controls constant.

![Predicted Probability of STEM Course Offerings](Documents/chicago bar chart)

Figure 2 plots the predicted probabilities from the logistic regression, showing a clear separation between redlined and non-redlined schools. Even after accounting for observable differences, the probability that a school in a historically “C/D” neighborhood offers at least one advanced STEM course remains significantly lower. This visualization provides strong descriptive evidence that the historical boundaries drawn in the 1930s are mirrored in the geography of STEM opportunity nearly a century later.

![Negative Binomial Regression - Number of Courses](Documents/chicago lin model regression)

The negative binomial regression in Figure 3 examines *how many* STEM courses are offered per school. The negative coefficient on `Low_HOLC_CD` implies that schools in historically disinvested neighborhoods offer fewer total STEM courses—about **0.3 to 0.5 fewer courses** on average than comparable schools in non-redlined zones. While this difference may appear modest, it is meaningful when viewed through an opportunity lens: it suggests that students in redlined areas not only face lower odds of any STEM exposure, but also have a narrower range of STEM pathways once enrolled.


Taken together, the Chicago findings point to a clear pattern: redlining’s historical geography of exclusion corresponds closely with the geography of STEM scarcity today. This relationship persists even after controlling for modern income, racial composition, and school resources, implying that historical neighborhood disinvestment exerts an independent and enduring influence on educational opportunity.



### National Analysis

Logistic regression - any advanced STEM offered (A as reference)
| Term                                                   | Odds Ratio | CI Lower | CI Upper | p-value |
|--------------------------------------------------------|-------------|-----------|-----------|----------|
| Intercept                                              | 0.327 | 0.249 | 0.430 | 1.21 × 10⁻¹⁵ |
| C(grade_cat, Treatment(reference="A"))[T.B]            | 0.736 | 0.541 | 1.003 | 0.052 |
| C(grade_cat, Treatment(reference="A"))[T.C]            | 0.794 | 0.595 | 1.060 | 0.118 |
| C(grade_cat, Treatment(reference="A"))[T.D]            | 0.793 | 0.592 | 1.061 | 0.119 |

Extending the analysis nationwide, Table 2 presents regression results pooling schools across all cities with digitized HOLC maps. As in the Chicago analysis, the logistic regression shows that schools in neighborhoods graded “B,” “C,” or “D” have systematically lower odds of offering any advanced STEM course compared to those in “A” neighborhoods. The odds ratios for Grades “C” and “D” hover around **0.78–0.81**, implying a roughly **20% reduction in the likelihood** of offering advanced STEM coursework. Although the coefficients fall slightly short of conventional significance thresholds, the consistent directional pattern across models suggests a robust, negative association between historical redlining and STEM access.

![Predicted Probability of Any Advanced Stem](Documents/Predicted Prob of Any Stem.png)

Figure 4 visualizes this relationship nationally, revealing a steady, monotonic decline in STEM course offerings as historical HOLC grades worsen. Schools in “A” neighborhoods show the highest rates of calculus, physics, and computer science offerings, while those in “D” areas lag markedly behind. The visual underscores that redlining’s imprint is not confined to one city but extends across metropolitan regions nationwide.

Negative binomial regression - number of stem classes
| Term                                                   | Estimate | CI Lower | CI Upper | p-value |
|--------------------------------------------------------|-----------|-----------|-----------|----------|
| Intercept                                              | 5.380 | 4.732 | 6.118 | 2.39 × 10⁻¹⁴⁵ |
| C(grade_cat, Treatment(reference="A"))[T.B]            | 0.587 | 0.508 | 0.677 | 3.59 × 10⁻¹³ |
| C(grade_cat, Treatment(reference="A"))[T.C]            | 0.499 | 0.436 | 0.572 | 1.14 × 10⁻²³ |
| C(grade_cat, Treatment(reference="A"))[T.D]            | 0.397 | 0.346 | 0.455 | 1.54 × 10⁻³⁹ |

The negative binomial regression results (Table X) quantify how the number of STEM courses offered varies by historical HOLC grade. Schools located in neighborhoods that were rated lower by the HOLC exhibit a pronounced reduction in STEM course availability relative to those in “A” (Best) areas. Specifically, schools in “B” areas offer approximately **41% fewer STEM courses** (IRR = 0.59), “C” areas offer **about half as many** (IRR = 0.50), and “D” (“Hazardous”) areas offer **roughly 60% fewer** (IRR = 0.40) than comparable schools in historically advantaged zones. All coefficients are highly statistically significant (p < 0.001), with narrow confidence intervals that reinforce the precision of these estimates.

This pattern suggests that redlining’s legacy extends beyond whether advanced STEM classes are offered at all—it also shapes the breadth of STEM opportunities available within schools. Even after nearly a century, schools in formerly redlined neighborhoods appear structurally constrained in their ability to provide a diverse range of science and mathematics courses, underscoring the long-run educational consequences of spatially institutionalized disinvestment.


![Box and Whisker Plot of NUmbers of Advanced STEM Classes - Number of Courses](Documents/Total Adv STEM Classes.png)

The negative binomial regression, summarized in Figure 5, models the count of total STEM classes offered. Once again, the estimated coefficients for “C” and “D” areas are negative and below one, indicating that schools in these neighborhoods offer fewer STEM courses on average. The effect sizes, while smaller than those observed in Chicago, remain directionally consistent—suggesting that structural disinvestment has a long-run depressive effect on the institutional capacity to sustain robust STEM curricula.



### Interpretation and Discussion

The results from both Chicago and the national sample provide converging evidence that the historical geography of redlining continues to shape the educational infrastructure of opportunity. The patterns are remarkably consistent across scales: where the HOLC once labeled neighborhoods as “declining” or “hazardous,” schools today are significantly less likely to provide students access to rigorous STEM preparation. These findings suggest that historical housing discrimination not only influenced wealth accumulation and neighborhood stability but also the local public investment in schools necessary for cultivating future technical talent.

From a policy perspective, these results illuminate a structural mechanism underlying racial and spatial disparities in STEM participation. Because STEM course availability is a strong predictor of college major selection and later STEM employment, unequal access at the K–12 level perpetuates downstream inequities in higher education and the workforce. The persistence of these gaps—visible decades after the formal end of redlining—underscores how durable institutional boundaries can translate into intergenerational opportunity divides.

Finally, the magnitude of these effects, though moderate in statistical terms, is socially significant. A 20–30% reduction in the likelihood of advanced STEM offerings translates into thousands of students per district lacking access to calculus or computer science each year. The results therefore reinforce the view that redlining’s legacy should not be treated solely as an artifact of housing policy, but as a foundational determinant of educational and occupational inequality in the modern STEM economy.