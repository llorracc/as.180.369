import pandas as pd
from pathlib import Path
import sys


def build_macro_golden_source():
    print("--- MACRO + BANK DATA BUILDER (AUTO) ---")

    # Hardcoded filenames
    input_bank_file = "all_banks_merged.csv"
    fed_file = "fed_funds.csv"
    sent_file = "fomc_sentiment_data.csv"

    # Final Output filename
    output_file = "MASTER_MERGED_DATASET.csv"

    # Check for files (look in current dir, then parent dir)
    files = {'bank': input_bank_file, 'fed': fed_file, 'sent': sent_file}
    paths = {}

    for label, fname in files.items():
        if Path(fname).exists():
            paths[label] = fname
        elif Path(f"../{fname}").exists():
            paths[label] = f"../{fname}"
        else:
            print(
                f"CRITICAL ERROR: Could not find '{fname}' in current or parent directory.")
            sys.exit(1)

    # 1. Process Sentiment
    print(f"Processing {paths['sent']}...")
    df_sent = pd.read_csv(paths['sent'])

    # Simple column detection
    sent_col = next(
        (c for c in df_sent.columns if 'sentiment' in c.lower()), None)
    date_col_s = next(
        (c for c in df_sent.columns if 'date' in c.lower()), None)

    if not sent_col or not date_col_s:
        print(f"Error: Missing date/sentiment columns in {paths['sent']}")
        sys.exit(1)

    df_sent = df_sent[[date_col_s, sent_col]].rename(
        columns={date_col_s: 'date', sent_col: 'fed_sentiment'})
    df_sent['date'] = pd.to_datetime(df_sent['date'])

    # 2. Process Fed Funds
    print(f"Processing {paths['fed']}...")
    df_fed = pd.read_csv(paths['fed'])

    fed_col = next(
        (c for c in df_fed.columns if 'fund' in c.lower() or 'rate' in c.lower()), None)
    date_col_f = next((c for c in df_fed.columns if 'date' in c.lower()), None)

    if not fed_col or not date_col_f:
        print(f"Error: Missing date/rate columns in {paths['fed']}")
        sys.exit(1)

    df_fed = df_fed[[date_col_f, fed_col]].rename(
        columns={date_col_f: 'date', fed_col: 'fed_funds_rate'})
    df_fed['date'] = pd.to_datetime(df_fed['date'])

    # 3. Merge & Aggregate Macro Data (In Memory Only)
    print("Aggregating macro data to quarterly level...")
    macro_df = pd.merge(df_sent, df_fed, on='date', how='outer')
    macro_df['quarter_key'] = macro_df['date'].dt.to_period('Q').astype(str)

    macro_clean = (
        macro_df.groupby('quarter_key')[['fed_sentiment', 'fed_funds_rate']]
        .mean()
        .reset_index()
    )

    # 4. Load Bank Panel
    print(f"Loading Bank Panel from {paths['bank']}...")
    df_bank = pd.read_csv(paths['bank'])

    # Create join key
    if 'quarter_key' not in df_bank.columns:
        if 'date' in df_bank.columns:
            df_bank['date'] = pd.to_datetime(df_bank['date'])
            df_bank['quarter_key'] = df_bank['date'].dt.to_period(
                'Q').astype(str)
        else:
            print("Error: Bank file needs 'date' or 'quarter_key' column.")
            sys.exit(1)

    # 5. Final Merge
    print(f"Merging macro data into {output_file}...")
    merged = pd.merge(df_bank, macro_clean, on='quarter_key', how='left')

    # 6. Save
    merged.to_csv(output_file, index=False)

    print(f"\nSUCCESS! Created '{output_file}' from '{input_bank_file}'.")
    print(f"Total Rows: {len(merged)}")
    print(merged[['quarter_key', 'fed_sentiment', 'fed_funds_rate']].head())


if __name__ == "__main__":
    build_macro_golden_source()
