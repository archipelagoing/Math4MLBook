<!-- answer-01:start -->
(w5-s01)=
:::::{dropdown} Show explained solution 1

::::{div} worked-step

<span class="step-label">Step 1 · Multiply each vector</span>

$A\mathbf v=(3,3)^T=3\mathbf v$; $A\mathbf w=(2,0)^T=2\mathbf w$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the defining conditions</span>

Both inputs are nonzero, and each output has one common scalar multiplier.
::::

::::{div} key-answer

The eigenvalues are $3$ for v and $2$ for w.
::::

**Diagnose:** Test the vector equation, not separate coordinate growth.

**Review:** {ref}`Return to the explanation <w5-transformations>`. **Retry:** {ref}`Problem 2 <w5-p02>` with answers closed.
:::::
<!-- answer-01:end -->

<!-- answer-02:start -->
(w5-s02)=
:::::{dropdown} Show explained solution 2

::::{div} worked-step

<span class="step-label">Step 1 · Compute both outputs</span>

$A(1,1)^T=(3,1)^T$ and $A(1,0)^T=(1,0)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compare ratios</span>

The first needs both $\lambda=3$ and $\lambda=1$, so it fails. The second satisfies the equation with $\lambda=1$.
::::

::::{div} key-answer

Only $(1,0)^T$ is an eigenvector among these two candidates.
::::

**Diagnose:** One common multiplier must satisfy every coordinate.

**Review:** {ref}`Return to the explanation <w5-transformations>`. **Retry:** {ref}`Problem 1 <w5-p01>` with answers closed.
:::::
<!-- answer-02:end -->

<!-- answer-03:start -->
(w5-s03)=
:::::{dropdown} Show explained solution 3

::::{div} worked-step

<span class="step-label">Step 1 · Read the coordinate directions</span>

$A\mathbf e_1=-2\mathbf e_1$ and $A\mathbf e_2=0\mathbf e_2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · State all vectors correctly</span>

$E_{-2}=\operatorname{span}\{\mathbf e_1\}$ and $E_0=\operatorname{span}\{\mathbf e_2\}$. Each eigenspace includes zero, but its eigenvectors are its nonzero members.
::::

::::{div} key-answer

The first direction reverses and doubles; the second collapses.
::::

**Diagnose:** Do not exclude a zero eigenvalue by confusing it with the forbidden zero eigenvector.

**Review:** {ref}`Return to the explanation <w5-eigenvectors>`. **Retry:** {ref}`Problem 4 <w5-p04>` with answers closed.
:::::
<!-- answer-03:end -->

<!-- answer-04:start -->
(w5-s04)=
:::::{dropdown} Show explained solution 4

::::{div} worked-step

<span class="step-label">Step 1 · Compute the determinant</span>

$\det(R-\lambda I)=\lambda^2+1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Interpret the roots</span>

There are no real roots, so no nonzero real eigenvectors. Over the complex numbers the roots are $i,-i$; the real-plane conclusion does not deny their existence.
::::

::::{div} key-answer

A quarter-turn has no real eigendirection.
::::

**Diagnose:** “No eigenvectors” must specify the field.

**Review:** {ref}`Return to the explanation <w5-eigenvectors>`. **Retry:** {ref}`Problem 3 <w5-p03>` with answers closed.
:::::
<!-- answer-04:end -->

<!-- answer-05:start -->
(w5-s05)=
:::::{dropdown} Show explained solution 5

::::{div} worked-step

<span class="step-label">Step 1 · Solve for A</span>

