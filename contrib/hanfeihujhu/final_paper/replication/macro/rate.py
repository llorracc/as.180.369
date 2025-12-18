import pandas as pd


def scrape_fed_funds():
    # URL for Daily Federal Funds Rate (DFF) from St. Louis Fed
    # Use 'FEDFUNDS' instead of 'DFF' if you want monthly averages
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF"

    print(f"Downloading data from {url}...")

    try:
        # Read CSV directly from the URL
        df = pd.read_csv(url)

        # Rename columns as requested
        df.columns = ['date', 'rate']

        # Convert date column to datetime objects for filtering
        df['date'] = pd.to_datetime(df['date'])

        # Filter for dates starting from 1982-01-01
        df = df[df['date'] >= '1976-01-01']

        # Save to CSV without the index number
        output_file = 'fed_funds.csv'
        df.to_csv(output_file, index=False)

        print(f"Success! Saved {len(df)} rows to {output_file}")
        print(f"Range: {df['date'].min().date()} to {df['date'].max().date()}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    scrape_fed_funds()
