(w5-index)=
# Eigenvalues and diagonalization

<div class="chapter-kicker">Lecture 5 · Page 1 of 4 · Find directions, separate strengths, keep what matters</div>

A matrix can change a vector’s direction as well as its length. We first find the directions it preserves, then describe its action in those coordinates. Later, SVD extends this idea to **every real matrix**, including rectangular ones. All examples and diagrams needed to read this chapter are included here.

<nav class="lecture-path" aria-label="Lecture 5 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Eigenvalues & diagonalization</span></a>
<a href="svd.html"><span class="path-number">02</span><span>Singular value decomposition</span></a>
<a href="applications.html"><span class="path-number">03</span><span>Reduction & recommendations</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Recall {ref}`determinants <w2-determinants>`, {ref}`null spaces <w3-null-space>` and {ref}`orthonormal columns <w4-orthonormal-vectors>`. We use real matrices; “no eigenvectors” will mean **no real eigenvectors**, not an absence over the complex numbers. Every eigenvector must be nonzero.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`A · Matrices as transformations <w5-transformations>`
- {ref}`B · Directions that stay on their line <w5-eigenvectors>`
- {ref}`C · Finding eigenvalues and eigenvectors <w5-finding>`
- {ref}`D · Eigendecomposition and diagonalization <w5-diagonalization>`
- {ref}`E · The spectral theorem <w5-spectral>`
::::

(w5-transformations)=
## A · Matrices as transformations

::::{div} section-intro

**Learning goal:** Distinguish a general transformed vector from a scaled copy of the original.

<span class="source-label">Lecture PDF pages 1–8</span>
::::

:::{admonition} Definition · Linear transformation
:class: definition

A matrix $A\in\mathbb R^{m\times n}$ defines the map $\mathbf v\mapsto A\mathbf v$ from $\mathbb R^n$ to $\mathbb R^m$. Its columns are the images of the coordinate unit vectors. Addition and scalar multiplication are preserved: $A(c\mathbf v+d\mathbf w)=cA\mathbf v+dA\mathbf w$.
:::

:::::{admonition} Worked example 5.1 · A vector turns and stretches
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Multiply the source matrix row by row</span>

$$A=\begin{bmatrix}2&-1\\1&2\end{bmatrix},\qquad \mathbf v=\begin{bmatrix}2\\3\end{bmatrix},\qquad
A\mathbf v=\begin{bmatrix}2(2)-3\\2+2(3)\end{bmatrix}=\begin{bmatrix}1\\8\end{bmatrix}.$$

::::

::::{div} worked-step

<span class="step-label">Step 2 · Check whether it is a scaled copy</span>

The coordinate ratios are $1/2$ and $8/3$, which differ. There is no single multiplier $\lambda$ with $A\mathbf v=\lambda\mathbf v$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Identify the rotation and uniform scaling</span>

The slide’s two basic maps are

$$R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix},\qquad S_\alpha=\alpha I_2.$$

Here $A=\sqrt5R_\theta$ with $\cos\theta=2/\sqrt5$, $\sin\theta=1/\sqrt5$. The length changes from $\sqrt{13}$ to $\sqrt{65}=\sqrt5\sqrt{13}$.
::::

::::{div} key-answer

For this input, the transformation changes both direction and length. General matrices may also shear, reflect, or collapse directions; not every matrix is just a uniform stretch and rotation.
::::
:::::

:::::{admonition} Worked example 5.2 · A direction that only scales
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Multiply the second source example</span>

$$B=\begin{bmatrix}2&1\\2&3\end{bmatrix},\qquad
B\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}2+2\\2+6\end{bmatrix}=\begin{bmatrix}4\\8\end{bmatrix}.$$

::::

::::{div} worked-step

<span class="step-label">Step 2 · Factor out the common multiplier</span>

$(4,8)^T=4(1,2)^T$. Both outputs lie on the line through $(1,2)^T$, so this direction is preserved and its scale factor is $4$.
::::

