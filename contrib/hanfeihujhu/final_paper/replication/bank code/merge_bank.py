import pandas as pd
import os
import glob


def find_file(filename, search_path="."):
    """Recursively searches for a file in the directory tree."""
    print(f"  Searching for '{filename}'...")
    # Recursive glob search
    matches = glob.glob(os.path.join(
        search_path, "**", filename), recursive=True)
    if matches:
        print(f"  -> Found at: {matches[0]}")
        return matches[0]
    return None


def run_smart_merge():
    print("==================================================")
    print("       SMART BANK DATA MERGER                     ")
    print("==================================================")
    print(f"Current Working Directory: {os.getcwd()}\n")

    # --- STEP 1: LOCATE FILES ---
    print("Step 1: Locating Input Files...")

    path_new = find_file("NEW_RAW_BANK_DATA.csv")
    path_old = find_file("OLD_RAW_BANK_DATA.csv")

    if not path_new and not path_old:
        print("\nCRITICAL ERROR: Could not find ANY bank data files.")
        print("You must run the builder scripts first:")
        print("  1. Run 'build_bank_data.py' (for Modern data)")
        print("  2. Run 'build_old_data_v2.py' (for Old data)")
        return

    # --- STEP 2: LOAD DATA ---
    print("\nStep 2: Loading Data...")
    dfs = []

    if path_new:
        try:
            df_new = pd.read_csv(path_new)
            print(f"  -> Loaded Modern Data: {len(df_new):,} rows")
            dfs.append(df_new)
        except Exception as e:
            print(f"  -> Error reading Modern Data: {e}")

    if path_old:
        try:
            df_old = pd.read_csv(path_old)
            print(f"  -> Loaded Old Data: {len(df_old):,} rows")
            dfs.append(df_old)
        except Exception as e:
            print(f"  -> Error reading Old Data: {e}")

    # --- STEP 3: MERGE ---
    print("\nStep 3: Merging...")
    if not dfs:
        print("  -> No data loaded. Exiting.")
        return

    merged_df = pd.concat(dfs, ignore_index=True)

    # Standardize Date
    merged_df['date'] = pd.to_datetime(merged_df['date'])

    # Deduplicate (Priority to Modern Data if overlaps exist)
    merged_df = merged_df.sort_values(['date', 'bank_id'])
    before_dedup = len(merged_df)
    merged_df = merged_df.drop_duplicates(
        subset=['bank_id', 'date'], keep='last')
    print(
        f"  -> Deduplication removed {before_dedup - len(merged_df):,} duplicates.")

    # --- STEP 4: SAVE ---
    output_filename = "ALL_BANKS_MERGED.csv"
    merged_df.to_csv(output_filename, index=False)

    print("\n" + "="*50)
    print(f"SUCCESS! Created '{output_filename}'")
    print(f"Total Rows: {len(merged_df):,}")
    print(f"Location: {os.path.abspath(output_filename)}")
    print("="*50)



if __name__ == "__main__":
    run_smart_merge()
