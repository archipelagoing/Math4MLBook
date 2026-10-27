(lecture-one)=
# Lecture 1 · Vectors and geometry

<div class="chapter-kicker">What does a view reveal—and what does it hide?</div>

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
<a href="index.html" aria-current="page"><span class="path-number">01</span><span>Vectors & geometry</span></a>
<a href="matrix-guide.html"><span class="path-number">02</span><span>Matrices & products</span></a>
<a href="practice.html"><span class="path-number">03</span><span>Exercises</span></a>
<a href="solutions.html"><span class="path-number">04</span><span>Solutions</span></a>
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
3. Compute dot products, lengths, unit vectors, and angles with their conditions.
4. Explain what a result means and check it independently.
:::

::::{div} page-roadmap

**On this page**

- {ref}`1.1 · Vector records <w1-vectors>`
- {ref}`1.2 · Addition and scaling <w1-vector-arithmetic>`
- {ref}`1.3 · Linear combinations <w1-combinations>`
- {ref}`1.4 · Dot products <w1-geometry>`
- {ref}`1.5 · Length and unit vectors <w1-norms>`
- {ref}`1.6 · Angles and the cosine formula <w1-angles>`
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

(w1-geometry)=
## 1.4 Dot products

::::{div} section-intro

**Learning goal:** Calculate a scalar dot product and use its algebraic properties correctly.

<span class="source-label">Lecture pages 20–23</span>

Two configurations can have equal coordinate sums and different horizontal
positions. The dot product compares matching point readings.
::::


Two profiles can have equal coordinate sums and different point positions. The
dot product compares matching entries; from it we define Euclidean length,
distance, and angle in the chosen record space.

### The dot product returns a scalar

:::{admonition} Definition 1.3 · Euclidean dot product
:class: definition

For $\mathbf u,\mathbf v\in\mathbb R^n$,

```{math}
:label: eq-w1-dot
\mathbf u\cdot\mathbf v=\langle\mathbf u,\mathbf v\rangle=\mathbf u^T\mathbf v
=\sum_{i=1}^n u_i v_i.
```

The summation means: multiply matching entries, then add the $n$ products.
The result is a real **number**, not a vector.
:::

For the two four-point profiles,

$$
(3,1,3,1)\cdot(1,3,1,3)=3+3+3+3=12.
$$

:::{admonition} Worked example 1.4 · The lecture's dot product
:class: example

**Given:** $\mathbf v=(3,4)^T$ and $\mathbf w=(4,3)^T$.

1. Pair the first coordinates: $3\cdot4=12$.
2. Pair the second coordinates: $4\cdot3=12$.
3. Add the products: $\mathbf v^T\mathbf w=12+12=24$.

The answer is one number. It is neither a new vector nor an angle yet.
:::

A dot product can read a point along a screen axis. With
$\mathbf p=(2,3,4)^T$ and horizontal unit direction $\mathbf h=(1,0,0)^T$,
$\mathbf h^T\mathbf p=2$ selects the horizontal coordinate. The front screen's
other axis $(0,1,0)^T$ selects 3; neither reading includes depth 4.

### Properties and a common misuse

Over the real numbers,

$$
\mathbf u^T\mathbf v=\mathbf v^T\mathbf u,
\qquad
\mathbf u^T(\mathbf v+\mathbf w)=\mathbf u^T\mathbf v+\mathbf u^T\mathbf w,
$$

$$
(c\mathbf u)^T\mathbf v=c(\mathbf u^T\mathbf v),
\qquad
\mathbf v^T\mathbf v=\sum_i v_i^2\ge0.
$$

Moreover, $\mathbf v^T\mathbf v=0$ only for the zero vector: a sum of nonnegative
squares can vanish only when every entry is zero.

