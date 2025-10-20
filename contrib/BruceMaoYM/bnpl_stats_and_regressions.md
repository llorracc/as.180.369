
# 📊 BNPL Statistics & Regression Framework  
*(Synthesized from CFPB Reports 2022–2025)*

## **1. Core Data Sources**

| Source | Title | Year | Key Variables |
|--------|-------|------|---------------|
| CFPB (2022) | *Buy Now, Pay Later: Market Trends and Consumer Impacts* | 2022 | Loan growth, charge-off rates, late fees, GMV, industry mix |
| CFPB (2023) | *Consumer Use of Buy Now, Pay Later* | 2023 | Demographics, credit utilization, debt levels, delinquencies |
| CFPB (2025) | *Consumer Use of Buy Now, Pay Later and Other Unsecured Debt* | 2025 | Comprehensive matched dataset, loan stacking, debt burden analysis |
| External | FRED, BLS | 2019-2022 | Macroeconomic controls (inflation, unemployment) |

## **2. Market Evolution & Scale (2019-2022)**

### **Growth Metrics**
| Metric | 2019 | 2020 | 2021 | 2022 | Growth |
|--------|------|------|------|------|--------|
| Daily Applications | ~100K | — | — | >1M | **10x+** |
| Approval Rate | 56% | 67% | 78% | 79% | **+23 p.p.** |
| Consumer Adoption | — | — | 17.6% | 21.2% | **+3.6 p.p.** |
| Heavy Users (% of borrowers) | — | — | 18% | 20% | **+2 p.p.** |
| Avg Annual Originations per Borrower | — | — | 8.5 | 9.5 | **+12%** |
| BNPL Loans (Five major lenders) | 16.8M | 90M | 180M | — | ↑ 970% growth |
| Dollar Volume (GMV) | $2B | $8.3B | $24.2B | $33.8B | ↑ 1,592% |
| Avg Order Value | $121 | $135 | $141 | $142 | CPI adjusted |
| Late Fee Incidence | 7.8% | 10.5% | — | — | ↑ 35% |
| Charge-off Rate | 2.9% | 3.8% | — | — | ↑ 31% |

### **2022 Market Scale (Scaled from 16% Sample)**
| Metric | Raw Sample | Scaled Aggregate |
|--------|------------|------------------|
| Loan Applications | 66.1M | 401.9M |
| Originated Loans | 45.6M | 277.3M |
| Gross Merchandise Value | $5.6B | $33.8B |
| % of Credit Card Spending | — | ~1% |

## **3. Consumer Demographics & Risk Profile**

### **Credit Score Distribution (2021-2022)**
| FICO Score Category | Share of Originations | Default Rate | Approval Rate (2022) |
|---------------------|----------------------|--------------|---------------------|
| No Score | 3.9% | 4.1% | 62% |
| Deep Subprime (300-579) | 45.0% | 3.5% | 78% |
| Subprime (580-619) | 16.0% | 1.1% | 78% |
| Near Prime (620-659) | 12.7% | 0.8% | — |
| Prime (660-719) | 13.2% | 0.7% | — |
| Super Prime (720-850) | 9.1% | 0.8% | — |

### **Age-Based Analysis (2022)**
| Age Group | BNPL Adoption | Avg Unsecured Debt | BNPL Share of Debt | Credit Utilization |
|-----------|---------------|-------------------|-------------------|-------------------|
| 18-24 | 37.1% | $9,068 | 27.9% | 70%+ |
| 25-33 | 33.6% | $20,486 | 16.6% | 65%+ |
| 34-40 | 28.7% | $25,425 | 16.0% | 60%+ |
| 41-50 | 19.1% | $28,991 | 14.1% | 55%+ |
| 51-64 | 9.9% | $26,453 | 14.2% | 50%+ |
| 65+ | 5.9% | $17,352 | 15.5% | 45%+ |

