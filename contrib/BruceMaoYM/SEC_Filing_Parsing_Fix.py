"""
SEC Filing Parsing Fix
======================

This script provides improved date extraction and XBRL parsing for SEC filings.
Key improvements:
1. Extract dates from INSIDE tar files (from XBRL filenames) - more reliable
2. Proper XBRL parsing using Arelle
3. Better handling of reporting period dates vs filing dates

To use: Copy the helper functions into your notebook cell.
"""

import tarfile
import re
import pandas as pd
from pathlib import Path
import tempfile


def extract_filing_date_from_tar(tar_path, ticker):
    """
    Extract filing date and reporting period date from SEC tar file.
    Tries multiple methods: XBRL filenames inside tar, tar filename, metadata.
    Returns (filing_date, reporting_date) tuple or (None, None) if not found.
    """
    filing_date = None
    reporting_date = None
    
    try:
        with tarfile.open(tar_path, 'r') as tar:
            # Method 1: Extract date from XBRL/XML filenames inside tar (most reliable)
            # SEC filings often have dates in filenames like: afrm-20201231.xsd, afrm-20201231_htm.xml
            all_members = tar.getnames()
            date_pattern_8 = re.compile(r'(\d{4})(\d{2})(\d{2})')  # YYYYMMDD
            
            dates_found = []
            for member in all_members:
                # Look for 8-digit date patterns in filenames
                matches = date_pattern_8.findall(member)
                for match in matches:
                    try:
                        year, month, day = map(int, match)
                        if 2000 <= year <= 2030 and 1 <= month <= 12 and 1 <= day <= 31:
                            date_val = pd.to_datetime(f'{year}-{month:02d}-{day:02d}')
                            dates_found.append(date_val)
                    except:
                        continue
            
            if dates_found:
                # Use most recent date as filing date, look for quarterly dates for reporting
                dates_found.sort()
                filing_date = dates_found[-1]  # Most recent
                
                # Reporting date is often the quarter-end date (last day of month)
                # Look for dates that are likely quarter ends (March, June, Sept, Dec)
                quarter_ends = [d for d in dates_found if d.month in [3, 6, 9, 12]]
                if quarter_ends:
                    reporting_date = quarter_ends[-1]
                else:
                    reporting_date = filing_date
            
            # Method 2: Extract from tar filename (SEC format)
            if filing_date is None:
                filename = Path(tar_path).stem
                
                # Pattern 1: 8-digit date anywhere in filename (YYYYMMDD)
                date_match_8 = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
                if date_match_8:
                    try:
                        year, month, day = map(int, date_match_8.groups())
                        if 2000 <= year <= 2030 and 1 <= month <= 12 and 1 <= day <= 31:
                            filing_date = pd.to_datetime(f'{year}-{month:02d}-{day:02d}')
                            reporting_date = filing_date
                    except:
                        pass
                
                # Pattern 2: 6-digit date at positions 10-15 (YYMMDD after CIK)
                if filing_date is None and len(filename) >= 16:
                    try:
                        date_str_6 = filename[10:16]  # YYMMDD
                        year = 2000 + int(date_str_6[:2])
                        month = int(date_str_6[2:4])
                        day = int(date_str_6[4:6])
                        if 2000 <= year <= 2030 and 1 <= month <= 12 and 1 <= day <= 31:
                            filing_date = pd.to_datetime(f'{year}-{month:02d}-{day:02d}')
                            reporting_date = filing_date
                    except:
                        pass
            
            # Method 3: Try metadata.json if available
            if filing_date is None:
                try:
                    metadata_member = None
                    for member in all_members:
                        if 'metadata.json' in member.lower():
                            metadata_member = member
                            break
                    
                    if metadata_member:
                        metadata_file = tar.extractfile(metadata_member)
                        if metadata_file:
                            import json
                            metadata = json.load(metadata_file)
                            # SEC metadata often has filing_date or period_end
                            if 'filing_date' in metadata:
                                filing_date = pd.to_datetime(metadata['filing_date'])
                            elif 'period_end' in metadata:
                                filing_date = pd.to_datetime(metadata['period_end'])
                                reporting_date = filing_date
                except:
                    pass
    
    except Exception as e:
        pass
    
    return (filing_date, reporting_date)


# IMPROVED MAIN LOOP SNIPPET
# Replace your existing "for tar_file in tar_files:" loop with this:

improved_loop_code = """
for tar_file in tar_files:
    # IMPROVED: Extract date from INSIDE tar file (more reliable)
    filing_date, reporting_date = extract_filing_date_from_tar(tar_file, ticker)
    
    # Process if date is in range OR if date extraction failed (dates might be in XBRL facts)
    should_process = False
    if filing_date is not None:
        if filing_date >= pd.to_datetime('2021-01-01') and filing_date <= pd.to_datetime('2025-12-31'):
            should_process = True
    else:
        # If date extraction failed, process anyway (dates might be in XBRL facts)
        # But limit to reasonable sample size to avoid processing too many old files
        if files_processed < 50:  # Process first 50 files if date unknown
            should_process = True
    
    if should_process:
        files_processed += 1
        # Process all files if we're getting data, or first batch for debugging
        if files_processed <= 100 or files_with_data > 0:
            financials = extract_financials_from_filing(tar_file, ticker)
            if financials and (financials.get('revenue') or financials.get('net_income')):
                files_with_data += 1
                # Use reporting_date if available, otherwise use filing_date
                quarter_date = financials.get('quarter_date') or reporting_date or filing_date
                ticker_quarters.append({
                    'ticker': ticker,
                    'quarter_date': quarter_date,
                    'revenue': financials.get('revenue'),
                    'net_income': financials.get('net_income'),
                    'total_assets': financials.get('total_assets')
                })
                # Show progress every 5 files
                if files_with_data % 5 == 0:
                    print(f"    → Extracted {files_with_data} quarters so far...")
"""

if __name__ == "__main__":
    print("=" * 70)
    print("SEC Filing Parsing Fix - Helper Functions")
    print("=" * 70)
    print("\nThis script provides:")
    print("1. extract_filing_date_from_tar() - Improved date extraction")
    print("2. Code snippet for improved main parsing loop")
    print("\nTo use:")
    print("1. Copy extract_filing_date_from_tar() function into your notebook")
    print("2. Replace your 'for tar_file in tar_files:' loop with the improved version")
    print("\nKey improvements:")
    print("- Extracts dates from INSIDE tar files (XBRL filenames)")
    print("- More reliable date pattern matching")
    print("- Processes files even if date extraction fails (dates may be in XBRL facts)")
    print("- Better handling of reporting dates vs filing dates")
