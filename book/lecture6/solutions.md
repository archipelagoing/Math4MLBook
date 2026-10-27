<!-- answer-01:start -->
(w6-s01)=
:::::{dropdown} Show explained solution 1

::::{div} worked-step

<span class="step-label">Step 1 · Count channels as entries</span>

$20\cdot30\cdot3=1800$ feature entries per image.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Place observations in rows</span>

Fifty images form a $50\times1800$ data matrix. Centered rank is at most $\min(49,1800)=49$, not necessarily 49.
::::

::::{div} key-answer

The image is a point in $\mathbb R^{1800}$.
::::

**Diagnose:** Pixels/features are not additional observation rows.

**Review:** {ref}`Return to the explanation <w6-dimensions>`. **Retry:** {ref}`Problem 2 <w6-p02>` with answers closed.
:::::
<!-- answer-01:end -->

<!-- answer-02:start -->
(w6-s02)=
:::::{dropdown} Show explained solution 2

::::{div} worked-step

<span class="step-label">Step 1 · Compute the mean and deviations</span>

$\mu=15/3=5$; deviations are $(-3,-1,4)$, summing to zero.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Translate the feature</span>

Values become $(12,14,19)$ with mean 15; deviations remain $(-3,-1,4)$.
::::

::::{div} key-answer

Centering removes a common translation.
::::

**Diagnose:** Subtract the average of the whole feature, not a separate value-dependent mean.

**Review:** {ref}`Return to the explanation <w6-mean>`. **Retry:** {ref}`Problem 3 <w6-p03>` with answers closed.
:::::
<!-- answer-02:end -->

<!-- answer-03:start -->
(w6-s03)=
:::::{dropdown} Show explained solution 3

::::{div} worked-step

<span class="step-label">Step 1 · Compute the two column means</span>

They are $(3,12)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Subtract by matching feature</span>

Centered rows are $(-2,-2),(0,2),(2,0)$. Both column sums are zero.
::::

::::{div} key-answer

The centered matrix is $\begin{bmatrix}-2&-2\\0&2\\2&0\end{bmatrix}$.
::::

**Diagnose:** Subtracting one row mean mixes unlike features and solves a different problem.

**Review:** {ref}`Return to the explanation <w6-mean>`. **Retry:** {ref}`Problem 2 <w6-p02>` with answers closed.
:::::
<!-- answer-03:end -->

<!-- answer-04:start -->
(w6-s04)=
:::::{dropdown} Show explained solution 4

::::{div} worked-step

<span class="step-label">Step 1 · Center and sum squared deviations</span>

The mean is 3; deviations $(-2,-1,3)$ have squared sum $4+1+9=14$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Apply the stated convention</span>

$s^2=14/(3-1)=7$; $s=\sqrt7$. The population-denominator value would be $14/3$.
::::

::::{div} key-answer

Sample variance $7$; sample standard deviation $\sqrt7$.
::::

**Diagnose:** The square root belongs to standard deviation, not variance.

**Review:** {ref}`Return to the explanation <w6-variance>`. **Retry:** {ref}`Problem 5 <w6-p05>` with answers closed.
:::::
<!-- answer-04:end -->

<!-- answer-05:start -->
(w6-s05)=
:::::{dropdown} Show explained solution 5

::::{div} worked-step

<span class="step-label">Step 1 · Separate centering from scaling</span>

The +100 changes the mean but not centered deviations. Multiplication by 2 doubles every deviation.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Square the scale factor</span>

$s_y^2=2^2\cdot9=36$, so $s_y=6$.
::::

::::{div} key-answer

Variance scales quadratically; standard deviation scales by the absolute scale.
::::

**Diagnose:** An additive shift does not add 100 to the variance.

**Review:** {ref}`Return to the explanation <w6-variance>`. **Retry:** {ref}`Problem 4 <w6-p04>` with answers closed.
:::::
<!-- answer-05:end -->

<!-- answer-06:start -->
(w6-s06)=
:::::{dropdown} Show explained solution 6

::::{div} worked-step

