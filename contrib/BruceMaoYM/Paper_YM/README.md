# Buy-Now-Pay-Later Stock Returns and Interest Rate Sensitivity

## Reproducibility Guide

This repository contains all code, data, and documentation necessary to reproduce the analysis in "Buy-Now-Pay-Later Stock Returns and Interest Rate Sensitivity: An Empirical Analysis of Monetary Policy Transmission to Fintech Credit Providers."

### Quick Start

To reproduce the entire analysis and build the paper:

```bash
# Make the reproduction script executable
chmod +x reproduce.sh

# Run the reproduction script
./reproduce.sh
```

The script will:
1. Create/update the conda environment from `binder/environment.yml`
2. Execute the data analysis notebook (`04_dataanalysis.ipynb`)
3. Build the PDF and HTML versions of the paper

### Manual Reproduction Steps

If you prefer to run steps manually:

#### 1. Set Up Environment

```bash
# Create/update conda environment
conda env update --file ./binder/environment.yml

# Activate environment
conda activate econark

# Install Jupyter kernel
python -m ipykernel install --user --name econark
```

#### 2. Execute Analysis

```bash
# Run the data analysis notebook
jupyter nbconvert --to notebook --execute --inplace 04_dataanalysis.ipynb
```

#### 3. Build Paper

```bash
# Build PDF and HTML
myst build --pdf --html
```

### Data Sources

All data are publicly available and collected automatically by the analysis code:

- **Stock Prices**: Yahoo Finance (via `yfinance` library)
  - Tickers: PYPL, AFRM, SEZL, SPY
  - Period: February 2020 - August 2025
  - Frequency: Monthly (month-end closing prices)

- **Macroeconomic Data**: FRED (Federal Reserve Economic Data, via `fredapi` library)
  - Federal Funds Rate (FEDFUNDS)
  - Consumer Sentiment Index (UMCSENT)
  - Real Disposable Personal Income (DSPIC96)
  - Consumer Price Index (CPIAUCSLSA)
  - Period: February 2020 - August 2025
  - Frequency: Monthly

**Note**: A free FRED API key is required. Register at https://fred.stlouisfed.org/docs/api/api_key.html and set the environment variable `FRED_API_KEY` before running the analysis.

### Software Requirements

- Python 3.11.10
- Key packages (see `binder/environment.yml` for complete list):
  - `pandas` 2.2.3
  - `statsmodels` 0.14.4
  - `matplotlib` 3.9.2
  - `yfinance` ≥0.2.0
  - `fredapi` ≥0.5.0
  - `mystmd` 1.3.16 (for building the paper)

### File Structure

```
Paper_YM/
├── 01_abstract.md          # Abstract
├── 02_introduction.md      # Introduction and methodology
├── 03_literature.md        # Literature review
├── 04_dataanalysis.ipynb   # Complete analysis code (data collection, regressions, diagnostics)
├── 05_conclusion.md        # Conclusions
├── 06_bibliography.ipynb   # Bibliography
├── 07_appendix.ipynb       # Appendix
├── binder/
│   └── environment.yml     # Conda environment specification
├── reproduce.sh            # Automated reproduction script
├── myst.yml                # Paper build configuration
└── references.bib          # Bibliography file
```

### Key Features for Reproducibility

1. **Complete Code**: All analysis code is in `04_dataanalysis.ipynb`, including:
   - Data collection from Yahoo Finance and FRED
   - Variable construction and transformations
   - Regression estimation (base and full models)
   - Diagnostic tests (VIF, Breusch-Pagan, Durbin-Watson, Jarque-Bera)
   - Robustness checks
   - Visualizations

2. **Public Data**: All data sources are publicly available and free to access

3. **Version Control**: Exact package versions specified in `environment.yml`

4. **Documentation**: Detailed comments and explanations throughout the code

5. **Automated Build**: Single script (`reproduce.sh`) reproduces entire analysis

### Troubleshooting

**Issue**: FRED API key not found
- **Solution**: Register for a free API key at https://fred.stlouisfed.org/docs/api/api_key.html and set `FRED_API_KEY` environment variable

**Issue**: Conda environment creation fails
- **Solution**: Ensure you have conda/mamba installed. Try using `mamba` instead of `conda` for faster package resolution

**Issue**: Notebook execution fails
- **Solution**: Ensure all cells are executed in order. The notebook is designed to be run from top to bottom

**Issue**: Paper build fails
- **Solution**: Ensure `mystmd` is installed and up to date. Check `myst.yml` configuration

### Contact

For questions about reproducibility or the analysis, please refer to the paper or open an issue in the repository.

### License

This research is provided for academic and research purposes. Data sources (Yahoo Finance, FRED) maintain their own terms of use.






