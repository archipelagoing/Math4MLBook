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

**Date:** 2026-10-26.
**Base commit:** `b1e21f70c9921e91c386f6836f3717498b14da06`; assessment includes
uncommitted Lecture 1 manuscript, design, build configuration, checks, and documentation.
**Status:** First locally validated chapter. Same five-week target and weights as
the initial 10/100 baseline; this is not a student grade or an exam-readiness score.
**Total:** **56.25/100**, provisional whole-book assessment. The full exam-readiness
gate remains unmet because later weeks and cumulative/timed practice are absent.

| Criterion | Weight | Score / 4 | Contribution | Evidence and included work | Missing / unknown |
| --- | ---: | ---: | ---: | --- | --- |
| Weekly coverage and source fidelity | 20 | 2 | 10 | `book/lecture1/source-notes.md`: complete Week 1 deck map and attributed added exposition. | Weeks 2–5, exact supporting-problem mapping, statistics/PCA gap, complete exam blueprint. |
| Mathematical correctness and precision | 20 | 2 | 10 | Five teaching sections and 24 solutions; 67 recomputation/pairing/figure checks; source image spot checks; hypotheses and derivations reviewed. | Independent reviewer absent; later-week mathematics not authored or audited. |
| Exposition and learning progression | 20 | 2 | 10 | Objectives, connected craft examples, formal definitions, derivations, method cues, five checkpoints, synthesis and transfer. | Later chapter progression and observed learning effectiveness unverified. |
| Practice and assessment | 15 | 2 | 7.5 | 24 graduated problems with explained answers, six optional synthesis hints, objective mapping and readiness prompts. | Whole-exam skill coverage, timed mock exam, scoring guide, reader performance. |
| Visual design and accessibility | 15 | 3 | 11.25 | Custom palette/typography, four SVGs, all reader pages checked at desktop/mobile widths, representative dark/print checks, keyboard answers, explicit contrast pairs. | Full assistive-technology audit, later-week figures, owner/reader aesthetic feedback. |
| Build integrity and reproducibility | 5 | 4 | 5 | Isolated Python 3.12 setup, pinned direct dependencies, README instructions, clean TeachBooks and strict Jupyter Book builds, valid references/assets. | Hosted CI/deployment unverified; MathJax depends on CDN access. |
| Editorial completeness and delivery | 5 | 2 | 2.5 | Working identity, reader navigation, source notes, setup guide, chapter conventions and review record. | Final human author credit, whole-book notation/credits, publication and full course coverage. |
| **Total** | **100** | | **56.25** | | |

**Checks performed:** [Lecture 1 review record](authoring/lecture1-review.md) gives
source pages, objective-to-practice mapping, checked calculations, dependency
versions, browser results, contrast pairs, and limitations. The original scaffold
had one warning; the current reader book builds without warnings. Browser checks
covered 11 pages at 1440/390 pixels, with 456 rendered math expressions per viewport,
no MathJax errors, no page-wide overflow, and no JavaScript errors. Practice links
use valid MyST references. Keyboard checkpoint answers and print expansion work.
The geometry diagram now uses equal unit scales in its orthonormal coordinates.

**Critical gaps:** The book is not complete midterm preparation. Weeks 2–5,
statistics/PCA placement, visual-only supporting PDFs, cumulative/timed assessment,
and exact homework/exam mapping remain open. No student outcome, independent
craft execution, independent math review, or live deployment is claimed.

**Top three next improvements:**

1. Review the first chapter with the owner/student and correct any confusing
   explanation or visual; gather evidence from unaided formal problems (§4).
2. Complete the source/notation map and author Lecture 2 using the checked chapter
   pattern, then continue in weekly order (§§2, 5–8).
3. Close exam coverage with cumulative practice, a timed mock exam, explained
   scoring, and targeted revision paths (§§9–10).

**Change since previous assessment:** +46.25 points against the same weights.
Credit now rests on a real first chapter and local verification, replacing the
source/template-only baseline. This gain does not establish an A-level outcome.
