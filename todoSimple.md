# Math4MLBook TODO

Last updated: 2026-10-26. The course resources and TeachBooks scaffold are present.
The show bible and rubric now define the textbook target; this checklist translates
them into ordered work. Weekly textbook chapters, custom design, and a successful
local build have not yet been completed or verified. This pass prepares the three
planning documents only; the implementation backlog remains unfinished.

## Maintenance instructions

- Read the current user request, [SHOW_BIBLE.md](SHOW_BIBLE.md), and relevant sources
  before work. Use [rubricatm.md](rubricatm.md) for quality assessment.
- Keep this as the authoritative checklist. Use `[x]` only when the stated outcome
  has evidence; keep unverified tasks open and name the missing check.
- After meaningful authorized work, update affected tasks, progress notes, next
  steps, and this date. Preserve unrelated work and owner edits.
- Keep each task in one section. Next steps summarize priorities without creating
  duplicate task statuses. Do not treat this backlog as authorization to publish,
  push commits, or execute unrelated work.
- Link source pages, chapter files, rendered artifacts, calculations, or command
  results in progress notes. Distinguish local success from deployed behavior.
- Preserve source PDFs, identify additions/corrections, and never invent source
  coverage or successful checks. Reassess the rubric after meaningful milestones.

## Next steps

1. Complete the detailed source map and notation conventions (§2), including the
   visual-only PDFs and statistics/PCA coverage gap.
2. Verify an isolated local build and establish shared reading styles (§3).
3. Build and inspect a complete Week 1 chapter (§4); refine the chapter pattern
   before proceeding through Weeks 2–5.
4. Complete the remaining weekly chapters in order (§§5–8), then close the midterm
   coverage map (§9).

The broad weekly sequence and proposed design direction are ready. Exact
section/page mapping, rendered appearance, and mathematical verification remain
implementation work. No chapter writing or site publication is included in this
planning pass.

## 1. Define the project

- [x] Fill `SHOW_BIBLE.md` with audience, premise, scope, source hierarchy,
  chapter format, mathematical rules, proposed design, and definition of done.
- [x] Fill `rubricatm.md` after the bible with project-specific criteria totaling
  100 and an evidence-based initial assessment.
- [x] Fill `todoSimple.md` after the rubric with ordered tasks and honest statuses.
- [x] Separate observed template behavior from planned textbook features.

Progress: Completed on 2026-10-26 in the requested order. Inspected source state at
`6657df146cf1bfa98d515d6f192ce16aa6d0d806`; the rubric records a provisional 10/100
baseline. Proposed palette, working title, and future chapter paths are design
choices recorded for implementation, not shipped features.

## 2. Audit sources and establish the learning map

- [x] Inventory all five lecture decks, six homework/recitation/worksheet PDFs,
  seven practice-exam PDFs, and the midterm topic list.
- [x] Extract available PDF text and identify sources needing visual inspection.
- [ ] Visually inspect `Recitation1_Solutions.pdf` and `PT1_f22Sol.pdf`; capture
  reliable page/problem references and any necessary transcriptions.
- [ ] Review diagrams and annotations in the other PDFs that extraction can miss.
- [ ] Create a persistent section-level source map with exact filenames, one-based
  PDF page ranges, supporting problem references, and planned chapter destinations.
- [ ] Map each `MidtermTopics.md` item to a source and learning destination; locate
  statistics/PCA support or define a labeled supplement with prerequisites.
- [ ] Publish a notation convention/reference and list prerequisites so symbols
  and dependencies remain consistent across weekly chapters.
- [ ] Record source discrepancies, needed corrections, and source/figure credits.

Progress: All 18 PDFs were processed with `pdftotext -layout` on 2026-10-26. Lecture
page counts are 48/36/35/28/44. Temporary extraction artifacts are not a persistent
source map. Two PDFs yielded no text; no claim is made that their pages are blank.
Week 5 text covers eigendecomposition/SVD, while statistics/PCA appear in the
midterm list and need further source review. Homework PDFs contain worked
solutions that must still be independently checked.

## Connected knitting-and-crochet analogy system

- [x] Create [ANALOGY_WEB.md](ANALOGY_WEB.md) as the separate source of truth for the
  actual stitch actions, cast-on/bind-off, magic-ring rounds, swatches/gauge,
  connected graph, precise mappings, and limitations.
- [x] Create [ANALOGY_RUBRIC.md](ANALOGY_RUBRIC.md) with weighted criteria and an
  honest assessment separate from the main textbook rubric.
- [x] Check the revised stitch-ledger examples, count transformations, gauge
  statistics, and action graph's structural connectivity.
