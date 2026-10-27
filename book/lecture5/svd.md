(w5-svd)=
# Singular value decomposition

<div class="chapter-kicker">Lecture 5 · Page 2 of 4 · Find directions, separate strengths, keep what matters</div>

Eigenvectors compare inputs and outputs in the same coordinate space. SVD uses a separate orthonormal basis on each side: **choose input directions, stretch them by nonnegative amounts, and express the results in output directions**. It exists even when ordinary diagonalization fails.

<nav class="lecture-path" aria-label="Lecture 5 learning path">
<a href="index.html"><span class="path-number">01</span><span>Eigenvalues & diagonalization</span></a>
<a href="svd.html" aria-current="page"><span class="path-number">02</span><span>Singular value decomposition</span></a>
<a href="applications.html"><span class="path-number">03</span><span>Reduction & recommendations</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

Recall {ref}`orthonormal columns <w4-orthonormal-vectors>`: $Q^TQ=I$, while $QQ^T$ is generally a projector if $Q$ is rectangular. That distinction determines which SVD factors have inverses.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`F · What the SVD means <w5-svd-meaning>`
- {ref}`G · Computing the factors <w5-svd-compute>`
::::

(w5-svd-meaning)=
## F · What the SVD means

::::{div} section-intro

**Learning goal:** Track factor dimensions and connect singular directions to the four spaces.

<span class="source-label">Lecture PDF pages 23–25</span>
::::

:::{admonition} Definition · Full and compact SVD
:class: definition

Every real $A\in\mathbb R^{m\times n}$ has a **full SVD**

$$\boxed{A=U\Sigma V^T}.$$

Here $U$ is $m\times m$ orthogonal, $V$ is $n\times n$ orthogonal, and $\Sigma$ is $m\times n$, with nonnegative diagonal entries and zeros elsewhere. The singular values are ordered $\sigma_1\ge\cdots\ge\sigma_p\ge0$, where $p=\min(m,n)$; exactly $r=\operatorname{rank}(A)$ are positive.

The **compact, rank-$r$ SVD** keeps only the positive directions:

$$A=U_r\Sigma_rV_r^T=\sum_{i=1}^r\sigma_i\mathbf u_i\mathbf v_i^T,$$

with sizes $m\times r$, $r\times r$, $r\times n$. Thus
$A\mathbf v_i=\sigma_i\mathbf u_i$ for $1\le i\le r$. Compact factors have orthonormal columns but are generally rectangular; do not write $V_r^{-1}$.
Some sources call the $p$-column form “reduced” or “thin”: it retains zero singular values when $r<p$. Here **compact** always means $r$ positive directions.
:::

```{figure} ../figures/lecture5/svd-geometry.svg
:alt: A unit circle in input space maps through a matrix to an ellipse in output space. Unit directions v1,v2 map to perpendicular output axes sigma1 u1,sigma2 u2.

A labeled reconstruction of the circle-to-ellipse picture on page 25. The singular values are nonnegative stretch lengths; left and right directions can differ.
```

:::{admonition} Read the product from right to left
:class: key-result

$V^T$ takes input components in the right-singular basis; $\Sigma$ scales them; $U$ expresses the output in the left-singular basis. In the full SVD:

| Directions | Space they span |
| --- | --- |
| $\mathbf v_1,\ldots,\mathbf v_r$ | Row space $C(A^T)$ |
| $\mathbf v_{r+1},\ldots,\mathbf v_n$ | Null space $N(A)$ |
| $\mathbf u_1,\ldots,\mathbf u_r$ | Column space $C(A)$ |
| $\mathbf u_{r+1},\ldots,\mathbf u_m$ | Left null space $N(A^T)$ |

Only the first $r$ columns span the row/column spaces. The remaining columns complete the ambient-space bases, correcting the unrestricted basis labels in the source’s full-SVD picture.
:::

```{figure} ../figures/lecture5/factor-shapes.svg
:alt: Full A m by n equals U m by m times Sigma m by n times V transpose n by n. Compact factors have inner size r; truncation replaces r by k and approximates A.

Full and compact factor shapes are shown together so the square and rectangular conventions cannot be mixed. Page 3 shows the corresponding truncated factors.
```

