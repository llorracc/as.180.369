+++ {"part": "limitations"}

## 7. Limitations

This study faces several important limitations that affect the interpretation of results and should be considered when evaluating the findings. These limitations stem from data availability, identification challenges, and methodological constraints inherent in analyzing a relatively new sector with limited historical data.

### 7.1 Sample Size Constraints

Our analysis uses 67 monthly observations spanning February 2020 to August 2025. This limited sample size creates several challenges:

**Statistical Power:** With only 67 observations and multiple regressors (5-6 variables in the full specification), statistical power is substantially reduced. This makes it difficult to detect effects that may be economically meaningful but statistically weak. The wide confidence intervals around our coefficient estimates (e.g., the 95% confidence interval for the interest rate coefficient ranges from -32.4 to 7.0) reflect this limited power. As a result, we cannot confidently reject the null hypothesis of no relationship even if a meaningful economic relationship exists.

**Coefficient Stability:** Small sample sizes lead to unstable coefficient estimates that are sensitive to individual observations. Outliers or unusual periods can substantially affect point estimates, making it difficult to distinguish signal from noise. We address this concern by using robust standard errors (HC3) and conducting outlier analysis, but the fundamental limitation remains.

**Future Research:** Future research should use higher-frequency data (weekly or daily) or event-study approaches around FOMC announcements to substantially increase sample size. Weekly data would provide approximately 260 observations over the same period, dramatically improving statistical power. Event studies focusing on FOMC announcement days could provide cleaner identification with narrower windows around policy changes.

### 7.2 Shock Identification Limitations

**Crude Shock Measure:** We use month-over-month changes in the Federal Funds Rate ($\Delta FFR$) as our primary measure of monetary policy changes. This measure has significant limitations:

- **Endogeneity:** $\Delta FFR$ captures both exogenous policy shocks and endogenous responses to economic conditions. The Federal Reserve adjusts rates in response to inflation, unemployment, and other economic indicators that also affect BNPL firms, creating potential omitted variable bias.

- **Not a Clean Shock:** Modern monetary policy research uses high-frequency identification around FOMC announcements (Gürkaynak, Sack, and Swanson 2005), narrative shocks (Romer and Romer 2004), or term structure movements to isolate exogenous policy changes. Our monthly $\Delta FFR$ measure does not provide this clean identification.

- **Measurement Error:** Monthly aggregation may miss important intra-month variation in policy expectations and market responses.

**Alternative Approaches:** Ideally, we would use:
- High-frequency event studies around FOMC announcements (30-minute windows)
- 2-year Treasury yield changes (better capture policy expectations)
- Narrative shocks or Jarociński-Karadi identification
- Shadow rates (Wu-Xia) for periods near the zero lower bound

As a robustness check, we examine specifications using 2-year Treasury yield changes, which better capture policy expectations, but acknowledge that this still does not provide the clean identification available from high-frequency event studies.

### 7.3 Dependent Variable Construction

**Portfolio Approach Limitations:** Our primary analysis uses an equally-weighted average of BNPL firm returns (PYPL, AFRM, SEZL). This approach has several limitations:

- **Equal Weighting:** Assumes equal BNPL exposure across firms, ignoring substantial differences in market capitalization. PayPal (PYPL) is a diversified payments company where BNPL represents only a portion of operations, while Affirm (AFRM) and Sezzle (SEZL) are pure-play BNPL providers.

- **Heterogeneity Masking:** The portfolio approach masks important firm-level heterogeneity. Different firms have different funding structures (e.g., Klarna's deposit-based model vs. Affirm's wholesale funding), business models, and regulatory environments that may affect interest rate sensitivity differently.

- **Limited Firm Coverage:** Our sample includes only three publicly-traded BNPL firms, which may not represent the broader BNPL sector. Private firms (e.g., Klarna before its IPO, Afterpay before acquisition) and international firms may exhibit different sensitivity patterns.

**Alternative Approaches:** Future research should:
- Use firm-level panel regressions with firm fixed effects
- Construct value-weighted portfolios based on market capitalization
- Extract common BNPL factors using principal component analysis
- Conduct separate analyses for pure-play vs. diversified BNPL firms

### 7.4 Missing Factor Controls

**Standard Asset Pricing Factors:** Our model does not include standard asset pricing factors that are essential in finance research:

- **Fama-French Factors:** Missing market excess return (MKT-RF), size factor (SMB), value factor (HML), and momentum factor (MOM). These factors are standard in asset pricing models and their omission may bias our estimates.

- **Volatility Measures:** Missing VIX (volatility index), which captures risk sentiment and is particularly relevant for growth stocks like BNPL firms.

- **Sector Controls:** Missing fintech sector ETFs (FINX, IPAY) that would control for sector-wide movements unrelated to monetary policy.

**Impact:** The omission of these factors creates potential omitted variable bias. If BNPL returns are correlated with these factors (which is likely), and these factors are correlated with interest rate changes, our interest rate coefficient may be biased. The high market beta we estimate ($\beta_5 = 2.38$) suggests that systematic risk factors are important, making their explicit inclusion crucial for proper identification.

