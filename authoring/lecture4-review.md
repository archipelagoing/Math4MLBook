# Lecture 4 · Implementation and verification

Date: 2026-10-27. Based on commit `718e1b7`; working tree was clean before this
chapter. No commit, push or publication was performed. Lecture 3 was separately
verified live at its `/main/lecture3/index.html` Pages URL; that deployment does
not contain these local Lecture 4 changes.

## Delivered

All 28 Week 4 PDF pages map to Parts A–K, preserving source order. The four
numbered sidebar pages are orthogonality/projections, subspaces/least squares,
orthonormal bases/Gram–Schmidt, and TL;DR. Topic practice and answers are included
fragments; there are no additional Exercises/Solutions sidebar destinations.

Fourteen numbered worked examples use blue action labels and yellow conclusions.
Eleven part-level checkpoints, six original reproducible SVGs and 28 integrated
questions develop the full topic set. Answers explain operations, verification,
specific error diagnoses and revision/retry links. Four no-hint mixed problems
include transparent editorial timing/scoring rather than invented course policy.
The final page collects formulas with conditions, method selection, fit and basis
recipes, stopping checks, a compact example and pitfalls.

[The coverage record](lecture4-coverage.md) maps every source page, numerical case,
selected worksheet/recitation question and editorial clarification. Symmetric
idempotent orthogonal projectors are distinguished from general idempotent maps;
independence hypotheses, unique output/nonunique coefficients, rectangular Q,
vertical least-squares gaps, and zero Gram–Schmidt remainders are explicit.

## Checks performed

- Strict full rebuild passes using
  `.venv/bin/jupyter-book build book --all --warningiserror --keep-going`.
- `tools/check_lecture4.py` passes **409 checks**. Exact Fraction arithmetic
  independently solves normal equations, reconstructs fitted outputs/residuals,
  checks squared errors and Pythagoras, verifies all projection matrices and
  complementary projectors, and compares alternative candidate fits. It recomputes
  source/worksheet/fresh Gram–Schmidt stages, checks pairwise perpendicularity
  and preservation of the original span, handles redundant inputs and verifies
  the complete dependent-column families by their base and null direction.
  Normalized source vectors/rotations additionally have numerical inner-product
  checks; symbolic reasoning and hypotheses are given in the chapter.
- Earlier arithmetic regressions pass: **95 Lecture 1**, **98 Lecture 2** and
  **223 Lecture 3** checks. Shared changes add the fourth caption/routes and extend
  the existing cheat-sheet print selectors; existing chapter content is preserved.
- `tools/review_lecture4.py` passes **10 page/viewport checks** at 1440 and 390px,
  with **181 local article links/assets**, no MathJax or JavaScript errors and no
  page-wide overflow, including with all 28 answers expanded. Actual numbered
  sidebar labels/order, current-route markers, part/checkpoint counts, example
  numbers/sequential steps, practice allocation, keyboard-opened answers and
  checkpoints, local section jumps and print-answer expansion are checked.
- The browser reviewer now additionally detects exposed LaTeX in Lecture 4 prose.
  Visual print inspection caught adjacent display blocks swallowing text even
  without a MathJax error. Paragraph breaks were corrected throughout the new
  chapter; a strict rebuild and browser review confirmed the fix.
- Main source Examples 4.8 and 4.12 and all six diagrams were captured and
  visually inspected. The Gram–Schmidt input and unit-vector lists use aligned
  vertical displays to improve phone reading. Final affected examples were checked
  again after that layout adjustment.
- The 390px sidebar was opened and its Lecture 4 Page 2 link clicked successfully;
  final mobile/example evidence is in `mobile-navigation.json` and the clean
  example captures alongside the main browser record.
- Shared navigation/print regression: `tools/review_lecture3.py` passes its 10
  desktop/phone checks and **244 local article links/assets** with the four-lecture
  sidebar present. Previous browser evidence is historical, not overwritten in
  the chapter’s dated prose.
- Dark-theme screenshots and all **three A4 cheat-sheet print pages** were
  inspected: readable tables, rendered formulas, highlighted steps/results and
  no duplicated print-title block. One website page need not fit one paper sheet.
- `git diff --check` passes.

Temporary evidence: `/tmp/math4ml-lecture4/` contains extracted source text,
rendered source pages, build log references and print-page renders;
`/tmp/math4ml-navigation/lecture4/` contains `review.json`, desktop/phone captures,
main-example and figure captures, dark screenshot and `cheatsheet-print.pdf`.
Build log: `/tmp/math4ml-lecture4-build.log`; browser logs:
`/tmp/math4ml-lecture4-browser.log` and `/tmp/math4ml-lecture4-regression.log`.
Optional Chromium tooling uses
`PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers`; it is not a book build dependency.
Figures regenerate with `tools/build_lecture4_figures.py`.

## Limits

Source coverage and selected supporting-question alignment are delivered; a full
course-wide exam blueprint, independent expert review, actual student performance,
full accessibility audit and later chapters are not established by these checks.
MathJax uses its configured CDN. Wide equations, figures and tables may scroll
inside their containers on narrow screens. Publication of Lecture 4 has not been
performed; inspect `book/_build/html/lecture4/index.html` for the local build.

## Standalone reading follow-up · 2026-10-27

Added the website-only reading gate to the authoring instructions, current show
bible and rubric. Lecture 4 now has six reproducible SVGs: new four-space and
subspace-projection figures accompany the relevant explanation instead of relying
on a source-picture reference. Restated the H model on Page 2 and added explicit
textbook links on Page 3. The updated arithmetic/asset checker passes 409 checks;
initial 405-check and 175-link results above describe the preceding revision.
Earlier chapters have not received a new slides-closed audit in this follow-up.

Follow-up verification: the strict build and 409-check arithmetic/asset run pass.
The updated browser review passes all 10 desktop/phone cases and 181 local
links/assets, with no MathJax errors, exposed LaTeX, JavaScript errors or page-wide
overflow. Both added figures were visually inspected; the null-space arrow label
was moved clear of its line. Lecture 4 remains local and unpublished.
