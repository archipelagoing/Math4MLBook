(w2-inverses-page)=
# Inverses and invertibility

<div class="chapter-kicker">Lecture 2 · Page 3 of 4 · Parts I–N</div>

A nonzero determinant tells us a square map can be undone. Now define its inverse,
test whether one exists, and compute it by elimination or cofactors, following
PDF pages 30–36.

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html"><span class="path-number">01</span><span>Systems & elimination</span></a>
<a href="elimination.html"><span class="path-number">02</span><span>Determinants & geometry</span></a>
<a href="inverses.html" aria-current="page"><span class="path-number">03</span><span>Inverses & invertibility</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Finish the lecture**

- {ref}`I · Matrix inverse <w2-inverse>`
- {ref}`J · Invertibility tests <w2-invertibility>`
- {ref}`K · Gauss–Jordan inverse <w2-inverse-elimination>`
- {ref}`L · Cofactor method <w2-cofactor-method>`
- {ref}`M · 2×2 inverse <w2-inverse-2>`
- {ref}`N · 3×3 inverse <w2-inverse-3>`
::::

(w2-inverse)=
## I · Matrix inverse

::::{div} section-intro

**Learning goal:** Define an inverse by multiplication and distinguish singular matrices.

<span class="source-label">Lecture PDF pages 30–31</span>
::::

:::{admonition} Definition · Inverse matrix
:class: definition

For square $A\in\mathbb R^{n\times n}$, its inverse $A^{-1}$ satisfies

$$\boxed{AA^{-1}=I_n=A^{-1}A}.$$

An inverse exists only for **invertible**, **regular**, or **nonsingular** matrices;
otherwise the matrix is **singular** or **noninvertible**. These are synonyms.
:::

If $A^{-1}$ exists, $A\mathbf x=\mathbf b$ has the unique solution
$\mathbf x=A^{-1}\mathbf b$: multiply on the left and use $A^{-1}A=I$.
For computation, elimination usually avoids forming the inverse explicitly.

:::::{admonition} Worked example 2.13 · Verify the lecture's inverse (p. 31)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read the proposed pair</span>

The slides give

$$Q=\begin{bmatrix}1&2&1\\4&4&5\\6&7&7\end{bmatrix},\qquad
B=\begin{bmatrix}-7&-7&6\\2&1&-1\\4&5&-4\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Multiply; do not invert entry by entry</span>

For instance, row 1 of $Q$ dotted with columns 1 and 2 of $B$ gives
$-7+4+4=1$ and $-7+2+5=0$. Completing all entries gives

$$QB=BQ=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}.$$

Thus $B=Q^{-1}$. Part N derives it rather than merely checking the answer.
::::
:::::

:::{admonition} Connection · Square inverse versus shadow reconstruction
:class: connection

The front-view matrix $O$ is $2\times3$ and the stacked-view matrix $H$ is
$4\times3$. Neither has a determinant or a two-sided inverse. Compatible $H$
readings can determine one point uniquely; this does not turn $H$ into a square map.
:::

:::{admonition} Check your understanding
:class: checkpoint

Is $A^{-1}$ obtained by replacing each entry with its reciprocal?
:::

:::{dropdown} Check your reasoning

No. It is a matrix whose products with $A$ are identity. The construction mixes entries; see Parts K–N.
:::

::::{div} section-recap

**Keep this:** An inverse undoes a square map; verify it with matrix multiplication.

**Practice:** {ref}`22 <w2-p22>` · {ref}`24 <w2-p24>` · {ref}`25 <w2-p25>`.
::::

(w2-invertibility)=
## J · Invertibility tests

::::{div} section-intro

**Learning goal:** Choose among determinant, pivots, and homogeneous-solution tests.

<span class="source-label">Lecture PDF pages 32</span>
::::

For a **square $n\times n$ matrix**, these statements are equivalent:

:::{admonition} Invertibility tests
:class: key-result

1. $A^{-1}$ exists.
2. $\det(A)\ne0$.
3. Elimination finds **$n$ pivots** in $A$; equivalently, $\operatorname{RREF}(A)=I_n$.
4. $A\mathbf x=\mathbf0$ has **only** the solution $\mathbf x=\mathbf0$.
:::

