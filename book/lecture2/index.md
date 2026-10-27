(lecture-two)=
# Systems and elimination

<div class="chapter-kicker">Lecture 2 · Page 1 of 4 · Systems and elimination</div>

This chapter follows **the full Week 2 lecture, in its original topic order**.
Page 1 covers A–D systems; Page 2 covers E–H determinants; Page 3 covers I–N inverses.
Use the {ref}`TL;DR cheat sheet <w2-cheatsheet>` for formulas, method selection,
and a compact worked solve after you have learned the steps.

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Systems & elimination</span></a>
<a href="elimination.html"><span class="path-number">02</span><span>Determinants & geometry</span></a>
<a href="inverses.html"><span class="path-number">03</span><span>Inverses & invertibility</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

You need signed arithmetic, substitution, and Lecture 1's
{ref}`matrix-vector multiplication <w1-products>`. Our running system uses the
fixed variable order $(x,y,z)$:

$$x+y+3z=15,\qquad x+2y+4z=21,\qquad x+y+2z=13.$$

:::{admonition} How to read the examples
:class: key-result

**Blue step labels** name the action; the sentence below explains how and why.
**Yellow results** identify what to retain. **Red pitfalls** flag mistakes that
change the answer. Try the checkpoint, then open its reasoning to check yourself.
:::

::::{div} page-roadmap

**Lecture order · PDF pages 2–21**

- {ref}`A · Systems of linear equations <w2-products>`
- {ref}`B · Gaussian elimination <w2-row-operations>`
- {ref}`C · REF versus RREF <w2-ref>`
- {ref}`D · Worked elimination and solution cases <w2-gaussian>`
::::

(w2-products)=
## A · Systems of linear equations

::::{div} section-intro

**Learning goal:** Read matrix-vector products, row constraints, and column combinations.

<span class="source-label">Lecture PDF pages 2–7</span>
::::

A solution must make **every equation true simultaneously**. Collect coefficients
in $A$, unknowns in $\mathbf x$, and constants in $\mathbf b$:

$$\underbrace{\begin{bmatrix}1&1&3\\1&2&4\\1&1&2\end{bmatrix}}_A
\underbrace{\begin{bmatrix}x\\y\\z\end{bmatrix}}_{\mathbf x}
=\underbrace{\begin{bmatrix}15\\21\\13\end{bmatrix}}_{\mathbf b}.$$

:::{admonition} Definition · Linear system
:class: definition

For $A\in\mathbb R^{m\times n}$, $\mathbf x\in\mathbb R^n$ and
$\mathbf b\in\mathbb R^m$, the system $A\mathbf x=\mathbf b$ means

$$(A\mathbf x)_i=\sum_{j=1}^n a_{ij}x_j=b_i.$$

One equation becomes one row. Missing variables have coefficient zero; terms such
as $xy$ or $x^2$ would make the equations nonlinear.
:::

(w2-pictures)=
### Matrix, row, and column pictures

**Rows:** dot each row with the same unknown vector. Geometrically, two-variable
row equations describe lines; three-variable equations describe planes. A solution
lies on all of them.

**Columns:** the unknowns are weights. If $\mathbf a_j$ is column $j$,

$$A\mathbf x=x_1\mathbf a_1+\cdots+x_n\mathbf a_n.$$

For the running system, this is
$x(1,1,1)^T+y(1,2,1)^T+z(3,4,2)^T=(15,21,13)^T$.
Multiplication predicts an output; solving finds inputs that produce the target.

:::::{admonition} Worked example 2.1 · Matrix-vector multiplication (p. 3)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read the columns</span>

The lecture uses $\mathbf u=(1,-1,0)^T$, $\mathbf v=(0,1,-1)^T$,
$\mathbf w=(0,0,1)^T$:

$$L=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix},\quad
L\mathbf x=\begin{bmatrix}x_1\\x_2-x_1\\x_3-x_2\end{bmatrix}
=x_1\mathbf u+x_2\mathbf v+x_3\mathbf w.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Multiply and reverse the calculation</span>

