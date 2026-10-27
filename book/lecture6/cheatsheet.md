(w6-cheatsheet)=
# TL;DR · Statistics and principal components

<div class="chapter-kicker">Lecture 6 · Page 4 of 4 · Center the data, keep its strongest variation</div>

**Choose the feature order and units, center, compute covariance, find the largest-eigenvalue directions, project, and check the variance/error budget.** This page is a compact method reference; the chapter’s examples explain each operation.

<nav class="lecture-path" aria-label="Lecture 6 learning path">
<a href="index.html"><span class="path-number">01</span><span>Statistics & PCA geometry</span></a>
<a href="principal-components.html"><span class="path-number">02</span><span>Compute principal components</span></a>
<a href="applications.html"><span class="path-number">03</span><span>Scaling, applications & pitfalls</span></a>
<a href="cheatsheet.html" aria-current="page"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Quantities and shapes

| Quantity | Formula / meaning | Shape or condition |
| --- | --- | --- |
| Mean | Feature-wise average | n entries |
| Centered data | Subtract the same feature mean from every row | m×n, column sums zero |
| Sample covariance | C=XᵀX/(m−1) | n×n, m>1 |
| Loadings Qₖ | Top k orthonormal covariance eigenvectors | n×k |
| Scores Z | XQₖ | m×k |
| Reconstructed deviations | ZQₖᵀ | m×n |
| Reconstructed observations | Add feature means back | m×n |

:::{admonition} Keep these formulas and conventions
:class: key-result

**Statistics:**

$$\mu=\frac1m\sum_i x_i,\qquad
s_x^2=\frac1{m-1}\sum_i(x_i-\mu)^2,\qquad s_x=\sqrt{s_x^2},$$

$$\operatorname{Cov}(x,y)=\frac1{m-1}\sum_i(x_i-\mu_x)(y_i-\mu_y).$$

Paired rows must stay paired. Covariance with itself is variance. Changing to denominator m changes values, not a fixed dataset’s principal directions.

**PCA:**

$$X=D-\mathbf1_m\boldsymbol\mu^T,\quad C=\frac{X^TX}{m-1},\quad C\mathbf q_j=\lambda_j\mathbf q_j,$$

with $\lambda_1\ge\cdots\ge\lambda_n\ge0$, $Q_k^TQ_k=I$.
For a column observation, $\mathbf z=Q_k^T(\mathbf d-\boldsymbol\mu)$ and
$\widehat{\mathbf d}=\boldsymbol\mu+Q_k\mathbf z$.

**Variance and error:** for positive total variance,

$$\operatorname{EVR}(k)=\frac{\sum_{j\le k}\lambda_j}{\sum_j\lambda_j},\qquad
\operatorname{SSE}=(m-1)\sum_{j>k}\lambda_j.$$

Average squared error is SSE/m. A target such as 95% is a chosen retention criterion, not a prediction guarantee. Zero total variance makes EVR undefined.

**Centered SVD bridge:** if $X=U\Sigma V^T$, loadings are right singular vectors,
$\lambda_j=\sigma_j^2/(m-1)$, and $Z=XV_k=U_k\Sigma_k$.

**Optional standardization:** $Y_{ij}=(D_{ij}-\mu_j)/s_j$ for $s_j>0$. Fit PCA on Y; undo with $\widehat D_{ij}=\mu_j+s_j\widehat Y_{ij}$. This changes the metric and may change the PCs.
:::

## Solve in order

1. **Declare** rows/columns, units, sample or population denominator, and whether you standardize. Remove or explicitly handle constant features before division.
2. **Center** feature columns. Check each sums to zero. If scaling, divide by the fitted feature standard deviations.
3. **Build covariance** with the matching denominator. Check symmetry and nonnegative diagonal entries.
4. **Find and sort eigenvalues.** Solve each eigenspace and choose orthonormal directions; normalize before projection. Keep eigenvalue/vector order matched.
5. **Select k** using the requested dimension or the smallest cumulative variance fraction meeting the declared target. Tied directions may not be unique.
6. **Calculate scores**, then reconstruct if requested. Restore scales and means in that order.
7. **Verify** unit/orthogonal loadings, score means zero, score sample variances equal retained eigenvalues, perpendicular residuals, and SSE=(m−1)×discarded variance.

:::::{admonition} Worked example 6.15 · A fresh compact full calculation
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Center and form covariance</span>

Use $D$ with rows $(0,0),(4,0),(0,2),(4,2)$. The mean is $(2,1)^T$ and centered rows are $(-2,-1),(2,-1),(-2,1),(2,1)$.

$$C=\frac13\begin{bmatrix}16&0\\0&4\end{bmatrix}=\operatorname{diag}(16/3,4/3).$$

::::

::::{div} worked-step

<span class="step-label">Step 2 · Keep the first component</span>

$\mathbf q_1=(1,0)^T$, with scores $(-2,2,-2,2)^T$. The retained variance fraction is $(16/3)/(20/3)=80\%$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Reconstruct and check the loss</span>

Add the mean back to the projected deviations: reconstructed rows are $(0,1),(4,1),(0,1),(4,1)$. Each residual has squared length 1, so SSE=$4=3(4/3)$ and average squared error is 1.
::::

::::{div} key-answer

The first coordinate retains 80% here; a 95% target would require both components.
::::
:::::

:::{admonition} Before handing it in
:class: pitfall

Do not skip centering, interchange $X^TX$ and $XX^T$, divide by the wrong denominator, use a nonunit loading, confuse directions with scores, omit the mean/scales from reconstruction, or identify uncorrelated scores with independence. High variance can reflect units or outliers; low variance can still contain useful signal. A curved pattern need not have a good straight-line reconstruction.
:::

**Rehearse:** {ref}`mixed Problems 25–28 <w6-readiness>`. Revisit {ref}`statistics <w6-variance>`, {ref}`covariance <w6-covariance>`, {ref}`the source calculation <w6-algorithm>` or {ref}`standardization <w6-scaling>` when a check fails.
