(w1-practice)=
# Practice: from point measurements to fresh mathematics

<nav class="lecture-path" aria-label="Lecture 1 learning path">
<a href="index.html"><span class="path-number">01</span><span>Vectors &amp; geometry</span></a>
<a href="matrix-guide.html"><span class="path-number">02</span><span>Matrices &amp; products</span></a>
<a href="practice.html" aria-current="page"><span class="path-number">03</span><span>Exercises</span></a>
<a href="solutions.html"><span class="path-number">04</span><span>Solutions</span></a>
</nav>


Try each problem before opening its solution. The first group isolates the tools;
the second changes the examples; the final group mixes concepts and asks for
justification. Write dimensions and conditions, not only the final numbers.

The labels describe this chapter's practice progression, not official exam marks.
Use Problems 19–24 as an unaided mixed review after learning the individual methods.

## Foundations

(w1-p01)=
### 1. What does a vector record?

The X coordinates of four labeled beads are $(4,-1,2,3)^T$. Is this a vector in
$\mathbb R^4$? Does the negative entry invalidate a coordinate record? Does this
record determine the beads’ depths? Explain all three answers.

{ref}`Solution 1 <w1-s01>`

(w1-p02)=
### 2. Signed vector arithmetic

For $\mathbf u=(2,-1,3)^T$ and $\mathbf v=(-1,4,0)^T$, find $2\mathbf u-\mathbf v$.

{ref}`Solution 2 <w1-s02>`

(w1-p03)=
### 3. Profile coefficients

Using e and a from the chapter, express $(4,2,4,2)^T$ as $\alpha\mathbf e+\beta\mathbf a$.
Can $(4,2,3,2)^T$ be expressed that way? Give a reason.

{ref}`Solution 3 <w1-s03>`

(w1-p04)=
### 4. Dot product and angle

For $\mathbf u=(3,4)^T$, $\mathbf v=(4,3)^T$, find the dot product, both norms,
and the cosine of the angle. Is the angle acute, right, or obtuse?

{ref}`Solution 4 <w1-s04>`

(w1-p05)=
### 5. Normalize carefully

Normalize $\mathbf u=(-3,0,4)^T$. Find $\|-2\mathbf u\|$.
Explain why the same normalization procedure fails for the zero vector.

{ref}`Solution 5 <w1-s05>`

(w1-p06)=
### 6. Entries, transpose, and trace

For $A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$, give its shape, $a_{23}$,
and $A^T$. Is $\operatorname{tr}(A)$ defined under this chapter's convention?

{ref}`Solution 6 <w1-s06>`

(w1-p07)=
### 7. Entrywise matrix arithmetic

For $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and
$B=\begin{bmatrix}2&0\\-1&1\end{bmatrix}$, compute $A+B$ and $2A-B$.

{ref}`Solution 7 <w1-s07>`

(w1-p08)=
### 8. More than one label can apply

Classify each as diagonal, identity, symmetric, and/or skew-symmetric:

$$
D=\begin{bmatrix}2&0\\0&0\end{bmatrix},\quad
K=\begin{bmatrix}0&2\\-2&0\end{bmatrix},\quad
S=\begin{bmatrix}1&2\\2&3\end{bmatrix},\quad
Z=\begin{bmatrix}0&0\\0&0\end{bmatrix}.
$$

{ref}`Solution 8 <w1-s08>`

## Standard applications

(w1-p09)=
### 9. A plane membership test

For $\mathbf v=(1,1,0)^T$ and $\mathbf w=(0,1,1)^T$, decide whether
$(2,5,3)^T$ and $(2,4,3)^T$ are combinations of v,w. Find coefficients when possible.

{ref}`Solution 9 <w1-s09>`

(w1-p10)=
### 10. Two listed vectors, one direction

Characterize all $c,d\in\mathbb R$ satisfying
$c(1,2)^T+d(2,4)^T=(3,6)^T$. Could the same left side equal $(3,7)^T$?

{ref}`Solution 10 <w1-s10>`

(w1-p11)=
### 11. Check distributivity numerically

For $\mathbf u=(1,-2,3)^T$, $\mathbf v=(2,0,-1)^T$, $\mathbf w=(0,4,1)^T$,
compute $\mathbf u^T(\mathbf v+\mathbf w)$ directly and by distributing.

{ref}`Solution 11 <w1-s11>`

(w1-p12)=
### 12. Same total, perpendicular records

Let $\mathbf r=(2,0,2,0)^T$ and $\mathbf s=(0,2,0,2)^T$.
Find their totals, dot product, norms, distance, and angle. Explain why equal
totals do not determine the angle.

{ref}`Solution 12 <w1-s12>`

(w1-p13)=
### 13. Decide before multiplying

A has shape $2\times3$ and B has shape $3\times4$. Decide which exist and give
their shapes: AB, BA, $A^T B$, $B^T A^T$, $I_2A$, $AI_3$.
Is trace(AB) defined here?

{ref}`Solution 13 <w1-s13>`

