(lecture-one)=
# Vectors and linear combinations

<div class="chapter-kicker">Lecture 1 · Page 1 of 4 · What does a view reveal?</div>

Move a marked bead toward a screen. Its front shadow can stay in exactly the same
place even though the bead moved. A second view can reveal the missing depth.
Linear algebra gives us a language for describing the point, its measurements,
and the information a view retains.

We use ideal **parallel-ray views of labeled points**, with fixed calibrated axes
and a shared reference origin. A point $\mathbf p=(X,Y,Z)^T$ has front-screen
coordinates $(X,Y)^T$; the side screen records $(Y,Z)^T$.
We follow matched point marks, rather than attempting to reconstruct a solid
object from its silhouette.

```{figure} ../figures/lecture1/shadow-views.svg
:name: fig-w1-shadows
:alt: Two point positions p=(2,3,4) and p-prime=(2,3,9) share front coordinates (2,3). The side view records (3,4) and (3,9), revealing the changed depth. The calibrated screen coordinates are labeled X,Y for the front and Y,Z for the side.

One point, two views. A front view keeps X and Y; the side view makes a change in Z
visible. This is an original idealized coordinate model, not a perspective photograph.
```

<nav class="lecture-path" aria-label="Lecture 1 learning path">
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Vectors & combinations</span></a>
<a href="geometry.html"><span class="path-number">02</span><span>Dot products & geometry</span></a>
<a href="matrix-guide.html"><span class="path-number">03</span><span>Matrices & products</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

You need signed arithmetic, fractions, square roots, and simple algebra. No optics
background is assumed. Keep two records distinct: a **single point’s coordinates**
and a **list of measurements across several labeled points**.

:::{admonition} What you will understand
:class: key-result

By the end of this page, you should be able to:

1. Read ordered coordinates and compute sums, differences, and scalar multiples.
2. Decide whether a target can be made from given vector directions.
3. Check a claimed combination against every target coordinate.
4. Explain what a result means and check it independently.
:::

::::{div} page-roadmap

**On this page**

- {ref}`1.1 · Vector records <w1-vectors>`
- {ref}`1.2 · Addition and scaling <w1-vector-arithmetic>`
- {ref}`1.3 · Linear combinations <w1-combinations>`
::::

(w1-vectors)=
## 1.1 Vector records

::::{div} section-intro

**Learning goal:** Read a vector and state what each coordinate records.

<span class="source-label">Lecture pages 3–6</span>

Label four beads A–D so each shadow mark can be matched to its point.
What can an ordered list of their screen positions tell you?
::::


### Start with the entries, not the brackets

On the front screen, four labeled beads A–D have horizontal positions
$3,1,3,1$, measured in the same chosen length unit. Their vertical coordinates
are fixed at $1,2,3,4$ so their marks remain distinguishable. The ordered horizontal
profile is $\mathbf r=(3,1,3,1)^T$. Entry 1 belongs to A, entry 2 to B, and so on.
Reordering entries changes the record unless the bead labels are also redefined.

:::{admonition} Definition 1.1 · Real column vector
:class: definition

A vector $\mathbf v\in\mathbb R^n$ is an ordered list of $n$ real entries,
written here as a column:

$$
\mathbf v=\begin{bmatrix}v_1\\v_2\\\vdots\\v_n\end{bmatrix}.
$$

The number $n$ is the number of coordinates. The symbol $v_i$ means entry $i$.
:::

Thus $\mathbf r=(3,1,3,1)^T\in\mathbb R^4$. The superscript $T$ turns the
horizontal list into a column; we will define transpose formally later. In
prose, a tuple such as $(3,1,3,1)$ names the entries; in products, we state whether
it is a row or a column.

The $\mathbb R$ means real-valued coordinates. Positions may be fractional or
negative: a negative X is simply left of the chosen origin. Any real value is permitted in this ideal
coordinate model.

| Record | Dimension | What it leaves out |
| --- | --- | --- |
| One point $(X,Y,Z)^T$ | $\mathbb R^3$ | Other points in the scene |
| Its front mark $(X,Y)^T$ | $\mathbb R^2$ | Depth Z |
| Four beads' X profile $(X_A,X_B,X_C,X_D)^T$ | $\mathbb R^4$ | Their Y and Z coordinates |

Our second profile is $\mathbf s=(1,3,1,3)^T$. Both profiles sum to eight, but they
place individual marks differently. The sum is a summary, not a full arrangement.

The lecture's house example uses $(3,2,2,2008,150000)^T$ for bedrooms, bathrooms,
floors, year, and price. Unlike our equally scaled X coordinates, those entries
have different units; a raw distance would need a reasoned choice of scaling.

