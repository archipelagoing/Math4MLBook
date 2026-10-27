(w1-products)=
# Matrix multiplication: combining and composing

A table becomes especially powerful when its columns are effects we can combine.
The lecture's column interpretation of multiplication and its row-by-column
calculation are two views of the **same operation**. Learn both: one explains
the meaning, and the other supplies a reliable calculation.

## A matrix times a vector combines columns

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

## From the lecture's directions to a rectangular map

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

## A matrix times a matrix computes several outputs at once

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

The row interpretation is equally useful. Row i of AB is
$\sum_{\ell}a_{i\ell}(\text{row }\ell\text{ of }B)$: the coefficients in a row
of A combine the rows of B. This and the column interpretation must agree with
all entrywise calculations.

## Summarize several sampler rows at once

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

## Composition: the rightmost map acts first

If B converts one input record to an intermediate record, and A converts that
record to the final output, then $A(B\mathbf x)=(AB)\mathbf x$.
In our sampler, S defines section groups and W records their contributions
across rows. The product WS is meaningful because the intermediate section
coordinates match. Always name and check that shared space.

For compatible dimensions, multiplication is **associative**:
$(AB)C=A(BC)$. It is **distributive**:
$(A+B)C=AC+BC$ and $A(B+C)=AB+AC$. These rules can be established by expanding
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

## Transposing a product reverses its order

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
