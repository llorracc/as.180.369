# BNPL Research Analysis

This directory contains research materials for the BNPL (Buy Now Pay Later) comparative analysis project.

## 📁 Directory Structure

```
BruceMaoYM/
├── notebooks/          # Jupyter notebooks for analysis
├── scripts/            # Python scripts for data collection
├── docs/               # Documentation and research notes
├── data/               # Data files (created when downloading)
└── README.md           # This file
```

## 📓 Notebooks (`notebooks/`)

- **`BNPL_Research_Analysis.ipynb`** - **Main analysis notebook**
  - Panel regression analysis
  - Financial performance comparisons
  - Visualizations and diagnostics
  
- **`BNPL_Comparative_Studies.ipynb`** - Comparative analysis studies

- **`BNPL_Literature_Map.ipynb`** - Literature mapping and citation networks

- **`GDP_Returns_Analysis.ipynb`** - GDP returns analysis (separate project)

## 🐍 Scripts (`scripts/`)

- **`download_sec_edgar_10q.py`** - Downloads 10-Q filings from SEC EDGAR
  ```bash
  python scripts/download_sec_edgar_10q.py
  ```

- **`parse_sec_10q_filings.py`** - Parses SEC filings to extract financial data

- **`BNPL_extracted_code_backup.py`** - Backup of extracted code (not actively used)

## 📄 Documentation (`docs/`)

- `Abstract.md` - Research paper abstract
- `Literature Review.md` - Comprehensive literature review  
- `Research Paper Pitch.md` - Research proposal
- `Introduction.md` - Personal introduction
- `SEC_Data_Extraction_Guide.md` - Guide for SEC data extraction
- Other research notes and reflections

## 🚀 Quick Start

1. **Run the main analysis:**
   ```bash
   cd notebooks
   jupyter notebook BNPL_Research_Analysis.ipynb
   ```

2. **Download SEC EDGAR data (optional):**
   ```bash
   python scripts/download_sec_edgar_10q.py
   ```

3. **View file index:**
   See `FILE_INDEX.md` for detailed file descriptions

## 📊 Data Sources

- **yfinance**: Recent financial data (~1.5 years)
- **SEC EDGAR**: Historical quarterly filings (2021+)
- **CFPB**: Consumer complaint data (2011+)

## ⚠️ Notes

- The main analysis works with yfinance data (last ~1.5 years)
- SEC EDGAR data provides historical data back to 2021
- CFPB complaint data can extend the analysis further
