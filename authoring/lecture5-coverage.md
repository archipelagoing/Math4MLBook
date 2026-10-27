# Lecture 5 · Complete source and practice map

Date: 2026-10-27. Source: Erisa Terolli’s CS 556
`resources/lectures/WK5_Matrix_Decomposition.pdf`, **44 PDF pages**.
All extracted pages and all 44 rendered pages were inspected. Visual inspection
controls matrix/vector order; text extraction scrambles several entries and
entirely omits the handwritten example on page 22.

## Slide-to-textbook map

| PDF pages | Retained substance | Destination |
| --- | --- | --- |
| 1–2 | Title and outline: eigen decomposition, SVD, reduction, movie recommendations | Chapter opener and four numbered pages |
| 3–5 | [2,−1;1,2](2,3)=(1,8); rotated/stretched vector; standard Rθ and αI maps | A, Example 5.1, transformed-vectors figure |
| 6–8 | [2,1;2,3](1,2)=(4,8)=4(1,2); eigenvalue/eigenvector labels | A, Example 5.2, second figure panel |
| 9 | Av=w versus Av=λv, preserved one-dimensional span | B definition, including reversal and zero-eigenvalue clarifications |
| 10–12 | Unit square, diag(1,2) stretch, axis directions and diagonal non-example | B, Example 5.3 Step 1, stretch/rotation redraw |
| 13–15 | Rotated-square graphic, “0 Eigenvectors”, check same span and magnitude | B, Example 5.3 Step 2; explicit 45° representative and no-real-eigenvector meaning |
| 16 | Av−λv=0 → (A−λI)v=0; nontrivial null space; singular shifted matrix; det=0; handwritten N(A−λI), invertible/trivial-null observation | C recipe, zero exclusion and invertible-shift explanation |
| 17 | First find roots, then find vectors in each shifted null space | C recipe and checkpoint |
| 18 | Full diag(1,2) determinant/null-space worked example and stretched-square picture | C, Example 5.4 and earlier self-contained redraw |
| 19 | Eigendecomposition: square map, eigenvectors and associated eigenvalues | D definition and matched column/root convention |
| 20 | AV=VΛ, V⁻¹AV=Λ, A=VΛV⁻¹; independent eigenvectors; coordinate-change interpretation; handwritten independence and orthonormality notes | D, Example 5.5, failure Example 5.6; general independence distinguished from symmetric orthonormal choice |
| 21 | Real symmetric spectral theorem, real roots, Q inverse=transpose; distinct-root perpendicularity proof and margin observation | E theorem/proof and repeated-root caveat |
| 22 | Handwritten S=[3,1;1,3]: positive definite? orthogonal or orthonormal? λ=4,2, eigenvectors (1,1), (−1,1), length √2; homogeneous reductions | E, Example 5.7, complete determinant/null-space/unit-vector/reconstruction work |
| 23–24 | SVD title; A=UΣVᵀ; full m×n factor dimensions and row/column basis picture | F definition, factor-shapes figure, four-space table |
| 25 | Circle→ellipse; orthonormal right/left directions; Avᵢ=σᵢuᵢ; nonnegative ordered strengths; r=rank; AV=UΣ | F, circle/ellipse figure, full/compact distinction and Example 5.8 |
| 26 | Gram derivations; eigenvectors of AᵀA/AAᵀ; square roots of Gram eigenvalues; handwritten square/symmetric and orthogonality annotations | G derivation, computation recipe, Example 5.9; rectangular products retained rather than dimensionally ambiguous Σ² |
| 27–31 | Reduction title and progressive exact rank-r blocks, sizes m×r,r×r,r×n | H definition and truncation diagram |
| 32–33 | Leading k blocks, all factor dimensions; Rₖ=UₖΣₖVₖᵀ; Eckart–Young 1936 closest-rank statement | H theorem with norms/at-most-k convention, Example 5.11, discarded-error recipe |
| 34–35 | Movie title; John/Tom/Alice ratings with observed 5,1,3,5 / ?,?,?,2 / 4,?,3,?; Argo/Seven/Righteous Kill/Heat posters | I first complete readable table, movie names and missing-data convention |
| 36–37 | Overfit/product-level taste representation, computational burden, higher-level shared tastes; Harry Potter/Fantastic Beasts motivation, compact/robust goal | I motivation and limits, original feature-flow diagram |
| 38 | Rating/factor dimensions; user affinities, item relevance, diagonal weights; exists-for-any-real-matrix assertion | I model definition; exact numerical SVD versus truncated/learned model distinction |
| 39 | All displayed ratings and all named-genre user/movie/weight entries, including final User m | I complete Markdown tables; every number retained |
| 40 | Highlight User 1 / Captain America; weighted row product; Fantasy feature changes 0.2→0.9 | I, Example 5.12; both versions recorded and checked, unchanged score 0.0249 |
| 41–42 | Source reference and closing | Source notes; reference recorded below |
| 43 | Final eigenproblem [3,1;4,6] | J, Example 5.13, λ=7,2 and complete eigenspaces/checks |
| 44 | Final SVD problem [4,0;3,−5] | J, Example 5.14, Gram eigenvalues 40,10, paired factors and exact reconstruction |

