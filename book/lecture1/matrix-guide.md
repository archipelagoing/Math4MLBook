(w1-matrix-guide)=
# Matrices and products

<div class="chapter-kicker">Lecture 1 · Page 3 of 4 · Organize observations, then compare views</div>

One point or one measurement profile gave us a vector. Recording several
configurations gives a matrix; placing screen-axis responses in its rows gives
a map from a point to its measurements. Keep those two uses of a matrix distinct.

<nav class="lecture-path" aria-label="Lecture 1 learning path">
<a href="index.html"><span class="path-number">01</span><span>Vectors & combinations</span></a>
<a href="geometry.html"><span class="path-number">02</span><span>Dot products & geometry</span></a>
<a href="matrix-guide.html" aria-current="page"><span class="path-number">03</span><span>Matrices & products</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

:::{admonition} What you will understand
:class: key-result

By the end of this page, you should be able to:

1. Read matrix entries/shapes and recognize the special structures in the lecture.
2. Add and scale matrices, transpose them, and compute a square matrix's trace.
3. Multiply using rows and columns, explain the output, and verify dimensions.
4. Distinguish associativity from changing factor order.
:::

::::{div} page-roadmap

**On this page**

- {ref}`1.7 · Matrix records <w1-matrices>`
- {ref}`1.8 · Special matrices <w1-special-matrices>`
- {ref}`1.9 · Matrix arithmetic <w1-matrix-arithmetic>`
- {ref}`1.10 · Transpose and trace <w1-transpose-trace>`
- {ref}`1.11 · Matrix-vector products <w1-products>`
- {ref}`1.12 · Matrix products and properties <w1-matrix-products>`
::::

(w1-matrices)=
## 1.7 Matrix records and dimensions

::::{div} section-intro

**Learning goal:** Read an entry and distinguish rows, columns, and shape.

<span class="source-label">Lecture pages 35–36</span>

Recording the same four beads in several configurations gives two index roles.
Which selects the configuration, and which selects the bead?
::::


One horizontal profile is a vector. Recording four configurations, alternating
r and s, gives a data matrix:

$$
W=\begin{bmatrix}
3&1&3&1\\
1&3&1&3\\
3&1&3&1\\
1&3&1&3
\end{bmatrix}.
$$

Here a row selects a configuration and a column selects one labeled bead A–D.
The entry $w_{23}=1$ means bead C has X=1 in configuration 2. It is a
horizontal measurement, not a complete three-dimensional position.

### Dimensions and entries

:::{admonition} Definition 1.5 · Real matrix
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

W happens to have four configurations and four beads, so it is square.
Recording three configurations would give a $3\times4$ matrix. Square shape
describes the numerical table, not the shape or dimensions of the physical frame.

The order **rows by columns** matters. A $2\times3$ matrix and a $3\times2$
matrix contain the same number of entries but usually represent different maps.
Write dimensions before multiplying them.



:::{admonition} Check your understanding
:class: checkpoint

A matrix has three rows and four columns. What is its shape, where is $a_{24}$, and is it square?
:::

:::{dropdown} Check your reasoning

Its shape is $3\times4$; $a_{24}$ is row 2, column 4. It is not square because 3 and 4 differ.
:::

::::{div} section-recap

**Keep this:** An m-by-n matrix has m rows and n columns; entry ij selects row i, column j.

**Try it yourself:** {ref}`Problem 6 <w1-p06>` · {ref}`Problem 13 <w1-p13>`.
::::

(w1-special-matrices)=
## 1.8 Diagonal, identity, symmetric, and skew-symmetric matrices

::::{div} section-intro

**Learning goal:** Classify a matrix by its entries and transpose relation.

<span class="source-label">Lecture pages 37–39</span>

A regular-looking arrangement of point marks can suggest a pattern, but a
special-matrix claim needs an exact test on the numerical array.
::::
:::{admonition} Definition 1.6 · Four special matrix structures
:class: definition

| Structure | Exact test for a real square matrix |
| --- | --- |
| Diagonal | $a_{ij}=0$ whenever $i\ne j$ |
| Identity | Diagonal entries are 1; all other entries are 0 |
| Symmetric | $A^T=A$ |
| Skew-symmetric | $A^T=-A$ |

