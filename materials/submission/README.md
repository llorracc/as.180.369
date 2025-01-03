# “The Submission”

## Overview

## Class 11
**[Homework from previous class](https://github.com/llorracc/as.180.369/tree/main/materials/draft#class-10)**
- Work on the presentation of your paper.


**Agenda**
- Share the work you have done on your presentation (10 mins ea.)
    - Focus on Conclusion
    - Show us the structure of your paper
- Brief example of how to set up workflows in PaperPile
- Discuss reproducibility.
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
- In class work time.
    - Bring your questions.
    - Receive help with Python, Jupyter, `build-jb`, `myst-start` LitMaps, Paperpile, … anything!
- Q&A About the final draft.

**Homework**
- Work on your Final Draft
- Make sure reproduce.sh works for your paper (using the instructions listed above in the Class Agenda)
- Revisit your PaperPile
    - denote with a tag the citations that you actually reference in your draft
    - Set up a workflow that will automatically update your bibfile when you change the papers you are referencing
 
- Please create a final Litmap with all the papers you used(should be > 10 and < 100). Make sure to have tagging done right(a solid number of tags + show which papers address multiple tags in a single paper)
