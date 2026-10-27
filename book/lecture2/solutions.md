<!-- Included answers; not a standalone reader page. -->

<!-- answer-01:start -->
(w2-s01)=
:::{dropdown} Show explained solution 1

The product is $(3,4,1)^T$. By columns it is $3(1,-1,0)^T+7(0,1,-1)^T+8(0,0,1)^T$. Recover $x_1=3$, $x_2=3+4=7$, $x_3=7+1=8$. Both computations agree.

**Review:** {ref}`Section on products <w2-products>`. **Retry:** {ref}`Problem 2 <w2-p02>`. **Return:** {ref}`Problem 1 <w2-p01>`.
:::
<!-- answer-01:end -->

<!-- answer-02:start -->
(w2-s02)=
:::{dropdown} Show explained solution 2

$O=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$ is $2\times3$, and the output is $(4,-1)^T$. The third column is zero: every $(4,-1,t)^T$ gives that same output. Negative coordinates are valid relative to our origin.

**Review:** {ref}`Section on products <w2-products>`. **Retry:** {ref}`Problem 7 <w2-p07>`. **Return:** {ref}`Problem 2 <w2-p02>`.
:::
<!-- answer-02:end -->

<!-- answer-03:start -->
(w2-s03)=
:::{dropdown} Show explained solution 3

$A=\begin{bmatrix}2&-1\\1&3\end{bmatrix}$, $\mathbf b=(5,6)^T$, and $x(2,1)^T+y(-1,3)^T=(5,6)^T$. $R_2\leftarrow R_2-\tfrac12R_1$ gives $\tfrac72 y=\tfrac72$, hence $y=1$, $x=3$. Check: $6-1=5$, $3+3=6$.

**Review:** {ref}`Section on pictures <w2-pictures>`. **Retry:** {ref}`Problem 11 <w2-p11>`. **Return:** {ref}`Problem 3 <w2-p03>`.
:::
<!-- answer-03:end -->

<!-- answer-04:start -->
(w2-s04)=
:::{dropdown} Show explained solution 4

With constant 4 the lines coincide, giving $(2-t,t)$ for real $t$. With constant 5 the lines are distinct and parallel, so no solution. With $x-y=0$, the lines meet once at $(1,1)$. Equation count alone does not distinguish the cases.

**Review:** {ref}`Section on pictures <w2-pictures>`. **Retry:** {ref}`Problem 16 <w2-p16>`. **Return:** {ref}`Problem 4 <w2-p04>`.
:::
<!-- answer-04:end -->

<!-- answer-05:start -->
(w2-s05)=
:::{dropdown} Show explained solution 5

$[A\mid\mathbf b]=\left[\begin{array}{ccc|c}-1&0&2&4\\3&1&0&2\\0&0&1&1\end{array}\right]$. The zeros indicate absent variables. $z=1$ gives $-x+2=4$, hence $x=-2$, and $y+3(-2)=2$ gives $y=8$. Original equations yield $4,2,1$.

**Review:** {ref}`Section on row operations <w2-row-operations>`. **Retry:** {ref}`Problem 12 <w2-p12>`. **Return:** {ref}`Problem 5 <w2-p05>`.
:::
<!-- answer-05:end -->

<!-- answer-06:start -->
(w2-s06)=
:::{dropdown} Show explained solution 6

Scaling by zero erased $x+y=2$. The remaining line includes $(0,0)$, which fails the original first equation. The true solution is $(1,1)$. The legal replacement is reversed by $R_2\leftarrow R_2+3R_1$, retaining row 1 throughout.

**Review:** {ref}`Section on row operations <w2-row-operations>`. **Retry:** {ref}`Problem 5 <w2-p05>`. **Return:** {ref}`Problem 6 <w2-p06>`.
:::
<!-- answer-06:end -->

<!-- answer-07:start -->
(w2-s07)=
:::{dropdown} Show explained solution 7

The matrix is $\left[\begin{array}{ccc|c}1&0&0&2\\0&1&0&3\\0&1&0&3\\0&0&1&9\end{array}\right]$. Subtract row 2 from row 3 and swap the zero row to the bottom. The unique point is $(2,3,9)^T$. With only the front mark it becomes the family $(2,3,t)^T$.

