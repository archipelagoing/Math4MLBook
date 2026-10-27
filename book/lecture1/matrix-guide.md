(w1-matrix-guide)=
# Lecture 1 · Matrices and products

<div class="chapter-kicker">Organize the sampler, then act on its records</div>

One row gave us a vector. Recording several rows gives a matrix; storing the effects
of stitch operations in its columns gives a map. This page develops both views,
keeping the input coordinates, output coordinates, and dimensions visible.

[Vectors and geometry](index.md) · **Matrices and products** · [Exercises](practice.md) · [Solutions](solutions.md)

(w1-matrices)=
## 1. Matrices: organized records

One row of section counts is a vector. Recording four rows at once gives a matrix:

$$
W=\begin{bmatrix}
3&1&3&1\\
1&3&1&3\\
3&1&3&1\\
1&3&1&3
\end{bmatrix}.
$$

Here a row means a worked row of the sampler and a column means one fixed
six-stitch section. The entry $w_{23}=1$ says row 2 has one pink stitch in
section C. It does not say that the third individual stitch is pink: the entry
summarizes a section.

### Dimensions and entries

:::{admonition} Definition · Real matrix
:class: definition

An $m\times n$ real matrix $A=(a_{ij})\in\mathbb R^{m\times n}$ has $m$ rows
and $n$ columns. The index $i$ selects a row; $j$ selects a column.

$$
A=\begin{bmatrix}
a_{11}&\cdots&a_{1n}\\
\vdots&\ddots&\vdots\\
a_{m1}&\cdots&a_{mn}
\end{bmatrix}.
$$

A column vector in $\mathbb R^n$ can be treated as an $n\times1$ matrix.
A row vector has shape $1\times n$.
:::

Our full panel happens to have four rows and four sections, so W is square.
A three-row observation of the same panel would be $3\times4$. Square shape is
a numerical property of the record, not a statement that the physical fabric
has equal width and height.

The order **rows by columns** matters. A $2\times3$ matrix and a $3\times2$
matrix contain the same number of entries but usually represent different maps.
Write dimensions before multiplying them.

### Addition and scaling remain entrywise

If A and B have the same shape,

$$
(A+B)_{ij}=a_{ij}+b_{ij},\qquad (cA)_{ij}=ca_{ij}.
$$

Adding two swatch count matrices can record combined counts across corresponding
rows and sections of two samples. It does not automatically specify one new
six-stitch section: the combined record may exceed the original per-section bound.
As with vectors, both coordinate alignment and physical interpretation matter.

:::{admonition} Worked example · Arithmetic before interpretation
:class: example

Let

$$
A=\begin{bmatrix}1&2\\3&4\end{bmatrix},\qquad
B=\begin{bmatrix}2&0\\-1&1\end{bmatrix}.
$$

Then

$$
A+B=\begin{bmatrix}3&2\\2&5\end{bmatrix},\qquad
2A-B=\begin{bmatrix}0&4\\7&7\end{bmatrix}.
$$

Check the lower-left entry independently: $2\cdot3-(-1)=7$.
The minus sign applies to the whole B, not only its positive entries.
:::

### Transpose swaps the index roles

The transpose $A^T$ has entries $(A^T)_{ji}=a_{ij}$. Thus an $m\times n$ matrix
becomes $n\times m$: its rows become columns and its columns become rows.

The lecture starts with
$A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and
$A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}$: the off-diagonal entries exchange places.

For an additional rectangular example

$$
R=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix},\qquad
R^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.
$$

The entry 5 changes position from $(2,2)$ to $(2,2)$; the entry 3 moves from
$(1,3)$ to $(3,1)$. Following entries is more reliable than memorizing a motion.
For a column vector, $\mathbf v^T$ is a row, so
$(1\times n)(n\times1)$ explains why $\mathbf u^T\mathbf v$ is a scalar.

