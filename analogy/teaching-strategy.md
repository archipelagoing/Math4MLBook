# Stitch by Stitch — Knitting and Crochet as the Teaching Backbone

2026-10-26 · Implementation plan; textbook chapters are not yet rewritten
[Current index](README.md) · [Craft canon](systems/knitting-crochet/canon.md)
[Source/topic register](course-map.md) · [Authoring method](build-method.md)

## 1. Make the craft do the mathematical teaching

Knitting and crochet lead the questions, explanations, diagrams, worked examples,
and chapter-to-chapter connections. They are the mathematical backbone as well as
the book's identity. Shadows and colored light remain optional supporting views
when they solve a specific learning problem; they do not take over the formal
exposition in the later weeks.

The key improvement is to develop several faithful records of the **same made
projects**, instead of stretching one aggregate stitch-count ledger to cover
every concept. A repeat has spatial structure. A marked round has coordinates.
A chart can have separable patterns. A swatch has measured gauge. These give the
craft enough mathematical range for the whole course.

The recurring question is:

> What can we make, what does this record retain, and what changes when we change the repeat?

Every analogy still lands in precise mathematics, with hypotheses, derivations,
checked calculations, countercases, and fresh formal exam problems. The aim is
the student's independent performance, not simply an appealing craft narrative.

## 2. Stay with two recognizable projects

### The knitted sampler

Cast on 24 stitches. Introduce knit/purl repeats and shaping. Add a four-row color
panel divided by markers into four six-stitch sections. Pink counts per section
alternate between `(3,1,3,1)` and `(1,3,1,3)`; remaining stitches are green.

This one panel supports vectors, a genuine data matrix, repeated columns, pattern
bases, projection to a uniform repeat, Gram–Schmidt, singular modes, approximation,
and centered PCA. A count cell summarizes six actual stitches; it is not a color
intensity or one chart square. A separate stitch-level chart controls placement.

### The crocheted motif

Start with 6 sc in a magic ring; use the specified increase rounds to reach 24.
Mark six sectors. Compare four plain stitches with increase/decrease shaping,
then shift which sector is recorded first. The same round supports initialization,
count constraints, change of recorded coordinates, a cyclic permutation, and
explicit eigen-directions. Circle shape alone is never the mathematical proof.

Use US terms and the exact conventions in the [craft canon](systems/knitting-crochet/canon.md).
The examples are count-checked teaching constructions, not physically tested
patterns. Knitting and crochet share count structures here, not identical fabrics.

## 3. The craft constructions that make the later chapters stronger

### Pattern geometry inside a swatch

For `r=(3,1,3,1)`, define `e=(1,1,1,1)` and `a=(1,-1,1,-1)`.
Then `r=2e+a`: a uniform baseline of two pink stitches per section plus an
alternating one-extra/one-fewer contrast. The vectors e,a are perpendicular in
the declared equal-section count metric. Signed a describes change from a
baseline, not negative yarn.

In normalized coordinates `q0=e/2`, `q1=a/2`, r is `(4,2)`. Plotting those two
coordinates gives an exact two-dimensional picture of this swatch-record subspace.
The projection to uniform repeats is `(4,0)` in that plot, or `(2,2,2,2)` in the
original section coordinates. We can teach geometric projection while staying
with the actual craft record rather than switching to a bead-and-screen story.

### Decomposition of the actual count chart

The four-row panel record W has alternating rows r and `2e-a`:

```text
W=[[3,1,3,1],
   [1,3,1,3],
   [3,1,3,1],
   [1,3,1,3]]
```

It decomposes as `W=2e e^T+a a^T`, with nonzero singular values 8 and 4.
Keeping just the first term makes every section contain two pink stitches and
removes the alternating pattern; squared Frobenius record error is 16.
The sections/rows provide input/output meanings. This is a decomposition of a
made-pattern record, not a claim that needles physically execute SVD.

Centering the same records removes the uniform term. The centered X has one
nonzero singular value, 4, and its covariance has leading eigenvalue 16/3.
The dominant raw mode is baseline; the dominant centered mode is alternation.
This distinction makes PCA teachable on the same swatch. Its related pattern rows
are not an independent experiment; the separate GAUGE dataset covers specimen
measurements and two nonzero variation directions.

### Eigen-directions in a marked crochet round

After appropriate within-sector shaping, use six recorded counts `(5,3,5,3,5,3)`.
Changing the recorded starting sector is a cyclic permutation P6. Its uniform
record direction has eigenvalue +1; its signed alternating direction has eigenvalue
−1 because its phase reverses. Neither statement requires negative stitches or
physical movement of the made fabric. The remaining modes prevent a complete
real eigenbasis; the formal field/diagonalization conditions still matter.