**Key Insights:**
- **61% of originations** go to subprime/deep subprime borrowers
- **Young consumers (18-24)** are 2x more likely to use BNPL
- **BNPL represents 28%** of total unsecured debt for 18-24 age group when borrowing

## **4. Loan Stacking & Usage Patterns**

### **Simultaneous Borrowing (2021-2022)**
| Metric | 2021 | 2022 | Notes |
|--------|------|------|-------|
| Simultaneous loans (any firm) | 62.8% | 62.7% | **63% average** |
| Cross-firm simultaneous loans | 31.7% | 32.6% | **33% average** |
| Avg days between originations | 42.4 | 44.8 | Slight increase |
| Median days between originations | 27.5 | 29.3 | **~2 weeks typical** |

### **Heavy vs. Occasional Users (2022)**
| User Type | Share | Median Originations | Median Days Between | Daily Active Loans |
|-----------|-------|-------------------|-------------------|-------------------|
| Heavy Users (>12 loans/year) | 20.3% | 23 | 13.6 | 2.6 |
| Occasional Users (1-12 loans) | 79.7% | 2 | 41.4 | 0.3 |

### **Default Rates Comparison**
| Age Group | BNPL Default Rate | Credit Card Default Rate (BNPL borrowers) |
|-----------|------------------|------------------------------------------|
| 18-24 | 2.9% | 7.3% |
| 25-33 | 2.4% | 10.4% |
| 34-40 | 1.9% | 11.7% |
| 41-50 | 1.5% | 11.0% |
| 51-64 | 1.5% | 8.7% |
| 65+ | 1.4% | 6.3% |
| **Overall** | **2.1%** | **10.1%** |

**Key Insights:**
- **BNPL default rates (2%)** significantly lower than credit cards (10%) for same population
- **Automatic repayment** requirement explains low BNPL default rates
- **Holiday season** drives simultaneous loan stacking

## **5. Financial Stress & Debt Burden Analysis**

### **Conditional Correlations (2020-2022)**
*Controlling for age, credit score, seasonal effects*
| Debt Type | Additional Amount Held by BNPL Users | % of Mean | Statistical Significance |
|-----------|---------------------------------------|-----------|------------------------|
| Credit Card Balances | +$871 | +18.1% | *** (99% confidence) |
| Student Loans | +$5,734 | +36.3% | *** (99% confidence) |
| Personal Loans | +$453 | +21.6% | *** (99% confidence) |
| Retail Loans | +$292 | +36.9% | *** (99% confidence) |
| Payday Loans | +$0.37 | +55.9% | *** (99% confidence) |
| Other AFS | +$29 | +58.6% | *** (99% confidence) |

### **Unsecured Debt by User Type (2022)**
| Debt Type | Heavy BNPL Users | Occasional BNPL Users | Non-BNPL Users |
|-----------|-------------------|----------------------|-----------------|
| Student Loans | $16,800 | $13,200 | $8,400 |
| Credit Cards | $4,800 | $4,600 | $4,600 |
| Personal Loans | $2,100 | $1,600 | $800 |
| Retail Loans | $1,200 | $900 | $600 |
| Other AFS | $200 | $100 | $50 |
| **Total Unsecured Debt** | **$25,100** | **$20,500** | **$14,450** |

### **Credit Utilization Patterns**
- **BNPL borrowers**: 60-66% average utilization vs. **Non-BNPL**: 34% average
- **Utilization rates increase** in the year before first BNPL use
- **Median BNPL borrower**: 70% credit card utilization
- **Financial stress indicator**: Utilization rates >30% may negatively impact credit scores

## **6. Regression Models Framework**

### **Model 1: Determinants of BNPL Use**
*Binary logistic regression to identify factors predicting BNPL adoption*

$$\begin{align}
\text{BNPL}_i &= \alpha + \beta_1 \text{CreditScore}_i + \beta_2 \text{IncomeGroup}_i \\
&\quad + \beta_3 \text{DebtToIncome}_i + \beta_4 \text{AgeGroup}_i + \beta_5 \text{Race}_i + \epsilon_i
\end{align}$$

