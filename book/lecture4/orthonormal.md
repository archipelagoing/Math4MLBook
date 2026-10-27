(w4-orthonormal)=
# Orthonormal bases and Gram–Schmidt

<div class="chapter-kicker">Lecture 4 · Page 3 of 4 · Finding the closest possible record</div>

The normal equations simplify dramatically when the basis directions are perpendicular and have length one. First use that structure; then build it by subtracting projections. The chapter ends with a fresh mixed check.

<nav class="lecture-path" aria-label="Lecture 4 learning path">
<a href="index.html"><span class="path-number">01</span><span>Orthogonality & projections</span></a>
<a href="least-squares.html"><span class="path-number">02</span><span>Subspaces & least squares</span></a>
<a href="orthonormal.html" aria-current="page"><span class="path-number">03</span><span>Orthonormal bases & Gram–Schmidt</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Follow the lecture**

- {ref}`I · Orthonormal vectors and matrices <w4-orthonormal-vectors>`
- {ref}`J · Projection using an orthonormal basis <w4-q-projection>`
- {ref}`K · The Gram–Schmidt process <w4-gram-schmidt>`
::::

(w4-orthonormal-vectors)=
## I · Orthonormal vectors and matrices

::::{div} section-intro

**Learning goal:** Recognize orthonormal columns and state when transpose really is inverse.

<span class="source-label">Lecture PDF pages 22–23</span>
::::

:::{admonition} Definition · Orthogonal plus normalized
:class: definition

Vectors $\mathbf q_1,\ldots,\mathbf q_n$ are **orthonormal** when

$$\mathbf q_i^T\mathbf q_j=\begin{cases}1&i=j,\\0&i\ne j.\end{cases}$$

For $Q=[\mathbf q_1\ \cdots\ \mathbf q_n]\in\mathbb R^{m\times n}$ this is exactly $Q^TQ=I_n$: each entry of $Q^TQ$ is a column dot product.
A **square orthogonal matrix** has orthonormal columns and satisfies $Q^{-1}=Q^T$ and $QQ^T=I$ as well.
:::

:::::{admonition} Worked example 4.9 · The lecture’s permutation matrix
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read the columns as basis vectors</span>

$$Q_1=\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}=[\mathbf e_3\ \mathbf e_2\ \mathbf e_1].$$

Each column has length $1$, and different columns have dot product zero. Therefore $Q_1^TQ_1=I_3$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check its action and inverse</span>

$Q_1(X,Y,Z)^T=(Z,Y,X)^T$. Swapping again returns the original vector, so $Q_1^2=I_3$. Here $Q_1^{-1}=Q_1^T=Q_1$.
::::

::::{div} key-answer

Permuting coordinates preserves dot products and lengths; it is orthogonal even though it is not a rotation.
::::
:::::

:::::{admonition} Worked example 4.10 · The lecture’s rotation matrix
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Check all column dot products</span>

$$Q_2=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}.$$

Each squared column length is $\cos^2\theta+\sin^2\theta=1$. Their dot product is $-\cos\theta\sin\theta+\sin\theta\cos\theta=0$. Thus $Q_2^TQ_2=I_2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Interpret the inverse</span>

Acting on points in fixed axes, $Q_2$ rotates counterclockwise by $\theta$. Its transpose rotates by $-\theta$ and undoes the action. For $\theta=90^\circ$, $(X,Y)^T\mapsto(-Y,X)^T$.
::::

::::{div} key-answer

For any orthogonal square $Q$, $\|Q\mathbf v\|^2=\mathbf v^TQ^TQ\mathbf v=\|\mathbf v\|^2$.
::::
:::::

:::{admonition} Pitfall · Rectangular Q has a different second product
:class: pitfall

For $Q\in\mathbb R^{m\times n}$ with $n<m$, $Q^TQ=I_n$, but generally $QQ^T\ne I_m$. It is a projector. Such a rectangular $Q$ has no two-sided inverse. Also, orthogonal columns without unit lengths give a diagonal $Q^TQ$, not necessarily the identity.
:::

:::{admonition} Check your understanding
:class: checkpoint

Does $Q=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$ satisfy both identity products?
:::

:::{dropdown} Check your reasoning

$Q^TQ=I_2$, while $QQ^T=\operatorname{diag}(1,1,0)$. The second projects onto the xy-plane.
:::

::::{div} section-recap