These anchors are developed and checked in the canon. They replace the idea that
advanced topics must be taught primarily through a separate domain.

## 4. Assign the supporting lenses a narrower role

| Lens | Role in the manuscript | Trigger for using it |
| --- | --- | --- |
| Knitting/crochet | Default explanation and substantial worked examples in every chapter | Always begin with the relevant stitch, section, round, chart, or gauge record. |
| Shadows | Optional geometric illustration or rescue explanation | The reader cannot yet interpret projection, an invisible direction, or an independent measurement after the craft example and definition. |
| Colored light | Optional short comparison about observation limits | A second concrete instance helps the reader separate physical input from a reduced record; introduce it after the yarn mathematics is understood. |
| Other canons | Alternative reference material | A specific learner benefits from a different domain; they are not required parallel textbook stories. |

Prefer a diagram of the craft record's own coordinate geometry before importing
another narrative. A supporting lens earns space by resolving a named misconception,
not by being ranked highly in a general-purpose comparison. Do not repeat three
full explanations per concept.

## 5. A section pattern that keeps yarn central

1. Show a specific craft action or observation and ask a mathematical question.
2. Label the record: entries, order, units, space, what it retains, and what it omits.
3. Give the exact definition/result and hypotheses in ordinary mathematical notation.
4. Work the craft-derived computation with method choice, reasoning, and verification.
5. Expose a countercase or physical limit without turning the whole explanation into caveats.
6. Ask a short understanding check on the same object and representation.
7. Add a supporting visual comparison only if the check exposes a conceptual gap.
8. Require a fresh formal problem with no craft vocabulary needed in the answer.
9. Diagnose the error and provide a targeted retry, then connect the next craft question.

A physical analogy need not be a literal operation at every stage. A signed pattern
contrast, a weighted count, or a record-space direction is legitimate when the
abstraction is named and grounded in the actual swatch. Inventing a fake stitch
for it would weaken the explanation.

## 6. Chapter-by-chapter plan

### Week 1 — From loops and repeats to vectors and matrices

Work actual knit/purl and sc sequences. Introduce whole-row counts, four-section
records, the panel matrix W, and the consumed/produced operation ledger. Compare
what each representation retains. Use row records for addition/scaling, dot
products, norms and unit directions, with the metric declared.

Matrix transpose swaps recorded row/section roles; it does not magically turn
fabric inside out. Compare compatible maps, identity, diagonal scaling, a symmetric
Gram map, trace, and the rectangular ledger H. A color chart and a numeric map
are not interchangeable without defining the encoding and operation.

**Exam skill:** Read dimensions, compute correctly, justify compatibility, and
interpret a result in the right space. A shadow diagram is optional support, not
the chapter's main example.

### Week 2 — Shape the next row or round

Derive `p+i=24`, `p+2i=30` from plain stitches and increases. Solve, then place
`(k3,kfb)` or `(3 sc,inc)` six times and verify consumed/produced counts.
Introduce decreases to create redundancy and parameter choices. Develop the
lecture's augmented systems, row operations, pivots, echelon forms and back substitution.

Use square B and a declared bookkeeping coordinate map for determinant properties,
cofactor expansion, Gauss–Jordan and inverses. Compare them with singular A.
Count-map area/volume is in coordinate space, not automatically fabric area.
Binding off is an edge-finishing/checking action, not the inverse of casting on.

**Exam skill:** Solve/classify systems, handle row swaps and missing pivots,
justify inverse conditions, and distinguish algebraic solutions from executable counts.

### Week 3 — Repeats, freedom, and invisible differences

Start with two different color rows that both contain eight pink stitches. Whole-row
totals lose their alternation; section records preserve it. Then use the operation
ledger's increase/decrease substitution to derive its null space and complete
solution family. Specify the map before asking what is invisible.

Work all four spaces with explicit input/output meanings. Derive rank, dependence,
span, basis, dimension and feasible constraints. Use e,a as a basis of the selected
repeat subspace, compare normalized/unnormalized coordinates, and use the existing
plain/increase versus plain/decrease bookkeeping bases where appropriate.

**Exam skill:** Compute the four spaces and full solution, distinguish rank from
number of written measurements, and separate invertible coordinate change from
lost information. Light may add a brief comparison after this is established.

### Week 4 — Find the nearest repeat and fit gauge

