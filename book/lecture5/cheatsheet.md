(w5-cheatsheet)=
# TL;DR · Eigenvalues, SVD, and reduction

<div class="chapter-kicker">Lecture 5 · Page 4 of 4 · Find directions, separate strengths, keep what matters</div>

**Choose the question first:** preserved directions, a basis that diagonalizes, singular stretch directions, a low-rank approximation, or an unknown-rating model. Then use the matching recipe and verify the original matrix.

<nav class="lecture-path" aria-label="Lecture 5 learning path">
<a href="index.html"><span class="path-number">01</span><span>Eigenvalues & diagonalization</span></a>
<a href="svd.html"><span class="path-number">02</span><span>Singular value decomposition</span></a>
<a href="applications.html"><span class="path-number">03</span><span>Reduction & recommendations</span></a>
<a href="cheatsheet.html" aria-current="page"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Select the method

| Asked for | Start with | Essential condition |
| --- | --- | --- |
| Eigenvalues/eigenvectors | det(A−λI)=0, then null spaces | A square; eigenvectors nonzero |
| Diagonalization | Independent eigenvectors as columns | A full basis exists over the chosen field |
| Symmetric spectral factorization | Normalize an eigenbasis | A real symmetric |
| SVD | Eigenvectors of AᵀA | Any real m×n matrix |
| Best rank-at-most-k approximation | Leading k singular terms | A complete numerical matrix and stated norm |
| Missing ratings | A model fitted to observed entries | Missing values are not numerical zeros |

:::{admonition} Essential formulas and conditions
:class: key-result

**Eigenpairs:** $A\mathbf v=\lambda\mathbf v$, $\mathbf v\ne0$;
$E_\lambda=N(A-\lambda I)$.
For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$,

$$\det(A-\lambda I)=\lambda^2-(a+d)\lambda+ad-bc.$$

**Diagonalization:** $A=V\Lambda V^{-1}$ with independent eigenvectors in $V$ and matched eigenvalues in $\Lambda$. Repeated roots require enough eigenspace directions. For real symmetric $A$, choose $Q^TQ=I$ and use $A=Q\Lambda Q^T$. Symmetric positive definite means every eigenvalue is positive.

**SVD:** $A=U\Sigma V^T$, with $\sigma_i\ge0$ in decreasing order;
$A^TA\mathbf v_i=\sigma_i^2\mathbf v_i$ and $\mathbf u_i=A\mathbf v_i/\sigma_i$ when $\sigma_i>0$.

| Form for m×n rank r matrix | U | Σ | Vᵀ |
| --- | --- | --- | --- |
| Full | m×m | m×n | n×n |
| Compact, exact | m×r | r×r | r×n |
| Truncated, k≤r | m×k | k×k | k×n |

**Truncation:**

$$A_k=\sum_{i=1}^k\sigma_i\mathbf u_i\mathbf v_i^T,\qquad
\|A-A_k\|_F^2=\sum_{i>k}\sigma_i^2.$$

For $k<r$, $\|A-A_k\|_2=\sigma_{k+1}$. Row coordinates $Z=AV_k=U_k\Sigma_k$ have size $m\times k$; reconstruction $ZV_k^T$ has size $m\times n$.

**Weighted feature score:** $\widehat R_{ij}=\sum_\ell L_{i\ell}w_\ell M_{j\ell}$. Named features need not be SVD coordinates or produce calibrated ratings.
:::

## Eigenvalue / diagonalization recipe

1. Subtract λ from the diagonal and solve the characteristic equation. Keep repeated roots and note whether real roots exist.
2. For each root, solve the homogeneous system and state an eigenspace basis. Exclude zero from the eigenvector answer.
3. Check Av=λv in the original matrix. For 2×2, also check the trace sum and determinant product.
4. If diagonalization is requested, count independent directions. Assemble V and Λ in matching order and verify AV=VΛ. Use transpose as inverse only for an orthonormal basis.

## SVD / reduction recipe

1. Form AᵀA, find its eigenvalues, and choose an orthonormal eigenbasis. Order the eigenvalues from largest down.
2. Take their nonnegative square roots. For each positive singular value, compute u=Av/σ using the exact chosen right vector.
3. If a full form is needed, complete the null-space bases. Never divide by zero; never invert a rectangular compact factor.
4. Check orthogonality, dimensions, ordered strengths and the product UΣVᵀ=A.
5. For rank k, keep the first k terms. Reconstruct, then sum the squares of discarded singular values for squared Frobenius error. Take a square root if the error itself is requested.

:::::{admonition} Worked example 5.15 · One matrix, two different kinds of values
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read its eigenpairs</span>

For $A=\operatorname{diag}(4,-2)$, the coordinate vectors are eigenvectors with eigenvalues $4,-2$. It is symmetric but not positive definite.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Put the sign in a left singular direction</span>

$U=\operatorname{diag}(1,-1)$, $\Sigma=\operatorname{diag}(4,2)$, $V=I$ give $U\Sigma V^T=A$. The singular values are $4,2$. Keeping the first gives $A_1=\operatorname{diag}(4,0)$ and squared error $(-2)^2=4$.
::::

::::{div} key-answer

Eigenvalues can carry signs; singular values are nonnegative. Here the rank-one Frobenius error is $2$, not $4$.
::::
:::::

:::{admonition} Before handing it in
:class: pitfall

Do not use zero as an eigenvector; assume every matrix diagonalizes; call arbitrary repeated-eigenvalue vectors perpendicular; replace a general inverse by transpose; forget square roots of Gram eigenvalues; choose unpaired singular-vector signs; change the reconstructed matrix’s outer size; or treat unobserved ratings as zeros. Uncentered SVD energy is not automatically statistical variance or PCA.
:::

**Rehearse:** {ref}`mixed Problems 25–28 <w5-readiness>`. Revisit {ref}`eigenspaces <w5-finding>`, {ref}`diagonalization <w5-diagonalization>`, {ref}`SVD computation <w5-svd-compute>` or {ref}`reduction <w5-reduction>` after diagnosing a mistake.
