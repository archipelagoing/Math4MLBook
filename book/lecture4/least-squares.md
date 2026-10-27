(w4-least-squares)=
# Subspaces and least squares

<div class="chapter-kicker">Lecture 4 · Page 2 of 4 · Finding the closest possible record</div>

A line uses one direction. A subspace uses several. The same rule still works: **the error must be perpendicular to every allowed direction**. This gives the normal equations and the lecture’s best-fitting line.

<nav class="lecture-path" aria-label="Lecture 4 learning path">
<a href="index.html"><span class="path-number">01</span><span>Orthogonality & projections</span></a>
<a href="least-squares.html" aria-current="page"><span class="path-number">02</span><span>Subspaces & least squares</span></a>
<a href="orthonormal.html"><span class="path-number">03</span><span>Orthonormal bases & Gram–Schmidt</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Follow the lecture**

- {ref}`F · Projection onto a subspace <w4-subspace>`
- {ref}`G · When is the Gram matrix invertible? <w4-invertibility>`
- {ref}`H · Least-squares line fitting <w4-least-squares-fit>`
::::

(w4-subspace)=
## F · Projection onto a subspace

::::{div} section-intro

**Learning goal:** Derive the normal equations and distinguish coefficients from a projected output.

<span class="source-label">Lecture PDF pages 12–13</span>
::::

Collect spanning directions into the columns of $A\in\mathbb R^{m\times n}$. Every allowed output is $A\mathbf x$. Asking the residual to be perpendicular to every column gives one equation per column.

```{figure} ../figures/lecture4/subspace-projection.svg
:alt: A shaded schematic plane is the column space of A. The projected vector p lies in that plane; the residual from p to b is perpendicular to every spanning column, so A transpose times the residual is zero.

The subspace-projection picture from PDF pages 12–13, redrawn with the fitted vector and residual labeled. The shaded plane represents the allowed outputs; the condition is perpendicularity to the whole subspace.
```

:::{admonition} Result · Normal equations and projection
:class: key-result

Set $\mathbf p=A\widehat{\mathbf x}$ and $\mathbf e=\mathbf b-A\widehat{\mathbf x}$. Then

$$A^T\mathbf e=0\quad\Longleftrightarrow\quad
\boxed{A^TA\widehat{\mathbf x}=A^T\mathbf b}.$$

These are the **normal equations**, an $n$-equation system in $n$ coefficient unknowns.
If the columns of $A$ are linearly independent,

$$\widehat{\mathbf x}=(A^TA)^{-1}A^T\mathbf b,\qquad
\mathbf p=A(A^TA)^{-1}A^T\mathbf b,\qquad
\boxed{P=A(A^TA)^{-1}A^T}.$$

The coefficient vector has $n$ entries; the fitted output and residual have $m$ entries; $P$ is $m\times m$. Solve the normal equations by elimination rather than computing an inverse just to fit one vector.
:::

:::{admonition} Why perpendicular means closest
:class: proof

For any other $\mathbf q\in C(A)$,
$\mathbf b-\mathbf q=\mathbf e+(\mathbf p-\mathbf q)$.
Here $\mathbf e\perp C(A)$, so Pythagoras gives

$$\|\mathbf b-\mathbf q\|^2=\|\mathbf e\|^2+\|\mathbf p-\mathbf q\|^2\geq\|\mathbf e\|^2.$$

Equality requires $\mathbf q=\mathbf p$. Thus the closest **output** is unique.
Also $P^T=P$, since $A^TA$ and its inverse are symmetric; and
$P^2=A(A^TA)^{-1}(A^TA)(A^TA)^{-1}A^T=P$.
The complementary projector $I-P$ produces the residual in $N(A^T)$.
:::

:::::{admonition} Worked example 4.6 · Derive the two-view averaging rule
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Form the small system</span>

For the calibrated front/side views, the input $(X,Y,Z)^T$ produces the record $(X,Y,Y,Z)^T$:

$$H=\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix},\qquad \mathbf b=(2,2,4,4)^T.$$

The two measurements of the same $Y$ coordinate disagree. Taking column dot products gives

$$H^TH=\begin{bmatrix}1&0&0\\0&2&0\\0&0&1\end{bmatrix},\qquad H^T\mathbf b=\begin{bmatrix}2\\6\\4\end{bmatrix}.$$

The middle entry is $2+4$, because both readings measure $Y$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve and reconstruct</span>

$\widehat X=2$, $2\widehat Y=6$, $\widehat Z=4$, hence $\widehat{\mathbf x}=(2,3,4)^T$ and $H\widehat{\mathbf x}=(2,3,3,4)^T$.
The residual $(0,-1,1,0)^T$ has $H^T\mathbf e=0$ and squared length $2$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Read the measurement-space projector</span>

