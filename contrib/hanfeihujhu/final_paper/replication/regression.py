import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

warnings.simplefilter(action='ignore', category=FutureWarning)


def run_robust_regression():
    print("--- [1] DATA PREPARATION & CLEANING ---")
    dataset_paths = [
        Path('master_merged_dataset.csv'),
        Path('MASTER_MERGED_DATASET.csv'),
    ]
    df = None
    for path in dataset_paths:
        if path.exists():
            df = pd.read_csv(path)
            print(f"Loaded dataset from {path}")
            break
    if df is None:
        print("MASTER dataset not found. Please run merge.py first.")
        return

    df['date'] = pd.to_datetime(df['date'])

    # --- ADDRESSING POINT 9: Drop Short Panels ---
    # Banks with fewer than 8 observations (2 years) do not contribute enough within-variance
    counts = df.groupby('bank_id')['date'].count()
    valid_banks = counts[counts >= 8].index
    df = df[df['bank_id'].isin(valid_banks)].copy()
    print(
        f" > Dropped short-lived entities. Banks remaining: {df['bank_id'].nunique():,}")

    # --- ADDRESSING POINT 1: Orthogonalization ---
    # Isolate pure sentiment from the rate level
    ortho_data = df[['fed_sentiment', 'fed_funds_rate']].dropna()
    X_ortho = sm.add_constant(ortho_data['fed_funds_rate'])
    model_ortho = sm.OLS(ortho_data['fed_sentiment'], X_ortho).fit()
    df.loc[ortho_data.index, 'sentiment_shock'] = model_ortho.resid

    # --- ADDRESSING POINT 2: Standardization ---
    # Standardize shock to 1 SD for interpretability
    df['sentiment_shock_std'] = df['sentiment_shock'] / \
        df['sentiment_shock'].std()

    # --- ADDRESSING POINT 4 & 10: Functional Form & Scaling ---
    # Log Assets
    df['log_assets'] = np.log(df['assets'].replace(0, np.nan))

    # CENTER Log Assets.
    # This is crucial. Now 'log_assets_centered' = 0 means "Average Sized Bank".
    # This fixes multicollinearity by orthogonalizing the interaction from the main effect.
    df['log_assets_centered'] = df['log_assets'] - df['log_assets'].mean()

    # Sort for Lagging
    df = df.sort_values(['bank_id', 'date'])

    # --- ADDRESSING POINT 5: Dynamic Structure ---
    # We MUST include lags of the dependent variable (Risk Taking)
    # We also lag controls to mitigate simultaneity (Point 8)
    vars_to_lag = ['risk_taking', 'sentiment_shock_std',
                   'fed_funds_rate', 'log_assets_centered']

    for var in vars_to_lag:
        df[f'{var}_lag'] = df.groupby('bank_id')[var].shift(1)

    # --- ADDRESSING POINT 3: Continuous Interaction ---
    # Instead of a dummy, we use Size as a continuous moderator.
    # Interaction = (Last Quarter's Shock) * (Last Quarter's Size)
    df['shock_x_size'] = df['sentiment_shock_std_lag'] * \
        df['log_assets_centered_lag']

    # --- ESTIMATION ---
    print("--- [2] ESTIMATING DYNAMIC PANEL MODEL ---")

    df = df.set_index(['bank_id', 'date'])

    reg_df = df.dropna(subset=[
        'risk_taking', 'risk_taking_lag',
        'sentiment_shock_std_lag', 'shock_x_size',
        'fed_funds_rate_lag', 'log_assets_centered_lag'
    ])

    exog_vars = [
        'const',
        'risk_taking_lag',           # Dynamics (Fixes Point 5)
        'sentiment_shock_std_lag',   # Main Effect (at mean size)
        # Interaction (Does Size change sensitivity?)
        'shock_x_size',
        'log_assets_centered_lag',   # Control for Size
        'fed_funds_rate_lag'         # Control for Rate
    ]

    reg_df['const'] = 1

    # ADDRESSING POINT 7: Fixed Effects
    mod = PanelOLS(reg_df['risk_taking'],
                   reg_df[exog_vars], entity_effects=True)

    # ADDRESSING POINT 6: Cluster Level
    # Explicitly clustering by Entity (Bank) and Time (Date)
    res = mod.fit(cov_type='clustered', cluster_entity=True, cluster_time=True)

    print(res)

    # --- DIAGNOSTIC CHECKS ---
    print("\n--- DIAGNOSTICS ---")
    print(f"Within R-squared: {res.rsquared_within:.4f}")
    print(
        f"Autocorrelation check (LDV coeff): {res.params['risk_taking_lag']:.4f}")


if __name__ == "__main__":
    run_robust_regression()
