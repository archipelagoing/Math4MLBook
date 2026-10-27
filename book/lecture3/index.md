(lecture-three)=
# Spaces and subspaces

<div class="chapter-kicker">Lecture 3 · Page 1 of 4 · Which records are possible?</div>

Lecture 2 solved equations. Lecture 3 explains the **sets behind those answers**:
which outputs a matrix can produce, which inputs it hides, and how many independent
directions remain. We follow all 35 PDF pages, including the handwritten examples.

<nav class="lecture-path" aria-label="Lecture 3 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Spaces & subspaces</span></a>
<a href="solutions-rank.html"><span class="path-number">02</span><span>Complete solutions & rank</span></a>
<a href="basis.html"><span class="path-number">03</span><span>Independence, span & basis</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Use {ref}`linear combinations <w1-combinations>` and
{ref}`Gaussian elimination and solution cases <w2-gaussian>`. You need to interpret
$A\mathbf x=\mathbf b$, identify pivots, and use free parameters. This page introduces
the spaces; the next counts their independent directions using rank.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`A · Vector spaces <w3-vector-spaces>`
- {ref}`B · Subspaces <w3-subspaces>`
- {ref}`C · Column space <w3-column-space>`
- {ref}`D · Null space <w3-null-space>`
- {ref}`E · Four fundamental subspaces <w3-four-spaces>`
::::

(w3-vector-spaces)=
## A · Vector spaces

::::{div} section-intro

**Learning goal:** Distinguish the whole coordinate space from a set that fails closure.

<span class="source-label">Lecture PDF pages 1–6</span>
::::

The lecture's $\mathbb R^2$ contains all real pairs, such as $(3,2)^T$ and $(0,0)^T$;
$\mathbb R^3$ contains all real triples, such as $(1,2,3)^T$ and $(0,0,0)^T$.
Adding compatible vectors or scaling by **any real number** keeps us in the same space.

:::{admonition} Definition · Real vector space
:class: definition

A real vector space has vector addition and real scalar multiplication satisfying
the usual algebraic rules: commutative/associative addition, a zero vector and
additive inverses, distributivity over vector/scalar sums, associative scaling,
and $1\mathbf v=\mathbf v$. It is closed under both operations.

For subsets of $\mathbb R^n$ with the usual operations, the algebraic rules are
inherited. The main issue is whether the subset retains zero and stays closed.
:::

A physical screen may have edges, but the coordinate space $\mathbb R^2$ does not.
Do not carry apparatus boundaries into its algebra.

:::::{admonition} Worked example 3.1 · Why the lecture's shaded region fails
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Choose a vector in the region</span>

The first-quadrant region in slides 5–6 contains $(1,1)^T$.
It may contain zero and be closed under addition, but that is not enough.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Test a negative scalar</span>

Multiplying by $-1$ gives $(-1,-1)^T$, outside the region.
Thus it is not closed under all real scalar multiplication. The lecture's
$\mathbf v,-\mathbf v$ arrows show precisely this failure.
::::

::::{div} key-answer

**Keep this result:** A bounded or quadrant-shaped region is not all of $\mathbb R^2$; closure must hold for every real scalar.
::::
:::::

```{figure} ../figures/lecture3/subspace-test.svg
:name: fig-w3-subspaces
:alt: A line through zero contains a vector and its negative. A first-quadrant region contains (1,1) but excludes (-1,-1), so negative scaling leaves it.

Test the operations, not the shading. A line through zero passes; the quadrant fails.
```

:::{admonition} Check your understanding
:class: checkpoint

Does containing the zero vector alone make a set a vector space?
:::

:::{dropdown} Check your reasoning

No. The first quadrant contains zero but fails closure under multiplication by −1.
:::

::::{div} section-recap

**Keep this:** A vector space supports all vector sums and all real scalar multiples.

**Practice:** {ref}`1 <w3-p01>` · {ref}`2 <w3-p02>`.
::::

(w3-subspaces)=
## B · Subspaces

::::{div} section-intro

**Learning goal:** Apply the zero and closure tests and recognize lines through zero.

<span class="source-label">Lecture PDF pages 7–8</span>
::::

:::{admonition} Definition · Subspace test
:class: definition

A subset $V$ of a real vector space is a **subspace** when it contains zero and
is closed under addition and scalar multiplication. Equivalently, for all
$\mathbf v,\mathbf w\in V$ and $\lambda,\mu\in\mathbb R$,

$$\lambda\mathbf v+\mu\mathbf w\in V,$$

with nonemptiness/zero included. Use arbitrary vectors to prove closure; one
counterexample disproves it.
:::

In $\mathbb R^2$, the complete list is: the zero subspace $\{\mathbf0\}$,
any line through the origin, and the whole plane. A translated line generally
fails the zero test. In $\mathbb R^3$, planes through the origin are possible too.

:::::{admonition} Worked example 3.2 · Prove a line is a subspace
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Check zero</span>

For $V=\{(t,2t)^T:t\in\mathbb R\}$, take $t=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check a general combination</span>