**Future Research:** Should include Fama-French factors, VIX, and sector controls to ensure that interest rate sensitivity is not confounded with other systematic risk factors.

### 7.5 Diagnostic Limitations

**Insufficient Reporting:** While we mention conducting diagnostic tests (VIF, outliers, HC3 standard errors), we do not report comprehensive diagnostic results:

- **Multicollinearity:** Correlation matrices and VIF tables are not reported, making it difficult to assess whether multicollinearity affects our estimates.

- **Serial Correlation:** Durbin-Watson, Breusch-Godfrey, and Ljung-Box tests are not reported. If serial correlation exists, we should use HAC standard errors (Newey-West) rather than HC3.

- **Stationarity:** Augmented Dickey-Fuller tests are not reported. If variables are non-stationary, we may need to use first differences or cointegration tests.

- **Residual Diagnostics:** QQ-plots, residual plots, and normality tests are not reported, making it difficult to assess whether regression assumptions are satisfied.

**Future Research:** Should report comprehensive diagnostic tables including all standard time series and cross-sectional diagnostic tests.

### 7.6 Generalizability Concerns

**Sector Representativeness:** Our sample includes only publicly-traded U.S. BNPL firms. This limits generalizability to:

- Private BNPL firms that may have different funding structures and business models
- International BNPL firms operating under different regulatory environments
- Smaller BNPL providers not included in our sample

**Time Period Specificity:** Our sample period (February 2020 to August 2025) includes:
- The COVID-19 pandemic period with unique economic conditions
- A dramatic monetary policy transition from near-zero to ~5% rates
- Rapid BNPL industry growth and maturation

These unique conditions may limit generalizability to other periods or economic environments.

**Regulatory Environment:** The sample period includes significant regulatory changes (e.g., CFPB's May 2024 ruling classifying BNPL as credit cards) that may affect relationships. Results may not generalize to periods with different regulatory frameworks.

### 7.7 Causal Interpretation Limitations

**Observational Data:** Our analysis uses observational data rather than experimental data, making causal inference challenging:

- **Omitted Variable Bias:** Despite controlling for multiple factors, unobserved variables may affect both BNPL returns and interest rates, biasing our estimates.

- **Reverse Causality:** While unlikely, it is theoretically possible that BNPL firm performance affects monetary policy (e.g., if BNPL defaults create financial stability concerns that influence Fed decisions).

- **Measurement Error:** Measurement error in our variables (particularly macroeconomic aggregates) may bias estimates toward zero.

**Correlation vs. Causation:** Our results should be interpreted as correlations rather than causal effects. While we control for many confounding factors and use monthly data to focus on short-term relationships, we cannot definitively establish causality from our regression results alone.

**Future Research:** Should employ alternative identification strategies such as:
- Instrumental variables approaches
- Natural experiments
- Event studies around FOMC announcements
- Difference-in-differences designs comparing BNPL firms to control groups

### 7.8 Factor Model Specification

**Appropriate Factor Model:** The appropriate factor model for fintech firms remains an open question. While we include standard macroeconomic variables, fintech-specific factors may be important:

- Technology sector returns
- Regulatory news and policy changes
- Fintech-specific sentiment indices
- Cryptocurrency market movements (for some fintech firms)

The omission of these factors may limit our ability to fully explain BNPL return variation and may bias our interest rate coefficient if these factors are correlated with monetary policy.

### 7.9 Interpretation of Statistically Insignificant Results

**Statistical vs. Economic Significance:** Our primary finding—that the interest rate coefficient is economically large ($\beta_1 = -12.68$) but statistically insignificant (p-value = 0.202)—requires careful interpretation:

- **Not Evidence of No Effect:** Statistical insignificance does not imply that no relationship exists. The wide confidence interval (-32.4 to 7.0) includes economically meaningful negative values, suggesting that a meaningful relationship may exist but cannot be detected with current statistical power.

- **Sample Size Constraint:** The lack of statistical significance likely reflects limited sample size rather than absence of an economic relationship. Firm-level evidence (e.g., Affirm's 394% increase in funding costs) provides microeconomic support for the macroeconomic relationship suggested by our point estimate.

- **Appropriate Language:** We frame results as "economically large but statistically indistinguishable from zero" rather than claiming statistical significance. This language appropriately reflects the uncertainty inherent in our estimates while acknowledging the economic magnitude suggested by the point estimate.

### 7.10 Conclusion on Limitations

Despite these limitations, our analysis provides valuable descriptive evidence on BNPL firms' sensitivity to monetary policy changes. The limitations primarily stem from:
1. The relatively recent emergence of publicly-traded BNPL firms (limiting historical data)
2. The challenges of identifying clean monetary policy shocks in observational data
3. The inherent difficulty of predicting stock returns, which are driven by many unobserved factors

These limitations do not invalidate our analysis but require that results be interpreted with appropriate caution. Our findings should be viewed as exploratory/descriptive rather than definitive causal evidence. The analysis establishes a foundation for future research with improved identification strategies, larger samples, and more comprehensive factor models.

Future research addressing these limitations will be able to provide more definitive evidence on the relationship between monetary policy and BNPL firm performance, contributing to understanding of how monetary policy affects fintech firms and the broader financial system.

+++

