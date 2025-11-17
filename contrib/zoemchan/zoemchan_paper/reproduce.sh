#!/bin/bash
# Create the environment
read -r -p "Do you want to create/update your environment? [y/n]" input

case $input in
    [yY][eE][sS]|[yY])
    conda env update --file ./binder/environment.yml 
    ;;
    [nN][oO]|[nN])
    echo "Environment will not be updated"
    ;;
    esac

# Activate environment
conda activate ./econ_ark
    
# Run the Jupyter notebook and execute all cells in place
python -m ipykernel install --user --name econark
jupyter nbconvert --to notebook --execute --inplace 04_dataanalysis.ipynb

# Build the PDF using myst
myst build --pdf
