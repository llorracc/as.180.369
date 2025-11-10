# “The Presentation”

## Overview

## Class 12

**[Homework from previous class](https://github.com/llorracc/as.180.369/tree/main/materials/submission)**

**Agenda**
- Discussion of individual presentations (10 min ea).
- Present your final (LitMap)
- Tips & tricks for slideshow presenting.
- reproduce.sh Q&A
- Updating GitHub

- - Discuss reproducibility.
    - Results need to be generated within your notebook
        - (or as a consequence of executing your notebook).
    - Single script should reproduce all outputs: `reproduce.sh`
    - "It works on my computer!" → reproducibility with binder.
        - There different version of python
        - different versions of packages we use (pandas, etc.)
        - mybinder is a tool that we can specify the specific versions of these
          things and generate a link that some one can click on and open a
          notebook with these things installed.
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
        - replace the packages with the list on your terminal 
    - Create a reproduce.sh file:
        - copy and paste the file from [AMonninger](../../contrib/AMonninger/Paper_Restructured)
        - Replace jupyter notebook names with the file names of your paper
        - give the script permission to be executable using your terminal
          - ```ls -las``` (shows if it is executable)
          - ```chmod u+x reproduce.sh ```
          - ```ls -las```(reproduce.sh file should be green now)
        - run the file using
            ```/bin/bash reproduce.sh```
        - NOTE: I build the paper using myst and save it as a pdf. To specify options here, adjust your [myst.yml](../../contrib/AMonninger/Paper_Restructured/myst.yml) file
    - Sync your GitHub fork to assure that binder can access all information



# Homework
- If you are a Windows user, install the Windows Subsystem for Linux(WSL)
- Then, for all(Mac and WSL) install Miniconda from the Miniconda website (if using WSL, install inside WSL)
- Work on Presentations: Don't just make them a paraphrased version of your paper! (feel free to see the template linked [here](https://github.com/llorracc/as.180.369/blob/main/contrib/Beyond_the_Streetlight.ipynb)
- # Final Paper deadline moved to Friday December 6
  - Make sure to increase the number of papers you're citing to ~15 or more
  - Be sure to run your final paper through ChatGPT/AI multiple times before submitting

## Class 13

**Agenda**
- Presentations
    - Students will present (15 mins.) on their papers.
    - Include polished visuals to help convey your assertions.
    - 10 minutes per student + 5 min Q&A + 5 min allocation (×7 students = 140 min)

- Set computers up for miniconda.
    - Windows WSL https://learn.microsoft.com/en-us/windows/wsl/install 
    - Miniconda: https://docs.conda.io/projects/miniconda/en/latest/

- Prepare your sciserver Fork:
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

- On your laptop
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
    - run reproduce.sh
    - to get jupyterlab-rise working (for your slideshows):
        ```
        conda uninstall httpx
        conda install httpx<0.28.0
        jupyter lab
        ```
        - once jupyter lab opens, click the extensions(puzzle piece) button on the left hand menu bar
        - type "rise" into the extensions search bar
        - install jupyterlab-rise

If you want to run your code without reproduce.sh
- Creat the environment (only need to do this once):
  ```
  conda env create -f ./binder/environment.yml
  ```
- Activate the environment (Do this everytime you start a new terminal):
  ```
  activate econark
  ```
- to get jupyterlab-rise working (for your slideshows, only need to do this once):
  ```
  conda uninstall httpx
  conda install httpx<0.28.0
  jupyter lab
  ```
  - once jupyter lab opens, click the extensions(puzzle piece) button on the left hand menu bar
  - type "rise" into the extensions search bar
  - install jupyterlab-rise
- run myst start or just build the pdf
  ```
  # to start
  myst start
  # to build
  myst build --pdf
  ```
- Alternatively: Launch Jupyter Lab and view paper & presentation draft locally.
  ```
  jupyter lab
  ```
