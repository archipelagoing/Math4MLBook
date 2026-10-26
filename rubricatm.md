# Math4MLBook — Rubric at the Moment

This file defines the target and holds one current assessment. The bible defines
identity and rules; this rubric measures the result; `todoSimple.md` tracks work.
Git history preserves older assessments.

## Project target

**Project:** [Math4MLBook](https://github.com/archipelagoing/Math4MLBook), working title
*Mathematical Foundations of Machine Learning*.

**Intended reader:** A student learning the course's first five weeks independently,
consolidating lectures, or preparing for the midterm.

**Core job:** Understand, explain, and apply the mathematics taught in the supplied
resources well enough to target an A on the exam: solve unfamiliar conceptual and computational problems independently, justify method selection, check work, and communicate reasoning under exam conditions.

**Best credible version:** A coherent professional textbook develops the weekly
slides into connected exposition, precise definitions and results, instructive
proofs, labeled mathematical figures, and fully explained examples. Five weekly
chapters build on one another and include graduated practice with checked solutions.
Statistics and PCA from the midterm topic list have explicit learning destinations,
with supplements identified where the lecture sources do not cover them. A warm,
colorful, consistent design supports sustained reading on desktop and mobile,
with legible math and useful print output. The book builds reproducibly and its
attribution, navigation, and documentation match the actual project.

**Professional accountability:** Evaluate this as a commissioned textbook written by a
paid professional educator responsible for giving the client the strongest practical
preparation for an A. Every section should remove a learning obstacle or develop an
assessed skill. The book must bridge the gap between understanding an example and
solving a fresh problem independently. Actual student performance is separate from
editorial completeness; record it only when observed or reported.

**Boundaries:** Initial coverage is Weeks 1–5 plus necessary bridges and midterm
review. A new application framework, accounts, grading platform, later course
units, and sophisticated interactive demonstrations are not completion requirements.
A standalone typeset PDF is a later goal; usable browser print is in scope.

**Target environment:** The existing TeachBooks/Jupyter Book v1/MyST/Sphinx project;
static HTML as primary output. Verify desktop and narrow layouts in available
browsers, keyboard access, math rendering, and browser print. No deployed site or
specific browser compatibility has been verified in this baseline.

**Success signals:** Each source topic maps to a chapter section; a student can
follow methods without the slides or lecture audio; every major method has a
verified worked example; practice and solutions address every learning objective;
readers can distinguish concepts through labels as well as color; builds and
rendered checks produce recorded evidence. An exam blueprint connects every assessed
skill to instruction and independent practice; fresh mixed and timed problems reveal
weaknesses; diagnostic feedback leads to targeted revision and successful retries.
Use a supplied official A cutoff when available and label any other practice threshold
as an editorial mastery target, not a statement of course grading policy.

**References:** [SHOW_BIBLE.md](SHOW_BIBLE.md), [todoSimple.md](todoSimple.md),
`resources/lectures/`, `resources/HW/`, `resources/practiceExams/`, `book/_toc.yml`,
`book/_config.yml`. The README is currently template documentation, not evidence
of completed textbook behavior.

**Analogy companion:** [ANALOGY_WEB.md](ANALOGY_WEB.md) is the canonical knitting/
crochet action web, grounded in named stitches, magic-ring rounds, cast-on/bind-off,
and swatch measurements; [ANALOGY_RUBRIC.md](ANALOGY_RUBRIC.md) scores its coverage,
fidelity, continuity, and transfer separately. Main textbook reviews should check
that chapter analogies explain actual craft mechanisms, preserve mathematics and
representation boundaries, and lead back to ordinary
exam questions. A high analogy score does not establish textbook completion.
Additional independent references and rubrics cover [bacteria/viruses](ANALOGY_BACTERIA_VIRUSES.md),
the [astrological wheel](ANALOGY_ASTROLOGICAL_WHEEL.md), and [pottery](ANALOGY_POTTERY.md).
Each reference links its own rubric. Verify the chosen lens against its own canon;
do not require all four analogies in every passage or conflate their entities.

## Scoring rules

- Score the checked-out implementation, identifying local changes separately.
  Plans and source PDFs do not count as completed reader-facing chapters.
- Each criterion receives 0–4. Contribution = `weight × score / 4`; weights total 100.
- Use 0 for confirmed absence, 1 for an initial scaffold with the main outcome
  blocked, 2 for partial usable coverage, 3 for the intended outcome with limited
  gaps, and 4 for the target with supporting evidence.
- Distinguish **missing** from **unknown**. Give provisional scores where feasible,
  explain uncertainty, and do not silently turn an unrun check into a failure.
- Source paths, verified calculations, build logs, and rendered artifacts support
  claims. Configuration alone does not prove deployed or accessible behavior.
- Keep weights stable. A changed goal or weight set establishes a new baseline.
- Record mathematical errors, inaccessible essential content, broken builds, and
  missing core coverage separately even when the total is high.
- Future assessments replace only **Latest assessment** unless the user requests
  changes to the target or criteria.

## Scoring rubric

| Criterion | Weight | A 4/4 means |
| --- | ---: | --- |
| Weekly coverage and source fidelity | 20 | All five weeks are mapped at section/page level; teaching progression is preserved; required midterm topics including statistics/PCA are accounted for in an exam blueprint linking each assessed skill to teaching, examples, independent practice, and readiness checks; additions and corrections are identified. |
| Mathematical correctness and precision | 20 | Definitions, theorems, dimensions, hypotheses, derivations, examples, and solutions are independently checked, including singular, dependent, zero, rectangular, and non-diagonalizable cases where relevant. |
| Exposition and learning progression | 20 | A student can study without lecture audio: prerequisites, motivation, connected explanations, proofs where useful, geometry, examples, synthesis, and transitions build understanding; explicit method-selection guidance and decreasing scaffolding prepare the student to solve unfamiliar exam questions unaided. |
| Practice and assessment | 15 | Every assessed skill has conceptual, computational, and transfer practice; scaffolding decreases toward fresh mixed and timed tasks; checked solutions model clear reasoning and verification; diagnostic feedback points to revision and retry problems; a mock exam and transparent practice scoring guide support an explicit readiness judgment. |
| Visual design and accessibility | 15 | Shared typography, palette, components, and figures form a polished reading experience; contrast, labels, alt text, keyboard access, mobile math, dark theme, and print have been checked in rendered output. |
| Build integrity and reproducibility | 5 | A documented isolated setup builds successfully; references, figures, links, and relevant notebook outputs are verified; dependencies and workflow are maintainable. |
| Editorial completeness and delivery | 5 | Identity, navigation, notation reference, source attribution, credits, reader guide, and maintenance docs are accurate; release evidence is recorded when publication is authorized. |
| **Total** | **100** | |

For coverage, a 1 means source inventory/scaffold only, a 2 means some complete
weekly chapters, and a 3 means all weeks are substantially taught with specific
coverage gaps remaining. For correctness, source solutions alone do not earn
verification credit. For visual design, a palette proposal alone earns no
implementation credit; a 1 may reflect the existing theme scaffold only.

**Exam-readiness gate:** Do not describe the book as A-level preparation complete
while assessed topics lack independent practice, major solutions remain unchecked,
or mixed/timed readiness checks and diagnostic revision paths are absent. Visual
polish cannot waive these gaps. Student readiness itself remains unverified until
there is evidence from their independent performance.

## Assessment prompt

```text
Assess the current Math4MLBook implementation using rubricatm.md.
Read the target, rules, SHOW_BIBLE.md, and current todoSimple.md first.
Inspect actual chapters against source PDF pages, supporting problems, and the
midterm topic list. Audit the exam blueprint, method-selection teaching, decreasing
scaffolding, fresh mixed/timed practice, diagnostic feedback, and readiness checks.
Distinguish completed preparation materials from observed student performance.
Review mathematical conditions and independently check
representative computations and solutions. Inspect rendered reading, practice,
navigation, accessibility, mobile math, and print where feasible. Run relevant
build checks and state exactly what was not tested.
For each criterion record score, contribution, included work, missing work,
unknowns, and evidence. Do not award chapter credit for plans or raw PDFs.
Identify the three improvements with the largest reader impact and observable
acceptance conditions, referencing the checklist rather than inventing issues.
Replace ONLY Latest assessment. Record date, commit, local changes, uncertainty,
checks, blockers, and whether comparisons use the same target and weights.
```

## Latest assessment

**Date:** 2026-10-26.  
**Commit:** `6657df146cf1bfa98d515d6f192ce16aa6d0d806` (`main`).  
**Local changes:** The three planning templates are being populated in this working
tree; this assessment gives no implementation credit for their planned chapters.  
**Status:** Provisional source-inspection baseline. No book build, rendered review,
full source visual audit, or independent mathematical audit performed.  
**Target version:** Initial five-week professional textbook, clarified on 2026-10-26
to require A-level exam preparation. Weights unchanged; this is the new target
baseline. Implementation remains the inspected scaffold, with no new readiness evidence.  
**Total:** **10/100 provisional**, with correctness, rendered accessibility, build
execution, and deployment outcomes unverified as described below.

| Criterion | Weight | Score / 4 | Contribution | Evidence and included work | Missing / unknown |
| --- | ---: | ---: | ---: | --- | --- |
| Weekly coverage and source fidelity | 20 | 1 | 5 | Five lecture PDFs and supporting materials exist in `resources/`; deck topics and page counts inspected by text extraction. | No weekly chapters or section-level source map; statistics/PCA placement unresolved. |
| Mathematical correctness and precision | 20 | 0 provisional | 0 | `book/some_content/overview.md` is filler; `book/intro.md` is a template welcome. | Intended mathematical exposition absent. Source answers and visual-only annotations are unverified, not established incorrect. |
| Exposition and learning progression | 20 | 0 | 0 | `book/_toc.yml` organizes template content and authoring tutorials. | No course learning path, explanatory weekly sections, objectives, or textbook synthesis. |
| Practice and assessment | 15 | 0 | 0 | Homework and exam PDFs exist; `book/exercises/` contains template authoring exercises. | Course practice and checked solutions are not integrated into the reader-facing book. |
| Visual design and accessibility | 15 | 1 provisional | 3.75 | Theme configuration, template logos, and `book/_static/attribution.css` provide an initial presentation scaffold. | Textbook styling/figures absent; theme usability, contrast, mobile, keyboard, dark mode, and print unverified. |
| Build integrity and reproducibility | 5 | 1 provisional | 1.25 | `requirements.txt`, `_config.yml`, `_toc.yml`, and `.github/workflows/call-deploy-book.yml` exist. | Build tools unavailable on inspected PATH; install, successful build, warning baseline, and CI results unverified. |
| Editorial completeness and delivery | 5 | 0 | 0 | Project files and template credits/license exist. | Title/author/URLs, reader navigation, source-specific attribution, and README remain template-oriented; live delivery unknown. |
| **Total** | **100** | | **10** | | |

**Checks performed:**

- Enumerated repository files and inspected book navigation, introduction,
  configuration, stylesheet, requirements, workflow, and planning templates.
- Extracted all 18 source PDFs using `pdftotext -layout` into temporary files outside
  the repository. The five lecture decks contain 48, 36, 35, 28, and 44 pages.
  This is a topic inventory, not a complete mathematical or diagram review.
- Compared extracted Week 5 topics with `MidtermTopics.md`: the list includes
  statistics/PCA, while their terms were not present in the extracted Week 5 text.
- Found no non-whitespace extracted content in `Recitation1_Solutions.pdf` or
  `PT1_f22Sol.pdf`; their actual page content remains to be reviewed visually.
- Checked CLI availability: neither `teachbooks` nor `jupyter-book` was on PATH.
  Dependencies were not installed for this documentation-only task.
- Did not run a build, execute notebook content, inspect a browser, or verify deployment.

**Critical gaps:** The main reader outcome is unavailable because weekly textbook
chapters are absent. The midterm scope gap and visual-only source pages require
explicit review during authoring. No mathematical failure or deployment failure
is claimed without verification.

**Top three next improvements:**

1. **Map sources and establish notation.** Every weekly topic and exam topic gets
   a planned destination with exact PDF pages/problem references; unreadable pages
   and statistics/PCA gaps are resolved or explicitly tracked. See checklist §2.
2. **Build a complete Week 1 chapter and shared visual pattern.** It teaches every
   Week 1 topic with checked examples, meaningful figures, checkpoints, practice,
   and explained solutions. A local build and desktop/mobile/print inspection
   establish a reusable chapter standard. See checklist §§3–4.
3. **Extend that standard through Weeks 2–5 and close exam coverage.** Each chapter
   meets the bible's definition of done and all midterm topics map to a learning
   section and practice. See checklist §§5–9.

**Change since previous assessment:** First project-specific assessment; the generic
template contained no usable prior scores. Future comparisons must use these same
weights and disclose differences in verification depth. The A-level commission
clarifies the target and strengthens acceptance criteria on 2026-10-26; the unchanged
10/100 scaffold baseline is not a measured improvement or student-readiness score.
