<!-- Included answers; not a standalone reader page. -->

<!-- answer-01:start -->
(w1-s01)=
:::{dropdown} Explained solution 1 · 1. A negative coordinate is a valid position

$(4,-1,2,3)^T$ is a vector in $\mathbb R^4$: it lists four real X coordinates.
The second bead is one unit left of the reference origin. The four entries refer to four beads, not four spatial axes of
one bead. Their depths are absent, so changing Z alone need not change this record.
Revisit {ref}`vectors and interpretation <w1-vectors>` if the coordinate meanings
were confused with the number of physical dimensions.

**Review and retry:** {ref}`Revisit the method <w1-vectors>`, then try {ref}`Problem 19 <w1-p19>` unaided.
:::
<!-- answer-01:end -->

<!-- answer-02:start -->
(w1-s02)=
:::{dropdown} Explained solution 2 · 2. Keep the subtraction signs

$$2\mathbf u-\mathbf v=(4,-2,6)^T-(-1,4,0)^T=(5,-6,6)^T.$$

Check the first entry: $4-(-1)=5$. A common error is to subtract only the positive
entries of v. Apply the operation to every matching coordinate.

**Review and retry:** {ref}`Revisit the method <w1-vector-arithmetic>`, then try {ref}`Problem 21 <w1-p21>` unaided.
:::
<!-- answer-02:end -->

<!-- answer-03:start -->
(w1-s03)=
:::{dropdown} Explained solution 3 · 3. Use the repeated-coordinate structure

A combination of e,a has coordinates $(\alpha+\beta,\alpha-\beta,
\alpha+\beta,\alpha-\beta)^T$. For $(4,2,4,2)^T$, the equations give
$\alpha=3$, $\beta=1$. Substitution verifies every entry.
For $(4,2,3,2)^T$, coordinates 1 and 3 differ, contradicting the structural form.
No coefficients work. Revisit {ref}`general combinations <w1-combinations>` rather
than trying endless numerical guesses.

**Review and retry:** {ref}`Revisit the method <w1-combinations>`, then try {ref}`Problem 9 <w1-p09>` unaided.
:::
<!-- answer-03:end -->

<!-- answer-04:start -->
(w1-s04)=
:::{dropdown} Explained solution 4 · 4. Normalize the comparison, not the answer's sign

$\mathbf u^T\mathbf v=24$, $\|\mathbf u\|=\|\mathbf v\|=5$, so
$\cos\theta=24/25>0$: the angle is acute, approximately $16.26^\circ$.
A raw dot product of 24 is not a cosine; divide by the product of lengths.
The cosine must lie between −1 and 1 for nonzero real Euclidean vectors.

**Review and retry:** {ref}`Revisit the method <w1-angles>`, then try {ref}`Problem 12 <w1-p12>` unaided.
:::
<!-- answer-04:end -->

<!-- answer-05:start -->
(w1-s05)=
:::{dropdown} Explained solution 5 · 5. The scale factor uses the positive norm

$\|\mathbf u\|=\sqrt{9+16}=5$, so
$\widehat{\mathbf u}=(-3/5,0,4/5)^T$ and $\|-2\mathbf u\|=2\cdot5=10$.
Check the unit length: $9/25+16/25=1$. Zero's norm is zero, so normalization would
divide by zero; it has no unit direction. Revisit {ref}`norms <w1-norms>` if the
negative multiplier produced a negative length.

**Review and retry:** {ref}`Revisit the method <w1-norms>`, then try {ref}`Problem 18 <w1-p18>` unaided.
:::
<!-- answer-05:end -->

<!-- answer-06:start -->
(w1-s06)=
:::{dropdown} Explained solution 6 · 6. Follow each entry's index

A is $2\times3$, $a_{23}=6$, and

$$A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}\in\mathbb R^{3\times2}.$$

Trace is not defined for this rectangular A under the chapter's convention.
Adding $1+5$ would silently change that convention. Revisit {ref}`matrix definitions <w1-matrices>`.

**Review and retry:** {ref}`Revisit the method <w1-transpose-trace>`, then try {ref}`Problem 13 <w1-p13>` unaided.
:::
<!-- answer-06:end -->

<!-- answer-07:start -->
(w1-s07)=
:::{dropdown} Explained solution 7 · 7. Entrywise arithmetic

$$A+B=\begin{bmatrix}3&2\\2&5\end{bmatrix},\qquad
2A-B=\begin{bmatrix}0&4\\7&7\end{bmatrix}.$$

Each position is independent. The lower-left entry in the second result is
$6-(-1)=7$. This is not a matrix product; no row-by-column summation is involved.

