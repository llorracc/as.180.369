#!/bin/bash
# Export notebook to HTML with code cells hidden

jupyter nbconvert --to html \
    --no-input \
    --output-dir=. \
    Notebooks/02_BNPL_Interest_Rate_Analysis.ipynb

echo "✓ HTML exported with code hidden"
echo "Open: 02_BNPL_Interest_Rate_Analysis.html"
