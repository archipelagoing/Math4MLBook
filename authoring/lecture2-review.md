# Lecture 2 · Implementation and verification

Date: 2026-10-27. Local work based on commit `a8cbdf7`; not published or pushed.

## Delivered scope

Four reader pages: systems/modelling, elimination/echelon forms, 18 exercises,
and explained solutions. Eight sections, definitions and key results, a short
reversible-operations proof, eight worked examples, eight checkpoints with hidden
answers, section recaps, three original SVG diagrams, readiness map and source notes.
The supplied Week 2 systems material is PDF pp. 1–21; determinants/inverses from
pp. 22–36 remain open. See [the source audit](lecture2-coverage.md).

## Verification

- `.venv/bin/jupyter-book build book --all --warningiserror --keep-going` passes.
- `.venv/bin/python tools/check_lecture2.py`: **64 checks** of exact arithmetic,
  main reduction matrices, independent RREF calculations, source and practice
  substitutions, affine-family base/directions, consistency, and page structure.
- `.venv/bin/python tools/check_lecture1.py`: **93 checks** pass unchanged.
- `tools/review_lecture2.py` checks the welcome page and four Lecture 2 pages at
  1440 and 390 pixels: **10 page/viewport checks**, zero MathJax errors, zero
  page-wide overflow, zero JavaScript errors. **211 article links/assets** resolve,
  including fragment targets. Four-page route/current markers, eight teaching
  section structures/examples, keyboard checkpoint opening, section jumps, and
  solution return links pass.
- Reviewed all three rendered figures, a worked example, mobile section/page
  screenshots, dark mode, and a browser print preview. Print exposes checkpoint
  answers. Wide mathematics and diagrams scroll inside their own containers on
  small screens. Printing from dark mode now forces legible dark panel titles
  and suppresses panel shadows. A long inline source path initially overflowed; inline code can
  now wrap without changing preformatted code blocks.
- Lecture 1's browser script now scopes its four-page sidebar assertion to the
  current chapter, since the book contains a second chapter. All ten Lecture 1
  page/viewport checks pass, including its 12 examples/checkpoints and return links.

Reproduce browser review with Playwright/Chromium installed, using
`PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers .venv/bin/python tools/review_lecture2.py`
in the current development environment. Optional browser packages are not book
build dependencies. Temporary review evidence is under `/tmp/math4ml-lecture2/`:
`browser-review.json`, figure/page screenshots, and `elimination-print.pdf`.

## Limits

These checks support local authoring quality; they are not an independent expert
review, learner effectiveness study, full accessibility audit, or confirmation of
live GitHub Pages. No official timed exam blueprint or supporting-homework problem
map has been completed. MathJax's configured CDN needs internet access. Print is
usable browser output rather than a dedicated typeset edition; the four-page
limit applies to website navigation, not printed sheets.
