# California Film Tax Credits - Final Submission

**Author:** Peter Li  
**Course:** AS.180.369  
**Title:** An Examination of the Effect on Employment and Wages of the California Film Tax Credit Programs

---

## 📁 Folder Contents

| Folder/File | Description |
|-------------|-------------|
| `California_Film_Tax_Credits_Peter_Li.pdf` | Final research paper (PDF) |
| `html/` | Static website (open `index.html` in browser) |
| `mystdemo/` | Paper source files (MyST markdown) |
| `Data Exploration/` | **All analysis code and raw data** |

---

## 🔬 Reproduce the Regressions

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
```

---

### 1️⃣ Difference-in-Differences (DiD) Regression

**Location:** `Data Exploration/DiD/`

**Raw Data Files (in `Data Exploration/`):**
- `2010.q1-q4 512110 Motion picture and video production.csv`
- `2011.q1-q4 512110 Motion picture and video production.csv`
- ... (through 2025)
- `unemployment-all-state-numeric.csv`
- `quarterly-gdp-by-state.csv`

**Run the Regression:**
```bash
cd "Data Exploration/DiD"
jupyter notebook difference-in-difference-clean.ipynb
```
Or run all cells in: `Data Exploration/DiD/difference-in-difference-clean.ipynb`

**Output Files:**
- `Data Exploration/DiD/did_results_summary.csv` ← Regression coefficients & p-values
- `Data Exploration/DiD/did_raw_trends.png`
- `Data Exploration/DiD/did_parallel_trends.png`

---

### 2️⃣ Synthetic Control Method (SCM)

**Location:** `Data Exploration/SCM/`

**Raw Data Files (in `Data Exploration/`):**
- Same QCEW files as DiD (2010-2025)

**Run the Regression:**
```bash
cd "Data Exploration/SCM"
jupyter notebook scm_execution.ipynb
```
Or use the Python script:
```bash
python run_synthetic_control.py
```

**Output Files:**
- `Data Exploration/SCM/scm_results_summary.csv` ← Treatment effects & p-values
- `Data Exploration/SCM/scm_results_2015_employment.png`
- `Data Exploration/SCM/scm_results_2020_employment.png`
- `Data Exploration/SCM/scm_placebo_tests_2015.png`
- `Data Exploration/SCM/scm_placebo_tests_2020.png`

---

### 3️⃣ Migration Analysis (ACS)

**Location:** `Data Exploration/Migration/`

**Raw Data Files:**
- ⚠️ **IPUMS ACS data required** (not included due to size/licensing)
- Download from: https://usa.ipums.org/usa/
- Save as: `Data Exploration/ipums_acs_extract.csv`

**Variables to download from IPUMS:**
- YEAR, STATEFIP, GQ, PERWT, INDNAICS, MIGPLAC1, MIGRATE1
- Years: 2009-2023

**Run the Analysis:**
```bash
cd "Data Exploration/Migration"
jupyter notebook acs.ipynb
```

**Output Files:**
- `Data Exploration/Migration/california_film_migration.png`

---

### 4️⃣ Electoral Cycle Analysis

**Location:** `Data Exploration/Electoral Cycle/`

**Analysis:** Qualitative/descriptive (no regression)

**Read:** `Data Exploration/Electoral Cycle/findings.md`

---

## 📊 Results Traceability

Every number in the paper traces to these output files:

| Paper Table | Result | Source CSV |
|-------------|--------|------------|
| Table 2 (DiD) | Employment -18.3%, p=0.316 | `DiD/did_results_summary.csv` |
| Table 2 (DiD) | **Wages +9.1%, p=0.003** | `DiD/did_results_summary.csv` |
| Table 3 (SCM) | 2015: +3.5%, p=0.286 | `SCM/scm_results_summary.csv` |
| Table 3 (SCM) | 2020: +4.3%, p=0.143 | `SCM/scm_results_summary.csv` |
| Table 4 (Migration) | +2,029/yr avg | `Migration/acs.ipynb` output |

---

## 📄 View the Paper

### Option 1: PDF
Open `California_Film_Tax_Credits_Peter_Li.pdf`

### Option 2: Static HTML
Open `html/index.html` in your browser

### Option 3: MyST (interactive)
```bash
cd mystdemo
pip install mystmd
myst start
```
Then open http://localhost:3000

---

## 📚 Full Documentation

See `mystdemo/README.md` for detailed documentation including:
- Complete data source descriptions
- IPUMS download instructions
- BibTeX bibliography information
- Paper structure details

