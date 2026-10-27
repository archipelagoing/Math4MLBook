# Lecture 2 · Full-deck implementation and verification

Date: 2026-10-27. Local work based on `e5b7724`, preserving the prior uncommitted
flow revision and expanding it to the newly requested full lecture. Not pushed or
published; no live GitHub Pages verification is claimed.

## Delivered

- Four numbered topic/review pages: A–D systems/elimination; E–H determinants/
  geometry; I–N inverses/invertibility; TL;DR. Sidebar lecture captions and Page 1–4
  labels mirror the on-page route. Practice banks are included by topic; each
  explained answer is expandable immediately below its question. Neither source
  bank is a standalone sidebar page.
- All 36 Week 2 PDF pages mapped in [the coverage audit](lecture2-coverage.md).
  Title pages/progressive reveals are consolidated. No systems-only scope limit remains.
- 14 lettered parts in source order, 14 checkpoints, three original SVG diagrams,
  and 17 worked examples (including the cheat-sheet example). Every example has
  numbered highlighted steps explaining what to do and how/why it works.
- Example 2.6 is one continuous six-step main-system solve, with blue action labels,
  row-operation explanations, optional RREF continuation, original-equation checks,
  and a yellow result panel. Existing practice/concept anchors remain valid.
- Full source determinant properties, both Laplace formulas, geometry, inverse
  definition/tests, Gauss–Jordan construction, cofactor recipe, 2×2 formula, and
  all source 3×3 minor/cofactor/adjugate/inverse arrays retained and checked.
  The p. 6 handwritten two-equation substitution check also has highlighted steps.
- TL;DR collects formulas with conditions, method selection, stopping rules,
  solution classification, error cues and a complete compact solve. The practice
  bank expands from 18 to 26 problems with hints, answers, review and retry links.

## Verification

- Strict Jupyter Book build with `--all --warningiserror --keep-going` passes.
- `tools/check_lecture2.py`: **98 checks** pass, including exact system arithmetic,
  independently computed permutation-sum determinants, minors/cofactors/adjugate,
  both inverse products, each inverse-elimination stage, parameter families,
  singular-system alternatives, geometry, and reader/practice structure.
- `tools/check_lecture1.py`: **95 checks** pass.
- `tools/review_lecture2.py` now uses shared `review_textbook.py` to verify
  actual sidebar page labels/order/captions, four-page topic routes, parts and
  practice allocation, preserved numbered examples and IDs, keyboard-opened
  answers/checkpoints, references, and print answer exposure. All answers are
  expanded for mobile overflow checks. New evidence is recorded under
  `/tmp/math4ml-navigation/lecture2/`; older full-deck evidence remains historical.


Reproduce with `.venv/bin/python tools/check_lecture2.py`, the strict book build,
and (with optional Playwright/Chromium installed)
`PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers .venv/bin/python tools/review_lecture2.py`.
Browser dependencies are review tooling, not book build dependencies.

## Limits

This establishes local source coverage and authoring checks, not measured student
comprehension, independent expert review, a full accessibility audit, official
exam-cutoff compliance, or a live-site deployment. Supporting homework and exam
blueprint mapping remain separate work. MathJax uses its configured CDN. The
cheat sheet is one website page; print output is not constrained to one physical
sheet and is not a dedicated typeset edition.

## Numbered-navigation verification · 2026-10-27

The strict build and current browser checks pass. The browser inspected the real
left-sidebar captions/Page 1–4 labels and the topic allocation of questions and
answers, not just the Markdown route. All original examples and solution IDs
remain available; answers were keyboard-opened and all were expanded for mobile
overflow checking. Desktop and mobile screenshots were visually reviewed.

This run covered 10 page/viewport combinations and 266 local article
links/assets, with zero MathJax errors, JavaScript errors or page-wide overflow.
