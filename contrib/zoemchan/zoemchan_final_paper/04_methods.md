# Methodology

## Data Sources
This study combines historical neighborhood data with contemporary administrative records on U.S. public high schools. Historical redlining boundaries are drawn from digitized Home Owners’ Loan Corporation (HOLC) maps compiled by the Mapping Inequality Project. These maps classify neighborhoods into four categories—A (“Best”), B (“Still Desirable”), C (“Definitely Declining”), and D (“Hazardous”)—based on assessments made in the late 1930s.

Contemporary school-level data come from two primary sources. The National Center for Education Statistics (NCES) Common Core of Data (CCD) provides information on school characteristics, including grade span, charter and magnet status, and Title I participation. Data on advanced STEM course offerings are drawn from the Civil Rights Data Collection (CRDC), which reports whether high schools offer calculus, computer science, and physics, as well as counts of these courses.

School addresses from the CCD are geocoded and spatially linked to historical HOLC boundaries. All spatial processing is conducted using standard geographic information system methods to ensure consistent alignment across historical and modern datasets.

## Sample Construction
The analytic sample consists of public high schools located in cities for which digitized HOLC maps are available. To focus on schools plausibly affected by historical neighborhood classification while minimizing confounding from broader city-level differences, I restrict attention to schools located within 0.25 miles of a historical HOLC boundary. This restriction allows for comparisons between schools in close geographic proximity but assigned to different HOLC grades.

Schools are further restricted to those with complete information on advanced STEM offerings and key school characteristics. The final national sample includes 1,767 high schools across 113 cities. City-level analyses focus on Chicago, Detroit, Philadelphia, and Los Angeles, which provide sufficient within-city variation in HOLC grades and school locations near boundaries.

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