In W, transposition changes “row of section counts” to “section's counts across
rows.” Its numeric array happens to equal its transpose. The physical meanings
of the two index roles still differ. Transpose is not turning the fabric over,
changing knitting to crochet, or generally taking an inverse.

Useful identities follow from the indices:

$$
(A^T)^T=A,\qquad (A+B)^T=A^T+B^T,\qquad (cA)^T=cA^T.
$$

We will derive the reversed-order identity for a product in the next section.

### Diagonal and identity matrices

A square **diagonal matrix** has zero off-diagonal entries. Its diagonal entries
can be any real numbers, including zero:

$$D=\operatorname{diag}(3,5,8)=\begin{bmatrix}3&0&0\\0&5&0\\0&0&8\end{bmatrix}.$$

A diagonal matrix scales individual coordinates without mixing them. In a
section-count record, $\operatorname{diag}(2,1,2,1)$ doubles contributions of
sections A and C while leaving B and D unchanged. The result is a numeric
weighted record; an actual six-stitch limit still needs checking.

The **identity matrix** $I_n$ has ones on the diagonal and zeros elsewhere.
For every $\mathbf x\in\mathbb R^n$, $I_n\mathbf x=\mathbf x$. Later, for
$A\in\mathbb R^{m\times n}$, the compatible identities are
$I_m A=A=A I_n$. The sizes of the left and right identities need not match.

### Symmetric and skew-symmetric structures

A real square matrix is **symmetric** when $A^T=A$, equivalently $a_{ij}=a_{ji}$.
The lecture's example is

$$
S=\begin{bmatrix}3&2&4\\2&5&6\\4&6&8\end{bmatrix}.
$$

Compare each off-diagonal pair: 2 with 2, 4 with 4, 6 with 6. Our W is another
symmetric numeric example. A symmetric record does not by itself prove that its
underlying fabric is physically mirror-symmetric.

A real square matrix is **skew-symmetric** when $K^T=-K$, so $k_{ij}=-k_{ji}$.
For example,

$$K=\begin{bmatrix}0&2&-1\\-2&0&3\\1&-3&0\end{bmatrix}.$$

Its diagonal must be zero: $k_{ii}=-k_{ii}$ implies $2k_{ii}=0$ over the reals.
A zero diagonal is necessary but not sufficient; the off-diagonal sign relation
must also hold. Likewise, being square is necessary for symmetry but does not
make every square matrix symmetric.

:::{admonition} Important distinction · A pattern and its encoding
:class: key-result

Special-matrix labels describe the **numeric array and operation you defined**.
Do not infer them from an attractive fabric picture alone. A binary stitch chart,
a section-count matrix, and a linear map can encode different things.
:::

### Trace: sum of the diagonal

For a square $n\times n$ matrix,

$$\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}.$$

The trace of the lecture's S is $3+5+8=16$. For W it is $3+3+3+3=12$.
The total pink count of the four-row panel is instead 32. Trace, total sum, and
matrix size are different quantities. The diagonal selects row/section positions
whose numeric indices coincide; it is not a count of all stitches or a physical
yarn measurement.

Trace is linear for compatible square matrices:

$$\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B),\qquad
\operatorname{tr}(cA)=c\operatorname{tr}(A).$$

In this course we use the usual square-matrix trace. Do not apply it to a
rectangular matrix by silently inventing a different convention.

:::{admonition} Check your understanding
:class: checkpoint

For $M=\begin{bmatrix}0&3\\-3&0\end{bmatrix}$, find $M^T$, classify its symmetry,
and compute its trace. Would zero trace alone imply the same classification?
:::

:::{dropdown} Reason it through

$M^T=\begin{bmatrix}0&-3\\3&0\end{bmatrix}=-M$, so M is skew-symmetric,
with trace 0. Zero trace alone is not enough: $\operatorname{diag}(1,-1)$ also
has zero trace but is symmetric, not skew-symmetric. Check the defining relation,
not just one consequence of it.
:::