**Review and retry:** {ref}`Revisit the method <w1-matrix-arithmetic>`, then try {ref}`Problem 22 <w1-p22>` unaided.
:::
<!-- answer-07:end -->

<!-- answer-08:start -->
(w1-s08)=
:::{dropdown} Explained solution 8 · 8. Definitions can overlap

D is diagonal and symmetric; it is neither identity nor skew-symmetric.
K is skew-symmetric, but neither diagonal, identity, nor symmetric.
S is symmetric, but neither diagonal, identity, nor skew-symmetric.
Z is diagonal, symmetric, and skew-symmetric, but not the $2\times2$ identity.
Indeed $Z^T=Z=-Z$. A definition does not require that its label exclude all others.

**Review and retry:** {ref}`Revisit the method <w1-special-matrices>`, then try {ref}`Problem 17 <w1-p17>` unaided.
:::
<!-- answer-08:end -->

<!-- answer-09:start -->
(w1-s09)=
:::{dropdown} Explained solution 9 · 9. Compare the target with the general form

$c\mathbf v+d\mathbf w=(c,c+d,d)^T$, so membership requires $y=x+z$.
For $(2,5,3)^T$, choose c=2,d=3; the middle coordinate is $2+3=5$.
For $(2,4,3)^T$, the required middle coordinate would be 5, not 4.
State both the coefficients for the successful case and the obstruction for the
failed one. {ref}`The plane example <w1-combinations>` shows why the condition is sufficient.

**Review and retry:** {ref}`Revisit the method <w1-combinations>`, then try {ref}`Problem 10 <w1-p10>` unaided.
:::
<!-- answer-09:end -->

<!-- answer-10:start -->
(w1-s10)=
:::{dropdown} Explained solution 10 · 10. The second direction is redundant

Because $(2,4)^T=2(1,2)^T$, the left side is $(c+2d)(1,2)^T$.
The target $(3,6)^T$ requires $c+2d=3$, giving all pairs
$(c,d)=(3-2t,t)$ for real t. The target $(3,7)^T$ is impossible because its second
entry is not twice its first. Two listed vectors need not give two different directions.

**Review and retry:** {ref}`Revisit the method <w1-combinations>`, then try {ref}`Problem 9 <w1-p09>` unaided.
:::
<!-- answer-10:end -->

<!-- answer-11:start -->
(w1-s11)=
:::{dropdown} Explained solution 11 · 11. Two computations of the same scalar

Directly, $\mathbf v+\mathbf w=(2,4,0)^T$, so
$\mathbf u^T(\mathbf v+\mathbf w)=2-8+0=-6$.
Separately, $\mathbf u^T\mathbf v=2+0-3=-1$ and
$\mathbf u^T\mathbf w=0-8+3=-5$. Their sum is −6.
This numerical check illustrates the identity; its general justification follows
from distributing real-number multiplication inside the finite sum.

**Review and retry:** {ref}`Revisit the method <w1-geometry>`, then try {ref}`Problem 4 <w1-p04>` unaided.
:::
<!-- answer-11:end -->

<!-- answer-12:start -->
(w1-s12)=
:::{dropdown} Explained solution 12 · 12. A total does not determine geometry

Both totals are 4. The dot product is 0 because no position has nonzero entries
in both vectors. Both norms are $\sqrt8=2\sqrt2$.
The difference is $(2,-2,2,-2)^T$ with norm 4; both vectors are nonzero and
perpendicular, so their angle is $90^\circ$.
The check $8+8-2\cdot0=16$ agrees with the squared distance.
Equal totals are only one scalar constraint, not a complete comparison of directions.

**Review and retry:** {ref}`Revisit the method <w1-angles>`, then try {ref}`Problem 4 <w1-p04>` unaided.
:::
<!-- answer-12:end -->

<!-- answer-13:start -->
(w1-s13)=
:::{dropdown} Explained solution 13 · 13. Shapes settle the question

AB exists and is $2\times4$; BA and $A^TB$ are undefined because their inner sizes
are respectively 4 versus 2, and 2 versus 3. $B^TA^T$ exists and is $4\times2$.
Both $I_2A$ and $AI_3$ exist and equal A, with shape $2\times3$.
AB is rectangular, so its trace is not defined here.
Revisit the {ref}`shape rule <w1-matrix-products>` before attempting numerical multiplication.

**Review and retry:** {ref}`Revisit the method <w1-matrix-products>`, then try {ref}`Problem 14 <w1-p14>` unaided.
:::
<!-- answer-13:end -->

<!-- answer-14:start -->
(w1-s14)=
:::{dropdown} Explained solution 14 · 14. Compute and interpret by columns

