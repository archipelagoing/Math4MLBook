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

**Analogy companion:** [Knitting Crochet](analogy/systems/knitting-crochet/canon.md) is the canonical knitting/
crochet action web, grounded in named stitches, magic-ring rounds, cast-on/bind-off,
and swatch measurements; [Knitting Crochet Rubric](analogy/systems/knitting-crochet/rubric.md) scores its coverage,
fidelity, continuity, and transfer separately. Main textbook reviews should check
that chapter analogies explain actual craft mechanisms, preserve mathematics and
representation boundaries, and lead back to ordinary
exam questions. A high analogy score does not establish textbook completion.
Additional independent references and rubrics cover [bacteria/viruses](analogy/systems/bacteria-viruses/canon.md),
the [astrological wheel](analogy/systems/astrology/canon.md),
[colored light](analogy/systems/colored-light/canon.md),
[multiple shadows](analogy/systems/shadows/canon.md), and [rebuilt pottery](analogy/systems/pottery/canon.md).
The [build method](analogy/build-method.md) defines the common artifact
standard; the four earlier pairs are unchanged in `analogy/old/`. All six current
rubrics use the same unscored evidence-ledger status; prior light/shadow scores
are historical. Exact PDF-page mappings live only in the shared course map.
The [head-to-head comparison](analogy/comparisons/light-vs-shadows.md) distinguishes
editorial preference from observed learner effectiveness.
Each reference links its own rubric. Verify the chosen lens against its own canon;
do not require all analogies in every passage or conflate their entities.

**Primary teaching strategy:** The [craft-centered plan](analogy/teaching-strategy.md)
requires knitting/crochet to lead substantial mathematical examples in every week.
The sampler panel and marked crochet round extend the ledger to geometric, spectral,
and statistical topics. Evaluate shadows/light as optional clarifications rather
than evidence that yarn can be omitted from later formal teaching.

**Lecture alignment:** [The shared analogy course map](analogy/course-map.md)
provides topic IDs, exact extractable lecture-page destinations, all current lens
routes, and proposed top-five routes. Check analogy claims against that register
and its source-precision notes; registered mappings are not delivered chapters.

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

**Date:** 2026-10-26. **Base commit:** `d32974f00ec255101866c20df1d0ffd13cf1deb6`;
includes uncommitted concise-edition changes.

**Current format:** The owner requested Lecture 1 in one or two pages. The reader
route now has two guides retaining every distinct lecture example, definition, formula,
and multiplication property, with concise explanations and exam warnings. The expanded manuscript and practice bank are retained as
source references outside the TOC. Evaluate the concise guide as a summary;
it does not offer the earlier full independent-study sequence.

The original five-week preparation criteria and weights remain below. The current
whole-book score is **52.5/100 provisional**; it measures remaining breadth and
assessment work, not whether the requested shorter format is preferable.

| Criterion | Weight | Score / 4 | Contribution | Current evidence and limits |
| --- | ---: | ---: | ---: | --- |
| Weekly coverage and source fidelity | 20 | 2 | 10 | Lecture 1 key concepts summarized with source attribution; expanded source map retained. Later weeks and complete exam blueprint remain open. |
| Mathematical correctness and precision | 20 | 2 | 10 | Definitions, conditions, example calculations, and matrix dimensions checked. Full independent review and later-week work remain open. |
| Exposition and learning progression | 20 | 2 | 10 | Concise source examples, coordinate interpretations, cosine/orthogonality derivation, and operation-selection warnings; later-week progression remains open. |
| Practice and assessment | 15 | 1 | 3.75 | Brief self-checks; the 24-problem bank remains in source files rather than reader navigation. Timed/cumulative assessment remains open. |
| Visual design and accessibility | 15 | 3 | 11.25 | Yellow formulas, red pitfalls, readable palette, mobile and desktop math checks, print layout. Full accessibility audit remains open. |
| Build integrity and reproducibility | 5 | 4 | 5 | Documented environment, clean strict build, numerical checks, updated browser review script. Live deployment of this revision unverified. |
| Editorial completeness and delivery | 5 | 2 | 2.5 | Two-page navigation and updated welcome/setup/status documents. Later guides, final credits, and publication remain open. |
| **Total** | **100** | | **52.5** | |

**Verification:** See [the current edition note](authoring/lecture1-review.md).
Strict build passed. All three reader pages were checked at 1440/390 pixels:
no MathJax errors, page-wide overflow, or JavaScript errors. The retained
expanded-edition checker still passes 77 numerical/structural checks, including restored source examples.

**Next improvements:** review the concise guide with the student; continue to
Lecture 2 when authorized; resolve the statistics/PCA and exam coverage gaps.
Student outcomes and independent review remain unverified.

**Comparison:** The earlier 56.25 assessment applied to the expanded reader route; the first compact edition scored 47.5 before source examples and derivations were restored.
This revision intentionally changes how much exposition/practice is shown;
the scores are not a direct comparison of the two formats' usefulness.
