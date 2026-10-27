(w3-basis-page)=
# Independence, span, and basis

<div class="chapter-kicker">Lecture 3 · Page 3 of 4 · Keep the necessary directions</div>

Rank counted pivots. The final lecture topics explain what those pivots mean:
independent ingredients, the space they span, a basis without redundancy, and
coordinates relative to that basis.

<nav class="lecture-path" aria-label="Lecture 3 learning path">
<a href="index.html"><span class="path-number">01</span><span>Spaces & subspaces</span></a>
<a href="solutions-rank.html"><span class="path-number">02</span><span>Complete solutions & rank</span></a>
<a href="basis.html" aria-current="page"><span class="path-number">03</span><span>Independence, span & basis</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Use {ref}`rank and pivot columns <w3-rank>`. We keep the source order:
independence → span → basis/dimension → change of basis. A basis is ordered
whenever we use it to assign a coordinate list.

::::{div} page-roadmap

**Follow the lecture**

- {ref}`H · Linear independence <w3-independence>`
- {ref}`I · Span <w3-span>`
- {ref}`J · Basis and dimension <w3-basis-dimension>`
- {ref}`K · Change of basis <w3-change-basis>`
::::

(w3-independence)=
## H · Linear independence

::::{div} section-intro

**Learning goal:** Test the zero combination and distinguish pairwise nonparallel from independent.

<span class="source-label">Lecture PDF pages 22–26</span>
::::

:::{admonition} Definition · Linear independence
:class: definition

$\mathbf v_1,\ldots,\mathbf v_k$ are **linearly independent** if

$$c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf0
\quad\Rightarrow\quad c_1=\cdots=c_k=0.$$

Otherwise they are dependent: some **not-all-zero coefficients** produce zero.
For $V=[\mathbf v_1\ \cdots\ \mathbf v_k]$, solve $V\mathbf c=0$.
Independence means $N(V)=\{0\}$, or one pivot for every column.
:::

For nonzero vectors, dependence means an ingredient can be made from the others.
Any set containing the zero vector is dependent. In $\mathbb R^n$, at most $n$
vectors can be independent: there cannot be more than $n$ pivots.

:::::{admonition} Worked example 3.11 · The lecture's three arrow tests (pp. 23–26)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compare directions, not lengths</span>

The first pair in the slides lies on one line, so one arrow is a multiple
of the other: **dependent**. The second pair is nonparallel, so neither is a
multiple of the other: **independent**.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check the ambient dimension</span>

The third picture has three arrows in a plane: **dependent**, even though
no pair need be collinear. For instance, $(1,0)^T,(0,1)^T,(1,1)^T$ obey
$\mathbf v_1+\mathbf v_2-\mathbf v_3=0$.
The separate three-dimensional sketch on p. 23 is independent when its third
vector lies outside the plane spanned by the first two.
::::

::::{div} key-answer

**Keep this result:** Two nonparallel arrows suffice in a plane; a third planar arrow adds redundancy, not dimension.
::::
:::::

```{figure} ../figures/lecture3/independence.svg
:name: fig-w3-independence
:alt: Three labeled planar cases show two collinear arrows (dependent), two nonparallel arrows (independent), and three arrows with the third equal to the sum of the first two (dependent).

Original coordinate examples illustrate the lecture's NO / YES / NO sequence.
```

:::{admonition} Check your understanding
:class: checkpoint

Can three pairwise nonparallel vectors in $\mathbb R^2$ be independent?
:::

:::{dropdown} Check your reasoning

No. Pairwise nonparallel rules out dependence of each pair, but three columns in two rows still cannot have three pivots.
:::

::::{div} section-recap

**Keep this:** Independence is a statement about the whole list and its zero combinations.

**Practice:** {ref}`17 <w3-p17>` · {ref}`18 <w3-p18>` · {ref}`24 <w3-p24>` · {ref}`27 <w3-p27>`.
::::

(w3-span)=
## I · Span

::::{div} section-intro

**Learning goal:** Find the generated space and solve membership equations.

<span class="source-label">Lecture PDF pages 27–29</span>
::::

:::{admonition} Definition · Span
:class: definition

$$\operatorname{span}\{\mathbf v_1,\ldots,\mathbf v_k\}
=\{c_1\mathbf v_1+\cdots+c_k\mathbf v_k:c_i\in\mathbb R\}.$$

