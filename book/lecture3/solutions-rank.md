(w3-solutions-rank-page)=
# Complete solutions and rank

<div class="chapter-kicker">Lecture 3 · Page 2 of 4 · Find every answer, then count freedom</div>

A null space tells us which changes leave an output unchanged. Add those changes
to one valid input to get every solution. Rank then counts the independent
constraints and determines how much freedom remains.

<nav class="lecture-path" aria-label="Lecture 3 learning path">
<a href="index.html"><span class="path-number">01</span><span>Spaces & subspaces</span></a>
<a href="solutions-rank.html" aria-current="page"><span class="path-number">02</span><span>Complete solutions & rank</span></a>
<a href="basis.html"><span class="path-number">03</span><span>Independence, span & basis</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Use {ref}`null-space reduction <w3-null-space>` and Lecture 2's row operations.
A **particular solution** is one input that works; it is not automatically the
only one. The handwritten systems below are separate examples with different matrices.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`F · Complete solutions <w3-complete-solutions>`
- {ref}`G · Matrix rank <w3-rank>`
::::

(w3-complete-solutions)=
## F · Complete solutions to a linear system

::::{div} section-intro

**Learning goal:** Separate a particular solution from every null-space direction, or identify inconsistency.

<span class="source-label">Lecture PDF pages 14–17</span>
::::

:::{admonition} Key result · All solutions, when the system is consistent
:class: key-result

$$\boxed{\mathbf x=\mathbf x_p+\mathbf x_n,\qquad \mathbf x_n\in N(A)}.$$

Find $\mathbf x_p$ by setting free variables to zero in a **consistent** reduced
system and solving for pivot variables. Then solve $A\mathbf x_n=0$: set one
free variable at a time to 1 and the others to 0 to get special solutions.
If a contradiction occurs, there is no particular solution to start from.
:::

:::{admonition} Why this gives all solutions
:class: proof

$A(\mathbf x_p+\mathbf x_n)=\mathbf b+0=\mathbf b$. Conversely, any other solution
$\mathbf x$ has $A(\mathbf x-\mathbf x_p)=\mathbf b-\mathbf b=0$, so its difference
from $\mathbf x_p$ belongs to $N(A)$. Both directions matter for completeness.
:::

For $\mathbf b\ne0$, the solution set is a shifted, or **affine**, copy of the
null space. It is not a subspace because it excludes zero. For $\mathbf b=0$,
the complete solution is the null space itself.

:::::{admonition} Worked example 3.6 · Handwritten Q1: one free variable (p. 16)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Reduce the new system</span>

For $x+y+3z=15$, $x+2y+4z=21$, $2x+2y+6z=30$,
apply $R_2\leftarrow R_2-R_1$, $R_3\leftarrow R_3-2R_1$, then
$R_1\leftarrow R_1-R_2$:

