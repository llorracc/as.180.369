# Methodology

## Data
This study integrates historical redlining maps with contemporary school-level administrative data to examine whether the legacy of HOLC neighborhood ratings continues to shape access to advanced STEM coursework. The analysis combines (1) digitized 1935–1940 HOLC residential security maps from the Mapping Inequality Project, (2) the 2021–22 National Center for Education Statistics (NCES) Common Core of Data (CCD) Public School Universe file, and (3) the 2020–21 Civil Rights Data Collection (CRDC). All spatial processing and file merging were conducted in Python using geopandas, shapely, pandas, and numpy. 

### HOLC Maps
The primary historical data source consists of digitized HOLC residential security maps produced between 1935 and 1940. These maps were originally created by the Home Owners’ Loan Corporation to guide mortgage refinancing decisions and assign neighborhoods grades from “A” (Best) to “D” (Hazardous). The digitized files used in this study come from the Mapping Inequality Project (Nelson et al., 2020), which provides complete GIS polygon files for nearly 240 U.S. cities, including polygon geometries, HOLC grade labels, and transcribed area descriptions. All maps were downloaded in GeoJSON format and reprojected from their original coordinate systems into EPSG:3857 for spatial analysis.

To construct the national analytic sample, I first identified all HOLC-mapped cities containing at least three distinct HOLC grade types (A, B, C, and D). Cities lacking this minimum variation were excluded, following the logic that boundary-discontinuity identification requires meaningful grade contrasts. This filtering process resulted in 113 eligible cities. For each city, I extracted the polygon geometries and generated 0.25-mile buffers (converted to meters) around the boundary lines separating adjacent HOLC grades. These buffers were used to identify schools located near historical grade transitions.

Schools were assigned to HOLC grades using a point-in-polygon spatial join. Each school received the grade of the HOLC polygon it physically intersected, and all schools outside any HOLC polygon were excluded. In line with boundary design conventions, I further restricted the sample to schools located within 0.25 miles of a HOLC boundary, ensuring that comparisons were made between schools in close geographic proximity but on opposite sides of historically distinct rating lines.

Across the 113 included cities, this process yielded a final national analytic dataset of 1,767 schools located both within HOLC coverage and within the 0.25-mile boundary zone.

### NCES CCD Data
To identify school coordinates and basic institutional characteristics, I used the 2021–22 NCES Common Core of Data (CCD) Public School Universe file. This dataset provides school-level attributes for all U.S. public schools, including latitude (LATCOD), longitude (LONCOD), school grade span, state and district identifiers, and Title I eligibility. Since the CCD includes separate files for public and private schools, only public schools were present in the dataset used for this analysis, eliminating the need for manual removal of private institutions.

School coordinates were projected into EPSG:3857 to match the reprojection of the HOLC files before executing spatial joins. Schools were restricted to those serving grades 9 through 12, defined as any school whose grade span included both 9th and 12th grade. This filtering ensured that only institutions capable of offering advanced STEM coursework—typically offered in high school—were included.

The CCD variable for Title I status was originally categorical; I recoded this into a binary indicator for use as a control in regressions. All other demographic, staffing, and enrollment variables were obtained from the CRDC dataset (see below), as the relevant CCD fields were incomplete or missing for many schools in the years used.

### CRCD Data
The 2020–21 Civil Rights Data Collection (CRDC) provides detailed school-level information on course offerings, teacher staffing, student demographics, and program participation. This dataset served as the primary source for constructing the STEM access outcome variables and for deriving control variables related to school composition and instructional resources.

STEM course access was measured using CRDC fields indicating whether a school offered calculus, physics, chemistry, or computer science. These variables were used to construct (1) a binary indicator equal to 1 if a school offered any advanced STEM course, and (2) a count variable reflecting the total number of distinct advanced STEM subjects available. For visualization purposes, I additionally used the raw CRDC variables to examine the prevalence of specific courses across HOLC grades, though these subject-specific measures were not used directly in regressions.

The CRDC also provided information on school-level enrollment, teacher counts, certified teacher counts, racial/ethnic composition, and charter/magnet status. Charter and magnet schools were retained but marked with indicator variables for all empirical models. Some variables, particularly total enrollment, exhibited missingness across cities; schools missing CRDC course-offering data were dropped from the analytic sample to ensure consistent measurement of the outcome.

All CRDC data were merged with CCD data using the NCESSCH unique school identifier.

### Sample Construction
After merging the HOLC, CCD, and CRDC datasets, the final national analysis sample includes only schools that:

1. Are public schools (from CCD Public School Universe),
2. Serve grades 9–12,
3. Fall inside a HOLC polygon,
4. Are located within 0.25 miles of a HOLC boundary, and
5. Have non-missing CRDC STEM course data.

