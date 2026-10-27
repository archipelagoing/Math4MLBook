# Building a Connected Analogy System

2026-10-26 · A reproducible authoring method for every analogy lens
[Shared course map](course-map.md) · [Light example](systems/colored-light/canon.md)
[Shadow example](systems/shadows/canon.md) · [Main bible](../SHOW_BIBLE.md)

## Purpose and evidence

This documents the authoring sequence used for the light/shadow references and
the common standard for all six systems. Selection history and earlier assessment
results live in [development history](verification/history.md). It describes editorial and mathematical work, not private
reasoning or an experiment that was never performed. Domain sources were consulted,
local lecture text was inspected, numerical identities were checked, and structural
checks were run. Physical demonstrations, rendered teaching figures, qualified
independent reviews, and learner trials were not performed.

“Equally built out” means equal required deliverables and course coverage, not
identical word counts or unsupported claims of equal teaching effectiveness.
An analogy canon is an editorial foundation; it does not by itself replace the
actual textbook chapters, full proofs, illustrations, and fresh exercise bank.

## 1. Start from the course, not an attractive metaphor

Read the five lecture PDFs, the exam topic list, and relevant supporting materials.
Extract PDF text with `pdftotext -layout` and retain one-based PDF page numbers.
Consolidate repeated reveal slides without dropping their teaching steps. Identify
pages whose diagrams/handwriting are not represented in extracted text.

**Current source reference:** The 36 topic groups and outstanding image-review
gaps are maintained in [the course map](course-map.md). Statistics/PCA must retain
their exam-topic supplement label until lecture support is established. Supporting
problem-number mapping remains incomplete.

**Deliverable:** A source/topic register. Every topic needs a source page or an
explicit supplement label. This register governs all lenses.

## 2. Choose one recognizable scene with a productive question

Specify something a person can do or observe, not a domain noun attached to a vector.
Choose a question that can deepen across all five weeks.

- Light: adjust sources and compare spectra with sensor readings. How can the
  underlying light change without its recorded response changing?
- Shadows: move a marked bead and observe calibrated screens. Which movements
  remain invisible, and what additional view reveals them?

**Deliverable:** A compelling opening, a central question, and a sequence of actual
mechanisms that naturally connects representation → equations → information loss
→ approximation → decomposition → variation.

## 3. Verify the domain premise and separate fact from invention

Use primary technical sources or recognized domain practitioners. Record sources
next to supported claims. Mark a toy model, invented dataset, illustrative parameter,
and original diagram as such. A citation to real metamerism does not make a toy
matrix a measured human-vision model; a reference on orthographic views does not
validate arbitrary silhouette reconstruction.

**Deliverable:** A short source boundary and a list of unverified domain assumptions.
Never claim a real experiment, calibrated apparatus, or empirical result that did
not happen. Recheck a source when adding a new factual claim outside its support.

## 4. Fix the scene's objects, spaces, and units

Write a canonical vocabulary before producing examples. For each symbol, state
what it represents, its dimension, its physical domain, and what it does not encode.

- Light: four sampled powers s, three responses y, sensor A, source spectra L,
  source coefficients c, available-source map G=AL.
- Shadows: one world point x, single view O, stacked views H, screen record b,
  embedded object projector P, measurement-space projector Q.

**Deliverable:** A vocabulary table and continuity rules. Distinguish real/signed
extensions from physical quantities, coordinates from objects, origin changes from
linear maps, and input space from output space.

## 5. Build a small exact anchor that teaches information loss

Choose numbers small enough to solve by hand. Keep the anchor throughout the
system. Show two distinct inputs with the same output, their difference in the
null space, and which physical distinctions the record omits.

- Light: A maps two nonnegative four-band spectra to the same three readings.
- Shadows: O maps points with different Z coordinates to the same XY screen mark.

Then derive rank, a full solution family, and **all four fundamental subspaces**.
Some subspaces can be zero. Explain physical feasibility separately from real
solutions; do not manufacture four nontrivial spaces for visual symmetry.

**Deliverable:** An explicit matrix, computed example, full solution family,
rank/nullity, bases or defining equations for the four spaces, and a stated limit.

## 6. Add one complementary anchor for reachability or consistency

The first map may be surjective or have no left-null direction. Introduce a second
mechanism in the same scene to expose the other side of the problem.

- Light: a restricted lamp set G makes some responses unavailable; a target in its
  real span may still require a physically invalid negative intensity.
- Shadows: stacked H removes input ambiguity but adds a consistency condition
  between repeated Y observations.

**Deliverable:** At least one unique/invertible example and one rank-deficient
example across the system, with compatible dimensions and physical constraints.

## 7. Derive projection, fitting, and Gram–Schmidt from an actual difficulty

Choose a target the model cannot meet exactly or observations that disagree.
Compute xhat, p, and e; verify `A^T e=0`. Name the error metric and units.
State the independent-column condition before using inverse normal equations.
Distinguish a subspace projection from a constrained physical fit.

- Light: fit an unavailable response with the declared source columns.
- Shadows: average conflicting Y observations from two screens under equal weights.

Use actual independent columns/rows to work Gram–Schmidt; the resulting signed
orthonormal directions need not be literal physical actions.

**Deliverable:** Checked fit, residual, assumptions, an explicit projector when
useful, and an actual Gram–Schmidt computation or a derived orthonormal case.

