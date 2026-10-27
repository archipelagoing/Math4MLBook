(w1-geometry)=
# Dot products, lengths, and angles

Two repeat records can have the same total and still differ in every section.
A useful comparison should say more than “the entries add to eight.” The dot
product gives us one scalar comparison, and from it we can define Euclidean
length, distance, and angle.

## The dot product returns a scalar

:::{admonition} Definition · Euclidean dot product
:class: definition

For $\mathbf u,\mathbf v\in\mathbb R^n$,

```{math}
:label: eq-w1-dot
\mathbf u\cdot\mathbf v=\mathbf u^T\mathbf v
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

## Properties and a common misuse

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

## Length from a vector's self-comparison

:::{admonition} Definition · Euclidean norm and distance
:class: definition

$$
\|\mathbf v\|=\sqrt{\mathbf v^T\mathbf v}=\sqrt{\sum_i v_i^2},
\qquad
\operatorname{dist}(\mathbf u,\mathbf v)=\|\mathbf u-\mathbf v\|.
$$

The Euclidean norm is the nonnegative square root. In particular,
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

## Normalize a direction, with its hypothesis

For $\mathbf v\ne\mathbf0$, define

$$\widehat{\mathbf v}=\frac{\mathbf v}{\|\mathbf v\|}.$$

Its norm is $\|\mathbf v\|/\|\mathbf v\|=1$, and the positive scaling preserves
direction. The lecture normalizes $(3,4)^T$ to $(3/5,4/5)^T$.
Our record $\mathbf r$ normalizes to $(3,1,3,1)^T/(2\sqrt5)$.

:::{admonition} Common pitfall · Unit direction is not a stitch instruction
:class: pitfall

You cannot normalize the zero vector: division by its norm would divide by zero.
A normalized count record usually has fractional entries; it describes a direction
in the record space, not an executable row of fractional stitches.
:::

## Orthogonality of actual repeat records

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

## The cosine formula and where it comes from

For nonzero vectors, the Euclidean angle $\theta\in[0,\pi]$ satisfies

```{math}
:label: eq-w1-cosine
\cos\theta=\frac{\mathbf u^T\mathbf v}{\|\mathbf u\|\|\mathbf v\|}.
```

To derive it, compare two expressions for the squared distance between endpoints.
Expanding the dot product gives

$$
\|\mathbf u-\mathbf v\|^2
=\|\mathbf u\|^2+\|\mathbf v\|^2-2\mathbf u^T\mathbf v.
$$

The cosine rule applied to the triangle gives

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

## A short machine-learning connection

Normalized dot products compare directions without retaining overall magnitude.
For nonzero records, cosine similarity is the right-hand side of
{eq}`eq-w1-cosine`. Equal directions can have different lengths. A model might
care about direction, magnitude, or both; choosing one is a modeling decision.

Feature units also matter. Our section counts have matching units and equal
section widths. In a record combining construction year and price, changing
price from dollars to thousands of dollars changes the raw norm and angle.
Do not interpret an unscaled dot product as universal semantic similarity.

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
