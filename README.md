# Mathematical Foundations of Machine Learning

A TeachBooks textbook built from the course materials in `resources/`, using
marked points and calibrated shadow views to develop the mathematics.

**Lecture 1 is a four-page textbook chapter:**

1. [Vectors and geometry](book/lecture1/index.md).
2. [Matrices and products](book/lecture1/matrix-guide.md).
3. [Exercises](book/lecture1/practice.md).
4. [Solutions](book/lecture1/solutions.md).

The shadow-based reading pages contain 12 numbered learning sections, page objectives, section
roadmaps, four diagrams, 12 worked examples, 12 checkpoint answers, highlighted
results, and an end-of-chapter readiness map. Each solution links to a relevant
explanation and a retry problem. All distinct lecture examples and
properties remain; [the coverage audit](authoring/lecture1-coverage.md) maps them
to the chapter. Each lecture is limited to four website pages including practice
and solutions. Printed page count is not the navigation limit. Lecture 2 now covers systems of linear equations; determinants/inverses and
Weeks 3–5 remain unfinished. The earlier condensed PDF is an archived summary, not the current
textbook reading experience.

**Lecture 2 is also four pages:** [Systems and modelling](book/lecture2/index.md),
[elimination and echelon forms](book/lecture2/elimination.md),
[18 exercises](book/lecture2/practice.md), and [explained solutions](book/lecture2/solutions.md).
It covers Week 2 PDF pages 1–21, with eight learning sections/checkpoints, the slide
systems, Gaussian elimination/back substitution, Gauss–Jordan, REF/RREF, and solution
classification. [Source audit](authoring/lecture2-coverage.md) and
[review record](authoring/lecture2-review.md) identify scope and checks.

## Read locally

Use **Python 3.12**, the version tested for this book:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
teachbooks build book
python -m http.server 8000 --bind 127.0.0.1 --directory book/_build/html
```

Open <http://127.0.0.1:8000>. Stop the server with Ctrl+C.
You can also open `book/_build/html/index.html` directly. MathJax loads from its
configured CDN, so equation rendering requires an internet connection.

## Author and check

Chapter sources are MyST Markdown in `book/lecture1/` and `book/lecture2/`; reader navigation is in
`book/_toc.yml`, and shared styling is in `book/_static/textbook.css`.

```sh
python tools/build_lecture1_figures.py
python tools/check_lecture1.py
python tools/build_lecture2_figures.py
python tools/check_lecture2.py
jupyter-book build book --all --warningiserror --keep-going
```

The calculation checker recomputes the chapter's numerical examples and verifies
practice/solution pairing. It does not replace mathematical proofreading.
See [Lecture 1 review evidence](authoring/lecture1-review.md) for source checks,
browser checks, and remaining limitations. The installed browser tooling is an
optional review aid and is not a book build dependency.

## Editorial references

- [Show bible](SHOW_BIBLE.md): teaching goals, style, and scope.
- [Main rubric](rubricatm.md): whole-book quality criteria and current assessment.
- [Checklist](todoSimple.md): implementation status and next work.
- [Analogy reference](analogy/README.md): shared mathematical mappings.
- [Lecture 1 source audit](authoring/lecture1-coverage.md): attribution and scope.

The repository began with the [TeachBooks template](https://github.com/TeachBooks/template).
Its authoring examples remain available in the source tree, outside the reader's
navigation. The existing [license](LICENSE) does not establish ownership of the
supplied course PDFs; source-specific attribution is recorded in each chapter.
Local authoring and checking do not publish the book. Deployment uses the existing
GitHub workflow when publication is authorized.
