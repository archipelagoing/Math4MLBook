# Lecture 3 · Implementation and verification

Date: 2026-10-27. Local work based on commit `2d3dad1`; existing uncommitted
Lecture 2 assessment/status changes were preserved. No commit, push or publication
was performed as part of this work.

## Delivered chapter

All 35 lecture PDF pages map to Parts A–K in source order, across four numbered
sidebar pages: spaces/subspaces; complete solutions/rank; independence/span/basis;
TL;DR. Source questions/answers are included by topic, not exposed as extra pages.

The chapter contains 16 numbered worked examples with highlighted how/why steps,
11 checkpoints with hidden explanations, four original SVG diagrams, 28 integrated
practice problems with stepwise answers/diagnosis/retry links, and a formula/
condition/method cheat sheet. Three supplied recitation/assignment problems are
explicitly mapped. Other regular questions use fresh cases; four no-hint mixed
questions provide an editorial 20-minute, 16-point rehearsal with transparent
practice scoring. This is preparation material, not evidence of a student's performance.

The p. 16 Q2 particular-solution error, p. 17 intermediate arithmetic and p. 29
set/span wording are addressed explicitly. The source's exact matrix/vector data,
both rank questions, graphic-only examples and natural/tilted/change-of-basis
examples remain. See [the source and practice audit](lecture3-coverage.md).

## Verification evidence

- `.venv/bin/jupyter-book build book --all --warningiserror --keep-going` passes.
- `.venv/bin/python tools/check_lecture3.py`: **223 exact checks** pass. They cover
  displayed row operations, particular/null families, both ambient-space null
  problems, independence/completeness of generators, original column membership,
  rank/consistency/parameter cases, supplied-source corrections, fresh practice,
  basis conversion matrices/round trips, question/answer pairing and SVG structure.
  Complete affine families are verified by their exact base, null directions,
  independent free-coordinate count and consistency, not by a few parameter samples.
- Existing arithmetic/pairing regressions pass: **95 checks for Lecture 1** and
  **98 for Lecture 2**. Their reader content was not rewritten for this chapter.
- `tools/review_lecture3.py` uses the shared Chromium review: **10 page/viewport
  checks** (welcome plus four pages at 1440 and 390 pixels), **239 local article
  links/assets**, zero MathJax errors, zero JavaScript errors, zero page-wide
  overflow, including with all answers expanded. Actual sidebar captions and
  Page 1–4 labels, per-page practice/part allocation, all 16 example numbers and
  sequential step labels, keyboard-opened checkpoints/answers, section jumps,
  print-answer expansion and a dark-theme screenshot pass.
- Additional browser inspection captures all four figures and worked Examples
  3.5/3.7/3.15. The phone sidebar was opened and its Page 2 link followed successfully.
- Temporary evidence: `/tmp/math4ml-lecture3/build.log`, source-page PNGs, figure/
  example captures; `/tmp/math4ml-navigation/lecture3/review.json`, desktop/mobile
  screenshots and `cheatsheet-print.pdf`. Rendered figures and representative
  worked steps were visually inspected, not inferred from source markup alone.

Run the same arithmetic/build commands to reproduce. Optional browser review uses
`PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers .venv/bin/python tools/review_lecture3.py`
with Playwright/Chromium installed. Browser tooling is not a book build dependency.
Original figures regenerate with `tools/build_lecture3_figures.py`.

## Limits and remaining work

Coverage is complete for this lecture and selected supporting problems, not for
every homework or practice exam. Recitation 2 Problem 4's orthonormal/projection
material belongs to Lecture 4. Course-wide mock-exam/assessment mapping and
Lecture 2's recorded readiness tasks remain open. Independent expert review,
measured learner comprehension, a full accessibility audit and live GitHub Pages
verification have not been performed. MathJax still uses its configured CDN.
The cheat sheet was reviewed across its three A4 print sheets, including table
contrast, equations and worked-step/result boundaries. One website cheat-sheet
page need not be one physical printed sheet.
