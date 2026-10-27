# Math4MLBook TODO

Last updated: 2026-10-26. The owner selected **shadows and matched point measurements**
as the primary analogy, replacing knitting/crochet. Lecture 1 retains its four-page
route, 12 numbered learning sections, all lecture examples/formulas, and 24 explained
exercises. Active prose, diagrams, and problem feedback use the shadow canon; earlier
craft material remains historical/reference work. This revision is local.

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

1. Review the completed Lecture 1 reading experience and gather reader feedback (§4).
2. Complete the remaining source/notation map, including visual-only supporting
   PDFs and statistics/PCA (§2).
3. Review the complete Lecture 2 and its cheat sheet (§5), then proceed through
   Weeks 3–5 and close midterm coverage (§§6–9).

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

- [x] Create [Knitting Crochet](analogy/systems/knitting-crochet/canon.md) as the separate source of truth for the
  actual stitch actions, cast-on/bind-off, magic-ring rounds, swatches/gauge,
  connected graph, precise mappings, and limitations.
- [x] Create [Knitting Crochet Rubric](analogy/systems/knitting-crochet/rubric.md) with weighted criteria and an
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

- [x] Create [the bacteria/virus canon](analogy/systems/bacteria-viruses/canon.md) and
  [its rubric](analogy/systems/bacteria-viruses/rubric.md), grounded in actual division,
  infection, lysis, compartment counts, and measurement limitations.
- [x] Create [the astrological-wheel canon](analogy/systems/astrology/canon.md) and
  [its rubric](analogy/systems/astrology/rubric.md), grounded in degree placements,
  aspects, declared house conventions, rotations, and chart records.
- [x] Create [the original pottery canon](analogy/old/ANALOGY_POTTERY.md) and
  [its rubric](analogy/old/ANALOGY_POTTERY_RUBRIC.md), grounded in clay preparation, wheel
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

## Lecture-linked analogy index and ranked options

- [x] Rename the generic analogy filenames to `ANALOGY_KNITTING_CROCHET.md` and
  `ANALOGY_KNITTING_CROCHET_RUBRIC.md` inside `analogy/`; fix moved-file links.
- [x] Align the knitting reference with the other canons: domain/source boundary,
  fixed objects, action cards, numerical anchors, course register, graph, and status;
  add a weekly route and formal transfer anchors.
- [x] Rank five original candidate frameworks with course-specific strengths,
  boundaries, recognizable scenes, and linked domain foundations.
- [x] Map 36 topic IDs to exact one-based lecture PDF pages or the exam-topic list;
  supply a destination in every current lens and every candidate framework.
- [x] Add cross-lens translation cards and shared graph; connect each canon/rubric
  to the shared register; verify local links, topic coverage, and graph connectivity.
- [ ] Visually review W3 pp. 16–17 and W5 p. 22; complete supporting-problem mapping
  and independent review of topic-level mechanisms and source precision.
- [ ] Convert selected mappings into chapter passages, illustrations, and a full
  fresh transfer bank. Light and shadows are now selected for full drafts; the other
  three ranked options remain proposals.

Progress, 2026-10-26: Reviewed extractable page content from all five lecture decks.
The shared index links all current systems through mathematics and source pages;
it does not imply physical equivalence. Knitting/crochet remains primary. New
lecture-page mapping supersedes older notes that it was wholly absent; supporting
problem references, source images, manuscript integration, and learner evidence
remain incomplete. Earlier specialized rubric scores are preserved as dated
baselines, with a source-map addendum rather than an unsupported score increase.

## Colored light versus multiple shadows — replacing pottery

- [x] Develop [the light canon](analogy/systems/colored-light/canon.md) with actual
  emission/sensing/filtering mechanisms, checked anchors, complete lecture route,
  graph, formal transfer anchors, and explicit toy-sensor/perception boundaries.
- [x] Develop [the shadow canon](analogy/systems/shadows/canon.md) with matched points,
  calibrated views, hidden depth, checked reconstruction/fitting/SVD examples,
  complete lecture route, graph, and formal transfer anchors.
- [x] Create separate, equally weighted [light](analogy/systems/colored-light/rubric.md)
  and [shadow](analogy/systems/shadows/rubric.md) rubrics with domain-specific rejection tests.
