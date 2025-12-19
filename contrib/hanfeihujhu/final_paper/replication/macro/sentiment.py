import os
import glob
import pandas as pd
import pysentiment2 as ps

# 1. Setup
# Folder containing the text meetings. We try common locations so the script works
# whether you generated files with fomc3.py (meetings_txt_all) or an earlier step (meetings_txt).
candidate_dirs = [
    'fomc_data/processed/meetings_txt_all',
    'fomc_data/processed/meetings_txt',
    '/Users/hfh/Downloads/meetings_txt',  # fallback to absolute path if used elsewhere
]
folder_path = next((d for d in candidate_dirs if os.path.isdir(d)), candidate_dirs[0])
lm = ps.LM()  # Initialize the Financial Dictionary
results = []

# 2. The Loop
# glob.glob grabs all .txt files in the folder
file_list = glob.glob(os.path.join(folder_path, "*.txt"))
if not file_list:
    raise FileNotFoundError(
        f"No .txt files found in '{folder_path}'. "
        "Check the path or run fomc3.py to generate the meeting text files."
    )

print(f"Found {len(file_list)} files. Starting analysis...")

for file_path in file_list:
    try:
        # Get filename (e.g., "meeting_1976-03-29.txt")
        filename = os.path.basename(file_path)

        # Extract Date from filename
        # Assumes format "meeting_YYYY-MM-DD.txt"
        date_str = filename.replace('meeting_', '').replace('.txt', '')

        # Read the text file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

        # 3. Analyze Sentiment
        tokens = lm.tokenize(text)
        score = lm.get_score(tokens)

        # Calculate Net Sentiment: (Pos - Neg) / (Pos + Neg)
        net_sentiment = score['Polarity']

        # Store data
        results.append({
            'date': date_str,
            'net_sentiment': net_sentiment,
            'positive_count': score['Positive'],
            'negative_count': score['Negative'],
            'word_count': len(tokens),
            'filename': filename
        })

    except Exception as e:
        print(f"Error reading {filename}: {e}")

# 4. Save Results
df = pd.DataFrame(results)

# Convert 'date' column to actual datetime objects for sorting/merging later
if df.empty:
    raise ValueError("No sentiment results produced; verify the input files.")

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

print("Analysis Complete.")
print(df.head())

# Save to CSV for the next step of your paper
output_csv = 'fomc_sentiment_data.csv'
df.to_csv(output_csv, index=False)
print(f"Saved results to {output_csv}")