The source’s Eckart–Young reference is
`https://citeseer.ist.psu.edu/viewdoc/download;jsessionid=6B65A9A35513A03050594C88798801DB?doi=10.1.1.23.1831&rep=rep1&type=pdf`.
This is a recorded source citation, not a claim to have fetched that external PDF.
The source’s movie picture credits Di Noia and Ostuni (2015), chapter DOI
10.1007/978-3-319-21768-0_4. Poster art is replaced by readable names and original
diagrams; no student needs to open the source picture to interpret its ratings.

## Precision corrections and editorial additions

- Matrix/vector order follows rendered pages. In particular, the first product
  is (2,3)→(1,8), the eigen-example is (1,2)→(4,8), and the final matrices are
  [3,1;4,6] and [4,0;3,−5]. Extraction suggests incorrect alternatives.
- An eigenvector is nonzero; a zero eigenvalue is allowed. “Same direction” means
  same span, including reversal or collapse. Rotation’s “0 Eigenvectors” means
  no real eigenvectors; the unlabeled rotated-square diagram is made explicit
  with an editorial 45° rotation. Each eigendirection contains infinitely many
  nonzero multiples, not just one eigenvector.
- Use A−λI, not a matrix minus an unspecified scalar. Diagonalization requires
  independent eigenvectors; they need not be orthogonal or unit. A repeated root
  may succeed or fail depending on eigenspace dimension (new defective countercase).
- Symmetric distinct-eigenvalue vectors are perpendicular; arbitrary vectors in
  one repeated eigenspace need not be. The theorem permits an orthonormal choice.
  The supplied proof establishes distinct-root perpendicularity, not the entire
  existence theorem; this boundary is stated explicitly.
- Full U/V span the ambient spaces. Only their first r columns span column/row
  spaces. Compact V has no two-sided inverse. Positive singular values end at r;
  full/reduced forms can also retain zeros. Gram products are ΣᵀΣ and ΣΣᵀ for
  rectangular full Σ, and zero singular values never enter a division.
- Eckart–Young needs a norm and rank convention; the book states both Frobenius
  and spectral errors, rank at most k, tied-cutoff behavior, and k=0/r endpoints.
- The source’s genre factors are illustrative, not a verified literal SVD:
  User 1 / Notebook reconstructs as 0.28 rather than rating 5. User 1 / Captain
  America gives raw score 0.0249, not a calibrated rating. The 0.2→0.9 change has
  no effect because the user’s corresponding entry is zero. No missing entry is
  imputed as zero, and existence of SVD does not imply validated missing prediction.
- Positive definiteness/semidefiniteness, complete eigenspace conventions, powers,
  exact SVD/Gram checks, truncation errors, record-coordinate maps, storage counts,
  the observed-entry objective and fresh mixed practice develop the source’s ideas
  for independent study; they are editorial additions, not new source examples.

## Four pages and assessment blueprint

| Reader page | Source-order parts | Practice / examples |
| --- | --- | --- |
| 1 · Eigenvalues & diagonalization | A–E, PDF 1–22 | Examples 5.1–5.7; Problems 1–10 |
| 2 · Singular value decomposition | F–G, PDF 23–26 | Examples 5.8–5.10; Problems 11–18 |
| 3 · Reduction & recommendations | H–J, PDF 27–44 | Examples 5.11–5.14; Problems 19–24, fresh mixed 25–28 |
| 4 · TL;DR cheat sheet | Review | Conditions, selection cues, two stepwise recipes, Example 5.15 |

Ten part-level goals/source ranges/checkpoints/takeaways, 15 highlighted worked
examples, six reproducible labeled SVGs, 28 questions with nearby explained
answers and specific diagnosis/revision/retry links. Regular practice decreases
scaffolding; the four mixed questions do not name the method or give hints.
The editorial 25-minute/16-point rehearsal and 14/16 target are not official exam
rules or evidence of an actual student grade. Banks remain included fragments.

## Supporting sources and remaining gaps

| Resource | Verified alignment | Destination |
| --- | --- | --- |
| Linear_Algebra_Worksheet-1.pdf, Problem 13, p.4 | A=[1,4;2,3], A+I; eigenvalue shift and unchanged eigenspaces | Practice 5, complete checked solution |
| Same worksheet, Problem 14, p.4 | A=[3,0;4,5], full SVD | Example 5.9 and Example 5.11 truncation |
| MidtermTopics.md | Eigenvalues/eigenvectors, SVD, orthogonal/symmetric special matrices; prior prerequisites | A–J, method selector, independent variants and mixed check |

Worksheet p.4 was visually inspected during Lecture 4 and rechecked against its
extracted data. No comprehensive practice-exam question audit is claimed here.
Statistics (mean/variance/standard deviation/covariance) and PCA are **not taught
in this deck**: their separate labeled supplement and cumulative exam blueprint
remain open. Matrix energy percentages are not described as centered variance.