- [x] Write [the head-to-head case](analogy/comparisons/light-vs-shadows.md), including
  opening hooks, strongest objections, lecture comparison, and a fair transfer trial.
- [x] Replace pottery with both contenders in the active source map and bible;
  retain the old pottery documents in `analogy/old/` with historical status.
- [x] Verify the new exact numerical anchors, all 36 active topic destinations,
  graph connectivity, rubric arithmetic, and local file links.
- [ ] Develop matched illustrated teaching samples and fresh equivalent transfer
  questions; obtain independent domain/math review and record learner evidence.
- [ ] Select the preferred lens after reviewing the concrete comparison; no change
  to the existing primary knitting/crochet thread is inferred yet.

Progress, 2026-10-26: Both competing frameworks are drafted, source-linked, and
calculation-checked. Light makes nonunique observation memorable; shadows has a
particularly direct geometric route through the four spaces and projection. These
are editorial judgments. No calibrated optics demonstration, rendered figure,
complete chapter, independent review, or comparative learner trial has run.

## Common-method rebuild of the four earlier analogy systems

- [x] Write [Build Method](analogy/build-method.md) first,
  documenting the actual light/shadow workflow, checks, gaps, and shared contract.
- [x] Move the eight original canon/rubric files unchanged into
  [analogy/old/](analogy/old/README.md); record source paths and SHA-256 hashes.
- [x] Rebuild knitting/crochet, biology, astrology, and pottery with concrete scenes,
  stable vocabulary, unique/nonunique cases, four spaces, fitting/Gram–Schmidt,
  eigen/SVD distinctions/shapes/truncation, and checked statistics/PCA anchors.
- [x] Embed all 36 exact lecture/topic destinations and six chapter routes in each
  rebuilt canon; provide six answered formal transfer anchors with diagnostic feedback.
- [x] Add connected graphs, accessible prose, diagram briefs, objections/responses,
  source/model boundaries and cross-lens translation links to each reference.
- [x] Rebuild the four separate rubrics with identical weights, domain-specific
  rejection tests, evidence ledgers, and no unearned inherited scores.
- [x] Restore pottery as a current rebuilt reference; update the six-lens source
  map and current links while preserving earlier selection/history statements.
- [x] Verify exact arithmetic, original hashes, 36-topic/six-route coverage,
  current links, graph reachability and rubric weights; record the remaining gaps.
- [ ] Complete independent domain/math review, exact supporting problem references,
  image-only lecture review, full chapter passages and a fresh exercise bank.
- [ ] Render and inspect the proposed figures; collect matched reader-transfer
  evidence before assigning comparative effectiveness or exam-readiness claims.

Progress, 2026-10-26: Four canon/rubric pairs rebuilt using the newly documented
method. The original bytes are preserved in old/. Each rebuilt system now covers
all five lecture weeks plus the exam statistics/PCA supplement, with the same
required artifact set. Mathematical checks are author verification, not outside
review; no physical experiment, rendered figure, completed chapter or learner
trial is claimed. Older notes about pottery retirement and absent topic mapping
are historical; the current six-lens source map and this section govern current state.

## Analogy folder organization and consistency

- [x] Group all six current canon/rubric pairs under `analogy/systems/<theme>/`;
  use concise filenames and update current project links.
- [x] Keep the index, build method, and authoritative source map at the folder root;
  group comparison documents under `comparisons/` and checks/history under `verification/`.
- [x] Centralize all exact PDF-page mappings in `analogy/course-map.md`; retain
  local mechanism indexes with direct topic-anchor links instead of copied page tables.
- [x] Move prior selections, rebuild commentary and numerical rubric scores into
  `verification/history.md`; retain all mathematical examples and current limitations.
- [x] Standardize all six rubrics: editorial draft, author checks recorded,
  independent review pending, weighted total unassigned; keep evidence differences explicit.
- [x] Preserve every file in `analogy/old/` unchanged, including README and manifest.
- [x] Check current local links/fragments, topic coverage, graphs, rubric weights,
  unchanged numerical code blocks and preserved historical hashes; document results
  in `analogy/verification/layout.md`.