**Review:** {ref}`Section on workflow <w2-workflow>`. **Retry:** {ref}`Problem 8 <w2-p08>`. **Return:** {ref}`Problem 7 <w2-p07>`.
:::
<!-- answer-07:end -->

<!-- answer-08:start -->
(w2-s08)=
:::{dropdown} Show explained solution 8

The stacked right side is $(2,2,4,4)^T$. $R_3\leftarrow R_3-R_2$ produces $[0,0,0\mid2]$, or $0=2$. There is no exact solution. $(2,3,4)^T$ predicts $(2,3,3,4)^T$, failing both Y readings. Averaging would require a separately stated approximate-fitting objective.

**Review:** {ref}`Section on workflow <w2-workflow>`. **Retry:** {ref}`Problem 18 <w2-p18>`. **Return:** {ref}`Problem 8 <w2-p08>`.
:::
<!-- answer-08:end -->

<!-- answer-09:start -->
(w2-s09)=
:::{dropdown} Show explained solution 9

$A$: REF only (nonunit pivots). $B$: RREF; column 3 need not be zero because it is not a pivot column. $C$: neither, because a zero row sits above a nonzero row. $D$: REF only; the 2 lies above the second pivot.

**Review:** {ref}`Section on ref <w2-ref>`. **Retry:** {ref}`Problem 10 <w2-p10>`. **Return:** {ref}`Problem 9 <w2-p09>`.
:::
<!-- answer-09:end -->

<!-- answer-10:start -->
(w2-s10)=
:::{dropdown} Show explained solution 10

Pivot columns are 1,3,4. Column 2 has no pivot; its 3 is allowed. Under the stated augmented interpretation, $x_2=t$, $x_1=3-3t$, $x_3=9$, $x_4=4$, with $t\in\mathbb R$. These satisfy $x_1+3x_2=3$, $x_3=9$, $x_4=4$.

**Review:** {ref}`Section on ref <w2-ref>`. **Retry:** {ref}`Problem 16 <w2-p16>`. **Return:** {ref}`Problem 10 <w2-p10>`.
:::
<!-- answer-10:end -->

<!-- answer-11:start -->
(w2-s11)=
:::{dropdown} Show explained solution 11

$R_2\leftarrow R_2-3R_1$ gives $\left[\begin{array}{cc|c}1&-2&1\\0&8&8\end{array}\right]$, an REF. Then $y=1$ and $x=1+2=3$. Check $3-2=1$, $9+2=11$. It is not necessary to reach RREF to solve.

**Review:** {ref}`Section on gaussian <w2-gaussian>`. **Retry:** {ref}`Problem 3 <w2-p03>`. **Return:** {ref}`Problem 11 <w2-p11>`.
:::
<!-- answer-11:end -->

<!-- answer-12:start -->
(w2-s12)=
:::{dropdown} Show explained solution 12

With original augmented rows $(1,2,3\mid6)$, $(2,5,2\mid4)$, $(6,-3,1\mid2)$, use $R_2-2R_1$ and $R_3-6R_1$ to get $(0,1,-4\mid-8)$ and $(0,-15,-17\mid-34)$. Then $R_3\leftarrow R_3+15R_2$ gives $(0,0,-77\mid-154)$. Thus $z=2$, $y-8=-8$ gives $y=0$, and $x+6=6$ gives $x=0$. Every variable column has a pivot, so the solution is unique. Substituting gives exactly $(6,4,2)^T$.

**Review:** {ref}`Section on gaussian <w2-gaussian>`. **Retry:** {ref}`Problem 13 <w2-p13>`. **Return:** {ref}`Problem 12 <w2-p12>`.
:::
<!-- answer-12:end -->

<!-- answer-13:start -->
(w2-s13)=
:::{dropdown} Show explained solution 13

Swap the two augmented rows to get $[1,1\mid3]$, $[0,2\mid4]$. Then $y=2$, $x=1$; check $2(2)=4$, $1+2=3$. Swapping rows reorders equations. Swapping columns reorders variable meanings and is not one of the elementary row operations used here.

**Review:** {ref}`Section on gaussian <w2-gaussian>`. **Retry:** {ref}`Problem 11 <w2-p11>`. **Return:** {ref}`Problem 13 <w2-p13>`.
:::
<!-- answer-13:end -->