Apply the definition to the entries; visual regularity alone is not a test.
:::

### Diagonal and identity matrices

A square **diagonal matrix** has zero off-diagonal entries. Its diagonal entries
can be any real numbers, including zero:

$$D=\operatorname{diag}(3,5,8)=\begin{bmatrix}3&0&0\\0&5&0\\0&0&8\end{bmatrix}.$$

A diagonal matrix scales individual coordinates without mixing them. In a
four-bead profile, $\operatorname{diag}(2,1,2,1)$ doubles the X coordinates of
A and C while leaving B and D unchanged. It scales recorded coordinates; it is
not necessarily a rigid movement of the whole frame.

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
underlying point configuration is physically mirror-symmetric.

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
Do not infer them from a picture alone. A point-coordinate table, a table of
observations, and an observation map encode different things.
:::



:::{admonition} Check your understanding
:class: checkpoint

Which labels apply to the $2\times2$ zero matrix: diagonal, identity, symmetric, skew-symmetric?
:::

:::{dropdown} Check your reasoning

It is diagonal, symmetric, and skew-symmetric: $0^T=0=-0$. It is not identity, whose diagonal entries must be 1.
:::

::::{div} section-recap

**Keep this:** Test the array against its definition; an arrangement of marks or a zero diagonal alone is insufficient.

**Try it yourself:** {ref}`Problem 8 <w1-p08>` · {ref}`Problem 17 <w1-p17>`.
::::

(w1-matrix-arithmetic)=
## 1.9 Matrix addition and scalar multiplication

::::{div} section-intro

**Learning goal:** Compute entrywise operations while preserving the matrix shape.

<span class="source-label">Lecture pages 40–41</span>

Adding matching displacement records combines corresponding movements. This
operation is entrywise; it does not use the row-by-column rule for products.
::::
### Addition and scaling remain entrywise

If A and B have the same shape,

$$
(A+B)_{ij}=a_{ij}+b_{ij},\qquad (cA)_{ij}=ca_{ij}.
$$

Adding two displacement tables combines entries only when configuration and bead
labels agree. Adding arbitrary photographs is not the operation defined here.
As with vectors, state the coordinate meaning before interpreting an array sum.

:::{admonition} Worked example 1.8 · Arithmetic before interpretation
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



:::{admonition} Check your understanding
:class: checkpoint

For $Y=\begin{bmatrix}1&-2\\0&3\end{bmatrix}$, find $-2Y$. What happens to its shape?
:::

:::{dropdown} Check your reasoning

$-2Y=\begin{bmatrix}-2&4\\0&-6\end{bmatrix}$. Every entry is scaled and the shape remains $2\times2$; no row-column products are taken.
:::

::::{div} section-recap

**Keep this:** Add equally shaped matrices entrywise; scalar multiplication changes every entry.

**Try it yourself:** {ref}`Problem 7 <w1-p07>`.
::::

(w1-transpose-trace)=
## 1.10 Transpose and matrix trace

::::{div} section-intro

**Learning goal:** Swap the index roles and compute the diagonal sum when it is defined.

<span class="source-label">Lecture pages 42–43</span>

A transpose reorganizes the same entries. A trace selects a particular set
of entries. Keeping those operations distinct prevents a common exam mistake.
::::
### Transpose swaps the index roles

The transpose $A^T$ has entries $(A^T)_{ji}=a_{ij}$. Thus an $m\times n$ matrix
becomes $n\times m$: its rows become columns and its columns become rows.

:::{admonition} Worked example 1.9 · The lecture's transpose
:class: example

1. For $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, make its first row the first column:
   $A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}$.
2. Check an off-diagonal entry: $a_{12}=2$ becomes $(A^T)_{21}=2$.
The shape remains $2\times2$ here. The rectangular example below shows that
transposition also works when the row and column counts differ.
:::

For an additional rectangular example

$$
R=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix},\qquad
R^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.
$$

The entry 5 stays at $(2,2)$; the entry 3 moves from
$(1,3)$ to $(3,1)$. Following entries is more reliable than memorizing a motion.
For a column vector, $\mathbf v^T$ is a row, so
$(1\times n)(n\times1)$ explains why $\mathbf u^T\mathbf v$ is a scalar.

