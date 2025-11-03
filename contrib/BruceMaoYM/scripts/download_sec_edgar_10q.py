"""
SEC EDGAR 10-Q Data Download Script
====================================

This script downloads 10-Q quarterly filings from SEC EDGAR using the datamule library.
Files are downloaded locally for potential parsing and analysis.

Usage:
    python download_sec_edgar_10q.py
    
    Or import in notebook:
    from download_sec_edgar_10q import download_edgar_filings
    
    tickers = ['AFRM', 'SOFI', 'UPST']
    results = download_edgar_filings(tickers)

Method: datamule Portfolio API
- Installation: pip install datamule
- API: Portfolio(company_name).download_submissions(ticker='...', submission_type='10-Q')
"""

import time
import os
from typing import List, Dict, Optional


def download_edgar_filings(
    tickers: List[str],
    company_names: Optional[Dict[str, str]] = None,
    max_companies: Optional[int] = None,
    date_start: Optional[str] = None,
    skip_if_exists: bool = True
) -> Dict[str, Dict]:
    """
    Download SEC EDGAR 10-Q filings for specified tickers.
    
    Parameters:
    -----------
    tickers : List[str]
        List of stock ticker symbols to download filings for
    company_names : Dict[str, str], optional
        Mapping of ticker to company name (for datamule lookup)
        If None, uses default mapping
    max_companies : int, optional
        Maximum number of companies to download (for testing)
    date_start : str, optional
        Start date for filtering (if datamule supports it)
        Format: 'YYYY-MM-DD'
    skip_if_exists : bool
        If True, skip companies that already have downloaded files
        
    Returns:
    --------
    Dict[str, Dict]
        Dictionary with ticker as key and status info as value
    """
    print("=" * 80)
    print("SEC EDGAR DATA EXTRACTION (datamule)")
    print("=" * 80)
    print("\n⚠ NOTE: This section is OPTIONAL. The analysis works fine with yfinance data only.")
    print("   Set max_companies=0 to skip all downloads.\n")
    
    # Check if we should skip
    if max_companies == 0:
        print("⏭ Skipping SEC EDGAR download (max_companies=0)")
        print("   Analysis will proceed with yfinance data only")
        return {}
    
    # Import datamule
    USE_DATAMULE = False
    try:
        from datamule import Portfolio
        USE_DATAMULE = True
        print("✓ datamule library found")
    except ImportError:
        print("⚠ datamule not installed")
        print("  Installing datamule...")
        try:
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", "datamule", "-q"])
            from datamule import Portfolio
            USE_DATAMULE = True
            print("✓ Installation complete - datamule ready")
        except Exception as e:
            print(f"  datamule installation failed: {str(e)[:50]}")
            USE_DATAMULE = False
            return {}
    
    # Default company name mapping
    if company_names is None:
        company_names = {
            'AFRM': 'affirm holdings',
            'SEZL': 'sezzle',
            'SQ': 'block',
            'PYPL': 'paypal holdings',
            'KLAR': 'klarna',
            'SOFI': 'sofi technologies',
            'UPST': 'upstart',
            'LC': 'lendingclub',
            'COF': 'capital one',
            'DFS': 'discover financial',
            'SYF': 'synchrony financial',
            'AXP': 'american express'
        }
    
    # Limit downloads if specified
    if max_companies is not None and max_companies > 0:
        tickers = tickers[:max_companies]
        print(f"⚠ Limiting to first {max_companies} companies")
    
    if date_start:
        print(f"⚠ Date filter: {date_start} onwards (may not be supported by datamule)")
    
    print(f"\nDownloading 10-Q filings for {len(tickers)} companies...\n")
    print("Note: If '0 submissions' appears, this may be due to:")
    print("  - SEC EDGAR system issues (check SEC.gov status)")
    print("  - Company name matching issues")
    print("  - The analysis will proceed with yfinance data if EDGAR fails\n")
    
    edgar_filings = {}
    successful_fetches = 0
    
    if USE_DATAMULE:
        for idx, ticker in enumerate(tickers):
            # Skip if already downloaded
            if skip_if_exists:
                download_dir = f"./datamule/{ticker}/10-Q"
                if os.path.exists(download_dir) and len(os.listdir(download_dir)) > 0:
                    file_count = len([f for f in os.listdir(download_dir) 
                                     if os.path.isfile(os.path.join(download_dir, f))])
                    if file_count > 0:
                        print(f"  {ticker}: Already downloaded ({file_count} filings) - skipping")
                        edgar_filings[ticker] = {
                            'status': 'already_exists',
                            'count': file_count
                        }
                        successful_fetches += 1
                        continue
            
            print(f"  {ticker}: Downloading 10-Q filings...", end=" ")
            try:
                # Try using ticker directly first (more reliable)
                portfolio = Portfolio(ticker)
                
                # Try to limit date range - check if datamule supports date filtering
                try:
                    if date_start:
                        result = portfolio.download_submissions(
                            ticker=ticker,
                            submission_type='10-Q',
                            start_date=date_start  # May not be supported
                        )
                    else:
                        result = portfolio.download_submissions(
                            ticker=ticker,
                            submission_type='10-Q'
                        )
                except TypeError:
                    # If date filtering not supported, download all
                    result = portfolio.download_submissions(
                        ticker=ticker,
                        submission_type='10-Q'
                    )
                    if not date_start:
                        print(f"[Note: All historical filings - may be many files]", end=" ")
                
                # Check if files were actually downloaded
                download_dir = f"./datamule/{ticker}/10-Q"
                if os.path.exists(download_dir):
                    file_count = len([f for f in os.listdir(download_dir) 
                                     if os.path.isfile(os.path.join(download_dir, f))])
                    if file_count > 0:
                        edgar_filings[ticker] = {
                            'status': 'downloaded_via_datamule',
                            'count': file_count
                        }
                        print(f"✓ ({file_count} filings)")
                        successful_fetches += 1
                        
                        # Warn if too many files
                        if file_count > 20:
                            print(f"      ⚠ Warning: {file_count} files downloaded - this may take a while")
                    else:
                        # Try alternative: use company name if ticker doesn't work
                        company_name = company_names.get(ticker, ticker.lower())
                        portfolio_alt = Portfolio(company_name)
                        portfolio_alt.download_submissions(ticker=ticker, submission_type='10-Q')
                        
                        if os.path.exists(download_dir):
                            file_count = len([f for f in os.listdir(download_dir) 
                                             if os.path.isfile(os.path.join(download_dir, f))])
                            if file_count > 0:
                                edgar_filings[ticker] = {
                                    'status': 'downloaded_via_datamule',
                                    'count': file_count
                                }
                                print(f"✓ ({file_count} filings)")
                                successful_fetches += 1
                            else:
                                print(f"⚠ (0 submissions found)")
                        else:
                            print(f"⚠ (directory not created)")
                else:
                    print(f"⚠ (directory not created)")
                
                time.sleep(1.0)  # Rate limiting - increased to avoid SEC throttling
                
            except KeyboardInterrupt:
                print("\n\n⚠ Download interrupted by user")
                print("   To continue later, re-run this script")
                break
            except Exception as e:
                error_msg = str(e)
                print(f"✗ Error: {error_msg[:60]}")
                edgar_filings[ticker] = {'status': 'error', 'error': error_msg[:60]}
        
        if successful_fetches > 0:
            print(f"\n✓ Downloaded 10-Q filings using datamule for {successful_fetches} companies")
            print("  Files saved locally")
        else:
            print("\n⚠ No filings downloaded via datamule")
    else:
        print("\n⚠ datamule not available - skipping SEC EDGAR download")
    
    print("\n" + "=" * 80)
    print("SEC EDGAR DATA EXTRACTION SUMMARY")
    print("=" * 80)
    if successful_fetches > 0:
        print(f"✅ SUCCESS: datamule downloaded 10-Q filings for {successful_fetches} companies")
        print("  Files saved locally - can be parsed for financial data")
    else:
        print("⚠ datamule not available or no filings downloaded")
        print("  Analysis will proceed with yfinance data only")
    print("=" * 80)
    
    return edgar_filings