Progress, 2026-10-26: The root now contains only the index, build method, and course
map. Six system folders, comparison and verification folders separate current
teaching references from decision history. All six rubric statuses agree; historical
scores remain recorded. Old snapshot links retain their original relative paths
because the entire old folder is immutable; use the current index for navigation.
This cleanup changes organization/documentation, not mathematical models or the
remaining chapter, illustration, review, and learner-validation tasks.

## Three-role textbook teaching strategy

- [x] Write [teaching-strategy.md](analogy/teaching-strategy.md): distinct roles,
  six chapter routes, all 36 topic allocations, a worked cross-lens transition,
  formal transfer/feedback, visual rules, implementation order, and acceptance criteria.
- [x] Link the guide from the analogy index and show bible; verify local links,
  topic anchors and the fresh formal transfer example.
- [x] Implement the strategy through a complete Week 1 chapter, inspect its rendered
  output, and test fresh formal problems before repeating the pattern.

Historical progress, 2026-10-26: Initially proposed shadows as the mathematical
backbone. The craft-centered strategy below now supersedes that proposal; light
and shadows are optional support.
The guide develops the recommendation without requiring three explanations per
concept. This is a written implementation plan; no chapter, figure, independent
review, or learner-effectiveness result is completed by this documentation pass.

## Strengthen knitting/crochet as the mathematical backbone

- [x] Rewrite the teaching strategy so craft examples lead every chapter and all
  36 topic groups; shadows/light are optional supporting views.
- [x] Add a four-row, 24-stitch color panel with four marked six-stitch sections;
  derive record geometry, uniform-repeat projection and Gram–Schmidt from it.
- [x] Derive the panel's baseline/alternating SVD, null directions, full/compact
  shapes and truncation loss; center the same record for a distinct PCA lesson.
- [x] Add a six-sector crochet relabeling operator with checked uniform/alternating
  eigen-directions, and explicit real-basis/physical limits.
- [x] Generate a labeled stitch-count schematic; verify its two panels each contain
  96 cells, 32 pink and 64 green. Visual/technique review remains separate.
- [x] Update the canon's 36 mechanisms, six transfer anchors, graph, rubric and
  source-map summaries; verify the new calculations and current links.
- [ ] Work or obtain qualified craft review of the panel and marked-round
  constructions; inspect the SVG and develop loop-accurate technique diagrams.
- [ ] Build and review the actual Week 1 chapter, then carry the same projects
  through subsequent weeks with a fresh formal exercise bank and learner checks.

Progress, 2026-10-26: The earlier shadow-led proposal is superseded. Yarn now carries
the mathematics as well as the book's identity. The same swatch supports bases,
projection, SVD and PCA; the crochet motif supports a specific permutation/eigenvector
example. These are checked mathematical constructions and a generated schematic,
not physical pattern execution or measured learning outcomes. Lecture 1 now implements
the count-record backbone; its review is recorded below.

## 3. Establish the book and visual foundation

- [x] Create an isolated Python environment, install the repository requirements,
  verify the CLI, and record a reproducible local build command.
- [x] Build the existing scaffold and record a warning/error baseline before
  substantial changes; identify dependency or configuration issues.
- [x] Replace template identity, repository links, base URL, and opening page with
  the textbook's working identity and an accurate reader guide.
- [x] Replace reader navigation with the available textbook chapters; remove template
  tutorials from reader navigation while retaining useful authoring references.
- [x] Implement shared typography, spacing, palette, light/dark tokens, and named
  teaching components from the bible; verify stylesheet loading.
- [x] Establish mathematical figure conventions: axes, labels, line styles,
  captions, alt text, and reproducible vector/plot sources.
- [x] Provide useful search, chapter/section navigation, visible keyboard focus,
  controlled equation overflow, and printable solutions.

Progress: Python 3.12 environment installed; the original template built with one
warning. Lecture 1 now has a clean strict build, textbook identity/navigation,
shared light/dark styles, reproducible SVGs, keyboard-accessible checkpoint answers,
local math/diagram overflow, and printable explanations. Build versions and browser
results are in [the review record](authoring/lecture1-review.md). Template authoring
sources are retained outside reader navigation; unpublished weeks are not empty stubs.