**Takeaway:** Check lengths as well as pairwise dot products, and check matrix shape. Practice: Problems 17–18.
::::

(w4-q-projection)=
## J · Projection using an orthonormal basis

::::{div} section-intro

**Learning goal:** Use dot products directly as basis coefficients.

<span class="source-label">Lecture PDF pages 24</span>
::::

If the spanning columns are already orthonormal, the Gram matrix is the identity. The small system needs no elimination: each coefficient is just the component of the data in that basis direction.

:::{admonition} Result · Dot products supply the coordinates
:class: key-result

For $Q^TQ=I_n$,

$$\widehat{\mathbf c}=Q^T\mathbf b,\qquad
\mathbf p=Q\widehat{\mathbf c}=\sum_{i=1}^n(\mathbf q_i^T\mathbf b)\mathbf q_i,\qquad
\boxed{P=QQ^T}.$$

Since $(QQ^T)^T=QQ^T$ and $(QQ^T)^2=Q(Q^TQ)Q^T=QQ^T$, this is an orthogonal projector.
If $\mathbf b$ lies in the span, these are its exact coordinates; otherwise they describe its closest vector in the span.
:::

:::::{admonition} Worked example 4.11 · An orthonormal basis for the two-view records
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Normalize the independent record directions</span>

For the {ref}`two-view record space <w4-subspace>`, whose records have the form $(X,Y,Y,Z)^T$, choose

$$\mathbf q_1=(1,0,0,0)^T,\quad
\mathbf q_2=\frac1{\sqrt2}(0,1,1,0)^T,\quad
\mathbf q_3=(0,0,0,1)^T.$$

The second column of $H$ has length $\sqrt2$, so divide it by $\sqrt2$. These three directions are mutually perpendicular.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Take components, then reconstruct</span>

With $\mathbf b=(2,2,4,4)^T$,

$$Q^T\mathbf b=(2,3\sqrt2,4)^T,\qquad
\mathbf p=2\mathbf q_1+3\sqrt2\mathbf q_2+4\mathbf q_3=(2,3,3,4)^T.$$

$\widehat{\mathbf c}$ gives coefficients in the normalized record basis; it differs from the physical-coordinate estimate $(2,3,4)^T$ in the original $H$ basis.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check the same projector and error</span>

$QQ^T$ is the same {ref}`measurement projector $P_H$ <w4-subspace>`. Again $\mathbf e=(0,-1,1,0)^T$, and each $\mathbf q_i^T\mathbf e=0$. Changing the basis has not changed the projected record.
::::

::::{div} key-answer

Orthonormal coordinates simplify the computation while preserving the subspace and its closest vector.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Why can you not use $A^T\mathbf b$ directly as coefficients for arbitrary independent columns of $A$?
:::

:::{dropdown} Check your reasoning

Because their Gram matrix need not be $I$. Dot products can include overlap and nonunit lengths. Solve $A^TA\widehat{\mathbf x}=A^T\mathbf b$, or first construct an orthonormal basis.
:::

::::{div} section-recap

**Takeaway:** Independent directions need a Gram-system solve; orthonormal directions need dot products. Practice: Problems 19–20.
::::

(w4-gram-schmidt)=
## K · The Gram–Schmidt process

::::{div} section-intro

**Learning goal:** Remove old components, normalize new directions, and handle a zero remainder.

<span class="source-label">Lecture PDF pages 25–28</span>
::::

Gram–Schmidt turns independent vectors into an orthonormal basis for the **same span**. Each new vector loses its projections onto the directions already kept. The leftover is perpendicular to those directions; normalization makes its length one.

:::{admonition} Recipe · Subtract, check, normalize
:class: definition

For inputs $\mathbf a_1,\ldots,\mathbf a_n$, construct

$$\mathbf u_1=\mathbf a_1,\qquad \mathbf q_1=\frac{\mathbf u_1}{\|\mathbf u_1\|},$$

$$\mathbf u_j=\mathbf a_j-\sum_{i<j}(\mathbf q_i^T\mathbf a_j)\mathbf q_i,\qquad
\mathbf q_j=\frac{\mathbf u_j}{\|\mathbf u_j\|}.$$

Alternatively, subtract $(\mathbf u_i^T\mathbf a_j)/(\mathbf u_i^T\mathbf u_i)\,\mathbf u_i$ using the **orthogonal, not yet normalized** vectors. These two versions agree; do not mix their denominators.
For independent inputs each remainder is nonzero. If a remainder is zero, that input adds no new direction: skip it when finding a basis for a span, and never divide by its norm.
:::

