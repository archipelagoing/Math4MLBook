(w6-index)=
# Statistics and PCA geometry

<div class="chapter-kicker">Lecture 6 · Page 1 of 4 · Center the data, keep its strongest variation</div>

Principal component analysis (PCA) replaces many correlated measurements with fewer coordinates while preserving as much variation as possible. We first learn how to measure variation, then derive and compute its best directions. This chapter includes the full 39-page Week 6 deck; no slides need to be open beside the website.

<nav class="lecture-path" aria-label="Lecture 6 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Statistics & PCA geometry</span></a>
<a href="principal-components.html"><span class="path-number">02</span><span>Compute principal components</span></a>
<a href="applications.html"><span class="path-number">03</span><span>Scaling, applications & pitfalls</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Recall {ref}`orthogonal projections <w4-subspace>`, {ref}`the symmetric spectral theorem <w5-spectral>` and {ref}`SVD <w5-svd-meaning>`. Throughout, **rows are observations and columns are features**. There are $m$ observations and $n$ features. Unless stated otherwise, covariance and variance use the sample denominator $m-1$, requiring $m>1$.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`A · Why reduce dimensions? <w6-dimensions>`
- {ref}`B · Mean and centering <w6-mean>`
- {ref}`C · Variance and standard deviation <w6-variance>`
- {ref}`D · Covariance and its matrix <w6-covariance>`
- {ref}`E · From a point cloud to a few coordinates <w6-geometry>`
::::

(w6-dimensions)=
## A · Why reduce dimensions?

::::{div} section-intro

**Learning goal:** Distinguish the number of measured features from the number of directions needed to describe variation.

<span class="source-label">Lecture PDF pages 1–4</span>
::::

:::::{admonition} Worked example 6.1 · One image is one high-dimensional observation
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Count the entries</span>

The lecture’s image has $300\times300$ pixels with three channels per pixel (R,G,B): $300\cdot300\cdot3=270{,}000$ numbers. For example, its magnified first pixel has channel values $(251,244,239)$. Flattening all pixels in a fixed order makes one vector in $\mathbb R^{270000}$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Separate ambient size from variation</span>

Many such images form many rows of a dataset, not 270,000 observations in one image. If their patterns vary together, their centered rows may lie near a much smaller subspace. Fewer coordinates can ease computation, visualization and interpretation.
::::

::::{div} key-answer

High ambient dimension does not force high intrinsic linear dimension. A compact approximation still has an error that must be measured.
::::
:::::

```{figure} ../figures/lecture6/dimensions.svg
:alt: A fixed-order RGB pixel array becomes one long observation row. A second schematic panel shows three-dimensional points near a plane, where two coordinates can describe most variation.

The image-entry count and near-plane idea from pages 2–4, redrawn without needing the original photograph. A plane is an approximation when points do not lie exactly on it.
```

:::{admonition} Definition · Dimensionality reduction
:class: definition

Dimensionality reduction maps $n$ feature values to $k<n$ coordinates. PCA chooses a **linear subspace for centered data**. In original coordinates, the reconstructed data lie on an affine set through the mean. It preserves large sample variation, not necessarily every useful distinction.
:::

:::{admonition} Check your understanding
:class: checkpoint

Does a point cloud drawn in three dimensions always need three PCA coordinates?
:::

:::{dropdown} Check your reasoning

No. A cloud near a plane may be approximated with two, and one near a line with one. Whether that approximation is adequate depends on the lost variation and the task.
:::

::::{div} section-recap

**Takeaway:** Count features first; then assess how many independent directions carry variation. Practice: Problem 1.
::::

(w6-mean)=
## B · Mean and centering

::::{div} section-intro

**Learning goal:** Compute a mean and translate observations to deviations from it.

<span class="source-label">Lecture PDF pages 5</span>
::::

:::{admonition} Definition · Empirical mean
:class: definition

For numbers $x_1,\ldots,x_m$,

$$\mu=\frac1m\sum_{i=1}^m x_i.$$