::::{div} key-answer

$(1,2)^T$ is an eigenvector of $B$ with eigenvalue $4$.
::::
:::::

```{figure} ../figures/lecture5/transformed-vectors.svg
:alt: Fixed x,y axes show the first vector (2,3) mapped to (1,8), changing direction, and the second vector (1,2) mapped to (4,8) on the same line.

The two source transformations from PDF pages 3–8. The first changes direction; the second preserves a line through zero. Both panels use equal x/y scales.
```

:::{admonition} Check your understanding
:class: checkpoint

If $A\mathbf v=4\mathbf v$, what happens to $2\mathbf v$?
:::

:::{dropdown} Check your reasoning

$A(2\mathbf v)=2A\mathbf v=4(2\mathbf v)$. Every nonzero multiple is another eigenvector for the same eigenvalue.
:::

::::{div} section-recap

**Takeaway:** Test a single common multiplier, not just whether both entries grow. Practice: Problems 1–2.
::::

(w5-eigenvectors)=
## B · Directions that stay on their line

::::{div} section-intro

**Learning goal:** Interpret positive, negative and zero eigenvalues, and a rotation with no real eigendirection.

<span class="source-label">Lecture PDF pages 9–15</span>
::::

:::{admonition} Definition · Eigenpair and eigenspace
:class: definition

For a square $n\times n$ matrix, an **eigenpair** satisfies

$$\boxed{A\mathbf v=\lambda\mathbf v,\qquad \mathbf v\ne0}.$$

An eigenvalue is the scalar $\lambda$; an eigenvector is a nonzero vector $\mathbf v$.
If $\lambda>0$, direction is preserved; if $\lambda<0$, it reverses along the same line; if $\lambda=0$, the vector collapses to zero. The eigenspace is $E_\lambda=N(A-\lambda I)$; it includes zero, but zero is never an eigenvector.
:::

:::::{admonition} Worked example 5.3 · The source’s stretch and rotated-square pictures
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Check the diagonal stretch</span>

For $D=\operatorname{diag}(1,2)$,
$D\mathbf e_1=\mathbf e_1$ and $D\mathbf e_2=2\mathbf e_2$.
But $D(1,1)^T=(1,2)^T$ is not parallel to $(1,1)^T$. The two coordinate axes are eigendirections; the diagonal is not.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Make the rotated picture precise</span>

The source next rotates a square without supplying a numerical angle or matrix. An explicit representative is $R_{45^\circ}=\frac1{\sqrt2}\begin{bmatrix}1&-1\\1&1\end{bmatrix}$.
For a real eigenvalue, $\det(R_\theta-\lambda I)=\lambda^2-2\cos\theta\lambda+1=0$.
At $45^\circ$ the discriminant is $-2<0$, so there is no real eigenvalue or real eigenvector. The coordinate vectors turn, rather than stay on their original lines.
::::

::::{div} key-answer

The stretch has **two independent eigendirections**, not merely two eigenvectors. A nontrivial planar rotation through an angle other than $180^\circ$ has no real eigendirection.
::::
:::::

```{figure} ../figures/lecture5/stretch-and-rotation.svg
:alt: A square becomes a vertically stretched rectangle under diag(1,2); a second square rotates by 45 degrees. The coordinate axes remain eigenlines only for the stretch.

A labeled redraw of the stretch/rotation comparison from pages 10–15 and 18. The 45° angle makes the otherwise unlabeled rotation explicit; it is an editorial choice.
```

:::{admonition} Shadow connection · Retained and hidden directions
:class: connection

The embedded front-view projector $P=\operatorname{diag}(1,1,0)$ acts on world coordinates: $P\mathbf e_X=\mathbf e_X$, $P\mathbf e_Y=\mathbf e_Y$, $P\mathbf e_Z=0$. Its eigenvalues are $1,1,0$. The rectangular screen map $O(X,Y,Z)^T=(X,Y)^T$ is different: the ordinary square-matrix eigenvalue equation does not apply to $O$.
:::