<span class="step-label">Step 1 · Compute centered columns</span>

The mean is $(3,4)^T$; centered rows are $(-2,2),(0,-2),(2,0)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Take paired column products</span>

Each squared-column sum is 8; the cross sum is $-4$. Divide by 2 to get $C=\begin{bmatrix}4&-2\\-2&4\end{bmatrix}$.
::::

::::{div} key-answer

The negative covariance records opposite-sign deviations on balance.
::::

**Diagnose:** Reordering just one feature column destroys the original pairs.

**Review:** {ref}`Return to the explanation <w6-covariance>`. **Retry:** {ref}`Problem 7 <w6-p07>` with answers closed.
:::::
<!-- answer-06:end -->

<!-- answer-07:start -->
(w6-s07)=
:::::{dropdown} Show explained solution 7

::::{div} worked-step

<span class="step-label">Step 1 · Center each feature</span>

The means are $0,2/3$. The cross-deviation sum is $(-1)(1/3)+0(-2/3)+1(1/3)=0$, hence covariance zero.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the relationship</span>

Knowing x determines y exactly; y is not constant. In particular x=0 forces y=0, so these variables are dependent despite zero covariance.
::::

::::{div} key-answer

Zero covariance rules out this linear cross-deviation measure, not all dependence.
::::

**Diagnose:** Uncorrelated and independent are different conclusions.

**Review:** {ref}`Return to the explanation <w6-covariance>`. **Retry:** {ref}`Problem 6 <w6-p06>` with answers closed.
:::::
<!-- answer-07:end -->

<!-- answer-08:start -->
(w6-s08)=
:::::{dropdown} Show explained solution 8

::::{div} worked-step

<span class="step-label">Step 1 · Take dot products</span>

$z_1=(3+3)/\sqrt2=3\sqrt2$, $z_2=(3-3)/\sqrt2=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and check</span>

$z_1\mathbf q_1=(3,-3)^T$, so the residual is zero. This one point lies exactly on the retained line.
::::

::::{div} key-answer

The two-entry loading and one scalar score have different roles.
::::

**Diagnose:** A zero discarded score here is a fact about this point, not all possible inputs.

**Review:** {ref}`Return to the explanation <w6-geometry>`. **Retry:** {ref}`Problem 9 <w6-p09>` with answers closed.
:::::
<!-- answer-08:end -->

<!-- answer-09:start -->
(w6-s09)=
:::::{dropdown} Show explained solution 9

::::{div} worked-step

<span class="step-label">Step 1 · Project and reconstruct</span>

