(w1-matrices)=
# Matrices: many rows, one structured record

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

## Dimensions and entries

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

## Addition and scaling remain entrywise

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

## Transpose swaps the index roles

The transpose $A^T$ has entries $(A^T)_{ji}=a_{ij}$. Thus an $m\times n$ matrix
becomes $n\times m$: its rows become columns and its columns become rows.

For the rectangular example

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

## Diagonal and identity matrices

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

## Symmetric and skew-symmetric structures

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

## Trace: sum of the diagonal

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
