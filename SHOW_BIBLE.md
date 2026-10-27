# Math4MLBook — Project Show Bible

A living reference for the textbook's identity, editorial rules, and visual direction.
Observed implementation and intended experience are recorded separately.

## 0. At a glance

| Field | Answer |
| --- | --- |
| Project | [Math4MLBook](https://github.com/archipelagoing/Math4MLBook) |
| Working title | Mathematical Foundations of Machine Learning |
| Premise | A beautiful, rigorous, readable textbook that develops the course's weekly slides into a complete learning experience. |
| Current stage | Lecture 1: four website pages, with 12 numbered learning sections, objectives, worked steps, checkpoints, and synthesis. |
| Canonical branch | `main`; current teaching-structure revision based on `9d932e0`. This local revision is not deployed. |
| Decision maker | Repository owner; final title and aesthetic preferences remain adjustable. |
| Last verified | 2026-10-26: local strict build and Lecture 1 desktop/mobile/dark/print checks; live deployment unverified. |
| Start here | This file → [rubricatm.md](rubricatm.md) → [todoSimple.md](todoSimple.md); implementation in `book/`, course sources in `resources/`. |

## 1. The premise

**Reader and problem.** A student studying mathematical foundations of machine learning needs a coherent explanation between lectures, practice, and exams. Slides provide a strong teaching sequence but often rely on spoken explanation, animated reveals, and omitted intermediate steps. The textbook supplies those connections.

**Outcome.** Prepare the student to earn an A on the exam: understand the material deeply, recognize what an unfamiliar question is asking, choose and justify a method, carry out the mathematics accurately, and present a clear solution under exam conditions.

**Professional commission.** Write as a paid professional educator on a stipend, accountable to a client whose goal is an A. Take responsibility for the usefulness of every explanation, example, diagram, and exercise. Anticipate where this particular student will get stuck, expose hidden prerequisites, explain the steps a lecturer might omit, and provide a practical route from first understanding to independent exam performance. Judge a section by what the student can do after studying it. An attractive page or a correct summary alone does not meet the commission.

**A-level preparation standard.**

- Build an exam blueprint from the supplied topic list, lectures, homework, and practice exams. Map each assessed skill to instruction, a worked example, independent practice, and a readiness check. Distinguish observed past-exam patterns from predictions about the upcoming exam.
- Teach method selection: the cues in a question, why the chosen method applies, its assumptions, plausible alternatives, and how to recognize when it fails.
- Model clear written reasoning, intermediate steps, and quick checks. Explain common ways to lose credit without inventing an instructor's marking scheme.
- Progress from a fully worked example to partially scaffolded practice, then independent variants with changed numbers, representations, and conditions. Include counterexamples, conceptual justifications, and mixed problems that do not announce the method.
- Use cumulative retrieval and timed practice after concepts are learned. Include feedback that diagnoses the cause of an error and directs the student to a specific explanation and retry problem.
- End chapters with a concrete “Can you do this unaided?” checklist. Provide a final mixed mock exam, explained solutions, a transparent practice scoring guide, and a targeted revision path. Match exam timing and permitted aids only where the supplied instructions establish them; identify assumptions otherwise.
- Treat readiness as demonstrated performance on fresh representative problems, not familiarity with solutions. Record the official A cutoff if supplied; until then, label any practice mastery threshold as an editorial target rather than the course grading policy. An A is the preparation objective; an actual grade is evidence only when reported.

**Experience in three beats.**

1. Enter a weekly chapter through an inviting opening, prerequisites, and concrete learning objectives.
2. Move through intuition, precise statements, diagrams, derivations, and fully worked examples.
3. Check understanding, practice independently, consult explained solutions, and connect to the next week.

**Promise.** The book respects the slides' substance and teaching order while giving the reader enough explanation to study without attending the lecture. Color and illustration clarify mathematics; every important conclusion has a reason.

**Initial scope.** Weeks 1–5 and their supporting homework, recitations, worksheets, and midterm materials. Statistics and PCA appear in the midterm topic list and must be accounted for explicitly. Later course units, accounts, grading systems, and a custom application platform are outside the first milestone.

## 2. Canon: what exists today

| Area | Observed state | Evidence | Caveat |
| --- | --- | --- | --- |
| Book | Lecture 1: two structured teaching pages, 24 exercises, and explained solutions; four website pages total. | `book/lecture1/`, `book/_toc.yml` | Weeks 2–5 and cumulative exam preparation remain unfinished. |
| Lectures | Five PDF decks, 191 PDF pages in total. | `resources/lectures/` | Counts include title pages and progressive reveals; these are not 191 distinct lessons. |
| Supporting materials | Six homework/worksheet/recitation PDFs; seven exam PDFs and a topic list. | `resources/HW/`, `resources/practiceExams/` | Inventory and text extraction completed; full mathematical and visual review remains. |
| Build stack | Python 3.12, pinned TeachBooks/Jupyter Book v1 and sphinx-design; clean strict local build. | `requirements.txt`, `authoring/lecture1-review.md` | MathJax uses a CDN; deployment is unverified. |
| Visual implementation | Shared craft palette, light/dark styles, four original SVGs, printable checkpoint answers. | `book/_static/textbook.css`, `book/figures/lecture1/` | Representative browser checks, not a full accessibility audit. |
| Automation | Reusable TeachBooks deployment workflow triggered by book/config changes and manual dispatch. | `.github/workflows/call-deploy-book.yml` | Successful runs and GitHub Pages availability unverified. |
| Project identity | Working title, point/view mark, repository links, reader guide, setup README, chapter navigation. | `README.md`, `book/_config.yml`, `book/_toc.yml` | Final human author credit and publication URL remain to be settled. |

**Known source limitations.** `Recitation1_Solutions.pdf` and `PT1_f22Sol.pdf` yielded no non-whitespace text with `pdftotext -layout`; inspect their pages visually or with OCR before relying on their contents. Extractable PDFs can still contain diagrams and handwritten annotations that text extraction misses. The Week 5 extracted text covers eigendecomposition and SVD but does not mention statistics or PCA; check the visual source and supporting materials before choosing where to add a clearly identified supplement.

## 3. The world and its rules

**Primary analogy: shadows and matched point measurements.** The owner selected
[The Object Behind the Shadows](analogy/systems/shadows/canon.md), replacing the
knitting/crochet backbone. Its [rubric](analogy/systems/shadows/rubric.md) owns the
domain/math acceptance tests; [the teaching strategy](analogy/teaching-strategy.md)
owns the classroom route. Use ideal parallel-ray views of matched labeled points,
fixed calibrated axes, and a declared origin. World coordinates, screen readings,
and multi-point measurement profiles are different records with explicit dimensions.
A front view keeps X,Y and hides Z; an independent side view adds Y,Z.

One four-bead X profile supplies the connected vector/data examples; O and stacked
H supply the view maps. Coordinate arithmetic, geometry, composition, reconstruction,
spaces, projection, SVD and PCA develop from those declared records. Preserve every
lecture example and formal transfer problem. The analogy must not promise arbitrary
solid reconstruction from silhouettes or identify record-space angles with physical
frame rotations. Negative and fractional coordinates are valid; the former physical
stitch-count restrictions do not apply.

The [knitting/crochet system](analogy/systems/knitting-crochet/canon.md) and
[earlier craft strategy](analogy/verification/knitting-teaching-strategy.md) remain
reference/history. Their earlier primary-backbone decisions are superseded.

**Shared lecture source and translation index.**
[Course Map](analogy/course-map.md) connects 36 topic IDs to
specific lecture PDF pages and each current analogy, preserving the original five-option comparison.
Its translation cards explain the exact shared mathematics. Every chapter analogy
must identify a topic ID, local mechanism, mathematical landing, boundary, and
source. [Top Five](analogy/comparisons/top-five-options.md) ranks sound, colored light,
multiple shadows, a hanging mobile, and dance capture. The owner has selected
colored light and multiple shadows for full competing drafts in place of pottery,
then requested the current common-method rebuild of all four earlier lenses.
Their [head-to-head comparison](analogy/comparisons/light-vs-shadows.md) makes the case
for each; the owner has now selected shadows as the primary thread.

**Shared authoring method and originals.**
[Build Method](analogy/build-method.md) documents the light/shadow
workflow and the rebuild contract. The original four canon/rubric pairs are
preserved unchanged in [analogy/old/](analogy/old/README.md), with SHA-256 hashes.
Knitting/crochet, biology, astrology, and pottery have been rebuilt with six chapter
routes, 36-topic mechanism indexes linked to the source register, checked anchors, six answered
transfer anchors, graph/diagram briefs, and separate evidence-based rubrics.
These are equally structured editorial references; completed chapters, independent
review, and student evidence remain separate unfinished work.

**Analogy references.** Keep each lens’s objects, graphs, mathematical boundaries,
and rubric distinct. Shadows is the selected primary lens; others remain references:

| Lens | Source of truth | Separate rubric |
| --- | --- | --- |
| Bacteria versus viruses | [Cells, Infection, and Measurement](analogy/systems/bacteria-viruses/canon.md) | [Biology rubric](analogy/systems/bacteria-viruses/rubric.md) |
| Astrological wheel | [Around the Zodiac](analogy/systems/astrology/canon.md) | [Wheel rubric](analogy/systems/astrology/rubric.md) |
| Colored light | [Different Light, the Same Color](analogy/systems/colored-light/canon.md) | [Light rubric](analogy/systems/colored-light/rubric.md) |
| Multiple shadows | [The Object Behind the Shadows](analogy/systems/shadows/canon.md) | [Shadow rubric](analogy/systems/shadows/rubric.md) |
| Pottery, rebuilt | [From Spinning Clay to Fired Form](analogy/systems/pottery/canon.md) | [Pottery rubric](analogy/systems/pottery/rubric.md) |

Each lens covers the same mathematical course scope through its own connected
mechanisms. Shadows is now the primary textbook thread; these are additional lenses, not an instruction to repeat
all lens explanations for every concept. Use a deliberate lens for a passage and name
any switch. Shared mathematics can connect lenses; their physical/symbolic entities
must not silently merge. The six reference frameworks remain drafts; shadows now has Lecture 1
integration. Later chapters and learner validation remain pending.

| Term | Meaning here |
| --- | --- |
| Week / chapter | A course unit anchored in one weekly slide deck, split into readable sections as needed. |
| Source map | A record connecting textbook sections to PDF filenames, one-based PDF page ranges, and supporting problem numbers. |
| Worked example | A complete problem with reasoning, intermediate steps, result, and a check or interpretation. |
| Checkpoint | A short question following a concept, with accessible answer and explanation. |
| Supplement | An explicitly identified bridge or extension added where the supplied materials need more context. |
| Complete chapter | A chapter meeting the editorial, mathematical, practice, accessibility, and rendered-output criteria below. |

**Invariants.**

1. Preserve the slides' conceptual progression; consolidate repeated reveal slides into one coherent explanation.
2. Trace every core topic to supplied material. Mark added explanations and distinguish source corrections from transcription.
3. State dimensions, domains, hypotheses, and exceptional cases when introducing a formula or theorem.
4. Define notation before use and keep it consistent across weeks. Record any necessary change from source notation.
5. Verify solutions independently; a document named “Solutions” is supporting evidence, not a correctness guarantee.
6. Connect symbolic work to geometry or interpretation whenever it improves understanding.
7. Keep exercise statements usable without exposing the answer; make solutions reachable and meaningful in print.
8. Never use color alone to distinguish vectors, cases, answers, or warnings. Labels and structure must carry meaning.
9. Preserve the original PDFs. Keep planning documents outside reader navigation.
10. Describe unbuilt features as planned and untested behavior as unverified.

**Editorial voice.** Clear, patient, mathematically precise, and adult. Write connected prose with purposeful headings. Explain why a method is used before presenting its steps. Avoid unexplained leaps, decorative jargon, slide fragments, and motivational filler. Proofs should expose the idea and the assumptions; computational recipes should explain when they apply.

**Notation conventions (planned).** Work over the real numbers unless a section explicitly introduces another field. Use bold lowercase vectors, uppercase matrices, indexed entries, column-vector convention, transpose `A^T`, Euclidean norm, and `m × n` dimension declarations. Define span, column space, null space, rank, and coordinate vectors consistently. Reserve `Q` for orthonormal columns where appropriate; distinguish a full SVD from a reduced or truncated SVD. Publish a notation reference before chapters proliferate.

| Principle | Practical consequence |
| --- | --- |
| Explain, then formalize | Begin with a motivating question, develop intuition, then give the exact statement and derivation. |
| Preserve the good teaching | Retain useful examples and the slides' progression; add the missing connective tissue. |
| Show the mathematics | Use labeled figures, justified transformations, and checked computations. |
| Design for sustained reading | Favor generous spacing, consistent components, and quiet page surfaces with purposeful color. |
| Make practice diagnostic | Include conceptual, computational, and transfer questions with explanations of common mistakes. |

**Constraints.** Retain the existing TeachBooks repository and author in MyST Markdown unless a concrete limitation warrants a documented change. HTML is the primary reading format; browser print should remain legible, while a polished standalone PDF is a later milestone. Track attribution per source and figure; the template's CC BY license and author field do not establish rights for every course PDF. This is an attribution task, not a reason to interrupt local planning or authoring.

## 4. Components and source hierarchy

**Roles.** Students read and practice; the repository owner sets direction; authors expand sources; reviewers check mathematics, teaching, and rendered presentation.

**System map.** Course PDFs and topic list → source mapping and editorial synthesis → MyST chapters, mathematical figures, and exercises in `book/` → TeachBooks/Sphinx build → static HTML, with deployment handled by the existing workflow when authorized.

| Component | Responsibility | Source of truth |
| --- | --- | --- |
| Lectures | Weekly scope, teaching sequence, primary examples | `resources/lectures/` |
| Homework and recitations | Methods, practice, solution styles to verify | `resources/HW/` |
| Midterm materials | Coverage checks and assessment styles | `resources/practiceExams/` |
| Book content | Reader-facing explanation and practice | `book/` |
| Navigation and configuration | Chapter order, identity, extensions, build behavior | `book/_toc.yml`, `book/_config.yml` |
| Styling and illustrations | Shared visual tokens, section hierarchy, teaching components, and mathematical figures | `book/_static/textbook.css`, `book/figures/lecture1/` |
| Governance | Identity → assessment → execution checklist | `SHOW_BIBLE.md`, `rubricatm.md`, `todoSimple.md` |

**Source priority.** Use lectures for scope and exposition, supporting problems for depth, and the topic list to detect gaps. Mathematical correctness takes precedence when sources conflict. Cite the discrepancy and explain the correction. Sources use varying course labels; do not infer that one identifier is authoritative without owner confirmation.

## 5. Visual and interaction language

**Direction.** A modern academic textbook with a cute, lively personality: hot pink and bright green, balanced by warm caramel brown, buttery yellow, and blush paper, with deep warm brown text and blue structural accents. Reserve red for attention cues and yellow for important highlights. The reading page should feel carefully typeset, welcoming, and calm, with memorable diagrams and consistent teaching devices. Proposed defaults below can be refined through the first rendered chapter.

| Role | Proposed token | Use |
| --- | --- | --- |
| Blush paper | `#FFF9F5` | Warm pink-cream reading surface |
| Cocoa ink | `#543124` | Main text and headings |
| Bright green | `#8DEB42` | Geometry and worked-example accents |
| Hot pink | `#FF4FA3` | Definition and connection accents |
| Deep pink | `#C91E70` | Pink text, meaningful outlines, and diagram strokes |
| Leaf green | `#357D22` | Green text, meaningful outlines, and diagram strokes |
| Pink wash | `#FFF0F6` | Definition and connection panel backgrounds |
| Green wash | `#EFF9E7` | Geometry and worked-example panel backgrounds |
| Caramel brown | `#A5633D` | Warm secondary accents and figure details |
| Structural blue | `#3975DB` | Navigation accents, section rules, and structural borders |
| Butter yellow | `#FFF0A6` | Important results, key takeaways, and highlighted passages |
| Attention red | `#B83A3A` | Attention labels, caution borders, and common-pitfall cues |
| Pale rose | `#FCE5E5` | Light background for red attention panels |

Keep hot pink and bright green as vivid accents and figure fills. Use deep pink and leaf green for text, meaningful borders, and diagram strokes; use pink/green washes behind panels with cocoa text. The bright accent fills alone must not carry an essential boundary or label. Use warm brown for typography, blue for structural accents such as navigation accents, section rules, and structural borders, and yellow to highlight important material. Reserve red for attention and pitfalls; pair red labels or borders with pale rose surfaces. Important results should receive yellow highlighting, including inside another teaching component when appropriate.

**Verified light-palette contrast (2026-10-26).** Calculated from the hex values using sRGB relative luminance: deep pink on blush paper is 5.15:1; leaf green on blush paper is 4.90:1; cocoa on pink wash is 10.34:1; cocoa on green wash is 10.52:1. Deep pink on pink wash and leaf green on green wash also exceed 4.5:1. Use these role-specific pairs rather than assuming every palette color contrasts with every other color. Pink and green must not be layered as text/background pairs; distinguish them in diagrams with labels and line styles as well as hue. Keep semantic red/yellow cues labeled and spatially distinct from pink/green teaching accents. Structural blue on blush paper is 4.24:1: use it for structure and sufficiently large headings; use a darker, verified companion for normal-size blue text. Rendered checks remain open: validate normal text at 4.5:1, large text and essential graphical boundaries at 3:1, including hover/focus states. Provide explicit dark-theme pairs rather than assuming automatic image inversion preserves diagram meaning.

**Typography and spacing.** Prefer a readable serif body, restrained sans-serif navigation/headings, and compatible mathematical typography. Start around an 18px desktop body, 1.65 line height, and a 65–75-character reading measure. Use an 8px spacing scale with generous section breaks. Use available fonts or self-hosted assets with fallbacks; no external font service should be required to read the book.

**Teaching components.** Use named, consistently styled blocks for Definition, Theorem, Proof, Worked Example, Check Your Understanding, Common Pitfall, and ML Connection. Keep ordinary exposition outside boxes. Pair each role's color with a visible label; number and cross-reference important results, figures, and examples.

**Figures.** Prefer reproducible SVG or plotting-based mathematical figures with consistent axes, vector labels, line styles, captions, and alt text. Show constructions in readable stages when needed. Avoid screenshots of equations and decorative images that compete with the mathematics.

**Interaction.** Offer weekly navigation, section contents, previous/next links, search, keyboard-visible focus, and collapsible solutions where supported. Core explanations and exercises must remain readable without interactive code. On small screens, keep navigation manageable and contain wide equations locally rather than overflowing the page. Print must expose essential content and preserve figure labels in grayscale.

**Signature moments.** A weekly “What you will understand” opener; a diagram connected directly to its algebra; a closing concept map or synthesis followed by graduated practice. Lecture 1 implements these components; its rendered prototype and checks are recorded in [the review](authoring/lecture1-review.md). Owner aesthetic approval and learner feedback remain open.

## 6. Chapter architecture and weekly content

Each weekly chapter follows this adaptable sequence:

1. Opening question, prerequisites, and measurable learning objectives.
2. Concept sections: intuition → definition/result → explanation or proof → worked example → short checkpoint.
3. Geometric interpretation and an appropriate machine-learning connection, without requiring future material.
4. Common misconceptions and a synthesis linking the chapter's main ideas.
5. Key terms/results and exercises grouped as foundational, standard, and synthesis/challenge.
6. Hints and explained solutions, source notes, and a bridge to the next week.

Apply the A-level preparation standard above to every chapter. Use at least one complete worked example for each major computational method and each substantially different case. Include conceptual checks and transfer problems as well as calculations. Length follows the teaching need; do not pad to a page quota.

| Week | Primary source and PDF pages | Planned chapter coverage |
| --- | --- | --- |
| 1 | `WK1_ Vectors and Matrices.pdf`, 1–48 | Vectors and representation; addition/scaling and linear combinations; dot product, angles, norm, and unit vectors; matrix dimensions and special matrices; addition, scaling, transpose, trace, matrix-vector and matrix-matrix multiplication and properties. |
| 2 | `WK2_SLE_Inverse_Determinants.pdf`, 1–36 | Systems and column interpretation; augmented matrices; elimination, pivots, echelon forms, and back substitution; determinants and geometric meaning; invertibility and Gauss–Jordan; cofactor formulas and limitations. |
| 3 | `WK3_VectorSpaces_SLE_Rank.pdf`, 1–35 | Vector spaces and subspaces; column/null spaces and four fundamental subspaces; complete solutions to `Ax=b`; rank, independence, span, basis, dimension, and change of basis. |
| 4 | `WK4_Orthogonality_and_Projections.pdf`, 1–28 | Orthogonality and the four subspaces; projections onto lines/subspaces; least squares and normal equations; orthonormal bases; Gram–Schmidt, including independence assumptions. |
| 5 | `WK5_Matrix_Decomposition.pdf`, 1–44 | Linear transformations; eigenvalues/eigenvectors; diagonalization and its conditions; spectral theorem; full/reduced/truncated SVD; dimensionality reduction and the recommendation example with its modeling limitations. |
| Coverage bridge | `MidtermTopics.md`; exact supporting pages to map | Mean, variance, standard deviation, covariance, and principal component analysis. Confirm source coverage; add a labeled supplement after the necessary Week 5 prerequisites if no supplied explanation exists. |

These ranges identify whole decks, not a completed section-level source audit. In particular, PCA is a topic-list requirement, not a confirmed Week 5 lecture topic.

### Flow: Learn a weekly chapter

- **Trigger:** Reader selects a week.
- **Path:** Objectives → explanation and examples → checkpoints → synthesis → practice and solutions.
- **Success:** Reader can explain the central ideas and solve a new representative problem.
- **Recovery:** Link prerequisite concepts, provide hints, explain common errors, and expose worked solutions.
- **Implementation/status:** Lectures 1 and 2 (systems portion) implement this route in four website pages each; remaining material is unfinished.

### Flow: Review for the midterm

- **Trigger:** Reader starts from the exam topic list or a missed practice problem.
- **Path:** Topic → relevant chapter/results → related example → practice → explained solution.
- **Success:** Every listed exam topic has a specific learning destination.
- **Recovery:** Flag uncovered topics in the editorial checklist rather than implying they are taught.
- **Implementation/status:** Source files exist; review navigation and coverage map planned.

### Flow: Author and verify a section

- **Trigger:** Next authorized task in `todoSimple.md`.
- **Path:** Read source pages and relevant problems → draft → check mathematics → render → inspect → update source notes and checklist.
- **Success:** Section meets the shared chapter standard and builds with valid references.
- **Recovery:** Keep unreadable source pages and unresolved mathematical discrepancies explicitly open.
- **Implementation/status:** Workflow defined here; chapter implementation not started.

## 7. Continuity ledger

| Date | Decision | Reason and tradeoff | Revisit when |
| --- | --- | --- | --- |
| 2026-10-26 | Complete bible, rubric, then checklist before writing chapters. | User-requested sequence; establish a shared target first. | These documents are complete. |
| 2026-10-26 | Expand the weekly slides into textbook prose. | Preserve their effective teaching while supplying independent-study depth. | A source ordering creates a prerequisite problem. |
| 2026-10-26 | Keep TeachBooks for the first milestone. | Existing stack fits a mathematical book; configuration cleanup still required. | A demonstrated requirement cannot be met. |
| 2026-10-26 | Establish the design and editorial pattern through Week 1, then proceed in order. | Validate one complete chapter before repeating its patterns. | The first chapter exposes improvements. |
| 2026-10-26 | Use a proposed palette and working title until reviewed in context. | Makes implementation concrete without treating taste as settled. | Owner feedback or rendered review. |
| 2026-10-26 | Use green, pink, brown, and yellow as the main palette; reserve red for attention and yellow for important highlights. | Owner clarified the cute palette and semantic color roles; keep light surfaces distinct from readable foreground colors. | First rendered chapter review. |

**Open questions, not blockers to this planning pass:** Final title/author credit; visual preferences after the first prototype; exact location and source support for the statistics/PCA bridge; attribution details for course materials; current deployment status. Resolve each when its related work becomes active.

## 8. Roadmap

| Horizon | Outcome | Evidence of done |
| --- | --- | --- |
| Now | Complete planning documents in the requested order. | Project-specific bible, weighted baseline rubric, and actionable checklist. |
| Next | Owner/student review of Lecture 1; remaining source map and Lecture 2. | Improve the validated chapter pattern and continue in weekly order. |
| Then | Weeks 2–5 built and reviewed in order. | All five chapters satisfy the same rubric and source coverage requirements. |
| Then | Close statistics/PCA and midterm coverage gaps; integrate review. | Each topic and representative practice type maps to a verified section. |
| Later | Publication-ready navigation, identity, attribution, accessibility, and delivery. | Successful build, rendered review, and separately authorized deployment verification. |

**Parking lot.** Dedicated print/PDF edition, richer interactive figures, executable demonstrations, and later course units. These do not delay a complete initial textbook.

## 9. Authoring and definition of done

Read this file, the rubric, checklist, and relevant source pages before drafting. Match existing chapter conventions or record a deliberate change. Complete a coherent section or chapter and its checks before broadening scope.

A chapter is complete only when source coverage is mapped; prerequisites and objectives are explicit; exposition is continuous; formulas state conditions; examples and solutions are checked; figures have meaningful labels/captions/alt text; practice covers objectives; notation and references are consistent; and the rendered output has been inspected on desktop, a narrow viewport, and print. Log unresolved issues rather than silently waiving them.

**Build verification plan.** Create an isolated environment, install `requirements.txt`, and verify the installed TeachBooks CLI. The intended local build command is `teachbooks build book`; validate it during environment setup before documenting it as tested. Inspect warnings, navigation, references, math, and figures. Do not claim that disabled notebook execution (`book/_config.yml`) validates notebook calculations.

**Handoff.** State the reader outcome, source filenames/page ranges, chapter location, prerequisites, applicable conventions, concrete acceptance checks, open choices, and which documentation needs updating.

## 10. Maintenance

Update canon only after implementation and verification. Keep the roadmap in sync with the single checklist, and reassess the rubric at meaningful milestones. Review this bible at each weekly chapter completion and project restart. Preserve owner edits and separate proposed choices from verified facts.

| Date | Change |
| --- | --- |
| 2026-10-26 | Replaced generic template with the source-grounded textbook brief, planned design system, weekly scope, authoring rules, and verification standard. |
| 2026-10-26 | Revised the proposed palette to soft pastels at the owner's request and clarified foreground usage. |
| 2026-10-26 | Refined the palette to green, pink, brown, and yellow; specified red attention cues and yellow important highlights. |
| 2026-10-26 | Brightened pink to hot pink and green to bright green; warmed brown to caramel and deep cocoa per owner feedback. |
| 2026-10-26 | Assigned structural accents to blue (`#3975DB`); retained warm brown for typography and secondary details. |
| 2026-10-26 | Retained vivid pink/green accents, added contrasting foreground and panel variants, and recorded calculated light-palette contrast ratios. |
| 2026-10-26 | Made A-level exam preparation the professional commission, with method selection, scaffolded-to-independent practice, diagnostic feedback, and demonstrated readiness as acceptance standards. |
| 2026-10-26 | Established the separate knitting/crochet analogy bible and rubric as the canonical connected metaphor system for all taught concepts. |
| 2026-10-26 | Replaced the rejected studio metaphor with actual stitch-action analogies and a specificity-first rubric, following owner correction. |
| 2026-10-26 | Added independent bacteria/virus, astrological-wheel, and original pottery analogy canons and rubrics, preserving knitting/crochet as the main thread. |
| 2026-10-26 | Renamed knitting canon/rubric explicitly; linked all analogy lenses and five ranked candidates through a 36-topic lecture-page source and translation map. |
| 2026-10-26 | Replaced pottery in the active set with full colored-light and multiple-shadow canons and equal-weight rubrics; archived pottery and prepared a head-to-head teaching comparison. |
| 2026-10-26 | Documented the build method, preserved eight originals unchanged in old/, and rebuilt knitting/crochet, biology, astrology, and pottery to a shared six-chapter/36-topic standard. |
| 2026-10-26 | Organized analogy systems into per-theme folders, centralized PDF pages in course-map.md, moved development history to verification/, and standardized all six rubrics as unscored evidence ledgers. |
| 2026-10-26 | Added the three-role teaching strategy: shadows for formal structure, light for targeted contrasts, yarn for recurring narrative and concrete checks, with all-topic allocation and an implementation sequence. |
| 2026-10-26 | Strengthened knitting/crochet as the formal teaching backbone using repeated colorwork, uniform/alternating pattern geometry, marked crochet sectors, chart SVD and centered PCA; shadows/light are optional support. |

**Lecture 1 implementation, 2026-10-26.** [Review record](authoring/lecture1-review.md) documents source coverage, numerical checks, rendered checks, and limits. Later-week plans remain plans.

**Reader format decision, 2026-10-26.** The owner requested Lecture 1 be much shorter,
ideally one or two pages. Its reader route now consists of two concise guides:
vectors/geometry and matrices/products. Prioritize essential definitions, formulas,
a brief craft example, and red exam warnings. Earlier expanded sources remain
available for authoring; the main navigation does not include their long practice
and solution sections. This is a summary, not the earlier full teaching sequence.

**Coverage clarification, 2026-10-26.** The concise Lecture 1 must retain all listed
vector/matrix topics, every distinct lecture example, the cosine/orthogonality proof
relationships, dot-product properties, and all matrix-product properties. Combine
progressive reveals and shorten prose; do not omit formulas or examples to meet a
printed page count. Keep two reader pages, allowing additional print sheets for
legible mathematics. [Coverage audit](authoring/lecture1-coverage.md) is the checklist.

**Current reader format, 2026-10-26.** The owner clarified that the problem was
excessive website navigation, not print length, and rejected the formula-sheet
presentation. Restore the original textbook voice, prose, diagrams, worked
examples and checkpoints; consolidate concepts instead of compressing typography.
**Maximum four website pages per lecture, including exercises and solutions.**
Lecture 1 uses vectors/geometry, matrices/products, exercises, solutions. Source
notes and synthesis belong within these pages. Printed sheet count does not govern
content. Earlier short-guide/print-limit decisions above are superseded.

**Teaching structure requirement.** Four website pages is a navigation cap, not
permission to flatten a chapter into continuous text. Lecture 1 uses sections
1.1–1.12. Each has a learning goal, a motivating question, a source-page label,
explanation/definitions, a checkpoint, a takeaway, and linked practice. Number
worked examples and show intermediate reasoning and verification. Distinguish
Definition, Theorem/Key Result, Proof, Worked Example, ML Connection, and Pitfall
visually and by text labels. Open with prerequisites and measurable outcomes;
close with synthesis, an unaided readiness checklist, and a targeted exercise map.

**Current analogy decision.** The owner selected shadows. Active reading pages,
examples, four diagrams, exercises, solutions, and book branding now use marked
points and calibrated views. Retain the 12-section teaching structure and four-page
navigation cap. Other lenses remain available as references; prior craft-centered
instructions above are historical where they conflict with this decision.

**Lecture 2 systems implementation, 2026-10-27.** The requested Week 2 systems
material (PDF pp. 1–21) follows the same shadow-led teaching sequence in four
website pages: systems/modelling, elimination/echelon forms, exercises, solutions.
Eight numbered sections/checkpoints, three original diagrams, and 18 explained
practice problems preserve source examples and distinguish Gaussian elimination
with back substitution from Gauss–Jordan to RREF. Determinants/inverses on
pp. 22–36 remain open. See [coverage](authoring/lecture2-coverage.md) and
[review](authoring/lecture2-review.md). Publication and learner outcomes are unverified.
