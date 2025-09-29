# Pitch

Redlining, formalized through the Home Owners’ Loan Corporation (HOLC) maps of the 1930s, has been shown to exert enduring effects on neighborhood wealth, credit access, and education. Aaronson, Hartley, and Mazumder (2021) provide causal evidence that neighborhoods graded “C” and “D” experienced declines in homeownership, housing values, and credit access relative to adjacent, higher-rated areas. Extending this work, Aaronson et al. (2022) demonstrate that children raised in redlined neighborhoods had significantly worse long-term outcomes, including lower educational attainment and adult earnings, compared to those raised just across boundary lines. These findings highlight how redlining not only depressed asset values but also constrained intergenerational opportunities, suggesting an indirect pathway through which access to resource-intensive educational tracks, such as those leading to STEM fields, may have been curtailed.

Empirical evidence supports this link between redlining, school funding, and educational opportunity. Lukes and Cleveland (2021) show that schools located in historically redlined neighborhoods continue to receive less per-pupil funding, enroll larger shares of minority students, and post lower standardized test scores in math and reading compared to schools in higher-graded areas. Lynch et al. (2021) similarly find that historically redlined neighborhoods are associated with higher poverty, lower income, and reduced educational attainment, reinforcing the persistence of educational disadvantage. Since U.S. schools are primarily funded through local property taxes, depressed property values in redlined areas directly translate into reduced school resources, fewer advanced courses, and limited access to specialized science and math instruction. These structural barriers map closely onto the preparation needed for students to pursue postsecondary STEM degrees.

National statistics underscore how such disparities play out in STEM pathways. According to the NSF’s 2023 Diversity and STEM report, Black and Hispanic students comprise 37% of the U.S. college-age population but earn only 26% of science and engineering bachelor’s degrees, with even sharper underrepresentation in engineering. Workforce gaps mirror these patterns, as underrepresented minorities make up 24% of the labor force but hold only 16% of bachelor’s-level STEM jobs. Taken together, these studies suggest that the legacy of redlining plausibly contributes to the underrepresentation of Black and Hispanic students in STEM by shaping access to rigorous STEM preparation in K–12 schools. Testing this hypothesis would involve merging digitized HOLC map data (Mapping Inequality) with modern education data, such as the Civil Rights Data Collection (CRDC) on advanced coursework access and the American Community Survey (ACS) on field-of-degree attainment, and applying boundary discontinuity designs akin to Aaronson et al. (2021). Such an approach could provide direct evidence of whether historically redlined neighborhoods remain disadvantaged in producing STEM opportunities, extending the literature on structural racism into the domain of STEM education and workforce equity.

# Methods

Compare neighborhoods (or schools) immediately on either side of HOLC map boundaries to estimate whether historically lower-rated HOLC areas (C/D) have lower present-day STEM access (advanced math/science course availability, AP STEM offerings). Use boundary buffers + nearby comparison boundaries (propensity-weighted) to address pre-existing differences — essentially following Aaronson et al. (2021).

## Outcome

Y: school level indicator
- Share of students with access to calculus / physics / AP science / AP CS (from CRDC or state course catalogs).
- Binary: school offers AP calculus / AP physics / computer science (1/0).

## Independent Variable

REDLINE(treatment): indicator = 1 if geographic unit g lies on the lower-graded side of an HOLC boundary (C or D)

## Contemporary cross section

Y=α+βREDLINE+Xγ+δ+η+ε
- δ: city / CBSA fixed effects (compare within metro areas).
- 𝜂: boundary fixed effect if using buffer pairs. If you use a border approach, 𝜂 will be the same across the two sides and absorbs many local confounders.
- β estimates the association between historical HOLC grade and present STEM access controlling for observed covariates and local unobservables.

## Controls

- Median household income (ACS), poverty rate.
- % Black, % Hispanic, % foreign-born.
- % adults with BA or higher (to capture contemporaneous education).
- Population density / urbanicity indicator.
- School/district-level per-pupil funding (NCES CCD / state finance data).
- Distance to nearest 4-year college / technical college.
- Unemployment rate; median home value (modern).
- If school-level: school grade span, total enrollment, share free/reduced lunch.
	​
## Design choices to address pre-existing trends / differences across sides

1. Propensity-weighted comparison boundaries (construct matched pseudo-borders where pre-treatment trends are similar; then triple-diff).
2. Narrow bandwidth: restrict to units within X meters (e.g., 0.25 mile / 0.5 mile) of the HOLC border. Show sensitivity to bandwidth.
3. Covariate balancing: check whether pre-1930 (or earliest available) covariates differ — if so, use weighting or include historical controls.
4. Placebo tests: run the same RD on outcomes you expect no long-run effect on (e.g., adult rates of unrelated majors like classics), or run fake borders.

## Data Options
- [Historic redlining data](https://dsl.richmond.edu/panorama/redlining/#loc=5/39.1/-94.6)
- [k-12 course access](https://ocrdata.ed.gov/)
- K-12 School Funding: Common Core of Data (CCD) — National Center for Education Statistics (NCES). Includes district finance data (per-pupil expenditures, revenue sources).
- [college level degree completions be field, ethnicity, geography](https://nces.ed.gov/ipeds/)
- [acs 5 year estimates](https://data.census.gov/)
- Mortgage Lending / Property Values — HMDA (Home Mortgage Disclosure Act) datasets or Zillow property data for modern property value controls
- [historical 1940 census variables](https://www2.census.gov/ces/wp/2022/CES-WP-22-56.pdf?utm_source=chatgpt.com): to help control for pre HOLC variations
