(w1-geometry-page)=
# Dot products and geometry

<div class="chapter-kicker">Lecture 1 · Page 2 of 4 · Compare direction and length</div>

The previous page built vectors from simpler directions. Now compare those vectors:
measure how they align, how long they are, and the angle between them.

<nav class="lecture-path" aria-label="Lecture 1 learning path">
<a href="index.html"><span class="path-number">01</span><span>Vectors & combinations</span></a>
<a href="geometry.html" aria-current="page"><span class="path-number">02</span><span>Dot products & geometry</span></a>
<a href="matrix-guide.html"><span class="path-number">03</span><span>Matrices & products</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## Before you begin

Use the signed vector arithmetic from {ref}`Page 1 <w1-vector-arithmetic>`.
You will compute dot products, norms, unit vectors, and angles, stating when each
formula is defined.

::::{div} page-roadmap

**On this page**

- {ref}`1.4 · Dot products <w1-geometry>`
- {ref}`1.5 · Norms and unit vectors <w1-norms>`
- {ref}`1.6 · Angles <w1-angles>`
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

(w1-practice-geometry)=
## Practice · dot products, lengths, and angles

Try each problem before opening its explained answer directly below. Problem numbers
remain stable across the chapter; the questions here follow this page’s topics.

```{include} practice.md
:start-after: <!-- geometry:start -->
:end-before: <!-- geometry:end -->
```
