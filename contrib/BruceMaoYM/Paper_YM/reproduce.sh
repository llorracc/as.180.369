#!/bin/bash
# Reproduction script for "Buy-Now-Pay-Later Stock Returns and Interest Rate Sensitivity"
# This script reproduces the complete analysis and builds the paper

set -e  # Exit on error

echo "=" | tr -d '\n'
echo "======================================================================"
echo "REPRODUCING ANALYSIS: BNPL Interest Rate Sensitivity"
echo "======================================================================"
echo ""

# Step 1: Environment setup
read -r -p "Do you want to create/update your conda environment? [y/n] " input

case $input in
    [yY][eE][sS]|[yY])
    echo ""
    echo "Creating/updating conda environment from binder/environment.yml..."
    conda env update --file ./binder/environment.yml --prune
    echo "✓ Environment updated"
    ;;
    [nN][oO]|[nN])
    echo "Skipping environment update (assuming environment already exists)"
    ;;
    *)
    echo "Invalid input. Skipping environment update."
    ;;
esac

# Step 2: Activate environment
echo ""
echo "Activating conda environment 'econark'..."
echo "Note: If activation fails, you may need to run: conda activate econark"
conda activate econark || {
    echo "⚠️  Could not activate environment. Please activate manually:"
    echo "   conda activate econark"
    echo "   Then run this script again or continue manually."
    exit 1
}

# Step 3: Install Jupyter kernel
echo ""
echo "Installing Jupyter kernel..."
python -m ipykernel install --user --name econark || echo "⚠️  Kernel installation warning (may already exist)"

# Step 4: Check for FRED API key
echo ""
if [ -z "$FRED_API_KEY" ]; then
    echo "⚠️  FRED_API_KEY environment variable not set."
    echo ""
    echo "The analysis requires a free FRED API key from the Federal Reserve."
    echo "To get your API key:"
    echo "  1. Visit: https://fred.stlouisfed.org/docs/api/api_key.html"
    echo "  2. Register for a free account (if needed)"
    echo "  3. Create an API key"
    echo ""
    read -r -p "Do you have a FRED API key? [y/n] " has_key
    
    if [[ $has_key =~ ^[Yy]$ ]]; then
        echo ""
        read -r -p "Please enter your FRED API key: " api_key
        if [ -n "$api_key" ]; then
            export FRED_API_KEY="$api_key"
            echo "✓ FRED_API_KEY set for this session"
            echo "  (To make it permanent, add to your ~/.bashrc or ~/.zshrc:)"
            echo "  export FRED_API_KEY='$api_key'"
        else
            echo "⚠️  No API key provided. Exiting."
            exit 1
        fi
    else
        echo ""
        echo "Please get a FRED API key first:"
        echo "  https://fred.stlouisfed.org/docs/api/api_key.html"
        echo ""
        echo "Then run this script again and enter your key when prompted."
        exit 1
    fi
else
    echo "✓ FRED_API_KEY is set"
fi

# Step 5: Execute data analysis notebook
echo ""
echo "Executing data analysis notebook (04_dataanalysis.ipynb)..."
echo "This may take several minutes as it downloads data and runs all analyses..."
jupyter nbconvert --to notebook --execute --inplace 04_dataanalysis.ipynb || {
    echo "⚠️  Error executing notebook. Check the output above for details."
    exit 1
}
echo "✓ Notebook executed successfully"

# Step 6: Build the paper
echo ""
echo "Building PDF and HTML versions of the paper..."
myst build --pdf --html || {
    echo "⚠️  Error building paper. Check the output above for details."
    exit 1
}
echo "✓ Paper built successfully"

# Step 7: Summary
echo ""
echo "======================================================================"
echo "✓ REPRODUCTION COMPLETE!"
echo "======================================================================"
echo ""
echo "Output files:"
echo "  PDF: Paper_YM.pdf"
echo "  HTML: _build/site/index.html"
echo ""
echo "To preview the HTML website locally, run:"
echo "  myst start"
echo ""
echo "All analysis results are in: 04_dataanalysis.ipynb"
echo ""

