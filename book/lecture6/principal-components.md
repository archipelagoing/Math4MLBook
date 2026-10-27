(w6-principal-components)=
# Compute principal components

<div class="chapter-kicker">Lecture 6 · Page 2 of 4 · Center the data, keep its strongest variation</div>

PCA’s two descriptions are equivalent: **minimize squared reconstruction error** or **maximize the variation retained in orthogonal projections**. We derive that equivalence, then carry the lecture’s student dataset from its raw table to scores and a checked reconstruction.

<nav class="lecture-path" aria-label="Lecture 6 learning path">
<a href="index.html"><span class="path-number">01</span><span>Statistics & PCA geometry</span></a>
<a href="principal-components.html" aria-current="page"><span class="path-number">02</span><span>Compute principal components</span></a>
<a href="applications.html"><span class="path-number">03</span><span>Scaling, applications & pitfalls</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Follow the lecture**

- {ref}`F · The reconstruction objective <w6-objective>`
- {ref}`G · Why covariance eigenvectors are optimal <w6-eigenproblem>`
- {ref}`H · Find and use the components <w6-algorithm>`
- {ref}`I · Explained variance and choosing k <w6-explained>`
::::

(w6-objective)=
## F · The reconstruction objective

::::{div} section-intro

**Learning goal:** Relate shortest perpendicular errors to the sum of squared retained coordinates.

<span class="source-label">Lecture PDF pages 15–19</span>
::::

:::{admonition} Definition · Directions, scores and reconstruction
:class: definition

Let $Q_k=[\mathbf q_1\ \cdots\ \mathbf q_k]\in\mathbb R^{n\times k}$ have orthonormal columns. For a centered observation $\mathbf x\in\mathbb R^n$,

$$\mathbf z=Q_k^T\mathbf x\in\mathbb R^k,\quad \widehat{\mathbf x}=Q_k\mathbf z=Q_kQ_k^T\mathbf x,\quad\mathbf e=\mathbf x-\widehat{\mathbf x}.$$

The q vectors are **principal directions/loadings** when chosen optimally; z contains that observation’s **scores**. The reconstructed original point is $\widehat{\mathbf d}=\boldsymbol\mu+\widehat{\mathbf x}$. Do not confuse a direction, a score vector and a reconstructed feature vector.
:::

```{figure} ../figures/lecture6/projection-objective.svg
:alt: A centered vector splits into its projection on a unit direction and a perpendicular residual. Pythagoras separates total squared length into retained squared score and residual squared length; a cloud’s long direction retains more score variation than its short direction.

The projection triangle and long/short-axis question from pages 15–19. Residuals are perpendicular to the chosen subspace, rather than vertical distances to a fitted response line.
```

:::{admonition} Result · Two views of one optimization
:class: key-result

For centered rows $\mathbf x_i^T$ of X and $1\le k\le n$,

$$\min_{Q_k^TQ_k=I_k}\frac1m\sum_i\|\mathbf x_i-Q_kQ_k^T\mathbf x_i\|^2$$

is equivalent to

$$\max_{Q_k^TQ_k=I_k}\frac1m\sum_i\sum_{j=1}^k(\mathbf x_i^T\mathbf q_j)^2.$$

For each observation, Pythagoras gives

$$\|\mathbf x_i\|^2=\|\mathbf e_i\|^2+\sum_j(\mathbf x_i^T\mathbf q_j)^2.$$

The total on the left is fixed, so retaining more squared length leaves less error. Unit lengths and orthogonality are essential: scaling a direction arbitrarily or counting the same direction twice would not represent a projection.
:::

:::::{admonition} Worked example 6.6 · Check the objective identity on one vector
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Project and reconstruct</span>