$L(2,5,9)^T=(2,3,4)^T$. Given that output instead, recover
$x_1=2$, $x_2=2+3=5$, $x_3=5+4=9$. Substitution gives the same three readings.
::::
:::::

:::::{admonition} Worked example 2.2 · Two lines, one solution (p. 4)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Write the same system three ways</span>

For $x-2y=1$, $3x+2y=11$,

$$\begin{bmatrix}1&-2\\3&2\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
=\begin{bmatrix}1\\11\end{bmatrix},\qquad
x\begin{bmatrix}1\\3\end{bmatrix}+y\begin{bmatrix}-2\\2\end{bmatrix}
=\begin{bmatrix}1\\11\end{bmatrix}.$$

The row picture asks where the two lines intersect.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve and check</span>

Add the original equations: $4x=12$, so $x=3$. Then $3-2y=1$ gives
$y=1$. Check both: $3-2=1$, $9+2=11$. The intersection $(3,1)$ supplies the
column weights; $(1,11)$ is the target output.
::::

::::{div} key-answer

**Keep this result:** $(x,y)=(3,1)$; every equation must agree.
::::
:::::

```{figure} ../figures/lecture2/three-pictures.svg
:name: fig-w2-pictures
:alt: Lines x-2y=1 and 3x+2y=11 intersect at (3,1), whose entries weight columns (1,3) and (-2,2) to give (1,11).

Two pictures of the same answer: intersection coordinates are column weights.
```

:::::{admonition} Worked example 2.3 · Three equations, three planes (p. 5)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Translate into a matrix product</span>

The equations are $x+2y+3z=6$, $2x+5y+2z=4$, $6x-3y+z=2$:

$$\begin{bmatrix}1&2&3\\2&5&2\\6&-3&1\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}6\\4\\2\end{bmatrix}.$$

By columns, $x(1,2,6)^T+y(2,5,-3)^T+z(3,2,1)^T=(6,4,2)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find a candidate and verify it</span>

Twice column 3 gives the target, so $(x,y,z)=(0,0,2)$ works.
Check: $3(2)=6$, $2(2)=4$, $1(2)=2$. Substitution proves existence;
{ref}`Problem 12 <w2-p12>` uses elimination to prove uniqueness.
::::
:::::

:::::{admonition} Lecture annotation · Substitution check (p. 6)
:class: connection

::::{div} worked-step

<span class="step-label">Step 1 · Express the same unknown two ways</span>

The handwritten note uses $x+y=3$, $x-y=1$. Rearranging gives
$x=3-y$ and $x=1+y$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Equate, solve, and check</span>

$3-y=1+y$ gives $2y=2$, so $y=1$ and $x=2$.
Check: $2+1=3$ and $2-1=1$. Elimination reaches the same answer by
subtracting the second equation from the first.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

In our running system, which column multiplies $y$?
:::

:::{dropdown} Check your reasoning

Column 2, $(1,2,1)^T$: the coefficients of $y$ across the equations.
:::

::::{div} section-recap

**Keep this:** Rows describe constraints; unknowns weight the columns.

**Practice:** {ref}`1 <w2-p01>` · {ref}`3 <w2-p03>` · {ref}`5 <w2-p05>`.
::::

(w2-row-operations)=
## B · Gaussian elimination

::::{div} section-intro

**Learning goal:** Choose reversible row operations that simplify the system.

<span class="source-label">Lecture PDF pages 7–8</span>
::::

Gaussian elimination simplifies a system by clearing entries **below pivots**.
A pivot is the nonzero entry used to eliminate entries beneath it; in echelon
form it is a row's first nonzero entry.

The **augmented matrix** $[A\mid\mathbf b]$ keeps constants attached to coefficients.
The last column is not another variable. Keep columns in the chosen variable order.

:::{admonition} Key result · Legal row operations
:class: key-result

| Action | Notation | Condition |
| --- | --- | --- |
| Swap equations | $R_i\leftrightarrow R_j$ | Distinct rows |
| Scale an equation | $R_i\leftarrow cR_i$ | $c\ne0$ |
| Add a multiple of another equation | $R_i\leftarrow R_i+cR_j$ | $i\ne j$; retain source row $j$ |