(w1-products)=
## 2. Matrix multiplication: combining and composing

A table becomes especially powerful when its columns are effects we can combine.
The lecture's column interpretation of multiplication and its row-by-column
calculation are two views of the **same operation**. Learn both: one explains
the meaning, and the other supplies a reliable calculation.

### A matrix times a vector combines columns

Return to the shaping operations. One plain operation consumes one old stitch and
produces one new stitch; one increase consumes one and produces two. Put those
effect vectors into the columns of a matrix:

$$
B=\begin{bmatrix}1&1\\1&2\end{bmatrix},\qquad
\mathbf x=\begin{bmatrix}18\\6\end{bmatrix}.
$$

Then

$$
B\mathbf x
=18\begin{bmatrix}1\\1\end{bmatrix}
+6\begin{bmatrix}1\\2\end{bmatrix}
=\begin{bmatrix}24\\30\end{bmatrix}.
$$

The input lists counts of operation types; the output lists consumed and produced
stitches. Equal vector lengths do not make these the same coordinate meaning.
`(k3,kfb)` or `(3 sc,inc)` six times realizes these aggregate counts for the selected
operations, subject to actual placement and technique.

:::{admonition} Key result · Column interpretation
:class: key-result

If $A=[\mathbf a_1\ \cdots\ \mathbf a_n]\in\mathbb R^{m\times n}$ and
$\mathbf x=(x_1,\ldots,x_n)^T$, then

```{math}
:label: eq-w1-columns
A\mathbf x=x_1\mathbf a_1+\cdots+x_n\mathbf a_n\in\mathbb R^m.
```

Input coefficients live in $\mathbb R^n$; output combinations live in
$\mathbb R^m$.
:::

A row of A supplies one output coordinate:
$(A\mathbf x)_i=\sum_{j=1}^n a_{ij}x_j$. For B, the first output is
$18+6=24$ and the second is $18+2\cdot6=30$. This is the same computation as
the column combination, organized differently.

```{figure} ../figures/lecture1/operation-map.svg
:name: fig-w1-operation-map
:alt: Input counts 18 plain operations and 6 increases multiply the columns consumed 1 produced 1, and consumed 1 produced 2. The combined output is 24 old stitches consumed and 30 new stitches produced.

Read a product by naming its spaces. The matrix converts **operation counts**
into a **consumed/produced record**; it does not specify all details of the fabric.
```

### From the lecture's directions to a rectangular map

The source example uses

$$
L=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix}.
$$

Its columns are $(1,-1,0)^T$, $(0,1,-1)^T$, $(0,0,1)^T$. Therefore

$$
L\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=\begin{bmatrix}x_1\\x_2-x_1\\x_3-x_2\end{bmatrix}.
$$

For input $(2,5,9)^T$, the output is $(2,3,4)^T$. Check it using either rows or
columns. Although this particular L is square, matrix-vector multiplication does
not require square shape. For instance, the consumed/produced map including a
decrease is

$$
H=\begin{bmatrix}1&1&2\\1&2&1\end{bmatrix}\in\mathbb R^{2\times3},
\qquad H\begin{bmatrix}15\\3\\3\end{bmatrix}
=\begin{bmatrix}24\\24\end{bmatrix}.
$$

A decrease consumes two stitches and produces one. This input contains 15 plain,
3 increase, and 3 decrease operations. Equal input/output totals do not say that
the fabric is unchanged. Different operations and placements can share this record.

### A matrix times a matrix computes several outputs at once

If B contains several input vectors as columns, multiplying A by B applies A to
each one:

$$A[\mathbf b_1\ \cdots\ \mathbf b_k]
=[A\mathbf b_1\ \cdots\ A\mathbf b_k].$$

This observation determines the shape rule:

:::{admonition} Definition · Matrix product
:class: definition

For $A\in\mathbb R^{m\times n}$ and $B\in\mathbb R^{n\times k}$,
the product $AB\in\mathbb R^{m\times k}$ has entries

