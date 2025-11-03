# SEC Filing Date Extraction Fix

## Problem
The current date extraction logic isn't finding dates in the 2021-2025 range because:
1. Date extraction from tar filenames is failing (filename format variations)
2. Dates should be extracted from INSIDE tar files (from XBRL filenames) - more reliable

## Solution

### Key Insight
SEC filing tar files contain XBRL files with dates in their filenames, e.g.:
- `afrm-20201231.xsd` → date: 2020-12-31
- `afrm-20201231_htm.xml` → date: 2020-12-31

These are more reliable than parsing the tar filename itself.

### Implementation

Add this helper function to your notebook (before the main parsing loop):

```python
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
                dates_found.sort()
                filing_date = dates_found[-1]  # Most recent
                
                # Reporting date is often quarter-end (March, June, Sept, Dec)
                quarter_ends = [d for d in dates_found if d.month in [3, 6, 9, 12]]
                if quarter_ends:
                    reporting_date = quarter_ends[-1]
                else:
                    reporting_date = filing_date
            
            # Method 2: Fallback - extract from tar filename
            if filing_date is None:
                filename = Path(tar_path).stem
                
                # Pattern 1: 8-digit date anywhere (YYYYMMDD)
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
                        date_str_6 = filename[10:16]
                        year = 2000 + int(date_str_6[:2])
                        month = int(date_str_6[2:4])
                        day = int(date_str_6[4:6])
                        if 2000 <= year <= 2030 and 1 <= month <= 12 and 1 <= day <= 31:
                            filing_date = pd.to_datetime(f'{year}-{month:02d}-{day:02d}')
                            reporting_date = filing_date
                    except:
                        pass
    
    except Exception as e:
        pass
    
    return (filing_date, reporting_date)
```

### Updated Main Loop

Replace your existing `for tar_file in tar_files:` loop with:

```python
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
        # But limit to reasonable sample size
        if files_processed < 50:  # Process first 50 files if date unknown
            should_process = True
    
    if should_process:
        files_processed += 1
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
                if files_with_data % 5 == 0:
                    print(f"    → Extracted {files_with_data} quarters so far...")
```

## Why This Works

1. **Extracts dates from XBRL filenames inside tar**: More reliable than tar filename parsing
2. **Multiple fallback methods**: If one method fails, tries others
3. **Processes files even if date extraction fails**: Dates may be in XBRL facts, not filenames
4. **Better reporting date detection**: Identifies quarter-end dates

## Next Steps

1. **Add the helper function** to your notebook (before the parsing loop)
2. **Update the main loop** with the improved version
3. **Test on a few tickers** first to verify it's working
4. **Check Arelle installation**: Make sure Arelle is properly installed and `HAS_ARELLE = True`

## Additional Recommendations

Since you mentioned focusing on 2024-2025 data for research purposes:

1. **Use yfinance for recent quarters**: yfinance typically has 5-6 recent quarters (2024-2025)
2. **Supplement with SEC filings**: Use SEC filings to fill gaps or extend to 2021-2023 if needed
3. **Manual entry for key quarters**: For critical missing quarters, manual entry from SEC filings may be fastest

## Testing

After implementing, you should see output like:
```
AFRM: Processing 14 filings...
  ✓ SUCCESS: Extracted 12 quarters from 12/14 processed filings
     Date range: 2021-03-31 to 2025-06-30
```

If you're still seeing "No filings found in 2021-2025 date range", the issue is likely:
- Arelle not properly parsing XBRL (check `HAS_ARELLE` flag)
- XBRL facts not containing expected financial metrics
- Need to update concept names in XBRL extraction function

