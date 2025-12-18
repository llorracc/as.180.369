#!/bin/bash  # Use the Bash shell to run this script
# Create the environment
read -r -p "Do you want to create/update your environment? [y/n]" input # Read user input safely (-r) and show prompt (-p)

# Check user response and run the appropriate command
case $input in
    [yY][eE][sS]|[yY])  # Match "yes" in any capitalization or a single "y"
    conda env update --file ./binder/environment.yml   # Update/create the conda environment using this YAML file
        ;;
    ;;
    [nN][oO]|[nN])  # Match "no" in any capitalization or a single "n"
    echo "Environment will not be updated" # Display message if user chooses no
    ;;
    esac

# Activate environment
conda activate ./econ_ark
    
# Run the Jupyter notebook and execute all cells in place # Register this environment as a Jupyter kernel named "econark"
python -m ipykernel install --user --name econark
jupyter nbconvert --to notebook --execute --inplace 04_dataanalysis.ipynb

# Build the PDF using myst
myst build --pdf