In W, transposition changes “beads within one configuration” to “configurations
for one bead.” Its numerical array happens to equal its transpose, but the index
meanings still differ. Transpose does not physically turn the scene around and is
not generally an inverse observation map.

Useful identities follow from the indices:

$$
(A^T)^T=A,\qquad (A+B)^T=A^T+B^T,\qquad (cA)^T=cA^T.
$$

We will derive the reversed-order identity for a product in the next section.

### Trace: sum of the diagonal

For a square $n\times n$ matrix,

$$\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}.$$

:::{admonition} Worked example 1.10 · The lecture's trace
:class: example

1. **Check the shape:** S from {ref}`Section 1.8 <w1-special-matrices>` is square.
2. **Select the main diagonal:** its entries are 3, 5, and 8.
3. **Add:** $\operatorname{tr}(S)=3+5+8=16$.

The off-diagonal entries do not enter this sum.
:::

For W the trace is $3+3+3+3=12$.
The sum of all recorded X coordinates is instead 32. Trace, whole-table sum,
and matrix size are different quantities. The diagonal selects configuration/bead
positions with equal numeric indices; it is not a physical length of the frame.

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


::::{div} section-recap

**Keep this:** Transpose swaps index roles; trace adds a square matrix’s main diagonal.

**Try it yourself:** {ref}`Problem 6 <w1-p06>` · {ref}`Problem 17 <w1-p17>`.
::::

(w1-products)=
## 1.11 Matrix-vector multiplication

::::{div} section-intro

**Learning goal:** Interpret a matrix-vector product as a combination of column effects.

<span class="source-label">Lecture pages 44–45</span>

Start with the point’s X,Y,Z coordinates. Which changes move its front mark?
The columns of the view map record the effect of each coordinate separately.
::::


A table becomes especially powerful when its columns are effects we can combine.
The lecture's column interpretation of multiplication and its row-by-column
calculation are two views of the **same operation**. Learn both: one explains
the meaning, and the other supplies a reliable calculation.

### A matrix times a vector combines columns

The front screen records X and Y, so its ideal coordinate map is

$$
O=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix},\qquad
\mathbf p=\begin{bmatrix}2\\3\\4\end{bmatrix}.
$$

Reading the product by columns gives

$$
O\mathbf p
=2\begin{bmatrix}1\\0\end{bmatrix}
+3\begin{bmatrix}0\\1\end{bmatrix}
+4\begin{bmatrix}0\\0\end{bmatrix}
=\begin{bmatrix}2\\3\end{bmatrix}.
$$

The input has **three world coordinates**; the output has **two screen coordinates**.
The third column is zero: moving in Z alone changes neither front-screen reading.
This is the opening scene expressed as a matrix-vector product.

:::{admonition} Key result 1.2 · Column interpretation
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
$(A\mathbf x)_i=\sum_{j=1}^n a_{ij}x_j$. For O, the first output is
$1\cdot2+0\cdot3+0\cdot4=2$ and the second is
$0\cdot2+1\cdot3+0\cdot4=3$. Rows and columns organize the same computation.

```{figure} ../figures/lecture1/shadow-map.svg
:name: fig-w1-view-map
:alt: The three world coordinates 2,3,4 multiply the front-view map O to give the screen coordinates 2,3. Its column effects are (1,0), (0,1), and (0,0); a Z change is invisible to this view.

Name both spaces: O maps a **three-dimensional point** to a **two-dimensional mark**.
Its zero third column explains why this particular view does not retain depth.
```

### From the lecture's directions to a rectangular map

:::{admonition} Worked example 1.11 · The lecture's matrix-vector map
:class: example

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
columns.
:::

Although L is square, an observation map need not be. The front map O is $2\times3$.
Add a side view that records Y,Z and stack both views:

$$
H=\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix},\qquad
H\begin{bmatrix}2\\3\\4\end{bmatrix}
=\begin{bmatrix}2\\3\\3\\4\end{bmatrix}.
$$

The four outputs mean front X,Y followed by side Y,Z. The Y coordinate appears
twice because the two views share it. These are **four measurements of a
three-dimensional point**, not four spatial coordinates of one point. Later we
will ask which additional measurements contribute genuinely new information.

