# “The Draft”

## Overview

## Class 5

<!-- - *MZ*: Before class, create a public repo with the presentation. -->
<!-- - *MZ*: Prepare to be able to explain how to get a FredAPI key. -->

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/personal/mzahn2_jh_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmzahn2%5Fjh%5Fedu%2FDocuments%2FFall%202023%20AS%2E160%2E369%20Class%20Recordings%2F2023%2E10%2E02%20Class%205%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&ga=1)

**Agenda**
1. **CC, TA** Markdown links (20 min)
   - Teach students how to copy a header link in a markdown file and attach to other text
   - Have each student update the weekly course agenda links to better line up with the syllabus
2. Get and use your own FredAPI Key! (20 min)
    - Register a FRED account
    - Login to FRED account and go to "API Key" to find key
3. Use code-demo to show students how to write a program (80 min)
   - Will analyze FRED data on stock market returns based on presidential term


**Homework**
- Students will pick another variable instead of stock returns from the FRED database to analyze.
- Make a pull request upstream with the code and sentence or two with conclusion.
- Take information from data visualization presentation to improve the visuals of your program. 

## Class 6 — Making Progress

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/:v:/g/personal/mzahn2_jh_edu/EQdZHFe5L8pJu5vCz0mMYIYBtB5NVxPLGpiDp8IxA43Nsg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&e=uE33s1)

