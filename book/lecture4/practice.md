<!-- projection:start -->

(w4-p01)=
### Problem 1 · Orthogonal is not unit

Test $\mathbf v=(2,1,-1)^T$ and $\mathbf w=(1,0,2)^T$ for orthogonality. Check Pythagoras and decide whether the pair is orthonormal.

:::{dropdown} Hint

Compute the dot product before the lengths.
:::

```{include} solutions.md
:start-after: <!-- answer-01:start -->
:end-before: <!-- answer-01:end -->
```

(w4-p02)=
### Problem 2 · Test the whole subspace

Are $V=\operatorname{span}\{(1,0,0)^T,(0,1,0)^T\}$ and $W=\operatorname{span}\{(1,0,1)^T\}$ orthogonal? Explain why one zero dot product is insufficient.

```{include} solutions.md
:start-after: <!-- answer-02:start -->
:end-before: <!-- answer-02:end -->
```

(w4-p03)=
### Problem 3 · Dimensions and complements

A $6\times4$ matrix has rank $3$. State the dimensions and ambient spaces of all four fundamental spaces, and pair the complements.

```{include} solutions.md
:start-after: <!-- answer-03:start -->
:end-before: <!-- answer-03:end -->
```

(w4-p04)=
### Problem 4 · Use rows as perpendicular tests

For $A=\begin{bmatrix}1&2&0\\0&0&1\end{bmatrix}$, find $N(A)$ and verify it is perpendicular to both rows.

```{include} solutions.md
:start-after: <!-- answer-04:start -->
:end-before: <!-- answer-04:end -->
```

(w4-p05)=
### Problem 5 · Coordinate split

Project $\mathbf b=(-2,5,4)^T$ onto the xy-plane and its perpendicular complement. Give both matrices and check the sum.

```{include} solutions.md
:start-after: <!-- answer-05:start -->
:end-before: <!-- answer-05:end -->
```

(w4-p06)=
### Problem 6 · Idempotence alone

Let $B=\begin{bmatrix}1&1\\0&0\end{bmatrix}$. Check $B^2=B$. Is $B$ the orthogonal projector onto the x-axis? Test $\mathbf b=(0,1)^T$.

```{include} solutions.md
:start-after: <!-- answer-06:start -->
:end-before: <!-- answer-06:end -->
```

(w4-p07)=
### Problem 7 · Fit a new repeated reading

For the chapter’s $H$, fit $\mathbf b=(1,3,7,-2)^T$ with equal squared-error weights. Give the point estimate, fitted record and residual.

```{include} solutions.md
:start-after: <!-- answer-07:start -->
:end-before: <!-- answer-07:end -->
```

(w4-p08)=
### Problem 8 · A fresh slanted line

Project $\mathbf b=(4,1)^T$ onto $\operatorname{span}\{(2,1)^T\}$. Give $P$, $\widehat x$, $\mathbf p$, and $\mathbf e$.

:::{dropdown} Hint

The denominator is the squared length of the direction.
:::

```{include} solutions.md
:start-after: <!-- answer-08:start -->
:end-before: <!-- answer-08:end -->
```

<!-- projection:end -->

<!-- fitting:start -->

(w4-p09)=
### Problem 9 · A plane with an easy Gram matrix

Let $A=\begin{bmatrix}1&0\\0&1\\1&0\end{bmatrix}$ and $\mathbf b=(1,2,5)^T$. Find a least-squares solution, its output, and its residual.

```{include} solutions.md
:start-after: <!-- answer-09:start -->
:end-before: <!-- answer-09:end -->
```

(w4-p10)=
### Problem 10 · Worksheet 8 · A nonorthogonal spanning pair

From **Linear Algebra Worksheet, Problem 8**: project $\mathbf b=(2,4,6)^T$ onto the span of $\mathbf a_1=(1,1,0)^T$, $\mathbf a_2=(1,1,1)^T$. Find the residual and check both dot products.

```{include} solutions.md
:start-after: <!-- answer-10:start -->
:end-before: <!-- answer-10:end -->
```

(w4-p11)=
### Problem 11 · Same fit, many coefficients

Let $A=\begin{bmatrix}1&3\\0&0\\1&3\end{bmatrix}$ and $\mathbf b=(2,4,0)^T$. Find all least-squares coefficients, the fitted output and the minimum squared error.

```{include} solutions.md
:start-after: <!-- answer-11:start -->
:end-before: <!-- answer-11:end -->
```

(w4-p12)=
### Problem 12 · Complementary projector

For an orthogonal projector $P$, prove $I-P$ is also an orthogonal projector. Identify its range. This is the skill in **Worksheet 10(c)**.

```{include} solutions.md
:start-after: <!-- answer-12:start -->
:end-before: <!-- answer-12:end -->
```

(w4-p13)=
### Problem 13 · Fit a fresh line

Fit $y=c+mt$ to $(0,1),(1,2),(2,2)$. Give the minimum squared error.

:::{dropdown} Hint

Use rows [1,t], not [t,1] unless you also reverse the coefficient order.
:::

```{include} solutions.md
:start-after: <!-- answer-13:start -->
:end-before: <!-- answer-13:end -->
```

(w4-p14)=
### Problem 14 · The constant-only model

Fit $y=c$ to responses $1,4,7,8$. Why is the fitted constant their mean?

```{include} solutions.md
:start-after: <!-- answer-14:start -->
:end-before: <!-- answer-14:end -->
```

(w4-p15)=
### Problem 15 · Why the fit is the closest

