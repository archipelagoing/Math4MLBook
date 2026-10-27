# Mathematical Foundations of Machine Learning

A TeachBooks textbook built from the course materials in `resources/`, using a
connected knitting-and-crochet sampler to develop the mathematics.

**Available:** [Lecture 1 — Vectors and matrices](book/lecture1/index.md), with
worked examples, four original diagrams, checkpoints, 24 practice problems,
explained solutions, and a page-level source map. Weeks 2–5 remain in the authoring
backlog. The project does not yet constitute complete midterm preparation.

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