This is every output the ingredients can build; it is always a subspace.
To test membership, put the ingredients in columns and solve $V\mathbf c=\mathbf v$.
A spanning list can contain redundant vectors.
:::

:::::{admonition} Worked example 3.12 · All three span cases on p. 28
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Use coordinate directions</span>

$(1,0)^T,(0,1)^T$ span all $\mathbb R^2$, since
$(x,y)^T=x(1,0)^T+y(0,1)^T$. Adding $(5,6)^T$ leaves the span unchanged:
that third vector is already $5\mathbf e_1+6\mathbf e_2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Check for a multiple</span>

$(1,1)^T,(3,3)^T$ span only the line $y=x$, since
$a(1,1)^T+b(3,3)^T=(a+3b)(1,1)^T$. The second vector adds no new direction.
::::

::::{div} key-answer

**Keep this result:** A list can span the whole space without being independent; extra vectors may add nothing.
::::
:::::

:::::{admonition} Worked example 3.13 · The lecture's membership calculation (p. 29)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Write coefficient equations</span>

Let $\mathbf v=(1,2,0)^T$ and
$S=\{(1,1,0)^T,(1,7,0)^T\}$. Solve
$a+b=1$, $a+7b=2$; the third equation is $0=0$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Solve and check</span>

Subtract to get $6b=1$, so $b=1/6$ and $a=5/6$.
Then $(5/6)(1,1,0)^T+(1/6)(1,7,0)^T=(1,2,0)^T$.
::::

::::{div} key-answer

**Keep this result:** $\mathbf v\in\operatorname{span}(S)$, but $\mathbf v\notin S$ itself.
::::
:::::

:::{admonition} Source clarification · A set and its span are different
:class: pitfall

Page 29 writes $\mathbf v\in S$. Its displayed calculation proves membership in
**span(S)**. The vector is neither of the two listed elements of S. Keep that
distinction: belonging to the generated space need not mean being an ingredient.
:::

:::{admonition} Check your understanding
:class: checkpoint

Does adding $2\mathbf v_1$ to a spanning list enlarge its span?
:::

:::{dropdown} Check your reasoning

No. It is already a combination of the existing vector, so it adds no attainable outputs.
:::

::::{div} section-recap

**Keep this:** Span asks what can be produced; independence asks whether the ingredients are redundant.

**Practice:** {ref}`18 <w3-p18>` · {ref}`19 <w3-p19>` · {ref}`20 <w3-p20>` · {ref}`27 <w3-p27>`.
::::

(w3-basis-dimension)=
## J · Basis and dimension

::::{div} section-intro

**Learning goal:** Remove redundancy and count independent coordinates in each space.

<span class="source-label">Lecture PDF pages 30–33</span>
::::

:::{admonition} Definition · Basis and dimension
:class: definition

A **basis** of a space is a list that is both **independent** and **spanning**.
Every vector in the space then has a unique coefficient list.
The **dimension** is the number of vectors in any basis. Different bases have
the same length. The zero space has dimension 0 and the empty basis, not a basis
consisting of the zero vector.
:::

Why uniqueness? Subtract two proposed representations. Independence forces every
coefficient difference to be zero. Spanning guarantees existence; independence
guarantees uniqueness.

:::::{admonition} Worked example 3.14 · Natural and tilted bases (pp. 32–33)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Read the natural basis correctly</span>

The plotted natural basis is $\mathbf e_1=(1,0)^T$,
$\mathbf e_2=(0,1)^T$. Any $(x,y)^T=x\mathbf e_1+y\mathbf e_2$, uniquely.
The diagram and column order matter; text extraction can reverse displayed entries.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Replace it with independent tilted directions</span>

The next slide uses general directions $\mathbf r=(r_1,r_2)^T$ and
$\mathbf s=(s_1,s_2)^T$. They form another basis of $\mathbb R^2$ when they
are nonparallel, equivalently when the square matrix $[\mathbf r\ \mathbf s]$
has two pivots (nonzero determinant). Their grid need not be perpendicular or unit-spaced.
::::

::::{div} key-answer

**Keep this result:** The basis changes the coordinate labels, not which vectors belong to the space.
::::
:::::

### Finding a basis in a computation

