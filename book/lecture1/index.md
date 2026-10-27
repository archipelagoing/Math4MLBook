(lecture-one)=
# Lecture 1 · Vectors and geometry

<div class="chapter-kicker">From stitch records to linear algebra</div>

A pattern tells your hands what to do. A mathematical record lets you compare
what you made, combine patterns, and predict counts. We will follow a **24-stitch
sampler**, divided into four sections of six stitches. A row has pink-stitch counts
$\mathbf r=(3,1,3,1)^T$; another has $\mathbf s=(1,3,1,3)^T$.
Both total eight, but their sections differ. A vector preserves that distinction.

```{figure} ../figures/lecture1/sampler.svg
:name: fig-w1-sampler
:alt: Four rows of 24 stitch cells grouped into four sections of six. The section-count matrix alternates rows 3,1,3,1 and 1,3,1,3. Each row has eight pink stitches; the rest are green.

Each matrix entry summarizes **six stitches**, rather than encoding one stitch.
The same sampler will connect vectors, geometry, and matrix multiplication.
```

**Four pages for this lecture:** vectors and geometry → [matrices and products](matrix-guide.md)
→ [exercises](practice.md) → [solutions](solutions.md).
Use the contents panel to jump between sections on this page.

You need signed arithmetic, fractions, square roots, and simple algebra. You do
not need craft experience. The examples name their records explicitly; drawings
are count schematics rather than loop-by-loop technique instructions.

(w1-vectors)=
## 1. Vectors: meaning, addition, and scaling

### Start with the entries, not the brackets

Our four marked sections contain $3,1,3,1$ pink stitches. The order matters:
entry 1 belongs to section A, entry 2 to B, and so on. Reversing or rearranging
the entries changes the record unless we also explain how the section labels changed.

:::{admonition} Definition · Real column vector
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

The $\mathbb R$ means real-valued coordinates. Actual stitch counts are
nonnegative integers no larger than six per section in this example. We use the
larger real coordinate space so that differences and later algebra make sense.
A result can be mathematically valid while failing the conditions for a literal
row of stitches.

A whole-row total loses the sections; section counts lose the order of stitches
inside each section. Choose the record that answers your question. The lecture's
house example uses $(3,2,2,2008,150000)^T$ for bedrooms, bathrooms, floors, year,
and price. Unlike section counts, those coordinates have different units; a raw
distance would need a reasoned choice of scaling.

**The lecture's first vectors** are $(5,2)^T\in\mathbb R^2$ and
$(1,7,3)^T\in\mathbb R^3$. Adding a coordinate, as in
$(1,2)^T\to(1,2,3)^T$, changes the coordinate space.

### Algebraic and geometric views

In $\mathbb R^2$, the vector $(a,b)^T$ can be drawn as an arrow from the origin
to the point $(a,b)$. Its components are displacement along two coordinate axes.
The same displacement can be drawn from another starting point; its coordinates
still describe the change, not the arrow's absolute location.

For the sampler, the four coordinates are **section counts**, not four spatial
axes of the cloth. We can still use the geometry of $\mathbb R^4$ to compare
these records, provided that we say what metric we are using. Later we will find
a two-dimensional family of repeats and draw its coordinate geometry without
pretending that the fabric itself lives on that plot.

The standard directions make this representation explicit:
$\mathbf e_1=(1,0)^T$, $\mathbf e_2=(0,1)^T$, and
$(a,b)^T=a\mathbf e_1+b\mathbf e_2$.
In three dimensions the coordinate directions are $(1,0,0)^T$, $(0,1,0)^T$,
$(0,0,1)^T$; combining them with coefficients a,b,c gives $(a,b,c)^T$.

A simple two-coordinate craft record might count knit and purl operations:
$\mathbf k=(2,2)^T$ records one `k2,p2` repeat. It does not encode their order:
`k,p,k,p` gives the same count vector. An ordered chart is a richer record.

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
coordinates**. Four section counts should not be added to four unrelated gauge
measurements merely because both lists have length four.

:::{admonition} Worked example · Combine two recorded rows
:class: example

For $\mathbf r=(3,1,3,1)^T$ and $\mathbf s=(1,3,1,3)^T$,