## 8. Separate same-space eigenstructure from input/output SVD

Provide a square transformation whose eigen-directions have a concrete meaning.
Then decompose the recurring rectangular or rank-deficient observation map.

- Light: band filter eigen-directions versus sensor singular input/output modes.
- Shadows: rotations/projectors versus stacked-view singular modes.

State full, compact, and truncated shapes. Verify singular pairs, null completions,
repeated-value freedom, and approximation loss. Use symmetric Gram matrices for
the spectral theorem; do not claim every transformation diagonalizes.

**Deliverable:** Checked eigenpairs and singular pairs, shapes, one truncation/error
example, and a clear reason these are different mathematical questions.

## 9. Build the statistics/PCA bridge from repeated declared records

Specify what a row and a column mean. Center the data, compute mean, sample or
population variance, standard deviation and covariance, then connect covariance
eigenvectors with the centered data's right singular vectors. State scaling,
normalization, signs, ties, reconstruction, and restoring the mean.

**Deliverable:** A small checked dataset and interpretation. Do not call dominant
variation causal, best, physically feasible, or uniquely identifying by default.
For the recommendation lecture, introduce a separate rating table explicitly;
missing values are not zeros and ordinary SVD alone is not a validated predictor.

## 10. Write mechanism cards and cover the course at two resolutions

Give each physical action/observation a stable card ID, its mathematical job,
callback, and boundary. Provide both:

1. A chapter route for Weeks 1–5 plus the statistics/PCA supplement.
2. A **36-row local mechanism index** linked by topic ID to the sole source-page
   register in `course-map.md`, with the mathematical landing required locally.

Maintain exact source pages only in the course map. Local tables are mechanism
indexes, not independent page registers. A source map is not a completed derivation
or manuscript passage.

## 11. Make the teaching concrete before evaluating it

Write a sample opening and checked ordinary mathematical questions for each weekly
chapter plus the supplement. Include answers, a verification step, and diagnostic
feedback about likely mistakes. Mark reused anchors separately from a future
fresh transfer bank.

**Deliverable:** At least six worked transfer anchors, a diagram brief, and a
clear path from mechanism to formal reasoning without requiring domain vocabulary
in the student's eventual exam answer.

## 12. Connect the graph through mathematics

Build a connected graph whose edges explain why one action motivates the next.
Provide an accessible prose route. Connect lenses through shared topic IDs and
relationships such as `A(x+v)=Ax`, not by declaring different physical objects equal.

**Deliverable:** Connected Mermaid graph, explanatory text, and cross-lens callbacks.
Check reachability structurally; report rendering and semantic review separately.

## 13. Build a separate, domain-specific rubric

Keep identical weights across lenses for future comparisons:

| Criterion | Weight |
| --- | ---: |
| Domain mechanism specificity | 25 |
| Mathematical fidelity and boundaries | 25 |
| Connected narrative and stable canon | 15 |
| Complete course and manuscript coverage | 15 |
| Teaching, visual explanation, and transfer design | 10 |
| Independent review and learning evidence | 10 |
| **Total** | **100** |

Score each 0–4; contribution is weight × score / 4. Define a 4 with observable
evidence. Add specific rejection tests for plausible misuse of that domain.
A high total cannot waive mathematical errors, absent coverage, or false claims.

**Deliverable:** A separate rubric, review method, evidence/gap ledger, and an
honest assessment. All current rubrics use the same evidence-ledger format. Leave
the weighted total unassigned until formal scoring is completed; record past scores
in history rather than inheriting them into a new artifact or claiming effectiveness.

## 14. Verify the actual artifacts and preserve originals

- Check examples with exact rational arithmetic or explicit normalized identities;
  use numerical tolerances only where appropriate and report them.
- Check every topic ID, source path/page range, graph, local link, rubric weight,
  and any computed score. Check mathematical claims semantically as well as structurally.
- Keep historical originals unchanged in `old/`; record original location and hash.
  Historical relative links can reflect their old locations. The live index must
  point to current canons, not silently treat old documents as current.
- Update the main bible, source map, textbook rubric, and checklist where the
  current status changed. Do not award chapter/learner credit for authoring plans.

**Deliverable:** A concise verification record and explicit remaining work.
Running calculations is not independent review; a graph check is not a rendered
figure; a beautiful analogy is not evidence that the student can solve fresh problems.

## 15. Compare only after making each case concrete

The light/shadow comparison includes each lens's strongest hook, coherent journey,
exam contribution, visual opportunity, strongest objection, and response. It also
specifies matched teaching samples and equivalent fresh transfer problems.

Use that method for any later comparison. Separate editorial judgment from reader
evidence. Do not manufacture a winner from identical rubric weights or assume
a memorable metaphor has improved learning without a transfer check.

## Authoring acceptance checklist

Each pair must contain the scene/source boundary, vocabulary, exact recurring
anchors, unique and nonunique cases, all four spaces, fitting/orthogonality,
eigen/SVD distinction and shapes, statistics/PCA, action cards, six chapter routes,
36 local mechanism entries linked to the source register, six answered transfer anchors, diagram brief, connected
graph/prose, cross-lens links, and its own rubric with explicit evidence gaps.
Unrendered figures and absent learner trials remain open, not quietly completed.

Development sequence and prior assessment differences are recorded in
[history](verification/history.md).