| Given | Procedure |
| --- | --- |
| A spanning list | Put vectors in columns, reduce, retain original pivot columns |
| $C(A)$ | Original pivot columns of A |
| $C(A^T)$ | Nonzero rows of REF/RREF |
| $N(A)$ or $N(A^T)$ | Solve the appropriate homogeneous system; use one special vector per free variable |

For $A\in\mathbb R^{m\times n}$ of rank r, the four dimension counts are

$$\boxed{\dim C(A)=\dim C(A^T)=r,\quad\dim N(A)=n-r,\quad\dim N(A^T)=m-r}.$$

Each free coordinate gives an independent special solution; their combinations
produce every homogeneous solution. This proves the **rank–nullity** count
$r+\dim N(A)=n$. Applying it to $A^T$, whose row/column rank is also r, gives
the left-null count. Distinct leading positions make nonzero echelon rows independent.

For Page 1's 3×3 A, the four dimensions are **2, 1, 2, 1** in column/null/row/left-null
order. For H they are **3, 0, 3, 1**. Matching dimensions does not mean equal spaces:
they may even have different ambient dimensions.

:::{admonition} Check your understanding
:class: checkpoint

Are two independent vectors in $\mathbb R^3$ a basis of $\mathbb R^3$?
:::

:::{dropdown} Check your reasoning

No. They form a basis of their two-dimensional span, but do not span all of $\mathbb R^3$.
:::

::::{div} section-recap

**Keep this:** A basis must be independent and span the stated space; name that space.

**Practice:** {ref}`7 <w3-p07>` · {ref}`8 <w3-p08>` · {ref}`20 <w3-p20>` · {ref}`21 <w3-p21>` · {ref}`24 <w3-p24>`.
::::

(w3-change-basis)=
## K · Change of basis

::::{div} section-intro

**Learning goal:** Distinguish the vector from its coordinate list and choose the conversion direction.

<span class="source-label">Lecture PDF pages 34–35</span>
::::

An ordered basis $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ for $\mathbb R^n$
forms the square matrix $B=[\mathbf b_1\ \cdots\ \mathbf b_n]$.

:::{admonition} Change-of-basis directions
:class: key-result

$$\boxed{\mathbf x_E=B[\mathbf x]_{\mathcal B},\qquad
[\mathbf x]_{\mathcal B}=B^{-1}\mathbf x_E}.$$

The columns of B are the **new basis vectors written in the original coordinates**.
Multiplying by B converts new coefficients to original coordinates; its inverse
converts back. For two ordered bases B,C of the same $\mathbb R^n$,
$[\mathbf x]_{\mathcal C}=C^{-1}B[\mathbf x]_{\mathcal B}$.
:::

:::::{admonition} Worked example 3.15 · The lecture's coordinate conversion (p. 34)
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Build the matrix in the declared order</span>

The displayed vectors are $\mathbf b_1=(3,1)^T$, $\mathbf b_2=(1,1)^T$:

$$B=\begin{bmatrix}3&1\\1&1\end{bmatrix},\quad
[\mathbf x]_{\mathcal B}=\begin{bmatrix}3/2\\1/2\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct in the natural coordinates</span>

Multiply columns by their coefficients:

$$\mathbf x_E=\tfrac32\begin{bmatrix}3\\1\end{bmatrix}
+\tfrac12\begin{bmatrix}1\\1\end{bmatrix}
=\begin{bmatrix}9/2+1/2\\3/2+1/2\end{bmatrix}
=\begin{bmatrix}5\\2\end{bmatrix}.$$
::::

::::{div} worked-step

<span class="step-label">Step 3 · Convert back and check</span>

$\det B=2$, so

$$B^{-1}=\tfrac12\begin{bmatrix}1&-1\\-1&3\end{bmatrix},\qquad
B^{-1}\begin{bmatrix}5\\2\end{bmatrix}
=\tfrac12\begin{bmatrix}3\\1\end{bmatrix}
=\begin{bmatrix}3/2\\1/2\end{bmatrix}.$$

The round trip restores the original coefficients. Swapping the basis columns
without swapping their coefficients would change the represented vector.
::::

::::{div} key-answer

**Keep this result:** $(5,2)^T$ and $(3/2,1/2)^T$ describe the same vector in different ordered bases.
::::
:::::