For $\mathbf x=(2,1)^T$ and $\mathbf q=(1,0)^T$, the score is $z=\mathbf q^T\mathbf x=2$. The projection is $(2,0)^T$ and residual is $(0,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check squared lengths</span>

$\|\mathbf x\|^2=5$, $z^2=4$, $\|\mathbf e\|^2=1$; indeed $5=4+1$. The residual dot q is zero. For an entire centered cloud, maximize the **sum** of retained squared scores, not closeness to one selected point.
::::

::::{div} key-answer

PCA chooses the line for the whole dataset; projection then chooses the nearest point on that line for each observation.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Does the first PC follow the direction with the largest perpendicular residuals?
:::

:::{dropdown} Check your reasoning

No. It maximizes projected score variation and minimizes total perpendicular squared residuals. In the source’s elongated downward cloud, the long downward axis is preferred over its perpendicular short axis.
:::

::::{div} section-recap

**Takeaway:** Fixed total variation splits into retained variation plus residual error. Practice: Problems 9–10.
::::

(w6-eigenproblem)=
## G · Why covariance eigenvectors are optimal

::::{div} section-intro

**Learning goal:** Turn the projection objective into a unit-vector quadratic form and identify its maximum.

<span class="source-label">Lecture PDF pages 20–22</span>
::::

:::{admonition} Derivation · The Rayleigh-quotient argument
:class: proof

For a unit direction v, the row scores are $X\mathbf v$, so

$$\frac1m\|X\mathbf v\|^2=\frac1m\mathbf v^TX^TX\mathbf v
=\frac{m-1}{m}\mathbf v^TC\mathbf v.$$

The positive constant changes the value, not the maximizing direction. With $C=Q\Lambda Q^T$ and $\mathbf w=Q^T\mathbf v$, we have $\|\mathbf w\|=1$ and

$$\mathbf v^TC\mathbf v=\sum_j\lambda_jw_j^2\le\lambda_1\sum_jw_j^2=\lambda_1.$$

Equality holds for a unit vector in the largest-eigenvalue eigenspace. If the largest eigenvalue is simple, both $\mathbf q_1$ and $-\mathbf q_1$ work. For k directions, take orthonormal eigenvectors for the k largest eigenvalues. Repeated eigenvalues permit different orthonormal choices; eigenvalue zero carries no variation.

The sample variance of score column $X\mathbf q_j$ is $\lambda_j$, and
$\operatorname{Cov}(XQ_k)=Q_k^TCQ_k=\operatorname{diag}(\lambda_1,\ldots,\lambda_k)$.
Thus scores are uncorrelated on the fitted data, which does not imply statistical independence.
:::

:::::{admonition} Worked example 6.7 · The recurring marked-point cloud
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State and center all four records</span>

Use fixed calibrated XY records $(3,2),(2,3),(1,0),(0,1)$ for four labeled points. Their mean is $(3/2,3/2)^T$ and

$$X=\begin{bmatrix}3/2&1/2\\1/2&3/2\\-1/2&-3/2\\-3/2&-1/2\end{bmatrix},\qquad
C=\frac13X^TX=\begin{bmatrix}5/3&1\\1&5/3\end{bmatrix}.$$

::::

::::{div} worked-step

<span class="step-label">Step 2 · Find the principal directions</span>

$C(1,1)^T=(8/3)(1,1)^T$, while $C(1,-1)^T=(2/3)(1,-1)^T$. Normalize both by $\sqrt2$. The first has sample score variance $8/3$, the second $2/3$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Take the retained scores and check their meaning</span>

Along $\mathbf q_1=(1,1)^T/\sqrt2$, scores are $(\sqrt2,\sqrt2,-\sqrt2,-\sqrt2)^T$. Distinct points can now have the same score. Keeping this direction summarizes their main variation; it does not recover unmeasured depth or establish that paired points were physically identical.
::::

::::{div} key-answer

This is PCA of a collection of measured point records, distinct from projecting one world point onto a screen.
::::
:::::

:::{admonition} Connection · PCA is centered SVD
:class: connection

If $X=U\Sigma V^T$ is the SVD of the **centered** row-data matrix, then

$$C=V\frac{\Sigma^T\Sigma}{m-1}V^T,\qquad \boxed{\lambda_j=\frac{\sigma_j^2}{m-1}}.$$

The right singular vectors are principal directions; $Z=XV_k=U_k\Sigma_k$ contains scores. Centered rank is at most $\min(n,m-1)$. PCA reconstruction is the truncated SVD of X, followed by adding the mean. Running SVD on raw uncentered D generally answers a different question.
:::

:::{admonition} Check your understanding
:class: checkpoint

Do $X^TX$, $X^TX/m$, and $C=X^TX/(m-1)$ have the same eigenvalues?
:::

:::{dropdown} Check your reasoning

No. They have the same eigendirections but differently scaled eigenvalues. Their maximizing subspaces and explained-variance ratios agree; report numerical variance using the declared denominator.
:::

::::{div} section-recap

**Takeaway:** Use covariance eigenvalues for sample score variances, and square singular values before converting. Practice: Problems 11–12.
::::

(w6-algorithm)=
## H · Find and use the components

::::{div} section-intro

**Learning goal:** Carry the complete source dataset through centering, covariance, normalized eigenvectors and scores.

<span class="source-label">Lecture PDF pages 23–24</span>
::::

Use this sequence: choose features/units → subtract feature means → compute covariance → sort and normalize its eigenvectors → retain k → form scores → reconstruct when requested. The next page addresses the optional scaling decision; this source example uses its original numerical units.

:::::{admonition} Worked example 6.8 · The lecture’s complete study-time / exam-score PCA
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Write the original data and center each feature</span>

| Student | Study time | Exam score |
| --- | ---: | ---: |
| 1 | 10 | 90 |
| 2 | 6 | 80 |
| 3 | 20 | 100 |

The column means are $(12,90)^T$, so

$$D=\begin{bmatrix}10&90\\6&80\\20&100\end{bmatrix},\qquad
X=\begin{bmatrix}-2&0\\-6&-10\\8&10\end{bmatrix}.$$

Each centered column sums to zero.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compute covariance entry by entry</span>

$$X^TX=\begin{bmatrix}4+36+64&0+60+80\\0+60+80&0+100+100\end{bmatrix}
=\begin{bmatrix}104&140\\140&200\end{bmatrix}.$$

Divide by $m-1=2$:

$$C=\begin{bmatrix}52&70\\70&100\end{bmatrix}.$$

::::

::::{div} worked-step

<span class="step-label">Step 3 · Solve and normalize the eigendirections</span>

$$\det(C-\lambda I)=(52-\lambda)(100-\lambda)-70^2
=\lambda^2-152\lambda+300=(\lambda-150)(\lambda-2).$$

At 150, $-98a+70b=0$, giving the source vector $(5/7,1)^T$, or equivalently $(5,7)^T$.
At 2, $50a+70b=0$, giving $(-7/5,1)^T$, or $(-7,5)^T$.
Thus

$$\mathbf q_1=\frac1{\sqrt{74}}\begin{bmatrix}5\\7\end{bmatrix},\qquad
\mathbf q_2=\frac1{\sqrt{74}}\begin{bmatrix}-7\\5\end{bmatrix}.$$

Both are unit, their dot product is $(-35+35)/74=0$, and $C\mathbf q_j=\lambda_j\mathbf q_j$.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Project every student onto the first direction</span>

$$\begin{aligned}
z_1&=\frac{5(-2)+7(0)}{\sqrt{74}}=\frac{-10}{\sqrt{74}}\approx-1.1625,\\
z_2&=\frac{5(-6)+7(-10)}{\sqrt{74}}=\frac{-100}{\sqrt{74}}\approx-11.6248,\\
z_3&=\frac{5(8)+7(10)}{\sqrt{74}}=\frac{110}{\sqrt{74}}\approx12.7872.
\end{aligned}$$

The exact scores sum to zero; their sample variance is
$(100+10000+12100)/(74\cdot2)=150$. The source’s displayed decimals are approximations; keeping exact vectors until the end avoids rounding drift.
::::

::::{div} key-answer

Two features per student become one centered score. The loading is the two-entry unit vector q₁; the three entries in Xq₁ are student scores, not three principal directions.
::::
:::::

```{figure} ../figures/lecture6/student-pca.svg
:alt: The three source students are shown relative to their mean (12,90). Their centered points project onto the line in direction (5,7); residuals join the originals to the nearest points on that line.

A fully labeled reconstruction of the source calculation. The PCA line passes through the mean in original coordinates and through zero after centering.
```

:::{admonition} Check your understanding
:class: checkpoint

For a new student, should you recompute the means using that one new row before calculating its score?
:::

:::{dropdown} Check your reasoning

No. Apply the already fitted training means, optional scales and principal directions to the new row. Re-estimating preprocessing would change the coordinate system.
:::

::::{div} section-recap

**Takeaway:** The fitted model includes the mean and the basis, not just a list of scores. Practice: Problems 13–14.
::::

(w6-explained)=
## I · Explained variance and choosing k

::::{div} section-intro

**Learning goal:** Select a retained dimension and verify its variance and reconstruction-error accounting.

<span class="source-label">Lecture PDF pages 25–26</span>
::::

:::{admonition} Result · Variance fraction and residual error
:class: key-result

When total variance $\sum_j\lambda_j>0$,

$$\boxed{\operatorname{EVR}(k)=\frac{\sum_{j\le k}\lambda_j}{\sum_j\lambda_j}}.$$

Choose the smallest k meeting a declared target, if variance retention is the chosen criterion. The slide’s **90–95%** is a heuristic, not a universal rule or exam grading threshold. With row-data sample covariance,

$$\|X-XQ_kQ_k^T\|_F^2=(m-1)\sum_{j>k}\lambda_j,$$

so the average squared error per observation is $(m-1)\sum_{j>k}\lambda_j/m$. When all data are constant, total variance is zero and the fraction is undefined. Ties may make the chosen basis or retained subspace nonunique.
:::

:::::{admonition} Worked example 6.9 · Finish the source’s variance quiz and reconstruction
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compute the fraction without rounding</span>

For the student example, the retained fraction is $150/(150+2)=75/76\approx98.6842\%$. Of the source quiz choices **50%, 75%, 90%, 99%**, choose **99%**. One component meets either a 90% or 95% retention target.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct in the original feature coordinates</span>

Use $\widehat{\mathbf d}_i=(12,90)^T+z_i\mathbf q_1$. For student 1,

$$\widehat{\mathbf d}_1=\begin{bmatrix}12\\90\end{bmatrix}
+\frac{-10}{74}\begin{bmatrix}5\\7\end{bmatrix}
=\begin{bmatrix}419/37\\3295/37\end{bmatrix}
\approx\begin{bmatrix}11.3243\\89.0541\end{bmatrix}.$$

The other reconstructed rows are $(194/37,2980/37)$ and $(719/37,3715/37)$. The mean must be added back.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check perpendicularity and total loss</span>

Original-minus-reconstructed residual rows are

$$E=\frac1{37}\begin{bmatrix}-49&35\\28&-20\\21&-15\end{bmatrix}.$$

Every residual row has dot product zero with $(5,7)^T$. Their total squared length is $4=(3-1)\lambda_2$; average squared error is $4/3$. Discarded **sample variance** is $2$, a different normalization.
::::

::::{div} key-answer

Retained variance: about 98.7%. Total squared reconstruction error: 4. The two values agree with the same eigenvalue accounting.
::::
:::::

```{figure} ../figures/lecture6/variance-budget.svg
:alt: Two equal-height bars show total sample variance 152. The original feature variances are 52 and 100; the principal-coordinate variances are 150 and 2. Retaining the first gives 75/76 of the total.

The variance-budget figure from page 26. Orthogonal re-expression preserves the trace; discarding PC2 leaves 150 of the total 152.
```

:::{admonition} Pitfall · Percentages depend on the preprocessing metric
:class: pitfall

The 98.7% result uses the original numerical units of study time and exam score. Rescaling a feature, such as converting hours to minutes, can change covariance PCA. Standardizing first defines a different metric and can produce different loadings and percentages.
:::

:::{admonition} Check your understanding
:class: checkpoint

Does retaining one of two original features imply retaining half the variance?
:::

:::{dropdown} Check your reasoning

No. PCA retains directions, not necessarily original feature columns, and the eigenvalues can be very unequal. Here one combined direction retains about 98.7% rather than 50%.
:::

::::{div} section-recap

**Takeaway:** Report the chosen k, normalization and error as well as the percentage. Practice: Problems 15–16.
::::

(w6-practice-compute)=
## Practice · Principal components and variance accounting

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- compute:start -->
:end-before: <!-- compute:end -->
```

**Next:** {ref}`Page 3 · Scaling, applications and pitfalls <w6-applications>` makes the preprocessing choices and limits explicit.
