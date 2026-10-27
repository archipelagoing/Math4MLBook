<!-- statistics:start -->

(w6-p01)=
### Problem 1 · Count dimensions

Flatten a 20×30 RGB image into one observation. What is its ambient dimension? What is the data-matrix shape for 50 such images?

```{include} solutions.md
:start-after: <!-- answer-01:start -->
:end-before: <!-- answer-01:end -->
```

(w6-p02)=
### Problem 2 · Mean and translation

Find the mean and centered values of 2,4,9. What changes if you add 10 to each value?

```{include} solutions.md
:start-after: <!-- answer-02:start -->
:end-before: <!-- answer-02:end -->
```

(w6-p03)=
### Problem 3 · Center each feature

Center the rows $(1,10),(3,14),(5,12)$. State the mean vector and check both centered columns.

```{include} solutions.md
:start-after: <!-- answer-03:start -->
:end-before: <!-- answer-03:end -->
```

(w6-p04)=
### Problem 4 · Variance and standard deviation

For values 1,2,6, calculate the sample variance and sample standard deviation.

:::{dropdown} Hint

Compute deviations before squaring.
:::

```{include} solutions.md
:start-after: <!-- answer-04:start -->
:end-before: <!-- answer-04:end -->
```

(w6-p05)=
### Problem 5 · How units affect spread

A feature has sample variance 9. Transform it by y=2x+100. Find the new sample variance and standard deviation.

```{include} solutions.md
:start-after: <!-- answer-05:start -->
:end-before: <!-- answer-05:end -->
```

(w6-p06)=
### Problem 6 · A fresh paired covariance matrix

For rows $(1,6),(3,2),(5,4)$, calculate the sample covariance matrix.

```{include} solutions.md
:start-after: <!-- answer-06:start -->
:end-before: <!-- answer-06:end -->
```

(w6-p07)=
### Problem 7 · Zero covariance is not independence

Use equally weighted outcomes x=−1,0,1 with y=x². Calculate their sample covariance and explain why independence does not follow.

```{include} solutions.md
:start-after: <!-- answer-07:start -->
:end-before: <!-- answer-07:end -->
```

(w6-p08)=
### Problem 8 · One direction, one coordinate

For a centered point $(3,-3)^T$, compute coordinates along $\mathbf q_1=(1,-1)^T/\sqrt2$ and $\mathbf q_2=(1,1)^T/\sqrt2$. Reconstruct using the first only.

```{include} solutions.md
:start-after: <!-- answer-08:start -->
:end-before: <!-- answer-08:end -->
```

<!-- statistics:end -->

<!-- compute:start -->

(w6-p09)=
### Problem 9 · Pythagoras for projection

Project $\mathbf x=(1,3)^T$ onto unit direction $\mathbf q=(1,1)^T/\sqrt2$. Find the score, projection, residual and squared error.

```{include} solutions.md
:start-after: <!-- answer-09:start -->
:end-before: <!-- answer-09:end -->
```

(w6-p10)=
### Problem 10 · Why orthonormality is a constraint

For centered observations $(1,0)^T$ and $(−1,0)^T$, someone keeps the same unit direction e₁ twice and claims retained squared score total 4. Explain the mistake.

```{include} solutions.md
:start-after: <!-- answer-10:start -->
:end-before: <!-- answer-10:end -->
```

(w6-p11)=
### Problem 11 · Find a maximum without guessing

For $C=\operatorname{diag}(9,1)$, maximize $\mathbf v^TC\mathbf v$ over unit real v. State the maximum and all maximizing unit directions.

```{include} solutions.md
:start-after: <!-- answer-11:start -->
:end-before: <!-- answer-11:end -->
```

(w6-p12)=
### Problem 12 · Singular values versus variances

A centered matrix with m=5 has positive singular values 6 and 2. Find covariance eigenvalues, rank-one retained fraction, SSE and mean squared reconstruction error.

```{include} solutions.md
:start-after: <!-- answer-12:start -->
:end-before: <!-- answer-12:end -->
```

(w6-p13)=
### Problem 13 · A complete rank-one dataset

Find the mean, covariance, leading component, scores and reconstructions for rows $(1,0),(3,0),(5,0)$.

```{include} solutions.md
:start-after: <!-- answer-13:start -->
:end-before: <!-- answer-13:end -->
```

(w6-p14)=
### Problem 14 · Apply an already fitted model

A fitted model has mean $(10,20)^T$ and loading $(3,4)^T/5$. Encode and reconstruct a new point $(14,23)^T$, then check its residual.

```{include} solutions.md
:start-after: <!-- answer-14:start -->
:end-before: <!-- answer-14:end -->
```

(w6-p15)=
### Problem 15 · Choose a retention dimension