:::::{admonition} Worked example 5.8 · Singular directions of the two-view shadow map
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State the complete measurement model</span>

$$H=\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix},\qquad
H(X,Y,Z)^T=(X,Y,Y,Z)^T.$$

$H^TH=\operatorname{diag}(1,2,1)$, so choose ordered right directions $\mathbf v_1=\mathbf e_Y$, $\mathbf v_2=\mathbf e_X$, $\mathbf v_3=\mathbf e_Z$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Pair each direction with its output</span>

$$\begin{aligned}
\sigma_1&=\sqrt2,&\mathbf u_1&=(0,1,1,0)^T/\sqrt2,\\
\sigma_2&=1,&\mathbf u_2&=(1,0,0,0)^T,\\
\sigma_3&=1,&\mathbf u_3&=(0,0,0,1)^T.
\end{aligned}$$

Check $H\mathbf v_1=\sqrt2\mathbf u_1$, $H\mathbf v_2=\mathbf u_2$, $H\mathbf v_3=\mathbf u_3$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Complete the full output basis</span>

Choose $\mathbf u_4=(0,1,-1,0)^T/\sqrt2$. It satisfies $H^T\mathbf u_4=0$ and is perpendicular to the other three unit columns.
Full shapes are $U:4\times4$, $\Sigma:4\times3$, $V:3\times3$, with $\Sigma$ having diagonal $(\sqrt2,1,1)$ and a zero fourth row. Compact shapes are $4\times3$, $3\times3$, $3\times3$.
::::

::::{div} key-answer

The duplicated Y reading has stretch $\sqrt2$ in the declared Euclidean measurement units. This reflects repetition and scaling, not greater intrinsic importance of Y in the object.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

For a rank-$2$ matrix of size $4\times3$, what are the full and compact factor sizes?
:::

:::{dropdown} Check your reasoning

Full: $U:4\times4$, $\Sigma:4\times3$, $V^T:3\times3$. Compact: $U_r:4\times2$, $\Sigma_r:2\times2$, $V_r^T:2\times3$. There is one right-null and two left-null directions.
:::

::::{div} section-recap

**Takeaway:** Singular vectors inhabit different spaces; their counts must match the chosen SVD convention. Practice: Problems 11–13.
::::

(w5-svd-compute)=
## G · Computing the factors

::::{div} section-intro

**Learning goal:** Use a symmetric Gram matrix, keep signs paired, and handle zero singular values.

<span class="source-label">Lecture PDF pages 26</span>
::::

:::{admonition} Derivation · Why Gram matrices reveal singular directions
:class: key-result

For the full factorization,

$$A^TA=V\Sigma^T\Sigma V^T,\qquad AA^T=U\Sigma\Sigma^TU^T.$$

These matrices are square, symmetric and positive semidefinite, since $\mathbf x^TA^TA\mathbf x=\|A\mathbf x\|^2\ge0$.
Their positive eigenvalues are $\sigma_i^2$, so the singular values are **square roots**, not the Gram eigenvalues themselves. For rectangular $\Sigma$, retain $\Sigma^T\Sigma$ and $\Sigma\Sigma^T$; writing one common square $\Sigma^2$ hides a shape mismatch.

**Compute in this order:** find and normalize eigenvectors of $A^TA$; order their eigenvalues decreasingly; take nonnegative square roots; for each $\sigma_i>0$ set

$$\boxed{\mathbf u_i=\frac{A\mathbf v_i}{\sigma_i}}.$$

Complete $U$ with an orthonormal basis of $N(A^T)$ when needed. For zero singular values, never divide by zero; keep the appropriate null-space directions instead. Verify both orthogonality products and $U\Sigma V^T=A$. Computing U and V separately without pairing their signs can give a wrong product.
:::

:::::{admonition} Worked example 5.9 · A complete SVD from Worksheet Problem 14
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Build the Gram matrix and find its roots</span>

For the supplied worksheet’s matrix

$$A=\begin{bmatrix}3&0\\4&5\end{bmatrix},\qquad A^TA=\begin{bmatrix}25&20\\20&25\end{bmatrix}.$$

$\det(A^TA-\mu I)=(25-\mu)^2-400=(\mu-45)(\mu-5)$, so $\sigma_1=3\sqrt5$ and $\sigma_2=\sqrt5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Normalize the right directions</span>

