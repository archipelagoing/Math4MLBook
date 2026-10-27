(w6-applications)=
# Scaling, applications, and PCA’s limits

<div class="chapter-kicker">Lecture 6 · Page 3 of 4 · Center the data, keep its strongest variation</div>

The algebra is only part of a PCA solution. You also need to state what the features mean, whether they were scaled, and what retained variance can tell you. This page follows the source’s preprocessing sequence, genetics/eigenfaces examples, and three failure cases.

<nav class="lecture-path" aria-label="Lecture 6 learning path">
<a href="index.html"><span class="path-number">01</span><span>Statistics & PCA geometry</span></a>
<a href="principal-components.html"><span class="path-number">02</span><span>Compute principal components</span></a>
<a href="applications.html" aria-current="page"><span class="path-number">03</span><span>Scaling, applications & pitfalls</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Follow the lecture**

- {ref}`J · The complete preprocessing and reconstruction path <w6-scaling>`
- {ref}`K · Genetics and eigenfaces <w6-applications-reading>`
- {ref}`L · Failure cases and final takeaways <w6-failures>`
::::

(w6-scaling)=
## J · The complete preprocessing and reconstruction path

::::{div} section-intro

**Learning goal:** Standardize when appropriate, keep fitted parameters, and undo both scaling and centering after reconstruction.

<span class="source-label">Lecture PDF pages 27–32</span>
::::

:::{admonition} Recipe · Choose the metric before fitting
:class: definition

For each nonconstant feature, sample-standardized entries are

$$Y_{ij}=\frac{D_{ij}-\mu_j}{s_j},\qquad
C_Y=\frac1{m-1}Y^TY.$$

The diagonal of $C_Y$ is one: it is the correlation matrix. PCA on centered X uses the original numerical feature metric; PCA on Y uses standardized units. Standardization is useful when units/scales should not determine dominance, but it is a modeling decision, not an unconditional requirement. Handle $s_j=0$ explicitly.

After fitting orthonormal loadings Q in standardized coordinates, calculate

$$Z=YQ_k,\quad\widehat Y=ZQ_k^T,\quad
\boxed{\widehat D_{ij}=\mu_j+s_j\widehat Y_{ij}}.$$

Keep the fitted mean, scales and loadings for later observations. Reconstruction first restores the discarded-coordinate approximation, then rescales and adds the mean. The optimal error claim is in the metric used for fitting; standardized PCA need not minimize unweighted original-unit error.
:::

```{figure} ../figures/lecture6/preprocessing.svg
:alt: Six panels show raw paired observations, feature centering, division by feature standard deviations, computation of perpendicular principal axes, projection to the leading axis, and restoration of feature units and means.

The full six-step sequence from pages 27–32, redrawn using the declared toy observations from the next example. These are reproducible teaching points, not digitized copies of the source scatter.
```

:::::{admonition} Worked example 6.10 · Follow all six preprocessing stages
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State the toy data, means and scales</span>

For rows $(1,10),(2,20),(3,30)$, feature means are $(2,20)$.
Centered rows are $(-1,-10),(0,0),(1,10)$; sample standard deviations are $s_1=1$, $s_2=10$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Standardize and find the axes</span>

$$Y=\begin{bmatrix}-1&-1\\0&0\\1&1\end{bmatrix},\qquad
C_Y=\frac12Y^TY=\begin{bmatrix}1&1\\1&1\end{bmatrix}.$$

Its eigenvalues are $2,0$. Choose $\mathbf q_1=(1,1)^T/\sqrt2$ and $\mathbf q_2=(1,-1)^T/\sqrt2$. The axes are perpendicular and unit.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Project, reconstruct, and undo preprocessing</span>

Scores are $Z=(-\sqrt2,0,\sqrt2)^T$. Multiplying by $\mathbf q_1^T$ recovers all rows of Y. Multiply column 1 by 1, column 2 by 10, and add $(2,20)$: the original rows return exactly.
In raw units the line has slope 10; in standardized coordinates it has slope 1. The zero discarded eigenvalue explains the exact reconstruction.
::::