Suppose $\mathbf p\in C(A)$ and $A^T(\mathbf b-\mathbf p)=0$. Prove no other $\mathbf q\in C(A)$ can be closer, and state when equality occurs. This extends **Worksheet 10(a–b)**.

```{include} solutions.md
:start-after: <!-- answer-15:start -->
:end-before: <!-- answer-15:end -->
```

(w4-p16)=
### Problem 16 · Worksheet 9 · Four-point line fit

From **Linear Algebra Worksheet, Problem 9**: fit $y=C+Dt$ to $(0,1),(1,8),(2,8),(3,20)$. Show the normal equations and a residual check.

```{include} solutions.md
:start-after: <!-- answer-16:start -->
:end-before: <!-- answer-16:end -->
```

<!-- fitting:end -->

<!-- bases:start -->

(w4-p17)=
### Problem 17 · Normalize or merely orthogonal?

Let $M=\begin{bmatrix}1&1\\1&-1\\0&0\end{bmatrix}$. Compute $M^TM$ and build an orthonormal-column matrix for the same span.

```{include} solutions.md
:start-after: <!-- answer-17:start -->
:end-before: <!-- answer-17:end -->
```

(w4-p18)=
### Problem 18 · Products of orthogonal matrices

As in **Worksheet 12(a)**, show that the product of two same-size square orthogonal matrices $Q_1,Q_2$ is orthogonal. Identify its inverse.

```{include} solutions.md
:start-after: <!-- answer-18:start -->
:end-before: <!-- answer-18:end -->
```

(w4-p19)=
### Problem 19 · Projection from an orthonormal basis

Let $\mathbf q_1=(1,0,1)^T/\sqrt2$, $\mathbf q_2=(0,1,0)^T$. Project $\mathbf b=(4,-1,0)^T$ onto their span.

```{include} solutions.md
:start-after: <!-- answer-19:start -->
:end-before: <!-- answer-19:end -->
```

(w4-p20)=
### Problem 20 · Dot products are coordinates only for unit directions

Let $\mathbf u=(2,0)^T$, $\mathbf v=(0,3)^T$, $\mathbf b=(4,6)^T$. Recover the exact coefficients of b. Explain why $\mathbf u^T\mathbf b$ and $\mathbf v^T\mathbf b$ are not those coefficients.

```{include} solutions.md
:start-after: <!-- answer-20:start -->
:end-before: <!-- answer-20:end -->
```

(w4-p21)=
### Problem 21 · Gram–Schmidt with changed numbers

Construct an orthonormal basis from $\mathbf a_1=(1,0,1)^T$, $\mathbf a_2=(1,1,1)^T$.

:::{dropdown} Hint

Subtract the first component before normalizing the second direction.
:::

```{include} solutions.md
:start-after: <!-- answer-21:start -->
:end-before: <!-- answer-21:end -->
```

(w4-p22)=
### Problem 22 · A redundant third input

Apply Gram–Schmidt to $\mathbf a_1=(1,1,0)^T$, $\mathbf a_2=(1,0,0)^T$, $\mathbf a_3=(2,1,0)^T$. How many basis vectors remain?

```{include} solutions.md
:start-after: <!-- answer-22:start -->
:end-before: <!-- answer-22:end -->
```

(w4-p23)=
### Problem 23 · Worksheet 11/15 · Orthogonalize in four dimensions

From **Linear Algebra Worksheet, Problems 11 and 15** (the same data): find an orthogonal basis from $\mathbf a=(1,2,0,1)^T$, $\mathbf b=(1,0,0,1)^T$, $\mathbf c=(0,1,0,1)^T$. Then state how to normalize it.

```{include} solutions.md
:start-after: <!-- answer-23:start -->
:end-before: <!-- answer-23:end -->
```

(w4-p24)=
### Problem 24 · Worksheet 12(b–c) · Coefficients in a unit basis

Using the three unit vectors from worked example 4.12, solve $x_1\mathbf q_1+x_2\mathbf q_2+x_3\mathbf q_3=(1,2,1)^T$. Explain the dot-product rule. This is **Worksheet 12(b–c)**.

```{include} solutions.md
:start-after: <!-- answer-24:start -->
:end-before: <!-- answer-24:end -->
```

<!-- bases:end -->

<!-- mixed:start -->

(w4-p25)=
### Problem 25 · Mixed 1

Find the point on $\operatorname{span}\{(1,-1,1)^T\}$ closest to $\mathbf b=(2,1,0)^T$. Give a check that proves your answer.

```{include} solutions.md
:start-after: <!-- answer-25:start -->
:end-before: <!-- answer-25:end -->
```

(w4-p26)=
### Problem 26 · Mixed 2

For $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$ and $\mathbf b=(3,1)^T$, find all coefficients giving the closest output. Is $(A^TA)^{-1}$ available?

```{include} solutions.md
:start-after: <!-- answer-26:start -->
:end-before: <!-- answer-26:end -->
```

(w4-p27)=
### Problem 27 · Mixed 3

Find the best-fitting line $y=c+mt$ for $(-1,2),(0,0),(1,1)$ and verify the fit.

```{include} solutions.md
:start-after: <!-- answer-27:start -->
:end-before: <!-- answer-27:end -->
```

(w4-p28)=
### Problem 28 · Mixed 4

Find an orthonormal basis for the span of $\mathbf a_1=(0,1,1)^T$, $\mathbf a_2=(1,1,1)^T$. Use it to find the closest vector to $\mathbf b=(2,3,1)^T$.

```{include} solutions.md
:start-after: <!-- answer-28:start -->
:end-before: <!-- answer-28:end -->
```

<!-- mixed:end -->

