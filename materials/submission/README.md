# “The Submission”

## Overview

## Class 11
**[Homework from previous class](https://github.com/llorracc/as.180.369/tree/main/materials/draft#class-10)**
- Work on the presentation of your paper.


**Agenda**
- Share the work you have done on your presentation (10 mins ea.)
    - Focus on Conclusion
    - Show us the structure of your paper
- How to format paper correctly for Myst 
    - show how to combine multiple jupyter notebooks and markdown files into one pdf or html.
    - Click on [Adrian's example](https://github.com/llorracc/as.180.369/blob/main/contrib/AMonninger/Paper_Restructured/myst.yml) and adapt to your name and file names.
- How to create a bibliograpy
    - Option 1: Use paperpile and export a bibtec to github
    - Option 2: Input using DOI
  ```
        - pip install requests
        - dois = ["doi 1", "doi 2, ...]
        - output_file = "references.bib"
        - with open(output_file, "w", encoding="utf-8") as f:
    for doi in dois:
        url = f"https://doi.org/{doi}"
        headers = {"Accept": "application/x-bibtex"}
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            bibtex_entry = r.text.strip()
            f.write(bibtex_entry + "\n\n")
            print(f"✅ Added {doi}")
        else:
            print(f"❌ Failed to fetch {doi} (status {r.status_code})")

``

- In class work time.
    - Bring your questions.
    - Receive help with Python, Jupyter, `build-jb`, `myst-start` LitMaps, Paperpile, … anything!
- Q&A About the final draft.

**Homework**
- Work on your Final Draft
- Work on your slides. 
- Revisit your PaperPile
    - denote with a tag the citations that you actually reference in your draft
    - Set up a workflow that will automatically update your bibfile when you change the papers you are referencing
 
- Please create a final Litmap with all the papers you used(should be > 10 and < 100). Make sure to have tagging done right(a solid number of tags + show which papers address multiple tags in a single paper)