<!-- answer-14:start -->
(w2-s14)=
:::{dropdown} Show explained solution 14

$R_2\leftarrow R_2-3R_1$ gives $[0,1\mid1]$. $R_1\leftarrow R_1-R_2$ gives $[2,0\mid4]$. Divide row 1 by 2 to obtain $\left[\begin{array}{cc|c}1&0&2\\0&1&1\end{array}\right]$. Thus $(x,y)=(2,1)$, and $4+1=5$, $12+4=16$.

**Review:** {ref}`Section on jordan <w2-jordan>`. **Retry:** {ref}`Problem 15 <w2-p15>`. **Return:** {ref}`Problem 14 <w2-p14>`.
:::
<!-- answer-14:end -->

<!-- answer-15:start -->
(w2-s15)=
:::{dropdown} Show explained solution 15

(a) Yes. (b) $z=2$, $y=4$, $x=5$. (c) $R_3\leftarrow-R_3$, then $R_1\leftarrow R_1-3R_3$ and $R_2\leftarrow R_2-R_3$, then $R_1\leftarrow R_1-R_2$. The result is $[I_3\mid(5,4,2)^T]$. Check the original equations as in Example 2.6.

**Review:** {ref}`Section on jordan <w2-jordan>`. **Retry:** {ref}`Problem 14 <w2-p14>`. **Return:** {ref}`Problem 15 <w2-p15>`.
:::
<!-- answer-15:end -->

<!-- answer-16:start -->
(w2-s16)=
:::{dropdown} Show explained solution 16

Pivot variables are $x,z$; $y=t$ is free. All solutions are $(3-2t,t,4)^T$, $t\in\mathbb R$. The first row gives $3-2t+2t=3$ and the second gives $z=4$ for every $t$. Conversely those rows force this form once $y$ is chosen.

**Review:** {ref}`Section on solutions <w2-solutions>`. **Retry:** {ref}`Problem 17 <w2-p17>`. **Return:** {ref}`Problem 16 <w2-p16>`.
:::
<!-- answer-16:end -->

<!-- answer-17:start -->
(w2-s17)=
:::{dropdown} Show explained solution 17

Let $x_2=s$ and $x_4=t$ be independent real parameters. Then $x_1=3-2s+t$, $x_3=5-4t$. All solutions are $(3-2s+t,s,5-4t,t)^T$. Two parameters are necessary. Substitution gives $x_1+2x_2-x_4=3$ and $x_3+4x_4=5$ identically.

**Review:** {ref}`Section on solutions <w2-solutions>`. **Retry:** {ref}`Problem 16 <w2-p16>`. **Return:** {ref}`Problem 17 <w2-p17>`.
:::
<!-- answer-17:end -->

<!-- answer-18:start -->
(w2-s18)=
:::{dropdown} Show explained solution 18

$R_3\leftarrow R_3-R_2$ yields $[0,0,0\mid c-b]$. The system is consistent exactly when $b=c$. When consistent it has the unique point $(a,b,d)^T$, whose readings are $(a,b,b,d)^T$. The repeated Y row adds an agreement test but no new coordinate direction. If $b\ne c$, report no exact solution; do not silently fit an average.

**Review:** {ref}`Section on solutions <w2-solutions>`. **Retry:** {ref}`Problem 8 <w2-p08>`. **Return:** {ref}`Problem 18 <w2-p18>`.
:::
<!-- answer-18:end -->

<!-- answer-19:start -->
(w2-s19)=
:::{dropdown} Show explained solution 19

Row scaling gives $3(-5)=-15$. The swap changes its sign to $15$. Only one row was scaled, so the scale factor is 3, not $3^n$.

**Review:** {ref}`Relevant lecture part <w2-det-properties>`. **Retry:** {ref}`Problem 20 <w2-p20>`. **Return:** {ref}`Problem 19 <w2-p19>`.
:::
<!-- answer-19:end -->

<!-- answer-20:start -->
(w2-s20)=
:::{dropdown} Show explained solution 20

Row 1 gives $1(1)-2(3)+3(0)=-5$. Row 3 gives only $1(1\cdot1-2\cdot3)=-5$. Laplace expansion computes the same determinant along any fixed row or column; sparsity changes the work, not the answer.