:::{admonition} Check your understanding
:class: checkpoint

For $\mathbf p=(5,-2,7)^T$, compute $O\mathbf p$.
Would changing only Z from 7 to 10 change the front mark?
:::

:::{dropdown} Check your reasoning

$O\mathbf p=(5,-2)^T$. Changing Z alone leaves this output unchanged because
O’s third column is zero. The negative Y is a valid signed screen coordinate.
:::

::::{div} section-recap

**Keep this:** The entries of x weight the columns of A; a row computes one output coordinate.

**Try it yourself:** {ref}`Problem 15 <w1-p15>` · {ref}`Problem 24 <w1-p24>`.
::::

(w1-matrix-products)=
## 1.12 Matrix products, composition, and properties

::::{div} section-intro

**Learning goal:** Multiply compatible matrices, explain rows and columns, and preserve factor order.

<span class="source-label">Lecture pages 46–48</span>

Once one input vector can be transformed, a matrix of input vectors lets us
transform several at once. The same multiplication rule then describes composition.
::::

### Several outputs at once

If B contains several input vectors as columns, multiplying A by B applies A to
each one:

$$A[\mathbf b_1\ \cdots\ \mathbf b_k]
=[A\mathbf b_1\ \cdots\ A\mathbf b_k].$$

This observation determines the shape rule:

:::{admonition} Definition 1.7 · Matrix product
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

:::{admonition} Worked example 1.12 · The lecture's product
:class: example

$$
A=\begin{bmatrix}1&2&3\\3&2&1\end{bmatrix},\qquad
B=\begin{bmatrix}0&2\\1&1\\0&1\end{bmatrix}.
$$

1. **Check the shapes:** $(2\times3)(3\times2)$ gives a $2\times2$ result.
2. **Compute each row-column pairing:**

   $$
   \begin{aligned}
   (AB)_{11}&=1\cdot0+2\cdot1+3\cdot0=2,\\
   (AB)_{12}&=1\cdot2+2\cdot1+3\cdot1=7,\\
   (AB)_{21}&=3\cdot0+2\cdot1+1\cdot0=2,\\
   (AB)_{22}&=3\cdot2+2\cdot1+1\cdot1=9.
   \end{aligned}
   $$

3. **Assemble:** $AB=\begin{bmatrix}2&7\\2&9\end{bmatrix}$.
4. **Check by columns:** the first B column is $(0,1,0)^T$, so the first product
   column must equal A's second column, $(2,2)^T$. It does.
:::

The row interpretation is equally useful:

$$\operatorname{row}_i(AB)=\operatorname{row}_i(A)B
=\sum_{\ell=1}^{n}a_{i\ell}\operatorname{row}_{\ell}(B).$$

The coefficients in row i of A combine the rows of B. This and the column interpretation must agree with
all entrywise calculations.

### Summarize several point profiles at once

The four-configuration data matrix is

$$W=\begin{bmatrix}3&1&3&1\\1&3&1&3\\3&1&3&1\\1&3&1&3\end{bmatrix}.$$

Let e be the four-entry all-ones vector. Then $W\mathbf e=(8,8,8,8)^T$ gives
the sum of X coordinates within each configuration. In contrast,
$W^T\mathbf e=(8,8,8,8)^T$ sums each bead’s X coordinate across configurations.
The numbers coincide here;
the questions are still different.

To sum the A/B and C/D bead coordinates separately, use

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
Here S defines bead groups and W records their coordinates across configurations.
The product WS is meaningful because the intermediate bead coordinates match.
Grouping is a further summary of the front-view record; it does not recover depth.

:::{admonition} Key result 1.3 · Multiplication properties
:class: key-result

- **Associativity:** $(AB)C=A(BC)$ for A $m\times n$, B $n\times p$, C $p\times q$.
- **Left distributivity:** $(A+B)C=AC+BC$.
- **Right distributivity:** $A(C+D)=AC+AD$.
- **Identity:** $I_mA=A=AI_n$ for A $m\times n$.

In the distributive identities, A,B are $m\times n$ and C,D are $n\times p$.
These follow by expanding {eq}`eq-w1-product` and regrouping finite scalar sums.
:::

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
to an observation device. With rectangular matrices, one order may not exist at all.

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


