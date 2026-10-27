(w2-elimination-page)=
# Determinants and geometry

<div class="chapter-kicker">Lecture 2 · Page 2 of 4 · Parts E–H</div>

After solving systems, the lecture asks what a square matrix preserves or collapses.
Follow determinant definitions, properties, Laplace expansion, and geometric uses
in PDF pages 22–29. Inverses follow on Page 3.

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html"><span class="path-number">01</span><span>Systems & elimination</span></a>
<a href="elimination.html" aria-current="page"><span class="path-number">02</span><span>Determinants & geometry</span></a>
<a href="inverses.html"><span class="path-number">03</span><span>Inverses & invertibility</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Continue in lecture order**

- {ref}`E · Determinants <w2-determinants>`
- {ref}`F · Determinant properties <w2-det-properties>`
- {ref}`G · Laplace expansion <w2-laplace>`
- {ref}`H · Applications <w2-det-applications>`
::::

(w2-determinants)=
## E · Determinants

::::{div} section-intro

**Learning goal:** Interpret determinant notation and compute the 2×2 case.

<span class="source-label">Lecture PDF pages 22–23</span>
::::

:::{admonition} Definition · Determinant
:class: definition

The **determinant** assigns a real number to a **square** matrix:
$\det(A)=|A|$. Vertical bars around a matrix mean determinant, not entrywise
absolute values. For $2\times2$,

$$\boxed{\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc}.$$
:::

A nonzero determinant means the square map preserves enough information to be
reversed. A zero determinant means it collapses at least one direction. The
sign records orientation; the absolute value records area/volume scaling.

:::::{admonition} Worked example 2.9 · Compute a 2×2 determinant
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Identify the diagonal products</span>

For $C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, use $a=2,b=1,c=1,d=1$.
The products are $ad=2$ and $bc=1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Subtract in the correct order</span>

$\det(C)=2(1)-1(1)=1$. Because this is nonzero, an inverse exists.
We will compute it in Parts K and M.
::::

::::{div} key-answer

**Keep this result:** $\det(C)=1$. The formula is $ad-bc$, not $ad+bc$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Does a $2\times3$ matrix have a determinant?
:::

:::{dropdown} Check your reasoning

No. The determinant here is defined only for square matrices.
:::

::::{div} section-recap

**Keep this:** Determinant: one number for a square matrix, with zero marking collapse.

**Practice:** {ref}`19 <w2-p19>` · {ref}`22 <w2-p22>`.
::::

(w2-det-properties)=
## F · Basic and derived determinant properties

::::{div} section-intro

**Learning goal:** Use determinant rules without losing a sign or scale factor.

<span class="source-label">Lecture PDF pages 24–25</span>
::::

### Basic properties (p. 24)

$\det(I_n)=1$. Swapping two rows reverses the sign. Scaling one row by $t$
scales the determinant by $t$. It is **linear in one row at a time**, with all
other rows held fixed:

$$\begin{vmatrix}ta&tb\\c&d\end{vmatrix}
=t\begin{vmatrix}a&b\\c&d\end{vmatrix},$$
$$\begin{vmatrix}a+a'&b+b'\\c&d\end{vmatrix}
=\begin{vmatrix}a&b\\c&d\end{vmatrix}
+\begin{vmatrix}a'&b'\\c&d\end{vmatrix}.$$

### Derived properties (p. 25)

| Property | What to use |
| --- | --- |
| Two equal rows or a zero row | $\det(A)=0$ |
| Add a multiple of another row | Determinant unchanged |
| Upper or lower triangular matrix | $\det(A)=\prod_i a_{ii}$ |
| Same-size square product | $\det(AB)=\det(A)\det(B)$ |
| Transpose | $\det(A^T)=\det(A)$ |
| Invertible versus singular | Invertible iff $\det(A)\ne0$; singular iff $\det(A)=0$ |

The corresponding column statements follow by transposing. For an invertible
matrix, $\det(A^{-1})=1/\det(A)$ by applying the product rule to $AA^{-1}=I$.

:::{admonition} Why row addition leaves the determinant unchanged
:class: proof

Linearity splits the changed row into the original row plus a multiple of another
row. The added determinant has two equal rows, so that added term is zero.
:::

:::::{admonition} Worked example 2.10 · Use elimination to compute a determinant
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Make the coefficient matrix triangular</span>

For the running system's $A$, subtract row 1 from rows 2 and 3:

$$A=\begin{bmatrix}1&1&3\\1&2&4\\1&1&2\end{bmatrix}
\longrightarrow U=\begin{bmatrix}1&1&3\\0&1&1\\0&0&-1\end{bmatrix}.$$

These row additions leave the determinant unchanged. Compute a determinant of
**$A$**, not of the rectangular augmented array.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Multiply the diagonal and account for operations</span>

$\det(A)=\det(U)=1\cdot1\cdot(-1)=-1$.
If you had swapped $s$ rows or scaled rows by nonzero factors $t_1,\ldots,t_k$,
then $\det(U)=(-1)^s(t_1\cdots t_k)\det(A)$: undo those effects.
::::

::::{div} key-answer

**Keep this result:** Row addition is determinant-preserving; row swaps and scaling require bookkeeping.
::::
:::::

:::{admonition} Pitfall · Not linear in the whole matrix
:class: pitfall

In general, $\det(A+B)\ne\det(A)+\det(B)$. Scaling every row gives
$\det(tA)=t^n\det(A)$ for an $n\times n$ matrix, not merely $t\det(A)$.
Row operations preserve **solutions** when applied to an augmented system;
only row addition automatically preserves its coefficient determinant.
:::