### **Model 2: Credit Risk Impact of BNPL Usage**
*Linear regression examining BNPL's effect on delinquency rates*

$$\begin{align}
\text{DelinqRate}_i &= \alpha + \beta_1 \text{BNPLUse}_i + \beta_2 \text{CreditScore}_i \\
&\quad + \beta_3 \text{Utilization}_i + \beta_4 \text{Income}_i + u_i
\end{align}$$

### **Model 3: Financial Fragility Analysis**
*Linear regression modeling liquidity constraints*

$$\begin{align}
\text{Liquidity}_i &= \alpha + \beta_1 \text{BNPLUse}_i + \beta_2 \text{IncomeVolatility}_i \\
&\quad + \beta_3 \text{DebtLoad}_i + \epsilon_i
\end{align}$$

### **Model 4: Cross-Firm Loan Stacking**
*Analysis of simultaneous loans across multiple BNPL providers*

$$\begin{align}
\text{CrossFirmStacking}_i &= \alpha + \beta_1 \text{BNPLFrequency}_i + \beta_2 \text{CreditScore}_i \\
&\quad + \beta_3 \text{HolidaySeason}_t + \beta_4 \text{AgeGroup}_i + \epsilon_i
\end{align}$$

### **Model 5: Credit Utilization Dynamics**
*Panel regression on credit card utilization before/after first BNPL use*

$$\begin{align}
\text{CreditUtilization}_{i,t} &= \alpha + \beta_1 \text{MonthsToFirstBNPL}_i + \beta_2 \text{PostBNPL}_i \\
&\quad + \beta_3 \text{CreditScore}_i + \beta_4 \text{AgeGroup}_i + \gamma_t + \epsilon_{i,t}
\end{align}$$

### **Model 6: Heavy vs. Occasional User Analysis**
*Logistic regression distinguishing heavy users (>12 loans/year) from occasional users*

$$\begin{align}
\text{HeavyUser}_i &= \alpha + \beta_1 \text{CreditScore}_i + \beta_2 \text{AgeGroup}_i + \beta_3 \text{StudentLoanBalance}_i \\
&\quad + \beta_4 \text{CreditCardUtilization}_i + \beta_5 \text{PersonalLoanBalance}_i + \epsilon_i
\end{align}$$

## **7. Data Methodology & Sample Design**

### **CFPB Data Collection (2025 Report)**
- **Sample Design**: 16% random sample based on day of birth from 6 major BNPL firms
- **Firms Included**: Affirm, Afterpay, Klarna, PayPal, Sezzle, Zip
- **Time Period**: 2017-2022 (firms began lending 2017-2020)
- **Total Applications**: ~145 million BNPL applications
- **Matched Dataset**: Consumer Credit Information Panel (CCIP) with credit records

### **Sample Characteristics**
- **520,000 consumers** per year in matched sample
- **Age Range**: 18-70 (born 1953-2006)
- **2% match rate** between BNPL data and credit records
- **Representative** of U.S. adults with credit records
- **Probabilistic matching** used to link de-identified BNPL loans to credit records

### **Variable Categories for Analysis**
| Category | Example Metrics | Source |
|----------|----------------|---------|
| BNPL Market Structure | GMV growth, merchant mix, charge-off rate | CFPB 2022, 2025 |
| Borrower Risk Profile | Credit score, utilization, debt-to-income | CFPB 2023, 2025 |
| Financial Health Controls | Well-being index, income variability, liquidity | CFPB 2022, 2025 |
| Outcome Variables | Late fee %, charge-off rate, default incidence | CFPB 2022, 2025 |
| Demographic Covariates | Race, gender, income group, age | CFPB 2023, 2025 |
| Macro Controls | Inflation, unemployment | FRED, BLS |

## **8. Policy Implications & Regulatory Concerns**