:::{admonition} Check your understanding
:class: checkpoint

Is $(0,0,1)^T$ an eigenvector of $P=\operatorname{diag}(1,1,0)$ even though its output has no direction?
:::

:::{dropdown} Check your reasoning

Yes: it is nonzero and satisfies $P\mathbf v=0\mathbf v$. Eigenvalue zero is allowed; the eigenvector zero is not.
:::

::::{div} section-recap

**Takeaway:** “Same line” permits reversal and collapse. Practice: Problems 3–4.
::::

(w5-finding)=
## C · Finding eigenvalues and eigenvectors

::::{div} section-intro

**Learning goal:** Solve a determinant equation, then a separate homogeneous system for each root.

<span class="source-label">Lecture PDF pages 16–18</span>
::::

:::{admonition} Recipe · Shift, solve, check
:class: key-result

From $A\mathbf v=\lambda\mathbf v$ obtain $(A-\lambda I)\mathbf v=0$.
A nonzero solution requires a nontrivial null space, so

$$\boxed{\det(A-\lambda I)=0}.$$

First solve this **characteristic equation** for $\lambda$. Then, for each root, solve
$(A-\lambda I)\mathbf v=0$ and exclude $\mathbf v=0$. Check each answer in $A\mathbf v=\lambda\mathbf v$.
For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$,

$$\det(A-\lambda I)=(a-\lambda)(d-\lambda)-bc
=\lambda^2-(a+d)\lambda+(ad-bc).$$

Thus the eigenvalues sum to the trace and multiply to the determinant, counting multiplicities. Subtract $\lambda$ only from diagonal entries. An invertible $A-\lambda I$ has null space $\{0\}$ and yields no eigenvector: this is the handwritten null-space observation on page 16.
:::

:::::{admonition} Worked example 5.4 · The lecture’s complete diagonal-matrix calculation
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Find the roots</span>

For $D=\begin{bmatrix}1&0\\0&2\end{bmatrix}$,

$$\det(D-\lambda I)=(1-\lambda)(2-\lambda)=0,$$

so $\lambda=1,2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve the first null space</span>

At $\lambda=1$,

$$\begin{bmatrix}0&0\\0&1\end{bmatrix}\begin{bmatrix}v_1\\v_2\end{bmatrix}=0
\quad\Rightarrow\quad v_2=0.$$

Thus $E_1=\operatorname{span}\{(1,0)^T\}$; its eigenvectors are $t(1,0)^T$ with $t\ne0$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Solve the second null space and check</span>

At $\lambda=2$,

$$\begin{bmatrix}-1&0\\0&0\end{bmatrix}\begin{bmatrix}v_1\\v_2\end{bmatrix}=0
\quad\Rightarrow\quad v_1=0.$$

Thus $E_2=\operatorname{span}\{(0,1)^T\}$. Directly, $D\mathbf e_1=\mathbf e_1$, $D\mathbf e_2=2\mathbf e_2$. Trace $3=1+2$ and determinant $2=1\cdot2$ provide two quick checks.
::::

::::{div} key-answer

Report a basis for each eigenspace, or all its nonzero multiples when asked for all eigenvectors.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Why not row-reduce $A$ first and use the reduced matrix’s eigenvalues?
:::

:::{dropdown} Check your reasoning

Row operations preserve solutions of a corresponding transformed system, not eigenvalues of the original map. For example, $\operatorname{diag}(1,2)$ reduces to $I$, whose only eigenvalue is $1$. Reduce $A-\lambda I$ only after choosing a root.
:::

::::{div} section-recap

**Takeaway:** Find roots first; find null-space directions second. Practice: Problems 5–6.
::::

(w5-diagonalization)=
## D · Eigendecomposition and diagonalization