:::{admonition} Check your understanding
:class: checkpoint

If a row swap gives a triangular matrix with diagonal $2,3,-1$, what was the original determinant?
:::

:::{dropdown} Check your reasoning

The triangular determinant is $-6$. One swap reverses the sign, so the original determinant was 6.
:::

::::{div} section-recap

**Keep this:** Track swaps and row scales; then use the triangular diagonal product.

**Practice:** {ref}`19 <w2-p19>` · {ref}`20 <w2-p20>`.
::::

(w2-laplace)=
## G · Laplace expansion

::::{div} section-intro

**Learning goal:** Compute a determinant from correctly signed minors.

<span class="source-label">Lecture PDF pages 26–28</span>
::::

Delete row $i$ and column $j$ to obtain the submatrix $A_{\widehat i,\widehat j}$.
Its determinant is the **minor** $M_{ij}$; the signed minor is the **cofactor**
$C_{ij}=(-1)^{i+j}M_{ij}$. The sign grid begins
$\begin{bmatrix}+&-&+\\-&+&-\\+&-&+\end{bmatrix}$.

:::{admonition} Formula · Expand along one fixed row or column
:class: key-result

**Row $i$:** $\displaystyle\det(A)=\sum_{j=1}^n a_{ij}(-1)^{i+j}\det(A_{\widehat i,\widehat j})$.

**Column $j$:** $\displaystyle\det(A)=\sum_{i=1}^n a_{ij}(-1)^{i+j}\det(A_{\widehat i,\widehat j})$.

Choose a row or column with many zeros. Every deleted submatrix is $(n-1)\times(n-1)$.
:::

:::::{admonition} Worked example 2.11 · The lecture's Laplace expansion (pp. 27–28)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Choose row 1 and its signs</span>

For $D=\begin{bmatrix}1&2&3\\3&1&2\\0&0&1\end{bmatrix}$,
row 1 has signs $+,-,+$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Delete the row and column for each entry</span>

The three minors are

$$M_{11}=\begin{vmatrix}1&2\\0&1\end{vmatrix}=1,\quad
M_{12}=\begin{vmatrix}3&2\\0&1\end{vmatrix}=3,\quad
M_{13}=\begin{vmatrix}3&1\\0&0\end{vmatrix}=0.$$
::::

::::{div} worked-step

<span class="step-label">Step 3 · Multiply entry × signed minor, then add</span>

$\det(D)=1(1)-2(3)+3(0)=-5$.
Check along row 3 instead: its only nonzero term is
$1\begin{vmatrix}1&2\\3&1\end{vmatrix}=1-6=-5$.
::::

::::{div} key-answer

**Keep this result:** $\boxed{\det(D)=-5}$. A sparse row gives the same result with less work.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

What sign multiplies the minor at position $(2,3)$?
:::

:::{dropdown} Check your reasoning

$(-1)^{2+3}=-1$. The cofactor changes the sign of that minor; the minor itself may already be negative.
:::

::::{div} section-recap

**Keep this:** Fix one row or column; delete, sign, multiply, add.

**Practice:** {ref}`20 <w2-p20>` · {ref}`25 <w2-p25>`.
::::

(w2-det-applications)=
## H · Determinant applications

::::{div} section-intro

**Learning goal:** Connect determinant magnitude to geometry and nonzero determinant to inversion.

<span class="source-label">Lecture PDF pages 29</span>
::::

For a square matrix whose columns are edge vectors, $|\det(A)|$ is the area of
the spanned parallelogram in 2D or volume of the parallelepiped in 3D. Applied
to a region, it is the factor by which the linear map scales area or volume.
The sign distinguishes preserved from reversed orientation.

:::::{admonition} Worked example 2.12 · Interpret the lecture determinant geometrically
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Use the correct shape and dimension</span>

The three columns of $D$ in Part G span a parallelepiped in $\mathbb R^3$,
not an arbitrary solid or a triangle.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Take the absolute value for volume</span>

Since $\det(D)=-5$, that parallelepiped has volume $5$.
The negative sign indicates reversed orientation; volume itself is not negative.
A triangle formed from two 2D edges has area $\tfrac12|\det(A)|$.
::::

::::{div} key-answer

**Keep this result:** Use $|\det|$ for area/volume; keep the sign when orientation matters.
::::
:::::

In the shadow scene, apply $C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$ to a
front-screen coordinate record. Its determinant 1 preserves screen area, and
its inverse can undo this coordinate mixing. It cannot recover depth that the
front view never recorded.

The second application is **inversion**: an inverse requires $\det(A)\ne0$.
The inverse formula divides the **adjugate**, not the original matrix, by that
number. We now build that method in the lecture's order.

:::{admonition} Check your understanding
:class: checkpoint

If a 2D transformation has determinant $-3$, what happens to an area of 4?
:::

:::{dropdown} Check your reasoning

Its image has area $|-3|\cdot4=12$, and orientation reverses.
:::

::::{div} section-recap

**Keep this:** Absolute determinant measures geometric scaling; nonzero determinant permits inversion.

**Practice:** {ref}`21 <w2-p21>`.
::::


(w2-practice-determinants)=
## Practice · determinants and geometry

Try each problem before opening its explained answer directly below. Problem numbers
remain stable across the chapter; the questions here follow this page’s topics.

```{include} practice.md
:start-after: <!-- determinants:start -->
:end-before: <!-- determinants:end -->
```

**Next:** [Page 3 · Inverses and invertibility](inverses.md).