```{math}
:label: eq-w1-product
(AB)_{ij}=\sum_{\ell=1}^n a_{i\ell}b_{\ell j}.
```

The inner sizes n match; the outer sizes m and k give the result. Entry $(i,j)$
is row i of A dotted with column j of B.
:::

Do not multiply corresponding entries: that is a different operation. The usual
matrix product combines shared-coordinate contributions through the summation.

:::{admonition} Worked example · The lecture's product
:class: example

$$
A=\begin{bmatrix}1&2&3\\3&2&1\end{bmatrix},\qquad
B=\begin{bmatrix}0&2\\1&1\\0&1\end{bmatrix}.
$$

Their shapes are $2\times3$ and $3\times2$, so the product is $2\times2$:

$$
AB=\begin{bmatrix}
1\cdot0+2\cdot1+3\cdot0 & 1\cdot2+2\cdot1+3\cdot1\\
3\cdot0+2\cdot1+1\cdot0 & 3\cdot2+2\cdot1+1\cdot1
\end{bmatrix}
=\begin{bmatrix}2&7\\2&9\end{bmatrix}.
$$

Check by columns: the first B column is $(0,1,0)^T$, so the first product column
must be the second column of A, namely $(2,2)^T$. This provides an independent
interpretation of part of the calculation.
:::

The row interpretation is equally useful:

$$\operatorname{row}_i(AB)=\operatorname{row}_i(A)B
=\sum_{\ell=1}^{n}a_{i\ell}\operatorname{row}_{\ell}(B).$$

The coefficients in row i of A combine the rows of B. This and the column interpretation must agree with
all entrywise calculations.

### Summarize several sampler rows at once

The panel count matrix is

$$W=\begin{bmatrix}3&1&3&1\\1&3&1&3\\3&1&3&1\\1&3&1&3\end{bmatrix}.$$

Let e be the four-entry all-ones vector. Then $W\mathbf e=(8,8,8,8)^T$ gives
total pink counts for each row. In contrast, $W^T\mathbf e=(8,8,8,8)^T$ gives
pink counts for each section across all four rows. The numbers coincide here;
the questions are still different.

To sum A/B sections and C/D sections separately, use

$$
S=\begin{bmatrix}1&0\\1&0\\0&1\\0&1\end{bmatrix},\qquad
WS=\begin{bmatrix}4&4\\4&4\\4&4\\4&4\end{bmatrix}.
$$

W has shape $4\times4$, S has shape $4\times2$, and WS has shape $4\times2$.
Each product column combines W columns; each row gives the two grouped totals.
The alternating pattern disappears in this summary. Multiplication can be
correct and still discard information the original record retained. Later we
will study that loss using rank and null spaces.

### Composition: the rightmost map acts first

If B converts one input record to an intermediate record, and A converts that
record to the final output, then $A(B\mathbf x)=(AB)\mathbf x$.
In our sampler, S defines section groups and W records their contributions
across rows. The product WS is meaningful because the intermediate section
coordinates match. Always name and check that shared space.

For $A\in\mathbb R^{m\times n}$, $B\in\mathbb R^{n\times p}$,
$C\in\mathbb R^{p\times q}$, multiplication is **associative**:
$(AB)C=A(BC)$. It is **distributive**:
$(A+B)C=AC+BC$ and $A(C+D)=AC+AD$ for
$A,B\in\mathbb R^{m\times n}$, $C,D\in\mathbb R^{n\times p}$.
These are both distributive identities from the lecture. These rules can be established by expanding
the finite sums in {eq}`eq-w1-product` and regrouping scalar products.

Multiplication is generally **not commutative**, even when both orders exist.
For example,

$$
D=\begin{bmatrix}2&0\\0&1\end{bmatrix},\qquad
P=\begin{bmatrix}0&1\\1&0\end{bmatrix}
$$

satisfy

