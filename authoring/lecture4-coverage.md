# Lecture 4 · Source and practice coverage

Date: 2026-10-27. Source: Erisa Terolli’s CS 556
`resources/lectures/WK4_Orthogonality_and_Projections.pdf`, **all 28 PDF pages**.
All extracted pages and all 28 rendered pages were inspected, including matrix
entries, vector coordinates, signs, square roots and the handwritten topic numbers.
No mathematical handwritten additions appear beyond the printed development;
numbering annotations are represented by the ordered textbook parts below.

## Complete slide map

| PDF pages | Retained mathematical content | Textbook destination |
| --- | --- | --- |
| 1–2 | Deck identity and orthogonality title | Page 1 opener, Part A |
| 3 | Zero dot product, Pythagorean norm identity; every-pair definition of orthogonal subspaces | A, Example 4.1, checkpoint, Problems 1–2 |
| 4 | Four-space diagram: input/output spaces, dimensions r,n−r,m−r, right angles, row-space-to-column-space and null-to-zero arrows | B, redrawn four-space diagram, table and proof, Example 4.2, Problems 3–4 |
| 5 | N(A) perpendicular to C(Aᵀ), row-dot-product proof; N(Aᵀ) perpendicular to C(A) | B, proof and checkpoint |
| 6–7 | Projection section title; closest vector in S, line/plane intuition; symmetry and idempotence, Pb | C definition; E line diagram; F subspace proof |
| 8 | b=(1,2,3); z-axis and xy-plane projections p₁=(0,0,3), p₂=(1,2,0); both exact matrices, p₁+p₂=b and P₁+P₂=I; orthogonal complements | C, Example 4.3 and front-view analogy |
| 9 | Inconsistent Ax=b means b outside C(A); solve closest Ax̂=p instead | D, Example 4.4 and repeated-reading diagram |
| 10–11 | Line diagram; p=x̂a, aᵀ(b−p)=0; scalar, vector and matrix formulas with denominator aᵀa | E, derivation and Example 4.5; line-projection diagram |
| 12–13 | Projection onto span of columns a₁,a₂; error perpendicular to both; Aᵀ(b−Ax̂)=0, normal equations, inverse-based coefficient/vector/projector formulas | F, redrawn subspace-projection diagram, dimensional explanation and Example 4.6 |
| 14 | Independent columns imply invertible AᵀA; null-space proof using xᵀAᵀAx=norm(Ax)² | G theorem/proof; dependent countercase Example 4.7 |
| 15–21 | Least-squares title and progressive line-fit reveal: points (1,1),(2,2),(3,2), y=c+mt, original inconsistent system; squared-error objective; AᵀA=[3,6;6,14], Aᵀb=(5,11); equations and c=2/3,m=1/2 | H definition, Example 4.8 Steps 1–5 and line-fit diagram; residual/SSE/verification added |
| 22–23 | Orthonormal-vector title; qᵢᵀqⱼ=δᵢⱼ, column-product interpretation QᵀQ=I; permutation [0,0,1;0,1,0;1,0,0] and rotation [cosθ,−sinθ;sinθ,cosθ] | I definition, Examples 4.9–4.10; square/rectangular warning |
| 24 | Orthonormal-basis reduction of general inverse formulas: ĉ=Qᵀb, P=QQᵀ; Pᵀ=P, P²=P | J formulas/proof, Example 4.11 |
| 25–26 | Gram–Schmidt title; independent inputs; keep first, subtract projections onto previous orthogonal directions; normalize A,B,C | K recipe; both unit and nonunit versions, zero-remainder stopping rule |
| 27 | x=(2,−2,0), y=(4,0,−4), z=(6,−6,6); A=x, B=(2,2,−4), C=(2,2,2); dot products 8,24,−24 and denominators 8,24; all three normalized vectors | K, Example 4.12, four fully worked stages with pairwise/length checks |
| 28 | Closing slide | Source notes and next-lecture connection |

The source’s symbolic line and plane diagrams contain no additional numerical
cases. The book develops their formulas and supplies original reproducible diagrams
and numerical examples. Progressive reveals 16–21 remain one connected worked
example, not six repeated examples.

## Clarifications and editorial additions

