<!-- answer-01:start -->
(w4-s01)=
:::::{dropdown} Show explained solution 1

::::{div} worked-step

<span class="step-label">Step 1 · Test the dot product</span>

$\mathbf v^T\mathbf w=2+0-2=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check lengths and the sum</span>

$\|\mathbf v\|^2=6$, $\|\mathbf w\|^2=5$, and $\|\mathbf v+\mathbf w\|^2=\|(3,1,1)^T\|^2=11=6+5$.
::::

::::{div} key-answer

Orthogonal, but not orthonormal: the lengths are $\sqrt6$ and $\sqrt5$.
::::

**Diagnose:** If you called the pair orthonormal, you checked the cross dot product but not the two lengths.

**Review:** {ref}`Return to the explanation <w4-orthogonality>`. **Retry:** {ref}`Problem 2 <w4-p02>` with answers closed.
:::::
<!-- answer-01:end -->

<!-- answer-02:start -->
(w4-s02)=
:::::{dropdown} Show explained solution 2

::::{div} worked-step

<span class="step-label">Step 1 · Test both basis pairs</span>

$(1,0,0)\cdot(1,0,1)=1$, while $(0,1,0)\cdot(1,0,1)=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Use the universal condition</span>

Orthogonal subspaces require every pair to have dot product zero. The first basis pair already disproves it.
::::

::::{div} key-answer

$V$ and $W$ are not orthogonal.
::::

**Diagnose:** One zero basis dot product does not test the whole subspace; a single nonzero pair disproves orthogonality.

**Review:** {ref}`Return to the explanation <w4-orthogonality>`. **Retry:** {ref}`Problem 1 <w4-p01>` with answers closed.
:::::
<!-- answer-02:end -->

<!-- answer-03:start -->
(w4-s03)=
:::::{dropdown} Show explained solution 3

::::{div} worked-step

<span class="step-label">Step 1 · Place the spaces</span>

$C(A^T),N(A)\subseteq\mathbb R^4$; $C(A),N(A^T)\subseteq\mathbb R^6$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Apply rank and nullity</span>

Row and column dimensions are $3$; null dimension is $4-3=1$; left-null dimension is $6-3=3$. Each pair adds to its ambient dimension.
::::

::::{div} key-answer

$C(A^T)=N(A)^\perp$ and $C(A)=N(A^T)^\perp$.
::::

**Diagnose:** If the dimensions do not add to 4 and 6 on their respective sides, separate input spaces from output spaces first.

**Review:** {ref}`Return to the explanation <w4-four-spaces>`. **Retry:** {ref}`Problem 4 <w4-p04>` with answers closed.
:::::
<!-- answer-03:end -->

<!-- answer-04:start -->
(w4-s04)=
:::::{dropdown} Show explained solution 4

::::{div} worked-step

<span class="step-label">Step 1 · Solve the homogeneous equations</span>

$x+2y=0$, $z=0$ give $\mathbf x=t(-2,1,0)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test both rows</span>

$(1,2,0)\cdot(-2,1,0)=0$ and $(0,0,1)\cdot(-2,1,0)=0$. The two rows are independent, so the dimensions are $2+1=3$.
::::

::::{div} key-answer

$N(A)=\operatorname{span}\{(-2,1,0)^T\}$.
::::

**Diagnose:** The free coordinate supplies a direction, not a single solution. Check both original row equations.

**Review:** {ref}`Return to the explanation <w4-four-spaces>`. **Retry:** {ref}`Problem 3 <w4-p03>` with answers closed.
:::::
<!-- answer-04:end -->

<!-- answer-05:start -->
(w4-s05)=
:::::{dropdown} Show explained solution 5

::::{div} worked-step

<span class="step-label">Step 1 · Keep allowed coordinates</span>

$P=\operatorname{diag}(1,1,0)$ gives $\mathbf p=(-2,5,0)^T$. $I-P=\operatorname{diag}(0,0,1)$ gives $\mathbf e=(0,0,4)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Verify</span>

$\mathbf p+\mathbf e=\mathbf b$, $\mathbf p^T\mathbf e=0$, and $\|\mathbf b\|^2=45=29+16$. Both matrices are symmetric and idempotent.
::::

::::{div} key-answer

