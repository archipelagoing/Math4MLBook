# Mathematical Foundations of Machine Learning

A TeachBooks textbook built from the course materials in `resources/`, using a
connected knitting-and-crochet sampler to develop the mathematics.

**Available:** Lecture 1 in two reading pages, retaining every distinct lecture example:
[vectors and geometry](book/lecture1/index.md) and
[matrices and multiplication](book/lecture1/matrix-guide.md).
[Download the complete guide PDF](authoring/lecture1-study-guide.pdf).
[Source-coverage audit](authoring/lecture1-coverage.md) maps every topic and example.
Yellow panels highlight essential formulas; red panels flag exam mistakes.
The earlier expanded explanations and 24-problem bank remain in `book/lecture1/`
as source references, outside the reader navigation. Weeks 2–5 remain unfinished.

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

Chapter sources are MyST Markdown in `book/lecture1/`; reader navigation is in
`book/_toc.yml`, and shared styling is in `book/_static/textbook.css`.

```sh
python tools/build_lecture1_figures.py
python tools/check_lecture1.py
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
- [Lecture 1 source notes](book/lecture1/source-notes.md): attribution and scope.

The repository began with the [TeachBooks template](https://github.com/TeachBooks/template).
Its authoring examples remain available in the source tree, outside the reader's
navigation. The existing [license](LICENSE.md) does not establish ownership of the
supplied course PDFs; source-specific attribution is recorded in each chapter.
Local authoring and checking do not publish the book. Deployment uses the existing
GitHub workflow when publication is authorized.
