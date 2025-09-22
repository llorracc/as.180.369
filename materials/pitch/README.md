# “The Pitch”

## Overview

In the pitch phase of this course, you will create a pitch for a compelling
research paper.

## Class 2: Demos & Topics



[Zoom recording. Requires JHU login.]()

**Agenda**
1. **CC, TA's** tool micro-demos 
    - [Github.com](https://github.com) Demo (60 mins)
        - What is a fork?
        - How do I sync my copy of the repository with the original?
        - How do I open and comment on issues?
        - What is a Pull Request?
     - Full tour of GitHub
     - Download GitHub desktop and use to clone repository 
    - Markdown Demo (10 mins)
        - What is Markdown, and how do I use it to format my documents?
        - How do I create headings?
        - How do I emphasize text?
        - How do I create unordered and ordered lists?
        - How do I create (simple) tables?
        - How do I embed mathematical equations using LaTeX?
        - How do I embed images?
        - References: [Get Started with Markdown on Github](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) & [Writing math in Markdown on Github](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
    - [`git`](https://docs.github.com/en/get-started/quickstart/hello-world) and [`gh`](https://cli.github.com/manual/examples) Demo (20 mins)
        - How do I `git clone`?
        - How do I `git push`?
        - How do I `git pull`?
        - How do I `git add` and `git commit`?
        - How do I use `gh`?
2. **CC, TA's** [BibTeX](https://www.bibtex.com) (10 min.)
    - [What is BibTeX?](https://www.bibtex.com/g/bibtex-format/#what-is-bibtex)
    - [BibTeX format explained](https://www.bibtex.com/g/bibtex-format/#bibtex-format-explained)
    - Discussion of BibTeX issues
3. **CC, TA's** [JHU Economics Libary Guide](https://guides.library.jhu.edu/economics) (5 min.)
4. **CC, TA's** [Paperpile](https://paperpile.com/) (20 min.)
    - Verify you have connected your account to the jhu library for help in finding papers
    - Sharing vs exporting bibliographies
    - How do you organize your Paperpile folders?
5. **CC, TA's** overview of term paper & process (15 mins): What is the overall goal of the term paper? What process will we follow? What do we want to accomplish through the pitch process?

**Homework**
- Choose a topic for your pitch
- Please view the JEP shared library (Journal of Economic Perspectives, 2022-Q2 through 2024-Q3). [JEP](https://paperpile.com/shared/JEP-Master-fXGs~p9Z6QT2ibDfuw3nruw)
    - You should be able to see the entire set of issues through that shared library. These papers will help guide you towards picking a topic, but you are welcome to use other sources in addition to this. 
- To get started on building your own Paperpile library, I’ve assigned you a specific issue of JEP. Please make sure to save all of the papers from this issue into your personal Paperpile library. To do this, you can drag the subfolder from the "Shared with me" section on the left side of the screen up to the "My library" section. 
- Prepare a markdown file in your contrib folder with your thoughts on the topic and what your initial hypothesis for the relationship is. Write two paragraphs. 
- You are welcome to use resources like ChatGPT for this assignment.

## Class 3 Tools—Pitch and JupyterLab

**Agenda**
1. **CC, TA** (10 min.)
    - Exhibit workflow for creating and sharing a new folder in PaperPile.
2. **CC** (60 min.)
    - Have each student present their paragraph from HW and describe their proposed topic.
    - CC will provide live feedback to students on their proposed topics.  
3. **CC, TA** JupyterHub (30 mins)
    - Create a Globus account with your hopkins login [Globus.org](https://www.globus.org/)
    - Log in to SciServer using your Globus login [SciServer](https://apps.sciserver.org/dashboard/)
    - Once on the Dashboard, press Compute, then create a new container with the course name. Make sure the Compute Image is econ-ark
    - Open a terminal page and change directory with: `cd ~/workspace/Storage/ID/persistent`
    - NOTE: ID should be the students SciServer username
    - clone the GitHub repo by typing:
        - `git clone https://github.com/llorracc/as.180.369.git`
    - Once created, click on the storage folder, then your jhed, then persistent. You should find the course repo here.  
    - Provide demo on how to use terminal, notebook, and other features.
4. **CC** Beyond the Streetlight (10 mins)
    - Copy the Beyond the Streetlight file into their directory
    - `mv Beyond_the_Streetlight.ipynb`
    - [`git`](https://docs.github.com/en/get-started/quickstart/hello-world) and [`gh`](https://cli.github.com/manual/examples) Check: From Jupyrerhub, clone your fork, make a commit, and push back to Github. (10 mins)
        - `git status` to see if there is any uncommitted work.
        - `git add` Beyond the Streetlight **notebook**
        - `git status` to check what is in your staging area (to inspect what has been `git add`ed)
        - `git commit -m …` the changes you `git add`ed.
        - `git push origin` to synchronize the changes from your Jupyterhub to Github.
    - **You should NEVER EVER edit ANYTHING on the Github website again** All changes should be made in Jupyterhub and then `git push`ed up.
    
**Homework**
- Use Litmaps to conduct at least two literature searches.

    - 1 search for the topic you have selected to pitch.
- Prepare yourself to discuss, in the next class, what you found in your literature searches.
    - Review this [additional Paperpile resource](https://www.youtube.com/watch?v=y7vDPfSr-k0)
    - You will need to explain why you picked some papers and did not include all of them.
    - You will need to identify what you think are the most important papers, **and why**.
    - You will need to discuss which of your two topics seems more promising.
        - based upon your review of the literatures.

## Class 4: Research Pitches

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/personal/mzahn2_jh_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmzahn2%5Fjh%5Fedu%2FDocuments%2FFall%202023%20AS%2E160%2E369%20Class%20Recordings%2F2023%2E09%2E25%20Class%204%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&ga=1)

1. **CC, TA** Create a Jupyter Notebook (20 min)
   - Create a new Notebook that contains your Litmaps and any associated text.
   - Push to course Github in your contrib folder.
  
2. **CC, TA** Use AI to improve Jupyter Notebook (20 min)
   - Research any methods for this that do not involve copy and pasting into ChatGPT.
  
3. **TA** Sign up for course groupchat and send introduction (15 min)
   - [GroupMe link](https://groupme.com/join_group/110309543/gWmJH3OW)
   - Send a quick introduction for other students to read.

4. **CC, TA** Pitch (70 min)
   - You will share a pitch, no longer than 5 minutes in duration, that should convey the following items:

- Exhibit understanding of existing literature around your topics 
    - You will share your screen showing LitMaps results.
- Clear research question 
    - Do you understand the topic you selected?
    - Were you able to articulate it as a research question?
- Preview/outline of what you plan to do to answer that question.
- Fit & finish
    - Visual aides should be clear, concise, and not too wordy.
    - Speaking style should be slow and understandable.

**Additional Guidelines**
- 5 minutes per student + 5 min Q&A (×7 students = 70 min)

**Homework**
- Continue to upload your Litmaps and upload into PaperPile account. 
- Pick some of your papers from your Litmap and read them. 
- Write a summary paragraph for each paper. This will help with the Literature Review down the line.
- Refine the ideas presented in your pitch. 
- We are looking for deeper knowledge of literature and refined ideas.
- Also, find some information about your data options and include a pitch on what type of data you plan to use. 
- Make an update to your fork and then make pull request to the main course repo. This is how will turn in assignments from now on. 