$$P_H=H(H^TH)^{-1}H^T=
\begin{bmatrix}1&0&0&0\\0&1/2&1/2&0\\0&1/2&1/2&0\\0&0&0&1\end{bmatrix}.$$

It replaces both middle readings by their mean. Check $P_H\mathbf b=(2,3,3,4)^T$, $P_H^T=P_H$, and $P_H^2=P_H$.
::::

::::{div} key-answer

$P_H$ acts on **four-entry records**. It differs from the three-dimensional front-view projector $O^TO$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Why check $A^T\mathbf e=0$ rather than just $\mathbf p^T\mathbf e=0$?
:::

:::{dropdown} Check your reasoning

The first checks perpendicularity to every column, hence the whole subspace. Being perpendicular to a single fitted vector is generally insufficient.
:::

::::{div} section-recap

**Takeaway:** Find a vector in the column space whose leftover error lies in the left null space. Practice: Problems 9–10.
::::

(w4-invertibility)=
## G · When is the Gram matrix invertible?

::::{div} section-intro

**Learning goal:** Check the hypothesis before using the inverse formula.

<span class="source-label">Lecture PDF pages 14</span>
::::

:::{admonition} Theorem · Independence is exactly the condition
:class: definition

The **Gram matrix** $G=A^TA$ is invertible if and only if $A$ has linearly independent columns. It is always symmetric, but symmetry alone does not guarantee invertibility.
:::

:::{admonition} Proof · A zero squared length forces a zero vector
:class: proof

Suppose $A^TA\mathbf x=0$. Multiplying on the left by $\mathbf x^T$ gives

$$0=\mathbf x^TA^TA\mathbf x=(A\mathbf x)^T(A\mathbf x)=\|A\mathbf x\|^2.$$

Thus $A\mathbf x=0$. If the columns are independent, $\mathbf x=0$, so the square matrix $A^TA$ has trivial null space and is invertible.
Conversely, if $A\mathbf x=0$ for some nonzero $\mathbf x$, then $A^TA\mathbf x=0$ too, so $A^TA$ is singular. In fact $N(A^TA)=N(A)$.
:::

:::::{admonition} Worked example 4.7 · Dependent columns do not destroy the closest output
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Expose the singular Gram matrix</span>

Let $A=\begin{bmatrix}1&2\\0&0\end{bmatrix}$ and $\mathbf b=(3,4)^T$.
Then $A^TA=\begin{bmatrix}1&2\\2&4\end{bmatrix}$ has determinant zero. The inverse formula is unavailable.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve the normal equations anyway</span>

$A^T\mathbf b=(3,6)^T$, so both normal equations reduce to $x_1+2x_2=3$. Thus
$\widehat{\mathbf x}=(3-2t,t)^T$ for every real $t$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check what is unique</span>

Every such vector gives $\mathbf p=A\widehat{\mathbf x}=(3,0)^T$ and $\mathbf e=(0,4)^T$, with $A^T\mathbf e=0$.
Alternatively, use just the independent first column: projection onto the x-axis has matrix $\operatorname{diag}(1,0)$.
::::

::::{div} key-answer

The closest output is unique; its coefficients need not be. Remove redundant spanning columns before using an inverse.
::::
:::::

:::{admonition} Pitfall · More equations does not guarantee independent columns
:class: pitfall

Even a tall matrix can repeat a column. Check rank or the column relations. Normal equations still characterize least-squares fits when columns are dependent, but $(A^TA)^{-1}$ does not exist.
:::

:::{admonition} Check your understanding
:class: checkpoint

Can $A^TA$ be invertible when $A$ is a $2\times3$ matrix?
:::

:::{dropdown} Check your reasoning

No. At most two columns in $\mathbb R^2$ can be independent. Here $N(A)$ is nontrivial, so $N(A^TA)$ is nontrivial.
:::

::::{div} section-recap

**Takeaway:** An inverse needs full **column** rank. Practice: Problems 11–12.
::::

(w4-least-squares-fit)=
## H · Least-squares line fitting

::::{div} section-intro

**Learning goal:** Translate data into a matrix, fit the model, and verify the residual.

<span class="source-label">Lecture PDF pages 15–21</span>
::::

The lecture asks for the closest line to $(1,1)$, $(2,2)$ and $(3,2)$. To make “closest” precise, fit $y=c+mt$ by minimizing the **sum of squared vertical errors**. We use $t$ for the horizontal coordinate so it cannot be confused with the coefficient vector.

