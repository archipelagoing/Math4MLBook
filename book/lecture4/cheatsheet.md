(w4-cheatsheet)=
# TL;DR · Orthogonality, projection, and fitting

<div class="chapter-kicker">Lecture 4 · Page 4 of 4 · Finding the closest possible record</div>

**Choose the target subspace, fit inside it, then check the leftover error is perpendicular to it.** Keep this page beside fresh practice; the other three pages explain why the recipes work.

<nav class="lecture-path" aria-label="Lecture 4 learning path">
<a href="index.html"><span class="path-number">01</span><span>Orthogonality & projections</span></a>
<a href="least-squares.html"><span class="path-number">02</span><span>Subspaces & least squares</span></a>
<a href="orthonormal.html"><span class="path-number">03</span><span>Orthonormal bases & Gram–Schmidt</span></a>
<a href="cheatsheet.html" aria-current="page"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Pick the method

| Given or asked | Use | Check before starting |
| --- | --- | --- |
| Are vectors/subspaces orthogonal? | All relevant dot products | Same ambient space; test every basis pair |
| Nearest vector on one line | Line projection | Nonzero direction |
| Nearest output in a column space / best fit | Normal equations | Inverse formula needs independent columns |
| Orthonormal basis already given | Dot-product coefficients | Both perpendicularity and unit length |
| Construct an orthonormal basis | Gram–Schmidt | Never normalize a zero remainder |

## Essential formulas and conditions

:::{admonition} Keep these together
:class: key-result

**Orthogonality:** $\mathbf v^T\mathbf w=0$. Then
$\|\mathbf v+\mathbf w\|^2=\|\mathbf v\|^2+\|\mathbf w\|^2$.

**Four spaces:** for rank-$r$ $A\in\mathbb R^{m\times n}$,
$C(A^T)=N(A)^\perp$ in $\mathbb R^n$ (dimensions $r,n-r$);
$C(A)=N(A^T)^\perp$ in $\mathbb R^m$ (dimensions $r,m-r$).

**One line, $\mathbf a\ne0$:**

$$\widehat x=\frac{\mathbf a^T\mathbf b}{\mathbf a^T\mathbf a},\qquad
\mathbf p=\widehat x\mathbf a,\qquad P=\frac{\mathbf a\mathbf a^T}{\mathbf a^T\mathbf a}.$$

**General fit:** solve $A^TA\widehat{\mathbf x}=A^T\mathbf b$;
$\mathbf p=A\widehat{\mathbf x}$, $\mathbf e=\mathbf b-\mathbf p$, $A^T\mathbf e=0$.
With independent columns only,

$$\widehat{\mathbf x}=(A^TA)^{-1}A^T\mathbf b,\qquad P=A(A^TA)^{-1}A^T.$$

**Orthonormal columns:** $Q^TQ=I$, $\widehat{\mathbf c}=Q^T\mathbf b$, $\mathbf p=QQ^T\mathbf b$.
For **square** $Q$, also $Q^{-1}=Q^T$ and $QQ^T=I$.

**Orthogonal projectors:** $P^T=P$, $P^2=P$; $I-P$ projects onto the perpendicular complement. The minimum squared error is $\|\mathbf e\|^2$, and
$\|\mathbf b\|^2=\|\mathbf p\|^2+\|\mathbf e\|^2$.
:::

## Solve in this order

1. **Declare the model and dimensions.** Identify the target span. For a line fit $y=c+mt$, use one row $[1\ t_i]$ per data point, with coefficients in the order $(c,m)$.
2. **Choose the shortest valid calculation.** One direction: line ratio. Orthonormal columns: dot products. Other columns: form and solve the normal equations. Check rank before writing an inverse.
3. **Reconstruct the output.** Compute p from the coefficients; the coefficients themselves may live in a different space.
4. **Check and stop.** Verify p lies in the target span and the residual is perpendicular to **every** spanning direction. Report the squared error if requested. Dependent columns can give multiple coefficients but only one closest output.

## Build a basis in this order

1. Keep the first nonzero input and normalize it.
2. For each later input, subtract its projections onto **all** previously kept unit directions:

$$\mathbf u_j=\mathbf a_j-\sum_{i<j}(\mathbf q_i^T\mathbf a_j)\mathbf q_i.$$

3. If $\mathbf u_j=0$, skip it when finding a basis for the span. Otherwise set $\mathbf q_j=\mathbf u_j/\|\mathbf u_j\|$.
4. Stop after processing every input. Verify $Q^TQ=I$ and that the kept directions span the original list.

:::::{admonition} Worked example 4.14 · A compact fresh projection
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Take the two dot products</span>

Project $\mathbf b=(2,0,1)^T$ onto $\mathbf a=(1,1,0)^T$. The ratio is $\widehat x=(2+0+0)/(1+1+0)=1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and check</span>

$\mathbf p=(1,1,0)^T$, $\mathbf e=(1,-1,1)^T$. Then $\mathbf a^T\mathbf e=1-1+0=0$ and $\|\mathbf e\|^2=3$. Also $\|\mathbf b\|^2=5=2+3$.
::::

::::{div} key-answer

Nearest vector: $(1,1,0)^T$. Coefficient: $1$. Squared distance: $3$.
::::
:::::

:::{admonition} Before you hand it in
:class: pitfall

Do not omit the denominator for a nonunit direction; confuse $\mathbf p$ with $\widehat{\mathbf x}$; invert a singular Gram matrix; assume rectangular $QQ^T=I$; normalize zero; or call vertical line-fit residuals perpendicular distances in the data plot.

$P^2=P$ alone does not prove **orthogonal** projection: also check $P^T=P$. If you flip the residual sign, keep the convention consistent; the squared error is unchanged.
:::

**Rehearse:** {ref}`mixed Problems 25–28 <w4-readiness>` → diagnose mistakes → return to the linked part → retry with changed data. The chapter explains {ref}`orthogonality <w4-orthogonality>`, {ref}`normal equations <w4-subspace>`, {ref}`line fitting <w4-least-squares-fit>` and {ref}`Gram–Schmidt <w4-gram-schmidt>`.
