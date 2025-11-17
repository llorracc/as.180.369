# File Index - BNPL Research Project

Quick reference guide to understand what each file does.

## 📓 Notebooks (`notebooks/`)

| File Name | Purpose |
|-----------|---------|
| `BNPL_Research_Analysis.ipynb` | **Main analysis notebook** - Panel regression, financial analysis, visualizations |
| `BNPL_Comparative_Studies.ipynb` | Comparative analysis of BNPL vs traditional fintech |
| `BNPL_Literature_Map.ipynb` | Literature mapping and citation network analysis |
| `GDP_Returns_Analysis.ipynb` | GDP returns analysis (separate project) |

## 🐍 Scripts (`scripts/`)

| File Name | Purpose |
|-----------|---------|
| `download_sec_edgar_10q.py` | Downloads 10-Q filings from SEC EDGAR database |
| `parse_sec_10q_filings.py` | Parses downloaded SEC filings to extract financial data |
| `BNPL_extracted_code_backup.py` | Backup of extracted code from notebook (not actively used) |

## 📄 Documentation (`docs/`)

| File Name | Purpose |
|-----------|---------|
| `Abstract.md` | Research paper abstract |
| `Literature Review.md` | Comprehensive literature review |
| `Research Paper Pitch.md` | Research proposal/pitch |
| `Essay Summary and Stats Outline.md` | Essay summary and statistics outline |
| `Introduction.md` | Personal introduction/bio |
| `Korinek Reflection.md` | Reflection on Korinek's work |
| `Class01_Dennett_Summary.md` | Summary of class 01 on Dennett |
| `SEC_Data_Extraction_Guide.md` | Guide for extracting data from SEC filings |

## 📁 Data (`data/`)

Created automatically when downloading SEC EDGAR data or exporting results.
- SEC EDGAR filings (downloaded via `download_sec_edgar_10q.py`)
- CSV/Excel exports from analysis notebooks

## 🔄 Workflow

1. **Data Collection**: Run `scripts/download_sec_edgar_10q.py` to download SEC filings
2. **Data Parsing**: Use `scripts/parse_sec_10q_filings.py` to extract financial metrics
3. **Analysis**: Run `notebooks/BNPL_Research_Analysis.ipynb` for main analysis
4. **Documentation**: Reference `docs/` folder for research notes and guides
