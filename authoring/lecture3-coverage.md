# Lecture 3 · Source and practice coverage

Date: 2026-10-27. Source: Erisa Terolli's CS 556
`resources/lectures/WK3_VectorSpaces_SLE_Rank.pdf`, **all 35 PDF pages**.
Parts A–K retain lecture topic order. Title/thank-you pages and progressive reveals
are consolidated; handwritten mathematics on pages 16–17 is explicitly included.

## Slide-to-textbook map

| PDF pages | Retained topic / example | Destination |
| --- | --- | --- |
| 1–2 | Deck and vector-space titles | Page 1 opener |
| 3–6 | Rn; R2 examples (3,2),(0,0); R3 examples (1,2,3),(0,0,0); closure; shaded-quadrant failure under −v | A, Example 3.1 and original subspace-test diagram |
| 7–8 | Subspace closure, zero, arbitrary λv+μw; all R2 subspaces: plane, origin-lines, zero | B, Example 3.2 and zero/closure checkpoints |
| 9–10 | Column combinations/solvability; P=[1,0;4,3;2,3], coefficients .4,.3, output (.4,2.5,1.7), generated plane | C, Example 3.3 |
| 11–12 | Null-space definition and ambient dimensions; A=[1,1,2;2,1,3;3,1,4], reduction, pivots/free variable, special solution (−1,−1,1), null line; relaxing constraints annotation | D, Example 3.4 and Practice 6 |
| 13 | All four fundamental subspaces, notation and ambient spaces; what each means | E, Example 3.5, original O/H diagram; dimension/basis recipes formalized in J |
| 14–15 | Particular + null complete-solution recipe | F, short two-direction proof |
| 16, Q1 | [1,1,3;1,2,4;2,2,6] with right side (15,21,30), particular (9,6,0), null (−2,−1,1) | F, Example 3.6, full reduction/verification |
| 16, Q2 | Four unknowns, rows [1,2,3,5], [2,4,8,12], [3,6,7,13], right side (0,6,−6); two null directions | F, Example 3.7, corrected particular and all parameter directions |
| 17, Q3 | Rows [1,1,2], [3,−1,14], [1,2,0], right side (−2,6,0); inconsistent system | F, Example 3.8, checked contradiction 0=5 |
| 18–20 | Rank, pivot count/bounds, information interpretation; 2×4 matrix [1,1,0,1;2,1,0,5] and planar column arrows | G, Example 3.9, rank 2 and column relation |
| 21 | Rank of [1,2,1;−2,−3,1;3,5,0] | G, Example 3.10, full reduction/rank 2 |
| 22–26 | Independence via zero combination; out-of-plane third vector; collinear pair/nonparallel pair/three planar arrows NO/YES/NO; at most n independent in Rn | H, Example 3.11, original independence diagram and fresh tests |
| 27–28 | Span definition; e1,e2 span R2; adding (5,6) changes no span; (1,1),(3,3) span one line | I, Example 3.12 |
| 29 | v=(1,2,0), S={(1,1,0),(1,7,0)}, weights 5/6,1/6 | I, Example 3.13, clarification v∈span(S) rather than v∈S |
| 30–33 | Basis: independent+spanning, unique representation, multiple bases, dimension; natural e1=(1,0), e2=(0,1); generic tilted r,s grid | J, Example 3.14, proof of coordinate uniqueness, basis/dimension recipes |
| 34 | B=[3,1;1,1], basis coordinates (3/2,1/2), natural coordinates (5,2), inverse/round trip | K, Example 3.15, original coordinate diagram |
| 35 | Closing slide | Source/next-lecture bridge |

## Corrections and representation choices

- **Page 16 Q2:** the handwritten particular vector starts with −3, but its first
  original equation with c=3, b=d=0 would evaluate to 6, not 0. The correct particular
  is **(−9,0,3,0)**. The source null vectors (−2,1,0,0) and (−2,0,−1,1) are valid.
- **Page 17:** retain the displayed original equations and the no-solution conclusion.
  Recompute the intermediate arithmetic; the explicit chosen sequence yields 0=5.
- **Page 29:** the calculation establishes membership in span(S), not in the
  two-element set S. Both the weights and all original vector coordinates remain.
- **Page 13:** spaces are subsets of their ambient spaces; use ⊆, not element ∈.
- The vector-space explanation states the usual algebraic axioms and distinguishes
  those inherited by subsets of Rn from the closure tests. Zero/nonempty conditions
  are explicit; rank zero is allowed.
- Updated-row usage in p. 12 elimination is written in an unambiguous legal order.
  Original columns are used for column-space generators; nonzero reduced rows for row space.
- Extracted display order can reverse vector entries. The rendered p. 28/p. 34
  images establish (5,6), B=[3,1;1,1], and coordinates (3/2,1/2)→(5,2), all retained.
- Read all extracted pages and inspected the unique graphic/matrix/annotated source
  pages, particularly 4–7, 10–13, 15–17, 19–21, 23–24, 26–29, 31–34. Third-party
  source artwork is described mathematically and replaced with original SVGs.
  Decorative and superseded craft annotations are not repeated as textbook mathematics.

## Four numbered reader pages

1. `index.md`: A–E spaces/subspaces and four spaces; Practice 1–8.
2. `solutions-rank.md`: F–G complete solutions/rank; Practice 9–16.
3. `basis.md`: H–K independence/span/basis/coordinates; Practice 17–24 and mixed 25–28.
4. `cheatsheet.md`: formula/condition/method reference and original Example 3.16.

`practice.md` and `solutions.md` are included banks, not extra reader pages. Each
answer follows its question as an expandable, numbered-step explanation.
There are 11 part-level checkpoints and 16 numbered worked examples. All new
problem, solution, concept and figure IDs use w3/lecture3 prefixes.

## Supporting-source and independent-practice map

| Supplied source | Implemented destination | What was verified |
| --- | --- | --- |
| Recitation2_Solutions.pdf p. 2, Problem 2 | Practice 8: four spaces of [1,3,1,2;2,6,4,8;0,0,2,4] | Original pivot columns, reduced row basis, both null spaces, independence/counts. Opposite left-null vectors and alternate row bases span the same spaces. |
| Recitation2_Solutions.pdf p. 3, Problem 3 | Practice 15: recover A and attainable right sides from a complete solution | A=[1,−1,0;2,−2,0;2,−2,0], rank 1, exact output family |
| Recitation2_Solutions.pdf p. 1, Problem 1; mfmlhw2.pdf Problem 1, pp. 1–4 | Practice 16, β notation replacing source scalar b | Row-swap case β=−2, singular case β=−1, consistency g=−1, family and selected z=2 solution |
| MidtermTopics.md | A–K and mixed readiness set | Named topic coverage: spaces/subspaces, four spaces, rank, independence, span, basis/change of basis, elimination. This is not a full-course exam blueprint. |

The other regular questions are fresh numerical/conceptual variants rather than
copies of worked source matrices. Four no-hint mixed problems include a subspace/
basis test, inconsistent rank comparison, span/dependence task and non-unit-determinant
coordinate round trip. They include an editorial 20-minute suggestion, 16-point
practice criteria, checked solutions and targeted diagnosis/retry links. No official
course timing, A cutoff, or actual student-readiness claim is inferred.

Recitation 2 Problem 4 requires orthonormal bases and projection, so it is deferred
to Lecture 4 rather than silently included as a Lecture 3 prerequisite. Full
supporting-exam coverage and cross-course cumulative readiness remain open.