- [ ] Map analogy IDs to exact course pages/problems and eventual chapter passages;
  register every additional taught concept discovered during source review.
- [ ] Develop each mapping into chapter explanations with formal mathematical
  landings, useful callbacks, clear boundaries, and checked transfer questions.
- [ ] Review difficult mappings for mathematical and craft misconceptions; inspect
  graph rendering and accessible equivalents, and audit cross-chapter consistency.
- [ ] Gather reader/reviewer evidence of transfer to fresh exam problems and update
  the specialized rubric, without treating editorial completion as a grade guarantee.

Progress, 2026-10-26: Replaced the owner-rejected generic studio model with
`Yarn in Your Hands`: specific stitch operations and fixed knitted/crocheted
projects. The revised rubric prioritizes actual craft mechanisms and mathematical
boundaries. Checked terminology/gauge/magic-ring references and recalculated the
new stitch-ledger, basis, projection, SVD, and gauge examples. The old feature-model
anchors are superseded. Physical samples, loop diagrams, exact course-page mapping,
qualified review, chapter integration, and learner transfer remain pending.

## Additional connected analogy references

- [x] Create [the bacteria/virus canon](ANALOGY_BACTERIA_VIRUSES.md) and
  [its rubric](ANALOGY_BACTERIA_VIRUSES_RUBRIC.md), grounded in actual division,
  infection, lysis, compartment counts, and measurement limitations.
- [x] Create [the astrological-wheel canon](ANALOGY_ASTROLOGICAL_WHEEL.md) and
  [its rubric](ANALOGY_ASTROLOGICAL_WHEEL_RUBRIC.md), grounded in degree placements,
  aspects, declared house conventions, rotations, and chart records.
- [x] Create [the original pottery canon](ANALOGY_POTTERY.md) and
  [its rubric](ANALOGY_POTTERY_RUBRIC.md), grounded in clay preparation, wheel
  actions, profiles, trimming, stage measurements, and fired pieces.
- [x] Check original numerical anchors, graph connectivity, local links, and rubric
  arithmetic; distinguish domain-source facts from invented models/data.
- [ ] Complete exact course-page/manuscript mapping and formal edge-case examples
  for each additional lens as it is selected for chapter development.
- [ ] Develop annotated domain figures and transfer questions; obtain relevant
  independent domain/math review and gather learner evidence.

Progress, 2026-10-26: Six new documents provide three separate complete-scope
analogy drafts and domain-specific rubrics. Domain sources were consulted and
linked; mathematical anchors checked with exact arithmetic/structural identities.
Graph rendering, empirical examples, qualified review, chapter integration, and
learner effectiveness remain unverified. Knitting/crochet stays the primary
thread; additional lenses can be selected without repeating all four everywhere.

## 3. Establish the book and visual foundation

- [ ] Create an isolated Python environment, install the repository requirements,
  verify the CLI, and record a reproducible local build command.
- [ ] Build the existing scaffold and record a warning/error baseline before
  substantial changes; identify dependency or configuration issues.
- [ ] Replace template identity, repository links, base URL, and opening page with
  the textbook's working identity and an accurate reader guide.
- [ ] Replace reader navigation with the planned weekly structure; remove template
  tutorials from reader navigation while retaining useful authoring references.
- [ ] Implement shared typography, spacing, palette, light/dark tokens, and named
  teaching components from the bible; verify stylesheet loading.
- [ ] Establish mathematical figure conventions: axes, labels, line styles,
  captions, alt text, and reproducible vector/plot sources.
- [ ] Provide useful search, chapter/section navigation, visible keyboard focus,
  controlled equation overflow, and printable solutions.

Progress: `requirements.txt`, `book/_config.yml`, `book/_toc.yml`, and the deployment
workflow exist. No build executed; `teachbooks` and `jupyter-book` were absent from
the inspected PATH. The existing template enables notebook execution “off” and
image inversion; any new notebook calculations or colored diagrams need explicit
verification. The bible's palette and typography remain proposals. On 2026-10-26,
the owner refined the cute palette to hot pink (`#FF4FA3`), bright green
(`#8DEB42`), warm caramel brown (`#A5633D`), and yellow on blush paper with
deep warm cocoa text (`#543124`). Structural accents use blue (`#3975DB`). Red is reserved for attention cues; yellow highlights
important material. Calculated light-palette contrast now supports deep pink
(`#C91E70`) and leaf green (`#357D22`) foregrounds plus cocoa text on pale
pink/green panels; exact ratios and usage rules are in the bible. Rendered
contrast, interaction-state, and dark-theme checks remain part of implementation.