::::{div} section-intro

**Learning goal:** Check whether eigenvectors form a basis before writing an inverse.

<span class="source-label">Lecture PDF pages 19–20</span>
::::

:::{admonition} Definition · Diagonalizable
:class: definition

If $A$ has $n$ independent eigenvectors, place them in the columns of $V$, with their eigenvalues in the same order in $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$. Then

$$AV=V\Lambda,\qquad V^{-1}AV=\Lambda,\qquad \boxed{A=V\Lambda V^{-1}}.$$

Applied to a vector, $V^{-1}$ changes to eigenvector coordinates, $\Lambda$ scales those coordinates, and $V$ changes back. Distinct eigenvalues give independent eigenvectors; repeated roots require checking the eigenspace dimension.
A root’s algebraic multiplicity is its count in the characteristic polynomial; its geometric multiplicity is $\dim N(A-\lambda I)$. Diagonalization needs $n$ independent directions in total. Over the reals it also requires real eigenvalues.
:::

:::::{admonition} Worked example 5.5 · Diagonalize the earlier nonsymmetric example
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Find both eigenspaces</span>

For $B=\begin{bmatrix}2&1\\2&3\end{bmatrix}$,
$\det(B-\lambda I)=(2-\lambda)(3-\lambda)-2=(\lambda-4)(\lambda-1)$.
At $4$, the equation $-2v_1+v_2=0$ gives $(1,2)^T$; at $1$, $v_1+v_2=0$ gives $(1,-1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Match the column and eigenvalue order</span>

$$V=\begin{bmatrix}1&1\\2&-1\end{bmatrix},\quad \Lambda=\begin{bmatrix}4&0\\0&1\end{bmatrix},\quad
V^{-1}=\frac13\begin{bmatrix}1&1\\2&-1\end{bmatrix}.$$

$\det V=-3\ne0$, so these are a basis. They are not orthogonal: $(1,2)\cdot(1,-1)=-1$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check the reconstruction</span>

$$V\Lambda V^{-1}=\frac13\begin{bmatrix}4&1\\8&-1\end{bmatrix}\begin{bmatrix}1&1\\2&-1\end{bmatrix}
=\frac13\begin{bmatrix}6&3\\6&9\end{bmatrix}=B.$$

For powers, the inner inverse products cancel: $B^k=V\Lambda^kV^{-1}$ for nonnegative integers $k$.
::::

::::{div} key-answer

Diagonalizable does not mean orthogonally diagonalizable; do not replace $V^{-1}$ by $V^T$ without orthonormal columns.
::::
:::::

:::::{admonition} Worked example 5.6 · A repeated eigenvalue can fail
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Count the roots</span>

For $J=\begin{bmatrix}2&1\\0&2\end{bmatrix}$, $\det(J-\lambda I)=(2-\lambda)^2$: the only root is $2$, with algebraic multiplicity $2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count independent directions</span>

$(J-2I)\mathbf v=0$ gives $v_2=0$, so $E_2=\operatorname{span}\{(1,0)^T\}$ has dimension $1$. Two multiples of this vector cannot form an invertible $V$.
::::

::::{div} key-answer

$J$ is not diagonalizable. In contrast, $2I$ has the same repeated eigenvalue and a two-dimensional eigenspace, so it is diagonalizable.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

If a matrix has $n$ eigenvectors written down, is that enough?
:::

:::{dropdown} Check your reasoning

Only if the $n$ chosen vectors are independent. Scaling one eigenvector into many copies does not produce a basis. For repeated roots, compute each null space and count its independent directions.
:::

::::{div} section-recap

**Takeaway:** A full basis, not a list of roots alone, makes diagonalization possible. Practice: Problems 7–8.
::::

(w5-spectral)=
## E · The spectral theorem

::::{div} section-intro

**Learning goal:** Use symmetry to choose an orthonormal eigenbasis and test positive definiteness.

<span class="source-label">Lecture PDF pages 21–22</span>
::::

:::{admonition} Theorem · Real symmetric matrices
:class: key-result

Every real symmetric $S=S^T$ has real eigenvalues and an orthonormal eigenbasis:

$$\boxed{S=Q\Lambda Q^T,\qquad Q^TQ=I}.$$

Eigenvectors belonging to **distinct eigenvalues** are perpendicular. Within a repeated eigenspace, arbitrary eigenvectors need not be perpendicular, but an orthonormal basis can be chosen. For example, $I$ has eigenvectors $(1,0)^T$ and $(1,1)^T$, which are not perpendicular.
For symmetric $S$, positive definite means $\mathbf x^TS\mathbf x>0$ for every nonzero $\mathbf x$; this holds exactly when all eigenvalues are positive. Positive semidefinite permits zero and requires all eigenvalues nonnegative.
:::

:::{admonition} Proof · Why distinct eigenvalues are perpendicular
:class: proof

If $S\mathbf x=\lambda_1\mathbf x$ and $S\mathbf y=\lambda_2\mathbf y$, symmetry gives $\lambda_1\mathbf x^T\mathbf y=(S\mathbf x)^T\mathbf y=\mathbf x^TS\mathbf y=\lambda_2\mathbf x^T\mathbf y$. Thus $(\lambda_1-\lambda_2)\mathbf x^T\mathbf y=0$; distinct roots force $\mathbf x^T\mathbf y=0$. This proves the perpendicularity claim, not the entire existence theorem. For positivity, write $\mathbf z=Q^T\mathbf x$: $\mathbf x^TS\mathbf x=\sum_i\lambda_i z_i^2$.
:::

:::::{admonition} Worked example 5.7 · The handwritten in-class example on page 22
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Find the eigenvalues</span>

$$S=\begin{bmatrix}3&1\\1&3\end{bmatrix},\qquad
\det(S-\lambda I)=(3-\lambda)^2-1=(\lambda-4)(\lambda-2).$$

Both eigenvalues are positive, so this symmetric matrix is positive definite.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve and normalize</span>

For $4$, $-v_1+v_2=0$ gives $(1,1)^T$. For $2$, $v_1+v_2=0$ gives $(-1,1)^T$. Their dot product is zero, but both lengths are $\sqrt2$. Thus

$$Q=\frac1{\sqrt2}\begin{bmatrix}1&-1\\1&1\end{bmatrix},\qquad\Lambda=\operatorname{diag}(4,2).$$

::::

::::{div} worked-step

<span class="step-label">Step 3 · Verify the spectral reconstruction</span>

$$Q\Lambda Q^T=\frac12\begin{bmatrix}4&-2\\4&2\end{bmatrix}\begin{bmatrix}1&1\\-1&1\end{bmatrix}
=\frac12\begin{bmatrix}6&2\\2&6\end{bmatrix}=S.$$

The original eigenvectors were orthogonal, not orthonormal; dividing by $\sqrt2$ supplies the missing unit lengths.
::::

::::{div} key-answer

$S$ is positive definite and admits $Q\Lambda Q^T$. This includes both questions and the full handwritten computation from the source.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Can a real symmetric matrix have a negative eigenvalue?
:::

:::{dropdown} Check your reasoning

Yes: $\operatorname{diag}(2,-1)$ is symmetric. Symmetry guarantees a real orthonormal eigenbasis, not positive definiteness.
:::

::::{div} section-recap

**Takeaway:** Symmetry gives an orthonormal choice; positivity is an additional property. Practice: Problems 9–10.
::::

(w5-practice-eigen)=
## Practice · Eigenvalues and diagonalization

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- eigen:start -->
:end-before: <!-- eigen:end -->
```

**Next:** {ref}`Page 2 · Singular value decomposition <w5-svd>` separates input and output directions, so rectangular matrices are included.