::::{div} section-recap

**Keep this:** Match inner dimensions, compute row-column products, and keep the factor order.

**Try it yourself:** {ref}`Problem 14 <w1-p14>` · {ref}`Problem 16 <w1-p16>` · {ref}`Problem 20 <w1-p20>`.
::::

(w1-review)=
## Chapter synthesis · From a point to its observations

**Record → combine → compare → organize → observe.** The same marked points
connect all five steps: coordinates give vectors; displacement patterns give
combinations; dot products give geometry; profiles form data matrices; screen
axes define observation maps. Each map determines what its output can distinguish.

:::{admonition} Four checks before handing in
:class: key-result

1. **Object:** should the output be a scalar, vector, or matrix?
2. **Shape and conditions:** do dimensions match; are normalization/angle inputs nonzero?
3. **Method:** is this entrywise arithmetic, a dot product, or row-by-column multiplication?
4. **Verification:** substitute coefficients, check a column, or test the defining relation.
:::

### Can you do this unaided?

- [ ] Read vector/matrix coordinates and state what their indices mean.
- [ ] Test a linear-combination claim, including an impossible target.
- [ ] Compute and distinguish dot products, norms, unit directions, and angles.
- [ ] Recognize diagonal, identity, symmetric, and skew-symmetric matrices.
- [ ] Compute matrix arithmetic, transpose, trace, and compatible products.
- [ ] Explain why changing parentheses differs from changing factor order.

### Choose a practice route

| Skill to check | Independent practice |
| --- | --- |
| Vector records and arithmetic | {ref}`1 <w1-p01>`, {ref}`2 <w1-p02>` |
| Linear combinations | {ref}`3 <w1-p03>`, {ref}`9 <w1-p09>`, {ref}`10 <w1-p10>` |
| Dot products, norms, and angles | {ref}`4 <w1-p04>`, {ref}`5 <w1-p05>`, {ref}`11 <w1-p11>`, {ref}`12 <w1-p12>` |
| Matrix shape and structure | {ref}`6 <w1-p06>`, {ref}`8 <w1-p08>`, {ref}`13 <w1-p13>`, {ref}`17 <w1-p17>` |
| Matrix arithmetic and products | {ref}`7 <w1-p07>`, {ref}`14 <w1-p14>`, {ref}`15 <w1-p15>`, {ref}`16 <w1-p16>` |
| Fresh mixed reasoning | {ref}`19–24 <w1-p19>` on the exercises page |

Try the {ref}`practice below <w1-practice-matrices>` before opening its answers.
For a missed skill, revisit its explanation, retry without the answer, and then
attempt a changed problem. In Lecture 2, the question becomes: which input x
produces a given output b in $A\mathbf x=\mathbf b$?

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

The shadow/point records, four original diagrams, checkpoints, and practice are added
teaching material. Source pages were checked visually where text extraction
reordered coordinates. In particular, the addition uses $(0,2)^T$, the vector
outside the lecture's plane is $(1,2,3)^T$, and the lecture product has rows $(2,7)$
and $(2,9)$. These are transcription checks, not claims of source errors.

The analogy uses ideal parallel-ray views of matched labeled points, with fixed
calibrated axes and a declared common origin. The front map O retains X,Y; the
side map retains Y,Z. It does not reconstruct arbitrary solid objects from
silhouettes, unknown correspondences, occlusion, or perspective photographs.
A four-bead X profile is a separate record in $\mathbb R^4$, not a single point in
four-dimensional physical space. Record-space normalization/angles need not equal
an object's physical size/orientation. Adding displacement records does not claim
that moving a coordinate origin is a linear map.

The synthesis exercises on symmetric/skew parts and trace(AB)=trace(BA) extend the
lecture using definitions already taught. No physical camera experiment or
independent learner validation is claimed.

(w1-practice-matrices)=
## Practice · matrices and products

Try each problem before opening its explained answer directly below. Problem numbers
remain stable across the chapter; the questions here follow this page’s topics.

```{include} practice.md
:start-after: <!-- matrices:start -->
:end-before: <!-- matrices:end -->
```

**Review:** [Page 4 · TL;DR cheat sheet](cheatsheet.md).