:::{admonition} Definition · Least squares
:class: definition

A least-squares solution minimizes

$$E(\mathbf x)=\|A\mathbf x-\mathbf b\|^2=\sum_{i=1}^m\big((A\mathbf x)_i-b_i\big)^2.$$

It satisfies $A^TA\widehat{\mathbf x}=A^T\mathbf b$. When columns are independent, it is unique. Squaring the norm does not change the minimizer.
:::

:::::{admonition} Worked example 4.8 · The lecture’s complete three-point fit
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Build one row per observation</span>

The equations would be $c+m=1$, $c+2m=2$, $c+3m=2$:

$$A=\begin{bmatrix}1&1\\1&2\\1&3\end{bmatrix},\quad
\mathbf x=\begin{bmatrix}c\\m\end{bmatrix},\quad\mathbf b=\begin{bmatrix}1\\2\\2\end{bmatrix}.$$

The first two equations give $c=0,m=1$, which fails the third ($3\ne2$). No exact line passes through all three points.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Form the normal equations with dot products</span>

$$A^TA=\begin{bmatrix}1+1+1&1+2+3\\1+2+3&1+4+9\end{bmatrix}
=\begin{bmatrix}3&6\\6&14\end{bmatrix},\quad
A^T\mathbf b=\begin{bmatrix}1+2+2\\1+4+6\end{bmatrix}=\begin{bmatrix}5\\11\end{bmatrix}.$$

Its determinant is $42-36=6\ne0$, so the fit has unique coefficients.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Eliminate to find the slope, then the intercept</span>

$$\left[\begin{array}{cc|c}3&6&5\\6&14&11\end{array}\right]
\xrightarrow{R_2\leftarrow R_2-2R_1}
\left[\begin{array}{cc|c}3&6&5\\0&2&1\end{array}\right].$$

Thus $2\widehat m=1$, so $\widehat m=1/2$. Then
$3\widehat c+6(1/2)=5$, so $\widehat c=2/3$.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Compute fitted values and signed residuals</span>

$$\mathbf p=A\widehat{\mathbf x}=\begin{bmatrix}7/6\\5/3\\13/6\end{bmatrix},\qquad
\mathbf e=\mathbf b-\mathbf p=\begin{bmatrix}-1/6\\1/3\\-1/6\end{bmatrix}.$$

The residual convention is observed minus fitted. Its squared length is
$E_{\min}=1/36+1/9+1/36=1/6$.
::::

::::{div} worked-step

<span class="step-label">Step 5 · Verify optimality in the original model</span>

$$A^T\mathbf e=\begin{bmatrix}-1/6+1/3-1/6\\-1/6+2/3-3/6\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}.$$

The residual is perpendicular to both the constant column and the $t$ column, proving this fit is optimal. Substituting the fitted coefficients gives the three values in $\mathbf p$, not the unattainable original $\mathbf b$.
::::

::::{div} key-answer

**Best-fitting line:** $\boxed{y=\frac23+\frac12t}$. **Minimum squared error:** $\boxed{1/6}$.
::::
:::::

```{figure} ../figures/lecture4/least-squares-line.svg
:alt: The data (1,1), (2,2), (3,2), the line y=2/3+t/2, and vertical observed-minus-fitted residuals minus 1/6, plus 1/3, minus 1/6.

The plotted gaps are vertical. The perpendicular projection happens in response space R³, where b=(1,2,2) and p=(7/6,5/3,13/6).
```

:::{admonition} Pitfall · Two geometries are in play
:class: pitfall

The fitted line is drawn in the $(t,y)$ plane, but $\mathbf b$ and $\mathbf p$ are **three-entry response vectors**. Ordinary least squares minimizes vertical gaps in the plot; it does not minimize the perpendicular distances of those plotted points to the line.
:::

:::{admonition} Check your understanding
:class: checkpoint

What changes in the design matrix if the model must pass through the origin?
:::

:::{dropdown} Check your reasoning

Use $y=mt$: drop the constant column, so $A=(1,2,3)^T$ and $\widehat m=(1+4+6)/(1+4+9)=11/14$. This is a different model and generally a different fitted line.
:::

::::{div} section-recap

**Takeaway:** Build rows from the chosen model; solve, reconstruct, and check columnwise residual orthogonality. Practice: Problems 13–16.
::::

(w4-practice-fitting)=
## Practice · Subspaces and least squares

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- fitting:start -->
:end-before: <!-- fitting:end -->
```

**Next:** {ref}`Page 3 · Orthonormal bases and Gram–Schmidt <w4-orthonormal>` makes the Gram matrix the identity.
