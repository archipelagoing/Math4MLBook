# Lecture 2 · Full-deck coverage

Date: 2026-10-27. Source: Erisa Terolli's CS 556
`resources/lectures/WK2_SLE_Inverse_Determinants.pdf`, **all 36 PDF pages**.
The former systems-only boundary is superseded. Pages count from the first PDF
page; title pages and progressive reveals are consolidated. The reader's parts
A–N follow lecture topic order without omitting the determinant/inverse material.

| PDF pages | Lecture topic and retained examples/formulas | Textbook part |
| --- | --- | --- |
| 1–3 | Deck/unit titles; difference matrix with columns (1,−1,0), (0,1,−1), (0,0,1); row dot products and column combinations | A, Example 2.1 |
| 4 | x−2y=1, 3x+2y=11; row, column, matrix pictures and (3,1) | A, Example 2.2 |
| 5 | x+2y+3z=6, 2x+5y+2z=4, 6x−3y+z=2; matrix and three planes | A, Example 2.3; full elimination in Problem/Solution 12 |
| 6–7 | Main system (solution 5,4,2); handwritten x+y=3, x−y=1 substitution check; row exchange, scale, addition | A–B; Example 2.4; full solve in D |
| 8 | Gaussian elimination; REF/RREF definitions; 4×5 RREF matrix with pivots 1,3,4 | B–C, Example 2.5 |
| 9–21 | Progressive main-system reduction through final RREF | D, Example 2.6: six highlighted steps, including back substitution and RREF continuation |
| 22–23 | Determinant title, real scalar function on square matrices, determinant bars | E; 2×2 computation in Example 2.9 |
| 24 | det(I)=1, row-swap sign, separate row linearity with scale and additive formulas | F: both row-linearity identities retained |
| 25 | Equal/zero rows, row replacement, triangular diagonal product, singular/invertible test, product and transpose identities | F; Example 2.10 with determinant bookkeeping |
| 26 | Both fixed-row and fixed-column Laplace sums; deleted submatrix dimensions | G: explicit row/column deletion notation and sign grid |
| 27–28 | D=[1,2,3;3,1,2;0,0,1], row-1 expansion, determinant −5 | G, Example 2.11; sparse-row cross-check added |
| 29 | Area/volume and inverse applications | H, Example 2.12; absolute value, shape and orientation clarified |
| 30–31 | Inverse definition, two-sided identity, terminology, Q=[1,2,1;4,4,5;6,7,7] and supplied inverse | I, Example 2.13; both products verified |
| 32 | n pivots, nonzero determinant, only zero solves Ax=0 | J: equivalent square-matrix tests, with singular-system caveat |
| 33 | [A|I]→[I|A⁻¹] Gauss–Jordan schematic | K, Example 2.14; original complete 2×2 reduction replaces the third-party schematic image |
| 34 | Minors, checkerboard cofactors, transpose/adjugate, determinant division | L: full recipe and short justification |
| 35 | General 2×2 inverse formula | M, Example 2.15, derived from the cofactor construction |
| 36 | Q's exact minors, cofactors, adjugate and inverse | N, Example 2.16; all four intermediate/result matrices retained and determinant 1 shown |

## Reader route and review support

1. `index.md`: **Page 1 · Systems and elimination**, Parts A–D, practice 1–18.
2. `elimination.md`: **Page 2 · Determinants and geometry**, Parts E–H, practice 19–21.
3. `inverses.md`: **Page 3 · Inverses and invertibility**, Parts I–N, practice 22–26.
4. `cheatsheet.md`: **Page 4 · TL;DR**, formulas, method recipes and Example 2.17.

Sidebar links are explicitly numbered under a Lecture 2 caption and mirror the
on-page route. `practice.md` and `solutions.md` are included source banks; each
answer appears as a dropdown directly after its question on the correct topic
page. All original problem/solution labels and concept labels are retained.

All 17 worked examples have numbered, highlighted action steps explaining the
operation and its purpose. Yellow result panels identify major results; red
pitfalls identify invalid operations or conclusions. Blue remains structural,
pink introduces definitions, and green groups worked examples.

## Corrections and additions

- Row scaling is explicitly nonzero. Row replacement retains the source row and
  updates every augmented entry. Gaussian forward elimination and Gauss–Jordan
  continuation are distinguished without changing the source's end result.
- The p. 8 ordinary matrix is not silently treated as augmented. Problem 10
  explicitly declares that interpretation before using its rightmost column as constants.
- Laplace deleted-submatrix notation states exactly which row and column are
  removed for each summation index, avoiding the source's ambiguous shorthand.
- Geometry uses absolute determinant for parallelogram area/parallelepiped volume;
  triangle area takes one half. Sign tracks orientation, not negative volume.
- The adjugate, not A itself, is divided by the determinant. Cofactor signs are
  applied before transposing. The nonzero-determinant condition is stated.
- The point-view matrices O and H are rectangular, with no determinant or two-sided
  inverse. Square screen-coordinate mixing supplies a separate, explicitly declared
  determinant/inverse model; undoing it does not recover unmeasured depth.
- Example 2.17 and C=[2,1;1,1], extra checks/practice, solution classification,
  shadow constructions, readiness mapping and short proofs are editorial additions.
- Every source matrix above was checked against rendered PDF pages. No supplied
  source figure is reproduced; the book uses original SVG diagrams.

Supporting-homework problem alignment, official exam-cutoff policy, independent
expert review and measured learner outcomes remain outside the verified scope.
