(w4-index)=
# Orthogonality and projections

<div class="chapter-kicker">Lecture 4 · Page 1 of 4 · Finding the closest possible record</div>

Lecture 3 described which outputs a matrix can produce. Now suppose the measured output is impossible: **which possible output is closest?** Orthogonality supplies the check; projection supplies the answer. We develop the entire Week 4 deck in its original topic order.

<nav class="lecture-path" aria-label="Lecture 4 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Orthogonality & projections</span></a>
<a href="least-squares.html"><span class="path-number">02</span><span>Subspaces & least squares</span></a>
<a href="orthonormal.html"><span class="path-number">03</span><span>Orthonormal bases & Gram–Schmidt</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Recall {ref}`dot products and lengths <w1-geometry>` and {ref}`the four fundamental spaces <w3-four-spaces>`. Vectors are real column vectors; distance means Euclidean distance. A hat marks a fitted coefficient, not an exact solution of the original equations.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`A · Orthogonal vectors and subspaces <w4-orthogonality>`
- {ref}`B · Orthogonality of the four spaces <w4-four-spaces>`
- {ref}`C · Coordinate projections <w4-coordinate>`
- {ref}`D · Why projections are needed <w4-why>`
- {ref}`E · Projection onto a line <w4-line>`
::::

(w4-orthogonality)=
## A · Orthogonal vectors and subspaces

::::{div} section-intro

**Learning goal:** Test perpendicularity and distinguish orthogonality from unit length.

<span class="source-label">Lecture PDF pages 1–3</span>
::::

Start with two directions. If moving along one does not contribute any component along the other, their dot product is zero. This algebraic test works even when we cannot draw the space.

:::{admonition} Definition · Orthogonality
:class: definition

Vectors $\mathbf v,\mathbf w\in\mathbb R^n$ are **orthogonal** when $\mathbf v^T\mathbf w=0$.
For nonzero vectors this means a right angle. The zero vector is orthogonal to every vector, but its angle is undefined.

Subspaces $V,W$ are orthogonal when **every** $\mathbf v\in V$ and **every** $\mathbf w\in W$ satisfy $\mathbf v^T\mathbf w=0$. Testing every pair of basis vectors suffices, because the dot product distributes over linear combinations.
:::

:::::{admonition} Worked example 4.1 · Check a right angle algebraically
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compute the dot product</span>

For $\mathbf v=(1,2)^T$ and $\mathbf w=(2,-1)^T$, $\mathbf v^T\mathbf w=1(2)+2(-1)=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the length identity</span>

$\|\mathbf v\|^2=5$, $\|\mathbf w\|^2=5$, and $\|\mathbf v+\mathbf w\|^2=\|(3,1)^T\|^2=10$. Thus $5+5=10$.
::::

::::{div} key-answer

The vectors are **orthogonal**, although neither has length $1$.
::::
:::::

:::{admonition} Result · Pythagoras in any dimension
:class: key-result

Expand the squared norm:

$$\|\mathbf v+\mathbf w\|^2=\|\mathbf v\|^2+2\mathbf v^T\mathbf w+\|\mathbf w\|^2.$$

Therefore $\mathbf v\perp\mathbf w$ exactly when
$\|\mathbf v+\mathbf w\|^2=\|\mathbf v\|^2+\|\mathbf w\|^2$.
:::

:::{admonition} Check your understanding
:class: checkpoint

Is $\operatorname{span}\{(1,0,0)^T,(0,1,0)^T\}$ orthogonal to $\operatorname{span}\{(0,0,1)^T\}$?
:::

:::{dropdown} Check your reasoning

Yes. Both basis dot products are zero, so every $(a,b,0)^T$ is perpendicular to every $(0,0,c)^T$. One successful pair alone would not establish this.
:::

::::{div} section-recap

**Takeaway:** Orthogonal means zero dot product; unit length is a separate condition. Practice: Problems 1–2 below.
::::

(w4-four-spaces)=
## B · Orthogonality of the four spaces

::::{div} section-intro

**Learning goal:** Identify the ambient space and the correct orthogonal-complement pair.

<span class="source-label">Lecture PDF pages 4–5</span>
::::