Covariance eigenvalues are 7,2,1. What is the smallest k retaining at least 85%? If m=6, give the corresponding SSE and average squared error.

```{include} solutions.md
:start-after: <!-- answer-15:start -->
:end-before: <!-- answer-15:end -->
```

(w6-p16)=
### Problem 16 · No variation and tied variation

Contrast a dataset with all rows identical and a dataset with C=2I₂. Is the first component unique, and is the variance fraction defined?

```{include} solutions.md
:start-after: <!-- answer-16:start -->
:end-before: <!-- answer-16:end -->
```

<!-- compute:end -->

<!-- applications:start -->

(w6-p17)=
### Problem 17 · Standardize and undo it

For rows $(2,20),(4,40),(6,60)$, compute feature means and sample standard deviations, standardize, and give the inverse formula.

```{include} solutions.md
:start-after: <!-- answer-17:start -->
:end-before: <!-- answer-17:end -->
```

(w6-p18)=
### Problem 18 · Changing units can change raw PCA

A centered dataset has C=diag(4,1). If feature 2 is multiplied by 10, what is the new covariance and leading raw direction? What is the standardized covariance?

```{include} solutions.md
:start-after: <!-- answer-18:start -->
:end-before: <!-- answer-18:end -->
```

(w6-p19)=
### Problem 19 · Read a two-PC application plot

A genetics score plot uses PC1 and PC2. Are these longitude/latitude? Can two nearby plotted observations still differ in omitted features?

```{include} solutions.md
:start-after: <!-- answer-19:start -->
:end-before: <!-- answer-19:end -->
```

(w6-p20)=
### Problem 20 · Pixel features versus observation features

An image dataset has 100 grayscale faces, each 20×30 pixels, stored as rows. Give X, covariance, Qₖ and score shapes for k=5. Count per-face scores and shared mean/loading entries.

```{include} solutions.md
:start-after: <!-- answer-20:start -->
:end-before: <!-- answer-20:end -->
```

(w6-p21)=
### Problem 21 · Outlier effect

A feature covariance is diag(3,1) before a refit and diag(3,20) after an extreme point is added. What happens to the first PC, and why does that not contradict the PCA objective?

```{include} solutions.md
:start-after: <!-- answer-21:start -->
:end-before: <!-- answer-21:end -->
```

(w6-p22)=
### Problem 22 · A one-dimensional curve

If points lie exactly on a curved arc in a plane, must one-component linear PCA reconstruct all of them exactly?

```{include} solutions.md
:start-after: <!-- answer-22:start -->
:end-before: <!-- answer-22:end -->
```

(w6-p23)=
### Problem 23 · High retained variance, lost label signal

A covariance is diag(100,0.1), and class labels differ only in the second coordinate. What variance fraction does PC1 retain, and why might one component be poor for classification?

```{include} solutions.md
:start-after: <!-- answer-23:start -->
:end-before: <!-- answer-23:end -->
```

(w6-p24)=
### Problem 24 · Decide what to scale

One feature is measured in meters and another in millimeters. Should PCA always divide by standard deviation? State the decision and the zero-variance exception.

```{include} solutions.md
:start-after: <!-- answer-24:start -->
:end-before: <!-- answer-24:end -->
```

<!-- applications:end -->

<!-- mixed:start -->

(w6-p25)=
### Problem 25 · Mixed 1

For paired rows $(1,4),(3,0),(8,2)$, find means, sample standard deviations and covariance matrix, and interpret the cross term.

```{include} solutions.md
:start-after: <!-- answer-25:start -->
:end-before: <!-- answer-25:end -->
```

(w6-p26)=
### Problem 26 · Mixed 2

Reduce rows $(5,5),(4,6),(1,3),(2,2)$ to one variance-maximizing coordinate. Give the mean, covariance, loading, scores, retained fraction, reconstructed rows and total squared error.

```{include} solutions.md
:start-after: <!-- answer-26:start -->
:end-before: <!-- answer-26:end -->
```

(w6-p27)=
### Problem 27 · Mixed 3

A centered 6×4 matrix has singular values 10,5,0,0. Find sample covariance eigenvalues and choose the smallest dimension retaining at least 85%. Give the discarded SSE.

```{include} solutions.md
:start-after: <!-- answer-27:start -->
:end-before: <!-- answer-27:end -->
```

(w6-p28)=
### Problem 28 · Mixed 4

A fitted standardized model has means $(10,100)$, scales $(2,10)$ and loading $(1,1)^T/\sqrt2$. Encode and reconstruct $(14,110)^T$. State the metric in which its residual is perpendicular.

```{include} solutions.md
:start-after: <!-- answer-28:start -->
:end-before: <!-- answer-28:end -->
```

<!-- mixed:end -->

