+++ {"part": "introduction"}

## 1. Introduction and Research Question

The Federal Reserve's ability to influence consumer spending through interest rate policy rests on a critical assumption: that consumer credit responds to rate changes. This assumption is being challenged by the explosive growth of Buy Now, Pay Later (BNPL) services, which have expanded from near-zero to over USD 24.2 billion in annual transaction volume in just two years (2019-2021), according to the Consumer Financial Protection Bureau. My analysis reveals a troubling reality: this rapidly growing form of consumer credit appears completely insensitive to monetary policy interventions.

**How do BNPL firms' stock returns respond to changes in the Federal Funds Rate, after controlling for market-wide movements and macroeconomic factors?**

This question addresses a fundamental challenge to monetary policy effectiveness. BNPL firms operate differently from traditional banks: they rely on wholesale funding (warehouse credit facilities, securitization, commercial paper) rather than consumer deposits, and they operate with thin profit margins. When interest rates rise, their funding costs increase immediately, and those thin margins mean even small cost increases can eliminate profitability. The Consumer Financial Protection Bureau reports that BNPL Gross Merchandise Volume (GMV) grew from USD 2 billion in 2019 to USD 24.2 billion in 2021, while unit margins declined from 1.27% in 2020 to 1.01% in 2021—a 20% compression in a single year. This combination of extreme growth and falling margins suggests BNPL firms should be particularly vulnerable to monetary policy changes. However, my empirical analysis reveals the opposite: BNPL stock returns show zero sensitivity to Federal Reserve interest rate changes, operating outside traditional monetary policy transmission channels.

This question matters because understanding how these firms respond to monetary policy helps investors assess risk and helps policymakers understand financial stability implications. Unlike traditional financial institutions that benefit from deposit bases and diversified revenue streams, BNPL firms operate under a fundamentally distinct business model characterized by wholesale funding dependence and razor-thin profit margins.

### 1.1.1 U.S. BNPL Market Context and Growth Statistics

The U.S. BNPL market has grown rapidly: 21% of consumers with credit records used BNPL in 2022, and adoption continues expanding. However, this growth comes with risks. About 61% of BNPL borrowers have subprime credit scores, and 34-41% report late payments. Approximately 63% of BNPL borrowers originated multiple simultaneous loans in 2022, and 33% held loans across multiple BNPL providers. This customer base—financially constrained consumers with high debt burdens and loan stacking behavior—suggests BNPL firms are vulnerable to economic shocks. These patterns imply that BNPL returns should be particularly exposed to tightening cycles, since a more fragile borrower base is likely to reduce spending and default more as rates rise. When interest rates rise or consumer spending falls, these borrowers are more likely to default, directly affecting BNPL profitability and stock returns.

### 1.1.2 Klarna's IPO: Natural Experiment

The magnitude of this phenomenon is illustrated by recent market events. Klarna's IPO in September 2025 offers a concrete example of BNPL sensitivity to interest rates. The company's valuation collapsed from USD 46 billion in 2021 to USD 13-14 billion by 2025—a 70% decline that coincided precisely with the Fed's rate hikes from near-zero to 5%. This happened despite continued revenue growth, suggesting the collapse reflected investor concerns about profitability in a higher-rate environment, not operational failure.

**Important caveat:** Klarna operates under a European banking license and funds loans through consumer deposits, unlike most U.S. BNPL firms that rely on wholesale funding. This means Klarna's sensitivity profile differs from firms like Affirm or PayPal. The case study illustrates the general principle that BNPL valuations respond to interest rates, but the specific mechanisms may vary by funding structure.

This case motivates the regression analysis, but the regression is needed because Klarna alone is not enough evidence. Klarna went public at the very end of my sample period (September 2025), so its stock data cannot be directly incorporated into the regression. Moreover, Klarna's deposit-funded model differs from the wholesale-funded U.S. BNPL firms that comprise my portfolio. The regression analysis provides systematic evidence across multiple firms and time periods, complementing this illustrative case study.

## 1.2 Research Contribution

This study contributes to three distinct strands of literature: fintech firm valuation, monetary policy transmission mechanisms, and consumer credit markets research. A detailed discussion of these contributions and the specific gaps in existing research that this study addresses is provided in Section 2.6 (Literature Review).

**Fintech Valuation:** My results show that BNPL stocks exhibit high market beta (β = 2.38) but economically large though statistically insignificant sensitivity to Federal Funds Rate changes (β₁ = -12.68, p = 0.202), suggesting BNPL behaves more like growth-oriented technology stocks than rate-sensitive financial institutions, despite their structural exposure to funding costs.

**Monetary Policy Transmission:** The analysis reveals that inflation (β₄ = -12.94, p = 0.049) and market returns dominate BNPL return variation, while direct interest rate sensitivity, though economically meaningful, is statistically undetectable in monthly data. This suggests monetary policy affects BNPL firms primarily through indirect channels (market sentiment, inflation effects on consumer purchasing power) rather than direct funding cost pass-through visible in stock returns.

**Consumer Credit Markets:** The high market beta and inflation sensitivity indicate that BNPL firms' stock performance is closely tied to broader economic conditions affecting consumer spending capacity, consistent with their role serving financially constrained consumers who are particularly vulnerable to economic shocks.

## 1.3 Methodology Overview

I use a multi-factor regression framework to estimate how BNPL stock returns respond to Federal Funds Rate changes, controlling for market movements, consumer confidence, disposable income, and inflation. The base model includes only interest rate changes; the full model adds controls to isolate the direct interest rate effect.

**Base Model:** $\log(BNPL\_Return_t) = \beta_0 + \beta_1 \Delta FFR_t + \varepsilon_t$

**Full Model:** $\log(BNPL\_Return_t) = \beta_0 + \beta_1 \Delta FFR_t + \beta_2 \Delta CC_t + \beta_3 \Delta DI_t + \beta_4 \Delta \pi_t + \beta_5 R_{Market,t} + \varepsilon_t$

I use log-transformed returns (standard in financial econometrics) and robust standard errors (HC3) to handle heteroskedasticity. The sample covers February 2020 to August 2025 (67 monthly observations), capturing the Fed's transition from near-zero rates to 5%. The analysis includes three publicly-traded BNPL firms: PayPal (PYPL), Affirm (AFRM), and Sezzle (SEZL). Detailed methodology is presented in Section 4 (Data Analysis).

**Identification:** I interpret β₁ as descriptive sensitivity, not strict causal effect, because of several limitations: (1) Federal Funds Rate changes are endogenous to economic conditions that also affect BNPL returns; (2) omitted variables (firm-specific news, regulatory changes, competitive dynamics) confound the relationship; and (3) reverse causality is possible if BNPL sector performance influences monetary policy decisions (though unlikely given BNPL's small market share). The inclusion of market returns, consumer confidence, disposable income, and inflation as controls addresses omitted variable bias, but the estimates should be interpreted as conditional correlations rather than causal effects.

+++