Pair spaces on the **same side of the map**, as shown below. If $A$ is $m\times n$ with rank $r$, inputs live in $\mathbb R^n$ and outputs in $\mathbb R^m$.

```{figure} ../figures/lecture4/four-space-complements.svg
:alt: Input Rn contains complementary row and null spaces of dimensions r and n minus r. Output Rm contains complementary column and left null spaces of dimensions r and m minus r. A maps row space onto column space and null space to zero.

The four fundamental spaces, redrawn from the lecture's PDF page 4. Vertical pairs are perpendicular complements; horizontal/slanted arrows show the action of A, not a claim of perpendicularity across different ambient spaces.
```

:::{admonition} Result · Two complementary pairs
:class: key-result

| Ambient space | Orthogonal complements | Dimensions |
| --- | --- | --- |
| Input $\mathbb R^n$ | $C(A^T)$ and $N(A)$ | $r$ and $n-r$ |
| Output $\mathbb R^m$ | $C(A)$ and $N(A^T)$ | $r$ and $m-r$ |

The orthogonal complement $S^\perp$ contains **all** vectors perpendicular to $S$.
Every vector in the ambient space splits uniquely into a part in $S$ and a part in $S^\perp$. Orthogonal subspaces need not fill the ambient space; complements do.
:::

:::{admonition} Proof · Read the equations row by row
:class: proof

If $A\mathbf x=0$, every row of $A$ has dot product zero with $\mathbf x$. So $N(A)\perp C(A^T)$; their dimensions add to $n$, making them complements. Apply the same argument to $A^T$ to obtain $N(A^T)=C(A)^\perp$.

The arrows in the figure above have different jobs: $A$ sends null-space components to zero. Its restriction from $C(A^T)$ onto $C(A)$ is one-to-one and onto: the only row-space vector in $N(A)$ is zero, and both spaces have dimension $r$.
:::

:::::{admonition} Worked example 4.2 · The two-view measurement space
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Declare the map and its spaces</span>

For the same calibrated, matched point from Lecture 3,

$$H=\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix},\qquad H(X,Y,Z)^T=(X,Y,Y,Z)^T.$$

Here $m=4$, $n=r=3$: the two screens repeat the same $Y$ coordinate.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find the output direction that no point can produce</span>

Every possible record has equal middle entries. The vector $\boldsymbol\ell=(0,1,-1,0)^T$ satisfies $H^T\boldsymbol\ell=0$ and
$\boldsymbol\ell^T(X,Y,Y,Z)^T=Y-Y=0$.
Thus $C(H)$ has dimension $3$ and $N(H^T)=\operatorname{span}\{\boldsymbol\ell\}$ has dimension $1$.
::::

::::{div} key-answer

In $\mathbb R^4$, possible records and the discrepancy direction are orthogonal complements. In $\mathbb R^3$, $C(H^T)=\mathbb R^3$ and $N(H)=\{0\}$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

For a rank-$2$, $5\times3$ matrix, what is perpendicular to its column space, and what is that space’s dimension?
:::

:::{dropdown} Check your reasoning

$N(A^T)\subseteq\mathbb R^5$, of dimension $5-2=3$. $N(A)$ instead lies in $\mathbb R^3$ and has dimension $1$.
:::

::::{div} section-recap

**Takeaway:** Pair row with null, and column with left null. Practice: Problems 3–4.
::::

(w4-coordinate)=
## C · Coordinate projections

::::{div} section-intro

**Learning goal:** Split the lecture’s vector into its nearest z-axis and xy-plane parts.

<span class="source-label">Lecture PDF pages 6–8</span>
::::

:::{admonition} Definition · Orthogonal projection
:class: definition

The orthogonal projection of $\mathbf b$ onto a subspace $S$ is the closest vector $\mathbf p\in S$ to $\mathbf b$. Its residual is $\mathbf e=\mathbf b-\mathbf p\in S^\perp$.

A matrix representing this operation satisfies $P^T=P$ and $P^2=P$; then $\mathbf p=P\mathbf b$. Symmetry expresses perpendicular projection, and idempotence says projecting twice changes nothing further.
:::

:::::{admonition} Worked example 4.3 · The lecture’s z-axis and xy-plane split
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Keep only the z coordinate</span>

With $\mathbf b=(1,2,3)^T$, the closest point on the z-axis is