Update the **entire augmented row, including the constant**.
:::

:::{admonition} Why these operations preserve solutions
:class: proof

Each operation can be reversed: swap again, divide by the nonzero scale, or
subtract the added multiple. Therefore old and new equations imply each other.
Scaling by zero is forbidden because it erases an equation.
:::

:::::{admonition} Worked example 2.4 · How one row operation works
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Choose an entry to remove</span>

In the running system, rows 1 and 2 both have $x$ coefficient 1.
To remove $x$ from equation 2, subtract equation 1.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Subtract every matching entry</span>

Use $R_2\leftarrow R_2-R_1$:

$$[1,2,4\mid21]-[1,1,3\mid15]=[0,1,1\mid6].$$

This means $(x+2y+4z)-(x+y+3z)=21-15$, or $y+z=6$.
Adding the unchanged first equation back recovers the original second equation.
::::
:::::

(w2-workflow)=
### General solving steps

1. **Set up:** fix variable order and write $[A\mid\mathbf b]$.
2. **Choose a nonzero pivot:** swap with a lower row if needed. If the remaining
   column is zero, skip it and look right.
3. **Clear below:** with pivot $a\ne0$ in row $k$ and entry $c$ in row $i$, use
   $R_i\leftarrow R_i-(c/a)R_k$. The target becomes $c-(c/a)a=0$.
4. **Finish and check:** back substitute from REF, or continue to RREF; state all
   solutions and substitute into the original equations.

:::{admonition} Check your understanding
:class: checkpoint

Why must $R_2\leftarrow R_2-R_1$ change 21 to 6?
:::

:::{dropdown} Check your reasoning

It subtracts whole equations, including the right sides: $21-15=6$. Leaving 21 changes the problem.
:::

::::{div} section-recap

**Keep this:** Choose a pivot, clear below it, then move right and down.

**Practice:** {ref}`6 <w2-p06>` · {ref}`11 <w2-p11>` · {ref}`13 <w2-p13>`.
::::

(w2-ref)=
## C · Row echelon form versus reduced row echelon form

::::{div} section-intro

**Learning goal:** Recognize the two stopping forms before performing the full reduction.

<span class="source-label">Lecture PDF pages 8</span>
::::

:::{admonition} Definition · REF and RREF
:class: definition

**Row echelon form (REF)** requires zero rows at the bottom, each successive
pivot strictly to the right of the one above, and zeros below every pivot.

**Reduced row echelon form (RREF)** also requires every pivot to be 1 and the
only nonzero entry in its column.
:::

| Test | REF | RREF |
| --- | --- | --- |
| Staircase; zero rows last | Required | Required |
| Zeros below pivots | Required | Required |
| Unit pivots and zeros above | Not required | Required |

Every RREF is REF; the reverse is false. REF may vary with row choices; RREF is unique.
Pivots need not lie on the main diagonal, and rectangular matrices can be RREF.

:::::{admonition} Worked example 2.5 · Classify the lecture's matrix (p. 8)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Find the leading entries</span>

For

$$B=\begin{bmatrix}1&3&0&0&3\\0&0&1&0&9\\0&0&0&1&4\\0&0&0&0&0\end{bmatrix},$$

the pivot columns are **1, 3, 4**. They step right and the zero row is last.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check only the pivot columns</span>

Each pivot is a lone 1, so $B$ is **RREF**. Nonzero entries in nonpivot
columns 2 and 5 are allowed. This is an ordinary matrix; do not assume column 5
is a right side without declaring an augmented interpretation.
::::

::::{div} key-answer

**Keep this result:** REF is a staircase; RREF adds lone unit pivots.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Is $\begin{bmatrix}2&1\\0&3\end{bmatrix}$ REF or RREF?
:::

:::{dropdown} Check your reasoning

REF only: the pivots step right and entries below are zero, but the pivots are not 1 and there is an entry above the second.
:::

::::{div} section-recap

**Keep this:** REF is enough for back substitution; RREF makes pivot equations directly readable.

**Practice:** {ref}`9 <w2-p09>` · {ref}`10 <w2-p10>`.
::::