**The lecture's first vectors** are $(5,2)^T\in\mathbb R^2$ and
$(1,7,3)^T\in\mathbb R^3$. Adding a coordinate, as in
$(1,2)^T\to(1,2,3)^T$, changes the coordinate space.

### Algebraic and geometric views

In $\mathbb R^2$, the vector $(a,b)^T$ can be drawn as an arrow from the origin
to the point $(a,b)$. Its components are displacement along two coordinate axes.
The same displacement can be drawn from another starting point; its coordinates
still describe the change, not the arrow's absolute location.

For our four-bead profile, the four coordinates are **X measurements of four
points**, not four physical spatial axes. Geometry in $\mathbb R^4$ compares these
measurement records. A later plot will display a two-dimensional family of profiles;
it will not depict a physical rotation of the frame.

The standard directions make this representation explicit:
$\mathbf e_1=(1,0)^T$, $\mathbf e_2=(0,1)^T$, and
$(a,b)^T=a\mathbf e_1+b\mathbf e_2$.
In three dimensions the coordinate directions are $(1,0,0)^T$, $(0,1,0)^T$,
$(0,0,1)^T$; combining them with coefficients a,b,c gives $(a,b,c)^T$.

A two-coordinate screen mark $(2,2)^T$ has an equally concrete meaning:
two units along each screen axis. Many three-dimensional points can share it,
because the front view does not include Z.



:::{admonition} Check your understanding
:class: checkpoint

Profiles $(2,1,2,1)^T$ and $(1,2,1,2)^T$ both have coordinate sum six.
Do they place all four labeled marks at the same horizontal positions?
:::

:::{dropdown} Check your reasoning

No. Corresponding entries differ in all four positions. The equal total is only a summary; it does not recover the ordered record.
:::

::::{div} section-recap

**Keep this:** Coordinates carry both an order and a meaning; equal totals can hide different records.

**Try it yourself:** {ref}`Problem 1 <w1-p01>`.
::::

(w1-vector-arithmetic)=
## 1.2 Addition and scalar multiplication

::::{div} section-intro

**Learning goal:** Compute vector sums, differences, and scaled vectors.

<span class="source-label">Lecture pages 7–9</span>

Move each labeled bead horizontally, then apply a second set of movements.
The combined displacements add entry by entry; comparing two configurations gives
a signed difference profile.
::::

### Adding compatible vectors

Addition combines corresponding entries:

$$
\begin{bmatrix}u_1\\\vdots\\u_n\end{bmatrix}
+
\begin{bmatrix}v_1\\\vdots\\v_n\end{bmatrix}
=
\begin{bmatrix}u_1+v_1\\\vdots\\u_n+v_n\end{bmatrix}.
$$

Both vectors must belong to the same coordinate space **and describe matching
coordinates**. An A–D list of horizontal displacements cannot be added meaningfully
to an unrelated four-number record merely because both lists have length four.

:::{admonition} Worked example 1.1 · Combine horizontal movements
:class: example

For $\mathbf r=(3,1,3,1)^T$ and $\mathbf s=(1,3,1,3)^T$,

$$
\mathbf r+\mathbf s=\begin{bmatrix}4\\4\\4\\4\end{bmatrix}.
$$

Interpreted as successive horizontal displacements from a zero-X reference,
r followed by s moves **each bead four units**. The coordinate sum is $16=8+8$.
We added movement records; we did not add or superimpose shadow images.
:::

Geometrically, vector addition is the head-to-tail rule: draw the second
displacement from the endpoint of the first. The resulting displacement has the
sum of their components. This is why geometric and componentwise addition agree.

:::{admonition} Worked example 1.2 · Vector addition and subtraction
:class: example

**Given:** $\mathbf x=(0,2)^T$ and $\mathbf y=(2,2)^T$.

1. **Check compatibility.** Both vectors have two matching coordinates.
2. **Add entrywise:** $\mathbf x+\mathbf y=(0+2,2+2)^T=(2,4)^T$.
3. **Subtract entrywise:** $\mathbf x-\mathbf y=(0-2,2-2)^T=(-2,0)^T$.
4. **Check:** adding y back to the difference returns x.
:::

### Differences describe changes

Subtraction is addition of the negative:

$$
\mathbf r-\mathbf s=\begin{bmatrix}2\\-2\\2\\-2\end{bmatrix}.
$$

Compared with configuration s, A and C are two units farther right in r, while
B and D are two units farther left. The signed difference describes those
horizontal changes. Its entries sum to zero because the two coordinate sums agree.

The zero vector $\mathbf 0=(0,\ldots,0)^T$ has the appropriate dimension for its
context. A zero change means no change in that record; it does not imply an
an empty scene or the absence of depth changes that this record omits.

### Scalar multiplication

For a real scalar $c$,

$$c\mathbf v=(cv_1,\ldots,cv_n)^T.$$