:::::{admonition} Worked example 4.12 · The lecture’s full Gram–Schmidt calculation
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Keep the first direction</span>

The source inputs are

$$\begin{aligned}
\mathbf x&=(2,-2,0)^T,\\
\mathbf y&=(4,0,-4)^T,\\
\mathbf z&=(6,-6,6)^T.
\end{aligned}$$

Call the successive orthogonal remainders $\mathbf A,\mathbf B,\mathbf C$ (vectors, not matrices). Set $\mathbf A=\mathbf x$, so $\mathbf A^T\mathbf A=8$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Remove the first component from y</span>

$\mathbf A^T\mathbf y=2(4)+(-2)(0)+0(-4)=8$, so

$$\mathbf B=\mathbf y-\frac88\mathbf A
=(4,0,-4)^T-(2,-2,0)^T=(2,2,-4)^T.$$

Check $\mathbf A^T\mathbf B=4-4=0$ and $\mathbf B^T\mathbf B=4+4+16=24$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Remove both old components from z</span>

$\mathbf A^T\mathbf z=12+12=24$ and $\mathbf B^T\mathbf z=12-12-24=-24$. Therefore

$$\begin{aligned}\mathbf C&=\mathbf z-\frac{24}{8}\mathbf A-\frac{-24}{24}\mathbf B\\
&=(6,-6,6)^T-(6,-6,0)^T+(2,2,-4)^T\\&=(2,2,2)^T.\end{aligned}$$

The last term is **added** because its dot product is negative. Check $\mathbf A^T\mathbf C=4-4=0$, $\mathbf B^T\mathbf C=4+4-8=0$.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Normalize each nonzero remainder</span>

$\|\mathbf A\|=\sqrt8=2\sqrt2$, $\|\mathbf B\|=\sqrt{24}=2\sqrt6$, $\|\mathbf C\|=\sqrt{12}=2\sqrt3$, giving

$$\begin{aligned}
\mathbf q_1&=\frac1{\sqrt2}(1,-1,0)^T,\\
\mathbf q_2&=\frac1{\sqrt6}(1,1,-2)^T,\\
\mathbf q_3&=\frac1{\sqrt3}(1,1,1)^T.
\end{aligned}$$

The squared lengths are $2/2$, $6/6$, $3/3$; all pairwise dot products are zero. Hence $Q^TQ=I_3$.
::::

::::{div} key-answer

The span is preserved, and the final basis is orthonormal. Nonzero remainders at all three stages also establish input independence.
::::
:::::

```{figure} ../figures/lecture4/gram-schmidt.svg
:alt: The vector (1,2) decomposes into projection (1,0) along the first direction and remainder (0,2); normalization produces the coordinate unit vectors.

A two-dimensional illustration of the subtraction step: remove the old component before normalizing the new one.
```

:::{admonition} Shadow connection · A new view must add a direction
:class: connection

Compare the row directions $\mathbf e_X=(1,0,0)^T$ and $\mathbf v=(\cos\theta,0,\sin\theta)^T$. Subtracting the projection along $\mathbf e_X$ leaves $(0,0,\sin\theta)^T$. For $0<\theta\le90^\circ$, normalizing gives $\mathbf e_Z$. At $\theta=0$ the remainder is zero: the repeated view adds no depth information. A tiny nonzero remainder also warns that rounding or measurement errors can matter; algebraic independence alone does not guarantee a stable reconstruction.
:::

:::::{admonition} Worked example 4.13 · A dependent list from Recitation 2, Problem 4
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Orthogonalize the independent directions</span>

In $\mathbb R^4$, let $\mathbf a_1=(1,1,1,1)^T$, $\mathbf a_2=(3,1,1,3)^T$, $\mathbf a_3=\mathbf a_1+\mathbf a_2$.
Take $\mathbf u_1=\mathbf a_1$, with squared norm $4$. Then

$$\mathbf u_2=\mathbf a_2-\frac84\mathbf a_1=(1,-1,-1,1)^T,$$

also with squared norm $4$, and $\mathbf u_1^T\mathbf u_2=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Skip the redundant third vector</span>

Since $\mathbf a_3=3\mathbf u_1+\mathbf u_2$, removing those two components gives zero. Thus a basis is

