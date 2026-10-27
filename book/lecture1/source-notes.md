(w1-source-notes)=
# Source notes and lecture coverage

## Course source

This chapter follows **Erisa Terolli, “Matrices and Vectors,” CS 556**, the
48-page Week 1 PDF supplied with this repository:
[original lecture file](https://github.com/archipelagoing/Math4MLBook/blob/main/resources/lectures/WK1_%20Vectors%20and%20Matrices.pdf).
Page numbers below are one-based PDF pages, including title and reveal pages.

The chapter is newly written exposition with original schematic figures and
practice. Named source examples are attributed in the text. The progression and
mathematical scope follow the lecture; the knitting/crochet constructions,
record-space interpretations, checkpoints, mixed practice, and diagnostic feedback
are added teaching material.

## Section-level coverage

| Lecture pages | Source material | Textbook destination |
| --- | --- | --- |
| 1–6 | Context, numerical records, vector entries and geometric representation | [Opening](index.md), [vectors](vectors.md) |
| 7–9 | Addition and scalar multiplication | [Vectors](vectors.md) |
| 10–19 | Linear combinations, lines/planes, geometric membership example | [Combinations](combinations.md) |
| 20–26 | Dot product, properties, orthogonality, cosine formula and its derivation | [Geometry](geometry.md) |
| 27–34 | Norm, magnitude, unit vectors, normalization example | [Geometry](geometry.md) |
| 35–36, 40–41 | Matrix entries, dimensions, addition and scalar multiplication | [Matrices](matrices.md) |
| 37–39 | Diagonal, identity, symmetric and skew-symmetric matrices | [Matrices](matrices.md) |
| 42–43 | Transpose and trace | [Matrices](matrices.md) |
| 44–48 | Matrix-vector/product definitions, column and row views, algebraic properties | [Products](products.md) |

## Reading the original notation accurately

PDF text extraction can reorder entries of a displayed column or matrix. Source
pages 4, 19, 22, 28, 39, 42, 45, and 46 were inspected as rendered images as well
as text when preparing this chapter. In particular:

- The outside-plane example on page 19 is $(1,2,3)^T$, not $(1,3,2)^T$.
- The dot-product and norm examples use $(3,4)^T$.
- The page 46 multiplication example has A rows $(1,2,3)$ and $(3,2,1)$,
  with product rows $(2,7)$ and $(2,9)$.

These are transcription clarifications, not claims that the original examples
are mathematically wrong. Repeated reveal slides were consolidated into complete
explanations. We state conditions explicitly: nonzero vectors for angles/unit
directions, matching shapes for operations, and genuinely different directions
when combinations are said to fill a plane or all of space.

The source's informal warning about dot-product associativity is explained through
output types: a dot product produces a scalar, so it cannot simply be iterated
as though it returned another vector.

## Craft constructions and terminology

The sampler and operation ledger are illustrative mathematical constructions;
no completed physical sample or measured gauge dataset is claimed here. Each
section has six stitches; pink counts leave the rest green. Rows are displayed
in record order in the schematics, which are not loop-accurate technique diagrams.
Counts omit stitch order, tension, and other fabric properties.

Terminology follows the [Craft Yarn Council knitting abbreviations](https://www.craftyarncouncil.com/standards/knitting-abbreviations)
and [US crochet abbreviations](https://www.craftyarncouncil.com/standards/crochet-abbreviations).
Selected plain/increase/decrease operations are defined before they are counted.
The mathematical extension to real signed coordinates does not authorize negative
or fractional physical stitches.

## Scope of the first chapter

Projection, systematic elimination, determinants/inverses, four fundamental
subspaces, eigenvectors, SVD, and PCA are developed in later lectures. This
chapter provides their prerequisites and occasionally names the next question;
it does not require those later methods to solve Lecture 1 practice.

Two synthesis problems extend the lecture's operations: symmetric/skew-symmetric
decomposition and trace(AB)=trace(BA). They are explicitly derived from the
introduced definitions rather than presented as assumed background.
