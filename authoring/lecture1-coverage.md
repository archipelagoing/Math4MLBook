# Lecture 1 source-coverage audit

Current revision: 2026-10-26. The owner requires the listed topics **and all lecture
examples** to survive condensation. The two teaching pages, accompanied by exercises and solutions, retain every distinct
mathematical example and property below; progressive reveals are combined rather
than repeated. Artwork is summarized through its mathematical meaning, not copied.
PDF page numbers include the title/reveal slides.

Reader destinations: [vectors](../book/lecture1/index.md) and
[matrices](../book/lecture1/matrix-guide.md).

| PDF pages | Topic / original example retained | Destination |
| --- | --- | --- |
| 3–5 | Ordered real vectors; (5,2), (1,7,3); house record (3,2,2,2008,150000) | Vectors §1.1 |
| 6 | Standard coordinate directions and 2D/3D coordinate combinations | Vectors §1.1 |
| 7–8 | Head-to-tail addition; x=(0,2), y=(2,2), sum=(2,4), difference=(-2,0) | Vectors §1.2 |
| 9 | Scaling (2,2) by 2, 1/2, and -1, including geometric direction changes | Vectors §1.2 |
| 10–18 | Linear combinations; u=(1,2,4), v=(2,1,4), w=(9,8,7); line/plane/space and redundancy qualification | Vectors §1.3 |
| 19 | c(1,1,0)+d(0,1,1)=(c,c+d,d); plane y=x+z; outside vector (1,2,3) | Vectors §1.3 |
| 20–22 | All equivalent dot-product notations and sum; (3,4)·(4,3)=24 | Vectors §1.4 |
| 23 | Dot-product commutativity, distributivity, non-associativity warning explained using scalar output | Vectors §1.4 |
| 24–26 | Angle between vectors; perpendicular/Pythagorean case; cosine law and expanded squared-distance derivation; cosine formula | Vectors §1.6 |
| 27–34 | Length/magnitude/norm, sum of squares, norm=5, mu=1/5, unit vector=(3/5,4/5), unit length condition | Vectors §1.5 |
| 35–36 | General m-by-n real matrix and index meanings | Matrices §1.7 |
| 37 | Diagonal example diag(3,5,8) | Matrices §1.8 |
| 38 | General identity matrix, diagonal 1/off-diagonal 0 | Matrices §1.8 |
| 39 | Symmetric [[3,2,4],[2,5,6],[4,6,8]]; skew-symmetric definition | Matrices §1.8 |
| 40–41 | General entrywise matrix addition and scalar multiplication (no separate numerical examples on these slides) | Matrices §1.9 |
| 42 | Transpose [[1,2],[3,4]] to [[1,3],[2,4]] | Matrices §1.10 |
| 43 | Trace of the source symmetric matrix: 3+5+8=16 | Matrices §1.10 |
| 44–45 | Matrix-vector column combination; difference matrix and output (x1,x2-x1,x3-x2); Ax=b question | Matrices §1.11 |
| 46 | General matrix product and dimensions; [[1,2,3],[3,2,1]] times [[0,2],[1,1],[0,1]] gives [[2,7],[2,9]] | Matrices §1.12 |
| 47 | Product applied to every B column; product rows as combinations of B rows | Matrices §1.12 |
| 48 | Associativity, both distributive identities, left/right identities with compatible shapes | Matrices §1.12 |

The source PDF was read through extracted text, with rendered image checks on
pages 4–6, 8–9, 12, 15, 18–19, 22, 28, 39, 42, 45–46 to resolve coordinates.
Symbols are sometimes renamed locally; numerical examples retain the source data.
The addition example is (0,2)+(2,2), not (2,0)+(2,2): reading the displayed columns
matters. No claim is made that the source examples themselves were wrong.

The added angle value 16.26°, shadow/point records, absolute-value scaling reminder,
transpose-product identity, and exam warnings are labeled as added exposition.
A plane-normal check verifies that the source's third direction lies outside the
first two directions' plane; it does not introduce determinants as a prerequisite.
The textbook retains derivations, worked examples, and four original diagrams;
repeated reveals are combined. The 24-problem practice bank and explained solutions
are included in the reader navigation. Printed page count is not a constraint.

## Teaching structure within the four-page route

Sections 1.1–1.6 cover vector records, vector arithmetic, combinations, dot products,
norms/unit vectors, and angles. Sections 1.7–1.12 cover matrix records, special
structures, arithmetic, transpose/trace, matrix-vector products, and matrix products.
Each section includes an objective, source reference, checkpoint, takeaway, and
practice link. The chapter contains 12 numbered worked examples and an explicitly
labeled cosine-formula proof. Norms are defined before angles so the formula's
length terms are understood; the source-page labels retain the original locations.

## Selected analogy and changed supplemental exercises

The owner selected shadows. Original lecture examples and formal properties above
are unchanged. Supplemental examples now use O=[[1,0,0],[0,1,0]] and the canonical
stacked front/side H=[[1,0,0],[0,1,0],[0,1,0],[0,0,1]]. Problem 15 now computes
H(12,4,2)=(12,4,4,2). Problem 1 correctly accepts signed coordinates; Problem 19
uses a coordinate sum, with its hidden horizontal redistribution distinguished
from O's hidden depth. The four-bead X profiles retain r,s,e,a and W's exact numbers
but their domain is real coordinate measurements, not counts.