$$MN=\begin{bmatrix}0&2\\4&-1\end{bmatrix},\qquad
NM=\begin{bmatrix}2&7&3\\0&-3&-2\\4&5&0\end{bmatrix}.$$

For example, $(MN)_{12}=2\cdot2+1(-1)+(-1)\cdot1=2$.
The first N column is $(1,0,2)^T$, so the first MN column must be
$1(2,0)^T+0(1,3)^T+2(-1,2)^T=(0,4)^T$, matching the result.
Both orders exist; their shapes differ, so they cannot be equal matrices.

**Review and retry:** {ref}`Revisit the method <w1-matrix-products>`, then try {ref}`Problem 16 <w1-p16>` unaided.
:::
<!-- answer-14:end -->

<!-- answer-15:start -->
(w1-s15)=
:::{dropdown} Explained solution 15 · 15. Keep the views' coordinate labels

$$H\mathbf p=(12,4,4,2)^T.$$

The first two entries are front X,Y; the last two are side Y,Z. Entries 2 and 3
agree because both read the same Y=4. The input is still a point in $\mathbb R^3$;
the output is a four-entry measurement record. More entries do not by themselves
mean more physical dimensions or independent information. Revisit the
{ref}`column interpretation <w1-products>` if the input/output roles were swapped.

**Review and retry:** {ref}`Revisit the method <w1-products>`, then try {ref}`Problem 24 <w1-p24>` unaided.
:::
<!-- answer-15:end -->

<!-- answer-16:start -->
(w1-s16)=
:::{dropdown} Explained solution 16 · 16. Several summaries of one matrix

$$RS=\begin{bmatrix}3&3\\3&3\\3&3\end{bmatrix},\qquad
R\mathbf1_4=\begin{bmatrix}6\\6\\6\end{bmatrix},\qquad
R^T\mathbf1_3=\begin{bmatrix}6\\3\\6\\3\end{bmatrix}.$$

RS groups the A/B and C/D bead coordinates within each configuration.
$R\mathbf1_4$ sums X across beads in each configuration; $R^T\mathbf1_3$ sums
each bead’s X across configurations. The whole-table sum is 18 either way.
Grouping discards distinctions between individual point readings.

**Review and retry:** {ref}`Revisit the method <w1-matrix-products>`, then try {ref}`Problem 19 <w1-p19>` unaided.
:::
<!-- answer-16:end -->

<!-- answer-17:start -->
(w1-s17)=
:::{dropdown} Explained solution 17 · 17. Compare every corresponding entry

Symmetry requires $b=c$, with a,d arbitrary. Skew-symmetry requires
$a=d=0$ and $c=-b$. A matrix satisfying both has b=c and c=−b, so b=c=0;
the diagonal is also zero. Thus only the zero matrix is both over the reals.
Do not infer skew-symmetry from zero trace or zero diagonal alone.

**Review and retry:** {ref}`Revisit the method <w1-special-matrices>`, then try {ref}`Problem 22 <w1-p22>` unaided.
:::
<!-- answer-17:end -->

<!-- answer-18:start -->
(w1-s18)=
:::{dropdown} Explained solution 18 · 18. One construction, many possible answers

Choose $\mathbf w=(1,0,-1)^T$. Its dot product with $(2,-1,2)^T$ is $2-2=0$,
and its norm is $\sqrt2$. A unit choice is $(1,0,-1)^T/\sqrt2$.
There are many others: the requirement is $2w_1-w_2+2w_3=0$, or
$w_2=2w_1+2w_3$. Nonzero choices of the free coordinates give other directions.
A single example answers the construction request; it does not prove uniqueness.

**Review and retry:** {ref}`Revisit the method <w1-norms>`, then try {ref}`Problem 12 <w1-p12>` unaided.
:::
<!-- answer-18:end -->

<!-- answer-19:start -->
(w1-s19)=
:::{dropdown} Explained solution 19 · 19. An unchanged record need not mean an unchanged object

The coordinate-sum map is $J=[1\ 1\ 1\ 1]$. It returns 8 for both profiles.
For $\mathbf d=\mathbf s-\mathbf r=(-2,2,-2,2)^T$, $J\mathbf d=0$.
The nonzero difference does not change the sum, but it changes every bead’s X
coordinate. Thus the front marks differ despite equal summaries. Neither X
profile supplies depth. Here J hides horizontal redistributions; O hides changes
in Z. The map decides which differences become invisible. Later we call these
invisible input directions a null space.

**Review and retry:** {ref}`Revisit the method <w1-products>`, then try {ref}`Problem 24 <w1-p24>` unaided.
:::
<!-- answer-19:end -->

