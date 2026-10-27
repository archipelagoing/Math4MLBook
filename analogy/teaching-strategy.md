# Mathematics, in view — shadows as the teaching backbone

[Analogy index](README.md) · [Shadow canon](systems/shadows/canon.md) ·
[Source/topic register](course-map.md) · [Authoring method](build-method.md)

The owner selected **shadows: reconstructing a point from measurements** as the
primary analogy, replacing knitting/crochet. Preserve the four-page lecture limit
and the show bible's numbered teaching structure. The previous
[craft strategy](verification/knitting-teaching-strategy.md) remains historical.
Colored light and the other systems remain optional references, not competing
stories to repeat in every section.

## 1. One scene, explicit records

Use matched labeled points on an open frame, ideal parallel-ray views, fixed
calibrated axes, and a declared common reference origin. A front view records X,Y;
a side view records Y,Z. Moving a point only in Z changes the point while leaving
its front mark unchanged. Adding a side measurement reveals the missing coordinate.

The recurring question is: **what does this particular record let us distinguish?**

| Record | Meaning | Boundary |
| --- | --- | --- |
| p=(X,Y,Z) in R3 | One point's world coordinates | Not a whole object or a silhouette |
| Op=(X,Y) in R2 | Its front-screen coordinates | Depth is absent |
| r=(X_A,X_B,X_C,X_D) in R4 | Four labeled beads' horizontal readings | Four entries do not create four physical spatial axes |
| W, configurations by beads | Repeated horizontal profiles | Not a screen image or a physical rigid-motion operator |

For the classroom profile examples, the beads have fixed Y=1,2,3,4. Use
r=(3,1,3,1), s=(1,3,1,3), e=(1,1,1,1), a=(1,-1,1,-1).
Then r=2e+a and s=2e-a. Uniform and alternating **displacement records** supply
combinations and geometry; they do not claim that an origin translation is linear.
Negative/fractional coordinates are valid. Remove the former stitch-count
integrality/nonnegativity rules rather than carrying them into the new analogy.

## 2. The connected course route

Exact lecture pages remain in the [course map](course-map.md); the canon owns the
matrices and mechanism boundaries. Week 2 systems, determinants and inverses now have a written chapter; later routes remain plans.

| Course unit | Scene and mathematical purpose |
| --- | --- |
| Week 1 | Locate a point; distinguish world, screen, and multi-point records; add displacement profiles; compute dot products/norms/angles; organize observations; apply O and stacked H; interpret product columns/rows and order. |
| Week 2 | Reconstruct point coordinates from matched views. Use augmented equations, elimination, and consistency; reserve determinants and two-sided inverses for square maps. |
| Week 3 | Characterize invisible input motions and incompatible output records. Compare independent views with repeated measurements; distinguish coordinate changes from observation loss. |
| Week 4 | Reconcile noisy views with projections and least squares; separate the 2-by-3 view O from a 3-by-3 world-space projector and a measurement-space projector. Build orthonormal directions explicitly. |
| Week 5 | Rotate a point/frame using a declared same-space map; study eigen-directions separately from rectangular view SVD; show strong, weak, and invisible directions and approximation. |
| Statistics/PCA bridge | Compare point-coordinate or profile datasets with declared row/column roles; center, compute covariance, project and reconstruct. PCA does not recover missing depth without observations/assumptions. |

A separate recommendation-rating example must identify its new dataset. Ratings
are not coordinates and missing entries are not zero. Do not force that application
into a physical shadow claim.

## 3. Preserve the teaching architecture

Every section follows **question → definition → reasoning/figure → worked example
→ checkpoint → takeaway and independent practice**. A compelling image does not
replace the formulas or proofs. Preserve every distinct lecture example, including
examples with no analogy. Keep four website pages maximum per lecture, including
exercises and solutions; use numbered sections within them.

For Lecture 1, the topic route is:

- Sections 1.1–1.6: coordinates, displacement arithmetic, profile combinations,
  dot products, norms/unit directions, and angles in the declared record space.
- Sections 1.7–1.12: configuration-by-point matrices, special structures,
  entrywise arithmetic, transpose/trace, view maps, matrix products/properties.
- Integrated practice/solutions: 24 formal questions with fresh variants, diagnostic feedback,
  and links back to the method. Problems 1, 15, 16, and 19 now use the point scene.

The four generated SVGs show hidden depth, labeled point profiles, record-space
geometry, and the O view map. Their numbers must agree with prose and solutions.
Keep the approved palette; pink/green identify cases, red identifies warnings,
and yellow highlights important conclusions.

## 4. Nonnegotiable boundaries

- Use matched point coordinates, not reconstruction of arbitrary solid objects
  from silhouettes, occlusion, unknown correspondences, or perspective images.
- Declare input/output spaces and origins. Perspective division and origin changes
  are not silently linear maps.
- A dot product/norm/angle of a four-entry profile belongs to that record geometry;
  it need not be the physical frame's orientation or complete 3D displacement.
- O loses Z. A later coordinate sum J of four X values loses a different distinction.
  Always name which map hides which changes.
- More readings need not mean more independent information. Repeated Y in H is
  a visible example of the distinction.
- No physical experiment, independent domain review, or improved student performance
  is claimed from constructed examples and local rendering checks.

## 5. Current implementation

[Lecture 1](../book/lecture1/index.md) and its
[matrices page](../book/lecture1/matrix-guide.md) implement this scene;
[exercises](../book/lecture1/practice.md) and [solutions](../book/lecture1/solutions.md)
use consistent records. [The review](../authoring/lecture1-review.md) records
verification. Later-week mechanisms remain plans until their chapters are written.

## Lecture 2 implementation

[Systems](../book/lecture2/index.md) and [elimination](../book/lecture2/elimination.md)
use O and H to connect prediction to reconstruction, exact consistency, redundancy,
and missing-coordinate freedom. Matched readings must agree on Y. Row operations
rewrite constraints without changing the point; they do not create new observations.
The 26 exercises include symbolic consistency of front (a,b), side (c,d): a unique
point (a,b,d) exactly when b=c. Determinants/inverses are now included for declared square maps.

The full-deck chapter explicitly distinguishes rectangular views O/H from the
square screen-coordinate mixing map C=[2,1;1,1]. Det(C)=1 preserves screen area;
C inverse undoes that mixing. It cannot recover the depth removed by O. Parts
A–N preserve slide order; the TL;DR page supports subsequent exam review.

**Numbered topic navigation:** Both lectures now have three consecutive topic
pages followed by a TL;DR page. Lecture 1 separates dot products/geometry from
vectors/combinations; Lecture 2 separates determinants/geometry from inverses.
Practice and expandable answers follow the relevant topic. See `AGENTS.md` and
the current show-bible contract before extending this route.

## Lecture 3 implementation

[Spaces](../book/lecture3/index.md), [complete solutions/rank](../book/lecture3/solutions-rank.md),
and [basis/coordinates](../book/lecture3/basis.md) now develop the whole Week 3 deck.
O's hidden Z direction is N(O), its row space is the XY input plane and every
front pair is attainable. H has no hidden input direction but has the output
condition b2=b3 and left-null direction (0,1,−1,0). Matched views distinguish
input freedom from output compatibility without claiming arbitrary solid reconstruction.

The page-34 basis matrix B=[3,1;1,1] is a coordinate-description change on a fixed
front screen: (3/2,1/2) coefficients represent the same (5,2) screen vector. It does
not move the point or restore lost depth. Formal course matrices remain explicitly
separate examples. The chapter includes fresh practice and a mixed rehearsal;
[source coverage](../authoring/lecture3-coverage.md) records corrections and limits.
