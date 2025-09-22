# Research Project: HRRP, Observation Substitution, and Patient Welfare

---

## Research Question
**To what extent did hospitals’ substitution of inpatient readmissions into observation stays under the HRRP increase Medicare beneficiaries’ financial and welfare burdens, measured through out-of-pocket (OOP) spending, skilled nursing facility (SNF) access, and mortality?**

---

## Abstract
The Hospital Readmissions Reduction Program (HRRP) penalizes hospitals with excess 30-day readmissions for selected conditions. While the policy modestly reduced readmissions, hospitals often substituted these returns into observation stays. Because observation is billed under Medicare Part B, beneficiaries face higher out-of-pocket costs, itemized billing, and ineligibility for skilled nursing facility (SNF) coverage under the “three-day rule.” This study places observation stays at the center of HRRP evaluation by constructing an **Observation Substitution Index (OSI)** — a hospital-level measure of the extent to which decreases in inpatient readmissions were offset by increases in observation stays. Using Medicare claims data from 2008–2020, I estimate the association between hospitals’ substitution intensity (OSI) and patient-level financial and welfare outcomes. Outcomes include 30-day OOP spending, probability of covered SNF admission, and 30-/90-day mortality. Event-study analyses will assess dynamics of substitution pre- and post-HRRP. By quantifying the financial damages and access losses imposed on patients, this project reframes HRRP’s legacy from provider efficiency to patient welfare, offering evidence for reforms such as including observation stays in quality metrics or revising SNF eligibility rules.

---

## Introduction & Literature Review

### Policy Context
The HRRP, enacted under the Affordable Care Act, was designed to improve care coordination by penalizing hospitals with higher-than-expected 30-day readmissions. Starting in fiscal year 2013, hospitals could lose up to 3% of Medicare reimbursements. Targeted conditions included heart failure, acute myocardial infarction (AMI), and pneumonia, later expanded to COPD and elective joint replacements.

### What We Know
- **Effectiveness:** Studies show 30-day readmissions for targeted conditions declined by ~9%, less than the projected 25%.  
- **Substitution:** Evidence consistently documents increases in observation stays and ED visits post-HRRP (Zuckerman et al., 2016; Gupta et al., 2018).  
- **Unintended Consequences:** Patients in observation face higher OOP spending (Part B coinsurance), ineligibility for SNF under the three-day inpatient rule, and fragmented follow-up care.  
- **Debate:** Some analyses suggest HRRP contributed to higher mortality for heart failure and AMI patients (Khera et al., 2018), while others attribute this to coding artifacts.  

### Research Gap
Although substitution into observation stays is well documented, **few studies have quantified the resulting patient-level financial and welfare harms.** Most work focuses on system-level readmission rates rather than the patient’s lived burden. This study addresses that gap by measuring the dollar and access costs of substitution.

---

## Conceptual Flow

HRRP penalties (2013)  
        ↓  
Hospitals pressured to reduce readmissions  
        ↓  
Substitution into observation stays ↑  
        ↓  
Damages to patients:  
- Higher OOP costs (Medicare Part B billing)  
- Lost SNF eligibility (3-day inpatient rule)  
- Potential adverse outcomes (mortality, ED churn)  

---

## Hypothesis
1. **Observation Substitution:** Hospitals with higher OSI values will show greater post-HRRP increases in OOP spending for patients.  
2. **SNF Access:** High-OSI hospitals will see a larger decline in the probability of covered SNF admissions.  
3. **Mortality:** Patients discharged from high-OSI hospitals may have elevated 30-/90-day mortality rates compared to those at low-OSI hospitals.  

---

## Methodology

### Observation Substitution Index (OSI)
$$
OSI_h = \frac{\Delta \text{Observation}_h}{\lvert \Delta \text{Readmission}_h \rvert}
$$

- Calculated for each hospital as the ratio of the change in observation stays to the change in readmissions (per 100 discharges), pre- vs. post-HRRP.
- Interpreted as the intensity of substitution:
  - **OSI ≈ 0:** True reductions in readmissions (little substitution).
  - **OSI ≈ 1:** Nearly one-for-one substitution.
  - **OSI > 1:** Observation growth exceeds readmission decline.

### Empirical Strategy
- **Descriptive:** Plot pre/post trends in readmissions, observation, OOP, SNF access, and mortality by OSI quartile.  
- **Regression Framework:**

$$
Y_{iht} = \alpha + \beta \,(Post_t \times HighOSI_h) + \gamma X_{iht} + \mu_h + \lambda_t + \epsilon_{iht}
$$

Where:

- $Y_{iht}$: patient outcomes (e.g., OOP spending, SNF access, mortality).  
- $Post_t$: post-HRRP period indicator.  
- $HighOSI_h$: indicator for hospital in top quartile of the Observation Substitution Index.  
- $X_{iht}$: patient-level controls (age, sex, comorbidities, dual-eligibility).  
- $\mu_h$: hospital fixed effects.  
- $\lambda_t$: year fixed effects.  
- $\epsilon_{iht}$: error term.


- **Event Study:** Estimate year-specific effects for high- vs. low-OSI hospitals to validate pre-trends and trace dynamics.

---

## Data Preparation

### Data Sources
- **Medicare Claims (2008–2020):**
  - MedPAR (inpatient stays, readmissions).
  - Outpatient (observation stays, ED visits).
  - Carrier/Part B (OOP liabilities).
  - SNF claims (admissions and coverage status).
  - Master Beneficiary Summary File (MBSF: demographics, comorbidities, dual-eligibility).  
- **Hospital Characteristics:** AHA Annual Survey, CMS HRRP penalty files.  
- **Geographic Controls:** Area Deprivation Index (ADI), ZIP-level median income.

### Key Variables
- **Exposure:** Observation Substitution Index (OSI).  
- **Outcomes:**  
  - OOP spending (30 days post-discharge).  
  - SNF access and coverage.  
  - Mortality (30-/90-day).  
- **Controls:** Age, sex, comorbidities, dual-eligible status, hospital size, teaching status, safety-net indicator.

---

## Expected Contribution
By centering observation stays in the evaluation of HRRP, this study will produce the first national estimate of the **financial and access harms borne by patients** due to substitution. Results will directly inform CMS reforms such as including observation in readmission metrics and revising the 3-day SNF eligibility rule.