$$\left[\begin{array}{ccc|c}1&0&2&9\\0&1&1&6\\0&0&0&0\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Separate a particular input and a null direction</span>

Setting $z=0$ gives $\mathbf x_p=(9,6,0)^T$.
For the homogeneous rows, $x+2z=0$, $y+z=0$; setting $z=1$ gives
$\mathbf s=(-2,-1,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · State and check the complete family</span>

$\mathbf x=(9,6,0)^T+t(-2,-1,1)^T$ for $t\in\mathbb R$.
The first row gives $(9-2t)+(6-t)+3t=15$; the second gives
$(9-2t)+2(6-t)+4t=21$; the third is twice the first and gives 30.
::::

::::{div} key-answer

**Keep this result:** $\boxed{\mathbf x=(9-2t,6-t,t)^T}$, with one arbitrary real parameter.
::::
:::::

:::::{admonition} Worked example 3.7 · Handwritten Q2: two free variables (p. 16)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Keep the original equations</span>

The source uses variables $a,b,c,d$:

$$\begin{aligned}a+2b+3c+5d&=0,\\2a+4b+8c+12d&=6,\\3a+6b+7c+13d&=-6.\end{aligned}$$

Use $R_2\leftarrow R_2-2R_1$, $R_3\leftarrow R_3-3R_1$:

$$\left[\begin{array}{cccc|c}1&2&3&5&0\\0&0&2&2&6\\0&0&-2&-2&-6\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Normalize and clear the pivot in column 3</span>

Use $R_3\leftarrow R_3+R_2$, $R_2\leftarrow\tfrac12R_2$,
then $R_1\leftarrow R_1-3R_2$:

$$\left[\begin{array}{cccc|c}1&2&0&2&-9\\0&0&1&1&3\\0&0&0&0&0\end{array}\right].$$

Thus $b,d$ are free. Set both to zero to obtain $\mathbf x_p=(-9,0,3,0)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Choose one free variable at a time</span>

For the homogeneous system, setting $(b,d)=(1,0)$ gives
$\mathbf s_1=(-2,1,0,0)^T$; setting $(b,d)=(0,1)$ gives
$\mathbf s_2=(-2,0,-1,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Assemble and check</span>

All solutions are

$$\mathbf x=\begin{bmatrix}-9\\0\\3\\0\end{bmatrix}
+s\begin{bmatrix}-2\\1\\0\\0\end{bmatrix}
+t\begin{bmatrix}-2\\0\\-1\\1\end{bmatrix},\qquad s,t\in\mathbb R.$$

Substitution gives $0,6,-6$ for the particular input and $0,0,0$ for each
special direction. Two independent parameters are required.
::::

::::{div} key-answer

**Keep this result:** The correct particular solution is $(-9,0,3,0)^T$; the family has two free directions.
::::
:::::

:::{admonition} Source correction · Check the handwritten particular solution
:class: pitfall

The handwritten result on p. 16 shows first coordinate $-3$. With the displayed
$c=3$, $b=d=0$, that would give $-3+3(3)=6$, not the first equation's 0.
The correct coordinate is **$-9$**. The source's two null directions remain valid.
:::

:::::{admonition} Worked example 3.8 · Handwritten Q3: no particular solution (p. 17)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Eliminate using the displayed original data</span>

For
$\left[\begin{array}{ccc|c}1&1&2&-2\\3&-1&14&6\\1&2&0&0\end{array}\right]$,
use $R_2\leftarrow R_2-3R_1$, $R_3\leftarrow R_3-R_1$:

$$\left[\begin{array}{ccc|c}1&1&2&-2\\0&-4&8&12\\0&1&-2&2\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Expose the contradiction</span>

Scale $R_2\leftarrow-\tfrac14R_2$, giving $[0,1,-2\mid-3]$.
Then $R_3\leftarrow R_3-R_2$ gives $[0,0,0\mid5]$, or $0=5$.
The no-solution conclusion agrees with the handwritten page; the checked
constant follows directly from the original equations rather than its inconsistent intermediate arithmetic.
::::

::::{div} key-answer

**Keep this result:** No solution. Do not write $\mathbf x_p+N(A)$ when no $\mathbf x_p$ exists.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Is setting free variables to zero enough to give the complete answer?
:::

:::{dropdown} Check your reasoning

No. It gives one particular solution when the system is consistent. Add every independent null direction with an arbitrary real coefficient.
:::

::::{div} section-recap

**Keep this:** Consistency first; then one particular input plus all invisible changes.

**Practice:** {ref}`9 <w3-p09>` · {ref}`10 <w3-p10>` · {ref}`11 <w3-p11>` · {ref}`12 <w3-p12>` · {ref}`15 <w3-p15>` · {ref}`16 <w3-p16>`.
::::

(w3-rank)=
## G · Matrix rank

::::{div} section-intro

**Learning goal:** Count independent constraints and distinguish coefficient from augmented rank.

<span class="source-label">Lecture PDF pages 18–21</span>
::::

:::{admonition} Definition · Matrix rank
:class: definition

$\operatorname{rank}(A)=r$ is the number of pivots, equivalently the number of
independent column directions. For an $m\times n$ matrix,

$$0\le r\le\min(m,n).$$

The rank is a nonnegative integer; the zero matrix has rank 0. Count pivots or
nonzero **echelon** rows, not nonzero rows in the original matrix.
:::

:::::{admonition} Worked example 3.9 · The lecture's 2×4 rank example (p. 20)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Eliminate and find pivot columns</span>

For
$M=\begin{bmatrix}1&1&0&1\\2&1&0&5\end{bmatrix}$,
$R_2\leftarrow R_2-2R_1$ gives
$\begin{bmatrix}1&1&0&1\\0&-1&0&3\end{bmatrix}$.
There are two pivots. Negating row 2 and clearing above gives
$\begin{bmatrix}1&0&0&4\\0&1&0&-3\end{bmatrix}$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Explain the count</span>

Columns 1 and 2 of the original matrix are independent in $\mathbb R^2$.
Column 3 is zero; column 4 is $4\mathbf m_1-3\mathbf m_2=(1,5)^T$.
The slide's arrows $(1,1),(1,2),(1,5)$ all lie in this same two-dimensional output space.
::::

::::{div} key-answer

**Keep this result:** $\operatorname{rank}(M)=2$. Four columns do not mean four independent directions.
::::
:::::

:::::{admonition} Worked example 3.10 · The lecture's 3×3 rank question (p. 21)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Clear the first column</span>

For
$T=\begin{bmatrix}1&2&1\\-2&-3&1\\3&5&0\end{bmatrix}$,
use $R_2\leftarrow R_2+2R_1$, $R_3\leftarrow R_3-3R_1$:

$$\begin{bmatrix}1&2&1\\0&1&3\\0&-1&-3\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Count after removing redundancy</span>

$R_3\leftarrow R_3+R_2$ gives a zero row, so there are two pivots.
Further $R_1\leftarrow R_1-2R_2$ gives
$\begin{bmatrix}1&0&-5\\0&1&3\\0&0&0\end{bmatrix}$.
Check the redundancy in the original rows: row 3 = row 1 − row 2.
::::

::::{div} key-answer

**Keep this result:** $\boxed{\operatorname{rank}(T)=2}$, despite three nonzero original rows.
::::
:::::

### Use rank to describe a system

For $A\in\mathbb R^{m\times n}$:

| Rank information | Consequence |
| --- | --- |
| $\operatorname{rank}([A\mid\mathbf b])>\operatorname{rank}(A)$ | Inconsistent |
| Equal ranks $r$ | Consistent, with $n-r$ free variables |
| Consistent and $r=n$ | Unique solution |
| $r=m$ | Every right side is attainable |

A rectangular matrix may have full row rank or full column rank without having
a two-sided inverse. For square matrices, full rank means invertible, as in Lecture 2.

For the views, $\operatorname{rank}(O)=2$ and $\operatorname{rank}(H)=3$:
one independent depth measurement removes the hidden input direction. A duplicate
Y reading does not create a fourth independent direction. Part J gives the
formal dimension counts for all four spaces.

:::{admonition} Check your understanding
:class: checkpoint

A consistent 3×5 system has rank 2. How many free variables does it have?
:::

:::{dropdown} Check your reasoning

$5-2=3$. Use the number of variables, not the number of equations, to count input freedom.
:::

::::{div} section-recap

**Keep this:** Rank counts independent information; consistency decides whether that information can match the target.

**Practice:** {ref}`13 <w3-p13>` · {ref}`14 <w3-p14>` · {ref}`15 <w3-p15>` · {ref}`16 <w3-p16>`.
::::

(w3-practice-solutions)=
## Practice · complete solutions and rank

Try without the hint first. The explained answer is expandable directly below
each question; follow its review link before retrying a missed method.

```{include} practice.md
:start-after: <!-- solutions:start -->
:end-before: <!-- solutions:end -->
```

**Next:** [Page 3 · Independence, span, and basis](basis.md).
