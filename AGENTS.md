# Math4MLBook · Agent instructions

These instructions apply throughout this repository. User instructions take
priority. Read this file before editing, then the **Current authoring contract**
near the start of `SHOW_BIBLE.md`, `rubricatm.md`, and the relevant tasks in
`todoSimple.md`. Older show-bible decisions are history where the current
contract supersedes them. Do not infer current requirements from an old appendix.

## Purpose and source of truth

Write a professional educational textbook that prepares this student to solve
unfamiliar exam problems independently, aiming for an A. Build an accompanying
cheat sheet that helps the student select and execute methods. Accuracy,
source coverage, clarity, and useful practice matter as much as appearance.

- Course PDFs: `resources/lectures/`; supporting work: `resources/HW/` and
  `resources/practiceExams/`. Preserve the original files.
- Product/editorial rules: `SHOW_BIBLE.md`; assessment: `rubricatm.md`;
  implementation status: `todoSimple.md`.
- Analogy: `analogy/systems/shadows/canon.md` and `analogy/teaching-strategy.md`.
- Reader pages and source fragments: `book/lectureN/`.
- Actual sidebar/page order: `book/_toc.yml`. Headings in Markdown alone do
  not update the sidebar.
- Coverage and verification records: `authoring/lectureN-coverage.md` and
  `authoring/lectureN-review.md`.

## Full lecture coverage and teaching flow

1. Read the **entire** lecture deck. Map every topic, formula, condition, property,
   distinct example, and meaningful handwritten annotation to a textbook location.
   Combine title pages/progressive reveals without omitting their substance.
2. Follow lecture topic order. Use visible lettered parts for new lecture units;
   preserve established section labels and anchors when reorganizing existing work.
   Do not turn a user's list of salient topics into an unrequested scope limit.
3. Explain concrete examples before generalizing. Keep one running example where
   useful; identify any switch to another example. Explain prerequisites or reorder
   only as much as necessary, documenting the reason.
4. Each concept needs a goal, source-page reference, clear explanation and precise
   definition/result, a checkpoint with an expandable answer, takeaway and practice.
5. Every worked method needs numbered, visibly highlighted action steps. Each
   step names the operation and explains **how and why** it is done. Show intermediate
   arithmetic/matrices and the original-problem check. State conditions and failure
   cases. A list of bold final answers is insufficient.
6. Keep the prose concise and connected. Do not replace the teaching sequence with
   a formula sheet or remove source examples merely to shorten it.
7. Assume the reader has **only the website open**, without the slides or lecture
   audio. When referring to a source example, include its complete problem data,
   notation and worked reasoning on the textbook page. When referring to a source
   figure, include a faithful, labeled textbook diagram with a caption and alt text,
   explaining what the reader should notice. Page citations provide attribution;
   they must never substitute for essential content. Check each page with the PDF
   closed; restate or explicitly link any earlier textbook definition it needs.

## Sidebar and page architecture

- Maximum **four reader pages per lecture**, counting review/practice destinations.
  This is a website navigation limit, not a physical print-sheet limit.
- Group pages under an explicit lecture caption in the sidebar. Label them
  **Page 1**, **Page 2**, **Page 3**, **Page 4**, followed by informative topic names.
  Mirror the order and titles in the on-page route and welcome page.
- Split at natural consecutive lecture-topic boundaries. Do not organize the
  navigation as detached `Exercises` and `Solutions` pages.
- Place relevant practice after its topic, with the explained solution expandable
  immediately beside/below the problem. Keep practice and answers available in
  print. Source question/answer files may be included fragments; they are not
  additional reader pages.
- Finish each lecture with a dedicated **TL;DR cheat sheet**: key formulas and
  their conditions, method-selection cues, stepwise recipes/stopping rules, a
  compact worked example, and common errors.
- Current routes:
  - Lecture 1: vectors/combinations → dot products/geometry → matrices/products → TL;DR.
  - Lecture 2: systems/elimination → determinants/geometry → inverses/invertibility → TL;DR.
  - Lecture 3: spaces/subspaces → complete solutions/rank → independence/span/basis → TL;DR.
  - Lecture 4: orthogonality/projections → subspaces/least squares → orthonormal bases/Gram–Schmidt → TL;DR.
  - Lecture 5: eigenvalues/diagonalization → SVD → reduction/recommendations/final in-class exercises → TL;DR.
  - Lecture 6: statistics/PCA geometry → compute principal components → scaling/applications/pitfalls → TL;DR.
- Keep problem IDs, solution IDs, and concept anchors stable when moving content.
  Use MyST references so destinations follow the moved labels. Avoid stale direct
  links to source-only practice/solution fragments.

## Visual and mathematical conventions

- Preserve the established palette: blush paper, warm cocoa text, hot pink and
  bright green accents, **blue structure**, **yellow important results**,
  **red pitfalls**. Use the contrasting foreground/dark-theme pairs already in CSS.
- Use `worked-step`, `step-label`, and `key-answer` for procedural examples.
  Labels and mathematical meaning must remain clear without color.
- Use original reproducible SVG/plot diagrams with captions and meaningful alt
  text. Do not use screenshots of formulas as textbook mathematics.
- Shadows mean calibrated parallel-ray views of matched labeled points, fixed
  axes and one declared origin. Distinguish point coordinates from profiles.
  Rectangular O/H have no determinant or two-sided inverse; use declared square
  maps for those concepts. Never imply arbitrary silhouette reconstruction.
- Keep vector orientation, matrix dimensions, variable order, and assumptions
  explicit. Verify sign-sensitive arithmetic and parameters exactly.

## Implementation and verification

Use the existing Python 3.12 / TeachBooks / Jupyter Book v1 / MyST stack and
pinned `requirements.txt`. Use `.venv` when present. Do not replace the framework
or add dependencies for routine authoring work.

1. Inspect the working tree. Preserve unrelated and existing user changes.
2. Draft the source/page map and coherent material; update `_toc.yml` when routes move.
3. Recompute examples and solutions using `tools/check_lectureN.py`. Extend useful
   checks for new arithmetic, not assertions that merely repeat the prose.
4. Build strictly:

   ```sh
   .venv/bin/jupyter-book build book --all --warningiserror --keep-going
   ```

5. Run the affected `tools/review_lectureN.py` browser review when available.
   Verify actual left-sidebar labels/order, four-page routes, desktop (1440px)
   and phone (390px), MathJax, local links/fragments, keyboard-opened answers,
   step highlighting, dark mode and print. Inspect representative screenshots.
   In this development environment Chromium uses `PLAYWRIGHT_BROWSERS_PATH=/tmp/math4ml-browsers`.
   Browser review is optional tooling, not a book build dependency; request the
   required sandbox permission if Chromium cannot launch normally.
6. For shared changes, run relevant existing regression checks. Do not claim a
   check passed if it was not run or if tooling blocked it.
7. Update coverage, review evidence, current show-bible state, rubric and checklist.
   Distinguish delivered source coverage from homework alignment, expert review,
   learner outcomes and the live site. Do not append conflicting current rules
   into a historical section instead of updating the current contract.

Do not commit, push, or publish unless authorized. Local HTML under
`book/_build/html/` is not proof of a GitHub Pages update. Report the local preview
and whether publication was performed. Do not modify `.gitignore` or stage extra
files as a side effect of chapter work.
