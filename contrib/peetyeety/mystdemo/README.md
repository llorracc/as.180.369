# California Film Tax Credits Research Paper

**Author:** Peter Li  
**Title:** An Examination of the Effect on Employment and Wages of the California Film Tax Credit Programs

---

## Quick Start (View Paper)

### Prerequisites
- [Node.js](https://nodejs.org/) (v18 or higher)
- MyST CLI

### Install MyST
```bash
pip install mystmd
# or
npm install -g mystmd
```

### View the Paper (Web)
```bash
cd mystdemo
myst start
```
Then open **http://localhost:3000** in your browser.

### Build PDF
```bash
myst build --pdf
```
> **Note:** PDF generation requires LaTeX. Install with:
> - macOS: `brew install --cask mactex-no-gui` or `curl -sL "https://yihui.org/tinytex/install-bin-unix.sh" | sh`
> - Linux: `sudo apt install texlive-full`
> - Windows: [MiKTeX](https://miktex.org/download)

---

## Pre-built Outputs

- **PDF:** `California_Film_Tax_Credits_Peter_Li.pdf` (included)
- **HTML:** See `../html/index.html` (static website)

---

## 🔗 Results Traceability: Code → Paper

**Every number in the paper is traceable to code.** Below is the mapping:

### Difference-in-Differences Results (Table 2 in Paper)

| Result in Paper | Value | Source File | Output File |
|-----------------|-------|-------------|-------------|
| Employment Program 2.0 coefficient | -0.202 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| Employment Program 2.0 p-value | 0.316 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| Employment Program 3.0 coefficient | -0.036 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| Employment Program 3.0 p-value | 0.526 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| **Wages Program 2.0 coefficient** | **+0.087 (+9.1%)** | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| **Wages Program 2.0 p-value** | **0.003** | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| Wages Program 3.0 coefficient | -0.072 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |
| Wages Program 3.0 p-value | 0.153 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_results_summary.csv` |

### Synthetic Control Method Results (Table 3 in Paper)

| Result in Paper | Value | Source File | Output File |
|-----------------|-------|-------------|-------------|
| Program 2.0 (2015) effect | +3.5% | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_summary.csv` |
| Program 2.0 (2015) p-value | 0.286 | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_summary.csv` |
| Program 3.0 (2020) effect | +4.3% | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_summary.csv` |
| Program 3.0 (2020) p-value | 0.143 | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_summary.csv` |
| NY weight (both treatments) | 100% | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_summary.csv` |

### Migration Analysis (Table 4 in Paper)

| Result in Paper | Value | Source File | Output File |
|-----------------|-------|-------------|-------------|
| Average net migration | +2,029/year | `Data Exploration/Migration/acs.ipynb` | `Migration/california_film_migration.png` |
| 2015 net migration | +2,058 | `Data Exploration/Migration/acs.ipynb` | (in notebook output) |
| 2020 net migration | +1,667 | `Data Exploration/Migration/acs.ipynb` | (in notebook output) |

### Summary Statistics (Table 1 in Paper)

| Result in Paper | Value | Source File |
|-----------------|-------|-------------|
| CA mean employment | 109,656 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` |
| CA mean weekly wage | $2,338 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` |
| NY mean employment | 43,307 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` |
| GA mean employment | 10,158 | `Data Exploration/DiD/difference-in-difference-clean.ipynb` |

### Figures

| Figure in Paper | Source File | Output File |
|-----------------|-------------|-------------|
| Raw Trends | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_raw_trends.png` |
| Parallel Trends | `Data Exploration/DiD/difference-in-difference-clean.ipynb` | `DiD/did_parallel_trends.png` |
| SCM 2015 Results | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_2015_employment.png` |
| SCM 2020 Results | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_results_2020_employment.png` |
| Placebo Tests 2015 | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_placebo_tests_2015.png` |
| Placebo Tests 2020 | `Data Exploration/SCM/scm_execution.ipynb` | `SCM/scm_placebo_tests_2020.png` |
| Migration | `Data Exploration/Migration/acs.ipynb` | `Migration/california_film_migration.png` |

---

## Data Analysis Reproducibility

### Folder Structure

```
peetyeety/final/
├── California_Film_Tax_Credits_Peter_Li.pdf
├── html/                              # Static website
├── mystdemo/                          # Paper source
└── Data Exploration/                  # ALL ANALYSIS CODE
    ├── *.csv                          # QCEW raw data (2010-2025)
    ├── DiD/                           # Difference-in-Differences
    │   ├── difference-in-difference-clean.ipynb  ← RUN THIS
    │   ├── did_results_summary.csv               ← OUTPUT
    │   ├── did_raw_trends.png
    │   └── did_parallel_trends.png
    ├── SCM/                           # Synthetic Control Method
    │   ├── scm_execution.ipynb                   ← RUN THIS
    │   ├── run_synthetic_control.py              ← OR THIS
    │   ├── scm_results_summary.csv               ← OUTPUT
    │   └── scm_*.png
    ├── Migration/                     # ACS Migration
    │   ├── acs.ipynb                             ← RUN THIS
    │   └── california_film_migration.png         ← OUTPUT
    ├── Electoral Cycle/               # Political timing
    │   └── findings.md
    ├── unemployment-all-state-numeric.csv
    └── quarterly-gdp-by-state.csv
```

---

## Step-by-Step Replication

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
```

Or use conda:
```bash
conda env create -f binder/environment.yml
conda activate econark
```

---

### 1. Replicate DiD Results (Table 2)

**Navigate to:** `final/Data Exploration/DiD/`

**Raw data used (located in `final/Data Exploration/`):**
- `2010.q1-q4 512110 Motion picture and video production.csv` through `2025.q1-q1 512110*.csv`
- `unemployment-all-state-numeric.csv`
- `quarterly-gdp-by-state.csv`

**Run:**
```bash
cd "final/Data Exploration/DiD"
jupyter notebook difference-in-difference-clean.ipynb
```

**Execute all cells to generate:**
- `did_results_summary.csv` ← Contains exact coefficients and p-values for Table 2
- `did_raw_trends.png`
- `did_parallel_trends.png`

---

### 2. Replicate SCM Results (Table 3)

**Navigate to:** `final/Data Exploration/SCM/`

**Raw data used (located in `final/Data Exploration/`):**
- Same QCEW CSV files as DiD analysis

**Run (Option A - Jupyter):**
```bash
cd "final/Data Exploration/SCM"
jupyter notebook scm_execution.ipynb
```

**Run (Option B - Python script):**
```bash
cd "final/Data Exploration/SCM"
python run_synthetic_control.py
```

**Execute to generate:**
- `scm_results_summary.csv` ← Contains treatment effects and p-values for Table 3
- `scm_results_2015_employment.png`
- `scm_results_2020_employment.png`
- `scm_placebo_tests_2015.png`
- `scm_placebo_tests_2020.png`

---

### 3. Replicate Migration Analysis (Table 4)

**Navigate to:** `final/Data Exploration/Migration/`

**Raw data required:** `ipums_acs_extract.csv` (must download from IPUMS - see below)

**Run:**
```bash
cd "final/Data Exploration/Migration"
jupyter notebook acs.ipynb
```

**Execute all cells to generate:**
- `california_film_migration.png`
- Migration statistics printed in notebook output

---

### 4. Electoral Cycle Analysis (Table 5)

**Navigate to:** `final/Data Exploration/Electoral Cycle/`

**Read:** `findings.md` - Qualitative analysis, no regression code

---

## Data Sources

### ✅ Included Data

| File | Source | Used In |
|------|--------|---------|
| `2010-2025 512110*.csv` | [BLS QCEW](https://www.bls.gov/cew/) | DiD, SCM |
| `quarterly-gdp-by-state.csv` | BEA | DiD controls |
| `unemployment-all-state-numeric.csv` | BLS | DiD controls |

### ⚠️ Manual Download Required

#### 1. IPUMS ACS Microdata (for Migration Analysis)
- **Source:** [IPUMS USA](https://usa.ipums.org/usa/)
- **File needed:** `ipums_acs_extract.csv`
- **Location:** Save to `Data Exploration/`

**Variables to select:**
| Variable | Description |
|----------|-------------|
| YEAR | Survey year (2009-2023) |
| STATEFIP | State FIPS code |
| GQ | Group quarters status |
| PERWT | Person weight |
| INDNAICS | Industry (NAICS) |
| MIGPLAC1 | Migration place 1 year ago |
| MIGRATE1 | Migration status |

**Steps:**
1. Create free account at https://usa.ipums.org/usa/
2. Select ACS samples: 2009-2023
3. Add variables listed above
4. Submit extract, download CSV
5. Save as `Data Exploration/ipums_acs_extract.csv`

#### 2. County Market Tracker (optional, for additional analysis)
- **Source:** [Redfin Data Center](https://www.redfin.com/news/data-center/)
- **File:** `county_market_tracker.tsv000`

---

## Key Results Summary

| Analysis | Paper Section | Result | p-value | Significant? |
|----------|---------------|--------|---------|--------------|
| DiD Employment (2015) | Table 2 | -18.3% | 0.316 | No |
| DiD Employment (2020) | Table 2 | -3.5% | 0.526 | No |
| **DiD Wages (2015)** | Table 2 | **+9.1%** | **0.003** | **Yes** |
| DiD Wages (2020) | Table 2 | -6.9% | 0.153 | No |
| SCM Employment (2015) | Table 3 | +3.5% | 0.286 | No |
| SCM Employment (2020) | Table 3 | +4.3% | 0.143 | No |
| Migration | Table 4 | +2,029/yr avg | N/A | Persistent |
| Political Timing | Table 5 | Both election years | N/A | Descriptive |

---

## Paper Source Files

```
mystdemo/
├── myst.yml                 # MyST configuration
├── references.bib           # BibTeX bibliography (25 sources)
├── 00_paper_root.md         # Main document
├── 01_abstract.md           # Abstract
├── 02_introduction.md       # Introduction
├── 03_literature.md         # Literature Review
├── 04_methodology.md        # Methodology
├── 05_results.md            # Results (Tables 1-5)
├── 06_discussion.md         # Discussion
├── 07_conclusion.md         # Conclusion
├── 08_bibliography.md       # References
├── 07_appendix.ipynb        # Appendix
└── images/                  # All figures (copied from analysis)
```

---

## Contact

Peter Li - Johns Hopkins University
