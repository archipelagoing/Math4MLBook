(w1-vectors)=
# Vectors: a record with an order

## Start with the entries, not the brackets

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

## A record is a choice

The same row can be recorded at several levels:

| Record | Entries | What it loses |
| --- | --- | --- |
| Whole-row pink total | $8$ | Which sections contain those stitches |
| Pink counts by section | $(3,1,3,1)^T$ | Their order inside each six-stitch section |
| Stitch-by-stitch color chart | 24 labeled color choices | Tension, yarn path, thickness, and other physical properties |

This is a mathematical habit worth keeping: **state what each coordinate means
before calculating**. Equal records need not establish equal physical objects.
The second motif, $(1,3,1,3)^T$, has the same total but a different section record.

The lecture also uses a house represented by bedroom count, bathroom count,
floors, construction year, and price. Those entries are all numbers, but their
units and meanings differ. Later, a raw Euclidean distance between such records
would need a reasoned choice of scaling. Brackets alone do not make unlike units
comparable.

## Algebraic and geometric views

In $\mathbb R^2$, the vector $(a,b)^T$ can be drawn as an arrow from the origin
to the point $(a,b)$. Its components are displacement along two coordinate axes.
The same displacement can be drawn from another starting point; its coordinates
still describe the change, not the arrow's absolute location.

For the sampler, the four coordinates are **section counts**, not four spatial
axes of the cloth. We can still use the geometry of $\mathbb R^4$ to compare
these records, provided that we say what metric we are using. Later we will find
a two-dimensional family of repeats and draw its coordinate geometry without
pretending that the fabric itself lives on that plot.

A simple two-coordinate craft record might count knit and purl operations:
$\mathbf k=(2,2)^T$ records one `k2,p2` repeat. It does not encode their order:
`k,p,k,p` gives the same count vector. An ordered chart is a richer record.

## Adding compatible vectors

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

## Differences describe changes

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

## Scalar multiplication

For a real scalar $c$,

$$c\mathbf v=(cv_1,\ldots,cv_n)^T.$$

Six repetitions of the knit/purl count $(2,2)^T$ give $(12,12)^T$: 24 operations.
Scaling a geometric vector by positive $c$ changes its length by $c$ and preserves
its direction; negative $c$ reverses direction, with length scaled by $|c|$.
Multiplication by zero gives the zero vector.

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

## Useful algebraic rules

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