Why the last test? If an inverse exists, multiplying $A\mathbf x=0$ by it forces
$\mathbf x=0$. If a square matrix lacks a pivot, its homogeneous system instead
has a free variable and a nonzero solution. One test is enough; choose the easiest.

For the running system, Part F gave $\det(A)=-1\ne0$, agreeing with the three
pivots in Part D. Hence **every** right side has one solution.

:::{admonition} Pitfall · Singular does not always mean no solution
:class: pitfall

A singular square matrix cannot have a unique solution for $A\mathbf x=\mathbf b$.
Depending on $\mathbf b$, it can have no solution **or infinitely many**.
The homogeneous system always has the zero solution; the test asks whether it is the only one.
:::

:::{admonition} Check your understanding
:class: checkpoint

If a $3\times3$ matrix has only two pivots, can it have an inverse?
:::

:::{dropdown} Check your reasoning

No. One variable is free in the homogeneous system, so a nonzero input maps to zero and the transformation cannot be undone.
:::

::::{div} section-recap

**Keep this:** For square matrices: nonzero determinant ⇔ all pivots ⇔ only zero solves the homogeneous system.

**Practice:** {ref}`23 <w2-p23>` · {ref}`26 <w2-p26>`.
::::

(w2-inverse-elimination)=
## K · Gauss–Jordan elimination for the inverse

::::{div} section-intro

**Learning goal:** Apply row operations to two blocks and recognize the inverse endpoint.

<span class="source-label">Lecture PDF pages 33</span>
::::

To find an inverse, augment with **the identity**, not a vector of constants:

$$\boxed{[A\mid I_n]\ \longrightarrow\ [I_n\mid A^{-1}]}.$$

Every row operation acts on **both blocks**. The left block must actually become
$I_n$. If a pivot is missing, stop: $A$ is not invertible. The right block then
must not be reported as an inverse.

:::::{admonition} Worked example 2.14 · Find an inverse by Gauss–Jordan
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Attach the identity</span>

Use $C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$:

