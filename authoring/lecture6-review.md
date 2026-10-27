# Lecture 6 · Implementation and verification

Date: 2026-10-27. Base commit `f395bc4`; existing local Lecture 5 work, user-supplied
PCA/Week 8 PDFs and unrelated working-tree changes were preserved. No commit,
push or publication performed. This task authors Week 6, not the later Week 8 decks.

## Delivered

All 39 distinct PCA pages are mapped to Parts A–L on four numbered sidebar pages:
statistics/PCA geometry; compute principal components; scaling/applications/
pitfalls; TL;DR. The two supplied Week 6 PDFs are byte-identical and both remain.

Fifteen numbered examples use highlighted how/why steps, intermediate arithmetic,
original-problem checks and yellow conclusions. Twelve checkpoints, 28 integrated
questions with explained answers and specific diagnosis/revision/retry links, a
fresh four-problem mixed rehearsal and dedicated cheat sheet support independent
work. All source data, the student eigenvectors/scores/variance quiz and required
application illustrations are available on the website without the slides.

There are seven reproducible original SVG diagrams and two unchanged empirical
images extracted from the source PDF: the genetics/map comparison and eigenface
illustration, both credited. Toy geometry is explicitly identified; the book does
not fabricate source scatter arrays, research replications or face-training data.
[The coverage audit](lecture6-coverage.md) maps all source pages and clarifications.

Mean, sample variance/standard deviation, covariance, normalization conventions,
PCA/SVD, scoring/reconstruction and explained variance now have source-based
teaching destinations. The previous statistics/PCA teaching gap is closed; that
does not complete the cumulative exam-preparation work or demonstrate a student A.

## Verification evidence

- `.venv/bin/jupyter-book build book --all --warningiserror --keep-going` passes.
- `tools/check_lecture6.py` passes **646 checks**. Exact Fraction computations
  independently center observations and form covariance matrices; verify complete
  spectral decompositions, orthogonal projectors and score covariance; compute
  reconstructions, perpendicular residuals, sample score variances, EVR, SSE and
  mean squared error; and test standardization/inverse scaling, tied/zero/constant
  cases, outlier and label-signal examples, fresh practice and all mixed computations.
  Source student values are checked exactly; numerical two-by-two eigenvalue and
  decimal-score calculations provide additional cross-checks. Source duplicate
  hashes, bank pairing/part/example counts, SVG descriptions and PNG signatures/
  dimensions are also verified. This is not independent expert or learner testing.
- Earlier checkers pass: **95/98/223/409/632** for Lectures 1–5; together with Week 6,
  **2,103 checks** pass. No prior numerical lesson content was rewritten; Lecture 5’s
  source-note link now points to the delivered Week 6 statistics/PCA destination.
- `tools/review_lecture6.py` passes **10 page/viewport cases** (welcome + four pages,
  1440px and 390px), **196 local article links/assets**, and all 28 integrated
  solutions with answers expanded. Actual six-lecture captions and numbered
  Page 1–4 labels/order, current route, practice/part/checkpoint allocation,
  sequential worked-step/example numbers, keyboard answers/checkpoints, section
  jumps, local references and print-answer expansion pass. No MathJax errors,
  exposed TeX, JavaScript errors or page-wide overflow were detected.
- Lecture 5 shared-sidebar/print regression passes **10 cases and 189 local
  article links/assets**. Two preliminary attempts encountered a transient host
  ENOSPC error while saving screenshots/creating Chromium temporary directories.
  Only disposable source-preview PNGs generated in /tmp were cleared; repository
  PDFs/files remained intact. Retrying with `TMPDIR=/tmp` completed successfully.
- All seven SVGs and both empirical figures were visually inspected in rendered
  pages. The failure-case axes were shortened to stay inside their SVG after
  inspection; final affected content was strictly rebuilt and captured again.
  The three A4 cheat-sheet pages, main student calculation, phone layout,
  semantic highlights and dark-theme output were inspected.
- Additional browser checks actually open the phone sidebar and follow Lecture 6
  Page 2, capture the final student example at 390/1440px, and verify source figures
  are present and figures are keyboard-focusable. Wide figures/tables/equations
  remain horizontally scrollable inside their containers rather than overflowing
  the entire page.
- `git diff --check` passes. No Python dependencies were added. Normal book builds
  use the committed diagram assets; regenerating the two empirical source images
  uses the existing Poppler `pdfimages` utility.

Evidence: `/tmp/math4ml-lecture6/` contains extracted text, rendered source pages,
`build.log`, `browser.log`, `regression.log` and print renders.
`/tmp/math4ml-navigation/lecture6/` contains `review.json`, mobile navigation JSON,
page/example/figure captures, dark screenshot and `cheatsheet-print.pdf`.
Figures reproduce with `tools/build_lecture6_figures.py`. Optional browser commands:

```sh
TMPDIR=/tmp PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers .venv/bin/python tools/review_lecture6.py
TMPDIR=/tmp PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers .venv/bin/python tools/review_lecture5.py
```

## Limits and remaining work

The global skill/problem blueprint, cumulative mock, recorded Lecture 2 fresh-variant
work, full supporting-exam audit, earlier-chapter standalone audit, expert review,
full accessibility audit and actual student performance remain open. Editorial
25-minute rehearsal/14-of-16 target is not an official timing or grade rule.
Genetics and eigenfaces are interpreted using the supplied illustrations; their
raw research/training arrays are not available for numerical replication.
MathJax uses its configured CDN. Chromium checks do not establish all-browser
compatibility. Week 8 is inventoried but not taught by this work.

Local preview: `book/_build/html/lecture6/index.html`. No new live deployment is
claimed; local build success does not update GitHub Pages.
