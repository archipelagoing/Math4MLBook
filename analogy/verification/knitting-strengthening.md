# Craft-centered teaching — verification record

2026-10-26 · [Teaching strategy](../teaching-strategy.md)
[Knitting/crochet canon](../systems/knitting-crochet/canon.md)
[Count schematic](../systems/knitting-crochet/figures/repeat-panel.svg)

## What changed

Knitting/crochet now leads the mathematical explanations in all five weeks and the
statistics/PCA supplement. Shadows/light are optional targeted support. The same
24-stitch sampler gains a marked color panel; the crochet motif gains six sectors.
The added constructions extend the craft to geometry, eigen-directions, SVD and
PCA without pretending every abstract direction is a literal stitch.

All 36 topic routes in the strategy, craft canon and six-system source map now
identify a craft-led explanation. Exact lecture pages remain only in the central
source register. Old snapshots and the other five canons were not rewritten.

## Exact mathematical checks performed

Standard-library rational arithmetic, matrix products, dot products, and a small
exact determinant calculation checked:

- Four-row panel: 24 stitches per row, 8 pink/16 green, 32 pink/64 green overall;
  each entry of W is a pink count within six stitches.
- `W=2e e^T+a a^T`; equal row totals and the total-report null difference;
  uniform/alternating orthogonality; normalized versus unnormalized basis coordinates.
- Projection of `(3,1,3,1)` to uniform repeats, its residual and squared error 4;
  Gram–Schmidt baseline subtraction and normalization.
- W singular pairs/complete null basis; nonzero singular values 8,4; full/compact
  dimensions; rank-1 approximation and squared Frobenius loss 16.
- Column centering to X, sample covariance `(4/3)a a^T`, leading eigenvalue 16/3,
  section variances 4/3 and the 100% designed variance fraction. Raw baseline
  strength and centered alternating variation remain distinct.
- Crochet sector accounting: three plain sc plus an increase consumes 4/produces 5;
  two plain sc plus a decrease consumes 4/produces 3. Alternating three of each
  consumes/produces 24 overall.
- P6 cyclic action, inverse-transpose identity, sixth power identity, determinant −1,
  trace 0, uniform eigenvalue +1 and alternating eigenvalue −1.

The record-space and feasibility boundaries were reviewed during authoring:
negative contrasts are not negative yarn; eigenvectors of a relabeling do not mean
new fabric; W input/row roles differ; an executable rank-1 chart here does not make
generic SVD approximations knit-ready. This is author verification, not independent review.

## Document and schematic checks

- Strategy and canon have matching 36-topic destinations; six answered chapter
  anchors remain present. Topic links resolve to the source register.
- The new SVG is valid XML. Each of its two panels contains 96 schematic stitch
  cells, including 32 pink and 64 green. Diagram numerics match W and its uniform
  approximation; no image-render or visual/craft inspection was performed.
- Current local links and graph reachability pass structural checks.
- All six rubric totals remain unassigned with identical weights; the knitting
  rubric adds explicit craft-centrality, chart-encoding and centered-PCA rejection tests.
- All ten files in old/ match the pre-cleanup hashes; no archived bytes changed.

## What has not been established

No physical knitting/crochet sample was worked. No calibrated gauge dataset,
loop-accurate technique diagram, finished chapter, independent domain/math review,
rendered accessibility/print inspection, or learner trial is claimed. The SVG is
a labeled record schematic, not a tested pattern or proof of physical loop topology.

Craft review should verify working-direction/chart conventions and practical stitch
placement. Mathematical review and fresh formal problems should test whether these
representations improve method selection and independent reasoning. The aim remains
preparation for an A; no grade or comparative effectiveness has been demonstrated.