$$\mathbf p_1=\begin{bmatrix}0\\0\\3\end{bmatrix},\qquad P_1=\begin{bmatrix}0&0&0\\0&0&0\\0&0&1\end{bmatrix}.$$

Choosing any different height adds unnecessary squared distance.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Keep only the x and y coordinates</span>

For the xy-plane,

$$\mathbf p_2=\begin{bmatrix}1\\2\\0\end{bmatrix},\qquad P_2=\begin{bmatrix}1&0&0\\0&1&0\\0&0&0\end{bmatrix}.$$

The residual $\mathbf b-\mathbf p_2=(0,0,3)^T$ is perpendicular to the whole plane.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check the complementary split</span>

$\mathbf p_1+\mathbf p_2=\mathbf b$, $\mathbf p_1^T\mathbf p_2=0$, and $P_1+P_2=I_3$.
Both matrices are symmetric and squaring either leaves it unchanged.
::::

::::{div} key-answer

$\mathbf b=(1,2,0)^T+(0,0,3)^T$: plane part plus perpendicular part.
::::
:::::

:::{admonition} Shadow connection · Observation versus embedded projection
:class: connection

The front screen records $O(X,Y,Z)^T=(X,Y)^T$, with $O$ of size $2\times3$. The embedded world-space projection is $O^TO=P_2$, of size $3\times3$.
The screen record $(X,Y)^T$ and the projected world point $(X,Y,0)^T$ belong to different spaces. Neither recovers the hidden depth.
:::

:::{admonition} Check your understanding
:class: checkpoint

If $\mathbf b$ already lies in $S$, what are $P\mathbf b$ and $\mathbf e$?
:::

:::{dropdown} Check your reasoning

$P\mathbf b=\mathbf b$ and $\mathbf e=0$. This explains $P^2=P$: the first projected vector already lies in $S$.
:::

::::{div} section-recap

**Takeaway:** Projection retains the allowed part and removes the perpendicular part. Practice: Problems 5–6.
::::

(w4-why)=
## D · Why projections are needed

::::{div} section-intro

**Learning goal:** Replace an impossible exact fit with a precisely defined closest fit.

<span class="source-label">Lecture PDF pages 9</span>
::::

When $A\mathbf x=\mathbf b$ is inconsistent, elimination cannot create an exact solution. We instead choose $\mathbf p\in C(A)$ minimizing $\|\mathbf b-\mathbf p\|$, then solve $A\widehat{\mathbf x}=\mathbf p$. The measurement changes; the model matrix stays fixed.

:::::{admonition} Worked example 4.4 · Two screens disagree on the same coordinate
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Detect the impossible record</span>

For the $H$ above, take $\mathbf b=(2,2,4,4)^T$. Its middle entries disagree, so $\mathbf b\notin C(H)$ and $H\mathbf x=\mathbf b$ has no solution.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Fit the shared coordinate</span>

With equal squared-error weights, minimize

$$(X-2)^2+(Y-2)^2+(Y-4)^2+(Z-4)^2.$$

Since $(Y-2)^2+(Y-4)^2=2(Y-3)^2+2$, the minimum occurs at $(X,Y,Z)=(2,3,4)$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check the perpendicular error</span>

$\mathbf p=(2,3,3,4)^T$ and $\mathbf e=(0,-1,1,0)^T$.
Direct multiplication gives $H^T\mathbf e=(0,0,0)^T$, so the residual lies in $N(H^T)$.
::::

::::{div} key-answer

The fitted point is $\widehat{\mathbf x}=(2,3,4)^T$; the closest record is $\mathbf p=H\widehat{\mathbf x}$. They have different dimensions.
::::
:::::

```{figure} ../figures/lecture4/measurement-fit.svg
:alt: Two inconsistent middle readings 2 and 4 move to the common fitted value 3; residuals are minus one and plus one.

Equal weights reconcile repeated Y readings by averaging. This is a fit in four-dimensional measurement space, not proof of the point’s true physical location.
```

:::{admonition} Check your understanding
:class: checkpoint

Does a nonzero residual mean that the fitting method failed?
:::

:::{dropdown} Check your reasoning

No. If the original record is inconsistent, every possible fit has a nonzero residual. The correct test is perpendicularity to $C(A)$, not zero residual.
:::