## 4. Week 1 — Vectors and matrices

- [x] Draft a chapter opener, prerequisites, objectives, and a section sequence
  mapped to `WK1_ Vectors and Matrices.pdf`.
- [x] Develop vector representation, addition/scaling, linear combinations, dot
  product and angles, norm, and normalization into connected prose.
- [x] Develop matrix dimensions, diagonal/identity/symmetric/skew-symmetric matrices, addition,
  scaling, transpose, trace, matrix-vector and matrix-matrix products/properties.
- [x] Add complete checked examples for the major methods, including dimension
  checks, zero-vector limitations, and noncommutativity where relevant.
- [x] Create labeled figures connecting vector geometry and matrix operations to
  their equations; include useful, prerequisite-appropriate ML interpretation.
- [x] Add conceptual checkpoints, common pitfalls, summary, graduated practice,
  hints, and independently checked solutions aligned to objectives.
- [x] Verify source coverage, mathematics, references, and build output; inspect
  desktop, narrow viewport, dark theme, keyboard use, and browser print.
- [x] Refine the shared chapter pattern from the rendered result and update the
  bible/rubric/checklist to match verified implementation.

Progress: The complete first-deck scope is developed in [Lecture 1](book/lecture1/index.md),
with page-level attribution, four SVG diagrams, five checkpoints, 24 explained problems,
and six optional synthesis hints. 67 numerical/structural checks and a strict build
pass; 11 pages were checked at desktop/mobile widths, plus representative dark/print
views and keyboard access. See [review evidence](authoring/lecture1-review.md).
Independent reviewer and learner-performance evidence remain open, as do later weeks.

## 5. Week 2 — Systems, determinants, and inverses

- [x] Develop systems, column interpretation, augmented matrices, elementary row
  operations, elimination, echelon forms, pivots, and back substitution.
- [x] Explain unique/inconsistent/infinitely many solution cases with appropriate
  examples, distinguishing a needed row swap from actual singularity.
- [x] Develop determinants, expansion/properties, area/volume interpretation,
  invertibility, Gauss–Jordan, and cofactor inverse formulas with assumptions.
- [ ] Integrate mapped homework/recitation examples, figures, checkpoints,
  misconceptions, summary, graded practice, hints, and checked solutions.
- [x] Meet the chapter definition of done, including independent computations,
  source mapping, a successful build, and rendered inspection.

Progress (2026-10-27): All 36 lecture PDF pages are now mapped to Parts A–N in
lecture order, including determinants and inverses. Four reader pages contain
17 highlighted stepwise examples, 14 checkpoints, a dedicated TL;DR cheat sheet,
and 26 exercises with hints/expandable solutions. Source mapping, arithmetic,
strict build and rendered checks are recorded in
[coverage](authoring/lecture2-coverage.md) and [verification](authoring/lecture2-review.md).
Supporting homework/recitation problem alignment remains open; the combined
integration item above is not marked complete solely from slide coverage.

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

- [x] Replace the template README with actual setup/build instructions and a reader
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

## Lecture 1 concise edition

- [x] Condense the reader route to vectors/geometry and matrices/multiplication.
- [x] Highlight essential formulas in yellow and exam mistakes in red.
- [x] Retain a short, precise knitting/crochet connection on each page.
- [x] Preserve the expanded sources outside the concise reader navigation.
- [x] Update the welcome page and browser-check script for the new route.
- [x] Verify clean build, desktop/mobile math, and two A4 print pages; save
  [the combined PDF](authoring/lecture1-study-guide.pdf). Publication remains pending.

## Lecture 1 complete lecture coverage in the concise edition

- [x] Restore every requested vector/matrix topic and every distinct lecture example.
- [x] Restore both distributive laws, row/column product identities, and dot-product properties.
- [x] Retain the orthogonality/cosine derivation and the source normalization example.
- [x] Check original vector coordinates against slide images; record exact source destinations
  in [the coverage audit](authoring/lecture1-coverage.md).
- [x] Recompute restored source arithmetic: 77 checks now pass.
- [x] Verify complete-coverage reader pages on desktop/mobile and regenerate the
  PDF: four A4 sheets, two per reading page; retain legible math instead of dropping
  lecture content. Strict build passes; publication remains pending.