### **Credit Reporting Gap**
- **Hidden Debt Problem**: $33.8B in BNPL obligations not visible to other lenders
- **Cross-Firm Blind Spots**: 33% of borrowers use multiple providers simultaneously
- **Underwriting Challenges**: Other creditors can't see BNPL obligations when making lending decisions
- **Regulatory Arbitrage**: BNPL operates outside traditional credit reporting framework

### **Consumer Protection Issues**
- **Heavy Users**: 20% of borrowers, median 23 loans/year, 2.6 active loans daily
- **Subprime Concentration**: 61% of originations to subprime/deep subprime borrowers
- **Age Vulnerability**: 18-24 year olds most at risk, BNPL represents 28% of debt when borrowing
- **Financial Stress Indicators**: BNPL users hold $871-$5,734 MORE in other unsecured debt

### **Market Structure Concerns**
- **Counteroffers**: 8 p.p. increase in approval rates (2020 vs. 2022)
- **High Approval Rates**: 78% for subprime/deep subprime borrowers
- **Seasonal Risk**: Holiday season drives simultaneous loan stacking
- **Automatic Repayment**: Required by most BNPL firms (explains low 2% default rate)

## **9. Visualization & Analysis Framework**

### **Recommended Visualizations**
| Chart Type | Variables | Purpose |
|-------------|-----------|----------|
| Time Series | GMV, Loan Count, Charge-off rates | Growth & risk evolution |
| Histogram | Credit Score by BNPL status | Distributional differences |
| Boxplot | Liquidity levels vs BNPL use | Fragility comparison |
| Scatter | Approval Rate vs Late Fee % | Moral hazard visualization |
| Regression Coeff. Plot | Key β estimates | Visual clarity of determinants |
| Heatmap | Age × Credit Score × BNPL adoption | Multi-dimensional risk profiling |

### **Methodological Opportunities**
- **Natural Experiments**: Merchant partnerships, geographic variation in BNPL availability
- **Panel Data Analysis**: Track same consumers before/after first BNPL use
- **Instrumental Variables**: Use merchant-specific BNPL rollouts as exogenous variation
- **Difference-in-Differences**: Compare outcomes across regions with different BNPL penetration
- **Event Studies**: Analyze credit utilization patterns around first BNPL use

## **10. Summary & Research Framework**

### **Key Empirical Findings**
1. **Market Explosion**: 10x growth in applications (2019-2022), 79% approval rates
2. **Consumer Profile**: 21% adoption rate, 20% heavy users, 61% subprime concentration
3. **Financial Patterns**: BNPL users hold significantly more unsecured debt across all categories
4. **Age Effects**: 18-24 year olds most vulnerable, BNPL represents 28% of debt when borrowing
5. **Credit Dynamics**: Utilization rates increase before first BNPL use, suggesting credit stress

### **Regression Models (6 Total)**
- **Model 1**: Determinants of BNPL Use (logistic regression)
- **Model 2**: Credit Risk Impact of BNPL Usage (linear regression)
- **Model 3**: Financial Fragility Analysis (liquidity constraints)
- **Model 4**: Cross-Firm Loan Stacking (simultaneous borrowing)
- **Model 5**: Credit Utilization Dynamics (panel regression)
- **Model 6**: Heavy vs. Occasional User Analysis (logistic regression)

### **Data Integration**
- **CFPB 2022 Report**: Market trends, industry structure, aggregate statistics
- **CFPB 2023 Report**: Consumer demographics, credit utilization patterns  
- **CFPB 2025 Report**: Comprehensive matched dataset, loan stacking, debt burden analysis
- **External Data**: FRED, BLS for macroeconomic controls

### **Policy Implications**
- **Credit reporting gap**: $33.8B in "hidden debt" not visible to other lenders
- **Consumer protection**: Heavy users and young borrowers at highest risk
- **Regulatory arbitrage**: BNPL operates outside traditional credit reporting framework
- **Market structure**: Counteroffers and automatic repayment create unique risk profiles

This comprehensive framework provides the foundation for rigorous empirical analysis of BNPL's impact on consumer financial health and market dynamics.
