# California Film Tax Credits Research Project

**Author:** Peter Li  
**Course:** AS.180.369  
**Title:** An Examination of the Effect on Employment and Wages of the California Film Tax Credit Programs

---

## 📁 Project Structure

```
peetyeety/
├── final/                         ← SUBMISSION FOLDER (start here)
│   ├── README.md                  ← Instructions for reproducibility
│   ├── California_Film_Tax_Credits_Peter_Li.pdf
│   ├── html/                      ← Static website
│   ├── mystdemo/                  ← Paper source (MyST)
│   └── Data Exploration/          ← All analysis code & data
│
├── mystdemo/                      ← Original MyST project
├── Data Exploration/              ← Original analysis folder
├── Research Draft/                ← Draft materials
└── Brainstorm/                    ← Early exploration
```

---

## 🚀 Quick Start

### View the Paper
```bash
# PDF
open final/California_Film_Tax_Credits_Peter_Li.pdf

# HTML (static)
open final/html/index.html

# MyST (interactive)
cd final/mystdemo && pip install mystmd && myst start
```

---

## 🔬 Reproduce the Regressions

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
```

### 1️⃣ Difference-in-Differences (DiD)

**Location:** `final/Data Exploration/DiD/`

**Raw Data:** QCEW CSV files in `final/Data Exploration/` (2010-2025)

**Run:**
```bash
cd "final/Data Exploration/DiD"
jupyter notebook difference-in-difference-clean.ipynb
```

**Output:** `did_results_summary.csv` → Table 2 in paper

---

### 2️⃣ Synthetic Control Method (SCM)

**Location:** `final/Data Exploration/SCM/`

**Raw Data:** Same QCEW CSV files

**Run:**
```bash
cd "final/Data Exploration/SCM"
jupyter notebook scm_execution.ipynb
# OR
python run_synthetic_control.py
```

**Output:** `scm_results_summary.csv` → Table 3 in paper

---

### 3️⃣ Migration Analysis (ACS)

**Location:** `final/Data Exploration/Migration/`

**Raw Data:** ⚠️ Requires IPUMS ACS download (see below)

**Run:**
```bash
cd "final/Data Exploration/Migration"
jupyter notebook acs.ipynb
```

**Output:** `california_film_migration.png` → Figure in paper

---

### 4️⃣ Electoral Cycle Analysis

**Location:** `final/Data Exploration/Electoral Cycle/`

**Read:** `findings.md` (qualitative analysis)

---

## 📊 Results Traceability

| Paper Section | Result | Code Location | Output File |
|---------------|--------|---------------|-------------|
| Table 2 (DiD) | Wages +9.1%, p=0.003 | `DiD/difference-in-difference-clean.ipynb` | `did_results_summary.csv` |
| Table 3 (SCM) | 2015: +3.5%, p=0.286 | `SCM/scm_execution.ipynb` | `scm_results_summary.csv` |
| Table 3 (SCM) | 2020: +4.3%, p=0.143 | `SCM/scm_execution.ipynb` | `scm_results_summary.csv` |
| Table 4 | Migration +2,029/yr | `Migration/acs.ipynb` | notebook output |

---

## 📥 Data Sources

### ✅ Included in Repository
| Data | Files | Location |
|------|-------|----------|
| QCEW Employment | `2010-2025 512110*.csv` | `final/Data Exploration/` |
| State GDP | `quarterly-gdp-by-state.csv` | `final/Data Exploration/` |
| Unemployment | `unemployment-all-state-numeric.csv` | `final/Data Exploration/` |

### ⚠️ Manual Download Required

#### IPUMS ACS Microdata (for Migration Analysis)
1. Go to https://usa.ipums.org/usa/
2. Create free account
3. Select ACS samples: 2009-2023
4. Add variables: YEAR, STATEFIP, GQ, PERWT, INDNAICS, MIGPLAC1, MIGRATE1
5. Download CSV and save as `final/Data Exploration/ipums_acs_extract.csv`

#### County Market Tracker (optional)
- Source: [Redfin Data Center](https://www.redfin.com/news/data-center/)
- File: `county_market_tracker.tsv000`

---

## 📄 Paper Outputs

| Format | Location |
|--------|----------|
| **PDF** | `final/California_Film_Tax_Credits_Peter_Li.pdf` |
| **HTML** | `final/html/index.html` |
| **Source** | `final/mystdemo/` |

---

## 📚 Additional Documentation

- `final/README.md` - Submission folder instructions
- `final/mystdemo/README.md` - Detailed MyST & data documentation
- `final/Data Exploration/SCM/README.md` - SCM methodology details

---

## Contact

Peter Li - Johns Hopkins University