For $(s,2s)^T,(t,2t)^T\in V$,
$\lambda(s,2s)^T+\mu(t,2t)^T=(\lambda s+\mu t,2(\lambda s+\mu t))^T$,
which still has the required form. In contrast, $x+y=1$ excludes zero.
::::

::::{div} key-answer

**Keep this result:** One formula proves closure for every pair and every real coefficient; testing a few points cannot do that.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

Is $V=\{(x,y):y=x^2\}$ a subspace?
:::

:::{dropdown} Check your reasoning

No. It contains (1,1), but twice that vector is (2,2), which fails y=x².
:::

::::{div} section-recap

**Keep this:** Prove with arbitrary combinations; disprove with one failed requirement.

**Practice:** {ref}`2 <w3-p02>` · {ref}`3 <w3-p03>`.
::::

(w3-column-space)=
## C · Column space

::::{div} section-intro

**Learning goal:** Interpret solvability as membership in the set of possible outputs.

<span class="source-label">Lecture PDF pages 9–10</span>
::::

:::{admonition} Definition · Column space
:class: definition

For $A=[\mathbf a_1\ \cdots\ \mathbf a_n]\in\mathbb R^{m\times n}$,

$$C(A)=\{A\mathbf x:\mathbf x\in\mathbb R^n\}
=\operatorname{span}\{\mathbf a_1,\ldots,\mathbf a_n\}\subseteq\mathbb R^m.$$

Here **span** means every linear combination; Part I develops it further.
The system $A\mathbf x=\mathbf b$ is solvable **if and only if** $\mathbf b\in C(A)$.
:::

The column space is a subspace: $A\mathbf0=\mathbf0$ and
$\lambda A\mathbf x+\mu A\mathbf y=A(\lambda\mathbf x+\mu\mathbf y)$.
It describes achievable **outputs**, not all possible inputs.

:::::{admonition} Worked example 3.3 · The lecture's column-space plane (p. 10)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read the columns and weights</span>

For $P=\begin{bmatrix}1&0\\4&3\\2&3\end{bmatrix}$,
$\mathbf b=0.4(1,4,2)^T+0.3(0,3,3)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Compute and check the output</span>

$P(0.4,0.3)^T=(0.4,2.5,1.7)^T=\mathbf b$.
Thus $\mathbf b\in C(P)$. The two nonparallel columns generate a plane through
zero in $\mathbb R^3$, not all of $\mathbb R^3$. The lecturer's plane drawing
illustrates this family of outputs.
::::

::::{div} key-answer

**Keep this result:** The weights are an input in $\mathbb R^2$; the attainable vector is an output in $\mathbb R^3$.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

If a 3×2 matrix has a two-dimensional column space, can every vector in $\mathbb R^3$ be an output?
:::

:::{dropdown} Check your reasoning

No. Its output plane leaves vectors outside that plane unattainable.
:::

::::{div} section-recap

**Keep this:** To test whether an output is attainable, solve the coefficient equations.

**Practice:** {ref}`4 <w3-p04>` · {ref}`8 <w3-p08>`.
::::

(w3-null-space)=
## D · Null space

::::{div} section-intro

**Learning goal:** Compute invisible input directions by solving a homogeneous system.

<span class="source-label">Lecture PDF pages 11–12</span>
::::

:::{admonition} Definition · Null space
:class: definition

$$N(A)=\{\mathbf x\in\mathbb R^n:A\mathbf x=\mathbf0\}\subseteq\mathbb R^n.$$

These are **inputs** invisible to the map. It is a subspace because
$A(\lambda\mathbf x+\mu\mathbf y)=\lambda A\mathbf x+\mu A\mathbf y=0$
for null vectors. The zero input is always included.
:::

:::::{admonition} Worked example 3.4 · The lecture's null-space calculation (p. 12)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Reduce the homogeneous equations</span>

Let $A=\begin{bmatrix}1&1&2\\2&1&3\\3&1&4\end{bmatrix}$.
Apply $R_2\leftarrow R_2-2R_1$ and $R_3\leftarrow R_3-3R_1$:

$$\begin{bmatrix}1&1&2\\0&-1&-1\\0&-2&-2\end{bmatrix}.$$

Then negate row 2, use $R_3\leftarrow R_3+2R_2$, and
$R_1\leftarrow R_1-R_2$, with the **updated** row 2:

$$R=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Choose the free variable and solve</span>

Read $x_1+x_3=0$, $x_2+x_3=0$. Set $x_3=t$:
$\mathbf x=t(-1,-1,1)^T$. The lecture's **special solution** sets the free
variable to 1, giving $\mathbf s=(-1,-1,1)^T$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Verify in the original matrix</span>

$A\mathbf s=(-1-1+2,-2-1+3,-3-1+4)^T=\mathbf0$.
Conversely, every homogeneous solution has this form, so
$N(A)=\operatorname{span}\{\mathbf s\}$.
::::

::::{div} key-answer

**Keep this result:** A free variable describes a whole invisible direction, not just one extra answer.
::::
:::::

