# Mathematical Foundations of Machine Learning

A TeachBooks textbook built from the course materials in `resources/`, using
marked points and calibrated shadow views to develop the mathematics.

Each lecture has four **numbered topic pages in the left sidebar**, grouped under
its lecture title. Practice and expandable explained solutions follow the relevant
topic on the same page. They are not separate sidebar destinations.

| Page | Lecture 1 | Lecture 2 |
| --- | --- | --- |
| 1 | [Vectors and combinations](book/lecture1/index.md) | [Systems and elimination](book/lecture2/index.md) |
| 2 | [Dot products and geometry](book/lecture1/geometry.md) | [Determinants and geometry](book/lecture2/elimination.md) |
| 3 | [Matrices and products](book/lecture1/matrix-guide.md) | [Inverses and invertibility](book/lecture2/inverses.md) |
| 4 | [TL;DR cheat sheet](book/lecture1/cheatsheet.md) | [TL;DR cheat sheet](book/lecture2/cheatsheet.md) |

Lecture 1 retains 12 learning sections and 24 exercises. Lecture 2 covers all 36
PDF pages in Parts A–N, with 17 numbered stepwise examples and 26 exercises.
Source banks `practice.md` and `solutions.md` are included by topic, preserving
problem and solution IDs while placing answers directly below their questions.
TL;DR pages collect formulas/conditions, method recipes and checked examples.
The four-page cap concerns website navigation, not physical print sheets.
Weeks 3–5 and cumulative exam preparation remain unfinished.

Start agent work with [AGENTS.md](AGENTS.md), then the
[current contract in the show bible](SHOW_BIBLE.md#current-authoring-contract).
Coverage and verification records live in `authoring/lectureN-coverage.md` and
`authoring/lectureN-review.md`. Earlier condensed PDFs are historical summaries.

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
See [Lecture 1 review evidence](authoring/lecture1-review.md) and
[Lecture 2 review evidence](authoring/lecture2-review.md) for source checks,
browser checks, and remaining limitations. The installed browser tooling is an
optional review aid and is not a book build dependency.

## Editorial references

- [Agent instructions](AGENTS.md): source coverage, numbered topic navigation, authoring and build workflow.
- [Show bible](SHOW_BIBLE.md): current contract, teaching goals, style, and scope.
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
