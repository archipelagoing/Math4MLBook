# Lecture 1 editorial and validation record

Reviewed 2026-10-26 in the working tree based on `b1e21f70c9921e91c386f6836f3717498b14da06`.
This is a local chapter milestone, not a release or a measured student outcome.

## Delivered scope

The [chapter](../book/lecture1/index.md) expands the 48-page Week 1 deck into five
teaching sections, a synthesis, 24 problems and explained solutions, and source
notes. It includes skew-symmetric matrices, the cosine-law derivation, dimension
checks, zero-vector limits, column/row multiplication, and matrix properties.
Four original SVGs are generated from [a reproducible script](../tools/build_lecture1_figures.py).
No course PDF was changed. The reader navigation contains the completed chapter;
other weeks and the old template authoring pages remain outside that navigation.

## Source fidelity

[Source notes](../book/lecture1/source-notes.md) map the complete lecture by PDF
page ranges. The deck was read through extracted text; pages 4, 19, 22, 28, 39,
42, 45, and 46 were also inspected as rendered images to resolve entry ordering.
The plane's outside vector is (1,2,3), and the source product is [[2,7],[2,9]].
These are extraction clarifications, not corrections to the lecturer.

The sampler, operation-count ledger, practice, and diagrams are added exposition.
Symmetric/skew decomposition and trace(AB)=trace(BA) are identified as synthesis
extensions. Orthogonality and lengths refer to explicitly defined record spaces;
physical fabric, stitch order, and section counts are distinguished throughout.

## Objective-to-practice map

| Opening objective | Independent practice |
| --- | --- |
| 1. Interpret and operate on vectors | 1–2, 5, 12, 19 |
| 2. Combinations and membership | 3, 9–10, 24 |
| 3. Dot products, norms, unit vectors, angles | 4–5, 11–12, 18, 21, 24 |
| 4. Matrix dimensions and special structures | 6, 8, 13, 17, 22 |
| 5. Transpose, trace, and valid shapes | 6, 13, 17, 22–24 |
| 6. Products and column/row interpretations | 14–16, 19–20, 24 |
| 7. Explain, refute, and independently check | 8–10, 13, 17, 19–24 |

Problems progress from isolated tools to changed examples and synthesis. Six
optional first-step hints support the synthesis group. The solutions explain
reasoning and common errors; the synthesis/readiness page prompts unaided work.
This is chapter practice, not a course-specific marking scheme or timed mock exam.

## Checks and results

- Python 3.12 isolated environment; `pip check` passed. Direct build dependencies
  pinned in `requirements.txt`: TeachBooks 0.2.5, Jupyter Book 1.0.4.post1,
  sphinx-design 0.7.0. Sphinx 7.4.7 was used in this environment.
- Original scaffold build: one warning from a template credits link. The template
  pages are retained as authoring references and excluded from the textbook TOC.
- `teachbooks build book` and a fresh strict
  `jupyter-book build book --all --warningiserror --keep-going` pass with no warnings.
- [Calculation checker](../tools/check_lecture1.py): 67 arithmetic, solution-pairing,
  and SVG syntax checks passed. Manual review also checked hypotheses, dimensions,
  counterexamples, and the general derivations. This is not an independent reviewer.
- Browser review using Playwright/Chromium: all 11 reader pages at widths 1440 and
  390, 456 rendered math expressions per viewport, no MathJax error elements,
  no page-wide horizontal overflow, and no JavaScript errors. Wide equations stay
  locally scrollable. Wide diagrams retain readable sizing and a focusable scroll
  region on small screens.
- Keyboard Enter opens a chapter checkpoint. Browser print opens closed chapter
  explanations and restores their previous state afterwards. A4 print output and
  representative light/dark pages and all four diagrams were visually inspected.
  These are representative accessibility checks, not a complete assistive-technology audit.
- Local rendered links, fragments, and assets checked: 897 successful checks on the final build, alongside strict cross-reference checks.
- Contrast calculations: cocoa/paper 10.92:1; link/paper 6.47:1; deep pink/pink wash
  4.88:1; leaf green/green wash 4.72:1; red/rose 4.72:1; dark text/background 13.93:1;
  dark link/background 9.78:1; dark red/attention panel 7.15:1. Bright pink/green
  remain fills; labels and dark outlines convey meaning as well as color.

The original extension bundle produced duplicate inline-script declarations.
The book now explicitly loads the core extensions needed for static MyST chapters,
omitting unused live-kernel scripts. It retains TeachBooks and Jupyter Book.
The strict build also caught solution fragments that needed MyST label references;
all 24 solution links now resolve. A geometry figure's axis scales were equalized
so its drawn lengths/angles agree with the orthonormal coordinates.

Optional browser checks: install Playwright separately, run `python -m playwright
install chromium`, then `python tools/review_lecture1.py`. Previews are written
under `/tmp`; the output report is printed to stdout. MathJax requires network
access to its CDN. Browser executable location can be configured with Playwright's
`PLAYWRIGHT_BROWSERS_PATH` environment variable.

## Remaining work

Weeks 2–5, the statistics/PCA source gap, exact supporting homework/exam problem
mapping, cumulative and timed practice, and a whole-book notation reference remain
open. Knitting/crochet examples are count constructions, not physically executed
patterns or loop-accurate technique instruction. Qualified independent math/craft
review and evidence of student transfer remain outstanding. Publication, live
GitHub Pages behavior, and a polished standalone PDF edition were not verified.
