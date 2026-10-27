(w1-matrix-guide)=
# Lecture 1 · Matrices

::::{div} lecture-one-brief

**Part 2 of 2 · Matrix definitions, every lecture example, and multiplication properties.**

## 4. Matrices and special structures

$A=(a_{ij})\in\mathbb R^{m\times n}$ means **m rows, n columns**;
$a_{ij}$ is row i, column j. A sampler table can use worked rows and marked
sections as its two index roles. Equal numerical shapes alone do not make their
physical meanings interchangeable.

| Structure | Definition |
| --- | --- |
| Diagonal | Square; $a_{ij}=0$ whenever $i\ne j$ |
| Identity $I_n$ | Diagonal ones, off-diagonal zeros; $I_n\mathbf x=\mathbf x$ |
| Symmetric | Square; $A^T=A$, or $a_{ij}=a_{ji}$ |
| Skew-symmetric | Square; $K^T=-K$, or $k_{ij}=-k_{ji}$; hence diagonal entries are zero |

**Lecture examples (pp. 37–39):**

$$
D=\begin{bmatrix}3&0&0\\0&5&0\\0&0&8\end{bmatrix},\quad
I_n=(\delta_{ij}),\quad
S=\begin{bmatrix}3&2&4\\2&5&6\\4&6&8\end{bmatrix}.
$$

Here $\delta_{ij}=1$ if $i=j$, otherwise 0. Thus I is the lecture's general
identity matrix; S is symmetric. A zero diagonal alone does **not** imply skew-symmetry.

## 5. Matrix addition, scalar multiplication, transpose, and trace

:::{admonition} Essential formulas · Match the operation to the shape
:class: key-result

| Operation | Formula and shape |
| --- | --- |
| Matrix addition | $(A+B)_{ij}=a_{ij}+b_{ij}$; A and B must have the same shape |
| Scalar multiplication | $(\lambda A)_{ij}=\lambda a_{ij}$; same shape as A |
| Transpose | $(A^T)_{ji}=a_{ij}$; $m\times n\to n\times m$ |
| Matrix trace | $\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}$; square A |
:::

These entrywise formulas retain the lecture's general addition/scaling examples
(pp. 40–41); those slides do not supply separate numerical matrices to calculate.

**Lecture transpose example (p. 42):**
$A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ gives
$A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}$.
**Lecture trace example (p. 43):** for S above,
$\operatorname{tr}(S)=3+5+8=16$.
Transpose swaps index roles; trace adds only the main diagonal.

## 6. Matrix-vector and matrix-matrix multiplication

:::{admonition} Essential rule · Inner dimensions match; outer dimensions remain
:class: key-result

For $A\in\mathbb R^{m\times n}$, $B\in\mathbb R^{n\times p}$:

$$(AB)_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj},\qquad AB\in\mathbb R^{m\times p}.$$

Each entry is **row i of A dotted with column j of B**. For a vector,
$A\mathbf x=\sum_{j=1}^n x_j\mathbf a_j$, where $\mathbf a_j$ are A's columns;
$(A\mathbf x)_i=\sum_j a_{ij}x_j$.
:::

**Lecture matrix-vector example (p. 45):** with columns
$\mathbf u=(1,-1,0)^T$, $\mathbf v=(0,1,-1)^T$, $\mathbf w=(0,0,1)^T$,

$$
A\mathbf x=
\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=x_1\mathbf u+x_2\mathbf v+x_3\mathbf w
=\begin{bmatrix}x_1\\x_2-x_1\\x_3-x_2\end{bmatrix}.
$$

The source asks which coefficients produce a given b: **$A\mathbf x=\mathbf b$**.
That is the linear-system question developed in Lecture 2.

:::{admonition} Lecture matrix product example (p. 46)
:class: example

$$
A=\begin{bmatrix}1&2&3\\3&2&1\end{bmatrix},\quad
B=\begin{bmatrix}0&2\\1&1\\0&1\end{bmatrix},\quad
AB=\begin{bmatrix}2&7\\2&9\end{bmatrix}.
$$

Shapes: $(2\times3)(3\times2)=2\times2$.
For instance, $(AB)_{12}=1\cdot2+2\cdot1+3\cdot1=7$.
:::

**Both interpretations (p. 47):**

$$A[\mathbf b_1\ \cdots\ \mathbf b_p]=[A\mathbf b_1\ \cdots\ A\mathbf b_p],$$
$$\operatorname{row}_i(AB)=\operatorname{row}_i(A)B
=\sum_{k=1}^n a_{ik}\operatorname{row}_k(B).$$

Thus product columns combine **columns of A**; product rows combine **rows of B**.

**Crochet connection:** plain single crochet consumes/produces $(1,1)^T$;
an increase works two single crochets into one old stitch, giving $(1,2)^T$.
Then $\begin{bmatrix}1&1\\1&2\end{bmatrix}(18,6)^T=(24,30)^T$:
24 consumed, 30 produced. Counts do not specify placement.

:::{admonition} All lecture multiplication properties (p. 48)
:class: key-result

For compatible shapes:

- **Associativity:** $(AB)C=A(BC)$, with A $m\times n$, B $n\times p$, C $p\times q$.
- **Left distributivity:** $(A+B)C=AC+BC$.
- **Right distributivity:** $A(C+D)=AC+AD$.
- **Identity:** $I_mA=A=AI_n$ for A $m\times n$.

In the distributive identities, A and B are $m\times n$, C and D are $n\times p$.
:::

:::{admonition} Exam warnings
:class: pitfall

Matrix multiplication generally **does not commute**: $AB\ne BA$.
$AB\mathbf x$ applies B first. Transpose is not generally inverse;
$(AB)^T=B^TA^T$ reverses order. A trace is not the sum of all matrix entries.
:::

[Back to vectors](index.md).
*Source: Erisa Terolli, CS 556, Week 1 “Matrices and Vectors,” pp. 35–48;
[original slides](https://github.com/archipelagoing/Math4MLBook/blob/main/resources/lectures/WK1_%20Vectors%20and%20Matrices.pdf).
Crochet connection and additional exam warnings are added exposition.*
::::