$z=4/\sqrt2=2\sqrt2$ and $\mathbf p=z\mathbf q=(2,2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Verify the residual</span>

$\mathbf e=(-1,1)^T$ has $\mathbf e^T\mathbf q=0$ and squared length 2. Also $\|\mathbf x\|^2=10=z^2+\|\mathbf e\|^2=8+2$.
::::

::::{div} key-answer

The retained squared score is 8 and residual squared error is 2.
::::

**Diagnose:** Use the unit direction and perpendicular error, not a vertical gap.

**Review:** {ref}`Return to the explanation <w6-objective>`. **Retry:** {ref}`Problem 8 <w6-p08>` with answers closed.
:::::
<!-- answer-09:end -->

<!-- answer-10:start -->
(w6-s10)=
:::::{dropdown} Show explained solution 10

::::{div} worked-step

<span class="step-label">Step 1 · Compare with the fixed total</span>

The total squared data norm is $1+1=2$. Counting both identical directions gives 4, exceeding the total.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Identify the invalid premise</span>

The two columns are not orthogonal, so $Q^TQ\ne I$. They do not define a valid two-direction orthogonal coordinate system.
::::

::::{div} key-answer

Orthonormality prevents double-counting the same variation.
::::

**Diagnose:** Two unit vectors are not automatically an orthonormal pair.

**Review:** {ref}`Return to the explanation <w6-objective>`. **Retry:** {ref}`Problem 11 <w6-p11>` with answers closed.
:::::
<!-- answer-10:end -->

<!-- answer-11:start -->
(w6-s11)=
:::::{dropdown} Show explained solution 11

::::{div} worked-step

<span class="step-label">Step 1 · Use the unit constraint</span>

If $v_1^2+v_2^2=1$, the value is $9v_1^2+v_2^2=1+8v_1^2\le9$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Identify equality</span>

Equality needs $v_1^2=1$, $v_2=0$, so $\mathbf v=\pm\mathbf e_1$.
::::

::::{div} key-answer

Maximum sample score variance is 9 in either sign of the first axis.
::::

**Diagnose:** The sign of a PC is not uniquely determined by the variance objective.

**Review:** {ref}`Return to the explanation <w6-eigenproblem>`. **Retry:** {ref}`Problem 10 <w6-p10>` with answers closed.
:::::
<!-- answer-11:end -->

<!-- answer-12:start -->
(w6-s12)=
:::::{dropdown} Show explained solution 12

::::{div} worked-step

<span class="step-label">Step 1 · Convert with the sample denominator</span>

$\lambda_1=36/4=9$, $\lambda_2=4/4=1$. Retained fraction is $9/10=90\%$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check both error normalizations</span>

SSE=$\sigma_2^2=4=(m-1)\lambda_2$; average squared error is $4/5$.
::::

::::{div} key-answer

Covariance eigenvalues are 9 and 1, not 6 and 2.
::::

**Diagnose:** Square singular values and distinguish division by m−1 from division by m.

**Review:** {ref}`Return to the explanation <w6-eigenproblem>`. **Retry:** {ref}`Problem 15 <w6-p15>` with answers closed.
:::::
<!-- answer-12:end -->

<!-- answer-13:start -->
(w6-s13)=
:::::{dropdown} Show explained solution 13

::::{div} worked-step

<span class="step-label">Step 1 · Center and compute covariance</span>

The mean is $(3,0)^T$; centered rows $(-2,0),(0,0),(2,0)$ give $C=\operatorname{diag}(4,0)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Project and reconstruct</span>

Take $\mathbf q_1=\mathbf e_1$, with scores $(-2,0,2)^T$. Add $(3,0)^T$ after reconstruction: every original row returns, with 100% variance and zero SSE.
::::

::::{div} key-answer

One component is exact because all centered variation lies on one line.
::::

**Diagnose:** Add the mean back even when the discarded variance is zero.

**Review:** {ref}`Return to the explanation <w6-algorithm>`. **Retry:** {ref}`Problem 14 <w6-p14>` with answers closed.
:::::
<!-- answer-13:end -->

<!-- answer-14:start -->
(w6-s14)=
:::::{dropdown} Show explained solution 14

::::{div} worked-step

<span class="step-label">Step 1 · Center using the fitted mean</span>

The deviation is $(4,3)^T$; score $z=(12+12)/5=24/5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Decode in the original units</span>

The deviation reconstruction is $(72/25,96/25)^T$. Add the mean to get $(322/25,596/25)^T$. The residual is $(28/25,-21/25)^T$, perpendicular to $(3,4)^T$, with squared length $49/25$.
::::

::::{div} key-answer

Keep the fitted coordinate system; do not recenter a single new point at itself.
::::

**Diagnose:** Refitting the mean on the new point would falsely make its score zero.

**Review:** {ref}`Return to the explanation <w6-algorithm>`. **Retry:** {ref}`Problem 13 <w6-p13>` with answers closed.
:::::
<!-- answer-14:end -->

<!-- answer-15:start -->
(w6-s15)=
:::::{dropdown} Show explained solution 15

::::{div} worked-step

<span class="step-label">Step 1 · Accumulate ordered variances</span>

Total variance is 10. One component gives 70%; two give 90%, so k=2 is the smallest satisfying 85%.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Use the discarded variance</span>

Discarded variance is 1. SSE=$5\cdot1=5$ and mean squared error is $5/6$.
::::

::::{div} key-answer

k=2, SSE=5, average squared error 5/6.
::::

**Diagnose:** The smallest k is determined cumulatively, not by the size of each individual percentage.

**Review:** {ref}`Return to the explanation <w6-explained>`. **Retry:** {ref}`Problem 12 <w6-p12>` with answers closed.
:::::
<!-- answer-15:end -->

<!-- answer-16:start -->
(w6-s16)=
:::::{dropdown} Show explained solution 16

::::{div} worked-step

<span class="step-label">Step 1 · Treat the constant case</span>

Centering gives X=0, C=0. Any basis is possible, but total variance is zero, so EVR is 0/0 and undefined; the mean reconstructs every row.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Treat the tied positive case</span>

For 2I, every unit direction has variance 2. A single component is nonunique but its retained fraction is $2/4=50\%$.
::::

::::{div} key-answer

Nonuniqueness and zero-total-variance are separate issues.
::::

**Diagnose:** Do not report an automatic 100% by dividing zero by zero.

**Review:** {ref}`Return to the explanation <w6-explained>`. **Retry:** {ref}`Problem 11 <w6-p11>` with answers closed.
:::::
<!-- answer-16:end -->

<!-- answer-17:start -->
(w6-s17)=
:::::{dropdown} Show explained solution 17

::::{div} worked-step

<span class="step-label">Step 1 · Compute means and scales</span>

Means are $(4,40)$; sample standard deviations are $(2,20)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Standardize and restore</span>

Rows become $(-1,-1),(0,0),(1,1)$. Restore feature j by multiplying by its scale and adding its mean: $d_1=4+2y_1$, $d_2=40+20y_2$.
::::

::::{div} key-answer

Standardization is feature-wise, and zero scales would require separate handling.
::::

**Diagnose:** Mean shifts and scale factors are not interchangeable.

**Review:** {ref}`Return to the explanation <w6-scaling>`. **Retry:** {ref}`Problem 18 <w6-p18>` with answers closed.
:::::
<!-- answer-17:end -->

<!-- answer-18:start -->
(w6-s18)=
:::::{dropdown} Show explained solution 18

::::{div} worked-step

<span class="step-label">Step 1 · Transform the covariance</span>

The new covariance is diag(4,100); the leading raw axis switches from e₁ to e₂.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Remove marginal scales</span>

Both the original and transformed data have standardized covariance I₂, since covariance is zero and each nonconstant variance becomes one. Standardized leading directions are tied.
::::

::::{div} key-answer

Raw covariance PCA is not invariant to feature rescaling.
::::

**Diagnose:** Variance changes by the square of the unit conversion.

**Review:** {ref}`Return to the explanation <w6-scaling>`. **Retry:** {ref}`Problem 17 <w6-p17>` with answers closed.
:::::
<!-- answer-18:end -->

<!-- answer-19:start -->
(w6-s19)=
:::::{dropdown} Show explained solution 19

::::{div} worked-step

<span class="step-label">Step 1 · Identify the plotted quantities</span>

They are scores along fitted genetic-variation directions, not geographical coordinates. A geography map is an external comparison.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Account for omitted components</span>

Yes. Closeness in the retained score plot does not establish equality in the full original feature space.
::::

::::{div} key-answer

A two-PC plot is a representation with information discarded.
::::

**Diagnose:** Do not interpret score-axis units as physical map units.

**Review:** {ref}`Return to the explanation <w6-applications-reading>`. **Retry:** {ref}`Problem 20 <w6-p20>` with answers closed.
:::::
<!-- answer-19:end -->

<!-- answer-20:start -->
(w6-s20)=
:::::{dropdown} Show explained solution 20

::::{div} worked-step

<span class="step-label">Step 1 · Place the dimensions</span>

$X:100\times600$, $C:600\times600$, $Q_5:600\times5$, $Z:100\times5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count shared versus per-image storage</span>

Each face uses five scores; the shared decoder stores 600 mean entries and $600\cdot5=3000$ loadings. Across 100 faces this is $500+600+3000=4100$ numbers, versus 60000 raw pixels.
::::

::::{div} key-answer

Eigenfaces live in 600-dimensional pixel space, not 100-dimensional observation space.
::::

**Diagnose:** Compression counts must include the shared decoder, not just per-image scores.

**Review:** {ref}`Return to the explanation <w6-applications-reading>`. **Retry:** {ref}`Problem 19 <w6-p19>` with answers closed.
:::::
<!-- answer-20:end -->

<!-- answer-21:start -->
(w6-s21)=
:::::{dropdown} Show explained solution 21

::::{div} worked-step

<span class="step-label">Step 1 · Find each leading eigendirection</span>

Before, e₁ has the largest eigenvalue 3; after, e₂ has the largest eigenvalue 20.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Interpret the changed objective</span>

The extreme observation changed empirical variation. PCA is optimizing the new covariance, not promising stability to unusual points.
::::

::::{div} key-answer

The first component can change substantially under outliers.
::::

**Diagnose:** A high-variance direction may reflect exceptional observations rather than a typical pattern.

**Review:** {ref}`Return to the explanation <w6-failures>`. **Retry:** {ref}`Problem 23 <w6-p23>` with answers closed.
:::::
<!-- answer-21:end -->

<!-- answer-22:start -->
(w6-s22)=
:::::{dropdown} Show explained solution 22

::::{div} worked-step

<span class="step-label">Step 1 · Identify the reconstruction set</span>

One-component linear PCA reconstructs points on a straight affine line through the mean.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compare with the geometry</span>

A genuine curved arc is not contained in that one line, so nonzero residuals generally remain. A nonlinear one-parameter description is a different model.
::::

::::{div} key-answer

Low nonlinear intrinsic dimension does not guarantee exact low linear dimension.
::::

**Diagnose:** The PCA decoder is linear in scores, plus the mean.

**Review:** {ref}`Return to the explanation <w6-failures>`. **Retry:** {ref}`Problem 21 <w6-p21>` with answers closed.
:::::
<!-- answer-22:end -->

<!-- answer-23:start -->
(w6-s23)=
:::::{dropdown} Show explained solution 23

::::{div} worked-step

<span class="step-label">Step 1 · Compute the fraction</span>

$100/100.1=1000/1001\approx99.9001\%$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the task</span>

Keeping only the first coordinate removes the coordinate that distinguishes the classes. Variance retention does not evaluate that supervised goal.
::::

::::{div} key-answer

Nearly 99.9% retained variance can coexist with total loss of the class distinction.
::::

**Diagnose:** PCA does not use class labels in its unsupervised variance objective.

**Review:** {ref}`Return to the explanation <w6-failures>`. **Retry:** {ref}`Problem 21 <w6-p21>` with answers closed.
:::::
<!-- answer-23:end -->

<!-- answer-24:start -->
(w6-s24)=
:::::{dropdown} Show explained solution 24

::::{div} worked-step

<span class="step-label">Step 1 · Choose a meaningful metric</span>

Consider whether their relative numerical scales are meaningful for the task. If unit choice should not drive the result, standardization or another declared common scaling may be appropriate; it is not an automatic rule for every dataset.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Handle constants</span>

A zero-variance feature has no valid standard-deviation divisor. Remove or explicitly retain it separately, and store the fitted preprocessing for future data.
::::

::::{div} key-answer

State and justify the preprocessing metric before interpreting component variance.
::::

**Diagnose:** “Always standardize” can erase a scale difference that was intentionally meaningful.

**Review:** {ref}`Return to the explanation <w6-scaling>`. **Retry:** {ref}`Problem 18 <w6-p18>` with answers closed.
:::::
<!-- answer-24:end -->

<!-- answer-25:start -->
(w6-s25)=
:::::{dropdown} Show explained solution 25

::::{div} worked-step

<span class="step-label">Step 1 · Center each paired feature</span>

Means are $(4,2)$. Centered rows are $(-3,2),(-1,-2),(4,0)$; squared-column sums are 26 and 8, and the cross sum is $-6+2=-4$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Normalize and check</span>

$C=\begin{bmatrix}13&-2\\-2&4\end{bmatrix}$, so standard deviations are $\sqrt{13}$ and 2. The negative cross covariance reflects opposite-sign deviations on balance; C is symmetric and has nonnegative variances.
::::

::::{div} key-answer

Means (4,2), standard deviations (√13,2), covariance −2.
::::

**Diagnose:** Keep paired rows matched and divide the cross sum by m−1.

**Review:** {ref}`Return to the explanation <w6-covariance>`. **Retry:** {ref}`Problem 6 <w6-p06>` with answers closed.
:::::
<!-- answer-25:end -->

<!-- answer-26:start -->
(w6-s26)=
:::::{dropdown} Show explained solution 26

::::{div} worked-step

<span class="step-label">Step 1 · Compute centered covariance</span>

The mean is $(3,4)^T$, so centered rows are $(2,1),(1,2),(-2,-1),(-1,-2)$. Their covariance is $\begin{bmatrix}10/3&8/3\\8/3&10/3\end{bmatrix}$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find and normalize the principal directions</span>

The unit sum/difference directions have eigenvalues $6,2/3$. Choose $\mathbf q_1=(1,1)^T/\sqrt2$; scores are $(3/\sqrt2,3/\sqrt2,-3/\sqrt2,-3/\sqrt2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Reconstruct and verify</span>

Reconstructed rows are $(9/2,11/2),(9/2,11/2),(3/2,5/2),(3/2,5/2)$. Each residual has squared length $1/2$, so SSE=2=$3(2/3)$. Retained fraction is $6/(6+2/3)=90\%$.
::::

::::{div} key-answer

One component meets 90% but not 95%; changing the direction’s sign changes scores’ signs, not reconstructions.
::::

**Diagnose:** Check normalized loadings, original-unit mean restoration and discarded-variance error accounting.

**Review:** {ref}`Return to the explanation <w6-algorithm>`. **Retry:** {ref}`Problem 13 <w6-p13>` with answers closed.
:::::
<!-- answer-26:end -->

<!-- answer-27:start -->
(w6-s27)=
:::::{dropdown} Show explained solution 27

::::{div} worked-step

<span class="step-label">Step 1 · Convert strengths to sample variances</span>

Divide squared singular values by $6-1=5$: covariance eigenvalues are $20,5,0,0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Select and check</span>

One direction retains $20/25=80\%$; two retain 100%, so choose k=2. No positive singular value is discarded, hence SSE=0. A one-direction fit instead has SSE=25.
::::

::::{div} key-answer

Two components are required for 85% under this convention.
::::

**Diagnose:** Explained fractions use squared strengths, and retaining zero components does not add variance.

**Review:** {ref}`Return to the explanation <w6-eigenproblem>`. **Retry:** {ref}`Problem 12 <w6-p12>` with answers closed.
:::::
<!-- answer-27:end -->

<!-- answer-28:start -->
(w6-s28)=
:::::{dropdown} Show explained solution 28

::::{div} worked-step

<span class="step-label">Step 1 · Apply the fitted preprocessing and encode</span>

Standardized deviation is $(2,1)^T$, with score $3/\sqrt2$. Its standardized reconstruction is $(3/2,3/2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Undo and check</span>

Original-unit reconstruction is $(10+2(3/2),100+10(3/2))=(13,115)$. Standardized residual $(1/2,-1/2)^T$ is perpendicular to the loading; original residual is $(1,-5)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Distinguish the metrics</span>

The original decoded line direction is $(2,10)^T/\sqrt2$. Its ordinary dot product with $(1,-5)^T$ is $-48/\sqrt2\ne0$: perpendicularity and optimality here are in standardized coordinates, not unweighted original units.
::::

::::{div} key-answer

Standardization changes the geometry, and the inverse transformation must restore scales as well as means.
::::

**Diagnose:** Do not carry a standardized perpendicularity claim unchanged into an anisotropically scaled original space.

**Review:** {ref}`Return to the explanation <w6-scaling>`. **Retry:** {ref}`Problem 17 <w6-p17>` with answers closed.
:::::
<!-- answer-28:end -->