def main():
    """Main function for standalone execution."""
    # Default tickers from the research
    default_tickers = [
        'AFRM', 'SEZL', 'SQ', 'PYPL', 'KLAR',  # BNPL firms
        'SOFI', 'UPST', 'LC',  # Traditional fintech
        'COF', 'DFS', 'SYF', 'AXP'  # Credit card companies
    ]
    
    # Configuration
    MAX_COMPANIES_TO_DOWNLOAD = 3  # Set to None to download all, or 0 to skip
    DATE_START = '2021-01-01'  # Only download filings from this date onwards
    
    print("\n" + "=" * 80)
    print("SEC EDGAR Download Script - Standalone Execution")
    print("=" * 80)
    print(f"\nConfiguration:")
    print(f"  Tickers: {len(default_tickers)} companies")
    print(f"  Max companies: {MAX_COMPANIES_TO_DOWNLOAD if MAX_COMPANIES_TO_DOWNLOAD else 'All'}")
    print(f"  Date start: {DATE_START}")
    print("\nTo modify, edit the main() function or call download_edgar_filings() directly\n")
    
    results = download_edgar_filings(
        tickers=default_tickers,
        max_companies=MAX_COMPANIES_TO_DOWNLOAD,
        date_start=DATE_START
    )
    
    print(f"\n✓ Download complete. Results: {len(results)} companies processed")


if __name__ == "__main__":
    main()

