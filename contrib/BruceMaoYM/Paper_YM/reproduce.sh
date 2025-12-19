#!/bin/bash
# Reproduction script for "Buy-Now-Pay-Later Stock Returns and Interest Rate Sensitivity"
# This script reproduces the complete analysis and builds the paper

set -e  # Exit on error

# Save the initial directory
INITIAL_DIR="$(pwd)"

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

# Check if we're already in the right environment
if [ -n "$CONDA_DEFAULT_ENV" ] && [ "$CONDA_DEFAULT_ENV" = "econark" ]; then
    echo "✓ Already in 'econark' environment"
else
    # Check if conda is available
    if ! command -v conda &> /dev/null; then
        echo "⚠️  Conda not found. Please ensure conda is installed and in your PATH."
        exit 1
    fi
    
    # Get conda base directory
    CONDA_BASE="$(conda info --base 2>/dev/null || echo "")"
    
    if [ -z "$CONDA_BASE" ]; then
        echo "⚠️  Could not determine conda base directory"
        exit 1
    fi
    
    # Source conda initialization script
    if [ -f "${CONDA_BASE}/etc/profile.d/conda.sh" ]; then
        source "${CONDA_BASE}/etc/profile.d/conda.sh"
    else
        echo "⚠️  Conda initialization script not found at ${CONDA_BASE}/etc/profile.d/conda.sh"
        echo "   Please ensure conda is properly installed."
        exit 1
    fi
    
    # Try to activate the environment
    if conda activate econark 2>/dev/null; then
        echo "✓ Activated 'econark' environment"
    else
        echo "⚠️  Could not activate environment. Please activate manually:"
        echo "   conda activate econark"
        echo "   Then run this script again."
        exit 1
    fi
fi

# Step 3: Install Jupyter kernel
echo ""
echo "Installing Jupyter kernel..."
python -m ipykernel install --user --name econark --display-name "Python (econark)" || {
    echo "⚠️  Kernel installation failed. Checking if it already exists..."
    if jupyter kernelspec list | grep -q econark; then
        echo "✓ Kernel 'econark' already exists"
    else
        echo "⚠️  Failed to install kernel"
        exit 1
    fi
}

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

if [ ! -f "04_dataanalysis.ipynb" ]; then
    echo "⚠️  ERROR: 04_dataanalysis.ipynb not found in current directory"
    echo "  Current directory: $(pwd)"
    echo "  Contents:"
    ls -la *.ipynb 2>/dev/null || echo "  No .ipynb files found"
    exit 1
fi

jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 04_dataanalysis.ipynb || {
    echo "⚠️  Error executing notebook. Check the output above for details."
    exit 1
}
echo "✓ Notebook executed successfully"

# Step 6: Build the paper
echo ""
echo "Building PDF..."

# Clean previous builds
rm -rf _build

# Check if myst is available
if ! command -v myst >/dev/null 2>&1; then
    echo "⚠️  ERROR: myst command not found in PATH"
    echo "  Installing mystmd..."
    pip install mystmd || {
        echo "⚠️  Failed to install mystmd"
        exit 1
    }
fi

echo "Running myst build (skipping notebook execution - using cached outputs)..."
myst build --pdf 2>&1 | tee /tmp/myst_build.log | grep -E "(Building|Rendering|Writing|Error|Warning|✓|✗|Exported|Created)" || true

# Wait for build to complete
sleep 2