The dot product is not a closed operation from two vectors back to a vector.
Consequently, $\mathbf u\cdot(\mathbf v\cdot\mathbf w)$ is not another ordinary
vector dot product: the inner result is a scalar. Even the related scalar-vector
expressions $\mathbf u(\mathbf v\cdot\mathbf w)$ and
$(\mathbf u\cdot\mathbf v)\mathbf w$ generally differ. With
$\mathbf u=(1,0)^T$, $\mathbf v=\mathbf w=(0,1)^T$, the first is u and the second
is zero. Always track the **type and shape of the output**, not just the symbols.


**A zero dot product is called orthogonality.** Section 1.6 connects this algebraic
condition to a right angle between nonzero directions.

:::{admonition} Check your understanding
:class: checkpoint

For $\mathbf u=(3,-1)^T$ and $\mathbf v=(2,6)^T$, compute the dot product.
What can you conclude from its value?
:::

:::{dropdown} Check your reasoning

$3\cdot2+(-1)\cdot6=6-6=0$. Both vectors are nonzero, so they are orthogonal.
A matching total would not establish this; the coordinate products do.
:::

::::{div} section-recap

**Keep this:** The dot product multiplies matching entries, then sums; its output is a scalar.

**Try it yourself:** {ref}`Problem 4 <w1-p04>` · {ref}`Problem 11 <w1-p11>`.
::::

(w1-norms)=
## 1.5 Length, magnitude, norm, and unit vectors

::::{div} section-intro

**Learning goal:** Find a Euclidean length and normalize a nonzero direction.

<span class="source-label">Lecture pages 27–34</span>

Adding the X coordinates gives one summary. The Euclidean norm answers a
different question: how long is the ordered profile in its declared coordinate geometry?
::::

### Length, magnitude, and norm

:::{admonition} Definition 1.4 · Euclidean norm and distance
:class: definition

$$
\|\mathbf v\|=\sqrt{\mathbf v^T\mathbf v}=\sqrt{\sum_i v_i^2},
\qquad
\operatorname{dist}(\mathbf u,\mathbf v)=\|\mathbf u-\mathbf v\|.
$$

Length, magnitude, and Euclidean norm name the same quantity here.
It is the nonnegative square root. In particular,
$\|\mathbf v\|^2=\mathbf v^T\mathbf v$; the norm itself is not generally that sum.
:::

For $\mathbf v=(3,4)^T$, $\|\mathbf v\|=5$. For the four-point profile
$\mathbf r=(3,1,3,1)^T$,

$$\|\mathbf r\|=\sqrt{9+1+9+1}=\sqrt{20}=2\sqrt5.$$

Its entries sum to eight, but its norm is not eight. Sum and Euclidean length
answer different questions. For e and a from the profile family, both norms are 2.
For $\mathbf r-\mathbf s=(2,-2,2,-2)^T$, the distance is 4.
This compares the four horizontal coordinates together. It does not include
unrecorded depth, so it is not a full three-dimensional distance between objects.

Scaling changes norm by absolute magnitude:

$$
\|c\mathbf v\|=\sqrt{c^2\mathbf v^T\mathbf v}=|c|\,\|\mathbf v\|.
$$

The absolute value matters when $c<0$; lengths are not negative.

### Normalize a direction, with its hypothesis

For $\mathbf v\ne\mathbf0$, define

$$\widehat{\mathbf v}=\frac{\mathbf v}{\|\mathbf v\|}.$$

Its norm is $\|\mathbf v\|/\|\mathbf v\|=1$; positive scaling preserves direction.

:::{admonition} Worked example 1.5 · The lecture's normalization
:class: example

**Question:** Turn $(3,4)^T$ into a unit vector pointing the same way.

1. **Find its length:** $\sqrt{3^2+4^2}=5$.
2. **Choose the scalar:** $\mu=1/\|\mathbf v\|=1/5$.
3. **Scale:** $\widehat{\mathbf v}=\mu\mathbf v=(3/5,4/5)^T$.
4. **Verify unit length:** $(3/5)^2+(4/5)^2=1$; its norm is therefore 1.

For our four-point profile the same method gives
$\widehat{\mathbf r}=(3,1,3,1)^T/(2\sqrt5)$. Fractional coordinates describe a
direction in record space; it no longer retains the original coordinate scale.
:::

