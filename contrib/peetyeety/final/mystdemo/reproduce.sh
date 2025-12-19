#!/bin/bash
# Reproduce the MyST research paper

echo "=== California Film Tax Credits Research Paper ==="
echo ""

# Check if myst is installed
if ! command -v myst &> /dev/null; then
    echo "MyST is not installed. Installing..."
    pip install mystmd
fi

# Build the site
echo "Building MyST site..."
myst build

# Build PDF (requires LaTeX)
echo ""
read -r -p "Do you want to build the PDF? (requires LaTeX) [y/n] " input
case $input in
    [yY][eE][sS]|[yY])
        echo "Building PDF..."
        myst build --pdf
        echo "PDF saved as California_Film_Tax_Credits_Peter_Li.pdf"
        ;;
    *)
        echo "Skipping PDF build."
        ;;
esac

# Start server
echo ""
read -r -p "Do you want to start the local server? [y/n] " input
case $input in
    [yY][eE][sS]|[yY])
        echo "Starting server at http://localhost:3000"
        myst start
        ;;
    *)
        echo "Done! Run 'myst start' to view the paper."
        ;;
esac