- Slide 7’s projection matrix means **orthogonal** projection. A general idempotent
  matrix need not be symmetric; Problem 6 demonstrates the distinction.
- The inverse in slide 13 assumes independent columns, stated explicitly before
  use and proved in source order in G. Normal equations still characterize fits
  with dependent columns; Example 4.7 shows nonunique coefficients/unique output.
- Slide 26 switches from a,b,c to y,z. The general recipe uses aⱼ consistently;
  the numerical source example keeps x,y,z and capital intermediate vectors.
- Source Q₁ is the reversal permutation with middle row (0,1,0), not the cyclic
  permutation suggested by scrambled PDF extraction. The rendered slide controls.
- Line-fitting horizontal coordinate is named t to distinguish it from the vector
  of coefficients. Coordinates/observations and the coefficient order are unchanged.
- Minimality/unique-output proof, complementary projector, exact residuals/SSE,
  failure cases, normalized-coordinate versus physical-coordinate distinction,
  fresh mixed test and the matched-point shadow application are teaching additions.
- Shadow maps O (2×3), embedded OᵀO (3×3), H (4×3) and measurement projector P_H
  (4×4) stay in their declared spaces. Equal Y averaging assumes equal weights.
  No silhouette-reconstruction, statistical-independence or true-position claim.

## Four reader pages and practice blueprint

| Reader page | Parts | Relevant worked/practice destinations |
| --- | --- | --- |
| 1 · Orthogonality & projections | A–E | Examples 4.1–4.5; Problems 1–8 |
| 2 · Subspaces & least squares | F–H | Examples 4.6–4.8; Problems 9–16 |
| 3 · Orthonormal bases & Gram–Schmidt | I–K | Examples 4.9–4.13; Problems 17–24; mixed 25–28 |
| 4 · TL;DR cheat sheet | Review | Method selector, hypotheses, fit/GS recipes, Example 4.14 |

Eleven part-level goals, source ranges, checkpoints and takeaways; 14 numbered
examples; six original SVGs; 28 questions with nearby explained answers and
specific diagnosis/revision/retry links. The two banks are included fragments, not
additional sidebar pages. Mixed 25–28 contain no hints or named methods and use
fresh data, with editorial 20-minute/16-point scoring guidance, not course policy.

## Supporting-source alignment

| Resource | Verified source | Chapter destination |
| --- | --- | --- |
| Recitation2_Solutions.pdf | Problem 4, PDF p.4; (1,1,1,1), (3,1,1,3), their sum; closest to (1,0,0,0) | Example 4.13: dependence, normalized basis and projection |
| mfmlhw2.pdf | Problem 4, PDF p.12, same data as recitation | Example 4.13; duplicate source recognized rather than counted as new coverage |
| Linear_Algebra_Worksheet-1.pdf | Problem 8, pp.2–3; b=(2,4,6), a₁=(1,1,0), a₂=(1,1,1) | Problem 10 and complete normal-equation answer |
| Same worksheet | Problem 9, p.3, four-point line fit | Problem 16, coefficients, residual and SSE |
| Same worksheet | Problem 10(a–c), p.3, projector algebra/geometry/complement | Part F proofs, Problems 12 and 15 |
| Same worksheet | Problems 11/15, pp.3–4, duplicate R⁴ Gram–Schmidt list | Problem 23, orthogonal and normalized bases |
| Same worksheet | Problem 12(a–c), pp.3–4, product of orthogonal matrices and unit-basis coordinates | Problems 18 and 24; printed coefficient typo corrected explicitly |
| MidtermTopics.md | Orthogonality, projections, Gram–Schmidt; special orthogonal matrices | Parts A–K, relevant independent variants and mixed readiness set |

Worksheet pp.3–4 and annotated recitation p.4 were visually inspected as well as
text-extracted. Full course-wide exam-problem coverage is not claimed. Lecture 5,
statistics/PCA and the cumulative exam blueprint remain separate open work.

## Standalone reading revision · 2026-10-27

The owner clarified that readers use the website without the slide deck. Parts B
and F now include faithful redrawn four-space and subspace-projection diagrams,
with labels, captions and alt text. Source references remain attribution. Example
4.6 repeats the complete H matrix and measured record on its own page; Example
4.11 states the record-space condition and links the earlier projector. Source
examples retain their full input data and worked reasoning.