At $\mu=45$, $-20v_1+20v_2=0$, giving $(1,1)^T/\sqrt2$.
At $\mu=5$, $20v_1+20v_2=0$, giving $(1,-1)^T/\sqrt2$.
Thus $V=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ and $V^TV=I_2$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Compute the paired left directions</span>

$$\mathbf u_1=\frac{(3,9)^T/\sqrt2}{3\sqrt5}=\frac1{\sqrt{10}}(1,3)^T,\qquad
\mathbf u_2=\frac{(3,-1)^T/\sqrt2}{\sqrt5}=\frac1{\sqrt{10}}(3,-1)^T.$$

Their squared lengths are $10/10=1$ and their cross dot product is $(3-3)/10=0$.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Reconstruct by two outer products</span>

$$\begin{aligned}
U\Sigma V^T
&=\frac32\begin{bmatrix}1&1\\3&3\end{bmatrix}
+\frac12\begin{bmatrix}3&-3\\-1&1\end{bmatrix}\\
&=\begin{bmatrix}3&0\\4&5\end{bmatrix}=A.
\end{aligned}$$

Equivalently $U=\frac1{\sqrt{10}}\begin{bmatrix}1&3\\3&-1\end{bmatrix}$ and $\Sigma=\operatorname{diag}(3\sqrt5,\sqrt5)$.
::::

::::{div} key-answer

The Gram eigenvalues are $45,5$; the singular values are $3\sqrt5,\sqrt5$. The outer-product check verifies the signs and ordering.
::::
:::::

:::::{admonition} Worked example 5.10 · A rectangular, rank-deficient case
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Find the one surviving input direction</span>

$$A=\begin{bmatrix}1&1\\0&0\\0&0\end{bmatrix},\quad A^TA=\begin{bmatrix}1&1\\1&1\end{bmatrix}.$$

The eigenvalues are $2,0$, so $\mathbf v_1=(1,1)^T/\sqrt2$, $\mathbf v_2=(1,-1)^T/\sqrt2$, and the only positive singular value is $\sqrt2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Complete the output basis without dividing by zero</span>

$A\mathbf v_1=(\sqrt2,0,0)^T$, so $\mathbf u_1=\mathbf e_1$.
Choose $U=I_3$ and

$$\Sigma=\begin{bmatrix}\sqrt2&0\\0&0\\0&0\end{bmatrix},\qquad
V=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}.$$

Then $U\Sigma V^T=A$. The last two columns of $U$ span $N(A^T)$; $\mathbf v_2$ spans $N(A)$.
::::

::::{div} key-answer

Full SVD still exists. The compact form keeps only $\mathbf u_1$, $\sqrt2$ and $\mathbf v_1^T$. For the zero matrix, there are no positive directions at all; full factors can still be identity bases and a zero rectangular $\Sigma$.
::::
:::::

:::{admonition} Pitfall · SVD versus eigendecomposition
:class: pitfall

Singular values are always real and nonnegative; eigenvalues of a general real square matrix can be negative or complex. SVD allows different input/output bases and rectangular matrices. Diagonalization uses one basis and requires enough independent eigenvectors. For a real symmetric matrix, singular values are the absolute values of its eigenvalues, put in decreasing order; a negative sign moves into a left singular direction.
:::

:::{admonition} Check your understanding
:class: checkpoint

If you replace a right singular vector by its negative, what else must change?
:::

:::{dropdown} Check your reasoning

The corresponding left singular vector must also change sign when its singular value is positive. Then $\sigma_i(-\mathbf u_i)(-\mathbf v_i)^T=\sigma_i\mathbf u_i\mathbf v_i^T$. Singular-vector signs and tied-subspace bases are not unique, but the factor product must check.
:::

::::{div} section-recap

**Takeaway:** Normalize, order, pair, reconstruct. Practice: Problems 14–18. The source’s final in-class SVD appears after the applications on Page 3.
::::

(w5-practice-svd)=
## Practice · Singular values and factors

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- svd:start -->
:end-before: <!-- svd:end -->
```

**Next:** {ref}`Page 3 · Reduction and recommendations <w5-applications>` keeps selected singular directions and explains what the discarded information costs.