**Review:** {ref}`Relevant lecture part <w2-laplace>`. **Retry:** {ref}`Problem 21 <w2-p21>`. **Return:** {ref}`Problem 20 <w2-p20>`.
:::
<!-- answer-20:end -->

<!-- answer-21:start -->
(w2-s21)=
:::{dropdown} Show explained solution 21

The region maps to area $|-3|\cdot4=12$ with reversed orientation. The edge determinant is $1-6=-5$, so the triangle area is $\tfrac12|-5|=\tfrac52$.

**Review:** {ref}`Relevant lecture part <w2-det-applications>`. **Retry:** {ref}`Problem 22 <w2-p22>`. **Return:** {ref}`Problem 21 <w2-p21>`.
:::
<!-- answer-21:end -->

<!-- answer-22:start -->
(w2-s22)=
:::{dropdown} Show explained solution 22

$\det(C)=1$. Swap the diagonal and negate the off-diagonal entries to get $C^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$. Then $\mathbf x=(5-3,-5+6)^T=(2,1)^T$. The original equations give $2(2)+1=5$ and $2+1=3$; both inverse products are identity.

**Review:** {ref}`Relevant lecture part <w2-inverse-2>`. **Retry:** {ref}`Problem 23 <w2-p23>`. **Return:** {ref}`Problem 22 <w2-p22>`.
:::
<!-- answer-22:end -->

<!-- answer-23:start -->
(w2-s23)=
:::{dropdown} Show explained solution 23

$\det(S)=4-4=0$, so no inverse exists. For $(3,6)^T$, $R_2\leftarrow R_2-2R_1$ yields $0=0$ and solutions $(3-2t,t)^T$, $t\in\mathbb R$. For $(3,7)^T$ the same operation yields $0=1$, so there is no solution. Singularity alone does not distinguish these cases.

**Review:** {ref}`Relevant lecture part <w2-invertibility>`. **Retry:** {ref}`Problem 24 <w2-p24>`. **Return:** {ref}`Problem 23 <w2-p23>`.
:::
<!-- answer-23:end -->

<!-- answer-24:start -->
(w2-s24)=
:::{dropdown} Show explained solution 24

Start $[2,1\mid1,0]$, $[1,1\mid0,1]$. Swap rows, then $R_2\leftarrow R_2-2R_1$, giving $[1,1\mid0,1]$, $[0,-1\mid1,-2]$. Negate row 2 and replace $R_1\leftarrow R_1-R_2$. The result is $[I\mid\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}]$. Multiplication on either side by $C$ gives $I_2$.

**Review:** {ref}`Relevant lecture part <w2-inverse-elimination>`. **Retry:** {ref}`Problem 25 <w2-p25>`. **Return:** {ref}`Problem 24 <w2-p24>`.
:::
<!-- answer-24:end -->

<!-- answer-25:start -->
(w2-s25)=
:::{dropdown} Show explained solution 25

The minors are $\begin{bmatrix}-7&-2&4\\7&1&-5\\6&1&-4\end{bmatrix}$. The cofactors are $\begin{bmatrix}-7&2&4\\-7&1&5\\6&-1&-4\end{bmatrix}$; $C_{12}=-M_{12}=2$. Transposing gives $\operatorname{adj}(Q)=\begin{bmatrix}-7&-7&6\\2&1&-1\\4&5&-4\end{bmatrix}$. The determinant is $-7+4+4=1$, so this adjugate is the inverse. Both products with $Q$ give $I_3$.

**Review:** {ref}`Relevant lecture part <w2-inverse-3>`. **Retry:** {ref}`Problem 26 <w2-p26>`. **Return:** {ref}`Problem 25 <w2-p25>`.
:::
<!-- answer-25:end -->

<!-- answer-26:start -->
(w2-s26)=
:::{dropdown} Show explained solution 26

The determinant is zero, there is no inverse, and the homogeneous system has a free variable and hence nonzero solutions. For a general right side it may have no solutions or infinitely many; you must test consistency. It cannot have a unique solution.

**Review:** {ref}`Relevant lecture part <w2-invertibility>`. **Retry:** {ref}`Problem 19 <w2-p19>`. **Return:** {ref}`Problem 26 <w2-p26>`.
:::
<!-- answer-26:end -->
