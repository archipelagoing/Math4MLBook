# Mathematical Foundations of Machine Learning

A TeachBooks textbook built from the course materials in `resources/`, using
marked points and calibrated shadow views to develop the mathematics.

Each lecture has four **numbered topic pages in the left sidebar**, grouped under
its lecture title. Practice and expandable explained solutions follow the relevant
topic on the same page. They are not separate sidebar destinations.

| Page | Lecture 1 | Lecture 2 | Lecture 3 | Lecture 4 | Lecture 5 | Lecture 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Vectors and combinations](book/lecture1/index.md) | [Systems and elimination](book/lecture2/index.md) | [Spaces and subspaces](book/lecture3/index.md) | [Orthogonality and projections](book/lecture4/index.md) | [Eigenvalues and diagonalization](book/lecture5/index.md) | [Statistics and PCA geometry](book/lecture6/index.md) |
| 2 | [Dot products and geometry](book/lecture1/geometry.md) | [Determinants and geometry](book/lecture2/elimination.md) | [Complete solutions and rank](book/lecture3/solutions-rank.md) | [Subspaces and least squares](book/lecture4/least-squares.md) | [Singular value decomposition](book/lecture5/svd.md) | [Compute principal components](book/lecture6/principal-components.md) |
| 3 | [Matrices and products](book/lecture1/matrix-guide.md) | [Inverses and invertibility](book/lecture2/inverses.md) | [Independence, span and basis](book/lecture3/basis.md) | [Orthonormal bases and Gram–Schmidt](book/lecture4/orthonormal.md) | [Reduction and recommendations](book/lecture5/applications.md) | [Scaling, applications and pitfalls](book/lecture6/applications.md) |
| 4 | [TL;DR cheat sheet](book/lecture1/cheatsheet.md) | [TL;DR cheat sheet](book/lecture2/cheatsheet.md) | [TL;DR cheat sheet](book/lecture3/cheatsheet.md) | [TL;DR cheat sheet](book/lecture4/cheatsheet.md) | [TL;DR cheat sheet](book/lecture5/cheatsheet.md) | [TL;DR cheat sheet](book/lecture6/cheatsheet.md) |

Lecture 1 retains 12 learning sections and 24 exercises. Lecture 2 covers all 36
PDF pages in Parts A–N, with 17 numbered stepwise examples and 26 exercises.
Source banks `practice.md` and `solutions.md` are included by topic, preserving
problem and solution IDs while placing answers directly below their questions.
TL;DR pages collect formulas/conditions, method recipes and checked examples.
The four-page cap concerns website navigation, not physical print sheets.
Lecture 3 covers all 35 PDF pages with 16 worked examples, four diagrams and
28 checked practice questions, including fresh variants, mapped recitation tasks
and a mixed readiness check. Meaningful source corrections are explicit.
Lecture 4 covers all 28 PDF pages in 11 ordered parts, with 14 worked examples,
six original diagrams, 28 integrated problems and a method-focused cheat sheet.
Lecture 5 covers all 44 PDF pages, including handwritten notes and final in-class
exercises, in 10 ordered parts with 15 worked examples, six diagrams and 28
practice questions. Lecture 6 covers the complete 39-page PCA deck, including
mean, sample variance/standard deviation, covariance, the full student PCA example,
standardization, applications and failure cases. Its 15 examples, 28 questions,
seven original diagrams and two credited source images close the statistics/PCA
teaching gap. Cumulative exam preparation remains open.

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

Chapter sources are MyST Markdown in `book/lecture1/`, `book/lecture2/`, `book/lecture3/`, `book/lecture4/`, `book/lecture5/`, and `book/lecture6/`; reader navigation is in
`book/_toc.yml`, and shared styling is in `book/_static/textbook.css`.

```sh
python tools/build_lecture1_figures.py
python tools/check_lecture1.py
python tools/build_lecture2_figures.py
python tools/check_lecture2.py
python tools/build_lecture3_figures.py
python tools/check_lecture3.py
python tools/build_lecture4_figures.py
python tools/check_lecture4.py
python tools/build_lecture5_figures.py
python tools/check_lecture5.py
python tools/build_lecture6_figures.py
python tools/check_lecture6.py
jupyter-book build book --all --warningiserror --keep-going
```

The calculation checker recomputes the chapter's numerical examples and verifies
practice/solution pairing. It does not replace mathematical proofreading.
See [Lecture 1 review evidence](authoring/lecture1-review.md) and
[Lecture 2 review evidence](authoring/lecture2-review.md),
[Lecture 3 review evidence](authoring/lecture3-review.md) and
[Lecture 4 review evidence](authoring/lecture4-review.md) and
[Lecture 5 review evidence](authoring/lecture5-review.md) and
[Lecture 6 review evidence](authoring/lecture6-review.md) for source checks,
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

Lecture 3 was verified live on 2026-10-27 at
[its branch-specific Pages URL](https://archipelagoing.github.io/Math4MLBook/main/lecture3/index.html).
Lecture 4 is committed in `f395bc4`; its publication was not rechecked during
Lecture 5 authoring. Lectures 5–6 remain local until committed and pushed. The Week 6 duplicate PDFs
are preserved; later Week 8 resources are not yet authored.