$$
\mathbf r+\mathbf s=\begin{bmatrix}4\\4\\4\\4\end{bmatrix}.
$$

Each section has four pink stitches **across the two rows**, not four in a newly
specified single row. The record's interpretation changed from one row to two
rows, and we stated that change. The total $16$ agrees with $8+8$.
:::

Geometrically, vector addition is the head-to-tail rule: draw the second
displacement from the endpoint of the first. The resulting displacement has the
sum of their components. This is why geometric and componentwise addition agree.

:::{admonition} Lecture example · Vector addition and subtraction
:class: example

For $\mathbf x=(0,2)^T$ and $\mathbf y=(2,2)^T$,
$\mathbf x+\mathbf y=(2,4)^T$ and $\mathbf x-\mathbf y=(-2,0)^T$.
Check the two coordinates separately; subtraction changes every entry of y's sign.
:::

### Differences describe changes

Subtraction is addition of the negative:

$$
\mathbf r-\mathbf s=\begin{bmatrix}2\\-2\\2\\-2\end{bmatrix}.
$$

This says r has two more pink stitches in A and C, and two fewer in B and D.
There are no negative stitches in either actual row. The negative entries belong
to a **change record**. Its entries sum to zero because both rows have eight pink stitches.

The zero vector $\mathbf 0=(0,\ldots,0)^T$ has the appropriate dimension for its
context. A zero change means no change in that record; it does not imply an
empty fabric or the absence of physical differences omitted by the record.

### Scalar multiplication

For a real scalar $c$,

$$c\mathbf v=(cv_1,\ldots,cv_n)^T.$$

Six repetitions of the knit/purl count $(2,2)^T$ give $(12,12)^T$: 24 operations.
Scaling a geometric vector by positive $c$ changes its length by $c$ and preserves
its direction; negative $c$ reverses direction, with length scaled by $|c|$.
Multiplication by zero gives the zero vector.

The lecture separately scales $\mathbf x=(2,2)^T$:
$2\mathbf x=(4,4)^T$, $\tfrac12\mathbf x=(1,1)^T$,
and $-\mathbf x=(-2,-2)^T$. The first two preserve direction; the last reverses it.

Fractions and negative scalars are allowed in $\mathbb R^n$. But half an arbitrary
count vector need not be an executable stitch instruction. For example,
$\frac12(3,1,3,1)^T$ is a valid real vector with fractional coordinates. State the
physical constraints after doing the algebra.

:::{admonition} Check your understanding
:class: checkpoint

Let $\mathbf u=(5,2)^T$ and $\mathbf v=(1,7)^T$. Compute $\mathbf u-2\mathbf v$.
What must be true before interpreting this as a physical count record?
:::

:::{dropdown} Reason it through

$\mathbf u-2\mathbf v=(5-2,2-14)^T=(3,-12)^T$. It is a valid vector in
$\mathbb R^2$. It can describe a signed change if the coordinates match, but it
cannot itself be two nonnegative stitch counts. The meaning and feasible domain
must be supplied separately.
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

(w1-combinations)=
## 2. Linear combinations: reachable patterns

Addition and scalar multiplication become much more useful together. They let
us describe an entire family of records with a few directions and adjustable
coefficients. The important question is no longer just “what is this vector?”
but “which vectors can these ingredients produce?”

### Separate a baseline from an alternating contrast

Consider two section-count records from our panel:

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
The term $2\mathbf e$ means a shared baseline of two pink stitches per section.
The term $\mathbf a$ changes that baseline by one extra, one fewer, one extra,
one fewer. It is a signed contrast record, not a negative-yarn operation.

:::{admonition} Definition · Linear combination
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
The particular row $(3,1,3,1)^T$ uses $(\alpha,\beta)=(2,1)$.
The uniform row $(2,2,2,2)^T$ uses $(2,0)$.
The row $(3,1,2,1)^T$ cannot be produced: its first and third coordinates disagree.
This is a structural test that avoids guessing coefficients endlessly.

For a literal six-stitch section, each resulting count must be an integer from
0 through 6. Thus a real linear combination and an executable color-count row
are different questions. We first identify the algebraic family, then enforce
the physical constraints.

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