Six successive screen-plane displacements of $(2,2)^T$ combine to $(12,12)^T$.
Scaling a geometric vector by positive $c$ changes its length by $c$ and preserves
its direction; negative $c$ reverses direction, with length scaled by $|c|$.
Multiplication by zero gives the zero vector.

The lecture separately scales $\mathbf x=(2,2)^T$:
$2\mathbf x=(4,4)^T$, $\tfrac12\mathbf x=(1,1)^T$,
and $-\mathbf x=(-2,-2)^T$. The first two preserve direction; the last reverses it.

Fractions and negative scalars are allowed. Half the profile
$\tfrac12(3,1,3,1)^T=(1.5,0.5,1.5,0.5)^T$ is also a possible coordinate record.
Physical restrictions, such as a finite screen boundary, would be additional
assumptions; they do not come from the definition of a real vector.

:::{admonition} Check your understanding
:class: checkpoint

Let $\mathbf u=(5,2)^T$ and $\mathbf v=(1,7)^T$. Compute $\mathbf u-2\mathbf v$.
If the entries are screen coordinates, does the negative entry invalidate the result?
:::

:::{dropdown} Reason it through

$\mathbf u-2\mathbf v=(5-2,2-14)^T=(3,-12)^T$. It is a valid vector in
$\mathbb R^2$. With signed screen coordinates, -12 means twelve units below
the chosen horizontal reference axis. The calculation requires matching coordinate
meanings, not nonnegative entries.
:::

### Useful algebraic rules

For compatible real vectors and scalars,

$$
\mathbf u+\mathbf v=\mathbf v+\mathbf u,\qquad
(\mathbf u+\mathbf v)+\mathbf w=\mathbf u+(\mathbf v+\mathbf w),
$$

$$
c(\mathbf u+\mathbf v)=c\mathbf u+c\mathbf v,\qquad
(c+d)\mathbf u=c\mathbf u+d\mathbf u.
$$

These follow entry by entry from real-number arithmetic. They let us reorganize
computations without changing the result. **Compatibility comes first**; the rules
do not make addition between a two-entry and a three-entry vector meaningful.


::::{div} section-recap

**Keep this:** Add matching coordinates. Scale every entry. Interpret negative entries as changes when appropriate.

**Try it yourself:** {ref}`Problem 2 <w1-p02>`.
::::

(w1-combinations)=
## 1.3 Linear combinations

::::{div} section-intro

**Learning goal:** Construct a general combination and test whether a target belongs to its family.

<span class="source-label">Lecture pages 10–19</span>

Can moving all four beads together, plus one alternating displacement pattern,
produce every horizontal profile? Writing the general form exposes the limits.
::::


Addition and scalar multiplication become much more useful together. They let
us describe an entire family of records with a few directions and adjustable
coefficients. The important question is no longer just “what is this vector?”
but “which vectors can these ingredients produce?”

### Separate a baseline from an alternating contrast

Consider two horizontal profiles of our labeled points:

$$
\mathbf r=\begin{bmatrix}3\\1\\3\\1\end{bmatrix},\qquad
\mathbf s=\begin{bmatrix}1\\3\\1\\3\end{bmatrix}.
$$

Define

$$
\mathbf e=\begin{bmatrix}1\\1\\1\\1\end{bmatrix},\qquad
\mathbf a=\begin{bmatrix}1\\-1\\1\\-1\end{bmatrix}.
$$

Then $\mathbf r=2\mathbf e+\mathbf a$ and $\mathbf s=2\mathbf e-\mathbf a$.
The term $2\mathbf e$ places every bead at X=2. Adding a moves A and C one
unit right, and B and D one unit left. Subtracting a reverses the alternation.
Here e and a are displacement patterns across four labeled points.

:::{admonition} Definition 1.2 · Linear combination
:class: definition

For vectors $\mathbf v_1,\ldots,\mathbf v_k$ in the same real coordinate space,
a **linear combination** is

```{math}
:label: eq-w1-combination
\mathbf y=c_1\mathbf v_1+\cdots+c_k\mathbf v_k,
\qquad c_1,\ldots,c_k\in\mathbb R.
```

The coefficients specify how much of each direction is used. A zero coefficient
omits a direction; a negative coefficient reverses its contribution.
:::

All combinations of e and a have the form

$$
\alpha\mathbf e+\beta\mathbf a
=\begin{bmatrix}\alpha+\beta\\\alpha-\beta\\\alpha+\beta\\\alpha-\beta\end{bmatrix}.
$$

The third coordinate must equal the first, and the fourth must equal the second.
The particular profile $(3,1,3,1)^T$ uses $(\alpha,\beta)=(2,1)$.
The uniform profile $(2,2,2,2)^T$ uses $(2,0)$.
The profile $(3,1,2,1)^T$ cannot be produced: its first and third coordinates disagree.
This is a structural test that avoids guessing coefficients endlessly.