For a data matrix $D\in\mathbb R^{m\times n}$, compute a separate mean $\mu_j$ for each column. The centered matrix is

$$X=D-\mathbf1_m\boldsymbol\mu^T,\qquad X_{ij}=D_{ij}-\mu_j,$$

where $\boldsymbol\mu\in\mathbb R^n$ and $\mathbf1_m$ is a column of ones. Every centered column sums to zero. Subtract each **feature’s** mean, not a separate mean from each observation row.
:::

:::::{admonition} Worked example 6.2 · The source’s mean calculation
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Average the three numbers</span>

For $\{3,7,5\}$, $\mu=(3+7+5)/3=5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Center and check</span>

The deviations are $(3-5,7-5,5-5)=(-2,2,0)$. Their sum is zero. Adding $5$ back recovers the original numbers.
::::

::::{div} key-answer

Centering changes the origin, not the distances between observations.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

If every value in a feature increases by 100, what changes after centering?
:::

:::{dropdown} Check your reasoning

The mean increases by 100, but every deviation stays the same. Centered covariance PCA therefore has the same directions and scores for that translated feature.
:::

::::{div} section-recap

**Takeaway:** PCA should describe variation around the mean, not merely distance from an arbitrary origin. Practice: Problems 2–3.
::::

(w6-variance)=
## C · Variance and standard deviation

::::{div} section-intro

**Learning goal:** Measure spread with a declared denominator and restore the original units with a square root.

<span class="source-label">Lecture PDF pages 6</span>
::::

:::{admonition} Definition · Sample variance and standard deviation
:class: definition

The sample variance and standard deviation are

$$s_x^2=\frac1{m-1}\sum_{i=1}^m(x_i-\mu_x)^2,\qquad s_x=\sqrt{s_x^2}.$$

Variance has squared feature units; standard deviation has the feature’s original units. The lecture writes $\sigma^2$ but uses the sample denominator $m-1$. We write $s^2$ to make that convention explicit. A population/descriptive convention uses $m$ instead; never switch denominators silently.
:::

:::::{admonition} Worked example 6.3 · The source’s spread calculation, plus standard deviation
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Square the deviations</span>

The mean of $\{3,7,5\}$ is $5$, so the squared deviations are $4,4,0$, with total $8$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Divide by the sample degrees of freedom</span>

Here $m=3$, so $s^2=8/(3-1)=4$. Taking the square root gives $s=2$. With the alternate denominator $m$, the variance would be $8/3$, a different declared convention.
::::

::::{div} key-answer

Sample variance is $4$ and sample standard deviation is $2$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

A column is constant. What are its variance and standard deviation? Can you standardize it by dividing by its standard deviation?
:::

:::{dropdown} Check your reasoning

Both are zero. Division is undefined; remove the constant feature or handle it explicitly before standardization. It contributes no centered variance.
:::

::::{div} section-recap

**Takeaway:** Square, sum, divide by m−1, then take a square root only if standard deviation is requested. Practice: Problems 4–5.
::::

(w6-covariance)=
## D · Covariance and its matrix

::::{div} section-intro

**Learning goal:** Measure co-variation and assemble a symmetric feature-by-feature matrix.

<span class="source-label">Lecture PDF pages 7–8</span>
::::

:::{admonition} Definition · Sample covariance
:class: definition

For paired observations of features x and y,

$$\operatorname{Cov}(x,y)=\frac1{m-1}\sum_i(x_i-\mu_x)(y_i-\mu_y).$$

Positive values mean deviations tend to have matching signs; negative values mean opposite signs. Magnitude depends on feature units, so covariance is not a scale-free strength measure. Zero covariance does **not** imply statistical independence.

For two features and then n features,

$$C=\begin{bmatrix}s_x^2&\operatorname{Cov}(x,y)\\\operatorname{Cov}(y,x)&s_y^2\end{bmatrix},\qquad
\boxed{C=\frac1{m-1}X^TX\in\mathbb R^{n\times n}}.$$