Ask for the closest uniform four-section record to `(3,1,3,1)`. Derive p=2e,
residual a and orthogonality. Gram–Schmidt on e,r discovers uniform/alternating
coordinates. Draw the two-dimensional q0/q1 geometry of this very record.

Then work the inconsistent ledger report as a different error-model choice, and
use gauge measurements for least-squares line fitting. Preserve the lecture's
normal-equation derivation, full-column-rank hypothesis, projector conditions,
orthonormal basis formulas and computational practice.

**Exam skill:** Derive and verify projections, choose the correct subspace/metric,
compute an orthonormal basis, and recognize when the inverse formula is invalid.
A supporting shadow sketch may help visualize the already derived craft geometry.

### Week 5 — Read the structure hidden in the pattern

Relabel six marked crochet sectors and derive P6's real uniform/alternating
eigen-directions. Explain the field and diagonalization limits, with formal
counterexamples and the symmetric spectral theorem applied to a Gram map.

Decompose W into baseline and alternation, derive its singular pairs and full/
compact/truncated shapes, reconstruct and quantify discarded structure. Use the
existing 2-by-3 operation ledger H for a genuinely rectangular SVD. Keep row and
section roles distinct even when singular-vector coordinates happen to match.

For recommendation, declare maker-by-named-swatch ratings separately and teach
the lecture's actual user-rating example and missing-data limits. Ratings are not
loops, gauge, or section counts.

**Exam skill:** Select eigen versus singular-value reasoning, verify pairs and
shapes, handle zero/tied/defective cases, and interpret approximation accurately.

### Exam-topic supplement — What changes across rows and across swatches?

First center W: baseline disappears and alternating variation remains. Contrast
raw SVD strength with centered PCA variance. Explain why related designed rows
are not an independent random sample and what the covariance calculation does mean.

Then use GAUGE's explicitly invented specimen table for mean, sample/population
variance, standard deviation, covariance and two-direction PCA. State scaling,
center columns, connect covariance eigenvalues with centered singular values,
project/reconstruct and restore the mean. The supplement is required by the
exam-topic list; source attribution stays with the central register.

**Exam skill:** Compute statistics and PCA correctly, distinguish mean structure
from variation, and explain what the data do not establish.

## 7. A transition that stays inside the craft

Begin with the color rows `r1=(3,1,3,1)` and `r2=(1,3,1,3)`.
The total-count map `Jtotal=[1,1,1,1]` returns 8 for both. Their difference
`r2-r1=(-2,2,-2,2)` is a nonzero vector in N(Jtotal).

Now record each section separately: the difference is visible. The made rows
have not changed; the information retained by the record has changed. Later,
W's section-weighting null space asks a different question about repeated columns.
Do not confuse these two maps merely because they refer to the same panel.

State the general result: `Av=0` implies `A(x+v)=Ax`. Return to the operation
ledger to find its different null direction `(-3,1,1)`. The same mathematical
relationship links both craft situations without equating a color contrast with
an increase/decrease operation.

Then remove the craft vocabulary. For `N=[[1,0,1],[0,1,1]]`, solve `Nx=(3,4)`.
The complete real solution is `(3-t,4-t,t)`, with null direction `(-1,-1,1)`.
A student reporting only t=0 found a particular solution; return to the unnoticed
change, then require a fresh formal retry. Add a shadow/light comparison only
if that conceptual obstacle remains.

## 8. Topic-level allocation

Every main topic now has a craft lead. The topic IDs link to the sole source-page
register; the canon owns exact constructions and limits. Supporting lenses are
optional teaching aids, not replacements for the listed craft explanation.