$$DP=\begin{bmatrix}0&2\\1&0\end{bmatrix},\qquad
PD=\begin{bmatrix}0&1\\2&0\end{bmatrix}.$$

Scaling the first coordinate and then swapping is different from swapping and
then scaling whichever coordinate is now first. The records have explicit
coordinate labels; the arithmetic describes those operations, not magic changes
of stitch technique. With rectangular matrices, one order may not exist at all.

### Transposing a product reverses its order

For the same shapes as above,

$$(AB)^T=B^T A^T.$$

The reversal follows by comparing entry $(j,i)$:
$\sum_{\ell}a_{i\ell}b_{\ell j}=\sum_{\ell}(B^T)_{j\ell}(A^T)_{\ell i}$.
The shapes also agree: both results are $k\times m$. The expression $A^T B^T$
is generally wrong, and may not even be defined.

:::{admonition} Check your understanding
:class: checkpoint

A has shape $2\times3$ and B has shape $3\times4$. Which of AB, BA, $A^T B$,
and $B^T A^T$ exist, and what are their shapes?
:::

:::{dropdown} Reason it through

AB exists with shape $2\times4$. BA does not: inner sizes 4 and 2 differ.
$A^T B$ does not: inner sizes 2 and 3 differ. $B^T A^T$ exists, with shape
$(4\times3)(3\times2)=4\times2$, matching $(AB)^T$.
The answer comes from dimensions before any entries are required.
:::

The final question on the source slide is which input combination produces a
particular output b. We can now write that question as $A\mathbf x=\mathbf b$.
Solving it systematically, and deciding whether the answer is unique or even
exists, will be the focus of Lecture 2.

(w1-review)=
## 3. Before you move to the exercises

Use a consistent routine: **state shapes → choose a definition → calculate → check**.
For membership, substitute your coefficients. For a product, check one column
independently. For a claimed unit vector, compute its length. For symmetry, compare
A with its transpose rather than judging the picture.

Try the [24 exercises](practice.md) before consulting [solutions](solutions.md).
The first eight isolate the tools; the next ten apply them to changed examples;
the final six mix ideas. An error is useful if you can identify its cause and retry
without the answer visible. Systematic solution of $A\mathbf x=\mathbf b$ follows
in Lecture 2.

(w1-source-notes)=
## Lecture sources

This chapter develops **Erisa Terolli, “Matrices and Vectors,” CS 556**, the supplied
48-page Week 1 deck. [Original slides](https://github.com/archipelagoing/Math4MLBook/blob/main/resources/lectures/WK1_%20Vectors%20and%20Matrices.pdf).
Repeated reveal slides are combined; all distinct numerical examples and properties
are retained. Lecture examples are identified in context.

| PDF pages | Where to read |
| --- | --- |
| 1–19 | {ref}`Vectors <w1-vectors>` and {ref}`linear combinations <w1-combinations>` |
| 20–34 | {ref}`Dot products, norms, unit vectors, and angles <w1-geometry>` |
| 35–43 | {ref}`Matrices, special structures, arithmetic, transpose, and trace <w1-matrices>` |
| 44–48 | {ref}`Matrix-vector products, matrix products, and their properties <w1-products>` |

The stitch records, four original diagrams, checkpoints, and practice are added
teaching material. Source pages were checked visually where text extraction
reordered coordinates. In particular, the addition uses $(0,2)^T$, the vector
outside the lecture's plane is $(1,2,3)^T$, and the lecture product has rows $(2,7)$
and $(2,9)$. These are transcription checks, not claims of source errors.

Craft examples use US crochet terminology. A plain operation consumes one stitch
and produces one; an increase consumes one and produces two; a decrease consumes
two and produces one. Counts do not describe tension, placement, or the full fabric.
No physical pattern execution is claimed. The synthesis exercises on symmetric/skew
parts and trace(AB)=trace(BA) extend the lecture using definitions already taught.
