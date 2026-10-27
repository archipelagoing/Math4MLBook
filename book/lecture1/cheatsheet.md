(w1-cheatsheet)=
# TL;DR cheat sheet

<div class="chapter-kicker">Lecture 1 · Page 4 of 4 · Review after the lecture</div>

Choose the operation, check its conditions, calculate, then interpret the result.
The first three pages teach the concepts in lecture order; their practice and
expandable answers stay with each topic.

<nav class="lecture-path" aria-label="Lecture 1 learning path">
<a href="index.html"><span class="path-number">01</span><span>Vectors & combinations</span></a>
<a href="geometry.html"><span class="path-number">02</span><span>Dot products & geometry</span></a>
<a href="matrix-guide.html"><span class="path-number">03</span><span>Matrices & products</span></a>
<a href="cheatsheet.html" aria-current="page"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## 1 · Vectors and combinations

:::{admonition} Match coordinates before calculating
:class: key-result

$$\mathbf u+\mathbf v=(u_i+v_i)_i,\qquad c\mathbf u=(cu_i)_i,\qquad
\mathbf b=c_1\mathbf v_1+\cdots+c_k\mathbf v_k.$$

To test a combination: write its general coordinates, equate them to the target,
solve the coefficient equations, then check **every** coordinate. Vectors must
have compatible dimensions and coordinate meanings.
:::

## 2 · Dot product, norm, unit vector, angle

| Task | Formula | Condition or check |
| --- | --- | --- |
| Dot product | $\mathbf u^T\mathbf v=\sum_i u_iv_i$ | Matching dimensions; scalar output |
| Length / magnitude / norm | $\lVert\mathbf v\rVert=\sqrt{\sum_i v_i^2}$ | Nonnegative |
| Unit vector | $\widehat{\mathbf v}=\mathbf v/\lVert\mathbf v\rVert$ | $\mathbf v\ne0$; check length 1 |
| Distance | $\lVert\mathbf u-\mathbf v\rVert$ | Subtract before taking length |
| Angle | $\theta=\arccos\big(\mathbf u^T\mathbf v/(\lVert\mathbf u\rVert\lVert\mathbf v\rVert)\big)$ | Both nonzero; cosine in $[-1,1]$ |
| Orthogonality | $\mathbf u^T\mathbf v=0$ | A right angle requires nonzero vectors |

The cosine formula is $\mathbf u^T\mathbf v=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta$.
A positive dot product means an acute angle; a negative one means obtuse, for nonzero vectors.

:::::{admonition} Worked review · Compare two vectors
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Multiply matching entries and add</span>

For $\mathbf u=(3,4)^T$, $\mathbf v=(4,3)^T$,
$\mathbf u^T\mathbf v=3(4)+4(3)=24$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find both lengths and normalize</span>

Both lengths are $\sqrt{3^2+4^2}=5$, so
$\widehat{\mathbf u}=(3/5,4/5)^T$. Check: $(3/5)^2+(4/5)^2=1$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Divide before taking arccos</span>

$\cos\theta=24/(5\cdot5)=24/25$, hence $\theta=\arccos(24/25)$,
about $16.26^\circ$. The cosine is valid and positive: the angle is acute.
::::

::::{div} key-answer

**Keep this result:** The dot product is 24; the cosine is $24/25$. They are different quantities.
::::
:::::

## 3 · Matrices and products

| Task | Formula / method | Condition |
| --- | --- | --- |
| Addition / scaling | $(A+B)_{ij}=a_{ij}+b_{ij}$; $(cA)_{ij}=ca_{ij}$ | Same shapes for addition |
| Transpose | $(A^T)_{ij}=a_{ji}$ | Swap row/column roles |
| Trace | $\operatorname{tr}(A)=\sum_i a_{ii}$ | Square matrix here |
| Matrix-vector product | $(A\mathbf x)_i=\sum_j a_{ij}x_j$ | Columns of A = entries of x |
| Matrix product | $(AB)_{ij}=\sum_k a_{ik}b_{kj}$ | $(m\times n)(n\times p)$ gives $m\times p$ |

Diagonal matrices have zeros off the diagonal. $I$ has diagonal ones and acts as
identity. Symmetry means $A^T=A$; skew-symmetry means $A^T=-A$.

:::{admonition} Product rules to retain
:class: key-result

$$A(BC)=(AB)C,\quad A(B+C)=AB+AC,\quad (A+B)C=AC+BC,$$
$$(AB)^T=B^TA^T,\qquad A\mathbf x=\sum_j x_j\mathbf a_j.$$

**Product recipe:** check dimensions → dot each left row with each right column
→ record the output shape → check one entry independently. Keep factor order.
:::

:::{admonition} Common errors
:class: pitfall

Do not divide by the zero vector's length, assume $AB=BA$, or add incompatible
shapes. Associativity changes parentheses, not order. A summary of shadow
measurements may lose information; equal totals do not prove equal records.
:::

**Practice by topic:** {ref}`vectors <w1-practice-vectors>`,
{ref}`geometry <w1-practice-geometry>`, {ref}`matrices <w1-practice-matrices>`.
