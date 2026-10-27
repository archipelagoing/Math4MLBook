(w2-cheatsheet)=
# TL;DR cheat sheet

<div class="chapter-kicker">Lecture 2 · Page 4 of 4 · Review after the lecture</div>

**Exam route:** identify the task → choose the method → show legal steps → check.
Parts A–N in the three topic pages follow the full lecture; this page condenses
them into a working reference.

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html"><span class="path-number">01</span><span>Systems & elimination</span></a>
<a href="elimination.html"><span class="path-number">02</span><span>Determinants & geometry</span></a>
<a href="inverses.html"><span class="path-number">03</span><span>Inverses & invertibility</span></a>
<a href="cheatsheet.html" aria-current="page"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## 1 · Choose what you are trying to find

| Task | Start with | Stop when |
| --- | --- | --- |
| Multiply | Rows dotted with the input | Every output entry is computed |
| Solve $A\mathbf x=\mathbf b$ | $[A\mid\mathbf b]$ | All solutions are stated and checked |
| Find REF | Clear below pivots | Staircase; zero rows last |
| Find RREF | REF, then normalize/clear above | Each pivot is a lone 1 |
| Find a determinant | Square $A$ only | One scalar, with signs/scales accounted for |
| Find an inverse | $[A\mid I]$ or cofactors | $[I\mid A^{-1}]$; verify products |

## 2 · Keep these formulas and conditions

:::{admonition} Matrix-vector multiplication and elimination
:class: key-result

$$A\mathbf x=\sum_j x_j\mathbf a_j,\qquad (A\mathbf x)_i=\sum_j a_{ij}x_j.$$

To clear entry $c$ below pivot $a\ne0$ in row $k$:
$R_i\leftarrow R_i-(c/a)R_k$. Apply it to the **whole augmented row**.
Swap rows if the next pivot candidate is zero; if the remaining column is zero,
skip it. Row scaling must be nonzero.
:::

| After elimination | Solution case |
| --- | --- |
| $0=c$, $c\ne0$ | None |
| Consistent; pivot in every variable column | Unique |
| Consistent; a variable column without a pivot | Infinite; set free variables to real parameters |

:::{admonition} Determinants: formulas and bookkeeping
:class: key-result

$$\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc,\qquad
\det(A)=\sum_j a_{ij}(-1)^{i+j}\det(A_{\widehat i,\widehat j}).$$

Laplace: fix a row (or a column), delete its entry's row/column, apply the
checkerboard sign, multiply, and add. Choose many zeros when possible.

- $\det(I)=1$; a triangular determinant is the diagonal product.
- Swap rows: flip sign. Scale one row by $t$: multiply determinant by $t$.
- Add a multiple of another row: unchanged. Equal rows or a zero row: zero.
- $\det(AB)=\det(A)\det(B)$; $\det(A^T)=\det(A)$.
- Linear in **one row at a time**, not the entire matrix; $\det(tA)=t^n\det(A)$.
- $|\det|$ gives parallelogram area / parallelepiped volume, or scaling of area/volume.
:::

:::{admonition} Inverses: test before dividing
:class: key-result

For square $A$: inverse exists ⇔ $\det(A)\ne0$ ⇔ $n$ pivots ⇔ only zero solves $A\mathbf x=0$.

$$A^{-1}=\frac{\operatorname{adj}(A)}{\det(A)},\qquad
\operatorname{adj}(A)=\big[(-1)^{i+j}M_{ij}\big]^T.$$

**Cofactor recipe:** minors → checkerboard signs → transpose → divide.

$$\boxed{\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}
=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}},\qquad ad-bc\ne0.$$

**Elimination recipe:** $[A\mid I]\to[I\mid A^{-1}]$; operate on both blocks.
Check $AA^{-1}=A^{-1}A=I$. If invertible, $\mathbf x=A^{-1}\mathbf b$.
:::

## 3 · One complete example: solve, test, and check

:::::{admonition} Worked example 2.17 · A compact exam-style solve
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Write the system and augmented matrix</span>

Given $2x+y=5$, $x+y=3$, use

$$C=\begin{bmatrix}2&1\\1&1\end{bmatrix},\quad
\mathbf b=\begin{bmatrix}5\\3\end{bmatrix},\quad
\left[\begin{array}{cc|c}2&1&5\\1&1&3\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Swap to a unit pivot; eliminate below</span>

Apply $R_1\leftrightarrow R_2$, then $R_2\leftarrow R_2-2R_1$:

$$\left[\begin{array}{cc|c}1&1&3\\2&1&5\end{array}\right]
\longrightarrow\left[\begin{array}{cc|c}1&1&3\\0&-1&-1\end{array}\right].$$

This is REF. The bottom equation has only $y$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Back substitute; optionally finish RREF</span>

$-y=-1$ gives $y=1$; $x+y=3$ gives $x=2$.
If RREF is asked for, use $R_2\leftarrow-R_2$, then $R_1\leftarrow R_1-R_2$:

$$\left[\begin{array}{cc|c}1&0&2\\0&1&1\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 4 · Connect determinant and inverse</span>

$\det(C)=2(1)-1(1)=1\ne0$, so the solution is unique.
The 2×2 shortcut gives

$$C^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix},\qquad
C^{-1}\mathbf b=\begin{bmatrix}5-3\\-5+6\end{bmatrix}
=\begin{bmatrix}2\\1\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 5 · Check against the original problem</span>

$2(2)+1=5$ and $2+1=3$. The inverse check also gives
$CC^{-1}=C^{-1}C=I_2$.
::::

::::{div} key-answer

**Keep this result:** $\boxed{(x,y)=(2,1)}$. The system solve, determinant test, and inverse method agree.
::::
:::::

## 4 · Last-minute error check

:::{admonition} Avoid these lost marks
:class: pitfall

- Do not forget the augmented constant when changing a row.
- Do not call REF “RREF” while entries remain above pivots or a pivot is not 1.
- Do not infer “no solution” from a zero row or a singular matrix alone.
- Do not forget cofactor signs, the adjugate transpose, or determinant division.
- Do not take determinants or two-sided inverses of rectangular shadow-view matrices.
:::

**Use it actively:** close the example and try {ref}`Problem 24 <w2-p24>`.
For the full lecture's 3×3 solve, return to {ref}`Example 2.6 in Part D <w2-gaussian>`.
