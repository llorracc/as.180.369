#!/bin/bash
'''

BEFORE RUNNING

Download newraw and oldraw from 

Place the unzipped folders into replication/bank code.

place (new_bank_data.py) into replication/bank code/newraw
place (old_bank_data.py) into replication/bank code/oldraw

'''

# Exit immediately if a command exits with a non-zero status
set -e

echo "--- Starting Reproduction Pipeline ---"

# ==========================================
# 1. Bank Data Processing
# ==========================================
echo "[1/4] Processing Bank Data..."

# Process New Raw Data
cd "bank code/newraw"
python new_bank_data.py
mv NEW_RAW_BANK_DATA.csv ../
cd .. # Moves to 'bank code'

# Process Old Raw Data
cd "oldraw"
python old_bank_data.py
mv OLD_RAW_BANK_DATA.csv ../
cd .. # Moves to 'bank code'

# Merge Bank Data
# Now inside 'bank code' with both CSVs present
python merge_bank.py
mv ALL_BANKS_MERGED.csv ../
cd .. # Moves back to root 'replication' folder

# ==========================================
# 2. Macro Data Processing
# ==========================================
echo "[2/4] Processing Macro Data..."

cd macro
python data_fomc.py
python rate.py
python sentiment.py

# Move outputs to root
mv fomc_sentiment_data.csv ../
mv fed_funds.csv ../
cd .. # Moves back to root 'replication' folder

# ==========================================
# 3. Final Dataset Merge
# ==========================================
echo "[3/4] Running Final Merge..."

# Root now contains: fed_funds.csv, fomc_sentiment_data.csv, ALL_BANKS_MERGED.csv
python merge.py

# ==========================================
# 4. Build Paper
# ==========================================

echo "[4/4] Building PDF with MyST..."

cd ..

myst build --pdf


echo "--- Reproduction Complete ---"