:::{admonition} Common pitfall · A unit direction is not the full position record
:class: pitfall

You cannot normalize the zero vector: division by its norm would divide by zero.
A normalized record keeps direction but discards its original magnitude.
Fractional coordinates are valid; normalization does not recover omitted depth.
:::

### Orthogonality of displacement profiles

The uniform displacement e and alternating displacement a satisfy

$$\mathbf e^T\mathbf a=1-1+1-1=0.$$

They are perpendicular in the chosen Euclidean coordinate geometry. This does
not assert that the frame physically turns through a right angle. It says the
signed contrast has no net alignment with the uniform direction in this metric.

A useful consequence is visible in our profile:

$$
\mathbf r=2\mathbf e+\mathbf a,\qquad
\|\mathbf r\|^2=\|2\mathbf e\|^2+\|\mathbf a\|^2=16+4=20.
$$

Why are there no cross terms? Expanding the dot product gives

$$
(2\mathbf e+\mathbf a)^T(2\mathbf e+\mathbf a)
=4\mathbf e^T\mathbf e+4\mathbf e^T\mathbf a+\mathbf a^T\mathbf a.
$$

The middle term is zero. This is the algebra behind the Pythagorean relationship.
We will reuse these directions when studying projection and orthonormal bases.



:::{admonition} Check your understanding
:class: checkpoint

Find the norm and unit direction of $(0,-5)^T$. What would fail for $(0,0)^T$?
:::

:::{dropdown} Check your reasoning

The norm is $\sqrt{0^2+(-5)^2}=5$, so the unit direction is $(0,-1)^T$. Its norm is 1. The zero vector would require division by zero and has no unit direction.
:::

::::{div} section-recap

**Keep this:** A norm is a nonnegative length; normalization divides a nonzero vector by that length.

**Try it yourself:** {ref}`Problem 5 <w1-p05>` · {ref}`Problem 18 <w1-p18>`.
::::

(w1-angles)=
## 1.6 Angles and the cosine formula

::::{div} section-intro

**Learning goal:** Find the angle between nonzero vectors and explain why the cosine formula works.

<span class="source-label">Lecture pages 24–26</span>

Our two point profiles have equal coordinate sums and equal norms. Their angle
describes something neither summary alone captures: alignment in the record space.
::::

### From a dot product to an angle

:::{admonition} Theorem 1.1 · Cosine formula
:class: key-result theorem

For nonzero vectors, the Euclidean angle $\theta\in[0,\pi]$ satisfies

```{math}
:label: eq-w1-cosine
\cos\theta=\frac{\mathbf u^T\mathbf v}{\|\mathbf u\|\|\mathbf v\|}.
```

Divide by **both** lengths before applying arccos.
:::

Equivalently, $\mathbf u^T\mathbf v=\|\mathbf u\|\|\mathbf v\|\cos\theta$,
the cosine formula in the lecture’s original form.

::::{admonition} Proof · Why the cosine formula holds
:class: proof

To derive it, compare two expressions for the squared distance between endpoints.
Expanding the dot product gives

$$
\begin{aligned}
\|\mathbf u-\mathbf v\|^2
&=(\mathbf u-\mathbf v)^T(\mathbf u-\mathbf v)\\
&=\mathbf u^T\mathbf u-\mathbf u^T\mathbf v-\mathbf v^T\mathbf u+\mathbf v^T\mathbf v\\
&=\|\mathbf u\|^2+\|\mathbf v\|^2-2\mathbf u^T\mathbf v.
\end{aligned}
$$

For perpendicular nonzero directions, Pythagoras instead gives
$\|\mathbf u-\mathbf v\|^2=\|\mathbf u\|^2+\|\mathbf v\|^2$;
comparison with the expansion forces $\mathbf u^T\mathbf v=0$.
For a general angle, the cosine rule applied to the triangle gives

$$
\|\mathbf u-\mathbf v\|^2
=\|\mathbf u\|^2+\|\mathbf v\|^2
-2\|\mathbf u\|\|\mathbf v\|\cos\theta.
$$