The slide annotation asks about relaxing constraints: removing an **independent**
equation can enlarge the null space. Removing a redundant equation may change
nothing. Adding matched independent shadow measurements can instead remove freedom.

:::{admonition} Check your understanding
:class: checkpoint

For the front-view matrix $O$, which inputs are invisible?
:::

:::{dropdown} Check your reasoning

All $(0,0,t)^T$, since the front view keeps X,Y and omits Z. Thus $N(O)=\operatorname{span}\{(0,0,1)^T\}$.
:::

::::{div} section-recap

**Keep this:** Column space lives in the output space; null space lives in the input space.

**Practice:** {ref}`5 <w3-p05>` · {ref}`6 <w3-p06>` · {ref}`8 <w3-p08>`.
::::

(w3-four-spaces)=
## E · Four fundamental subspaces

::::{div} section-intro

**Learning goal:** Identify the four spaces and construct generators without mixing ambient dimensions.

<span class="source-label">Lecture PDF pages 13</span>
::::

For $A\in\mathbb R^{m\times n}$, keep **two input-space subspaces** and
**two output-space subspaces** separate:

| Name | Definition | Lives in |
| --- | --- | --- |
| Column space $C(A)$ | All $A\mathbf x$ | $\mathbb R^m$ |
| Null space $N(A)$ | Solutions of $A\mathbf x=0$ | $\mathbb R^n$ |
| Row space $C(A^T)$ | Combinations of rows, viewed as coordinate vectors | $\mathbb R^n$ |
| Left null space $N(A^T)$ | Solutions of $A^T\mathbf y=0$ | $\mathbb R^m$ |

A set is a **subset** of its ambient space, not an element of that space.
A generating set with no redundancy will be called a **basis** in Part J.

:::::{admonition} Worked example 3.5 · Generate all four spaces of the same matrix
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Use pivots correctly</span>

For Example 3.4's $A$, pivot columns are 1 and 2.
Use columns **of the original $A$** for $C(A)$, but the nonzero RREF rows for
$C(A^T)$:

$$C(A)=\operatorname{span}\{(1,2,3)^T,(1,1,1)^T\},$$
$$C(A^T)=\operatorname{span}\{(1,0,1)^T,(0,1,1)^T\}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve the two homogeneous problems</span>

We already found $N(A)=\operatorname{span}\{(-1,-1,1)^T\}$.
For $A^T\mathbf y=0$, its equations include
$y_1+2y_2+3y_3=0$ and $y_1+y_2+y_3=0$.
Subtracting gives $y_2=-2y_3$, then $y_1=y_3$. Therefore
$N(A^T)=\operatorname{span}\{(1,-2,1)^T\}$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Interpret the left-null constraint</span>

Any attainable right side must satisfy
$(1,-2,1)^T\mathbf b=b_1-2b_2+b_3=0$.
Both original pivot columns obey it, so every combination does too. Conversely,
when this holds, choose $x_3=0$, $x_1=b_2-b_1$, $x_2=2b_1-b_2$; all three rows
then match. Thus this condition describes $C(A)$ exactly.
::::

::::{div} key-answer

**Keep this result:** RREF preserves the row space and null space, but generally changes the column space.
::::
:::::

```{figure} ../figures/lecture3/four-spaces.svg
:name: fig-w3-four-spaces
:alt: Front view O maps R3 to R2, with hidden Z inputs and every screen pair attainable. Stacked H maps R3 to R4, with no invisible input and outputs constrained by equal Y readings. Row/null spaces share the input ambient space; column/left-null spaces share the output ambient space.

The familiar views give concrete meanings to all four spaces. Counts are formalized
as rank and dimension on the next pages.
```

For stacked $H$, $N(H)=\{0\}$, $C(H)=\{\mathbf b:b_2=b_3\}$,
$C(H^T)=\mathbb R^3$, and $N(H^T)=\operatorname{span}\{(0,1,-1,0)^T\}$.
Repeating Y creates an output agreement condition, not an invisible input motion.
Next lecture connects these pairs through orthogonality; here, their definitions
and the explicit equations are sufficient.

:::{admonition} Check your understanding
:class: checkpoint

For a 3×5 matrix, how many entries does a left-null vector have? A null vector?
:::

:::{dropdown} Check your reasoning

A left-null vector has 3 entries because $A^T\mathbf y$ requires $\mathbf y\in\mathbb R^3$. A null vector has 5 entries.
:::

::::{div} section-recap

**Keep this:** Use original pivot columns, nonzero reduced rows, and two homogeneous solves.

**Practice:** {ref}`7 <w3-p07>` · {ref}`8 <w3-p08>`.
::::

(w3-practice-spaces)=
## Practice · spaces and subspaces

Try without the hint first. The explained answer is expandable directly below
each question; follow its review link before retrying a missed method.

```{include} practice.md
:start-after: <!-- spaces:start -->
:end-before: <!-- spaces:end -->
```

**Next:** [Page 2 · Complete solutions and rank](solutions-rank.md).
