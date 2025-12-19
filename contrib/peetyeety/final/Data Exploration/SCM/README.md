# Synthetic Control Method - Minimal Files

## 📁 Files

### Core Analysis Files:
1. **`run_synthetic_control.py`** - The analysis script (analyzes BOTH 2015 & 2020)
2. **`scm_results_summary.csv`** - Key results (2 rows: 2015 & 2020)
3. **`scm_timeseries_employment_2015.csv`** - 2015 time series data
4. **`scm_timeseries_employment_2020.csv`** - 2020 time series data

### Generated Plots (when matplotlib available):
5. **`scm_results_2015_employment.png`** - 2015 trends & treatment effect
6. **`scm_placebo_tests_2015.png`** - 2015 placebo tests
7. **`scm_results_2020_employment.png`** - 2020 trends & treatment effect
8. **`scm_placebo_tests_2020.png`** - 2020 placebo tests

---

## 🚀 How to Run

### Option 1: Terminal (if you have matplotlib)
```bash
cd SCM
python3 run_synthetic_control.py
```

### Option 2: Jupyter Notebook (recommended)
1. Open `run_synthetic_control.py` in Jupyter as a text file
2. Copy the entire code
3. Paste into a new notebook cell
4. Run it

The script will use your Jupyter environment's packages (matplotlib, seaborn, etc.)

---

## ❓ Why didn't the .py work?

**Different Python environments!**

- Your **Jupyter notebook** uses one Python environment (has matplotlib ✓)
- Your **terminal `python3`** uses a different environment (no matplotlib ✗)

**Solution:** Just run the code in Jupyter where you already have the packages.

---

## 📊 Quick Results

### 2015 Program 2.0:
- **Effect**: +157.6% employment increase
- **Significance**: Not significant (p=0.67)
- **Weights**: NY 98.9%, GA 1.1%

### 2020 Program 3.0:
- **Effect**: +159.4% employment increase
- **Significance**: Not significant (p=0.67)
- **Weights**: NY 100%, GA 0%

**Why not significant?** Only 2 donor states → low statistical power

**Note on 2020**: Results include COVID-19 period effects

