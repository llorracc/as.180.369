import pandas as pd
import os
import glob
import re
from pandas.tseries.offsets import QuarterEnd


def build_xpt_dataset_smart():
    print("--- STARTING OLD ERA (XPT) DATA BUILDER V2 (CORRECTED) ---")

    # 1. Define SAS Variable Names (Old Era)
    # RSSD9001: Entity ID
    # RSSD9999: Report Date (Standard internal date variable)

    # ASSETS:
    # RCFD2170: Total Assets (Consolidated)
    # RCON2170: Total Assets (Domestic)

    # LOANS:
    # RCFD1763: Total C&I Loans (Consolidated) - CRITICAL for large banks
    # RCFD1766: C&I Loans to U.S. Addressees (Consolidated)
    # RCON1766: C&I Loans (Domestic)

    id_col = 'RSSD9001'
    date_col_internal = 'RSSD9999'

    # We define the columns we WANT to find.
    # Note: We don't filter strictly on read because read_sas reads the whole file anyway.
    target_cols = [
        'RSSD9001', 'RSSD9999',
        'RCFD2170', 'RCON2170',
        'RCFD1763', 'RCFD1766', 'RCON1766'
    ]

    root_dir = "."
    xpt_files = glob.glob(os.path.join(
        root_dir, "**", "*.xpt"), recursive=True)

    print(f"Found {len(xpt_files)} .xpt files. Processing...")

    master_list = []

    for file_path in xpt_files:
        filename = os.path.basename(file_path)
        date_obj = None

        # --- STRATEGY 1: PARSE FILENAME (YYMM) ---
        match = re.search(
            r'([0-9]{2})([0-9]{2})\.xpt$', filename, re.IGNORECASE)

        if match:
            yy = int(match.group(1))
            mm = int(match.group(2))

            # Year Pivot Logic (Window: 1950-2049)
            if yy > 50:
                full_year = 1900 + yy
            else:
                full_year = 2000 + yy

            try:
                # Snap to QuarterEnd
                date_obj = pd.Timestamp(
                    year=full_year, month=mm, day=1) + QuarterEnd(0)
            except:
                print(f"  Warning: Invalid date in filename {filename}")

        # --- STRATEGY 2: READ AND EXTRACT ---
        try:
            # Read SAS file
            df = pd.read_sas(file_path, format='xport')

            # Convert columns to Uppercase
            df.columns = [c.upper() for c in df.columns]

            # If date not found in filename, try internal SAS date
            if date_obj is None:
                if date_col_internal in df.columns:
                    # SAS Dates are days since 1960-01-01
                    sas_date_val = df[date_col_internal].mode()[0]
                    date_obj = pd.to_datetime(
                        '1960-01-01') + pd.to_timedelta(sas_date_val, unit='D')
                    print(
                        f"  Extracted internal date {date_obj.date()} from {filename}")
                else:
                    print(f"Skipping {filename}: Could not determine date.")
                    continue

            # Standardize ID
            if id_col not in df.columns:
                continue

            df[id_col] = pd.to_numeric(df[id_col], errors='coerce')
            df.rename(columns={id_col: 'bank_id'}, inplace=True)

            # --- STANDARDIZE ASSETS ---
            # Priority: RCFD (Consolidated) > RCON (Domestic)
            # Create a base series of NaNs
            df['assets'] = pd.NA

            if 'RCON2170' in df.columns:
                df['assets'] = df['RCON2170']

            if 'RCFD2170' in df.columns:
                # combine_first: if 'RCFD' is present, use it; else keep 'RCON'
                df['assets'] = df['RCFD2170'].combine_first(df['assets'])

            # --- STANDARDIZE C&I LOANS ---
            # Priority: RCFD1763 (Total Global) > RCFD1766 (US Global) > RCON1766 (Domestic)

            # Start with Domestic as baseline
            loan_series = df.get('RCON1766', pd.Series([pd.NA]*len(df)))

            # Update with US Global if available (fills gaps or overwrites depending on preference,
            # here we want RCFD to supersede RCON if the bank reports RCFD)
            if 'RCFD1766' in df.columns:
                loan_series = df['RCFD1766'].combine_first(loan_series)

            # Update with Total Global (Best Metric)
            if 'RCFD1763' in df.columns:
                loan_series = df['RCFD1763'].combine_first(loan_series)

            df['ci_loans'] = loan_series

            # --- FINAL DATA PREP ---
            df['date'] = date_obj

            # Keep only valid data columns
            df = df[['bank_id', 'date', 'assets', 'ci_loans']]
            df = df.dropna(subset=['bank_id'])

            master_list.append(df)
            print(
                f"Processed {filename}: {len(df)} banks. Date: {date_obj.date()}")

        except Exception as e:
            print(f"  Error reading {filename}: {e}")

    # --- COMPILE ---
    if not master_list:
        print("No data found.")
        return

    print("Compiling Old Era Master Dataset...")
    full_old_df = pd.concat(master_list, ignore_index=True)

    # Final Polish
    full_old_df['assets'] = pd.to_numeric(
        full_old_df['assets'], errors='coerce')
    full_old_df['ci_loans'] = pd.to_numeric(
        full_old_df['ci_loans'], errors='coerce')

    # Remove rows with 0 assets to avoid DivideByZero
    full_old_df = full_old_df[full_old_df['assets'] > 0]

    # Calculate Risk Taking
    full_old_df['risk_taking'] = full_old_df['ci_loans'] / \
        full_old_df['assets']

    # Final cleanup of NaNs created by risk calc
    full_old_df = full_old_df.dropna(subset=['risk_taking'])

    output_filename = 'OLD_RAW_BANK_DATA.csv'
    full_old_df.to_csv(output_filename, index=False)

    print(f"\nSUCCESS! Processed {len(full_old_df)} rows from Old Era.")
    print(f"Saved to: {output_filename}")


if __name__ == "__main__":
    build_xpt_dataset_smart()
