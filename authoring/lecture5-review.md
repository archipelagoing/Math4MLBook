# Lecture 5 · Implementation and verification

Date: 2026-10-27. Initial checkout was `718e1b7` with the existing Lecture 4 work.
The user committed Lecture 4 as `f395bc4` during this task; that work was preserved.
Unrelated `.DS_Store` changes were not staged or removed. No commit, push or
publication was performed by the agent. Lecture 5 is a local addition.

## Delivered chapter

All 44 source PDF pages map to ten ordered Parts A–J on four numbered topic/review
pages. This includes the text-extraction-invisible handwritten example on p.22,
all source matrix/vector data, the complete rating and genre-feature tables, and
both final in-class exercises on pp.43–44. Fifteen numbered worked examples use
blue action labels, intermediate calculations, verification and yellow results.
Ten checkpoints, six original SVGs, 28 integrated questions with explained answers
and targeted diagnostic/retry links, a fresh mixed rehearsal, and a dedicated
method/condition/recipe cheat sheet support independent study.

Relevant pictures are redrawn with captions and alt text, rather than requiring
the slides alongside the website. The source’s full/compact shape ambiguity,
general-diagonalization orthonormality note, repeated-eigenvalue perpendicularity
claim, real-rotation wording and movie-score interpretation are clarified.
See [the source/practice audit](lecture5-coverage.md) for all destinations and
source-versus-editorial boundaries. Statistics/PCA is explicitly still untaught.

## Validation

- Strict full build passes:
  `.venv/bin/jupyter-book build book --all --warningiserror --keep-going`.
  An initial build caught two unintended Markdown links in prose describing
  matrix products; those source-note strings were corrected before the passing run.
- `tools/check_lecture5.py` passes **632 checks**. Exact Fraction operations verify
  matrix products, eigenpairs, independence and complete eigenspace dimensions,
  characteristic trace/product conditions, diagonalization products, the handwritten
  spectral reconstruction, source/worksheet/variant Gram matrices, zero/tied/
  negative/rectangular cases, rank-deficient null bases, truncation arithmetic,
  source feature scores, data retention, bank pairing and SVG structure.
  Full SVDs are additionally reconstructed numerically from normalized chosen
  right directions and independently computed left directions, with all entries
  checked at 1e−11 tolerance and all left orthogonality products checked. The
  zero case avoids division. These are mathematical checks, not a claim of
  independent expert review or a numerically stable production SVD algorithm.
- Existing checkers pass: **95 Lecture 1**, **98 Lecture 2**, **223 Lecture 3**,
  **409 Lecture 4**. All five together have 1,457 checks. Prior content and source
  PDFs were preserved; shared changes add routes and extend cheat-sheet selectors.
- `tools/review_lecture5.py` passes **10 page/viewport cases** (welcome and four
  reader pages at 1440 and 390px) and **183 local article links/assets**. Actual
  five-lecture sidebar captions and Page 1–4 labels, active route, per-page parts/
  checkpoints/practice, all example numbers/sequential action labels, keyboard
  checkpoint/answer opening, section jumps and print-answer expansion pass.
  There are no MathJax errors, exposed LaTeX, JavaScript errors or page-wide
  overflow, including with all 28 answers expanded on phones.
- Shared regression: `tools/review_lecture4.py` passes its ten cases and **186
  local links/assets** with the five-lecture sidebar. This does not repeat a full
  mathematical/source audit of Lectures 1–4.
- All six rendered diagrams, representative source/worksheet worked examples,
  phone layouts, dark-theme cheat sheet and **all three A4 print pages** were
  visually inspected. A rotation-axis label was moved clear of its heading and
  the factor-shape caption was corrected to match the full/compact diagram.
  Final affected pages were strictly rebuilt and inspected again.
- The phone sidebar’s Lecture 5 Page 2 link is checked by an actual click, with
  clean desktop/phone captures of the worksheet and final in-class SVD examples.
- `git diff --check` passes. No new dependencies were added.

Evidence: `/tmp/math4ml-lecture5/` contains extracted/rendered source pages,
`build.log`, `browser.log`, `regression.log` and print-page renders.
`/tmp/math4ml-navigation/lecture5/` contains `review.json`, page/figure/example
captures, dark screenshot, `cheatsheet-print.pdf` and mobile navigation evidence.
The reviewer checks layout and MathJax in Chromium with
`PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers`; this optional tooling is not a
book build dependency. Figures regenerate with `tools/build_lecture5_figures.py`.

## Remaining limits

All five lecture decks now have implemented destinations, but that is not the
same as complete exam preparation. The statistics/PCA supplement, comprehensive
exam blueprint, cumulative mock, remaining Lecture 2 fresh-variant tasks,
independent expert review and actual learner performance remain open. Editorial
practice timing/scoring is not course grading policy. Wide tables/equations/
figures can scroll within their containers on phones. MathJax uses its configured
CDN. No full accessibility audit or browser-engine compatibility claim is made.

The source recommendation numbers demonstrate weighted feature arithmetic, not
validated rating prediction or a literal orthogonal SVD of the incomplete source
table. No new live deployment has been verified. Local preview:
`book/_build/html/lecture5/index.html`.