For city-specific analyses, I restricted the dataset to schools within the HOLC-covered area of each city (Chicago, Los Angeles, Philadelphia, Detroit) and applied the same boundary-based 0.25-mile inclusion rule. Separate regressions were run for each city.

## Empirical Strategy
The objective of this study is to estimate whether schools located in historically lower-rated HOLC neighborhoods (Grades C and D) exhibit reduced access to advanced STEM coursework compared to schools in higher-rated neighborhoods (Grades A and B). To isolate the local, quasi-experimental variation produced by discontinuities in HOLC grading, the analysis employs a boundary discontinuity design following Aaronson, Hartley, and Mazumder (2021). This design compares schools in close geographic proximity but assigned to different HOLC grades, thereby holding constant broader spatial factors that evolve smoothly across neighborhoods.

### Boundary Discontinuity Framework
HOLC maps exhibit sharp changes in assigned credit grades at their boundaries. These historical grading breaks represent discontinuous variation in perceived mortgage risk that is plausibly exogenous to modern school-level characteristics once contemporary controls are included. To leverage this variation, I restrict the sample to schools located within 0.25 miles (402 meters) of any boundary between two different HOLC grades. This buffer is constructed around the boundary lines separating HOLC polygons.

Each boundary line segment is treated as a comparison unit. Schools are assigned to the boundary_id of the segment whose buffer they fall within. Schools also receive the HOLC grade of the polygon they physically intersect. Schools outside any HOLC polygon or farther than 0.25 miles from any boundary are excluded. This creates a two-sided local comparison sample in which schools on opposite sides of the same historical boundary line are compared.

Identification is obtained by including boundary fixed effects, which absorb all unobserved, boundary-specific characteristics—such as localized housing stock, neighborhood development patterns, and historical socioeconomic conditions. Because the buffer window is narrow, and because schools on both sides are equidistant from the same boundary, the identifying assumption is that potential outcomes would vary smoothly in the absence of historical HOLC grade differences.

### Regression Models

The primary model for the binary indicator of STEM access is a logistic regression of the form:

$$
\text{logit}(AnySTEM_i)
= \alpha + \beta \cdot Redline_i + \gamma X_i + \eta_{b(i)} + \varepsilon_i,
$$

where \(AnySTEM_i = 1\) if school *i* offers calculus, physics, chemistry, or computer science, \(Redline_i = 1\) if school *i* is located in a C or D HOLC area. \(X_i\) represents school-level controls: Title I indicator, charter school indicator, magnet school indicator, and percent certified teachers. \(\eta_{b(i)}\) denotes boundary fixed effects, ensuring that identification comes entirely from variation across schools lying on opposite sides of the same historical boundary. Standard errors are clustered at the boundary segment level, consistent with the identification design.

To examine the extensive and intensive margins of STEM access, I also estimate a negative binomial regression for the number of advanced STEM subjects offered:

$$
NB(TotalSTEM_i)
= \alpha + \beta \cdot Redline_i + \gamma X_i + \eta_{b(i)} + \varepsilon_i,
$$

where \(TotalSTEM_i\) equals the total number of distinct advanced STEM subjects offered (calculus, physics, chemistry, computer science). This model uses a negative binomial specification to account for the over-dispersed distribution of course offerings. Boundary fixed effects and the same set of controls \(X_i\) are included, mirroring the binary outcome model.

Together, these models estimate whether historically lower-rated HOLC areas exhibit lower probabilities of offering any advanced STEM course and reduced breadth in STEM offerings.

### National and City-Level Analyses

Both models are estimated on a national dataset of 1,767 schools across 113 HOLC-mapped cities that contain at least three HOLC grade types. To examine regional heterogeneity, I estimate separate regressions for Chicago, Los Angeles, Philadelphia, and Detroit. Each city-specific sample includes only schools located within that city’s HOLC-mapped area and within 0.25 miles of at least one HOLC boundary. The same model specification and boundary fixed effects are used in all analyses.

### Identification Assumptions

The key assumption is that, conditional on controls and boundary fixed effects, potential outcomes vary smoothly within the narrow spatial window around each HOLC boundary. Under this assumption, any systematic difference in STEM access across boundaries can be attributed to historical HOLC grade assignment. Because identification occurs within the same boundary segment, broader city-level and district-level differences are not sources of bias.

### Software and Implementation

Spatial operations—including coordinate reprojection, buffer construction, boundary assignment, and polygon intersections—were performed in Python using geopandas, shapely, and pandas. Regressions were estimated with statsmodels, with standard errors clustered at the boundary level.