Equating them yields the formula. The nonzero hypothesis permits division by
both norms. In higher-dimensional Euclidean spaces the same relationship applies
in the plane generated by the two directions, with collinear cases handled by
the corresponding limiting angles.

::::

For nonzero vectors, a positive dot product means an angle below $90^\circ$;
a negative one means an angle above $90^\circ$; zero means a right angle.
Parallel and opposite directions give the endpoint angles $0^\circ$ and $180^\circ$. The zero vector has zero dot product
with everything and is algebraically orthogonal to every vector, but has no
geometric direction or defined angle.

:::{admonition} Worked example 1.6 · From the lecture's vectors to their angle
:class: example

1. **Compute the dot product:** for $(3,4)^T$ and $(4,3)^T$, it is 24.
2. **Find both lengths:** each is 5.
3. **Normalize the comparison:** $\cos\theta=24/(5\cdot5)=24/25$.
4. **Recover the angle:** $\theta=\arccos(24/25)\approx16.26^\circ$.

Check: $24/25$ is between -1 and 1 and positive, so the angle is below $90^\circ$.
The slides give the dot product; the angle evaluation applies their formula.
:::

:::{admonition} Worked example 1.7 · Similar summaries, different directions
:class: example

For $\mathbf r=(3,1,3,1)^T$ and $\mathbf s=(1,3,1,3)^T$, the dot product is 12
and both norms are $\sqrt{20}$. Thus

$$\cos\theta=\frac{12}{20}=\frac35,\qquad
\theta=\arccos(3/5)\approx53.13^\circ.$$

Check: $\|\mathbf r-\mathbf s\|^2=16$, and
$20+20-2\cdot12=16$. The distance and dot-product calculations agree.
:::

```{figure} ../figures/lecture1/shadow-geometry.svg
:name: fig-w1-profile-geometry
:alt: In orthonormal record coordinates q0=e/2 and q1=a/2, r has coordinates 4,2 and s has coordinates 4,-2. A horizontal uniform component of length 4 and a vertical alternating component of length 2 form a right triangle with squared hypotenuse length 20.

The geometry belongs to the **four-point profiles**. Orthonormal axes
$\mathbf q_0=\mathbf e/2$, $\mathbf q_1=\mathbf a/2$ preserve lengths and dot products
within this family. Thus r is plotted at $(4,2)$, not $(2,1)$.
```

:::{admonition} ML connection · Direction versus magnitude
:class: connection

The normalized dot product is cosine similarity: it compares direction without
retaining magnitude. Changing feature units can change a raw angle or norm, so
coordinate scaling is a modeling decision.
:::

:::{admonition} Check your understanding
:class: checkpoint

For $\mathbf u=(1,1)^T$, $\mathbf v=(1,-1)^T$, compute the dot product,
normalize both vectors, and identify the angle. What changes if u is replaced
by the zero vector?
:::

:::{dropdown} Reason it through

The dot product is 0; both norms are $\sqrt2$; the normalized vectors are
$(1,1)^T/\sqrt2$ and $(1,-1)^T/\sqrt2$. Their angle is $90^\circ$.
With zero u, the dot product remains zero, but normalization and the angle are
undefined. A familiar formula still requires its hypotheses.
:::


::::{div} section-recap

**Keep this:** Use a dot product and two nonzero lengths to find an angle; check the cosine before using arccos.

**Try it yourself:** {ref}`Problem 4 <w1-p04>` · {ref}`Problem 12 <w1-p12>`.
::::

## Page summary · Can you do this unaided?

- Read a record and distinguish individual coordinates from their sum.
- Add, subtract, and scale compatible vectors, including signed changes.
- Test a combination by comparing every target coordinate.
- Compute a dot product, norm, unit vector, and angle with conditions stated.

If a step is uncertain, use the linked exercises at each section's end, check the
solution, and retry. Next, [matrices and products](matrix-guide.md) organize several
records and apply maps to them. {ref}`Source notes <w1-source-notes>` identify the
lecture material and added teaching examples.