```{figure} ../figures/lecture1/repeat-family.svg
:name: fig-w1-repeat-family
:alt: A coordinate plot with alpha on the horizontal axis and beta on the vertical axis. The uniform record 2e is at 2,0; r equals 2e plus a at 2,1; s equals 2e minus a at 2,-1. Each labeled point has a separate four-entry section-count record.

Coordinates **of a repeat family**. This plot records coefficients of e and a;
it does not depict the physical width or height of a swatch.
```

### The lecture's plane example, fully worked

Take the source vectors

$$
\mathbf v=\begin{bmatrix}1\\1\\0\end{bmatrix},\qquad
\mathbf w=\begin{bmatrix}0\\1\\1\end{bmatrix}.
$$

Their combinations are

$$
c\mathbf v+d\mathbf w
=\begin{bmatrix}c\\c+d\\d\end{bmatrix}.
$$

If the coordinates are named $(x,y,z)$, every result satisfies $y=x+z$.
Conversely, if a vector satisfies $y=x+z$, choosing $c=x$ and $d=z$ produces
it. We have proved both directions:

:::{admonition} Key result · A complete membership test
:class: key-result

A vector $(x,y,z)^T$ is a combination of $(1,1,0)^T$ and $(0,1,1)^T$
**if and only if** $y=x+z$.
:::

The lecture asks for a vector outside the plane and displays $(1,2,3)^T$.
It is outside because $2\ne1+3$. In contrast, $(1,3,2)^T$ is inside:
$\mathbf v+2\mathbf w=(1,3,2)^T$. The order of entries decides the answer.

**Method choice:** When a problem asks whether a vector can be built from given
vectors, write the general combination and compare coordinates. In this example
that comparison yields one simple equation. In larger examples it becomes a
system of linear equations, which is the subject of the next lecture.

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

(w1-geometry)=
## 3. Dot products, lengths, and angles

Two repeat records can have the same total and still differ in every section.
A useful comparison should say more than “the entries add to eight.” The dot
product gives us one scalar comparison, and from it we can define Euclidean
length, distance, and angle.

### The dot product returns a scalar

:::{admonition} Definition · Euclidean dot product
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

For the two color rows,

$$
(3,1,3,1)\cdot(1,3,1,3)=3+3+3+3=12.
$$

The lecture's example $\mathbf v=(3,4)^T$, $\mathbf w=(4,3)^T$ gives
$\mathbf v\cdot\mathbf w=3\cdot4+4\cdot3=24$.
Matching dimension is necessary, but an interpretation also requires meaningful
coordinate pairing.

A dot product can apply weights. For $\mathbf n=(18,6,0)^T$ plain/increase/decrease
counts, $\mathbf h=(1,2,1)^T$ contains produced-stitch counts per operation.
Then $\mathbf h^T\mathbf n=30$ predicts the number of new stitches.
Those weights are justified by specified stitch actions. They do not estimate
yarn length or physical height without additional measurements.

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

### Length, magnitude, and norm

:::{admonition} Definition · Euclidean norm and distance
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

For $\mathbf v=(3,4)^T$, $\|\mathbf v\|=5$. For the panel record
$\mathbf r=(3,1,3,1)^T$,

$$\|\mathbf r\|=\sqrt{9+1+9+1}=\sqrt{20}=2\sqrt5.$$

Its entries sum to eight, but its norm is not eight. Sum and Euclidean length
answer different questions. For e and a from the repeat family, both norms are 2.
For $\mathbf r-\mathbf s=(2,-2,2,-2)^T$, the distance is 4.
This is distance between equal-width section-count records, not a physical
measurement of how far apart the swatches are.

Scaling changes norm by absolute magnitude:

$$
\|c\mathbf v\|=\sqrt{c^2\mathbf v^T\mathbf v}=|c|\,\|\mathbf v\|.
$$

The absolute value matters when $c<0$; lengths are not negative.

### Normalize a direction, with its hypothesis

For $\mathbf v\ne\mathbf0$, define

$$\widehat{\mathbf v}=\frac{\mathbf v}{\|\mathbf v\|}.$$

