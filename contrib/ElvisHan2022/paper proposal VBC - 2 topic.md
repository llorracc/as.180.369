# Value-Based Care and Hospital Performance: HRRP vs. HVBP

## Introduction
Value-based care policies link provider payments to quality and efficiency outcomes. Two of the most prominent federal initiatives are the **Hospital Readmissions Reduction Program (HRRP)** and the **Hospital Value-Based Purchasing (HVBP) Program**. Both aim to incentivize hospitals to improve care delivery but rely on different mechanisms: HRRP uses penalties for excessive readmissions, while HVBP redistributes funds based on performance across multiple domains. This project will analyze both programs econometrically to understand their impacts on hospital behavior and patient outcomes.

---

## Case Study 1: Hospital Readmissions Reduction Program (HRRP)

### Topic & Hypothesis
I will analyze the effect of the **HRRP** on hospital readmission rates and care delivery decisions.  

**Hypothesis:** HRRP penalties incentivized hospitals to reduce readmissions for targeted conditions (heart failure, pneumonia, AMI), but may have introduced uncertainty in care quality tradeoffs, such as increased observation stays or delayed discharges.

### Design & Data
- **Data sources:** 2008–2020 hospital-level panel data from CMS Hospital Compare and Medicare claims.  
- **Econometric design:** Difference-in-differences comparing HRRP-targeted conditions (subject to penalties) vs. non-targeted conditions, pre- and post-HRRP implementation.  
- **Outcomes:**  
  - 30-day readmission rates  
  - Length of stay  
  - Observation-stay use  
  - Mortality  
- **Controls:** hospital size, teaching status, payer mix, regional demographics.  
- **Extensions:** Event-study models to capture dynamic responses over time.

### Contribution
This case study highlights how penalty-based incentives in value-based care reshape provider decisions under policy-driven uncertainty, yielding insights on both the intended and unintended consequences of performance-based payment.

---

## Case Study 2: Hospital Value-Based Purchasing Program (HVBP)

### Topic & Hypothesis
I will examine the effect of the **HVBP Program** on hospital quality and patient outcomes.  

**Hypothesis:** HVBP’s redistribution of payments based on quality, safety, efficiency, and patient experience modestly improves outcomes, but the small size of incentives and resource disparities may limit effects, particularly for safety-net and rural hospitals.

### Design & Data
- **Data sources:** 2008–2020 CMS Hospital Compare (mortality, safety indicators, HCAHPS), Medicare claims, AHA Annual Survey.  
- **Econometric design:** Difference-in-differences comparing Medicare hospitals subject to HVBP with exempt hospitals (e.g., critical access hospitals), before and after program implementation.  
- **Outcomes:**  
  - Mortality rates  
  - Safety indicators (infections, falls)  
  - Patient satisfaction (HCAHPS)  
  - Spending efficiency  
- **Controls:** hospital size, teaching status, payer mix, baseline quality performance, local demographics.  
- **Extensions:** Event-study to examine dynamic effects; quantile regression to explore heterogeneity across high- vs. low-performing hospitals.

### Contribution
This case study evaluates whether HVBP’s financial incentives drive sustained improvements in care quality or primarily redistribute funds. Findings will inform debates about fairness, sustainability, and the design of future performance-linked incentive programs.

---

## Comparative Contribution
By analyzing **HRRP (penalty-driven, condition-specific)** and **HVBP (reward/redistribution, multidomain)** side by side, this project will provide a broader understanding of performance-linked incentives in value-based care. The comparative framework allows for assessing:
- Whether penalties or rewards more effectively change provider behavior.  
- How unintended consequences differ across program designs.  
- Which hospital types benefit or are disadvantaged under each model.  

The results will generate evidence to guide the refinement of future value-based care initiatives, balancing cost control, quality improvement, and equity.
