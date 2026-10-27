(lecture-two)=
# Lecture 2 · Systems of linear equations

<div class="chapter-kicker">Can the measurements determine the point?</div>

A front shadow tells us where a marked point sits horizontally and vertically,
but hides its depth. A matched side view supplies another constraint. Recovering
the coordinates means finding values that satisfy **every measurement at once**.
That is the central task of a system of linear equations.

We retain Lecture 1's ideal parallel-ray views, fixed calibrated axes and common
origin. Front coordinates are $(X,Y)$; side coordinates are $(Y,Z)$. Points are
labeled so their views can be matched. No optics background is needed.

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Systems & modelling</span></a>
<a href="elimination.html"><span class="path-number">02</span><span>Elimination & echelon forms</span></a>
<a href="practice.html"><span class="path-number">03</span><span>Exercises</span></a>
<a href="solutions.html"><span class="path-number">04</span><span>Solutions</span></a>
</nav>

## Before you begin

Review {ref}`matrix-vector multiplication <w1-products>` and linear
combinations from Lecture 1. You need signed arithmetic, fractions, substitution,
and the ability to keep variables in a fixed order.

:::{admonition} What you will understand
:class: key-result

1. Read $A\mathbf x=\mathbf b$ as equations, row dot products, and a combination of columns.
2. Build an augmented matrix with correct signs, zeros, and dimensions.
3. Choose legal row operations and explain why they preserve all solutions.
4. Set up a reliable workflow for elimination and checking.
:::

::::{div} page-roadmap

**On this page**

- {ref}`2.1 · Matrix-vector multiplication <w2-products>`
- {ref}`2.2 · Three pictures of a system <w2-pictures>`
- {ref}`2.3 · Augmented matrices and row operations <w2-row-operations>`
- {ref}`2.4 · A plan for solving systems <w2-workflow>`
::::

(w2-products)=
## 2.1 Matrix-vector multiplication: predict or recover?

::::{div} section-intro

**Learning goal:** Compute a product by rows and interpret the same product by columns.

<span class="source-label">Lecture pages 3–5; shadow construction added</span>

If the point is known, what readings should its views produce?
::::


### One product, two readings of the algebra

:::{admonition} Definition 2.1 · Matrix equation
:class: definition

For $A\in\mathbb R^{m\times n}$, an unknown $\mathbf x\in\mathbb R^n$ and
specified $\mathbf b\in\mathbb R^m$, a linear system can be written

$$A\mathbf x=\mathbf b,\qquad
(A\mathbf x)_i=\sum_{j=1}^n a_{ij}x_j.$$

A **solution** is a vector that makes all $m$ equations true simultaneously.
:::

The product has $m$ entries: each row takes a dot product with the **same** input.
Alternatively, if $\mathbf a_j$ is column $j$,

$$A\mathbf x=x_1\mathbf a_1+\cdots+x_n\mathbf a_n.$$

Multiplication asks for the output when the weights are known. Solving asks which
weights produce a specified output. It may have one answer, many, or none.

:::{admonition} Worked example 2.1 · The lecture's difference matrix
:class: example

The columns $\mathbf u=(1,-1,0)^T$, $\mathbf v=(0,1,-1)^T$ and
$\mathbf w=(0,0,1)^T$ form

$$L=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix},\qquad
L\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=\begin{bmatrix}x_1\\x_2-x_1\\x_3-x_2\end{bmatrix}.$$

1. **By rows:** take three dot products with $(x_1,x_2,x_3)^T$.
2. **By columns:** $L\mathbf x=x_1\mathbf u+x_2\mathbf v+x_3\mathbf w$.
3. **Predict:** $L(2,5,9)^T=(2,3,4)^T$.
4. **Recover:** if the output is $(2,3,4)^T$, then $x_1=2$, $x_2=2+3=5$,
   $x_3=5+4=9$. Substitution reproduces the readings.
:::

