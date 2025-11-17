+++ {"part": "introduction"}

## 1. Introduction and Research Question

**How do BNPL firms' stock returns respond to changes in the Federal Funds Rate, after controlling for market-wide movements and macroeconomic factors?**

This is the question this paper answers. BNPL firms operate differently from traditional banks: they rely on wholesale funding (warehouse credit facilities, securitization, commercial paper) rather than consumer deposits, and they operate with thin profit margins. When interest rates rise, their funding costs increase immediately, and those thin margins mean even small cost increases can eliminate profitability. The Consumer Financial Protection Bureau reports that BNPL unit margins declined from 1.27% in 2020 to 1.01% in 2021—a 20% compression in a single year. This suggests BNPL firms should be sensitive to interest rate changes, but we don't have quantitative evidence on how their stock returns actually respond.

This question matters because BNPL has grown rapidly (from USD 2 billion in GMV in 2019 to USD 24.2 billion in 2021), and understanding how these firms respond to monetary policy helps investors assess risk and helps policymakers understand financial stability implications. Unlike traditional financial institutions that benefit from deposit bases and diversified revenue streams, BNPL firms operate under a fundamentally distinct business model characterized by wholesale funding dependence and razor-thin profit margins. This structural difference suggests they may exhibit different sensitivity to interest rate changes compared to traditional financial stocks.

### 1.1 Market Context

The U.S. BNPL market has grown rapidly: 21% of consumers with credit records used BNPL in 2022, and adoption continues expanding. However, this growth comes with risks. About 61% of BNPL borrowers have subprime credit scores, and 34-41% report late payments. This customer base—financially constrained consumers with high debt burdens—suggests BNPL firms are vulnerable to economic shocks. When interest rates rise or consumer spending falls, these borrowers are more likely to default, directly affecting BNPL profitability.

### 1.2 Klarna Case Study: A Preview

Klarna's IPO in September 2025 offers a concrete example of BNPL sensitivity to interest rates. The company's valuation collapsed from USD 46 billion in 2021 to USD 13-14 billion by 2025—a 70% decline that coincided precisely with the Fed's rate hikes from near-zero to 5%. This happened despite continued revenue growth, suggesting the collapse reflected investor concerns about profitability in a higher-rate environment, not operational failure.

**Important caveat:** Klarna operates under a European banking license and funds loans through consumer deposits, unlike most U.S. BNPL firms that rely on wholesale funding. This means Klarna's sensitivity profile differs from firms like Affirm or PayPal. The case study illustrates the general principle that BNPL valuations respond to interest rates, but the specific mechanisms may vary by funding structure.


## 1.2 Research Contribution

This study contributes to three areas: fintech valuation (quantifying BNPL stock sensitivity to rates), monetary policy transmission (how unconventional credit providers respond to policy), and consumer credit markets (understanding BNPL's role in credit access). A detailed discussion of these contributions and the gaps this study fills is provided in Section 2.6 (Literature Review).

## 1.3 Methodology Overview

I use a multi-factor regression framework to estimate how BNPL stock returns respond to Federal Funds Rate changes, controlling for market movements, consumer confidence, disposable income, and inflation. The base model includes only interest rate changes; the full model adds controls to isolate the direct interest rate effect.

**Base Model:** $\log(BNPL\_Return_t) = \beta_0 + \beta_1 \Delta FFR_t + \varepsilon_t$

**Full Model:** $\log(BNPL\_Return_t) = \beta_0 + \beta_1 \Delta FFR_t + \beta_2 \Delta CC_t + \beta_3 \Delta DI_t + \beta_4 \Delta \pi_t + \beta_5 R_{Market,t} + \varepsilon_t$

I use log-transformed returns (standard in financial econometrics) and robust standard errors (HC3) to handle heteroskedasticity. The sample covers February 2020 to August 2025 (67 monthly observations), capturing the Fed's transition from near-zero rates to 5%. The analysis includes three publicly-traded BNPL firms: PayPal (PYPL), Affirm (AFRM), and Sezzle (SEZL). Detailed methodology is presented in Section 3 (Data and Methodology).

+++
