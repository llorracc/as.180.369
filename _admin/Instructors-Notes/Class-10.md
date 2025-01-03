### Agenda
- Discuss your results section (10 minutes ea).
- Discussion of ChatGPT/AI Whispering practices and approaches.

Graduate TA:
- Working with myst:
  - Create new econ-ark container (not necessary in future years)
  - Restructure your paper as in contrib/AMonninger/Paper_Restructured
  - Copy this folder into contrib/USERID/AMonninger
  - On Sciserver we can now use `myst`. Although the usual `myst start` does not work. Instead do the following
    ```
    pip install mystmd

    myst init
    ```
  - click no when asked to myst start
    ```
    myst-start
    ```
  - Open the given link (might take a few minutes) (looks like: https://apps.sciserver.org/dockervm16/STUFF/proxy/3000)
  - Go over structure (see yml files and 00_paper_root.md) and show how you can split up the paper in different md **and** ipynb files.

CC:
- Demonstrate jupyter-nbconvert to export jupyter rise slides using [Beyond the Streetlight](https://github.com/llorracc/beyond-the-streetlight)
  - git clone repo: git clone https://github.com/llorracc/beyond-the-streetlight
  -  ```pip install RISE jupyterlab-rise ```
  -  restart container (stop the container and restart!)
  - discuss: RS100_Discussion_Slides.ipynb
  - on top right corner click on the presentation symbol [Render the current notebook as Reveal Slideshow (Alt + R)] 
  - on the RHS of jupyter-lab go to **property inspector** --> **common tools**
  - ```jupyter-nbconvert RS100_Discussion_Slides.ipynb --to html```
  - vs **File** --> **Save and Export Notebook as** --> **Reveal.js Slides**
