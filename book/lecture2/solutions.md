(w2-solution-page)=
# Lecture 2 · Explained solutions

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html"><span class="path-number">01</span><span>Systems & modelling</span></a>
<a href="elimination.html"><span class="path-number">02</span><span>Elimination & echelon forms</span></a>
<a href="practice.html"><span class="path-number">03</span><span>Exercises</span></a>
<a href="solutions.html" aria-current="page"><span class="path-number">04</span><span>Solutions</span></a>
</nav>

Use these after an independent attempt. Compare your setup and row operations,
not only the final numbers. Follow the review link for the underlying idea,
then close this page and attempt the suggested retry.

(w2-s01)=
## Solution 1

The product is $(3,4,1)^T$. By columns it is $3(1,-1,0)^T+7(0,1,-1)^T+8(0,0,1)^T$. Recover $x_1=3$, $x_2=3+4=7$, $x_3=7+1=8$. Both computations agree.

**Review:** {ref}`Section on products <w2-products>`. **Retry:** {ref}`Problem 2 <w2-p02>`. **Return:** {ref}`Problem 1 <w2-p01>`.

(w2-s02)=
## Solution 2

$O=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$ is $2\times3$, and the output is $(4,-1)^T$. The third column is zero: every $(4,-1,t)^T$ gives that same output. Negative coordinates are valid relative to our origin.

**Review:** {ref}`Section on products <w2-products>`. **Retry:** {ref}`Problem 7 <w2-p07>`. **Return:** {ref}`Problem 2 <w2-p02>`.

(w2-s03)=
## Solution 3

$A=\begin{bmatrix}2&-1\\1&3\end{bmatrix}$, $\mathbf b=(5,6)^T$, and $x(2,1)^T+y(-1,3)^T=(5,6)^T$. $R_2\leftarrow R_2-\tfrac12R_1$ gives $\tfrac72 y=\tfrac72$, hence $y=1$, $x=3$. Check: $6-1=5$, $3+3=6$.

**Review:** {ref}`Section on pictures <w2-pictures>`. **Retry:** {ref}`Problem 11 <w2-p11>`. **Return:** {ref}`Problem 3 <w2-p03>`.

(w2-s04)=
## Solution 4

With constant 4 the lines coincide, giving $(2-t,t)$ for real $t$. With constant 5 the lines are distinct and parallel, so no solution. With $x-y=0$, the lines meet once at $(1,1)$. Equation count alone does not distinguish the cases.

**Review:** {ref}`Section on pictures <w2-pictures>`. **Retry:** {ref}`Problem 16 <w2-p16>`. **Return:** {ref}`Problem 4 <w2-p04>`.

(w2-s05)=
## Solution 5

$[A\mid\mathbf b]=\left[\begin{array}{ccc|c}-1&0&2&4\\3&1&0&2\\0&0&1&1\end{array}\right]$. The zeros indicate absent variables. $z=1$ gives $-x+2=4$, hence $x=-2$, and $y+3(-2)=2$ gives $y=8$. Original equations yield $4,2,1$.

**Review:** {ref}`Section on row operations <w2-row-operations>`. **Retry:** {ref}`Problem 12 <w2-p12>`. **Return:** {ref}`Problem 5 <w2-p05>`.

(w2-s06)=
## Solution 6

Scaling by zero erased $x+y=2$. The remaining line includes $(0,0)$, which fails the original first equation. The true solution is $(1,1)$. The legal replacement is reversed by $R_2\leftarrow R_2+3R_1$, retaining row 1 throughout.

**Review:** {ref}`Section on row operations <w2-row-operations>`. **Retry:** {ref}`Problem 5 <w2-p05>`. **Return:** {ref}`Problem 6 <w2-p06>`.

(w2-s07)=
## Solution 7

The matrix is $\left[\begin{array}{ccc|c}1&0&0&2\\0&1&0&3\\0&1&0&3\\0&0&1&9\end{array}\right]$. Subtract row 2 from row 3 and swap the zero row to the bottom. The unique point is $(2,3,9)^T$. With only the front mark it becomes the family $(2,3,t)^T$.

**Review:** {ref}`Section on workflow <w2-workflow>`. **Retry:** {ref}`Problem 8 <w2-p08>`. **Return:** {ref}`Problem 7 <w2-p07>`.

(w2-s08)=
## Solution 8

The stacked right side is $(2,2,4,4)^T$. $R_3\leftarrow R_3-R_2$ produces $[0,0,0\mid2]$, or $0=2$. There is no exact solution. $(2,3,4)^T$ predicts $(2,3,3,4)^T$, failing both Y readings. Averaging would require a separately stated approximate-fitting objective.

**Review:** {ref}`Section on workflow <w2-workflow>`. **Retry:** {ref}`Problem 18 <w2-p18>`. **Return:** {ref}`Problem 8 <w2-p08>`.

(w2-s09)=
## Solution 9

$A$: REF only (nonunit pivots). $B$: RREF; column 3 need not be zero because it is not a pivot column. $C$: neither, because a zero row sits above a nonzero row. $D$: REF only; the 2 lies above the second pivot.

**Review:** {ref}`Section on ref <w2-ref>`. **Retry:** {ref}`Problem 10 <w2-p10>`. **Return:** {ref}`Problem 9 <w2-p09>`.

(w2-s10)=
## Solution 10