(w2-gaussian)=
## D · Worked elimination and solution cases

::::{div} section-intro

**Learning goal:** Solve, state all solutions, and verify in the original equations.

<span class="source-label">Lecture PDF pages 9–21</span>
::::

Now apply Parts B–C to the running system. The slides reveal these operations
across pages 9–21; here they form one continuous example.

:::::{admonition} Worked example 2.6 · The lecture's main system
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Augment in the order (x, y, z)</span>

Given $x+y+3z=15$, $x+2y+4z=21$, $x+y+2z=13$,

$$M_0=\left[\begin{array}{ccc|c}1&1&3&15\\1&2&4&21\\1&1&2&13\end{array}\right].$$

Each row records one equation; the constants stay after the bar.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Clear below the first pivot</span>

Both entries below the first 1 are 1. Use the unchanged first row for
$R_2\leftarrow R_2-R_1$ and $R_3\leftarrow R_3-R_1$:

$$M_1=\left[\begin{array}{ccc|c}1&1&3&15\\0&1&1&6\\0&0&-1&-2\end{array}\right].$$

For row 3, subtract entrywise:
$[1-1,1-1,2-3\mid13-15]=[0,0,-1\mid-2]$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Recognize REF and stop the forward stage</span>

Pivots in columns 1, 2, 3 step right. The entry below pivot 2 is already
zero, so no further forward operation is needed. $M_1$ is REF, **not RREF**:
the final pivot is $-1$ and entries remain above pivots.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Back substitute from bottom to top</span>

Solve one unknown at a time:

$$\begin{aligned}-z=-2&\Rightarrow z=2,\\y+z=6&\Rightarrow y=6-2=4,\\
x+y+3z=15&\Rightarrow x=15-4-6=5.\end{aligned}$$

The system is now solved. Use the next step only if RREF is requested.
::::

::::{div} worked-step

<span class="step-label">Step 5 · If requested, continue to RREF</span>

Normalize the final pivot: $R_3\leftarrow-R_3$. Then remove $z$ above it
with $R_1\leftarrow R_1-3R_3$ and $R_2\leftarrow R_2-R_3$:

$$\left[\begin{array}{ccc|c}1&1&3&15\\0&1&1&6\\0&0&1&2\end{array}\right]
\longrightarrow
\left[\begin{array}{ccc|c}1&1&0&9\\0&1&0&4\\0&0&1&2\end{array}\right].$$

Finally $R_1\leftarrow R_1-R_2$ removes $y$ above pivot 2:

$$\left[\begin{array}{ccc|c}1&0&0&5\\0&1&0&4\\0&0&1&2\end{array}\right].$$

This **Gauss–Jordan continuation** produces RREF and the same solution.
::::

::::{div} worked-step

<span class="step-label">Step 6 · Check the original equations</span>

Substitute all three values into all three original equations:

$$\begin{aligned}5+4+3(2)&=15,\\5+2(4)+4(2)&=21,\\5+4+2(2)&=13.\end{aligned}$$

No contradiction and a pivot for every unknown establish uniqueness.
::::

::::{div} key-answer

**Keep this result:** $\boxed{\mathbf x=(5,4,2)^T}$. REF plus back substitution and RREF give the same answer.
::::
:::::

(w2-jordan)=
### Know the requested endpoint

**Find REF:** stop at the staircase. **Solve:** back substitute, or read from RREF.
**Find RREF:** make unit pivots and clear above them. The slides call the full
process Gaussian elimination; we distinguish its Gauss–Jordan continuation.

```{figure} ../figures/lecture2/echelon.svg
:name: fig-w2-echelon
:alt: Highlighted staircase pivots in REF (1,1,3|15), (0,1,1|6), (0,0,-1|-2) become lone unit pivots in RREF with right side (5,4,2).

The same system at two stopping points. Highlighted pivots show what changed.
```

(w2-solutions)=
### Read the complete solution set

| Reduced equations show | Conclusion |
| --- | --- |
| $[0\;\cdots\;0\mid c]$, $c\ne0$ | No solution: it requires $0=c$ |
| No contradiction; pivot in every variable column | Unique solution |
| No contradiction; a variable column without a pivot | Infinitely many solutions: use free real parameters |