## Restore the textbook experience with fewer navigation pages

- [x] Consolidate full teaching explanations into vectors/geometry and matrices/products.
- [x] Restore all four diagrams, worked examples, derivations, and checkpoint answers.
- [x] Reconnect the 24 exercises and explained solutions as the other two pages.
- [x] Move synthesis and source attribution into the teaching pages.
- [x] Rewrite concept links to anchors in the included pages; remove compressed styling.
- [x] Preserve all source examples/formulas and the four-page cap including exercises/solutions.
- [x] Update the reader guide and authoring references to describe website navigation,
  with no printed-page target. Publication remains pending.

## Restore the show bible's section and learning structure

- [x] Organize the teaching pages into sections 1.1–1.12 with visible numbered headings.
- [x] Add prerequisites, measurable page objectives, four-page route cards, and local roadmaps.
- [x] Give every section a learning goal, motivating question, and source-page reference.
- [x] Number definitions, theorem/key results, and 12 worked examples; expose reasoning
  and independent checks rather than only final results.
- [x] Provide 12 checkpoints with collapsible explanations and 12 section recaps linked
  to practice; keep all lecture examples/formulas and all four diagrams.
- [x] Add a chapter synthesis, unaided readiness checklist, and skill-to-exercise map.
- [x] Add specific concept/retry links to every explained solution.
- [x] Implement the hierarchy and role-specific formatting without adding website pages.
- [x] Verify the finished structure: strict build, 82 numerical/structural checks,
  683 local links/assets, and 10 desktop/mobile page checks pass. Section jumps,
  four-page navigation, keyboard checkpoints, and print answers work.

## Switch the textbook backbone to shadows

- [x] Record the owner's selection in the show bible, main rubric, analogy index,
  and current teaching strategy; preserve the prior craft strategy as history.
- [x] Rewrite the four active lecture pages and the welcome/branding around points,
  calibrated front/side views, and explicitly defined coordinate records.
- [x] Replace all four active diagrams; preserve the sectioning, palette, source
  examples/formulas, checkpoints, and exercise/solution route.
- [x] Correct domain-dependent explanations: negative/fractional coordinates are valid;
  one-point world coordinates and multi-point profiles have different meanings.
- [x] Use canonical O (2-by-3) and H (4-by-3), including the repeated Y reading;
  update Problem 15 and its answer, and remove the former count restrictions.
- [x] Extend the shadow canon with the actual Week 1 profile records and chapter links.
- [x] Check active reading pages contain no residual craft narrative; strict build
  and 93 arithmetic/structure/narrative checks pass. Publication remains pending.

## Lecture 2 flow refinement

- [x] Carry the main slide system through matrix notation, row operations, REF,
  back substitution and RREF with explicit transitions.
- [x] Reduce repetition and move supplementary slide examples to labeled dropdowns.
- [x] Introduce the shadow solution cases after teaching the method; retain all
  requested topics, eight checkpoints, 18 practice problems and the four-page route.

## Lecture 2 full-deck and cheat-sheet refinement

- [x] Cover every Week 2 slide topic/example; label Parts A–N in source order.
- [x] Highlight the operation and explain how/why at each worked-example step.
- [x] Add all determinant rules, Laplace expansion, geometry, invertibility tests,
  Gauss–Jordan inverse construction and full 2×2/3×3 cofactor methods.
- [x] Add a dedicated TL;DR page with formulas, conditions, method selection and
  a complete example; combine practice/answers to preserve four reader pages.
- [x] Extend the practice bank to 26 questions and verify all inverse/determinant examples.

## Numbered topic navigation and agent instructions

- [x] Add root `AGENTS.md` with source, teaching, navigation, verification and handoff rules.
- [x] Put the current authoring contract near the start of the show bible; distinguish history.
- [x] Group actual sidebar links by lecture and label each Page 1–4 with its topic.
- [x] Split Lecture 1 into vectors, geometry, matrices and TL;DR; Lecture 2 into systems, determinants, inverses and TL;DR.
- [x] Include practice and expandable answers immediately below each question on its topic page; preserve all IDs.
- [x] Keep all source examples and conditions; update welcome/routes and source coverage records.