Pivot columns are 1,3,4. Column 2 has no pivot; its 3 is allowed. Under the stated augmented interpretation, $x_2=t$, $x_1=3-3t$, $x_3=9$, $x_4=4$, with $t\in\mathbb R$. These satisfy $x_1+3x_2=3$, $x_3=9$, $x_4=4$.

**Review:** {ref}`Section on ref <w2-ref>`. **Retry:** {ref}`Problem 16 <w2-p16>`. **Return:** {ref}`Problem 10 <w2-p10>`.

(w2-s11)=
## Solution 11

$R_2\leftarrow R_2-3R_1$ gives $\left[\begin{array}{cc|c}1&-2&1\\0&8&8\end{array}\right]$, an REF. Then $y=1$ and $x=1+2=3$. Check $3-2=1$, $9+2=11$. It is not necessary to reach RREF to solve.

**Review:** {ref}`Section on gaussian <w2-gaussian>`. **Retry:** {ref}`Problem 3 <w2-p03>`. **Return:** {ref}`Problem 11 <w2-p11>`.

(w2-s12)=
## Solution 12

With original augmented rows $(1,2,3\mid6)$, $(2,5,2\mid4)$, $(6,-3,1\mid2)$, use $R_2-2R_1$ and $R_3-6R_1$ to get $(0,1,-4\mid-8)$ and $(0,-15,-17\mid-34)$. Then $R_3\leftarrow R_3+15R_2$ gives $(0,0,-77\mid-154)$. Thus $z=2$, $y-8=-8$ gives $y=0$, and $x+6=6$ gives $x=0$. Every variable column has a pivot, so the solution is unique. Substituting gives exactly $(6,4,2)^T$.

**Review:** {ref}`Section on gaussian <w2-gaussian>`. **Retry:** {ref}`Problem 13 <w2-p13>`. **Return:** {ref}`Problem 12 <w2-p12>`.

(w2-s13)=
## Solution 13

Swap the two augmented rows to get $[1,1\mid3]$, $[0,2\mid4]$. Then $y=2$, $x=1$; check $2(2)=4$, $1+2=3$. Swapping rows reorders equations. Swapping columns reorders variable meanings and is not one of the elementary row operations used here.

**Review:** {ref}`Section on gaussian <w2-gaussian>`. **Retry:** {ref}`Problem 11 <w2-p11>`. **Return:** {ref}`Problem 13 <w2-p13>`.

(w2-s14)=
## Solution 14

$R_2\leftarrow R_2-3R_1$ gives $[0,1\mid1]$. $R_1\leftarrow R_1-R_2$ gives $[2,0\mid4]$. Divide row 1 by 2 to obtain $\left[\begin{array}{cc|c}1&0&2\\0&1&1\end{array}\right]$. Thus $(x,y)=(2,1)$, and $4+1=5$, $12+4=16$.

**Review:** {ref}`Section on jordan <w2-jordan>`. **Retry:** {ref}`Problem 15 <w2-p15>`. **Return:** {ref}`Problem 14 <w2-p14>`.

(w2-s15)=
## Solution 15

(a) Yes. (b) $z=2$, $y=4$, $x=5$. (c) $R_3\leftarrow-R_3$, then $R_1\leftarrow R_1-3R_3$ and $R_2\leftarrow R_2-R_3$, then $R_1\leftarrow R_1-R_2$. The result is $[I_3\mid(5,4,2)^T]$. Check the original equations as in Example 2.6.

**Review:** {ref}`Section on jordan <w2-jordan>`. **Retry:** {ref}`Problem 14 <w2-p14>`. **Return:** {ref}`Problem 15 <w2-p15>`.

(w2-s16)=
## Solution 16

Pivot variables are $x,z$; $y=t$ is free. All solutions are $(3-2t,t,4)^T$, $t\in\mathbb R$. The first row gives $3-2t+2t=3$ and the second gives $z=4$ for every $t$. Conversely those rows force this form once $y$ is chosen.

**Review:** {ref}`Section on solutions <w2-solutions>`. **Retry:** {ref}`Problem 17 <w2-p17>`. **Return:** {ref}`Problem 16 <w2-p16>`.

(w2-s17)=
## Solution 17

Let $x_2=s$ and $x_4=t$ be independent real parameters. Then $x_1=3-2s+t$, $x_3=5-4t$. All solutions are $(3-2s+t,s,5-4t,t)^T$. Two parameters are necessary. Substitution gives $x_1+2x_2-x_4=3$ and $x_3+4x_4=5$ identically.

**Review:** {ref}`Section on solutions <w2-solutions>`. **Retry:** {ref}`Problem 16 <w2-p16>`. **Return:** {ref}`Problem 17 <w2-p17>`.

(w2-s18)=
## Solution 18

$R_3\leftarrow R_3-R_2$ yields $[0,0,0\mid c-b]$. The system is consistent exactly when $b=c$. When consistent it has the unique point $(a,b,d)^T$, whose readings are $(a,b,b,d)^T$. The repeated Y row adds an agreement test but no new coordinate direction. If $b\ne c$, report no exact solution; do not silently fit an average.

**Review:** {ref}`Section on solutions <w2-solutions>`. **Retry:** {ref}`Problem 8 <w2-p08>`. **Return:** {ref}`Problem 18 <w2-p18>`.