| Topic | Main craft explanation | Boundary or optional support |
| --- | --- | --- |
| [W1.01](course-map.md#w1-01) | SWATCH/COUNT: Record pink stitches in four fixed six-stitch sections; distinguish stitch order, whole-row totals and section vectors. | A shadow is an optional coordinate picture after the craft record is defined. |
| [W1.02](course-map.md#w1-02) | SWATCH/LEDGER: Add repeated section records and actual plain/increase/decrease effects; state real signed extensions. | Use formal vector arithmetic directly; no second domain is required. |
| [W1.03](course-map.md#w1-03) | SWATCH/REPEAT: Use dot products with uniform/alternating section directions and with the operation-output weights. | Light sensor weighting is an optional application after mastery. |
| [W1.04](course-map.md#w1-04) | SWATCH/REPEAT: Normalize the uniform and alternating count directions; compute record norms, angles and zero-vector limits. | Draw q0/q1 coordinates of the same repeat before using another scene. |
| [W1.05](course-map.md#w1-05) | SWATCH/LEDGER: Read W row/section entries and the rectangular operation map H with declared input/output spaces. | Do not equate count cells with single stitches or color intensity. |
| [W1.06](course-map.md#w1-06) | ROUND/CHARTMODES: Use sector permutation, identity/gain maps and symmetric W transpose W; compute trace in the declared record space. | A shadow rotation is optional for a geometric countercase. |
| [W1.07](course-map.md#w1-07) | CHARTMODES/FIT: Transpose swaps weighted section/row roles; residual pairing uses a transpose without claiming a physical inverse. | No mandatory second lens. |
| [W1.08](course-map.md#w1-08) | ROUND/LEDGER/CHARTMODES: Compose compatible relabeling, shaping-record and reporting maps; check spaces and order before multiplying. | Use an explicit formal noncommuting example if the craft model needs extension. |
| [W2.01](course-map.md#w2-01) | SOLVE: Derive consumed/produced requirements for 24 stitches becoming 30. | Shadows supplies an optional independent application, not the main derivation. |
| [W2.02](course-map.md#w2-02) | SOLVE: Eliminate the actual stitch equations, then develop larger source systems, pivots and back substitution. | Keep lecture computations and method selection explicit. |
| [W2.03](course-map.md#w2-03) | SOLVE/ROUND: Compute determinant/cofactor properties on square B and coordinate permutations; distinguish singular A and coordinate volume. | Shadow geometry can illustrate signed area without redefining fabric area. |
| [W2.04](course-map.md#w2-04) | SOLVE: Invert B or a declared bookkeeping map; distinguish counts recovered from original stitch order. | Do not call binding off an inverse. |
| [W3.01](course-map.md#w3-01) | SWATCH/LEDGER: Separate real repeat/ledger subspaces from physically feasible integer stitch records. | A vector-space counterexample can be formal without leaving the craft scene. |
| [W3.02](course-map.md#w3-02) | SWATCH/LEDGER/CHARTMODES: Contrast total-count invisibility, operation cancellation and repeated W columns; identify the specific map. | Light adds a short second example of invisible input only after this distinction is secure. |
| [W3.03](course-map.md#w3-03) | LEDGER/CHARTMODES: Derive all four spaces with operation/output or section/row-weight meanings and explicit ambient dimensions. | Shadows is a rescue picture if input versus output spaces remain unclear. |
| [W3.04](course-map.md#w3-04) | SOLVE/LEDGER: Give the complete real shaping family and then the finite feasible integer instructions. | Do not confuse a particular worked row with every algebraic solution. |
| [W3.05](course-map.md#w3-05) | LEDGER/CHARTMODES: Repeated pattern columns and redundant ledger totals explain rank and pivot count. | More marks or repeated counts do not necessarily add information. |
| [W3.06](course-map.md#w3-06) | LEDGER/SWATCH: Show increase plus decrease equals three plain ledger effects; repeated motifs produce dependent chart columns. | Physical fabric can differ even when a record is dependent. |
| [W3.07](course-map.md#w3-07) | SWATCH/SOLVE: Test whether a target record is in the repeat/operation span and separately whether counts are feasible. | Light gamut is an optional parallel distinction, not a substitute. |
| [W3.08](course-map.md#w3-08) | SWATCH/REPEAT: Use uniform/alternating repeat directions as a basis of the chosen two-dimensional record subspace. | Do not claim two motifs span every possible four-section row. |
| [W3.09](course-map.md#w3-09) | SWATCH/SOLVE/ROUND: Compare e,a with q0,q1 coordinates, bookkeeping bases and cyclic marker labels. | Keep representation change distinct from making new stitches. |
| [W4.01](course-map.md#w4-01) | REPEAT/LEDGER: Verify uniform and alternating count directions are perpendicular; derive both four-space complement pairs. | Crossed needles are not the argument. |
| [W4.02](course-map.md#w4-02) | REPEAT/FIT: Project r onto uniform repeats and compare with the contradictory-ledger fit under its own metric. | Draw the craft record in its q0/q1 plane; use shadows only if needed. |
| [W4.03](course-map.md#w4-03) | REPEAT/FIT: State independent-column conditions for a chosen repeat basis; contrast the dependent operation ledger. | Do not invert A transpose A for a dependent A. |
| [W4.04](course-map.md#w4-04) | REPEAT/FIT/GAUGE: Fit a closest repeat and a declared gauge trend, retaining the lecture line-fit derivation and assumptions. | Different trusted measurements imply different error models. |
| [W4.05](course-map.md#w4-05) | REPEAT: Use q0=e/2 and q1=a/2; distinguish the uniform-line projector from the two-direction repeat-plane projector. | All directions refer to records, not literal unit stitches. |
| [W4.06](course-map.md#w4-06) | REPEAT: Gram–Schmidt on e,r subtracts the shared baseline and isolates alternating contrast. | This signed residual is not a newly invented craft operation. |
| [W5.01](course-map.md#w5-01) | ROUND: Relabel six marked sectors with an explicit same-space permutation; distinguish a record action from fabrication. | A spatial rotation is optional supporting geometry. |
| [W5.02](course-map.md#w5-02) | ROUND/MODES: Derive +1 uniform and -1 alternating eigen-directions of P6; keep the optional T example and formal characteristic calculations. | Negative eigenvalue changes signed phase, not physical stitch sign. |
| [W5.03](course-map.md#w5-03) | ROUND/CHARTMODES: State P6 real-basis limits, retain formal defective cases and diagonalization hypotheses. | Do not assume every craft-derived matrix has a complete real eigenbasis. |
| [W5.04](course-map.md#w5-04) | CHARTMODES: Apply the real symmetric theorem to W transpose W; separate arbitrary repeated-eigenspace vectors from an orthonormal choice. | Light Gram maps are optional confirmation. |
| [W5.05](course-map.md#w5-05) | CHARTMODES/MODES: Derive W baseline/alternating singular pairs and full/compact shapes; H supplies different rectangular input/output dimensions. | Use a sensor only if the two-space interpretation still needs another example. |
| [W5.06](course-map.md#w5-06) | CHARTMODES/SWATCHPCA: Reconstruct the rank-1 uniform chart, quantify lost alternation, then distinguish centered data compression. | A general real approximation is not automatically a knit-ready chart. |
| [W5.07](course-map.md#w5-07) | GAUGE: Introduce maker-by-named-swatch ratings as a separate dataset; teach the supplied recommendation example and missing-data limits. | Ratings are not loops or section counts. |
| [B.01](course-map.md#b-01) | SWATCHPCA/GAUGE: Compute descriptive statistics on designed panel rows and specimen gauge; distinguish their data-generating interpretations. | Use sample/population conventions and units explicitly. |
| [B.02](course-map.md#b-02) | SWATCHPCA/GAUGE: Center W to isolate alternating variation, then use GAUGE for two nonzero modes and specimen-feature interpretation. | Principal variation is neither baseline strength nor proof of a causal tension mechanism. |

## 9. Visual, notation, and review rules

Make the actual stitches legible: loop paths, old/new stitch tops, marker labels,
row/section coordinates, pink/green counts and gauge units. Pair the full 24-stitch
panel with its 4-by-4 count record; do not draw a count cell as a single stitch.
Show the uniform approximation and alternating residual beside the same panel.
Show the crochet marker relabeling without depicting the fabric as newly worked.

Use warm brown readable text and blue structure. Pink/green are yarn/diagram
labels with text or patterns as well as color; yellow remains important highlights,
red attention. Diagram geometry belongs to the declared count space, not an
unsupported assertion about physical angles, tension or tactile distance.

Keep A (operation ledger), W (panel record), P6 (sector relabeling), and data X
(centered records) distinct. Explain every change of space, units, record granularity,
and physical feasibility. Reuse existing anchors before inventing new ones.

Review a section by asking: which actual action/observation taught the result?
Can the student state the exact mathematics and solve a new exam problem after
leaving the craft scene? A decorative yarn opener followed by a full shadow-led
lesson does not meet this strategy.

## 10. Implementation order and acceptance

1. Complete Week 1 around the sampler/panel, with explicit operation and count diagrams.
2. Build shaping systems and repeat-space reasoning in Weeks 2–3 using the same projects.
3. Develop panel projection and gauge fitting in Week 4; verify all hypotheses and residuals.
4. Develop crochet-sector eigenstructure and panel/ledger SVD in Week 5.
5. Close statistics/PCA, recommendation and cumulative exam coverage with checked practice.
6. Inspect rendered readability/accessibility/print, obtain craft/math review, then
   test fresh unaided mixed problems and revise from the observed mistakes.

This plan and its anchors are mathematical authoring work, not completed textbook
chapters, physically executed sample patterns, or learner validation. No grade is
guaranteed or claimed. The standard remains preparation for an A through complete
coverage, accurate reasoning, method selection, independent practice and verification.
