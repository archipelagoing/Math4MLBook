<!-- Included explained answers, placed immediately after each question. -->

<!-- answer-01:start -->
(w3-s01)=
:::::{dropdown} Show explained solution 1

::::{div} worked-step

<span class="step-label">Step 1 · Apply the necessary tests</span>

The quadrant fails because $(1,1)$ is allowed but $-(1,1)$ is not. The translated line fails because zero does not satisfy $x+y=2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Prove the remaining case</span>

The line $(t,-3t)$ contains zero. A general combination has form $(\lambda s+\mu t,-3(\lambda s+\mu t))$, so it remains on the line.
::::

**Diagnose:** If zero alone seemed sufficient, review closure under negative scaling.

**Review:** {ref}`Relevant lecture part <w3-subspaces>`. **Retry:** {ref}`Problem 2 <w3-p02>`. **Return:** {ref}`Problem 1 <w3-p01>`.
:::::
<!-- answer-01:end -->

<!-- answer-02:start -->
(w3-s02)=
:::::{dropdown} Show explained solution 2

::::{div} worked-step

<span class="step-label">Step 1 · Parameterize the constraint</span>

Let $y=s,z=t$. Then $x=2s-t$, so every vector is $s(2,1,0)^T+t(-1,0,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check closure</span>

Zero uses $s=t=0$. A real combination simply combines the two parameters, so it still satisfies $x-2y+z=0$. Conversely the parameterization represents every solution.
::::

**Diagnose:** Use arbitrary parameters to establish closure, not a few chosen points.

**Review:** {ref}`Relevant lecture part <w3-subspaces>`. **Retry:** {ref}`Problem 3 <w3-p03>`. **Return:** {ref}`Problem 2 <w3-p02>`.
:::::
<!-- answer-02:end -->

<!-- answer-03:start -->
(w3-s03)=
:::::{dropdown} Show explained solution 3

::::{div} worked-step

<span class="step-label">Step 1 · Select allowed inputs</span>

$(1,0)^T$ and $(0,1)^T$ each belong to the union.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test their sum</span>

The sum $(1,1)^T$ belongs to neither axis. Closure under addition fails, so the union is not a subspace.
::::

**Diagnose:** Different closure requirements must all hold; passing scaling does not imply passing addition.

**Review:** {ref}`Relevant lecture part <w3-subspaces>`. **Retry:** {ref}`Problem 1 <w3-p01>`. **Return:** {ref}`Problem 3 <w3-p03>`.
:::::
<!-- answer-03:end -->

<!-- answer-04:start -->
(w3-s04)=
:::::{dropdown} Show explained solution 4

::::{div} worked-step

<span class="step-label">Step 1 · Solve for the weights</span>

For output $(X,Y,Z)$, $Y=c_2$ and $X=c_1+2c_2$, hence $c_1=X-2Y$. Then $Z=c_1+3c_2=X+Y$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Apply and verify</span>

$C(P)=\{(X,Y,Z):Z=X+Y\}$. The first target uses weights $(2,1)$ and gives $(4,1,5)$. The second fails $6=4+1$ and has no weights.
::::

**Diagnose:** Membership is a consistency question; verify every output coordinate.

**Review:** {ref}`Relevant lecture part <w3-column-space>`. **Retry:** {ref}`Problem 19 <w3-p19>`. **Return:** {ref}`Problem 4 <w3-p04>`.
:::::
<!-- answer-04:end -->

<!-- answer-05:start -->
(w3-s05)=
:::::{dropdown} Show explained solution 5

::::{div} worked-step

<span class="step-label">Step 1 · Reduce and solve</span>

$R_1\leftarrow R_1-2R_2$ gives rows $(1,0,-7)$, $(0,1,3)$. With $x_3=t$, $x_1=7t$, $x_2=-3t$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Verify the generator</span>

$N(A)=\operatorname{span}\{(7,-3,1)^T\}$. Check: $7-6-1=0$ and $-3+3=0$. Every t is allowed, including zero.
::::

**Diagnose:** The special solution is a generator; multiply it by every real coefficient to describe the space.

**Review:** {ref}`Relevant lecture part <w3-null-space>`. **Retry:** {ref}`Problem 6 <w3-p06>`. **Return:** {ref}`Problem 5 <w3-p05>`.
:::::
<!-- answer-05:end -->

<!-- answer-06:start -->
(w3-s06)=
:::::{dropdown} Show explained solution 6

::::{div} worked-step

<span class="step-label">Step 1 · Read the original family</span>

The original solutions are $(-s-t,s,t)^T$. The doubled equation adds nothing, so both parameters remain.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Apply the independent condition</span>

$y=z$ forces $s=t$, leaving $t(-2,1,1)^T$. Removing an independent constraint can enlarge the null space; removing a redundant one need not.
::::

**Diagnose:** Do not equate an extra written row with an extra independent constraint.

**Review:** {ref}`Relevant lecture part <w3-null-space>`. **Retry:** {ref}`Problem 5 <w3-p05>`. **Return:** {ref}`Problem 6 <w3-p06>`.
:::::
<!-- answer-06:end -->

<!-- answer-07:start -->
(w3-s07)=
:::::{dropdown} Show explained solution 7

::::{div} worked-step

<span class="step-label">Step 1 · Separate input and output records</span>

Inputs have 6 entries; outputs have 4. Therefore $N(A)$ and $C(A^T)$ lie in $\mathbb R^6$, while $C(A)$ and $N(A^T)$ lie in $\mathbb R^4$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the left-null product</span>

The equation is $A^T\mathbf y=0$, with $A^T$ of shape $6\times4$ and $\mathbf y\in\mathbb R^4$. Ambient dimension is not automatically the subspace dimension.
::::

**Diagnose:** Left null uses the transpose and an output-sized vector.

**Review:** {ref}`Relevant lecture part <w3-four-spaces>`. **Retry:** {ref}`Problem 8 <w3-p08>`. **Return:** {ref}`Problem 7 <w3-p07>`.
:::::
<!-- answer-07:end -->

<!-- answer-08:start -->
(w3-s08)=
:::::{dropdown} Show explained solution 8

::::{div} worked-step

<span class="step-label">Step 1 · Reduce and select generators</span>

The RREF is $\begin{bmatrix}1&3&0&0\\0&0&1&2\\0&0&0&0\end{bmatrix}$. Original pivot columns $(1,2,0)^T,(1,4,2)^T$ generate $C(A)$; reduced rows $(1,3,0,0)^T,(0,0,1,2)^T$ generate the row space.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve the homogeneous systems and check</span>

$N(A)$ has generators $(-3,1,0,0)^T,(0,0,-2,1)^T$; multiplying by A gives zero. The row relation $-2R_1+R_2-R_3=0$ gives $N(A^T)=\operatorname{span}\{(-2,1,-1)^T\}$. The displayed generators are independent. Their dimensions are 2,2,2,1 in column/null/row/left-null order. The supplied answer uses different independent rows for the row space and the opposite left-null vector $(2,-1,1)^T$; these generate the same spaces.
::::

**Diagnose:** The row relation gives a left-null vector; it is not a null vector of A.

**Review:** {ref}`Relevant lecture part <w3-four-spaces>`. **Retry:** {ref}`Problem 21 <w3-p21>`. **Return:** {ref}`Problem 8 <w3-p08>`.
:::::
<!-- answer-08:end -->

<!-- answer-09:start -->
(w3-s09)=
:::::{dropdown} Show explained solution 9

::::{div} worked-step

<span class="step-label">Step 1 · Reduce the augmented rows</span>

Remove twice row 1 from row 2, move the zero row down, and clear above the y pivot. The nonzero rows are $[1,0,3\mid3]$, $[0,1,-1\mid1]$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Parameterize and check</span>

$\mathbf x=(3,1,0)^T+t(-3,1,1)^T$. The first row gives $3-3t+1+t+2t=4$, the second 8, and the third $1+t-t=1$.
::::

**Diagnose:** A redundant row does not require discarding a free-variable family.

**Review:** {ref}`Relevant lecture part <w3-complete-solutions>`. **Retry:** {ref}`Problem 10 <w3-p10>`. **Return:** {ref}`Problem 9 <w3-p09>`.
:::::
<!-- answer-09:end -->

<!-- answer-10:start -->
(w3-s10)=
:::::{dropdown} Show explained solution 10

::::{div} worked-step

<span class="step-label">Step 1 · Write pivot variables in terms of the free ones</span>

Let $x_3=s,x_4=t$. Then $x_2=2-s+t$ and $x_1=-1+2s-3t$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Separate and verify</span>

$\mathbf x=(-1,2,0,0)^T+s(2,-1,1,0)^T+t(-3,1,0,1)^T$. Substituting yields 3 and 2 independently of s,t; the free coordinates also show the two directions are independent.
::::

**Diagnose:** Use a separate parameter for every free variable; tying them together loses solutions.

**Review:** {ref}`Relevant lecture part <w3-complete-solutions>`. **Retry:** {ref}`Problem 11 <w3-p11>`. **Return:** {ref}`Problem 10 <w3-p10>`.
:::::
<!-- answer-10:end -->

<!-- answer-11:start -->
(w3-s11)=
:::::{dropdown} Show explained solution 11

::::{div} worked-step

<span class="step-label">Step 1 · Expose the conflicting requirement</span>

$R_2\leftarrow R_2-2R_1$ produces $[0,0,0\mid1]$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Conclude correctly</span>

The equation $0=1$ is impossible, so there is no particular solution and no complete family. The coefficient rank is 2; the augmented rank is 3.
::::

**Diagnose:** Do not add a null space to a nonexistent particular solution.

**Review:** {ref}`Relevant lecture part <w3-complete-solutions>`. **Retry:** {ref}`Problem 9 <w3-p09>`. **Return:** {ref}`Problem 11 <w3-p11>`.
:::::
<!-- answer-11:end -->

<!-- answer-12:start -->
(w3-s12)=
:::::{dropdown} Show explained solution 12

::::{div} worked-step

<span class="step-label">Step 1 · Subtract the two equations</span>

For solutions u,v, $A(u-v)=Au-Av=b-b=0$, so $u-v\in N(A)$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the subspace condition</span>

If b=0, the solution set is N(A), a subspace. If b≠0, zero is not a solution; the nonempty set is affine, not a subspace.
::::

**Diagnose:** A translated family can be closed under affine combinations without being a vector subspace.

**Review:** {ref}`Relevant lecture part <w3-complete-solutions>`. **Retry:** {ref}`Problem 25 <w3-p25>`. **Return:** {ref}`Problem 12 <w3-p12>`.
:::::
<!-- answer-12:end -->

<!-- answer-13:start -->
(w3-s13)=
:::::{dropdown} Show explained solution 13

::::{div} worked-step

<span class="step-label">Step 1 · Remove the redundant row</span>

$R_3\leftarrow R_3-R_1-R_2$ is shorthand for two successive legal replacements and produces zero. The first two rows have pivots in columns 1 and 2, so rank is 2.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find and check the freedom</span>

Choose $x_3=t$, then $x_2=-t$, $x_1=2t$. Thus N(M) is generated by $(2,-1,1)^T$; all three original row dot products are zero.
::::

**Diagnose:** Count nonzero rows only after forming an echelon matrix.

**Review:** {ref}`Relevant lecture part <w3-rank>`. **Retry:** {ref}`Problem 14 <w3-p14>`. **Return:** {ref}`Problem 13 <w3-p13>`.
:::::
<!-- answer-13:end -->

<!-- answer-14:start -->
(w3-s14)=
:::::{dropdown} Show explained solution 14

::::{div} worked-step

<span class="step-label">Step 1 · Handle the generic case</span>

For $\alpha\ne0,1$, the triangular matrix has three nonzero diagonal pivots, so rank 3.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Inspect the exceptions directly</span>

At $\alpha=0$, row 2 is zero but row 3 has a pivot −1 in column 3; move it upward, giving rank 2. At $\alpha=1$, rows 1 and 2 have two pivots and row 3 is zero, so rank 2. No value gives rank 1.
::::

**Diagnose:** A zero diagonal entry may still leave a later pivot; examine the matrix, not only its determinant.

**Review:** {ref}`Relevant lecture part <w3-rank>`. **Retry:** {ref}`Problem 26 <w3-p26>`. **Return:** {ref}`Problem 14 <w3-p14>`.
:::::
<!-- answer-14:end -->

<!-- answer-15:start -->
(w3-s15)=
:::::{dropdown} Show explained solution 15

::::{div} worked-step

<span class="step-label">Step 1 · Recover each column</span>

$2\mathbf a_1=(2,4,4)^T$, hence $\mathbf a_1=(1,2,2)^T$. The first null direction gives $\mathbf a_1+\mathbf a_2=0$; the second gives $\mathbf a_3=0$. Thus $A=\begin{bmatrix}1&-1&0\\2&-2&0\\2&-2&0\end{bmatrix}$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Interpret the family and verify</span>

Rank and row-space dimension are 1. Attainable right sides are $s(1,2,2)^T$, equivalently $b_2=2b_1,b_3=2b_1$. Multiplying the given full family gives $(2,4,4)^T$ for every c,d; its two null directions account for all freedom.
::::

**Diagnose:** Use a complete solution as information about the matrix columns; do not guess a matrix from rank alone.

**Review:** {ref}`Relevant lecture part <w3-rank>`. **Retry:** {ref}`Problem 16 <w3-p16>`. **Return:** {ref}`Problem 15 <w3-p15>`.
:::::
<!-- answer-15:end -->

<!-- answer-16:start -->
(w3-s16)=
:::::{dropdown} Show explained solution 16

::::{div} worked-step

<span class="step-label">Step 1 · Distinguish a swap from singularity</span>

The usual second pivot candidate vanishes at $\beta=-2$, but row 3 supplies a swap and the matrix is invertible. The determinant is $-(\beta+1)$, so singularity instead occurs at $\beta=-1$, with rank 2.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check consistency and solve the singular case</span>

At $\beta=-1$, adding reduced row 2 to row 3 gives $0=1+g$. Thus consistency requires $g=-1$. Then $(x,y,z)=(-t,-1-t,t)$; with z=2 it is $(-2,-3,2)$. Substitution gives 1,2,−1. For β≠−1 the solution is unique for any g.
::::

**Diagnose:** A row exchange fixes a temporary zero candidate; it does not imply singularity.

**Review:** {ref}`Relevant lecture part <w3-rank>`. **Retry:** {ref}`Problem 14 <w3-p14>`. **Return:** {ref}`Problem 16 <w3-p16>`.
:::::
<!-- answer-16:end -->

<!-- answer-17:start -->
(w3-s17)=
:::::{dropdown} Show explained solution 17

::::{div} worked-step

<span class="step-label">Step 1 · Handle the two pairs</span>

In (a), $-3\mathbf v_1+\mathbf v_2=0$, so dependent. In (b), $c_1+2c_2=0$ and $2c_1+c_2=0$ force $c_1=c_2=0$, so independent.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the appended zero</span>

In (c), choose coefficient 1 on the zero vector and 0 on the others. This nontrivial coefficient list produces zero, so the whole list is dependent.
::::

**Diagnose:** Different vectors can be multiples; the zero vector always creates dependence.

**Review:** {ref}`Relevant lecture part <w3-independence>`. **Retry:** {ref}`Problem 18 <w3-p18>`. **Return:** {ref}`Problem 17 <w3-p17>`.
:::::
<!-- answer-17:end -->

<!-- answer-18:start -->
(w3-s18)=
:::::{dropdown} Show explained solution 18

::::{div} worked-step

<span class="step-label">Step 1 · Find the dependence relation</span>

$-2\mathbf v_1+\mathbf v_2+\mathbf v_3=0$, so the three-vector list is dependent.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Keep a spanning independent pair</span>

$\mathbf v_1,\mathbf v_2$ already produce every $(x,y)$ uniquely. They are a basis of $\mathbb R^2$; removing $\mathbf v_3$ changes no attainable vectors.
::::

**Diagnose:** Spanning and independence are separate properties; a spanning list need not be a basis.

**Review:** {ref}`Relevant lecture part <w3-span>`. **Retry:** {ref}`Problem 20 <w3-p20>`. **Return:** {ref}`Problem 18 <w3-p18>`.
:::::
<!-- answer-18:end -->

<!-- answer-19:start -->
(w3-s19)=
:::::{dropdown} Show explained solution 19

::::{div} worked-step

<span class="step-label">Step 1 · Characterize all combinations</span>

$a(1,0,1)+b(0,2,1)=(a,2b,a+b)$. Thus $z=x+y/2$ describes exactly the span.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test and check</span>

The first target uses $a=3,b=2$ and satisfies the equation. The second has the same forced a,b but wrong z, so it is outside the span. Neither target is literally one of the listed elements of S.
::::

**Diagnose:** Coordinate matching settles membership; distinguish S from span(S).

**Review:** {ref}`Relevant lecture part <w3-span>`. **Retry:** {ref}`Problem 4 <w3-p04>`. **Return:** {ref}`Problem 19 <w3-p19>`.
:::::
<!-- answer-19:end -->

<!-- answer-20:start -->
(w3-s20)=
:::::{dropdown} Show explained solution 20

::::{div} worked-step

<span class="step-label">Step 1 · Remove redundancy and prove independence</span>

$\mathbf v_3=\mathbf v_1+\mathbf v_2$. In $a\mathbf v_1+b\mathbf v_2=0$, the first and third coordinates force $a=b=0$, so the first two form a basis.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Describe the space</span>

The general vector is $(a,a+b,b)^T$, so the span is the plane $y=x+z$ and its dimension is 2. It is not all of $\mathbb R^3$.
::::

**Diagnose:** After removing redundancy, verify independence and name the space actually spanned.

**Review:** {ref}`Relevant lecture part <w3-basis-dimension>`. **Retry:** {ref}`Problem 17 <w3-p17>`. **Return:** {ref}`Problem 20 <w3-p20>`.
:::::
<!-- answer-20:end -->

<!-- answer-21:start -->
(w3-s21)=
:::::{dropdown} Show explained solution 21

::::{div} worked-step

<span class="step-label">Step 1 · Apply the dimension formulas</span>

Column and row spaces have dimension 3; nullity is $4-3=1$; left nullity is $5-3=2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check full-rank claims</span>

Full row rank would require 5 pivots, and full column rank 4. It has neither. The dimensions 3+1 fill the input count 4; 3+2 fill the output count 5.
::::

**Diagnose:** Use n−r for null space and m−r for left null space.

**Review:** {ref}`Relevant lecture part <w3-basis-dimension>`. **Retry:** {ref}`Problem 8 <w3-p08>`. **Return:** {ref}`Problem 21 <w3-p21>`.
:::::
<!-- answer-21:end -->

<!-- answer-22:start -->
(w3-s22)=
:::::{dropdown} Show explained solution 22

::::{div} worked-step

<span class="step-label">Step 1 · Reconstruct u</span>

$B=\begin{bmatrix}2&1\\1&-1\end{bmatrix}$, so $B(2,-1)^T=(3,3)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find v coefficients and verify</span>

$B^{-1}=\tfrac13\begin{bmatrix}1&1\\1&-2\end{bmatrix}$, so $[\mathbf v]_{\mathcal B}=(1,2)^T$. Reconstruction gives $(2,1)+2(1,-1)=(4,-1)$. Applying $B^{-1}$ to u also returns $(2,-1)$.
::::

**Diagnose:** Identify which coordinate description is given before deciding whether to multiply or invert.

**Review:** {ref}`Relevant lecture part <w3-change-basis>`. **Retry:** {ref}`Problem 23 <w3-p23>`. **Return:** {ref}`Problem 22 <w3-p22>`.
:::::
<!-- answer-22:end -->

<!-- answer-23:start -->
(w3-s23)=
:::::{dropdown} Show explained solution 23

::::{div} worked-step

<span class="step-label">Step 1 · Convert through the common coordinates</span>

$\mathbf x_E=B(2,-1)^T=(1,-1)^T$. Solving $C\mathbf c=(1,-1)^T$ gives $\mathbf c=(1,-2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the direct map</span>

$C^{-1}B=\begin{bmatrix}1&1\\-1&0\end{bmatrix}$ gives $(1,-2)^T$ directly. Multiplying by C reconstructs $(1,-1)^T$.
::::

**Diagnose:** The correct order is destination-basis inverse times source-basis matrix.

**Review:** {ref}`Relevant lecture part <w3-change-basis>`. **Retry:** {ref}`Problem 22 <w3-p22>`. **Return:** {ref}`Problem 23 <w3-p23>`.
:::::
<!-- answer-23:end -->

<!-- answer-24:start -->
(w3-s24)=
:::::{dropdown} Show explained solution 24

::::{div} worked-step

<span class="step-label">Step 1 · Name the represented space</span>

The columns are independent and span $z=x+y$, a two-dimensional subspace of $\mathbb R^3$. Thus B is a valid basis matrix for that plane, with no square inverse.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve for coordinates</span>

The first target has unique coefficients $(2,-1)^T$. The second forces the same first two coefficients but fails the third coordinate $0=2-1$, so it has no coordinates in this plane basis.
::::

**Diagnose:** A rectangular basis can give unique coordinates inside its span without representing every ambient vector.

**Review:** {ref}`Relevant lecture part <w3-basis-dimension>`. **Retry:** {ref}`Problem 19 <w3-p19>`. **Return:** {ref}`Problem 24 <w3-p24>`.
:::::
<!-- answer-24:end -->

<!-- answer-25:start -->
(w3-s25)=
:::::{dropdown} Show explained solution 25

::::{div} worked-step

<span class="step-label">Step 1 · Decide and justify</span>

It contains zero, and any linear combination preserves $x_1-x_2=0$, so it is a subspace.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Give an independent spanning set</span>

Every vector is $(s,s,t)=s(1,1,0)+t(0,0,1)$. The two generators are independent, so this is a basis and the dimension is 2.
::::

**Diagnose:** If the decision or closure argument failed, retry Problem 2. If the basis/count failed, retry Problem 20.

**Review:** {ref}`Relevant lecture part <w3-subspaces>`. **Retry:** {ref}`Problem 2 <w3-p02>`. **Return:** {ref}`Problem 25 <w3-p25>`.
:::::
<!-- answer-25:end -->

<!-- answer-26:start -->
(w3-s26)=
:::::{dropdown} Show explained solution 26

::::{div} worked-step

<span class="step-label">Step 1 · Compare the original rows and constants</span>

Coefficient row 3 is row 1 plus row 2. Those two have pivots, so rank(A)=2. But $9\ne5+3$; replacing row 3 by row 3−row 1−row 2 gives $[0,0,0\mid1]$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · State the consequences</span>

The augmented rank is 3. The contradiction $0=1$ means no solution; no parameter family should be given.
::::

**Diagnose:** If a zero coefficient row was treated as harmless, redo Problem 11 and keep the constant attached.

**Review:** {ref}`Relevant lecture part <w3-complete-solutions>`. **Retry:** {ref}`Problem 11 <w3-p11>`. **Return:** {ref}`Problem 26 <w3-p26>`.
:::::
<!-- answer-26:end -->

<!-- answer-27:start -->
(w3-s27)=
:::::{dropdown} Show explained solution 27

::::{div} worked-step

<span class="step-label">Step 1 · Check redundancy and keep the necessary directions</span>

$\mathbf v_1+\mathbf v_2-\mathbf v_3=0$. The first two are independent because their first and third coordinates force any zero-combination coefficients to vanish. They form a basis of dimension 2.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test the target</span>

$2\mathbf v_1-\mathbf v_2=(2,1,-2)^T$, so the target belongs to the span. This also checks every coordinate of its coefficient representation.
::::

**Diagnose:** If spanning was confused with independence, redo Problem 18 before solving another membership test.

**Review:** {ref}`Relevant lecture part <w3-span>`. **Retry:** {ref}`Problem 20 <w3-p20>`. **Return:** {ref}`Problem 27 <w3-p27>`.
:::::
<!-- answer-27:end -->

<!-- answer-28:start -->
(w3-s28)=
:::::{dropdown} Show explained solution 28

::::{div} worked-step

<span class="step-label">Step 1 · Build and apply the matrix</span>

$B=\begin{bmatrix}2&-1\\1&1\end{bmatrix}$, so $\mathbf x_E=(-5,2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Invert and reconstruct the coefficients</span>

$\det B=3$ and $B^{-1}=\tfrac13\begin{bmatrix}1&1\\-1&2\end{bmatrix}$. Then $B^{-1}(-5,2)^T=\tfrac13(-3,9)^T=(-1,3)^T$, confirming the coordinate direction and determinant division.
::::

**Diagnose:** If the conversion ran backward or columns were swapped, redo Problem 22 and state the basis order aloud.

**Review:** {ref}`Relevant lecture part <w3-change-basis>`. **Retry:** {ref}`Problem 22 <w3-p22>`. **Return:** {ref}`Problem 28 <w3-p28>`.
:::::
<!-- answer-28:end -->