::::{div} key-answer

A stored score needs a shared fitted decoder: loadings, means, and any feature scales. Scores alone do not specify original-unit observations.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

If PCA was fitted on standardized features, can you reconstruct original observations by adding the mean without multiplying by the scales?
:::

:::{dropdown} Check your reasoning

No. First reconstruct standardized deviations, multiply each feature by its fitted standard deviation, then add its mean. Otherwise the result remains in the wrong units.
:::

::::{div} section-recap

**Takeaway:** Centering and scaling have separate inverses, applied in the right order. Practice: Problems 17–18.
::::

(w6-applications-reading)=
## K · Genetics and eigenfaces

::::{div} section-intro

**Learning goal:** Read real PCA application figures without confusing low-dimensional scores with original measurements.

<span class="source-label">Lecture PDF pages 33–35</span>
::::

The source moves from arithmetic to two applications. Their original empirical illustrations are included below with source credits; the supplied PDFs do not contain the underlying genetic matrix or face-training arrays, so these plots are interpreted rather than numerically re-created from invented data.

:::::{admonition} Worked example 6.11 · Read the genetics figure
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Identify observations, features and the plotted output</span>

A row represents one sampled person’s genetic measurements across many features. After the chosen preprocessing, two PCA scores place that person in a two-dimensional plot. The letters/colors in the supplied figure denote geographical groups; the map inset is a comparison, not the PCA input coordinate system.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Explain the resemblance and its limit</span>

The source uses the figure to show that genetic variation in the sampled data resembles European geography. PC axes are directions of variation, not latitude and longitude. Sign flips, rotations within tied subspaces and preprocessing conventions affect the display; the picture alone supplies no new person’s exact location or a predictive performance estimate.
::::

::::{div} key-answer

PCA can reveal structure in measured variation. Interpret the score plot together with feature definitions, sampling and source context.
::::
:::::

```{figure} ../figures/lecture6/genetics-source.png
:alt: The source genetics PCA plot has labeled PC1 and PC2 axes, many country-coded observations, larger group markers, and an inset map of Europe. The geographic resemblance is visible without opening the slides.

The empirical genetics illustration from source page 34; page 33 shows the same comparison before revealing the map. Credit: Novembre et al., “Genes mirror geography within Europe,” Nature 456 (2008), 98–101, as cited by the lecture. The original figure is reproduced from the supplied PDF, not replaced by synthetic measurements.
```

:::{admonition} Eigenfaces · A basis vector can be reshaped into an image
:class: definition

Flatten each aligned face image with a fixed pixel order. An image with p grayscale pixels is a point in $\mathbb R^p$; the **mean face** is the feature-wise mean image. Principal directions of centered face vectors can be reshaped into signed pixel patterns, called eigenfaces.
For a face vector d,

$$z_j=\mathbf q_j^T(\mathbf d-\boldsymbol\mu),\qquad
\widehat{\mathbf d}=\boldsymbol\mu+\sum_{j=1}^kz_j\mathbf q_j.$$

These q vectors live in **pixel-feature space**, so they are right singular vectors of the centered row-image matrix, or eigenvectors of its feature covariance. Signed basis patterns are not standalone people or probabilities.
:::

```{figure} ../figures/lecture6/eigenfaces-source.png
:alt: A source face is approximated by an average face plus weighted ghostlike eigenface patterns. Weights w1,w2,w3 label the first three directions; the image displays the original, mean and three component patterns side by side.

The source’s eigenface illustration (page 35). Credit in the lecture: Turk and Pentland, “Eigenfaces for recognition” (1991); eigenfaces computed from Labeled Faces in the Wild, Huang et al. (2007). The display illustrates the formula above; the original training pixels and weights are not supplied.
```