For our point scene, stack the front and side measurements:

$$H\mathbf p=\mathbf b,\qquad
\underbrace{\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix}}_{H\;\text{is }4\times3}
\underbrace{\begin{bmatrix}X\\Y\\Z\end{bmatrix}}_{\mathbf p\in\mathbb R^3}
=\underbrace{\begin{bmatrix}X\\Y\\Y\\Z\end{bmatrix}}_{\mathbf b\in\mathbb R^4}.$$

The second and third readings measure the same coordinate. Four entries in the
output do not automatically mean four different pieces of information.

```{figure} ../figures/lecture2/matched-views.svg
:name: fig-w2-views
:alt: A world point (2,3,4) gives front readings (2,3) and side readings (3,4). Stacking gives (2,3,3,4); the two Y entries repeat the same constraint. A front view alone leaves Z arbitrary.

Recover coordinates from matched readings. Repeating Y checks agreement; the
side view's Z reading supplies what the front view omitted.
```


:::{admonition} Check your understanding
:class: checkpoint

For $H$ above, compute $H(2,3,9)^T$. Which reading changes from $H(2,3,4)^T$?
:::

:::{dropdown} Check your reasoning

$(2,3,3,9)^T$. Only the fourth entry changes. Both front readings stay fixed; the side view reveals the changed depth.
:::

::::{div} section-recap

**Keep this:** Rows calculate readings; columns describe the contributions of unknown coordinates.

**Try it yourself:** {ref}`Problem 1 <w2-p01>` · {ref}`Problem 2 <w2-p02>`.
::::

(w2-pictures)=
## 2.2 Three pictures of the same system

::::{div} section-intro

**Learning goal:** Translate among scalar equations, geometry, and a column combination.

<span class="source-label">Lecture pages 4–5</span>

What does it mean for a point to satisfy two constraints at once?
::::


A linear equation uses a sum of constant coefficients times unknowns; products
such as $xy$, powers such as $x^2$, and $\sin x$ do not fit that form. Constants
belong on the right. Missing variables have coefficient zero.

:::{admonition} Worked example 2.2 · Two lines, one solution
:class: example

The lecture gives

$$x-2y=1,\qquad 3x+2y=11.$$

**Row picture:** each equation describes a line in the $(x,y)$ plane. A solution
must lie on both, so it is an intersection point.

**Column picture:** find weights that produce the target:

$$x\begin{bmatrix}1\\3\end{bmatrix}
+y\begin{bmatrix}-2\\2\end{bmatrix}=\begin{bmatrix}1\\11\end{bmatrix}.$$

**Matrix picture:**
$\begin{bmatrix}1&-2\\3&2\end{bmatrix}(x,y)^T=(1,11)^T$.

Adding the two original equations gives $4x=12$, hence $x=3$. The first equation
then gives $y=1$. Check both: $3-2=1$ and $9+2=11$. In the column picture,
$3(1,3)^T+(-2,2)^T=(1,11)^T$.
:::

```{figure} ../figures/lecture2/three-pictures.svg
:name: fig-w2-pictures
:alt: Lines y=(x-1)/2 and y=(11-3x)/2 intersect at (3,1). Beside them the column equation states that three copies of (1,3) plus one copy of (-2,2) give (1,11).

The intersection coordinates are the column weights. The target vector $(1,11)$
belongs to the output space; it is not the intersection point $(3,1)$.
```

### The lecture's three-dimensional example

The same translation works for

$$\begin{aligned}
x+2y+3z&=6,\\2x+5y+2z&=4,\\6x-3y+z&=2.
\end{aligned}$$

Its coefficient matrix and column picture are

$$A=\begin{bmatrix}1&2&3\\2&5&2\\6&-3&1\end{bmatrix},\quad
x\begin{bmatrix}1\\2\\6\end{bmatrix}
+y\begin{bmatrix}2\\5\\-3\end{bmatrix}
+z\begin{bmatrix}3\\2\\1\end{bmatrix}=\begin{bmatrix}6\\4\\2\end{bmatrix}.$$

