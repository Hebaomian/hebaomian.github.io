# Zishuo Zhao's personal website

An English academic homepage for Zishuo Zhao, built with plain HTML, CSS, and JavaScript for GitHub Pages. The layout is inspired by [academic-website-template](https://github.com/sbryngelson/academic-website-template) and [Xie Zhang's homepage](https://zhang-xie.github.io/).

## Contents

- `index.html`: biography, research directions, news, experience, and education.
- `publications.js`: publication metadata, links, summaries, and BibTeX.
- `site.js`: publication filters, expandable summaries and citations, and mobile navigation.
- `style.css`: responsive layout, accessibility states, and print styles.
- `assets/CV.pdf`: public English CV. The original private resume is not included.
- `tools/build_cv.py`: generates the public English CV with ReportLab.
- `.nojekyll`: serves the files directly through GitHub Pages.

## Local preview

Run from this directory:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Then open `http://127.0.0.1:4173`.

## GitHub Pages

Use a repository named `Hebaomian.github.io`. Upload the files in this directory to the repository root. In **Settings → Pages**, select **Deploy from a branch**, **main**, and **/(root)**.

The intended address is `https://hebaomian.github.io/`. It becomes available after the Pages deployment succeeds.

## Updating content

Edit text in `index.html` and paper records in `publications.js`. New publication records must have a unique `id`, a `group`, and a supported `topic` (`agents`, `nlp`, `multimodal`, or `knowledge`). Keep preprints distinct from accepted conference papers.

To regenerate the CV with ReportLab installed:

```sh
python3 tools/build_cv.py
```

The public version omits the personal phone number and internal business scenario identifiers. The academic contact email comes from the supplied resume.