$\det(A-\lambda I)=\lambda^2-4\lambda-5=(\lambda-5)(\lambda+1)$. For $5$, $-4v_1+4v_2=0$ gives $(1,1)^T$; for $-1$, $2v_1+4v_2=0$ gives $(-2,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Shift and check</span>

$(A+I)\mathbf v=(\lambda+1)\mathbf v$, so the same eigenspaces have roots $6,0$. Directly $A(1,1)^T=5(1,1)^T$ and $A(-2,1)^T=-(-2,1)^T$.
::::

::::{div} key-answer

Adding $cI$ shifts every eigenvalue by c and preserves its eigenspace.
::::

**Diagnose:** The shift acts on the diagonal only; it does not add one to every entry.

**Review:** {ref}`Return to the explanation <w5-finding>`. **Retry:** {ref}`Problem 6 <w5-p06>` with answers closed.
:::::
<!-- answer-05:end -->

<!-- answer-06:start -->
(w5-s06)=
:::::{dropdown} Show explained solution 6

::::{div} worked-step

<span class="step-label">Step 1 · Find the roots</span>

The triangular matrix has characteristic equation $(4-\lambda)(1-\lambda)=0$, so $4,1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve and check</span>

At $4$, $v_2=0$ gives $t(1,0)^T$. At $1$, $3v_1+2v_2=0$ gives $s(-2,3)^T$. Nonzero $t,s$ are required; $A(-2,3)^T=(-2,3)^T$. The sum $5$ and product $4$ match trace and determinant.
::::

::::{div} key-answer

$E_4=\operatorname{span}\{(1,0)^T\}$ and $E_1=\operatorname{span}\{(-2,3)^T\}$.
::::

**Diagnose:** A single normalized representative is not all eigenvectors.

**Review:** {ref}`Return to the explanation <w5-finding>`. **Retry:** {ref}`Problem 5 <w5-p05>` with answers closed.
:::::
<!-- answer-06:end -->

<!-- answer-07:start -->
(w5-s07)=
:::::{dropdown} Show explained solution 7

::::{div} worked-step

<span class="step-label">Step 1 · Find a basis and matched roots</span>

$5$ has vector $(1,0)^T$; $1$ has vector $(-1,2)^T$. Thus $V=\begin{bmatrix}1&-1\\0&2\end{bmatrix}$, $\Lambda=\operatorname{diag}(5,1)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Invert and verify</span>

$V^{-1}=\begin{bmatrix}1&1/2\\0&1/2\end{bmatrix}$, and $V\Lambda V^{-1}=\begin{bmatrix}5&2\\0&1\end{bmatrix}$. The column dot product is $-1$, so $V^T$ is not its inverse.
::::

::::{div} key-answer

The matrix diagonalizes in a basis that is not orthonormal.
::::

**Diagnose:** Independence permits an inverse; it does not make that inverse a transpose.

**Review:** {ref}`Return to the explanation <w5-diagonalization>`. **Retry:** {ref}`Problem 8 <w5-p08>` with answers closed.
:::::
<!-- answer-07:end -->

<!-- answer-08:start -->
(w5-s08)=
:::::{dropdown} Show explained solution 8

::::{div} worked-step

<span class="step-label">Step 1 · Find each eigenspace</span>

$N(J-3I)=\{(t,0)^T\}$ has dimension $1$, while $N(3I-3I)=\mathbb R^2$ has dimension $2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count basis directions</span>

$J$ lacks two independent eigenvectors. $3I=I(3I)I^{-1}$ already is diagonal.
::::

::::{div} key-answer

A repeated root is compatible with either success or failure; the null-space dimension decides.
::::

**Diagnose:** Multiplicity in the polynomial is not the number of independent eigenvectors.

**Review:** {ref}`Return to the explanation <w5-diagonalization>`. **Retry:** {ref}`Problem 7 <w5-p07>` with answers closed.
:::::
<!-- answer-08:end -->

<!-- answer-09:start -->
(w5-s09)=
:::::{dropdown} Show explained solution 9

::::{div} worked-step

<span class="step-label">Step 1 · Find and normalize the directions</span>

The roots of $(2-\lambda)^2-1$ are $3,1$, with unit vectors $(1,-1)^T/\sqrt2$ and $(1,1)^T/\sqrt2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and interpret</span>

$Q\operatorname{diag}(3,1)Q^T=\tfrac12\begin{bmatrix}4&-2\\-2&4\end{bmatrix}=S$. Both eigenvalues are positive; the orthonormal columns give positive definiteness.
::::

::::{div} key-answer

$S$ is positive definite.
::::

**Diagnose:** Check unit lengths before using the transpose reconstruction.

**Review:** {ref}`Return to the explanation <w5-spectral>`. **Retry:** {ref}`Problem 10 <w5-p10>` with answers closed.
:::::
<!-- answer-09:end -->

<!-- answer-10:start -->
(w5-s10)=
:::::{dropdown} Show explained solution 10

::::{div} worked-step

<span class="step-label">Step 1 · Use a repeated eigenspace</span>

$I_2$ is symmetric and has eigenvectors $(1,0)^T$ and $(1,1)^T$, both for eigenvalue $1$. Their dot product is $1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · State the corrected condition</span>

Distinct eigenvalues of a real symmetric matrix have perpendicular eigenvectors. Within a repeated eigenspace an orthonormal basis can be chosen; arbitrary choices need not be perpendicular.
::::

::::{div} key-answer

The blanket claim is false.
::::

**Diagnose:** The distinct-eigenvalue condition is part of the perpendicularity proof.

**Review:** {ref}`Return to the explanation <w5-spectral>`. **Retry:** {ref}`Problem 9 <w5-p09>` with answers closed.
:::::
<!-- answer-10:end -->

<!-- answer-11:start -->
(w5-s11)=
:::::{dropdown} Show explained solution 11

::::{div} worked-step

<span class="step-label">Step 1 · Match the factor shapes</span>

Full: $U:3\times3$, $\Sigma:3\times5$, $V^T:5\times5$. Compact: $3\times2$, $2\times2$, $2\times5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count surviving and null directions</span>

Column/row dimensions are $2$; left-null dimension is $3-2=1$ and null dimension is $5-2=3$.
::::

::::{div} key-answer

The compact V has shape $5\times2$, so it has no two-sided inverse.
::::

**Diagnose:** Different ambient spaces give different null-space counts.

**Review:** {ref}`Return to the explanation <w5-svd-meaning>`. **Retry:** {ref}`Problem 15 <w5-p15>` with answers closed.
:::::
<!-- answer-11:end -->

<!-- answer-12:start -->
(w5-s12)=
:::::{dropdown} Show explained solution 12

::::{div} worked-step

<span class="step-label">Step 1 · Find the right directions</span>

$A^TA=\operatorname{diag}(0,4)$, so take $\mathbf v_1=\mathbf e_2$, $\mathbf v_2=\mathbf e_1$ and singular values $2,0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Pair and reconstruct</span>

$A\mathbf e_2=2\mathbf e_1$. With $U=I$, $\Sigma=\operatorname{diag}(2,0)$, $V=\begin{bmatrix}0&1\\1&0\end{bmatrix}$, multiplication gives $U\Sigma V^T=A$.
::::

::::{div} key-answer

The zero singular value needs no division; the second left direction completes the basis.
::::

**Diagnose:** Order V by Gram eigenvalue, not by the original coordinate order.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 14 <w5-p14>` with answers closed.
:::::
<!-- answer-12:end -->

<!-- answer-13:start -->
(w5-s13)=
:::::{dropdown} Show explained solution 13

::::{div} worked-step

<span class="step-label">Step 1 · Read both kinds of values</span>

Eigenvalues are $-3,1$; $A^TA=\operatorname{diag}(9,1)$ gives singular values $3,1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Assign the sign to U</span>

$U=\operatorname{diag}(-1,1)$, $\Sigma=\operatorname{diag}(3,1)$, $V=I$ are orthogonal/diagonal factors and multiply to A.
::::

::::{div} key-answer

The negative sign is not a negative singular value.
::::

**Diagnose:** A singular value is a nonnegative length factor.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 17 <w5-p17>` with answers closed.
:::::
<!-- answer-13:end -->

<!-- answer-14:start -->
(w5-s14)=
:::::{dropdown} Show explained solution 14

::::{div} worked-step

<span class="step-label">Step 1 · Solve the Gram problem</span>

$A^TA=\begin{bmatrix}5&3\\3&5\end{bmatrix}$ has eigenvalues $8,2$ and unit directions $(1,1)^T/\sqrt2$, $(1,-1)^T/\sqrt2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Pair and verify</span>

$A\mathbf v_1=(2\sqrt2,0)^T$, $A\mathbf v_2=(0,\sqrt2)^T$, so $U=I$, $\Sigma=\operatorname{diag}(2\sqrt2,\sqrt2)$, $V=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$. Multiplication gives rows $(2,2)$ and $(1,-1)$.
::::

::::{div} key-answer

Both Gram eigenvalues need square roots before becoming singular values.
::::

**Diagnose:** If reconstruction has incorrect signs, compute each u from the exact chosen v.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 12 <w5-p12>` with answers closed.
:::::
<!-- answer-14:end -->

<!-- answer-15:start -->
(w5-s15)=
:::::{dropdown} Show explained solution 15

::::{div} worked-step

<span class="step-label">Step 1 · Choose the positive pair</span>

$A^TA=\operatorname{diag}(0,4)$, so $\mathbf v_1=\mathbf e_2$, $\mathbf u_1=\mathbf e_2$ in $\mathbb R^3$, and $\sigma_1=2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Complete and check</span>

$U=[\mathbf e_2\ \mathbf e_1\ \mathbf e_3]$, $V=[\mathbf e_2\ \mathbf e_1]$ and $\Sigma=\begin{bmatrix}2&0\\0&0\\0&0\end{bmatrix}$ reconstruct A. $N(A)=\operatorname{span}\{\mathbf e_1\}$ in $\mathbb R^2$; $N(A^T)=\operatorname{span}\{\mathbf e_1,\mathbf e_3\}$ in $\mathbb R^3$.
::::

::::{div} key-answer

A full left basis has three directions even though only one column-space direction survives.
::::

**Diagnose:** The first left direction is an output unit vector, not necessarily the first coordinate unit vector.

**Review:** {ref}`Return to the explanation <w5-svd-meaning>`. **Retry:** {ref}`Problem 11 <w5-p11>` with answers closed.
:::::
<!-- answer-15:end -->

<!-- answer-16:start -->
(w5-s16)=
:::::{dropdown} Show explained solution 16

::::{div} worked-step

<span class="step-label">Step 1 · Read the spectral information</span>

The positive singular values are $3,3$; their right subspace is $\operatorname{span}\{\mathbf e_1,\mathbf e_2\}$, and $N(A)=\operatorname{span}\{\mathbf e_3\}$. Any orthonormal basis of the tied subspace is possible.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Show missing output information</span>

$A_1=\begin{bmatrix}3&0&0\\0&3&0\end{bmatrix}$ and $A_2=\begin{bmatrix}-3&0&0\\0&3&0\end{bmatrix}$ have the same Gram matrix but opposite outputs for $\mathbf e_1$. The left vectors depend on A.
::::

::::{div} key-answer

The Gram matrix fixes strengths and right subspaces, not the full output orientation.
::::

**Diagnose:** Tied strengths do not identify a unique basis or a left-vector sign.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 17 <w5-p17>` with answers closed.
:::::
<!-- answer-16:end -->

<!-- answer-17:start -->
(w5-s17)=
:::::{dropdown} Show explained solution 17

::::{div} worked-step

<span class="step-label">Step 1 · Multiply the proposed factors</span>

They give $\operatorname{diag}(-2,1)$, not A, even though U and V are orthogonal.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Flip the matching left direction</span>

Use $U=\operatorname{diag}(-1,1)$ with the same V and Σ. Then the two negative signs cancel in the first outer product, giving A.
::::

::::{div} key-answer

Orthogonal factors and correct strengths are insufficient without reconstruction.
::::

**Diagnose:** Signs must be paired across the same singular term.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 13 <w5-p13>` with answers closed.
:::::
<!-- answer-17:end -->

<!-- answer-18:start -->
(w5-s18)=
:::::{dropdown} Show explained solution 18

::::{div} worked-step

<span class="step-label">Step 1 · Choose full orthogonal bases</span>

Use $U=I_2$, $V=I_3$, and $\Sigma=0_{2\times3}$. Then $U\Sigma V^T=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count rank and nullities</span>

Rank is zero. Row/column spaces both have dimension zero; $N(A)=\mathbb R^3$, $N(A^T)=\mathbb R^2$. There are no positive singular directions in a rank-zero compact form.
::::

::::{div} key-answer

SVD exists without any positive singular values.
::::

**Diagnose:** Never apply u=Av/σ to a zero σ.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 15 <w5-p15>` with answers closed.
:::::
<!-- answer-18:end -->

<!-- answer-19:start -->
(w5-s19)=
:::::{dropdown} Show explained solution 19

::::{div} worked-step

<span class="step-label">Step 1 · Keep the leading terms</span>

The singular values are $6,3,2$, so $R_2=\operatorname{diag}(6,3,0)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the discarded contribution</span>

$R-R_2=\operatorname{diag}(0,0,2)$, giving squared error $4$, Frobenius error $2$ and retained squared-norm fraction $(36+9)/(36+9+4)=45/49$.
::::

::::{div} key-answer

The reconstruction remains $3\times3$.
::::

**Diagnose:** Distinguish squared error from the norm itself.

**Review:** {ref}`Return to the explanation <w5-reduction>`. **Retry:** {ref}`Problem 21 <w5-p21>` with answers closed.
:::::
<!-- answer-19:end -->

<!-- answer-20:start -->
(w5-s20)=
:::::{dropdown} Show explained solution 20

::::{div} worked-step

<span class="step-label">Step 1 · Match dimensions</span>

$U_4:80\times4$, $\Sigma_4:4\times4$ diagonal, $V_4^T:4\times40$. Row coordinates $RV_4$ have size $80\times4$; reconstruction is $80\times40$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count entries actually stored</span>

$4(80+40+1)=484$ factor entries, counting four diagonal strengths, compared with $80\cdot40=3200$ original entries.
::::

::::{div} key-answer

The inner representation shrinks; the outer reconstructed table does not.
::::

**Diagnose:** Do not report k×k as the reconstructed matrix’s size.

**Review:** {ref}`Return to the explanation <w5-reduction>`. **Retry:** {ref}`Problem 19 <w5-p19>` with answers closed.
:::::
<!-- answer-20:end -->

<!-- answer-21:start -->
(w5-s21)=
:::::{dropdown} Show explained solution 21

::::{div} worked-step

<span class="step-label">Step 1 · Keep either tied direction</span>

Both $B_1=\operatorname{diag}(4,2,0)$ and $B_2=\operatorname{diag}(4,0,2)$ keep singular strengths $4,2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Verify the theorem’s error</span>

Each residual has one entry $2$, so its squared Frobenius error is $4$ and error is $2$. Both attain the discarded-strength bound.
::::

::::{div} key-answer

A tied cutoff can make the optimal approximation nonunique.
::::

**Diagnose:** An ordered singular-value list may still have multiple valid tied-direction choices.

**Review:** {ref}`Return to the explanation <w5-reduction>`. **Retry:** {ref}`Problem 19 <w5-p19>` with answers closed.
:::::
<!-- answer-21:end -->

<!-- answer-22:start -->
(w5-s22)=
:::::{dropdown} Show explained solution 22

::::{div} worked-step

<span class="step-label">Step 1 · Match and weight features</span>

$0.2(3)(0.5)+0.8(1)(0.25)=0.3+0.2=0.5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · State the interpretation</span>

The result is a weighted feature score. No target scale, fit or evaluation has been specified, so a calibrated rating is not established.
::::

::::{div} key-answer

Score $0.5$; predictive calibration remains unknown.
::::

**Diagnose:** Correct arithmetic does not establish an unprovided rating scale.

**Review:** {ref}`Return to the explanation <w5-recommendations>`. **Retry:** {ref}`Problem 24 <w5-p24>` with answers closed.
:::::
<!-- answer-22:end -->

<!-- answer-23:start -->
(w5-s23)=
:::::{dropdown} Show explained solution 23

::::{div} worked-step

<span class="step-label">Step 1 · Use only observed targets</span>

The observed-entry objective is $(5-B_{11})^2+(2-B_{22})^2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compare the invented targets</span>

Zero filling adds $B_{12}^2+B_{21}^2$, treating unknown ratings as known zeros. Those are additional constraints, not information in the source table.
::::

::::{div} key-answer

The two optimization problems are different.
::::

**Diagnose:** A question mark is absence of data, not a measured zero.

**Review:** {ref}`Return to the explanation <w5-recommendations>`. **Retry:** {ref}`Problem 28 <w5-p28>` with answers closed.
:::::
<!-- answer-23:end -->

<!-- answer-24:start -->
(w5-s24)=
:::::{dropdown} Show explained solution 24

::::{div} worked-step

<span class="step-label">Step 1 · Test the SVD condition</span>

$L^TL=\begin{bmatrix}1&1\\1&2\end{bmatrix}\ne I$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Separate model types</span>

L can be a user-factor matrix in $LWM^T$ without being orthogonal. Such a product is a general factor model, not automatically an SVD.
::::

::::{div} key-answer

The SVD claim fails; a general factor-model interpretation remains possible.
::::

**Diagnose:** Semantic feature names impose no orthogonality condition by themselves.

**Review:** {ref}`Return to the explanation <w5-recommendations>`. **Retry:** {ref}`Problem 22 <w5-p22>` with answers closed.
:::::
<!-- answer-24:end -->

<!-- answer-25:start -->
(w5-s25)=
:::::{dropdown} Show explained solution 25

::::{div} worked-step

<span class="step-label">Step 1 · Find roots and directions</span>

$\det(A-\lambda I)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. At $5$, $-v_1+2v_2=0$ gives $(2,1)^T$; at $2$, $v_1+v_2=0$ gives $(1,-1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Assemble and check</span>

$V=\begin{bmatrix}2&1\\1&-1\end{bmatrix}$ has determinant $-3$, so it is invertible; $\Lambda=\operatorname{diag}(5,2)$. Directly $A(2,1)^T=(10,5)^T$ and $A(1,-1)^T=(2,-2)^T$, hence $AV=V\Lambda$.
::::

::::{div} key-answer

Each eigenspace is the span of its displayed vector; eigenvectors exclude zero. A diagonalizes.
::::

**Diagnose:** Count independent directions and check the original product, not only the roots.

**Review:** {ref}`Return to the explanation <w5-finding>`. **Retry:** {ref}`Problem 6 <w5-p06>` with answers closed.
:::::
<!-- answer-25:end -->

<!-- answer-26:start -->
(w5-s26)=
:::::{dropdown} Show explained solution 26

::::{div} worked-step

<span class="step-label">Step 1 · Compute strengths and choose directions</span>

$A^TA=2I_2$, so choose $V=I_2$, $\sigma_1=\sigma_2=\sqrt2$. Then $\mathbf u_1=(1,1,0)^T/\sqrt2$ and $\mathbf u_2=(1,-1,0)^T/\sqrt2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Complete and verify</span>

Take $\mathbf u_3=(0,0,1)^T$, $U=[\mathbf u_1\ \mathbf u_2\ \mathbf u_3]$ and $\Sigma=\begin{bmatrix}\sqrt2&0\\0&\sqrt2\\0&0\end{bmatrix}$. The columns are orthonormal, and the scaled first two reconstruct A. $N(A^T)=\operatorname{span}\{\mathbf e_3\}$.
::::

::::{div} key-answer

The tied singular values permit different valid orthonormal paired directions.
::::

**Diagnose:** A full U needs three columns even when A has only two independent outputs.

**Review:** {ref}`Return to the explanation <w5-svd-compute>`. **Retry:** {ref}`Problem 14 <w5-p14>` with answers closed.
:::::
<!-- answer-26:end -->

<!-- answer-27:start -->
(w5-s27)=
:::::{dropdown} Show explained solution 27

::::{div} worked-step

<span class="step-label">Step 1 · Separate signed and nonnegative values</span>

The eigenvalues are $3,-1$; $A^TA=\operatorname{diag}(9,1)$ gives singular values $3,1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Truncate and check</span>

Use $A_1=\operatorname{diag}(3,0)$. Its residual is $\operatorname{diag}(0,-1)$, so squared Frobenius error is $1$ and Frobenius error is $1$. This is the discarded singular value’s square and its square root.
::::

::::{div} key-answer

The negative eigenvalue does not invalidate SVD or change the nonnegative discarded strength.
::::

**Diagnose:** Put the sign in a direction; compute the error from the discarded strength.

**Review:** {ref}`Return to the explanation <w5-reduction>`. **Retry:** {ref}`Problem 13 <w5-p13>` with answers closed.
:::::
<!-- answer-27:end -->

<!-- answer-28:start -->
(w5-s28)=
:::::{dropdown} Show explained solution 28

::::{div} worked-step

<span class="step-label">Step 1 · Use the rank-one condition</span>

If the missing entries are x and y, determinant zero gives $xy=5$. This allows many nonzero choices.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Construct and verify two possibilities</span>

$\begin{bmatrix}5&1\\5&1\end{bmatrix}$ and $\begin{bmatrix}5&5\\1&1\end{bmatrix}$ both have rank one and the observed diagonal entries 5 and 1, but disagree on both blanks. All shown values even lie in a 1–5 range.
::::

::::{div} key-answer

Low rank alone does not identify the missing ratings. More information or modeling assumptions and evaluation are needed.
::::

**Diagnose:** Existence of a low-rank factorization does not imply unique recovery of unobserved entries.

**Review:** {ref}`Return to the explanation <w5-recommendations>`. **Retry:** {ref}`Problem 23 <w5-p23>` with answers closed.
:::::
<!-- answer-28:end -->