Its norm is $\|\mathbf v\|/\|\mathbf v\|=1$, and the positive scaling preserves
direction. The lecture uses the scalar $\mu=1/\|\mathbf v\|=1/5$ to normalize
$(3,4)^T$ to $(3/5,4/5)^T$. The squared entries $9/25+16/25=1$ check its unit length.
Our record $\mathbf r$ normalizes to $(3,1,3,1)^T/(2\sqrt5)$.

:::{admonition} Common pitfall · Unit direction is not a stitch instruction
:class: pitfall

You cannot normalize the zero vector: division by its norm would divide by zero.
A normalized count record usually has fractional entries; it describes a direction
in the record space, not an executable row of fractional stitches.
:::

### Orthogonality of actual repeat records

The uniform record e and signed alternating record a satisfy

$$\mathbf e^T\mathbf a=1-1+1-1=0.$$

They are perpendicular in the chosen Euclidean coordinate geometry. This does
not assert that stitch columns physically cross at a right angle. It says the
signed contrast has no net alignment with the uniform direction in this metric.

A useful consequence is visible in our row:

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

### The cosine formula and where it comes from

For nonzero vectors, the Euclidean angle $\theta\in[0,\pi]$ satisfies

```{math}
:label: eq-w1-cosine
\cos\theta=\frac{\mathbf u^T\mathbf v}{\|\mathbf u\|\|\mathbf v\|}.
```

Equivalently, $\mathbf u^T\mathbf v=\|\mathbf u\|\|\mathbf v\|\cos\theta$,
the cosine formula in the lecture’s original form.

To derive it, compare two expressions for the squared distance between endpoints.
Expanding the dot product gives

$$
\|\mathbf u-\mathbf v\|^2
=\|\mathbf u\|^2+\|\mathbf v\|^2-2\mathbf u^T\mathbf v.
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

For nonzero vectors, a positive dot product means an angle below $90^\circ$;
a negative one means an angle above $90^\circ$; zero means a right angle.
Parallel and opposite directions give the endpoint angles $0^\circ$ and $180^\circ$. The zero vector has zero dot product
with everything and is algebraically orthogonal to every vector, but has no
geometric direction or defined angle.

For the lecture's $\mathbf u=(3,4)^T$, $\mathbf v=(4,3)^T$, both norms
are 5 and their dot product is 24. Thus $\cos\theta=24/25$ and
$\theta=\arccos(24/25)\approx16.26^\circ$. This angle evaluation is an
application of the lecture's formula; the original slides calculate the dot product.

:::{admonition} Worked example · Similar totals, different directions
:class: example

For $\mathbf r=(3,1,3,1)^T$ and $\mathbf s=(1,3,1,3)^T$, the dot product is 12
and both norms are $\sqrt{20}$. Thus

$$\cos\theta=\frac{12}{20}=\frac35,\qquad
\theta=\arccos(3/5)\approx53.13^\circ.$$

Check: $\|\mathbf r-\mathbf s\|^2=16$, and
$20+20-2\cdot12=16$. The distance and dot-product calculations agree.
:::

```{figure} ../figures/lecture1/repeat-geometry.svg
:name: fig-w1-repeat-geometry
:alt: In orthonormal record coordinates q0=e/2 and q1=a/2, r has coordinates 4,2 and s has coordinates 4,-2. A horizontal uniform component of length 4 and a vertical alternating component of length 2 form a right triangle with squared hypotenuse length 20.

The geometry belongs to the **repeat records**. Orthonormal axes
$\mathbf q_0=\mathbf e/2$, $\mathbf q_1=\mathbf a/2$ preserve lengths and dot products
within this family. Thus r is plotted at $(4,2)$, not $(2,1)$.
```

**Machine-learning connection.** The normalized dot product is cosine similarity:
it compares direction without retaining magnitude. Changing feature units can
change a raw angle or norm, so coordinate scaling is a modeling decision.

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

:::{admonition} Carry these ideas forward
:class: key-result

A vector retains ordered coordinates. A linear combination asks what the chosen
directions can produce. A dot product returns a scalar; norms and angles turn that
comparison into geometry. State coordinate meanings and hypotheses before calculating.
:::

Next, [matrices and products](matrix-guide.md) organize several records and apply
several operations at once. Lecture source pages for this page: **1–34**;
{ref}`source notes <w1-source-notes>` explain attribution and added examples.