$$\left[\begin{array}{cc|cc}2&1&1&0\\1&1&0&1\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Swap to use a unit pivot</span>

Apply $R_1\leftrightarrow R_2$, updating both blocks:

$$\left[\begin{array}{cc|cc}1&1&0&1\\2&1&1&0\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 3 · Clear below the first pivot</span>

$R_2\leftarrow R_2-2R_1$ gives

$$\left[\begin{array}{cc|cc}1&1&0&1\\0&-1&1&-2\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 4 · Normalize the second pivot</span>

$R_2\leftarrow-R_2$ gives

$$\left[\begin{array}{cc|cc}1&1&0&1\\0&1&-1&2\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 5 · Clear above and read the inverse</span>

$R_1\leftarrow R_1-R_2$ gives

$$\left[\begin{array}{cc|cc}1&0&1&-1\\0&1&-1&2\end{array}\right].$$

The left is $I_2$, so the right is $C^{-1}$. Check:
$CC^{-1}=C^{-1}C=I_2$.
::::

::::{div} key-answer

**Keep this result:** $\boxed{C^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}}$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

What goes on the right when finding an inverse: $\mathbf b$ or $I_n$?
:::

:::{dropdown} Check your reasoning

$I_n$. A single $\mathbf b$ solves one system; $I_n$ tracks the inverse transformation for every coordinate direction.
:::

::::{div} section-recap

**Keep this:** For an inverse, turn the whole left block into identity and carry the right block along.

**Practice:** {ref}`24 <w2-p24>`.
::::

(w2-cofactor-method)=
## L · The cofactor method

::::{div} section-intro

**Learning goal:** Keep minor, cofactor, adjugate, and inverse in the correct order.

<span class="source-label">Lecture PDF pages 34</span>
::::

The lecture's second inverse method builds the answer from determinants:

1. **Minors:** $M_{ij}=\det(A_{\widehat i,\widehat j})$.
2. **Cofactors:** $C_{ij}=(-1)^{i+j}M_{ij}$; apply the checkerboard signs.
3. **Adjugate:** $\operatorname{adj}(A)=C^T$; transpose the cofactor matrix.
4. **Inverse:** if $\det(A)\ne0$,

   $$\boxed{A^{-1}=\frac{\operatorname{adj}(A)}{\det(A)}}.$$

:::{admonition} Why the formula works
:class: proof

$A\operatorname{adj}(A)=\det(A)I$: a diagonal entry is a Laplace expansion of
$\det(A)$, while an off-diagonal entry is the corresponding expansion with two
rows equal, hence zero. The column argument gives
$\operatorname{adj}(A)A=\det(A)I$ too. Dividing by a nonzero determinant proves both inverse identities.
:::

Do not confuse the **minor** (a determinant) with the **deleted submatrix** itself.
Parts M–N now carry out this recipe in two dimensions and three.

:::{admonition} Check your understanding
:class: checkpoint

Which matrix gets transposed before division by the determinant?
:::

:::{dropdown} Check your reasoning

The cofactor matrix, producing the adjugate. Transposing the minors before applying signs skips a required operation.
:::

::::{div} section-recap

**Keep this:** Minors → signs → transpose → divide, only when the determinant is nonzero.

**Practice:** {ref}`25 <w2-p25>`.
::::

(w2-inverse-2)=
## M · Inverse of a 2×2 matrix

::::{div} section-intro

**Learning goal:** Use the shortcut with its nonzero-determinant condition.

<span class="source-label">Lecture PDF pages 35</span>
::::

For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, the minors are
$\begin{bmatrix}d&c\\b&a\end{bmatrix}$, the cofactors are
$\begin{bmatrix}d&-c\\-b&a\end{bmatrix}$, and their transpose gives the shortcut:

:::{admonition} Formula · 2×2 inverse
:class: key-result

$$\boxed{A^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}},
\qquad ad-bc\ne0.$$
:::

:::::{admonition} Worked example 2.15 · Use the 2×2 shortcut
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Check the determinant first</span>

For $C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$,
$ad-bc=2(1)-1(1)=1\ne0$, so division is allowed.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Swap the diagonal; negate the off-diagonal</span>

The numerator is $\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$.
Divide every entry by 1. This agrees with Gauss–Jordan in Part K.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Verify by multiplication</span>

$CC^{-1}=\begin{bmatrix}2-1&-2+2\\1-1&-1+2\end{bmatrix}=I_2$;
the reverse product is also $I_2$.
::::

::::{div} key-answer

**Keep this result:** $C^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$. This shortcut is specifically for 2×2 matrices.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

What if $ad-bc=0$?
:::

:::{dropdown} Check your reasoning

The formula would divide by zero. No two-sided inverse exists; return to elimination to classify a particular system.
:::

::::{div} section-recap

**Keep this:** Check determinant, swap diagonal entries, negate off-diagonal entries, divide.

**Practice:** {ref}`22 <w2-p22>` · {ref}`23 <w2-p23>`.
::::

(w2-inverse-3)=
## N · Inverse of a 3×3 matrix

::::{div} section-intro

**Learning goal:** Build and check every intermediate matrix in the cofactor method.

<span class="source-label">Lecture PDF pages 36</span>
::::

Return to the lecture's $Q$ and proposed inverse from Part I. Here is the full
cofactor construction; these intermediate matrices are all retained from the slides.

:::::{admonition} Worked example 2.16 · The lecture's 3×3 inverse (p. 36)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compute the nine minors</span>

For $Q=\begin{bmatrix}1&2&1\\4&4&5\\6&7&7\end{bmatrix}$,
delete one row and one column per entry. For example,
$M_{12}=\begin{vmatrix}4&5\\6&7\end{vmatrix}=28-30=-2$.
All nine give

$$M=\begin{bmatrix}-7&-2&4\\7&1&-5\\6&1&-4\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Apply checkerboard signs</span>

Multiply entrywise by $\begin{bmatrix}+&-&+\\-&+&-\\+&-&+\end{bmatrix}$:

$$C_Q=\begin{bmatrix}-7&2&4\\-7&1&5\\6&-1&-4\end{bmatrix}.$$

In particular, $C_{12}=-(-2)=2$: a negative minor can yield a positive cofactor.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Transpose to form the adjugate</span>

Rows become columns:

$$\operatorname{adj}(Q)=C_Q^T=\begin{bmatrix}-7&-7&6\\2&1&-1\\4&5&-4\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 4 · Compute the determinant and divide</span>

Expand along row 1 using **cofactors**, so signs are already included:

$$\det(Q)=1(-7)+2(2)+1(4)=1.$$

Hence $Q^{-1}=\operatorname{adj}(Q)/1$. This completes the recipe without
an extra sign change.
::::

::::{div} worked-step

<span class="step-label">Step 5 · Check both products</span>

Multiplication yields $QQ^{-1}=Q^{-1}Q=I_3$, as verified in Part I.
This catches a forgotten transpose or a cofactor sign error.
::::

::::{div} key-answer

**Keep this result:** $\boxed{Q^{-1}=\begin{bmatrix}-7&-7&6\\2&1&-1\\4&5&-4\end{bmatrix}}$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Why does the lecture inverse equal the adjugate numerically?
:::

:::{dropdown} Check your reasoning

Because this example has determinant 1. In general, every adjugate entry must be divided by the determinant.
:::

::::{div} section-recap

**Keep this:** The adjugate is not automatically the inverse; division and a multiplication check finish the method.

**Practice:** {ref}`25 <w2-p25>`.
::::


(w2-practice-inverses)=
## Practice · inverses and invertibility

Try each problem before opening its explained answer directly below. Problem numbers
remain stable across the chapter; the questions here follow this page’s topics.

```{include} practice.md
:start-after: <!-- inverses:start -->
:end-before: <!-- inverses:end -->
```
(w2-readiness)=
## Readiness: can you choose the method?

| Task | Method | Practice |
| --- | --- | --- |
| Solve a system | $[A\mid\mathbf b]$ → REF → back substitution | {ref}`12 <w2-p12>`, {ref}`15 <w2-p15>` |
| Classify all solutions | Contradictions, then variable-column pivots | {ref}`16 <w2-p16>`, {ref}`18 <w2-p18>`, {ref}`23 <w2-p23>` |
| Compute a determinant | 2×2 formula, sparse Laplace, or elimination with bookkeeping | {ref}`19 <w2-p19>`–{ref}`20 <w2-p20>` |
| Interpret area/volume | Absolute determinant with the correct shape | {ref}`21 <w2-p21>` |
| Find an inverse | $[A\mid I]$ or the cofactor formula; verify both products | {ref}`22 <w2-p22>`, {ref}`24 <w2-p24>`–{ref}`25 <w2-p25>` |
| Test invertibility | Nonzero determinant, all pivots, or homogeneous uniqueness | {ref}`26 <w2-p26>` |

Before moving on, solve a fresh system, find an inverse without notes, and explain
why a singular system can still have solutions. Use the
{ref}`TL;DR cheat sheet <w2-cheatsheet>` to identify a missed step, then retry it unaided.

(w2-source-notes)=
## Sources and coverage

This chapter develops **all 36 PDF pages** of Erisa Terolli's CS 556 Week 2 slides,
`resources/lectures/WK2_SLE_Inverse_Determinants.pdf`, in Parts A–N. Title pages and
progressive reveals are combined; every mathematical topic and distinct slide
example is retained. Page references count from the PDF's first page.
The determinant and inverse topics on pp. 22–36 are fully included here.

Step explanations, checks, extra practice, geometric qualifications, and the
shadow scenes are editorial additions. Row scaling requires a **nonzero** factor.
The deleted-submatrix notation in Laplace expansion explicitly identifies the
correct removed row and column for each term. The slides' p. 33 Gauss–Jordan
schematic is explained with an original worked 2×2 reduction; no third-party
image is reproduced. Exact source destinations and checks are recorded in
`authoring/lecture2-coverage.md` and `authoring/lecture2-review.md`.

**Review:** [Page 4 · TL;DR cheat sheet](cheatsheet.md).