(w1-p14)=
### 14. Both orders exist, with different shapes

Compute MN and NM for

$$M=\begin{bmatrix}2&1&-1\\0&3&2\end{bmatrix},\qquad
N=\begin{bmatrix}1&2\\0&-1\\2&1\end{bmatrix}.$$

Show a column-based check for one of the products.

{ref}`Solution 14 <w1-s14>`

(w1-p15)=
### 15. Two views of a new point

Use the stacked front/side map
$H=\begin{bmatrix}1&0&0\\0&1&0\\0&1&0\\0&0&1\end{bmatrix}$ and
$\mathbf p=(12,4,2)^T$. Compute Hp and identify each output entry.
Why must two entries agree? Do four readings make p a four-dimensional point?

{ref}`Solution 15 <w1-s15>`

(w1-p16)=
### 16. Group the point measurements

Let

$$R=\begin{bmatrix}2&1&2&1\\1&2&1&2\\3&0&3&0\end{bmatrix},\qquad
S=\begin{bmatrix}1&0\\1&0\\0&1\\0&1\end{bmatrix}.$$

Compute RS, $R\mathbf1_4$, and $R^T\mathbf1_3$, where $\mathbf1_n$ is the
n-entry all-ones column. Here R records three configurations (rows) of four
beads’ X coordinates (columns). Explain what the three results summarize.

{ref}`Solution 16 <w1-s16>`

(w1-p17)=
### 17. Use the definitions, not appearances

For $X=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, state the conditions for symmetry
and skew-symmetry. Which X are both?

{ref}`Solution 17 <w1-s17>`

(w1-p18)=
### 18. Construct a perpendicular direction

Find one nonzero vector orthogonal to $(2,-1,2)^T$ and normalize it. Explain
whether your answer is unique.

{ref}`Solution 18 <w1-s18>`

## Synthesis and exam-style reasoning

(w1-p19)=
### 19. What survives a summary?

Two configurations have X profiles r=(3,1,3,1) and s=(1,3,1,3). A summary keeps
only their coordinate sum. Show that their difference is invisible to that summary.
Does this establish identical front marks or identical three-dimensional positions?

:::{dropdown} Hint · Choose a first step

Write the total as one row multiplied by a column. Apply that row to the difference of the two records.
:::

{ref}`Solution 19 <w1-s19>`

(w1-p20)=
### 20. Refute a false product rule

For $U=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ and
$D=\begin{bmatrix}2&0\\0&1\end{bmatrix}$, compute UD and DU.
Explain why associativity does not permit swapping their order.

:::{dropdown} Hint · Choose a first step

Compute both orders. Associativity changes parentheses; ask whether it permits exchanging factors.
:::

{ref}`Solution 20 <w1-s20>`

(w1-p21)=
### 21. Refute two tempting norm rules

Use $\mathbf u=(1,0)^T$, $\mathbf v=(0,1)^T$ to test
$\|\mathbf u+\mathbf v\|=\|\mathbf u\|+\|\mathbf v\|$ and
$\widehat{\mathbf u+\mathbf v}=\widehat{\mathbf u}+\widehat{\mathbf v}$.
State the actual results and check their lengths.

:::{dropdown} Hint · Choose a first step

Choose the two coordinate unit vectors in two dimensions. Compare both lengths and both resulting vectors.
:::

{ref}`Solution 21 <w1-s21>`

(w1-p22)=
### 22. Split symmetry from skew-symmetry

For $M=\begin{bmatrix}2&5\\-1&4\end{bmatrix}$, compute
$S=(M+M^T)/2$, $K=(M-M^T)/2$. Verify $S^T=S$, $K^T=-K$, and $M=S+K$.
Explain why the same formulas work for every real square matrix.

:::{dropdown} Hint · Choose a first step

Use the entrywise formulas first. For the general claim, transpose each definition and simplify.
:::

{ref}`Solution 22 <w1-s22>`

(w1-p23)=
### 23. Same trace does not mean same product

For $A\in\mathbb R^{m\times n}$ and $B\in\mathbb R^{n\times m}$,
prove $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ using finite sums.
Does that imply $AB=BA$? Use Problem 14 to check.

:::{dropdown} Hint · Choose a first step

Expand the diagonal entries of each product as finite sums, then compare the two double sums.
:::

{ref}`Solution 23 <w1-s23>`

(w1-p24)=
### 24. Mixed task, no craft vocabulary

Let $A=\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}$ and $\mathbf x=(2,-1,3)^T$.

1. Compute y=Ax and normalize y.
2. Give a different input $\mathbf x'$ with $A\mathbf x'=\mathbf y$, and verify it.
3. Compute $A^T A$ and $AA^T$, stating their dimensions and symmetry.
4. What can you conclude about uniqueness from your answer to part 2? Does a
   correct output imply a unique input?

:::{dropdown} Hint · Choose a first step

Compute the output first. Look for a nonzero change in the input that changes neither output entry.
:::

{ref}`Solution 24 <w1-s24>`