$C$ is symmetric and positive semidefinite, because $\mathbf v^TC\mathbf v=\|X\mathbf v\|^2/(m-1)\ge0$. Its diagonal entries are feature variances; covariance of a feature with itself is its variance.
:::

:::::{admonition} Worked example 6.4 · Covariance from the same centered-number pattern
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Pair observations before multiplying</span>

Let $x=(3,7,5)$ and $y=(2,6,4)$. Their means are $5,4$; both centered columns are $(-2,2,0)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compute every matrix entry</span>

Each sample variance is $(4+4+0)/2=4$. The covariance is $((-2)(-2)+2(2)+0)/2=4$, so

$$C=\begin{bmatrix}4&4\\4&4\end{bmatrix}.$$

The repeated centered columns explain the redundancy. Scaling y by 10 would scale the covariance by 10 and its variance by 100.
::::

::::{div} key-answer

Always preserve row pairing and the feature order in C. This numerical covariance example is an editorial extension of the source definitions.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Why does $XX^T$ not have the same feature-covariance interpretation as $X^TX$?
:::

:::{dropdown} Check your reasoning

With rows as observations, $X^TX$ is n×n and compares features. $XX^T$ is m×m and compares observation rows. Both are Gram matrices, but only the former divided by m−1 is our feature covariance matrix.
:::

::::{div} section-recap

**Takeaway:** Covariance compares centered columns, in the original feature units. Practice: Problems 6–7.
::::

(w6-geometry)=
## E · From a point cloud to a few coordinates

::::{div} section-intro

**Learning goal:** Interpret the source’s pizza/gym cloud as a change of coordinates followed by deliberate information loss.

<span class="source-label">Lecture PDF pages 9–14</span>
::::

The source plots **pizza attendance horizontally and gym attendance vertically**. Its downward cloud suggests that a contrast between the two counts carries most of the variation. This is an illustrative association; it does not establish that one activity causes the other. The figures below reproduce the geometry using declared toy coordinates, because the slides supply no numerical table for their scatter points.

```{figure} ../figures/lecture6/pizza-gym.svg
:alt: Five toy pizza/gym counts form a downward line. Centering moves its mean to zero; perpendicular axes split the long contrast direction from the short direction; retaining one coordinate drops the short direction.

The sequence from pages 9–14: find long/short axes, express points in those axes, then drop the short coordinate. Orthogonal re-expression alone is reversible; discarding a coordinate is the reduction.
```

:::::{admonition} Worked example 6.5 · Compress a fully specified pizza/gym dataset
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State and center the toy observations</span>

Use $(1,5),(2,4),(3,3),(4,2),(5,1)$. The mean is $(3,3)^T$, so centered rows are $(-2,2),(-1,1),(0,0),(1,-1),(2,-2)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Take long and short coordinates</span>

Choose unit directions $\mathbf q_1=(1,-1)^T/\sqrt2$ and $\mathbf q_2=(1,1)^T/\sqrt2$.
The first scores are $(-2\sqrt2,-\sqrt2,0,\sqrt2,2\sqrt2)$; every second score is zero because each centered row’s entries sum to zero.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check what was lost</span>

For any first score t, reconstruction is $(3,3)^T+t\mathbf q_1$. It recovers every listed point exactly. A noisy cloud around this line would have nonzero short-direction scores, and dropping them would incur error.
::::

::::{div} key-answer

One signed contrast coordinate suffices for these five points. The source’s noisy picture is approximate; this toy line is exact.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

If you keep both orthogonal coordinates of a two-feature point, have you reduced its dimension?
:::

:::{dropdown} Check your reasoning

No. You have changed basis. Dimension reduction begins when you retain fewer coordinates; reconstruction then generally has a residual.
:::

::::{div} section-recap

**Takeaway:** Rotate the coordinate description, then distinguish retained information from discarded variation. Practice: Problem 8.
::::

(w6-practice-statistics)=
## Practice · Statistics and projection geometry

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- statistics:start -->
:end-before: <!-- statistics:end -->
```

**Next:** {ref}`Page 2 · Compute principal components <w6-principal-components>` derives why eigenvectors choose the best axes.