The complementary projection is the discarded z-axis part.
::::

**Diagnose:** The discarded coordinate is the complementary projection, not a second fit in the same plane.

**Review:** {ref}`Return to the explanation <w4-coordinate>`. **Retry:** {ref}`Problem 6 <w4-p06>` with answers closed.
:::::
<!-- answer-05:end -->

<!-- answer-06:start -->
(w4-s06)=
:::::{dropdown} Show explained solution 6

::::{div} worked-step

<span class="step-label">Step 1 · Check the matrix conditions</span>

$B^2=\begin{bmatrix}1&1\\0&0\end{bmatrix}=B$, but $B^T\ne B$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the residual</span>

$B\mathbf b=(1,0)^T$, and $\mathbf b-B\mathbf b=(-1,1)^T$ is not perpendicular to the x-axis. The closest x-axis point is $(0,0)^T$.
::::

::::{div} key-answer

$B$ is idempotent but not an orthogonal projector.
::::

**Diagnose:** An idempotent matrix may project obliquely. Symmetry and a perpendicular residual detect that difference.

**Review:** {ref}`Return to the explanation <w4-coordinate>`. **Retry:** {ref}`Problem 5 <w4-p05>` with answers closed.
:::::
<!-- answer-06:end -->

<!-- answer-07:start -->
(w4-s07)=
:::::{dropdown} Show explained solution 7

::::{div} worked-step

<span class="step-label">Step 1 · Reconcile the repeated coordinate</span>

