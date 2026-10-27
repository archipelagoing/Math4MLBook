<!-- eigen:start -->

(w5-p01)=
### Problem 1 · Test a proposed eigenpair

For $A=\begin{bmatrix}2&1\\0&3\end{bmatrix}$, test $\mathbf v=(1,1)^T$ and $\mathbf w=(1,0)^T$ as eigenvectors.

:::{dropdown} Hint

Multiply before trying to solve a characteristic polynomial.
:::

```{include} solutions.md
:start-after: <!-- answer-01:start -->
:end-before: <!-- answer-01:end -->
```

(w5-p02)=
### Problem 2 · A vector that changes direction

For $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, is $(1,1)^T$ an eigenvector? What happens to $(1,0)^T$?

```{include} solutions.md
:start-after: <!-- answer-02:start -->
:end-before: <!-- answer-02:end -->
```

(w5-p03)=
### Problem 3 · Reversal and collapse

Find the eigenvalues and eigenspaces of $\operatorname{diag}(-2,0)$. Explain why eigenvalue zero is allowed.

```{include} solutions.md
:start-after: <!-- answer-03:start -->
:end-before: <!-- answer-03:end -->
```

(w5-p04)=
### Problem 4 · A quarter-turn

For $R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$, find the characteristic polynomial and decide whether there are real eigenvectors.

```{include} solutions.md
:start-after: <!-- answer-04:start -->
:end-before: <!-- answer-04:end -->
```

(w5-p05)=
### Problem 5 · Worksheet 13 · Shift by the identity

From **Linear Algebra Worksheet, Problem 13**, find eigenvalues/eigenspaces of $A=\begin{bmatrix}1&4\\2&3\end{bmatrix}$ and $A+I$. What is the general relationship?

:::{dropdown} Hint

Use det(A−λI), then apply the identity shift to a verified eigenpair.
:::

```{include} solutions.md
:start-after: <!-- answer-05:start -->
:end-before: <!-- answer-05:end -->
```

(w5-p06)=
### Problem 6 · A nontrivial eigenspace

Find all eigenvectors of $A=\begin{bmatrix}4&2\\0&1\end{bmatrix}$. Check the trace and determinant.

```{include} solutions.md
:start-after: <!-- answer-06:start -->
:end-before: <!-- answer-06:end -->
```

(w5-p07)=
### Problem 7 · Diagonalization in a nonorthogonal basis

Diagonalize $A=\begin{bmatrix}5&2\\0&1\end{bmatrix}$. May you use $V^T$ as its inverse?

```{include} solutions.md
:start-after: <!-- answer-07:start -->
:end-before: <!-- answer-07:end -->
```

(w5-p08)=
### Problem 8 · Repeated roots: decide rather than guess

Compare $J=\begin{bmatrix}3&1\\0&3\end{bmatrix}$ and $3I_2$. Both have characteristic polynomial $(3-\lambda)^2$. Which diagonalizes?

```{include} solutions.md
:start-after: <!-- answer-08:start -->
:end-before: <!-- answer-08:end -->
```

(w5-p09)=
### Problem 9 · A symmetric positive-definite example

Find an orthonormal eigenbasis for $S=\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$ and decide whether S is positive definite.

```{include} solutions.md
:start-after: <!-- answer-09:start -->
:end-before: <!-- answer-09:end -->
```

(w5-p10)=
### Problem 10 · A false blanket claim

“Every pair of eigenvectors of a symmetric matrix is perpendicular.” Give a counterexample, and state the correct theorem.

```{include} solutions.md
:start-after: <!-- answer-10:start -->
:end-before: <!-- answer-10:end -->
```

<!-- eigen:end -->

<!-- svd:start -->

(w5-p11)=
### Problem 11 · Full versus compact shapes

A real $3\times5$ matrix has rank $2$. Give full and compact factor sizes and all four fundamental-space dimensions.

```{include} solutions.md
:start-after: <!-- answer-11:start -->
:end-before: <!-- answer-11:end -->
```

(w5-p12)=
### Problem 12 · An off-diagonal rank-one map

Find a full SVD of $A=\begin{bmatrix}0&2\\0&0\end{bmatrix}$.

```{include} solutions.md
:start-after: <!-- answer-12:start -->
:end-before: <!-- answer-12:end -->
```

(w5-p13)=
### Problem 13 · Negative eigenvalues, positive stretches

Give eigenvalues and an SVD of $A=\operatorname{diag}(-3,1)$.

```{include} solutions.md
:start-after: <!-- answer-13:start -->
:end-before: <!-- answer-13:end -->
```

(w5-p14)=
### Problem 14 · A fresh complete SVD

Compute an SVD of $A=\begin{bmatrix}2&2\\1&-1\end{bmatrix}$. Show the Gram matrix, paired directions and product.

:::{dropdown} Hint

The Gram matrix has equal diagonal entries, so sum/difference directions simplify it.
:::