### Agenda
- Alan Lujan discussion on MyST
- Discuss best practices for the visual communication of quantitative information (60 min)
    - show video from previous semesters
    - [Visualization Lecture](https://livejohnshopkins-my.sharepoint.com/personal/mzahn2_jh_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmzahn2_jh_edu%2FDocuments%2FFall+2023+AS.160.369+Class+Recordings%2F2023.10.02+Class+5.mp4&startedResponseCatch=true&referrer=StreamWebApp.Web&referrerScenario=AddressBarCopied.view.e8ad06dc-b25b-4b6e-bf9b-876ddbaa1b3b)
- Go over template for final paper and what is expected (60 min)
   - [sample paper](materials/draft/emurinson-paper.ipynb)

**Helpful notes**
- Abstract:
    - Results you hope to get. Write as if you got the results you wanted that align with your hypothesis.
    - Note why people should care about your findings.
    - Tight: Less than 200 words.
- Introduction:
    - Longer than Abstract.
    - Position the paper in terms of our current understanding/debates on the subject.
    - Motivate why you are studying this topic and why it is important. Big pictire, what is the point of your paper.
    - Aim for about a page or a page and a half (~500 to 750 words).
    - Focus on writing well. The content is less important than the process and demonstration of using the tools to improve the content you generate.


### Homework
- Watch tutorial on GitHub practices [Link to video](https://www.youtube.com/watch?v=RGOj5yH7evk)
  - Note: Use Jupyter Notebook instead of VS code 
- Continue working on the Literature Review and Abstract for final papers. Add what you have so far to MyST on Terminal.
- Include data visualization techniques reviewed in class to your analysis from last week. 
- Make a start on the introduction


## Class 7

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/:v:/g/personal/mzahn2_jh_edu/EZZescblGOBEpvWgNGqhJ6YB3dSjrDGW49exKc_EnpGmSw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&e=6m0VKz)

### Agenda
- Show us your data analysis with the FRED variables
    - Which variable did you choose and why?
    - What were the results? Were you suprised?
      
- Show us your current Introduction & **improved** Abstract!

- Discuss next steps for your paper.
    - Literature you plan to use (show latest Litmaps/paperpile).
    - What is the question that you will address with data?
    - What kind of data exist that you can use to answer your question?
      
- Go over template for final paper and what is expected
   - [sample paper](emurinson-paper.ipynb)
     
- Working with Data in your Jupyter Notebook
    - [Instructions](pandas-basics.ipynb)
    - What is tabular data? What is a pandas DataFrame?
    - How do I select columns from a DataFrame, how do I filter rows?
    - How do I perform aggregations/compute summary statistics?
         - TA will walk through ChatGPT prompts for data analysis. Consider how this will be used for your paper. 
    - How do I perform econometrics?
    - How do I create a new `pandas` DataFrame from some other data source?
        - How read a `.csv`, how to read an excel file (`.xls`, `.xlsx`)

     

**Homework**
- Read the [Korinek](https://www.aeaweb.org/articles?id=10.1257/jel.20231736) paper
    - Add it to your paperpile
    - Prepare to identify the tools/ideas you would consider using from the Korinek paper.
    - In the next class, you will write a paragraph on the above.
- Obtain and explore some data that are relevant to your topic.
    - Conduct an exploration/preliminary analysis of your obtained data set(s).
- Be prepared to present to the class on your preliminary analysis of the data.
- Make sure you are working on your SciServer account.
    - and are `git add`ing and `git commit`ing   your work regularly.
    - **Spread out commit messages over at least three days.**
- Prepare for 10 minute discussion where you are in the next class.
- **Once you're finished this, make sure to push all your work from your Sciserver into your Github Repo**
  - Once you try this, if you find you're having difficulty with this, ask AI. If you're still struggling, reach out to Jane.
  - Take everything written in Jupyter and add to MyST. Input into Alan's file from last class so formatting is correct. Use AI to figure this out if you are struggling. 

## Class 8

### Agenda
- HW Review (70 min.)
- You should write a paragraph on the tools/ideas you would consider using from the Korinek paper. (10 min.)
- CC will run through `git merge` conflicts and how to deal with them. (15 min.)
- Make sure all copies of repo are synchronized. We will fix any merge conflicts in class. Compile your MyST Markdown on your local computer. (15 min.)
- Make a subfolder in your contrib folder. Name it "paper." You will now start saving sections of your paper to this folder. 
- Make sure that all parts of paper are in separate Jupyter notebooks. Names should be standardized like:
```
  - abstract.md
  - introduction.md
  - literature-review.md
  - methodology.md
  - results.md
  - discussion.md
  - conclusion.md
```


<!-- [myst](https://mystmd.org) to create a webpage with bibliography.-->
- Writing your jupyterbook with multiple markdowns 
  
```sh
# copy jupyterbook folder contrib/cam/jupyterbook to your own contrib folder
# navigate to the new copy of /jupyterbook your contrib folder

# start terminal session in the folder of your notebook
# alternatively, use `cd` to navigate to your notebook folder

build-jb .

# open '_build/html'
```
  
**Homework**
- Improve your Korinek reflection: make it >300 words, and commit improvements over 3 separate days.
  - Use AI to improve your piece!
- Revise and improve your Literature Review
  - utilize ChatGPT/Claude and commit improvements over 3 days
- Begin your data empirical work (regressions, etc.)
  - Write the first draft of your methodology section in conjunction with your regressions, etc.
- After you have completed the methodology draft, ask an AI to resolve any inconsistencies with the introduction and literature review. 
- The above 2 sections of your paper should be in *separate* markdown files.
    - For a reference, use [Alan Lujan's REMARK](https://github.com/alanlujan91/SequentialEGM/blob/main/content/public/SequentialEGMn.pdf).
    - [Embed reference](https://github.com/alanlujan91/SequentialEGM/blob/main/content/paper/egmn.md)
    - [Other reference](https://mystmd.org/guide/embed#docs-include)

## Class 9

### Agenda

- HW Review: prompts people found useful for the Korinek reflection and lit review improvements (20 minutes)

- Instructional on best practices aiding your literature search (15 minutes)
  - Beyond Litmaps & Paperpile
       - Using AI
       - [NotebookLM](https://notebooklm.google/?utm_source=chatgpt.com) - understanding papers in your literature review
       - Note: Literature review papers are particularly helpful for getting your bearings
         
- Using AI to generate ideas for data analysis (10 min)
   - [Julius AI](https://julius.ai/chat)

- Updates on your paper progress (80 minutes)
  - roadblocks and problems you've encountered
  - methodology and lit review section updates
    
- Have each student go through their local machine or SciServer and make sure everything is sync'ed. (10 min)

- Review Myst files (on local machines) and fix any errors (15 min)


**Homework**
- Comment on a classmate's advice from the Korinek paper. 
- Write the first draft of the results section. ([Here's](https://twp.duke.edu/sites/twp.duke.edu/files/file-attachments/econ.original.pdf) a great resource from Duke on writing this and other sections.)
    - You should break your text into a number of smaller markdown cells.
        - This makes it easier to use ChatGPT for editing.
    - Be sure to get ChatGPT feedback on your writing.
    - In the commits you write, please include the prompts you used in ChatGPT.
 - Make sure that all parts of paper are in separate Jupyter notebooks. Names should be standardized like:
```
  - abstract.md
  - introduction.md
  - literature-review.md
  - methodology.md
  - results.md
  - discussion.md
  - conclusion.md
```

## Class 10


### Agenda
- Discuss your results section (10 minutes ea).
- Go over Beyond The Streetlight presentation to learn how to make presentations in HTML
  - Demonstrate jupyter-nbconvert to export jupyter rise slides using [Beyond the Streetlight](https://github.com/llorracc/beyond-the-streetlight)
  - ```pip install RISE jupyterlab-rise ```
  -  restart container (stop the container and restart!)
  -  important tools:
      - on top right corner click on the presentation symbol [Render the current notebook as Reveal Slideshow (Alt + R)] 
      - on the RHS of jupyter-lab go to **property inspector (two screws)** --> **common tools**
- Working with myst:
  - Create new econ-ark container
  - Restructure your paper as in contrib/AMonninger/Paper_Restructured
  - On Sciserver we can now use `myst`. Although the usual `myst start` does not work. Instead do the following
    ```
    pip install mystmd

    myst init

    myst-start
    ```
  - Open the given link (might take a few minutes)
 

**Homework**
- Create a conclusion section
- Break down your paper in multiple (at least 2) parts.
- Make a draft of the presentation of your paper.