## 4. Week 1 — Vectors and matrices

- [ ] Draft a chapter opener, prerequisites, objectives, and a section sequence
  mapped to `WK1_ Vectors and Matrices.pdf`.
- [ ] Develop vector representation, addition/scaling, linear combinations, dot
  product and angles, norm, and normalization into connected prose.
- [ ] Develop matrix dimensions, diagonal/identity/symmetric matrices, addition,
  scaling, transpose, trace, matrix-vector and matrix-matrix products/properties.
- [ ] Add complete checked examples for the major methods, including dimension
  checks, zero-vector limitations, and noncommutativity where relevant.
- [ ] Create labeled figures connecting vector geometry and matrix operations to
  their equations; include useful, prerequisite-appropriate ML interpretation.
- [ ] Add conceptual checkpoints, common pitfalls, summary, graduated practice,
  hints, and independently checked solutions aligned to objectives.
- [ ] Verify source coverage, mathematics, references, and build output; inspect
  desktop, narrow viewport, dark theme, keyboard use, and browser print.
- [ ] Refine the shared chapter pattern from the rendered result and update the
  bible/rubric/checklist to match verified implementation.

Progress: Scope mapped at whole-deck level (48 pages); no Week 1 manuscript or
rendered prototype yet. This is the first complete editorial and visual milestone.

## 5. Week 2 — Systems, determinants, and inverses

- [ ] Develop systems, column interpretation, augmented matrices, elementary row
  operations, elimination, echelon forms, pivots, and back substitution.
- [ ] Explain unique/inconsistent/infinitely many solution cases with appropriate
  examples, distinguishing a needed row swap from actual singularity.
- [ ] Develop determinants, expansion/properties, area/volume interpretation,
  invertibility, Gauss–Jordan, and cofactor inverse formulas with assumptions.
- [ ] Integrate mapped homework/recitation examples, figures, checkpoints,
  misconceptions, summary, graded practice, hints, and checked solutions.
- [ ] Meet the chapter definition of done, including independent computations,
  source mapping, a successful build, and rendered inspection.

Progress: Primary deck has 36 pages. Supporting homework contains elimination,
invertibility, and parameter-dependent systems; exact problem mapping remains open.

## 6. Week 3 — Vector spaces, rank, and bases

- [ ] Develop vector spaces/subspaces with valid examples and counterexamples;
  connect span, linear independence, bases, and dimension.
- [ ] Explain the four fundamental subspaces and their ambient dimensions, rank,
  pivots/free variables, and complete solutions to `Ax=b`.
- [ ] Develop coordinate representations and change of basis with an explicit
  direction convention and verified examples.
- [ ] Integrate source-mapped figures, worked examples, checkpoints, common
  misconceptions, synthesis, graduated exercises, hints, and checked solutions.
- [ ] Meet the chapter definition of done and verify dependencies on Weeks 1–2.

Progress: Primary deck has 35 pages. Textbook sections and practice are not written.

## 7. Week 4 — Orthogonality, projections, and least squares

- [ ] Explain orthogonal vectors/subspaces and the orthogonality relationships
  among the four fundamental subspaces, with dimensions stated.
- [ ] Derive line and subspace projections; explain residual orthogonality and
  the full-column-rank condition for inverse-based projection formulas.
- [ ] Develop least squares and the normal equations through the slides' line-fit
  example; discuss rank-deficient limitations at the appropriate depth.
- [ ] Explain orthonormal bases and Gram–Schmidt with checked computations and
  the linear-independence requirement.
- [ ] Integrate figures, checkpoints, pitfalls, synthesis, appropriate ML context,
  graded exercises, hints, and independently checked solutions.
- [ ] Meet the chapter definition of done and verify earlier cross-references.

Progress: Primary deck has 28 pages. Projection and least-squares diagrams are a
major opportunity for the shared visual language; no figures have been built yet.

## 8. Week 5 — Eigenvalues and matrix decompositions

- [ ] Develop transformation geometry, eigenvalues/eigenvectors, characteristic
  equations, eigenspaces, and checked computation methods.
- [ ] Explain diagonalization conditions and counterexamples; state the real
  symmetric spectral theorem with its assumptions.
- [ ] Develop SVD with correct dimensions, singular values/vectors, relationship
  to `A^T A`, and full/reduced/truncated forms.
- [ ] Explain dimensionality reduction and the recommendation example, identifying
  the difference between complete-matrix SVD and prediction with missing ratings.
