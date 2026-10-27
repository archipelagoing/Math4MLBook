# Math4MLBook — Rubric at the Moment

This file defines the target and holds one current assessment. The bible defines
identity and rules; this rubric measures the result; `todoSimple.md` tracks work.
Git history preserves older assessments.

## Project target

**Project:** [Math4MLBook](https://github.com/archipelagoing/Math4MLBook), working title
*Mathematical Foundations of Machine Learning*.

**Intended reader:** A student learning the course's first six weeks independently,
consolidating lectures, or preparing for the midterm.

**Core job:** Understand, explain, and apply the mathematics taught in the supplied
resources well enough to target an A on the exam: solve unfamiliar conceptual and computational problems independently, justify method selection, check work, and communicate reasoning under exam conditions.

**Best credible version:** A coherent professional textbook develops the weekly
slides into connected exposition, precise definitions and results, instructive
proofs, labeled mathematical figures, and fully explained examples. Six weekly
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

**Boundaries:** Authorized coverage is Weeks 1–6 plus necessary bridges and midterm
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

**Date:** 2026-10-27. **Base commit:** `f395bc4`, with the existing local Lecture 5
work preserved and new Week 6 content. No commit, push or publication performed.
The owner extended authoring to the newly supplied 39-page PCA deck. Its second
PDF is an identical copy, not a separate lecture; later Week 8 resources are not
counted as taught.

**Delivered:** Lectures 1–6 have four numbered topic/review pages each. Week 6
closes the prior statistics/PCA teaching gap with full source coverage, mean,
variance/standard deviation, covariance, objective/eigenvector derivation, complete
student scores/reconstruction, scaling, genetics/eigenfaces and failure cases.
The book now has 70 sections/parts with checkpoints, 89 numbered worked examples,
162 integrated questions, 30 original SVG diagrams and two credited empirical
source images. All six lectures finish with method-focused cheat sheets.

The provisional whole-book score remains **71.25/100**, in the same score bands
and weights as the prior assessment. Resolving statistics/PCA strengthens the
coverage, correctness and exposition evidence; a comprehensive exam blueprint,
cumulative mock assessment, remaining Lecture 2 practice tasks, independent expert
review and actual student outcomes are still not established. This is an editorial
assessment, not an A-grade prediction or a claim that later supplied decks are done.

| Criterion | Weight | Score / 4 | Contribution | Evidence and limits |
| --- | ---: | ---: | ---: | --- |
| Weekly coverage and source fidelity | 20 | 3 | 15 | Full source audits through Week 6, including all 39 PCA pages and the statistics requirements. Comprehensive supporting-exam/skill blueprint remains open; Week 8 is outside this task. |
| Mathematical correctness and precision | 20 | 3 | 15 | Six checkers pass. Week 6 verifies exact covariance/eigenvectors, projections, score variance, reconstructions, normalization, standardized metric, zero/tied/outlier cases and source data. Independent expert review remains open. |
| Exposition and learning progression | 20 | 3 | 15 | Six connected chapters, 70 sections/parts, 89 highlighted examples, complete source figures/data and six cheat sheets. Learner comprehension feedback and cumulative synthesis remain needed. |
| Practice and assessment | 15 | 2 | 7.5 | 162 questions with explanations and diagnostic revision/retry links, fresh mixed rehearsals through Week 6, and selected supporting-question mapping. The full mock/blueprint and existing Lecture 2 fresh-variant tasks remain incomplete. |
| Visual design and accessibility | 15 | 3 | 11.25 | 30 original diagrams and two credited source figures, semantic highlights, desktop/phone, keyboard, dark and print evidence. Full accessibility and learner testing remain open. |
| Build integrity and reproducibility | 5 | 4 | 5 | Strict build; 95/98/223/409/632/646 checks for Lectures 1–6; browser scripts, SVG generators and reproducible source-image extraction. Live publication is separate. |
| Editorial completeness and delivery | 5 | 2 | 2.5 | Numbered sidebar, integrated practice banks, current agent rules, source/review records and statistics/PCA destination. Final credits, cumulative assessment and current publication remain open. |
| **Total** | **100** | | **71.25** | |

**Evidence:** [Lecture 1](authoring/lecture1-review.md),
[Lecture 2](authoring/lecture2-review.md), [Lecture 3](authoring/lecture3-review.md),
[Lecture 4](authoring/lecture4-review.md), [Lecture 5](authoring/lecture5-review.md),
[Lecture 6](authoring/lecture6-review.md). Week 6 passes ten desktop/phone cases
and 196 local article links/assets, with no MathJax, exposed-TeX, JavaScript or
page-wide-overflow errors, including all 28 expanded answers. Lecture 5 regression
passes ten cases and 189 links/assets with the six-lecture sidebar. Source and
original figures, representative worked steps, dark theme and all three print
pages were inspected. Transient disk-space failures in the regression tooling
were resolved by using /tmp for Chromium temporary files; no source data was removed.

**Preserved open audit:** [Lecture 2 assessment](authoring/lecture2-assessment.md)
records repeated matrices in Problems 20/22/24/25; fresh determinant/inverse variants
and a mixed check remain needed. Earlier chapters have not all received a new
slides-closed audit during Week 6. Editorial practice timing and thresholds do
not establish official exam rules, a course A cutoff or demonstrated readiness.

**Next priorities:** Complete the course-wide skill/problem blueprint and a fresh
cumulative mock; address Lecture 2’s remaining practice gaps; gather comprehension
feedback. Author later weeks only when requested, following the same full-source
and standalone-reading rules.