Each nontrivial row equation describes a plane in unknown-coordinate space.
Here the three planes meet at $(0,0,2)$: substituting gives $6,4,2$.
In the column picture, twice the third column gives the target. We will verify
uniqueness by elimination in the exercises; a successful substitution alone
proves that a solution exists, not that it is the only one.

:::{admonition} Common pitfall · Count constraints, then test their information
:class: pitfall

Three equations in three unknowns need not meet at exactly one point. Equations
can repeat or contradict each other. Likewise, a rectangular system can have a
unique solution. Elimination determines which case actually occurs.
:::


:::{admonition} Check your understanding
:class: checkpoint

What are the row and column pictures of $x+y=2$, $2x+2y=4$?
:::

:::{dropdown} Check your reasoning

The second equation describes the same line as the first, so every point $(2-t,t)$ works. The columns are both $(1,2)^T$; their weights need only sum to 2.
:::

::::{div} section-recap

**Keep this:** The three pictures express one requirement: the same unknowns must satisfy every row.

**Try it yourself:** {ref}`Problem 3 <w2-p03>` · {ref}`Problem 4 <w2-p04>`.
::::

(w2-row-operations)=
## 2.3 Augmented matrices and legal row operations

::::{div} section-intro

**Learning goal:** Encode a system and transform it without changing its solution set.

<span class="source-label">Lecture pages 6–7</span>

Can we simplify equations while keeping exactly the same possible points?
::::


### Keep the constants attached

The **augmented matrix** $[A\mid\mathbf b]$ stores the coefficients and the right
side together. Fix the variable order first. For the lecture's main example,

$$\begin{aligned}x+y+3z&=15,\\x+2y+4z&=21,\\x+y+2z&=13\end{aligned}
\quad\longleftrightarrow\quad
\left[\begin{array}{ccc|c}1&1&3&15\\1&2&4&21\\1&1&2&13\end{array}\right].$$

The vertical bar separates constants from coefficients; it is not multiplication.
With three unknowns the augmented matrix has four columns. Its last column is
**not** a fourth unknown.

:::{admonition} Key result 2.1 · Elementary row operations
:class: key-result

| Operation | Notation | Condition |
| --- | --- | --- |
| Exchange two rows | $R_i\leftrightarrow R_j$ | Distinct rows |
| Scale a row | $R_i\leftarrow cR_i$ | $c\ne0$ |
| Add a multiple of another row | $R_i\leftarrow R_i+cR_j$ | $i\ne j$; retain row $j$ |

Apply the operation to the **entire augmented row**, including its constant.
The resulting system is row-equivalent: it has exactly the same solutions.
:::

:::{admonition} Proof · Why the solutions survive
:class: proof

Reordering equations changes no requirements. Multiplying an equality by a
nonzero number preserves it and can be undone by dividing. Adding $c$ times
another equality preserves every solution; subtracting that same multiple
recovers the old row because the source row was retained. Thus each operation
works in both directions. Scaling by zero fails this argument: it erases an equation.
:::

:::{admonition} Worked example 2.3 · Eliminate a repeated X coefficient
:class: example

Start with the augmented matrix above. Perform $R_2\leftarrow R_2-R_1$:

$$[1,2,4\mid21]-[1,1,3\mid15]=[0,1,1\mid6].$$

The new second equation is $y+z=6$; rows 1 and 3 stay unchanged. Any solution of
the originals satisfies this difference. Conversely, add row 1 back to recover
$x+2y+4z=21$. The operation simplified the equation without losing it.
:::

:::{admonition} Connection · Simplifying readings does not move the point
:class: connection

Subtracting the two Y equations in $H\mathbf p=\mathbf b$ tests whether their
readings agree. It does not move the point, rotate a screen, or create a new
independent measurement. We are rewriting the constraints on a fixed unknown.
:::