# Find the build directory
BUILD_DIR=""
if [ -d "_build/temp" ]; then
    # Look for directory containing Paper_YM.tex
    for dir in _build/temp/*/; do
        if [ -f "${dir}Paper_YM.tex" ]; then
            BUILD_DIR="${dir%/}"  # Remove trailing slash
            break
        fi
    done
fi

if [ -z "$BUILD_DIR" ] || [ ! -d "$BUILD_DIR" ]; then
    echo "⚠️  Warning: Could not find build directory"
    echo "  Searched in: _build/temp/"
    echo "  Contents of _build/:"
    find _build -name "*.tex" -type f 2>/dev/null | head -10 || echo "  No .tex files found"
    exit 1
fi

echo "Build directory: $BUILD_DIR"

# Step 6a: Copy images to build directory
if ls chart_*.png 1> /dev/null 2>&1; then
    echo "  Copying chart images..."
    cp chart_*.png "$BUILD_DIR/" 2>/dev/null || {
        echo "  ⚠️  Warning: Failed to copy some images"
    }
    # Also copy to files/ subdirectory if it exists (myst sometimes uses this)
    if [ -d "$BUILD_DIR/files" ]; then
        cp chart_*.png "$BUILD_DIR/files/" 2>/dev/null || true
    fi
    IMAGE_COUNT=$(ls -1 "$BUILD_DIR"/chart_*.png 2>/dev/null | wc -l | tr -d ' ')
    echo "  ✓ Copied ${IMAGE_COUNT} images"
else
    echo "  ⚠️  No chart images found. Run notebooks first."
fi

# Copy references.bib for bibliography
if [ -f "references.bib" ]; then
    cp references.bib "$BUILD_DIR/" 2>/dev/null && echo "  ✓ Copied references.bib"
fi

# Change to build directory for LaTeX processing
cd "$BUILD_DIR" || {
    echo "⚠️  Failed to change to build directory: $BUILD_DIR"
    exit 1
}

# Step 6b: Fix LaTeX issues
echo "  Fixing LaTeX issues..."

# Add float package if not present
if ! grep -q '\\usepackage{float}' Paper_YM.tex; then
    # Use perl instead of sed for better cross-platform compatibility
    perl -i -pe 's/\\usepackage{graphicx}/\\usepackage{graphicx}\n\\usepackage{float}/' Paper_YM.tex
fi

# Fix various LaTeX issues using Python (more reliable than sed)
python3 << 'PYTHONFIX'
import re
import glob
import sys

def fix_latex_issues(content):
    """Fix various LaTeX compilation issues."""
    
    # Fix figure/table placements
    content = re.sub(r'\\begin\{figure\}(\[.*?\])?', r'\\begin{figure}[H]', content)
    content = re.sub(r'\\begin\{table\}(\[.*?\])?', r'\\begin{table}[H]', content)
    content = re.sub(r'\[H\]\[H\]', '[H]', content)
    
    # Fix unicode characters
    content = content.replace('✓', '\\checkmark ')
    
    # Remove raw latex markers
    content = re.sub(r'```\{raw\} latex\s*\n', '', content)
    content = re.sub(r'```\s*\n', '', content)
    
    # Fix figure references
    content = re.sub(
        r'`` `\{raw\} latex Figure~\\ref\{fig:([^}]+)\} ` ``',
        r'Figure~\\ref{fig:\1}',
        content
    )
    
    # Remove excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove problematic \newpage\FloatBarrier combinations
    content = re.sub(r'\\newpage\s*\\FloatBarrier\s*', '\n', content)
    content = re.sub(r'\\FloatBarrier\s*\n', '\n', content)
    
    return content

def fix_centering_in_tables(content):
    """Remove invalid \centering commands from table cells."""
    lines = content.split('\n')
    new_lines = []
    in_tabular = False
    tabular_depth = 0
    
    for line in lines:
        if '\\begin{tabular' in line:
            in_tabular = True
            tabular_depth += 1
        elif '\\end{tabular' in line:
            tabular_depth -= 1
            if tabular_depth == 0:
                in_tabular = False
        
        if in_tabular and tabular_depth > 0:
            # Remove \centering from table cells
            line = re.sub(r'\\centering\s+', '', line)
            line = re.sub(r'&\s*\\centering\s+', '& ', line)
            line = re.sub(r'^\\centering\s+', '', line)
            line = re.sub(r'\\centering\s+\\\\', '\\\\', line)
        
        new_lines.append(line)
    
    return '\n'.join(new_lines)

def fix_missing_figure_labels(content):
    """Fix missing figure labels that are referenced but not defined."""
    # Fix fig_volatility label - check if referenced but not labeled
    if '\\ref{fig_volatility}' in content and '\\label{fig_volatility}' not in content:
        # Pattern to find figure with chart_l_volatility that doesn't have the label
        # Look for the specific pattern: \includegraphics with chart_l_volatility followed by \end{figure} without a label in between
        pattern = r'(\\includegraphics\[[^\]]*\]\{[^}]*chart_l_volatility[^}]*\})\s*(\\end\{figure\})'
        replacement = r'\1\n\\caption[]{Volatility Comparison}\n\\label{fig_volatility}\n\2'
        content = re.sub(pattern, replacement, content)
    
    return content

def ensure_single_bibliography(content, filename):
    """Ensure only one bibliography appears."""
    # For the bibliography section file: add bibliography command if missing
    if 'bibliography.tex' in filename:
        if '\\bibliography' not in content and '\\section{References}' in content:
            content = content.replace(
                '\\section{References}',
                '\\section{References}\n\\bibliographystyle{plainnat}\n\\bibliography{references}'
            )
    # For the main Paper_YM.tex file: remove auto-generated bibliography commands
    elif filename == 'Paper_YM.tex':
        # Remove auto-generated \bibliography and \bibliographystyle commands
        content = re.sub(r'\\bibliographystyle\{[^}]+\}\s*\n', '', content)
        content = re.sub(r'\\bibliography\{[^}]+\}\s*\n', '', content)
    
    return content

# Process all .tex files
for tex_file in glob.glob('Paper_YM*.tex'):
    try:
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        content = fix_latex_issues(content)
        content = fix_centering_in_tables(content)
        content = fix_missing_figure_labels(content)
        content = ensure_single_bibliography(content, tex_file)
        
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Fixed {tex_file}")
    except Exception as e:
        print(f"  ⚠️  Warning: Could not process {tex_file}: {e}")
        sys.exit(1)
PYTHONFIX

echo "  ✓ LaTeX issues fixed"

# Step 6c: Compile PDF
if ! command -v pdflatex >/dev/null 2>&1; then
    echo "  ⚠️  ERROR: pdflatex not found"
    echo "  Please install a LaTeX distribution:"
    echo "    - macOS: brew install --cask mactex"
    echo "    - Linux: sudo apt-get install texlive-full"
    echo "    - Windows: Install MiKTeX or TeX Live"
    cd "$INITIAL_DIR"
    exit 1
fi

echo "  Compiling PDF..."

# Try xelatex first (myst uses this), fall back to pdflatex
if command -v xelatex >/dev/null 2>&1; then
    echo "  Using xelatex (recommended for myst builds)..."
    for pass in 1 2; do
        echo "  Running xelatex (pass $pass)..."
        if ! xelatex -interaction=nonstopmode Paper_YM.tex > "/tmp/xelatex${pass}.log" 2>&1; then
            echo "  ⚠️  Pass $pass had warnings/errors"
            grep -i "error" "/tmp/xelatex${pass}.log" | head -10 || true
        fi
    done
elif command -v pdflatex >/dev/null 2>&1; then
    echo "  Using pdflatex (fallback)..."
    for pass in 1 2; do
        echo "  Running pdflatex (pass $pass)..."
        if ! pdflatex -interaction=nonstopmode Paper_YM.tex > "/tmp/pdflatex${pass}.log" 2>&1; then
            echo "  ⚠️  Pass $pass had warnings/errors"
            grep -i "error" "/tmp/pdflatex${pass}.log" | head -10 || true
        fi
    done
else
    echo "  ⚠️  ERROR: Neither xelatex nor pdflatex found"
    echo "  Please install a LaTeX distribution"
    cd "$INITIAL_DIR"
    exit 1
fi

# Check if PDF was created successfully
if [ -f "Paper_YM.pdf" ]; then
    PDF_SIZE=$(stat -f%z Paper_YM.pdf 2>/dev/null || stat -c%s Paper_YM.pdf 2>/dev/null || echo "0")
    
    if [ "${PDF_SIZE:-0}" -lt 50000 ]; then
        echo "  ⚠️  PDF seems incomplete (size: $PDF_SIZE bytes)"
        echo "  Check logs: /tmp/pdflatex*.log"
        cd "$INITIAL_DIR"
        exit 1
    fi
    
    # Copy PDF to initial directory
    cp Paper_YM.pdf "$INITIAL_DIR/"
    cd "$INITIAL_DIR"
    
    echo "  ✓ PDF created successfully ($(ls -lh Paper_YM.pdf | awk '{print $5}'))"
else
    echo "  ⚠️  PDF not created. Check logs: /tmp/pdflatex*.log"
    cd "$INITIAL_DIR"
    exit 1
fi

echo ""
echo "======================================================================"
echo "✓ REPRODUCTION COMPLETE!"
echo "======================================================================"
echo ""
echo "Output: Paper_YM.pdf"
echo ""