(lecture-one)=
# Vectors and matrices: reading a pattern mathematically

<div class="chapter-kicker">Lecture 1 · The language of linear algebra</div>

A knitting pattern tells your hands what to do. A mathematical representation tells
you what you can count, compare, and predict about those actions. The two are
connected, but they are not the same thing: two rows can contain the same number
of pink stitches while arranging them differently.

We will follow a small sampler with **24 stitches across**, divided by markers
into four sections of six stitches. One row has pink-stitch counts

$$
\mathbf r=\begin{bmatrix}3\\1\\3\\1\end{bmatrix}.
$$

The remaining stitches in each section are green. Another row uses
$\mathbf s=(1,3,1,3)^T$. Both contain eight pink stitches. A single total cannot
explain their difference; a vector can. Four such rows make a matrix, and matrix
multiplication lets us summarize many rows or combine several kinds of stitch
operation at once.

```{figure} ../figures/lecture1/sampler.svg
:name: fig-w1-sampler
:alt: Four rows of 24 stitch cells grouped into four sections of six. Pink counts alternate between 3,1,3,1 and 1,3,1,3. The adjacent four-by-four count matrix records those counts, with eight pink stitches in every row.

One sampler, several records. Each matrix entry summarizes **six stitches**;
it is not a single stitch or a shade of pink. Rows are displayed in record order.
```

This chapter develops the complete first lecture: vectors, combinations, dot
products, lengths and angles, matrices, special matrices, transpose, trace, and
matrix multiplication. We retain the lecture's progression and develop the
reasoning between its examples. You will meet the original geometric examples
alongside the craft constructions, then practice without either story.

## Before you begin

You need arithmetic with signed numbers and fractions, square roots, simple
algebra, and the idea of Cartesian coordinates. Summation notation is introduced
when it is needed. You do not need prior knitting or crochet experience: every
craft action used in a calculation is defined.

Our examples use US crochet terminology. A **plain** operation produces one new
stitch from one old stitch; a **single increase** produces two from one; a **single
decrease** produces one from two. These describe selected operations, not every
possible stitch. Their count records do not determine tension, texture, yarn use,
or the whole fabric.

:::{admonition} What you will be able to do
:class: key-result

By the end, you should be able to:

1. Declare what a vector's entries mean and compute with compatible vectors.
2. Form a linear combination and test a simple membership claim.
3. Compute dot products, norms, unit vectors, distances, and angles, with their conditions.
4. Read matrix dimensions and entries; recognize diagonal, identity, symmetric, and skew-symmetric matrices.
5. Transpose a matrix, compute its trace when defined, and check the shape of every expression.
6. Multiply a matrix by a vector and another matrix using both entrywise calculations and the column/row interpretations.
7. Explain a result, catch an invalid operation, and verify a fresh calculation independently.
:::

## Your route through the chapter

| Read | The central question |
| --- | --- |
| [Vectors and their meaning](vectors.md) | What does an ordered record retain? |
| [Combinations and reachable patterns](combinations.md) | What can addition and scaling produce? |
| [Dot products, lengths, and angles](geometry.md) | How can we compare two records? |
| [Matrices and special structures](matrices.md) | What changes when we record many rows? |
| [Multiplication and composition](products.md) | What does a matrix actually do? |
| [Synthesis and readiness](review.md) | Can you select and check the right operation? |
| [Practice](practice.md) and [explained solutions](solutions.md) | Can you solve unfamiliar problems unaided? |

Read the worked examples with a pencil. Before opening a checkpoint answer, write
a prediction. After a worked calculation, cover it and reproduce the reasoning.
The final practice mixes questions so the method is no longer supplied by the
section title.

A chapter is useful when you can do the mathematics after leaving the sampler
behind. That is the purpose of the formal practice at the end.

[Source notes and lecture coverage](source-notes.md) identify the original lecture
pages, the added teaching constructions, and the scope of this chapter.