::::{div} section-recap

**Takeaway:** Fit the closest achievable output; retain the residual as evidence of the mismatch. Practice: Problem 7.
::::

(w4-line)=
## E · Projection onto a line

::::{div} section-intro

**Learning goal:** Derive and use the scalar coefficient, projected vector, and projection matrix.

<span class="source-label">Lecture PDF pages 10–11</span>
::::

Every point on the line $\operatorname{span}\{\mathbf a\}$ is a multiple of $\mathbf a$. To find the nearest one, make the leftover error perpendicular to that direction. Assume $\mathbf a\ne0$.

:::{admonition} Derivation · Remove the perpendicular error
:class: key-result

Write $\mathbf p=\widehat x\mathbf a$. Then

$$\mathbf a^T(\mathbf b-\widehat x\mathbf a)=0
\quad\Longrightarrow\quad \mathbf a^T\mathbf b=\widehat x\,\mathbf a^T\mathbf a.$$

Hence

$$\boxed{\widehat x=\frac{\mathbf a^T\mathbf b}{\mathbf a^T\mathbf a}},\qquad
\boxed{\mathbf p=\frac{\mathbf a^T\mathbf b}{\mathbf a^T\mathbf a}\mathbf a},\qquad
\boxed{P=\frac{\mathbf a\mathbf a^T}{\mathbf a^T\mathbf a}}.$$

$\widehat x$ is one number, $\mathbf p\in\mathbb R^m$, and $P$ is $m\times m$. The numerator $\mathbf a\mathbf a^T$ is an outer product, not a dot product.
:::

:::::{admonition} Worked example 4.5 · A slanted line, with a complete check
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compute the coefficient</span>

Let $\mathbf a=(1,2)^T$, $\mathbf b=(3,1)^T$. Then $\mathbf a^T\mathbf b=5$ and $\mathbf a^T\mathbf a=5$, so $\widehat x=1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Separate fitted vector and error</span>

$\mathbf p=1(1,2)^T=(1,2)^T$ and $\mathbf e=(3,1)^T-(1,2)^T=(2,-1)^T$. Check $\mathbf a^T\mathbf e=2-2=0$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Build and verify the matrix</span>

$$P=\frac15\begin{bmatrix}1&2\\2&4\end{bmatrix},\qquad P\begin{bmatrix}3\\1\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}.$$

$P^T=P$, and $P^2=\frac1{25}\begin{bmatrix}5&10\\10&20\end{bmatrix}=P$.
Also $\|\mathbf b\|^2=10=\|\mathbf p\|^2+\|\mathbf e\|^2=5+5$.
::::

::::{div} key-answer

The residual is perpendicular to the **line**, and the result lies on the line. Check both.
::::
:::::

```{figure} ../figures/lecture4/line-projection.svg
:alt: On fixed x,y axes, b=(3,1) splits into p=(1,2) on the line through (1,2) and residual e=(2,-1). A right-angle marker shows perpendicularity.

Projection chooses the perpendicular foot. The residual arrow starts at p and ends at b.
```

:::{admonition} Pitfall · Unit-vector shortcuts have a condition
:class: pitfall

Use $\mathbf p=(\mathbf a^T\mathbf b)\mathbf a$ only when $\|\mathbf a\|=1$. Otherwise divide by $\mathbf a^T\mathbf a$. A zero direction cannot define this line formula; projection onto $\{0\}$ is simply zero.
:::

:::{admonition} Check your understanding
:class: checkpoint

If $\mathbf a$ is replaced by $7\mathbf a$, does the projected vector change?
:::

:::{dropdown} Check your reasoning

No. The scalar coefficient becomes $\widehat x/7$, while multiplying by $7\mathbf a$ gives the same $\mathbf p$. The line and its projection matrix are unchanged.
:::

::::{div} section-recap

**Takeaway:** A line projection is a multiple plus a perpendicular residual. Practice: Problem 8; then continue to several columns.
::::

(w4-practice-projection)=
## Practice · Orthogonality and line projections

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- projection:start -->
:end-before: <!-- projection:end -->
```

**Next:** {ref}`Page 2 · Subspaces and least squares <w4-least-squares>` replaces one line direction with several columns.