<!-- answer-20:start -->
(w1-s20)=
:::{dropdown} Explained solution 20 · 20. Associativity preserves order

$$UD=\begin{bmatrix}2&1\\0&1\end{bmatrix},\qquad
DU=\begin{bmatrix}2&2\\0&1\end{bmatrix}.$$

They differ in the upper-right entry. Associativity changes parentheses in a
three-factor product, $(AB)C=A(BC)$; it does not exchange factors.
A single counterexample refutes a universal commutativity claim.

**Review and retry:** {ref}`Revisit the method <w1-matrix-products>`, then try {ref}`Problem 14 <w1-p14>` unaided.
:::
<!-- answer-20:end -->

<!-- answer-21:start -->
(w1-s21)=
:::{dropdown} Explained solution 21 · 21. Normalization is not distributive

$\|\mathbf u+\mathbf v\|=\sqrt2$, while $\|\mathbf u\|+\|\mathbf v\|=2$.
The normalized sum is $(1,1)^T/\sqrt2$, of length 1. The sum of normalized vectors
is $(1,1)^T$, of length $\sqrt2$. They are different vectors.
Computing the output's length is a quick way to catch an alleged unit vector
that has not actually been normalized.

**Review and retry:** {ref}`Revisit the method <w1-norms>`, then try {ref}`Problem 5 <w1-p05>` unaided.
:::
<!-- answer-21:end -->

<!-- answer-22:start -->
(w1-s22)=
:::{dropdown} Explained solution 22 · 22. The transpose identifies the two parts

$$S=\begin{bmatrix}2&2\\2&4\end{bmatrix},\qquad
K=\begin{bmatrix}0&3\\-3&0\end{bmatrix},\qquad S+K=M.$$

For general square M, transposing the sum gives
$S^T=(M^T+M)/2=S$; transposing the difference gives
$K^T=(M^T-M)/2=-K$. Adding the two definitions returns M.
This exercise extends the lecture's definitions using only its transpose and
entrywise operations; it does not claim a new physical motion of the point frame.

**Review and retry:** {ref}`Revisit the method <w1-transpose-trace>`, then try {ref}`Problem 17 <w1-p17>` unaided.
:::
<!-- answer-22:end -->

<!-- answer-23:start -->
(w1-s23)=
:::{dropdown} Explained solution 23 · 23. Trace equality is weaker than matrix equality

Both products are square, although they may have different sizes:

$$
\operatorname{tr}(AB)=\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}b_{ji}
=\sum_{j=1}^{n}\sum_{i=1}^{m}b_{ji}a_{ij}
=\operatorname{tr}(BA).
$$

We changed the order of finite summation and commuted scalar products, not the
matrices. In Problem 14, trace(MN)=−1 and trace(NM)=$2-3+0=-1$, but the matrices
have different shapes and are not equal. An equal summary does not establish
equal objects—a familiar theme from incomplete observations.

**Review and retry:** {ref}`Revisit the method <w1-transpose-trace>`, then try {ref}`Problem 6 <w1-p06>` unaided.
:::
<!-- answer-23:end -->

<!-- answer-24:start -->
(w1-s24)=
:::{dropdown} Explained solution 24 · 24. One output, two verified inputs

1. $\mathbf y=(5,2)^T$, with norm $\sqrt{29}$ and unit direction
   $(5,2)^T/\sqrt{29}$.
2. Take $\mathbf x'=(1,-2,4)^T$. Then $A\mathbf x'=(1+4,-2+4)^T=(5,2)^T$.
   The difference $\mathbf x'-\mathbf x=(-1,-1,1)^T$ maps to zero.
3. The products are

   $$
   A^T A=\begin{bmatrix}1&0&1\\0&1&1\\1&1&2\end{bmatrix}\in\mathbb R^{3\times3},
   \qquad
   AA^T=\begin{bmatrix}2&1\\1&2\end{bmatrix}\in\mathbb R^{2\times2}.
   $$

   Both are symmetric; their entries or the reversed-order transpose identity
   verify this. Their shapes differ because their coordinate roles differ.
4. The input is not unique: two distinct verified inputs already disprove
   uniqueness. Correct output arithmetic alone cannot establish that there was
   only one possible input.

This final task brings together the chapter's main habits: state shapes, compute,
normalize only nonzero records, compare definitions, and test conclusions by
substitution rather than by the appeal of an analogy.

**Review and retry:** {ref}`Revisit the method <w1-products>`, then try {ref}`Problem 19 <w1-p19>` unaided.
:::
<!-- answer-24:end -->