- [ ] Integrate diagrams, checkpoints, pitfalls, chapter synthesis, graded practice,
  hints, and independently checked solutions.
- [ ] Meet the chapter definition of done, including repeated/zero eigenvalue and
  rectangular/rank-deficient cases where relevant.

Progress: Primary deck has 44 pages. Do not label statistics/PCA as taught in this
deck without source evidence; the bridge is tracked separately in §9.

## 9. Close coverage gaps and integrate midterm review

- [ ] Implement the statistics/PCA destination identified in §2: define data
  orientation, centering, mean, variance, standard deviation, covariance, and the
  connection between PCA and SVD; state normalization conventions.
- [ ] Add checked examples and exercises for that bridge and label material added
  beyond the lecture decks.
- [ ] Create a topic-to-section review guide covering every midterm topic.
- [ ] Integrate representative homework, recitation, and exam problem styles with
  source references and independently verified reasoning.
- [ ] Provide cumulative conceptual/computational practice with explained answers
  and clear links back to prerequisites and worked examples.
- [ ] Audit the coverage map: no exam topic or required learning objective is left
  without a teaching destination and appropriate practice.

Progress: The gap is documented, not resolved. Initial practice-exam extraction
reveals conceptual true/false reasoning as well as computational tasks; review
should prepare students for both.

- [ ] Build a skill-by-skill exam blueprint linking instruction, examples, independent
  practice, and readiness checks; distinguish past-exam evidence from predictions.
- [ ] Add explicit method-selection guidance and practice that moves from worked to
  partially scaffolded to independent, unfamiliar mixed problems.
- [ ] Add a timed mock exam with checked solutions, a transparent practice scoring
  guide, diagnostic revision links, and fresh retry questions; document timing/aid
  assumptions and distinguish editorial mastery targets from official grade cutoffs.

Progress update, 2026-10-26: The owner specified a paid professional educator's
commission: prepare the client to earn an A. The bible and rubric now require
observable exam skills and diagnostic practice. These materials and student
readiness are not yet verified.

## 10. Verify the whole textbook

- [ ] Check every mathematical statement's conditions and independently verify
  worked examples and solution keys; log and resolve source discrepancies.
- [ ] Audit notation, chapter dependencies, theorem/figure/example references,
  learning objectives, and source coverage across all weeks.
- [ ] Complete a clean build, review warnings, and check links and included assets.
- [ ] Inspect representative pages and every distinct teaching component on desktop
  and narrow viewports, including long equations and tables.
- [ ] Check contrast, labels beyond color, alt text, keyboard access, dark-theme
  figures, and browser print with essential solutions visible.
- [ ] Walk through a complete learning path and cumulative practice set as a reader;
  resolve blocking confusion and request owner review of the concrete result.
- [ ] Replace the rubric's latest assessment with evidence from the completed work.

Progress: No whole-book validation has run. The current assessment describes the
source/template baseline and explicitly identifies unverified outcomes.

## 11. Prepare delivery and final polish

- [ ] Replace the template README with actual setup/build instructions and a reader
  guide; align title, author credit, favicon, metadata, and navigation.
- [ ] Complete source/figure credits and confirm applicable permissions/attribution
  before public distribution; retain existing license notices appropriately.
- [ ] Remove remaining reader-facing filler, obsolete tutorial navigation, broken
  references, and accidental placeholder URLs.
- [ ] Record the reproducible dependency environment, known limitations, and release
  verification evidence without committing generated build artifacts.
- [ ] When publication is authorized, use the existing deployment workflow and
  verify the resulting site, navigation, math, figures, and assets.
- [ ] Update the bible's canon, checklist, and rubric to reflect the delivered state.

Progress: Deployment configuration exists, but a successful run and live site are
unverified. This checklist does not request a commit, push, or publication.

## Future priorities

Deferred until the initial textbook is complete: a dedicated typeset PDF edition,
interactive mathematical explorations, verified executable demonstrations, and
later course weeks. Promote these to concrete tasks only when their scope becomes
active; they are not requirements for the five-week milestone.

## Blockers and decisions

- **Planning blockers:** None. All three requested files exist and have been adapted.
- **Verification dependencies:** Isolated build environment; visual reading of two
  non-extractable PDFs; full source and mathematical review.
- **Open choices:** Final title/credit; visual refinements after the first rendered
  chapter; statistics/PCA placement and attribution details.
- **Decision, 2026-10-26:** Keep the existing stack, expand the slides into a genuine
  textbook, establish the pattern with Week 1, and proceed in weekly order.
- **Scope of this pass:** Documentation only, completed as bible → rubric → checklist.