All real coefficients are allowed in this coordinate model. Negative coordinates
place marks on the opposite side of the origin; fractional coordinates describe
fractional distances. If a particular apparatus has bounds, state them separately.

### One direction makes a line

All scalar multiples $c\mathbf u$ of one **nonzero** vector form a line through
the origin. If $\mathbf u=\mathbf 0$, the only result is the zero vector; there
is no nonzero direction to follow.

The lecture illustrates multiples of $(1,2,4)^T$ in three-dimensional space.
Although the vector has three entries, its multiples have only one freely
adjustable coefficient. They lie on a line, not throughout $\mathbb R^3$.
The number of entries and the number of genuinely different directions available
are different ideas. We will formalize the latter in Week 3.

### Two directions: a line or a plane?

Two nonzero vectors do not automatically produce a plane. If one is a multiple
of the other, adding them still gives only that same line. For instance,
$c(1,2)^T+d(2,4)^T=(c+2d)(1,2)^T$.

When two vectors are not multiples, their real combinations form a plane
through the origin in their ambient space. Our e and a are such a pair in
$\mathbb R^4$: e has all entries equal, while a alternates signs. Their combinations
form a two-dimensional family of four-entry records. This does not say that every
four-entry pattern belongs to that family.

```{figure} ../figures/lecture1/shadow-profiles.svg
:name: fig-w1-profiles
:alt: A coordinate plot with alpha on the horizontal axis and beta on the vertical axis. The uniform record 2e is at 2,0; r equals 2e plus a at 2,1; s equals 2e minus a at 2,-1. The associated physical panel locates the four labeled marks for each profile.

The screen panel shows the actual horizontal marks; the coefficient panel shows
**which record** a combination produces. Those are different coordinate systems.
```

:::{admonition} Worked example 1.3 · The lecture's plane-membership test
:class: example

**Question:** Which vectors can be made from
$\mathbf v=(1,1,0)^T$ and $\mathbf w=(0,1,1)^T$?

1. **Write a general combination:**
   $c\mathbf v+d\mathbf w=(c,c+d,d)^T$.
2. **Compare with a target $(x,y,z)^T$.** The first and third entries force
   $c=x$ and $d=z$, so the middle must satisfy **$y=x+z$**.
3. **Check sufficiency.** Whenever $y=x+z$, choosing those coefficients reproduces
   all three entries. This is an if-and-only-if membership test.
4. **Apply it.** The lecture's $(1,2,3)^T$ is outside because $2\ne1+3$.
   In contrast, $(1,3,2)^T=\mathbf v+2\mathbf w$ is inside.

**Method cue:** “Can this vector be built from these vectors?” means write the
combination first, then compare coordinates. Larger cases become linear systems.
:::

### The lecture's line, plane, and space example

The slides use $\mathbf u=(1,2,4)^T$, $\mathbf v=(2,1,4)^T$,
and $\mathbf w=(9,8,7)^T$. The combinations $c\mathbf u$ fill a line;
$c\mathbf u+d\mathbf v$ fill a plane; adding $e\mathbf w$ reaches all
of $\mathbb R^3$ because w lies outside that plane. A third vector already in
the plane would add no new direction. We will develop systematic tests later:
**counting vectors alone does not establish what they can produce.**

:::{admonition} Check your understanding
:class: checkpoint

Can $\mathbf t=(4,2,4,2)^T$ be written as $\alpha\mathbf e+\beta\mathbf a$?
Can $\mathbf q=(4,2,3,2)^T$? Explain before opening the answer.
:::

:::{dropdown} Reason it through

For t, solve $\alpha+\beta=4$, $\alpha-\beta=2$, giving $\alpha=3,\beta=1$.
The repeated-coordinate conditions hold. For q they fail: coordinate 3 is 3
rather than 4, so no choice of coefficients can work. A failed structural
condition settles the second question without solving an inconsistent system.
:::

A model can likewise describe a record as a weighted sum of simpler patterns.
Next we need a way to compare those patterns: dot products, lengths, and angles.


::::{div} section-recap

**Keep this:** A membership claim needs coefficients that reproduce every coordinate, or a condition that proves none can.

**Try it yourself:** {ref}`Problem 3 <w1-p03>` · {ref}`Problem 9 <w1-p09>`.
::::


(w1-practice)=
(w1-solutions)=

(w1-practice-vectors)=
## Practice · vectors and combinations

Try each problem before opening its explained answer directly below. Problem numbers
remain stable across the chapter; the questions here follow this page’s topics.

```{include} practice.md
:start-after: <!-- vectors:start -->
:end-before: <!-- vectors:end -->
```

**Next:** [Page 2 · Dot products and geometry](geometry.md).