:::::{admonition} Worked example 6.12 · A fully specified four-pixel decoder
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State the shared mean and unit eigenface</span>

For a small numerical illustration, take $\boldsymbol\mu=(2,2,2,2)^T$ and a unit direction $\mathbf q=(1,-1,-1,1)^T/2$. Given image $\mathbf d=(3,1,1,3)^T$, its centered deviation is $(1,-1,-1,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Encode and reconstruct</span>

$z=\mathbf q^T(\mathbf d-\boldsymbol\mu)=2$. Then $\boldsymbol\mu+2\mathbf q=(3,1,1,3)^T=\mathbf d$, so the reconstruction error is zero. The score is one number, while the mean and unit direction are shared stored model data.
::::

::::{div} key-answer

The source’s illustrative faces have about 600 pixels, compared with 270,000 RGB entries in its opening image. Fewer per-image scores can save space across many images, but the shared mean/loadings also require storage.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Is an eigenface one of the training photographs, and is its coefficient a probability?
:::

:::{dropdown} Check your reasoning

Neither is required. An eigenface is a signed direction of pixel variation; its coefficient is a signed projection score. The mean plus weighted directions reconstructs an approximation, whose pixel values may need a separate display convention.
:::

::::{div} section-recap

**Takeaway:** Identify whether a figure shows features, principal directions, scores or reconstructions. Practice: Problems 19–20.
::::

(w6-failures)=
## L · Failure cases and final takeaways

::::{div} section-intro

**Learning goal:** Recognize outlier sensitivity, nonlinear structure and task-relevant low-variance information.

<span class="source-label">Lecture PDF pages 36–39</span>
::::

```{figure} ../figures/lecture6/failure-cases.svg
:alt: Three panels reproduce the lecture’s failure mechanisms: one far outlier changes the leading direction, a straight PCA line misses a curved arch, and dropping the short vertical direction merges classes separated vertically.

All three failure cases from page 36, redrawn with declared toy points. High retained variance alone does not establish a useful representation for a later task.
```

:::::{admonition} Worked example 6.13 · One outlier can change the first component
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compute the original covariance</span>

The three rows $(-2,0),(0,0),(2,0)$ have mean zero and sample covariance $\operatorname{diag}(4,0)$, so PC1 is horizontal.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Add one point and refit</span>

Add $(0,10)$. The new mean is $(0,5/2)$; centered rows are $(-2,-5/2),(0,-5/2),(2,-5/2),(0,15/2)$.
Their covariance is $\operatorname{diag}(8/3,25)$: the cross products cancel, horizontal squared deviations sum to 8, and vertical ones sum to 75, each divided by 3. Now PC1 is vertical.
::::

::::{div} key-answer

The variance criterion is sensitive to large deviations. This exact toy demonstrates the tilt mechanism shown in the source.
::::
:::::

A **curved** cloud creates a different issue: even if points follow a one-dimensional curve, a straight PCA subspace cannot generally reconstruct that curve without residuals. Low intrinsic nonlinear dimension does not guarantee equally low linear PCA dimension.

:::::{admonition} Worked example 6.14 · Almost all variance can miss the class distinction
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State a balanced toy dataset</span>

Take eight rows: x runs through $-3,-1,1,3$ for each of two classes; class A has y=$-1/10$ and class B has y=$1/10$. Means are zero, and cross products cancel by symmetry.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compute the retained direction and what it removes</span>

The sample covariance is $\operatorname{diag}(40/7,2/175)$.
PC1 is the horizontal axis and retains $(40/7)/(40/7+2/175)=500/501\approx99.8\%$ of variance. Yet corresponding A/B points share the same x score after y is dropped, so the class difference is completely removed.
::::

::::{div} key-answer

PCA ignores the class labels in this example. A high explained-variance fraction is not a guarantee of preserving predictive information.
::::
:::::

:::{admonition} Keep the source’s takeaways, with their conditions
:class: key-result

Center first. Decide whether feature scaling fits the task. Principal directions are top covariance eigenvectors; their eigenvalues measure sample score variance. PCA is linear, sensitive to outliers, and optimized for variation rather than a label-dependent objective. Keep the fitted preprocessing with the basis, and inspect the reconstruction or downstream consequences.
:::

:::{admonition} Check your understanding
:class: checkpoint

A single PC retains 99% of variance. Does that prove the discarded coordinates are irrelevant?
:::

:::{dropdown} Check your reasoning

No. They might distinguish classes, preserve an important measured contrast, or carry another task-specific signal. PCA’s unsupervised variance objective cannot decide that on its own.
:::

::::{div} section-recap

**Takeaway:** Check the representation against its intended use, not just its variance percentage. Practice: Problems 21–24; then the mixed rehearsal.
::::

(w6-practice-applications)=
## Practice · Scaling, interpretation and failure cases

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- applications:start -->
:end-before: <!-- applications:end -->
```

(w6-readiness)=
## Can you do this unaided?

Close the examples and attempt **Problems 25–28 in 25 minutes**. This is an editorial rehearsal, not an official exam limit. Score each out of 4: **1** for a justified method/convention, **2** for correct calculations or reasoning, **1** for a check or interpretation. An editorial target is **14/16 with no unresolved conceptual error**; it is not the course’s A cutoff. Diagnose mistakes with the review links, then retry a fresh variant.

- Can you compute means, sample variances, standard deviations and paired covariances?
- Can you distinguish a principal direction from its observation scores?
- Can you center, project, reconstruct and restore the original units?
- Can you reconcile eigenvalues, retained variance and reconstruction error?
- Can you explain why scaling, outliers or low-variance signal may change the answer?

```{include} practice.md
:start-after: <!-- mixed:start -->
:end-before: <!-- mixed:end -->
```

(w6-source-notes)=
## Source notes

The chapter develops all **39 pages** of Erisa Terolli’s `WK6_PCA.pdf`, including graphic-only sequences and applications. `Week 6 Slides - PCA (1).pdf` is byte-for-byte identical; both originals are preserved. The full student table, source eigenvectors, variance quiz and statistics example are reproduced. The displayed student scores use exact loadings before rounding; the source’s truncated decimals are not a new dataset.

Seven reproducible original diagrams translate the image-dimensionality, pizza/gym, projection, student, variance-budget, preprocessing and failure-case pictures. Toy scatter coordinates are explicitly identified rather than passed off as the source’s unprovided raw data. The two empirical genetics/eigenface images are extracted unchanged from the supplied PDF, with their source credits and explanatory text. Decorative Freepik shop images and the opening portrait are replaced by original mathematical diagrams; all their teaching content is retained.

The source uses sample variance/covariance with m−1 but a reconstruction objective averaged by m. Both conventions are preserved and reconciled. Standard deviation, normalized correlation interpretation, the centered-SVD bridge, explicit reconstruction, zero-variance/tied cases, fitted-preprocessing cautions, additional numerical applications and fresh assessment are teaching extensions. Uncorrelated scores are not asserted to be statistically independent.

The source reference list includes Stanford CS168 lectures 7–8, a PCA video, Turk and Pentland (1991), Novembre et al. (2008), Huang et al. (2007), and Deisenroth, Faisal and Ong’s *Mathematics for Machine Learning* (2020). The bibliography and exact source-page mapping are recorded in the repository’s authoring audit. No unprovided research datasets or empirical replication are claimed.

Week 6 now provides the previously missing destinations for the midterm topic list’s mean, variance, standard deviation, covariance and PCA, alongside the earlier SVD chapter. Full practice-exam mapping and cumulative mock preparation remain separate work. Use {ref}`the TL;DR <w6-cheatsheet>` to rehearse the computation chain.