```{figure} ../figures/lecture3/basis-coordinates.svg
:name: fig-w3-basis
:alt: On fixed X,Y screen axes, b1=(3,1) and b2=(1,1). One and a half b1 plus one half b2 reaches x=(5,2); the partial endpoint (4.5,1.5) is shown before adding (0.5,0.5).

A fixed front-screen mark has different coefficient labels in a tilted basis.
The point does not move. These basis vectors are not orthonormal, so coefficient
lengths/angles cannot be treated as physical screen lengths/angles.
```

For a basis of a proper subspace, its column matrix may be rectangular.
Solve $B\mathbf c=\mathbf x$ for the unique coefficients of a vector **in that
subspace**; do not invent a square inverse for a rectangular matrix.

:::{admonition} ML connection · Describe the same information with fewer coordinates
:class: connection

Independent feature columns provide a nonredundant description of their span.
A basis represents reachable records uniquely; null-space directions explain
why redundant input coefficients may not be identifiable. Changing a basis
relabels retained information. It does not restore a coordinate discarded by a view.
:::

:::{admonition} Check your understanding
:class: checkpoint

If B contains new basis vectors in old coordinates, which operation recovers the new coefficients from an old coordinate vector?
:::

:::{dropdown} Check your reasoning

Solve $B\mathbf c=\mathbf x_E$, or multiply by $B^{-1}$ when B is a square basis matrix. Multiplying by B goes in the other direction.
:::

::::{div} section-recap

**Keep this:** Columns define the basis; coefficients describe the vector in that ordered basis.

**Practice:** {ref}`22 <w3-p22>` · {ref}`23 <w3-p23>` · {ref}`24 <w3-p24>` · {ref}`28 <w3-p28>`.
::::

(w3-practice-basis)=
## Practice · independence, span, basis, and coordinates

Try without the hint first. The explained answer is expandable directly below
each question; follow its review link before retrying a missed method.

```{include} practice.md
:start-after: <!-- basis:start -->
:end-before: <!-- basis:end -->
```

(w3-readiness)=
## Mixed readiness check · Try before opening any answers

**Suggested practice time: 20 minutes.** This is an editorial rehearsal, not an
official exam duration or grading cutoff. Four unseen tasks carry **4 practice
points each**. No method hints are supplied. Show reasoning and an independent check.

- Problem 25: decision, justification, valid basis, dimension — 1 point each.
- Problem 26: coefficient rank, augmented rank, contradiction, conclusion — 1 each.
- Problem 27: dependence relation, basis, target coefficients, dimension — 1 each.
- Problem 28: correctly ordered matrix, forward coordinates, inverse, round trip — 1 each.

A correct-looking answer without its required reasoning does not earn the
corresponding practice point. Use the solution's diagnostic link, then retry a
fresh question from that topic. Aim to reproduce every method unaided before
calling yourself ready; this is not a prediction of a course grade.

```{include} practice.md
:start-after: <!-- mixed:start -->
:end-before: <!-- mixed:end -->
```

(w3-source-notes)=
## Sources and next steps

This chapter develops Erisa Terolli's CS 556
`resources/lectures/WK3_VectorSpaces_SLE_Rank.pdf`, **all 35 PDF pages**, with
Parts A–K in source order. Title/reveal pages are consolidated. The handwritten
Q1–Q3 on pp. 16–17, the graphic-only column-space example, rank examples,
independence diagrams, span examples, and exact p. 34 coordinate conversion are
retained. Original diagrams replace third-party source artwork.

The p. 16 Q2 particular solution is corrected by substitution; the p. 17
contradiction is recomputed from its original equations; p. 29's membership
statement is clarified as membership in span(S). Added proofs, dimension counts,
shadow interpretations, numerical checks and fresh practice are editorial additions.
Practice 8 maps to supplied Recitation 2 Problem 2; Practice 15 to Recitation 2
Problem 3; Practice 16 to its Problem 1 and Assignment 2 Problem 1. Their mathematics
is independently checked rather than accepted from the supplied answers.

The supplied midterm topic list is represented here by spaces, subspaces,
rank, the four fundamental spaces, independence, span, basis, change of basis,
and elimination. The complete cross-course exam blueprint remains separate work.
Source-page/problem destinations and verification limits are recorded in the
repository's `authoring/lecture3-coverage.md` and `authoring/lecture3-review.md`.
Lecture 4 will develop orthogonality, projection, and least squares; it is not
part of this chapter's delivered scope.

**Review:** [Page 4 · TL;DR cheat sheet](cheatsheet.md).
