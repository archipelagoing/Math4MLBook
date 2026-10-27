(w1-combinations)=
# Linear combinations: what can a repeat produce?

Addition and scalar multiplication become much more useful together. They let
us describe an entire family of records with a few directions and adjustable
coefficients. The important question is no longer just “what is this vector?”
but “which vectors can these ingredients produce?”

## Separate a baseline from an alternating contrast

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

## One direction makes a line

All scalar multiples $c\mathbf u$ of one **nonzero** vector form a line through
the origin. If $\mathbf u=\mathbf 0$, the only result is the zero vector; there
is no nonzero direction to follow.

The lecture illustrates multiples of $(1,2,4)^T$ in three-dimensional space.
Although the vector has three entries, its multiples have only one freely
adjustable coefficient. They lie on a line, not throughout $\mathbb R^3$.
The number of entries and the number of genuinely different directions available
are different ideas. We will formalize the latter in Week 3.

## Two directions: a line or a plane?

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

## The lecture's plane example, fully worked

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

## Adding a third vector does not guarantee all of space

Three vectors in $\mathbb R^3$ fill all of space only when none of their
necessary directions is redundant. A third vector already in the plane adds no
new reachable direction. A vector outside the plane adds one.

For example, the vector $(1,2,3)^T$ above is outside $y=x+z$, so it supplies a
new direction beyond v and w. We will give exact tests using pivots, rank, and
independence later. For now, remember the qualification: counting vectors alone
does not determine how much of the ambient space their combinations cover.

## A craft action with a count vector

Let a plain operation consume one old stitch and produce one new stitch.
A single increase consumes one and produces two. Their count columns are

$$
\mathbf p=\begin{bmatrix}1\\1\end{bmatrix},\qquad
\mathbf i=\begin{bmatrix}1\\2\end{bmatrix},
$$

where the entries mean **consumed, produced**. Eighteen plain operations and six
increases give

$$
18\mathbf p+6\mathbf i=\begin{bmatrix}24\\30\end{bmatrix}.
$$

For selected knitting operations these can be `k1` and `kfb`; for crochet, sc
and two sc in the next stitch. `(k3,kfb)` or `(3 sc,inc)` repeated six times has
those totals. The counts agree across the two crafts; the resulting structures
are not asserted identical. Placement and technique still matter.

This is already a linear combination. Later, placing p and i into a matrix
will make the same calculation a matrix-vector product.

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

## Looking toward machine learning

A model often describes a complicated record as a weighted sum of simpler
patterns. Its coefficients may represent contributions of features or templates.
The mathematics is the same as combining repeat directions; whether the templates
are useful depends on the record and task. The later chapters will distinguish
spanning, choosing a basis, and approximating a target that the available directions
cannot produce exactly.
