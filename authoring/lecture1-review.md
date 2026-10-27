# Lecture 1 editorial and validation record

## Current edition · Numbered topic pages

2026-10-27: the sidebar is grouped under Lecture 1 with four explicit numbered
links: Page 1 vectors/combinations; Page 2 dot products/geometry; Page 3 matrices/
products; Page 4 TL;DR. The 12 teaching sections and all source mathematics are
preserved. The 24 questions/answers are included by topic, with each explained
solution expandable directly below its question. Original labels and retry links
remain. `practice.md`/`solutions.md` are source banks, not reader pages.

`tools/check_lecture1.py` passes **95** arithmetic/pairing/asset/narrative checks.
The strict book build passes. `tools/review_lecture1.py` delegates to the shared
`review_textbook.py`, which checks the actual sidebar labels, per-page section and
practice allocation, all original example numbers, references and keyboard answers
at desktop/mobile sizes, with every solution expanded for overflow checks.
Rendered evidence is recorded under `/tmp/math4ml-navigation/lecture1/`.
The earlier format-specific review below is historical. No deployment or observed
student effectiveness is implied by this local reorganization.

## Previous edition: show-bible teaching structure

**Selected scene:** The owner selected shadows to replace knitting/crochet. The
active welcome, two teaching pages, exercises, solutions, book mark and four SVGs
now use matched point coordinates and calibrated front/side views. Canonical O
and H retain their 2-by-3 and 4-by-3 shapes. The four-bead X profiles are explicitly
separate records from a single point's three-dimensional world coordinates.

Negative/fractional coordinates are valid. Former integer/nonnegative count
restrictions were removed, including the answer to Problem 1. Problem 15 and the
matrix-vector checkpoint now use actual view maps; associated feedback and checks
were rewritten. Source lecture examples, sectioning, colors and four-page cap are
preserved. Earlier craft material below is historical.

Based on `9d932e0`; includes the selected shadow-lens migration. Lecture 1 remains exactly four website pages, including exercises
and solutions. The two teaching pages now have 12 numbered sections (1.1–1.12),
page objectives and prerequisites, route cards, local roadmaps, source-page labels,
and motivating questions. Each section closes with a checkpoint, a takeaway, and
practice links. The chapter contains 7 numbered definition boxes, 12 numbered
worked examples, a named cosine-formula theorem/proof, and an ML connection.

Worked examples expose intermediate steps and checks. The final synthesis gives
an unaided readiness checklist and a skill-to-exercise map; every one of the
24 solutions links to an explanation and a related retry problem. All lecture
examples/properties and the four diagrams are preserved; see the
[coverage audit](lecture1-coverage.md).

The stylesheet gives the page route, section introduction, definition, example,
result, proof, warning, and recap distinct labeled roles. Bright fills accompany
readable dark text; the serif reading measure is capped at 75ch. Dark/mobile/print
styles retain the same hierarchy. No printed-page limit applies. The earlier
condensed PDF is an archived summary rather than the current reader format.

Validation: strict build, 93 arithmetic/structural/narrative checks, and browser checks cover
the five reader documents at desktop/mobile widths. The browser checker verifies
four lecture pages, six learning goals/recaps/checkpoints per teaching page,
12 consecutively numbered worked examples, route/current-page markers, checkpoint
keyboard access, section jumps, a solution return link, dark colors, and print
answer expansion. All 10 viewport/page checks report no MathJax errors, page-wide
overflow, or JavaScript errors; rendered local links/assets are checked separately. Section
jump checks wait for scrolling to finish and verify the target heading position.
Remaining independent reviewer/student outcomes are unverified.
The four active SVGs were visually inspected at desktop size, with labeled world,
front/side, and profile-coordinate panels. The browser also checks that all five
active article bodies contain no residual craft narrative. The new point/view
branding loads, and the old diagram assets remain outside the reader route.
This revision is local and has not been pushed or deployed.

## Expanded edition review (historical)

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

## Numbered-navigation verification · 2026-10-27

The strict build and current browser checks pass. The browser inspected the real
left-sidebar captions/Page 1–4 labels and the topic allocation of questions and
answers, not just the Markdown route. All original examples and solution IDs
remain available; answers were keyboard-opened and all were expanded for mobile
overflow checking. Desktop and mobile screenshots were visually reviewed.

This run covered 10 page/viewport combinations and 268 local article
links/assets, with zero MathJax errors, JavaScript errors or page-wide overflow.
