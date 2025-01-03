# Final Class: From Sciserver to local machines

1. On Sciserver
- Create a file of YOUR environment:
    - In your paper directory
    - Create a folder: binder 
        ```
        mkdir binder
        cd binder
        ```
    - create the environment file: This will create a file with all installed packages
        ```
        conda env export --from-history -f environment.yml
        ```
    - get the specified versions:
      ```
        conda list | grep -E -i -w "^$(conda env export --no-builds --from-history | awk '$1 == "-"{ if (key == "dependencies:") print $NF; next } {key=$1}' | sed 's/=.*//' | tr -s '\r\n' '|' | sed 's/|$//')\s" | awk '{ print $1 "=" $2 }' | sed 's/^/  - /'
      ```
    - replace the packages with the list on your terminal.
    - delete line for jupyterlab-rise=0.42.0

- Adjust reproduce.sh (see [example](../../contrib/AMonninger/Paper_Restructured/reproduce.sh))
    - make sure to activate the kernel
    ```
    python -m ipykernel install --user --name econark
    ```
- Push changes on GitHub

2. On your laptop
- Get your fork
    - Create a folder structure (Github/GitHubID)
    - In that newly created folder:
    ```
    git clone https://github.com/GITHUBID/as.380.369
    ```
- Give permission to execute reproduce.sh (If you have a mac):
    - open a terminal and navigate to folder of your paper
    - ```ls -las``` (shows if it is executable)
    - ```chmod u+x reproduce.sh ```
    - ```ls -las```(reproduce.sh file should be green now)
- to get jupyterlab-rise working (for your slideshows):
    - ```conda uninstall httpx```
    - ```conda install "httpx<0.28.0```
    - ```jupyter lab```
    - once jupyter lab opens, click the extensions(puzzle piece) button on the left hand menu bar
    - type "rise" into the extensions search bar
    - install jupyterlab-rise
- run reproduce.sh

If you want to run your code without reproduce.sh
- Creat the environment (only need to do this once)
  ```
  conda env create -f ./binder/environment.yml
  ```
- Activate the environment:
  ```
  activate econark
  ```
- run myst start or just build the pdf
  ```
  # to start
  myst start
  # to build
  myst build --pdf
  ```
  

OPEN QUESTIONS:
- [x] how to get jupyterlab-rise=0.42.0
- Do we want to create the environment in reproduce.sh
  - If yes: Add to reproduce.sh:
    ```
    # Create the environment
    ml anaconda
    conda env update --file ./binder/environment.yml
    conda activate ./econark
    ```
  - if no: Add to list above:
    - Create your environment
      ```
      conda env create -f ./binder/environment.yml
      conda activate econark
      ```