Keep $X=1$ and $Z=-2$; the middle readings average to $(3+7)/2=5$. Thus $\widehat{\mathbf x}=(1,5,-2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and verify</span>

$\mathbf p=(1,5,5,-2)^T$ and $\mathbf e=(0,-2,2,0)^T$. Multiplying gives $H^T\mathbf e=0$; squared error is $8$.
::::

::::{div} key-answer

The estimate has three entries; the fitted record has four.
::::

**Diagnose:** If you kept either observed Y value, you did not minimize the combined equal-weight error. Keep point coordinates separate from record entries.

**Review:** {ref}`Return to the explanation <w4-why>`. **Retry:** {ref}`Problem 9 <w4-p09>` with answers closed.
:::::
<!-- answer-07:end -->

<!-- answer-08:start -->
(w4-s08)=
:::::{dropdown} Show explained solution 8

::::{div} worked-step

<span class="step-label">Step 1 · Calculate the ratio and matrix</span>

$\widehat x=(8+1)/(4+1)=9/5$ and $P=\frac15\begin{bmatrix}4&2\\2&1\end{bmatrix}$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and check</span>

$\mathbf p=(18/5,9/5)^T$, $\mathbf e=(2/5,-4/5)^T$, and $(2,1)\cdot\mathbf e=4/5-4/5=0$. $P\mathbf b=\mathbf p$ and $\|\mathbf e\|^2=4/5$.
::::

::::{div} key-answer

The projection coefficient is $9/5$, not $9$; the direction is not unit.
::::

**Diagnose:** An answer nine times the direction omits the squared-length denominator; a reversed residual sign is harmless only if used consistently.

**Review:** {ref}`Return to the explanation <w4-line>`. **Retry:** {ref}`Problem 25 <w4-p25>` with answers closed.
:::::
<!-- answer-08:end -->

<!-- answer-09:start -->
(w4-s09)=
:::::{dropdown} Show explained solution 9

::::{div} worked-step

<span class="step-label">Step 1 · Form and solve the normal equations</span>

$A^TA=\operatorname{diag}(2,1)$ and $A^T\mathbf b=(6,2)^T$, giving $\widehat{\mathbf x}=(3,2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Verify the output</span>

$\mathbf p=(3,2,3)^T$ and $\mathbf e=(-2,0,2)^T$. Both column dot products with $\mathbf e$ are zero, so $A^T\mathbf e=0$. Squared error is $8$.
::::

::::{div} key-answer

The fitted plane is $\{(s,t,s)^T\}$, and the closest output has first and last entries averaged.
::::

**Diagnose:** If the first and last fitted entries differ, the proposed output is outside the model column space.

**Review:** {ref}`Return to the explanation <w4-subspace>`. **Retry:** {ref}`Problem 7 <w4-p07>` with answers closed.
:::::
<!-- answer-09:end -->

<!-- answer-10:start -->
(w4-s10)=
:::::{dropdown} Show explained solution 10

::::{div} worked-step

<span class="step-label">Step 1 · Build and solve the normal equations</span>

$A^TA=\begin{bmatrix}2&2\\2&3\end{bmatrix}$ and $A^T\mathbf b=(6,12)^T$.
The equations are $2x_1+2x_2=6$, $2x_1+3x_2=12$. Subtracting gives $x_2=6$, then $x_1=-3$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and check</span>

$\mathbf p=-3(1,1,0)^T+6(1,1,1)^T=(3,3,6)^T$. Then $\mathbf e=(-1,1,0)^T$, $\mathbf a_1^T\mathbf e=0$, $\mathbf a_2^T\mathbf e=0$, and squared error is $2$.
::::

::::{div} key-answer

The nearest vector is $(3,3,6)^T$.
::::

**Diagnose:** Raw column dot products are not coefficients for this nonorthonormal pair. Solve the Gram system before reconstructing.

**Review:** {ref}`Return to the explanation <w4-subspace>`. **Retry:** {ref}`Problem 9 <w4-p09>` with answers closed.
:::::
<!-- answer-10:end -->

<!-- answer-11:start -->
(w4-s11)=
:::::{dropdown} Show explained solution 11

::::{div} worked-step

<span class="step-label">Step 1 · Reduce the repeated-column model</span>

Every output is $(s,0,s)^T$ with $s=x_1+3x_2$. The objective is $(s-2)^2+16+s^2=2(s-1)^2+18$, minimized at $s=1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · State the family and verify</span>

$\widehat{\mathbf x}=(1-3t,t)^T$ gives $\mathbf p=(1,0,1)^T$, $\mathbf e=(1,4,-1)^T$. Both column dot products with the error are zero. $A^TA=\begin{bmatrix}2&6\\6&18\end{bmatrix}$ is singular.
::::

::::{div} key-answer

The minimum squared error is $18$; coefficients are nonunique, but the output is unique.
::::

**Diagnose:** If you tried to invert the Gram matrix, first notice the repeated column direction. A unique output does not imply unique coefficients.

**Review:** {ref}`Return to the explanation <w4-invertibility>`. **Retry:** {ref}`Problem 26 <w4-p26>` with answers closed.
:::::
<!-- answer-11:end -->

<!-- answer-12:start -->
(w4-s12)=
:::::{dropdown} Show explained solution 12

::::{div} worked-step

<span class="step-label">Step 1 · Check symmetry and idempotence</span>

$(I-P)^T=I-P$ and $(I-P)^2=I-2P+P^2=I-P$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Identify its output</span>

If $P$ projects onto $S$, $(I-P)\mathbf b$ is the residual in $S^\perp$. Conversely every $\mathbf v\in S^\perp$ satisfies $P\mathbf v=0$, so $(I-P)\mathbf v=\mathbf v$.
::::

::::{div} key-answer

$I-P$ projects onto $S^\perp$, which is $N(A^T)$ when $S=C(A)$.
::::

**Diagnose:** Idempotence alone does not identify the range: prove the complementary output is perpendicular to S and fixes every vector in that complement.

**Review:** {ref}`Return to the explanation <w4-subspace>`. **Retry:** {ref}`Problem 6 <w4-p06>` with answers closed.
:::::
<!-- answer-12:end -->

<!-- answer-13:start -->
(w4-s13)=
:::::{dropdown} Show explained solution 13

::::{div} worked-step

<span class="step-label">Step 1 · Set up and solve</span>

$A=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}$, $A^TA=\begin{bmatrix}3&3\\3&5\end{bmatrix}$, $A^T\mathbf b=(5,6)^T$. Subtracting the first normal equation from the second gives $2m=1$, then $c=7/6$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the fit</span>

$\mathbf p=(7/6,5/3,13/6)^T$, $\mathbf e=(-1/6,1/3,-1/6)^T$. The residual sums to zero and its $t$-weighted sum is $1/3-2/6=0$. Squared error is $1/6$.
::::

::::{div} key-answer

$y=7/6+t/2$, with squared error $1/6$.
::::

**Diagnose:** If the slope and intercept are swapped, compare your row order with your coefficient order; check both residual sums.

**Review:** {ref}`Return to the explanation <w4-least-squares-fit>`. **Retry:** {ref}`Problem 16 <w4-p16>` with answers closed.
:::::
<!-- answer-13:end -->

<!-- answer-14:start -->
(w4-s14)=
:::::{dropdown} Show explained solution 14

::::{div} worked-step

<span class="step-label">Step 1 · Build the one-column model</span>

$A=(1,1,1,1)^T$, so $A^TA=4$ and $A^T\mathbf b=20$. Hence $\widehat c=5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the residual</span>

$\mathbf e=(-4,-1,2,3)^T$ sums to zero, so it is perpendicular to the constant column. The squared error is $16+1+4+9=30$.
::::

::::{div} key-answer

A constant least-squares fit is the mean because the normal equation is $n\widehat c=\sum b_i$.
::::

**Diagnose:** If the fitted constant is not the mean, check the number of observations in the Gram entry, then the response sum.

**Review:** {ref}`Return to the explanation <w4-least-squares-fit>`. **Retry:** {ref}`Problem 13 <w4-p13>` with answers closed.
:::::
<!-- answer-14:end -->

<!-- answer-15:start -->
(w4-s15)=
:::::{dropdown} Show explained solution 15

::::{div} worked-step

<span class="step-label">Step 1 · Split the error</span>

Write $\mathbf b-\mathbf q=(\mathbf b-\mathbf p)+(\mathbf p-\mathbf q)$. The first part is perpendicular to every column, while the second is in their span.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Apply Pythagoras</span>

$\|\mathbf b-\mathbf q\|^2=\|\mathbf b-\mathbf p\|^2+\|\mathbf p-\mathbf q\|^2$. The second term is nonnegative and vanishes exactly when $\mathbf q=\mathbf p$.
::::

::::{div} key-answer

The closest output is unique, whether or not its coefficients are unique.
::::

**Diagnose:** The Pythagorean split requires perpendicularity to the whole column space, not merely to one chosen fitted vector.

**Review:** {ref}`Return to the explanation <w4-subspace>`. **Retry:** {ref}`Problem 12 <w4-p12>` with answers closed.
:::::
<!-- answer-15:end -->

<!-- answer-16:start -->
(w4-s16)=
:::::{dropdown} Show explained solution 16

::::{div} worked-step

<span class="step-label">Step 1 · Form the sums and solve</span>

$A^TA=\begin{bmatrix}4&6\\6&14\end{bmatrix}$ and $A^T\mathbf b=(37,84)^T$. From $4C+6D=37$, $6C+14D=84$, elimination gives $D=57/10$, $C=7/10$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and verify</span>

$\mathbf p=(7/10,32/5,121/10,89/5)^T$, $\mathbf e=(3/10,8/5,-41/10,11/5)^T$. The residual sum is zero, and $8/5-82/10+33/5=0$. Squared error is $(9+256+1681+484)/100=243/10$.
::::

::::{div} key-answer

$y=7/10+(57/10)t$.
::::

**Diagnose:** Keep the intercept column of ones. A residual sum or weighted sum different from zero locates an arithmetic or model-order error.

**Review:** {ref}`Return to the explanation <w4-least-squares-fit>`. **Retry:** {ref}`Problem 27 <w4-p27>` with answers closed.
:::::
<!-- answer-16:end -->

<!-- answer-17:start -->
(w4-s17)=
:::::{dropdown} Show explained solution 17

::::{div} worked-step

<span class="step-label">Step 1 · Compute all column products</span>

The squared lengths are $2$ and $2$, and the cross dot product is $1-1=0$. Thus $M^TM=2I_2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Normalize and check</span>

$Q=M/\sqrt2$ gives $Q^TQ=I_2$, while $QQ^T=\operatorname{diag}(1,1,0)$. The original columns were orthogonal but not unit.
::::

::::{div} key-answer

Normalizing works here because the columns were already perpendicular.
::::

**Diagnose:** Zero cross dot products establish perpendicularity; diagonal entries of the Gram matrix detect missing normalization.

**Review:** {ref}`Return to the explanation <w4-orthonormal-vectors>`. **Retry:** {ref}`Problem 18 <w4-p18>` with answers closed.
:::::
<!-- answer-17:end -->

<!-- answer-18:start -->
(w4-s18)=
:::::{dropdown} Show explained solution 18

::::{div} worked-step

<span class="step-label">Step 1 · Transpose in reverse order</span>

$(Q_1Q_2)^T(Q_1Q_2)=Q_2^TQ_1^TQ_1Q_2=Q_2^TIQ_2=I$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the inverse</span>

$(Q_1Q_2)^{-1}=Q_2^{-1}Q_1^{-1}=Q_2^TQ_1^T=(Q_1Q_2)^T$. The order reverses because undoing the last operation comes first.
::::

::::{div} key-answer

Products preserve orthogonality; the transpose reverses factor order.
::::

**Diagnose:** Transpose and inverse both reverse factor order. Cancel the two middle factors first.

**Review:** {ref}`Return to the explanation <w4-orthonormal-vectors>`. **Retry:** {ref}`Problem 17 <w4-p17>` with answers closed.
:::::
<!-- answer-18:end -->

<!-- answer-19:start -->
(w4-s19)=
:::::{dropdown} Show explained solution 19

::::{div} worked-step

<span class="step-label">Step 1 · Take components</span>

$\mathbf q_1^T\mathbf b=2\sqrt2$, $\mathbf q_2^T\mathbf b=-1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and check</span>

$\mathbf p=2\sqrt2\mathbf q_1-\mathbf q_2=(2,-1,2)^T$, $\mathbf e=(2,0,-2)^T$. Both basis dot products with $\mathbf e$ are zero; squared error is $8$.
::::

::::{div} key-answer

$\widehat{\mathbf c}=(2\sqrt2,-1)^T$ while the projected vector has three entries.
::::

**Diagnose:** If your coefficient vector has three entries, you have confused basis coordinates with the reconstructed three-dimensional output.

**Review:** {ref}`Return to the explanation <w4-q-projection>`. **Retry:** {ref}`Problem 20 <w4-p20>` with answers closed.
:::::
<!-- answer-19:end -->

<!-- answer-20:start -->
(w4-s20)=
:::::{dropdown} Show explained solution 20

::::{div} worked-step

<span class="step-label">Step 1 · Divide by each squared norm</span>

The columns are perpendicular, so $x_1=(\mathbf u^T\mathbf b)/(\mathbf u^T\mathbf u)=8/4=2$, $x_2=18/9=2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct to check</span>

$2\mathbf u+2\mathbf v=(4,6)^T$. The raw dot products $8,18$ would instead give $(16,54)^T$.
::::

::::{div} key-answer

Orthogonal and orthonormal are different hypotheses.
::::

**Diagnose:** The raw dot-product rule assumes unit lengths. Dividing by each squared length is valid here because the directions are orthogonal.

**Review:** {ref}`Return to the explanation <w4-q-projection>`. **Retry:** {ref}`Problem 19 <w4-p19>` with answers closed.
:::::
<!-- answer-20:end -->

<!-- answer-21:start -->
(w4-s21)=
:::::{dropdown} Show explained solution 21

::::{div} worked-step

<span class="step-label">Step 1 · Remove the first projection</span>

$\mathbf u_1=\mathbf a_1$, with norm squared $2$. Since $\mathbf u_1^T\mathbf a_2=2$, $\mathbf u_2=\mathbf a_2-(2/2)\mathbf u_1=(0,1,0)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Normalize and verify</span>

$\mathbf q_1=(1,0,1)^T/\sqrt2$, $\mathbf q_2=(0,1,0)^T$. Both are unit and have dot product zero. Also $\mathbf a_1=\sqrt2\mathbf q_1$ and $\mathbf a_2=\sqrt2\mathbf q_1+\mathbf q_2$.
::::

::::{div} key-answer

The new basis is orthonormal and spans the original pair.
::::

**Diagnose:** Normalizing the second original input without removing overlap leaves a nonzero cross dot product.

**Review:** {ref}`Return to the explanation <w4-gram-schmidt>`. **Retry:** {ref}`Problem 28 <w4-p28>` with answers closed.
:::::
<!-- answer-21:end -->

<!-- answer-22:start -->
(w4-s22)=
:::::{dropdown} Show explained solution 22

::::{div} worked-step

<span class="step-label">Step 1 · Build the first two directions</span>

$\mathbf u_1=(1,1,0)^T$, $\mathbf u_2=(1,0,0)^T-\tfrac12(1,1,0)^T=(1/2,-1/2,0)^T$. Thus $\mathbf q_1=(1,1,0)^T/\sqrt2$, $\mathbf q_2=(1,-1,0)^T/\sqrt2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test the third remainder</span>

$\mathbf q_1^T\mathbf a_3=3/\sqrt2$, $\mathbf q_2^T\mathbf a_3=1/\sqrt2$. Subtracting gives $(2,1,0)^T-(3/2,3/2,0)^T-(1/2,-1/2,0)^T=0$.
::::

::::{div} key-answer

Two unit directions remain. The third input equals $\mathbf a_1+\mathbf a_2$.
::::

**Diagnose:** A zero third remainder means redundancy, not a third unit vector or failure of the already constructed basis.

**Review:** {ref}`Return to the explanation <w4-gram-schmidt>`. **Retry:** {ref}`Problem 21 <w4-p21>` with answers closed.
:::::
<!-- answer-22:end -->

<!-- answer-23:start -->
(w4-s23)=
:::::{dropdown} Show explained solution 23

::::{div} worked-step

<span class="step-label">Step 1 · Remove the first overlap</span>

$\mathbf u_1=\mathbf a$ has norm squared $6$ and $\mathbf a^T\mathbf b=2$. Thus $\mathbf u_2=\mathbf b-\tfrac13\mathbf a=(2/3,-2/3,0,2/3)^T$, with norm squared $4/3$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Remove both old components</span>

$\mathbf a^T\mathbf c=3$ and $\mathbf u_2^T\mathbf c=0$, so $\mathbf u_3=\mathbf c-\tfrac12\mathbf a=(-1/2,0,0,1/2)^T$, with norm squared $1/2$. The three pairwise dot products are zero.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Choose a clean scaled basis and check</span>

An orthogonal basis is $(1,2,0,1)^T$, $(1,-1,0,1)^T$, $(-1,0,0,1)^T$. Their squared norms are $6,3,2$; divide by $\sqrt6,\sqrt3,\sqrt2$ respectively for an orthonormal basis.
::::

::::{div} key-answer

Scaling each orthogonal vector does not change its direction or the span.
::::

**Diagnose:** Scaled orthogonal answers can differ from the fractions shown. Verify all pairwise dot products and preservation of the original span.

**Review:** {ref}`Return to the explanation <w4-gram-schmidt>`. **Retry:** {ref}`Problem 22 <w4-p22>` with answers closed.
:::::
<!-- answer-23:end -->

<!-- answer-24:start -->
(w4-s24)=
:::::{dropdown} Show explained solution 24

::::{div} worked-step

<span class="step-label">Step 1 · Isolate one coefficient at a time</span>

Dotting with $\mathbf q_i$ kills every term except $x_i\mathbf q_i^T\mathbf q_i=x_i$. Thus $x_i=\mathbf q_i^T\mathbf b$; unit lengths are essential.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compute and verify</span>

$x_1=-1/\sqrt2$, $x_2=1/\sqrt6$, $x_3=4/\sqrt3$. Reconstructing gives $(-1/2,1/2,0)^T+(1/6,1/6,-1/3)^T+(4/3,4/3,4/3)^T=(1,2,1)^T$.
::::

::::{div} key-answer

These are coefficients, not vectors. The worksheet’s printed “xᵢ = qᵢ = b” is a typo.
::::

**Diagnose:** Dot with each unit direction; do not treat a direction vector as a scalar coefficient. The worksheet wording is corrected in the explanation.

**Review:** {ref}`Return to the explanation <w4-q-projection>`. **Retry:** {ref}`Problem 19 <w4-p19>` with answers closed.
:::::
<!-- answer-24:end -->

<!-- answer-25:start -->
(w4-s25)=
:::::{dropdown} Show explained solution 25

::::{div} worked-step

<span class="step-label">Step 1 · Select the one-direction calculation</span>

$\mathbf a\ne0$, $\mathbf a^T\mathbf b=1$, $\mathbf a^T\mathbf a=3$, so $\widehat x=1/3$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct and verify</span>

$\mathbf p=(1/3,-1/3,1/3)^T$, $\mathbf e=(5/3,4/3,-1/3)^T$, and $\mathbf a^T\mathbf e=5/3-4/3-1/3=0$. Squared error is $14/3$.
::::

::::{div} key-answer

The result lies in the requested span and its residual is perpendicular to it.
::::

**Diagnose:** If your candidate is on the line but the residual dot product is nonzero, revisit the projection ratio rather than the line equation.

**Review:** {ref}`Return to the explanation <w4-line>`. **Retry:** {ref}`Problem 8 <w4-p08>` with answers closed.
:::::
<!-- answer-25:end -->

<!-- answer-26:start -->
(w4-s26)=
:::::{dropdown} Show explained solution 26

::::{div} worked-step

<span class="step-label">Step 1 · Identify the actual span</span>

The second column is twice the first. Every output is $s(1,2)^T$ with $s=x_1+2x_2$. The closest multiple has $s=(3+2)/5=1$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · State the family and verify</span>

$\widehat{\mathbf x}=(1-2t,t)^T$ gives $\mathbf p=(1,2)^T$, $\mathbf e=(2,-1)^T$, and $A^T\mathbf e=0$. $A^TA=\begin{bmatrix}5&10\\10&20\end{bmatrix}$ is singular.
::::

::::{div} key-answer

All real $t$ give the unique closest output, with squared error $5$.
::::

**Diagnose:** Two columns do not necessarily supply two independent directions. Detect dependence before using any inverse formula.

**Review:** {ref}`Return to the explanation <w4-invertibility>`. **Retry:** {ref}`Problem 11 <w4-p11>` with answers closed.
:::::
<!-- answer-26:end -->

<!-- answer-27:start -->
(w4-s27)=
:::::{dropdown} Show explained solution 27

::::{div} worked-step

<span class="step-label">Step 1 · Build and solve the model</span>

$A=\begin{bmatrix}1&-1\\1&0\\1&1\end{bmatrix}$, $A^TA=\operatorname{diag}(3,2)$, $A^T\mathbf b=(3,-1)^T$. Thus $c=1$, $m=-1/2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the fitted values</span>

$\mathbf p=(3/2,1,1/2)^T$, $\mathbf e=(1/2,-1,1/2)^T$. Its sum and its $t$-weighted sum are zero. Squared error is $3/2$.
::::

::::{div} key-answer

$y=1-t/2$.
::::

**Diagnose:** A negative horizontal coordinate belongs in the second column with its sign. The two residual sums catch a reversed sign or swapped coefficient.

**Review:** {ref}`Return to the explanation <w4-least-squares-fit>`. **Retry:** {ref}`Problem 16 <w4-p16>` with answers closed.
:::::
<!-- answer-27:end -->

<!-- answer-28:start -->
(w4-s28)=
:::::{dropdown} Show explained solution 28

::::{div} worked-step

<span class="step-label">Step 1 · Construct the basis</span>

$\mathbf u_1=(0,1,1)^T$, $\mathbf u_1^T\mathbf a_2=2$, and $\mathbf u_1^T\mathbf u_1=2$. Subtract to get $\mathbf u_2=(1,0,0)^T$. Hence $\mathbf q_1=(0,1,1)^T/\sqrt2$, $\mathbf q_2=(1,0,0)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Project and verify</span>

$Q^T\mathbf b=(2\sqrt2,2)^T$. Reconstruct $\mathbf p=(2,2,2)^T$, with $\mathbf e=(0,1,-1)^T$. Both basis dot products with $\mathbf e$ are zero; squared error is $2$.
::::

::::{div} key-answer

Constructing the basis and projecting onto it are two separate steps.
::::

**Diagnose:** The component sum has two coefficients but reconstructs a three-entry vector. Check the basis before using its dot products.

**Review:** {ref}`Return to the explanation <w4-gram-schmidt>`. **Retry:** {ref}`Problem 21 <w4-p21>` with answers closed.
:::::
<!-- answer-28:end -->

