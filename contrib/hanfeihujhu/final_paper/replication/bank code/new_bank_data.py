import pandas as pd
import os
import glob
import re


def build_bank_dataset_recursive():
    print("--- STARTING BANK DATA BUILDER ---")

    # 1. Setup Columns
    # IDRSSD: Bank ID
    # RCFD2170: Total Assets (Consolidated)
    # RCON2170: Total Assets (Domestic - fallback)

    # LOANS:
    # RCFD1763: Total C&I Loans (Consolidated - Includes Foreign & Domestic)
    # RCFD1766: C&I Loans to U.S. Addressees (Consolidated - Partial)
    # RCON1766: C&I Loans (Domestic)

    asset_cols = ['IDRSSD', 'RCFD2170', 'RCON2170']
    # Added RCFD1763 for accurate Total C&I on global banks
    loan_cols = ['IDRSSD', 'RCFD1763', 'RCFD1766', 'RCON1766']

    all_quarters = []

    root_dir = "."
    subfolders = [f.path for f in os.scandir(root_dir) if f.is_dir()]

    print(f"Found {len(subfolders)} folders. Scanning for data files...")

    for folder in subfolders:
        # 2. Find Schedule RC (Assets) and Schedule RCCI (Loans)
        # CRITICAL FIX: The FFIEC file for loans is named "Schedule RCCI", not "Schedule CI"
        rc_files = glob.glob(os.path.join(folder, "*Schedule RC *.txt"))
        ci_files = glob.glob(os.path.join(folder, "*Schedule RCCI *.txt"))

        if not rc_files or not ci_files:
            # Silent skip or debug print if needed
            continue

        path_rc = rc_files[0]
        path_ci = ci_files[0]

        # Extract Date
        date_match = re.search(r'(\d{8})', os.path.basename(path_rc))
        if not date_match:
            print(f"Skipping {folder}: Could not determine date.")
            continue

        date_str = date_match.group(1)

        try:
            # 3. Read ASSETS (Schedule RC)
            df_rc = pd.read_csv(path_rc, sep='\t',
                                skiprows=0, low_memory=False)
            existing_asset_cols = [c for c in asset_cols if c in df_rc.columns]
            df_rc = df_rc[existing_asset_cols]

            # 4. Read LOANS (Schedule RC-C Part I)
            df_ci = pd.read_csv(path_ci, sep='\t',
                                skiprows=0, low_memory=False)
            existing_loan_cols = [c for c in loan_cols if c in df_ci.columns]
            df_ci = df_ci[existing_loan_cols]

            # 5. Merge
            if 'IDRSSD' not in df_rc.columns or 'IDRSSD' not in df_ci.columns:
                print(f"Skipping {date_str}: Missing IDRSSD column.")
                continue

            df_quarter = pd.merge(df_rc, df_ci, on='IDRSSD', how='inner')
            df_quarter['date'] = pd.to_datetime(date_str, format='%m%d%Y')

            # 6. Standardize Assets
            if 'RCFD2170' in df_quarter.columns:
                df_quarter['assets'] = df_quarter['RCFD2170'].fillna(
                    df_quarter.get('RCON2170', 0))
            elif 'RCON2170' in df_quarter.columns:
                df_quarter['assets'] = df_quarter['RCON2170']
            else:
                df_quarter['assets'] = pd.NA

            # 7. Standardize C&I Loans (Prioritize Total Global -> US Global -> Domestic)
            # RCFD1763 = Total C&I (Consolidated)
            # RCFD1766 = C&I to US Addressees (Consolidated)
            # RCON1766 = Total C&I (Domestic)

            df_quarter['ci_loans'] = 0  # Default

            if 'RCFD1763' in df_quarter.columns:
                # Primary for large banks
                df_quarter['ci_loans'] = df_quarter['RCFD1763']

            # Fill gaps where RCFD1763 might be missing but RCFD1766 exists
            if 'RCFD1766' in df_quarter.columns:
                df_quarter['ci_loans'] = df_quarter['ci_loans'].fillna(
                    df_quarter['RCFD1766'])
                # If we initialized with 0, fillna won't work on 0s, so we use logic:
                # If 1763 was missing, column is 0 (or NaN if we didn't init).
                # Better approach: Coalesce.

            # Re-doing clean coalescing logic:
            # Create a temporary series for the best available C&I data

            # Start with Domestic (RCON1766) as baseline
            temp_loans = df_quarter.get(
                'RCON1766', pd.Series([pd.NA]*len(df_quarter)))

            # Overwrite with RCFD1766 (US Addressees) if available
            if 'RCFD1766' in df_quarter.columns:
                temp_loans = df_quarter['RCFD1766'].combine_first(temp_loans)

            # Overwrite with RCFD1763 (Total Consolidated) if available - Best Metric
            if 'RCFD1763' in df_quarter.columns:
                temp_loans = df_quarter['RCFD1763'].combine_first(temp_loans)

            df_quarter['ci_loans'] = temp_loans

            # 8. Clean up
            df_quarter.rename(columns={'IDRSSD': 'bank_id'}, inplace=True)
            df_quarter = df_quarter[['bank_id', 'date', 'assets', 'ci_loans']]

            # Ensure numeric
            df_quarter['assets'] = pd.to_numeric(
                df_quarter['assets'], errors='coerce')
            df_quarter['ci_loans'] = pd.to_numeric(
                df_quarter['ci_loans'], errors='coerce')

            all_quarters.append(df_quarter)
            print(f"Processed {date_str}: {len(df_quarter)} banks.")

        except Exception as e:
            print(f"Error reading {date_str} in {folder}: {e}")

    # 9. Compile and Save
    if not all_quarters:
        print("CRITICAL: No data found. Ensure folders are named correctly (e.g. '03312008') and contain 'Schedule RC' and 'Schedule RCCI' files.")
        return

    print("Compiling Master Dataset...")
    master_df = pd.concat(all_quarters, ignore_index=True)

    # Calculate Risk Taking
    master_df['risk_taking'] = master_df['ci_loans'] / master_df['assets']

    # Filter
    master_df = master_df.dropna(subset=['assets', 'risk_taking'])
    master_df = master_df[master_df['assets'] > 0]

    output_filename = 'NEW_RAW_BANK_DATA.csv'
    master_df.to_csv(output_filename, index=False)

    print(f"\nSUCCESS! Built dataset with {len(master_df)} rows.")
    print(f"Saved to: {output_filename}")

    # Diagnostics
    count_2008 = len(master_df[master_df['date'].dt.year == 2008])
    print(f"Diagnostics: Rows found for 2008: {count_2008}")


if __name__ == "__main__":
    build_bank_dataset_recursive()