$$\mathbf q_1=\tfrac12(1,1,1,1)^T,\qquad\mathbf q_2=\tfrac12(1,-1,-1,1)^T.$$

There are two basis vectors, not three: $\dim S=2$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Find and check the nearest vector</span>

For $\mathbf b=(1,0,0,0)^T$, both dot products $\mathbf q_i^T\mathbf b=1/2$. Thus

$$\mathbf p=\tfrac12\mathbf q_1+\tfrac12\mathbf q_2=(1/2,0,0,1/2)^T.$$

$\mathbf e=(1/2,0,0,-1/2)^T$ has zero dot product with both basis vectors, and $\|\mathbf e\|^2=1/2$.
::::

::::{div} key-answer

Build an orthonormal basis for the **span**, then project onto that basis. Dependent input vectors do not require a third unit direction.
::::
:::::

:::{admonition} Pitfall · Normalize at the right stage
:class: pitfall

Dividing every original vector by its own length does not remove overlap. First subtract **all** earlier components, then normalize the remainder. Different input orders can give different orthonormal bases for the same span and the same projection.
:::

:::{admonition} Check your understanding
:class: checkpoint

If the third remainder is zero, is the span necessarily the zero space?
:::

:::{dropdown} Check your reasoning

No. It only says the third vector lies in the span already constructed. Keep the earlier nonzero directions; the dimension is the number retained.
:::

::::{div} section-recap

**Takeaway:** Each remainder isolates genuinely new information. Practice: Problems 21–24, then the mixed check.
::::

(w4-practice-bases)=
## Practice · Orthonormal bases and Gram–Schmidt

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- bases:start -->
:end-before: <!-- bases:end -->
```

(w4-readiness)=
## Can you do this unaided?

Close the worked examples. Allow **20 minutes for Problems 25–28**, then open the answers and diagnose mistakes. This is an editorial rehearsal, not an official exam time or grading scale.

Score each problem out of 4: **1** for a valid model/method with conditions, **2** for accurate calculations, **1** for a verification or explanation. An editorial target is **14/16 with no unresolved conceptual error**. A lower score directs revision; it does not predict a course grade. Retry with changed numbers after reviewing, rather than memorizing an answer.

- Can you identify the right ambient space and perpendicular complement?
- Can you produce both a fitted vector and a residual, and verify optimality?
- Can you distinguish unique output from unique coefficients?
- Can you construct an orthonormal basis and recognize redundant inputs?

```{include} practice.md
:start-after: <!-- mixed:start -->
:end-before: <!-- mixed:end -->
```

(w4-source-notes)=
## Source notes and next connection

This chapter develops **all 28 PDF pages** of Erisa Terolli’s CS 556
`WK4_Orthogonality_and_Projections.pdf`: orthogonality (1–5), projections (6–14), least squares (15–21), orthonormal vectors (22–24), Gram–Schmidt (25–28).
Title pages and progressive reveals are combined without removing mathematical content.
The coordinate split, permutation, rotation, three-point fit and full three-vector Gram–Schmidt example retain the source data.

Slide 26 switches names from a,b,c to y,z; here the recipe uses consistent inputs and the numerical example uses x,y,z. “Projection” throughout means **orthogonal** projection: a general idempotent matrix need not be symmetric. The inverse-based formulas explicitly require independent columns. These are clarifications, not new restrictions on the lecture’s scope.

The shadow examples, proofs of minimality/uniqueness, illustrations, rank-deficient case, checkpoints and fresh mixed rehearsal are editorial teaching additions. Worked example 4.13 develops **Recitation2_Solutions.pdf, Problem 4 (PDF page 4)**, also present in **mfmlhw2.pdf, Problem 4**. Practice 10, 16, 23 and 24 use **Linear_Algebra_Worksheet-1.pdf, Problems 8–12/15**, with the exact question identified beside each. Worksheet 12(b) has an apparent typo: the coefficient is a dot product with b, not “xᵢ = qᵢ = b”; the unit-length assumption is essential.

The supplied midterm topic list explicitly names orthogonality, projections, Gram–Schmidt and orthogonal matrices. This chapter teaches and practices those skills; eigenvalues, SVD and the statistics/PCA bridge remain later destinations. The source audit and validation details live in the repository’s authoring records.

**Next:** use {ref}`the TL;DR cheat sheet <w4-cheatsheet>` to select methods without retracing the whole chapter. Lecture 5 will study transformations through eigenvectors and decompositions.