A zero row $[0\;\cdots\;0\mid0]$ only says $0=0$. A pivot in the constant
column signals inconsistency, not a new variable.

:::::{admonition} Worked example 2.7 · A free variable gives a family
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read the reduced equations</span>

From
$\left[\begin{array}{ccc|c}1&2&0&3\\0&0&1&4\\0&0&0&0\end{array}\right]$,
read $x+2y=3$, $z=4$. Column 2 has no pivot, so $y$ is free.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Parameterize and verify every solution</span>

Let $y=t\in\mathbb R$. Then

$$\mathbf x=\begin{bmatrix}3-2t\\t\\4\end{bmatrix}
=\begin{bmatrix}3\\0\\4\end{bmatrix}+t\begin{bmatrix}-2\\1\\0\end{bmatrix}.$$

Check: $(3-2t)+2t=3$, and $z=4$. Conversely, the equations force this form once
$y$ is chosen. One convenient vector would not describe the whole solution set.
::::
:::::

:::{admonition} Pitfall · A zero pivot candidate is not “no solution”
:class: pitfall

Swap in a lower row with a nonzero entry; otherwise skip the column. A contradiction
in the **reduced equations**, not a zero candidate or a zero row, proves inconsistency.
:::

:::::{admonition} Worked example 2.8 · Shadows: one point, many points, or no point
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Write the matched-view equations</span>

With calibrated parallel-ray front $(X,Y)$ and side $(Y,Z)$ views,
fixed axes, one origin and matched labeled points,

$$H\mathbf p=\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix}
\begin{bmatrix}X\\Y\\Z\end{bmatrix}=\begin{bmatrix}X\\Y\\Y\\Z\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test agreement and remaining freedom</span>

Front $(2,3)$ and side $(3,4)$ give $(2,3,4)$. Subtract the Y rows to
get $0=0$ and move that row last: every coordinate still has a pivot, so the
point is unique. Front alone leaves $(2,3,t)$; front $(2,2)$ with side $(4,4)$
gives $Y=2$ and $Y=4$, hence $0=2$ and no exact solution.
::::
:::::

```{figure} ../figures/lecture2/matched-views.svg
:name: fig-w2-views
:alt: Point (2,3,4) gives front (2,3), side (3,4), and stacked readings (2,3,3,4); Y repeats and front alone leaves depth free.

Row operations rewrite constraints; they do not move the point or add information.
```

:::{admonition} ML connection · Exact fitting
:class: connection

A linear model also asks whether predictions $A\mathbf x$ match every target.
Conflicting measurements can prevent an exact match; least squares later chooses
an approximation. Averaging here would answer a different question. The shadows
model concerns labeled points, not arbitrary solids reconstructed from silhouettes.
:::

:::{admonition} Check your understanding
:class: checkpoint

Can four equations in three unknowns have a unique solution and a zero row?
:::

:::{dropdown} Check your reasoning

Yes: the stacked shadow views have a repeated Y equation, but all three coordinate columns still have pivots.
:::

::::{div} section-recap

**Keep this:** Check consistency first, then pivots. Verify in the original system.

**Practice:** {ref}`7 <w2-p07>` · {ref}`8 <w2-p08>` · {ref}`12 <w2-p12>` · {ref}`14 <w2-p14>` · {ref}`15 <w2-p15>` · {ref}`16 <w2-p16>` · {ref}`17 <w2-p17>` · {ref}`18 <w2-p18>`.
::::

**Next in the lecture:** {ref}`Page 2 · Determinants and geometry <w2-elimination-page>`.

(w2-practice)=
(w2-solution-page)=

(w2-practice-systems)=
## Practice · systems and elimination

Try each problem before opening its explained answer directly below. Problem numbers
remain stable across the chapter; the questions here follow this page’s topics.

```{include} practice.md
:start-after: <!-- systems:start -->
:end-before: <!-- systems:end -->
```

**Next:** [Page 2 · Determinants and geometry](elimination.md).
