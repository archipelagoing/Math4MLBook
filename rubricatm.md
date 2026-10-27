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

**Standalone reading gate:** Review with the slides closed. A slide reference
passes only when the textbook includes the example's full problem data and
reasoning, or a faithful labeled diagram with caption, alt text and explanation
for a referenced figure. A citation or “as shown in the slides” cannot replace
essential material. Earlier textbook dependencies must be restated or linked.

**References:** [SHOW_BIBLE.md](SHOW_BIBLE.md), [todoSimple.md](todoSimple.md),
`resources/lectures/`, `resources/HW/`, `resources/practiceExams/`, `book/_toc.yml`,
`book/_config.yml`. The README records local setup and chapter scope; inspect rendered output rather
than treating documentation alone as proof of behavior.

**Analogy companion:** [The Object Behind the Shadows](analogy/systems/shadows/canon.md)
is the selected canonical system; its [rubric](analogy/systems/shadows/rubric.md)
checks domain specificity, mathematics, continuity and transfer. Use matched points,
calibrated parallel-ray views, explicit spaces, and the distinction between one
point's coordinates and a profile across points. Do not infer arbitrary solid
reconstruction from silhouettes, or identify record-space geometry with physical
orientation. A high analogy score does not establish textbook completion.

Other systems remain references in [the analogy index](analogy/README.md).
The [build method](analogy/build-method.md) defines their common standard; original
snapshots in `analogy/old/` are unchanged. The
[comparison](analogy/comparisons/light-vs-shadows.md) records the reasoning for the
selected lens, without claiming measured learner effectiveness.

**Primary teaching strategy:** The [shadow-led plan](analogy/teaching-strategy.md)
requires a connected path from point coordinates to observations, independent
views, fitting, decomposition and point data. Use the selected canon's O and H;
identify supplementary record tables such as the four-bead X profiles. The earlier
craft-led strategy is historical. Preserve formal lecture examples and exam transfer.

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

**Date:** 2026-10-27. **Base commit:** `718e1b7`, with local Lecture 4 implementation.

**Current format:** Lecture 1 retains its 12 sections and 24 exercises. Lecture 2
now covers **all 36 PDF pages** in 14 lettered parts A–N, following lecture order.
It has 17 worked examples with highlighted numbered steps, 14 checkpoints,
a dedicated TL;DR cheat sheet and 26 exercises with expandable solutions.
Its four numbered reader pages are systems/elimination, determinants/geometry,
inverses/invertibility, and TL;DR. Practice and expandable answers are integrated
by topic. Lecture 1 likewise uses vectors, geometry, matrices and TL;DR. The earlier systems-only scope is superseded.
Lecture 3 now covers all 35 PDF pages in 11 ordered parts with 16 worked
examples, 28 questions, four diagrams and a mixed independent rehearsal.
Lecture 4 now covers all 28 PDF pages in 11 ordered parts with 14 stepwise worked
examples, six original diagrams, 28 integrated questions, selected worksheet/
recitation alignment and a fresh mixed rehearsal. Lecture 5, the statistics/PCA
bridge and cumulative exam assessment remain open.

The provisional whole-book score remains **56.25/100** under the same broad score
bands and weights. Four covered lecture decks strengthen delivered coverage, but
five-week completion, independent review and student outcomes are not established.

| Criterion | Weight | Score / 4 | Contribution | Current evidence and limits |
| --- | ---: | ---: | ---: | --- |
| Weekly coverage and source fidelity | 20 | 2 | 10 | Lectures 1–4 have specific source audits, including Week 4 projection/fit/Gram–Schmidt data and conditions. Week 5, statistics/PCA and the full exam blueprint remain open. |
| Mathematical correctness and precision | 20 | 2 | 10 | Exact systems, determinants, cofactor arrays, both inverse products, dimensions/conditions and parameter families checked. Independent expert review and later material remain open. |
| Exposition and learning progression | 20 | 2 | 10 | 48 learning sections/parts across Lectures 1–4. Highlighted steps explain operations and checks; later-week progression remains open. |
| Practice and assessment | 15 | 2 | 7.5 | 106 exercises with explained answers/revision links and 48 checkpoints; Lecture 3 adds fresh variants, selected supporting-problem mapping and a scored mixed rehearsal. All four TL;DR pages support review. Cumulative timed assessment and learner outcomes remain open. |
| Visual design and accessibility | 15 | 3 | 11.25 | Shared readable palette, 17 active diagrams, blue step labels, yellow results, red pitfalls, mobile/desktop and keyboard/print checks. Full accessibility audit remains open. |
| Build integrity and reproducibility | 5 | 4 | 5 | Strict build, 95 Lecture 1, 98 Lecture 2, 223 Lecture 3 and 409 Lecture 4 checks, reproducible diagrams and browser scripts. Lecture 3 verified live; Lecture 4 remains local. |
| Editorial completeness and delivery | 5 | 2 | 2.5 | Four numbered sidebar pages per lecture, integrated practice/answers, root AGENTS.md, current show-bible contract, source notes and review maps. Later chapters, final credits and publication remain open. |
| **Total** | **100** | | **56.25** | |

**Verification:** [Lecture 1 record](authoring/lecture1-review.md) and
[Lecture 2 record](authoring/lecture2-review.md), plus the current
[Lecture 3 record](authoring/lecture3-review.md) and
[Lecture 4 record](authoring/lecture4-review.md). Each browser review passes
10 page/viewport checks, inspecting actual numbered sidebar labels and topic-based
practice allocation. All answers can be keyboard-opened and all local article
links resolve. No math errors, JavaScript errors or page-wide overflow were found,
including with answers expanded on phones. Local success does not confirm the live site.

**Next improvements:** Gather comprehension feedback; continue remaining weekly
chapters; complete supporting-problem and official exam topic mapping. Apply the
full-deck, source-order, highlighted-step and TL;DR standard to subsequent work.

**Lecture 2 completion audit, 2026-10-27:** [Chapter assessment](authoring/lecture2-assessment.md)
distinguishes complete slide coverage from incomplete exam-readiness preparation.
Problems 20, 22, 24 and 25 repeat worked matrices; fresh determinant/inverse
variants and a mixed independent check remain needed. Supporting homework/exam
question mapping is still open. The 98-check arithmetic run and strict build
passed again. The provisional score above remains a whole-book score, not a
chapter grade; full A-level preparation is not declared complete.

**Lecture 3 evidence:** [Coverage](authoring/lecture3-coverage.md) and
[verification](authoring/lecture3-review.md) document the full source chapter,
source corrections and supporting-problem links. Ten new desktop/mobile checks
and 239 local article links pass. Fresh practice and a transparent mixed check
address the preparation weaknesses identified in the Lecture 2 audit, without
claiming that student readiness or whole-course exam alignment has been demonstrated.
The earlier Lecture 2 audit and its remaining tasks are unchanged.

**Lecture 4 evidence:** [Coverage](authoring/lecture4-coverage.md) and
[verification](authoring/lecture4-review.md) record the full deck, source-order
teaching, independent arithmetic, browser/print inspection, and selected worksheet
and recitation alignment. The whole-book score remains in the same provisional
bands: four lectures do not establish all-five-week coverage, expert review, a
complete exam blueprint or actual student readiness. The prior Lecture 2 audit
and its remaining preparation tasks are unchanged.