```{include} solutions.md
:start-after: <!-- answer-14:start -->
:end-before: <!-- answer-14:end -->
```

(w5-p15)=
### Problem 15 · Complete the rectangular bases

Give full factors for $A=\begin{bmatrix}0&0\\0&2\\0&0\end{bmatrix}$, identifying both null spaces.

```{include} solutions.md
:start-after: <!-- answer-15:start -->
:end-before: <!-- answer-15:end -->
```

(w5-p16)=
### Problem 16 · What the Gram matrix does not determine

If $A^TA=\operatorname{diag}(9,9,0)$ for a $2\times3$ matrix, what singular values and right subspaces are known? Can you recover the left vectors without A?

```{include} solutions.md
:start-after: <!-- answer-16:start -->
:end-before: <!-- answer-16:end -->
```

(w5-p17)=
### Problem 17 · Repair an unpaired sign

For $A=\operatorname{diag}(2,1)$, someone proposes $U=I$, $\Sigma=\operatorname{diag}(2,1)$, $V=\operatorname{diag}(-1,1)$. Explain the error and fix it.

```{include} solutions.md
:start-after: <!-- answer-17:start -->
:end-before: <!-- answer-17:end -->
```

(w5-p18)=
### Problem 18 · The zero matrix

Give a full SVD and the four-space dimensions for the zero $2\times3$ matrix.

```{include} solutions.md
:start-after: <!-- answer-18:start -->
:end-before: <!-- answer-18:end -->
```

<!-- svd:end -->

<!-- applications:start -->

(w5-p19)=
### Problem 19 · Read the truncation error

Find the best rank-at-most-two Frobenius approximation to $R=\operatorname{diag}(6,3,2)$. Give squared error, error, and retained energy fraction.

```{include} solutions.md
:start-after: <!-- answer-19:start -->
:end-before: <!-- answer-19:end -->
```

(w5-p20)=
### Problem 20 · Smaller coordinates, same reconstruction

For an $80\times40$ matrix, give the k=4 factor shapes, row-coordinate shape, reconstruction shape and factor storage count.

```{include} solutions.md
:start-after: <!-- answer-20:start -->
:end-before: <!-- answer-20:end -->
```

(w5-p21)=
### Problem 21 · Ties at the boundary

Give two equally good rank-two approximations of $\operatorname{diag}(4,2,2)$ and their Frobenius errors.

```{include} solutions.md
:start-after: <!-- answer-21:start -->
:end-before: <!-- answer-21:end -->
```

(w5-p22)=
### Problem 22 · A fresh weighted feature score

For user row $(0.2,0.8)$, weights $(3,1)$ and item row $(0.5,0.25)$, compute the score. Can it be called a calibrated rating?

```{include} solutions.md
:start-after: <!-- answer-22:start -->
:end-before: <!-- answer-22:end -->
```

(w5-p23)=
### Problem 23 · Observed entries versus zero filling

For $R=\begin{bmatrix}5&?\\?&2\end{bmatrix}$, write the unregularized squared-error objective over observed entries for a candidate matrix B. What extra terms does zero filling introduce?

```{include} solutions.md
:start-after: <!-- answer-23:start -->
:end-before: <!-- answer-23:end -->
```

(w5-p24)=
### Problem 24 · Named features do not establish an SVD

Can $L=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ serve as the orthogonal U of a full SVD? Can it still appear in a general feature model?

```{include} solutions.md
:start-after: <!-- answer-24:start -->
:end-before: <!-- answer-24:end -->
```

<!-- applications:end -->

<!-- mixed:start -->

(w5-p25)=
### Problem 25 · Mixed 1

For $A=\begin{bmatrix}4&2\\1&3\end{bmatrix}$, find all eigenspaces and determine whether A diagonalizes. Supply a verification.

```{include} solutions.md
:start-after: <!-- answer-25:start -->
:end-before: <!-- answer-25:end -->
```

(w5-p26)=
### Problem 26 · Mixed 2

Find a full SVD of $A=\begin{bmatrix}1&1\\1&-1\\0&0\end{bmatrix}$ and identify its left null space.

```{include} solutions.md
:start-after: <!-- answer-26:start -->
:end-before: <!-- answer-26:end -->
```

(w5-p27)=
### Problem 27 · Mixed 3

For $A=\operatorname{diag}(3,-1)$, give eigenvalues, singular values, a best rank-one Frobenius approximation, and both forms of its error.

```{include} solutions.md
:start-after: <!-- answer-27:start -->
:end-before: <!-- answer-27:end -->
```

(w5-p28)=
### Problem 28 · Mixed 4

A ratings table $R=\begin{bmatrix}5&?\\?&1\end{bmatrix}$ is assumed to have exact rank one. Does that determine both missing ratings uniquely? Give two completions and explain the implication for an SVD recommendation claim.

```{include} solutions.md
:start-after: <!-- answer-28:start -->
:end-before: <!-- answer-28:end -->
```

<!-- mixed:end -->

