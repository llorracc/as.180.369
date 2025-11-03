# How to Run SCM Analysis in Jupyter (to get 2020 plots)

## Quick Steps:

1. **Open your Jupyter notebook** (`mytry.ipynb` or create new one)

2. **Add a new cell** and paste this:

```python
# Change to SCM directory and run the script
import os
os.chdir('/Users/peterli/Documents/GitHub/as.180.369/contrib/peetyeety/Data Exploration/SCM')

# Run the entire script
exec(open('run_synthetic_control.py').read())
```

3. **Run the cell** - it will:
   - Analyze both 2015 and 2020 treatments
   - Generate 4 plots (2 for 2015, 2 for 2020)
   - Export CSV files

## What You'll Get:

### Plots Created:
- `scm_results_2015_employment.png` ✓ (you already have this)
- `scm_placebo_tests_2015.png` ✓ (you already have this)
- `scm_results_2020_employment.png` ✨ **NEW**
- `scm_placebo_tests_2020.png` ✨ **NEW**

### CSV Files:
- `scm_results_summary.csv` - Updated with both 2015 & 2020
- `scm_timeseries_employment_2015.csv`
- `scm_timeseries_employment_2020.csv` ✨ **NEW**

---

## Why This Works:

Your Jupyter environment has matplotlib installed, so the plots will generate properly. The terminal `python3` command uses a different Python environment without matplotlib.