:::{admonition} Check your understanding
:class: checkpoint

Is $R_2\leftarrow R_2-2R_1$ legal? Is $R_2\leftarrow0R_2$ legal? Must the constants change?
:::

:::{dropdown} Check your reasoning

The first is legal for distinct rows and updates every entry, including the constant. The second is not an elementary row operation because it cannot be reversed and can discard a constraint.
:::

::::{div} section-recap

**Keep this:** Preserve equations by reversible operations on whole augmented rows.

**Try it yourself:** {ref}`Problem 5 <w2-p05>` · {ref}`Problem 6 <w2-p06>`.
::::

(w2-workflow)=
## 2.4 A reliable plan for solving systems

::::{div} section-intro

**Learning goal:** Choose, execute, interpret, and check a solution method.

<span class="source-label">Lecture pages 6–8; shadow examples added</span>

How can you avoid reaching a neat matrix but giving an incomplete answer?
::::


### Use this sequence on an exam

1. **Model.** Choose the variable order, collect constants on the right, and write
   $[A\mid\mathbf b]$. Insert zeros for missing variables.
2. **Choose a pivot.** A pivot is the leading nonzero entry of a nonzero row in
   echelon form. While reducing, select a nonzero entry in the next available
   column; swap rows if necessary. Never divide by zero.
3. **Eliminate below.** Subtract suitable multiples of the pivot row from rows
   below. Move right and down, skipping columns with no remaining candidate.
4. **Interpret.** Identify contradictions, pivot variables and free variables.
   {ref}`The next page <w2-ref>` defines the precise stopping forms.
5. **Finish.** Back substitute from an echelon system, or continue to RREF if
   requested. State one vector, a parameterized family, or no solution.
6. **Verify.** Substitute into the **original** equations. A family must satisfy
   them for every parameter value, and you must account for all possibilities.

:::{admonition} Worked example 2.4 · Recover a point from two views
:class: example

**Given:** front mark $(2,3)$ and matched side mark $(3,4)$.

1. With unknowns $(X,Y,Z)$, augment $H$:

   $$\left[\begin{array}{ccc|c}1&0&0&2\\0&1&0&3\\0&1&0&3\\0&0&1&4\end{array}\right].$$

2. Replace $R_3\leftarrow R_3-R_2$, giving $[0,0,0\mid0]$ in row 3.
3. Swap rows 3 and 4 to put the zero row last. Read $X=2,Y=3,Z=4$.
4. **Check:** $H(2,3,4)^T=(2,3,3,4)^T$, exactly the given readings.

There are four equations and only three unknowns, yet the system is consistent
and unique. The zero row says one equation was redundant, not that a variable is free.
:::

### What changes with fewer or incompatible readings?

The front view alone gives $X=2,Y=3$ and leaves $Z$ arbitrary:
$\mathbf p=(2,3,t)^T$, $t\in\mathbb R$. Every member has the same front mark.

If instead the front mark is $(2,2)$ and the side mark is $(4,4)$, the two
Y equations require both $Y=2$ and $Y=4$. Subtracting yields $0=2$.
There is **no exact solution**. Averaging these readings answers a different,
approximate-fitting question, which belongs to least squares later in the course.


:::{admonition} Check your understanding
:class: checkpoint

Why should you not stop after checking just the first two equations of $H\mathbf p=\mathbf b$?
:::

:::{dropdown} Check your reasoning

They test only the front view. A candidate can have the wrong depth or fail the side Y reading. A system requires every equation simultaneously.
:::

::::{div} section-recap

**Keep this:** Set up, reduce, classify, finish, and check against the original problem.

**Try it yourself:** {ref}`Problem 7 <w2-p07>` · {ref}`Problem 8 <w2-p08>`.
::::

Continue to {ref}`elimination and echelon forms <w2-elimination-page>` for the complete reduction algorithm.
