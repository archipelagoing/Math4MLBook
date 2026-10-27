(w1-solutions)=
# Explained solutions and targeted revision

Use these after attempting the [practice](practice.md). When a result differs,
identify whether the issue was the chosen operation, a missing condition, a shape
mismatch, arithmetic, or interpretation. Redo the question with the answer covered,
then try a fresh related problem. Familiarity with a worked solution is not yet
independent performance.

## Foundations

(w1-s01)=
### 1. Real coordinates versus feasible counts

$(4,-1,2,3)^T$ is a vector in $\mathbb R^4$: all four entries are real numbers.
It is not an actual four-section pink-count row because the second count is negative.
As a **change** from another row, a negative entry could be meaningful. The record's
domain must be stated. Revisit {ref}`vectors and interpretation <w1-vectors>` if you
classified the algebraic vector as invalid merely because it is not executable.

(w1-s02)=
### 2. Keep the subtraction signs

$$2\mathbf u-\mathbf v=(4,-2,6)^T-(-1,4,0)^T=(5,-6,6)^T.$$

Check the first entry: $4-(-1)=5$. A common error is to subtract only the positive
entries of v. Apply the operation to every matching coordinate.

(w1-s03)=
### 3. Use the repeated-coordinate structure

A combination of e,a has coordinates $(\alpha+\beta,\alpha-\beta,
\alpha+\beta,\alpha-\beta)^T$. For $(4,2,4,2)^T$, the equations give
$\alpha=3$, $\beta=1$. Substitution verifies every entry.
For $(4,2,3,2)^T$, coordinates 1 and 3 differ, contradicting the structural form.
No coefficients work. Revisit {ref}`general combinations <w1-combinations>` rather
than trying endless numerical guesses.

(w1-s04)=
### 4. Normalize the comparison, not the answer's sign

$\mathbf u^T\mathbf v=24$, $\|\mathbf u\|=\|\mathbf v\|=5$, so
$\cos\theta=24/25>0$: the angle is acute, approximately $16.26^\circ$.
A raw dot product of 24 is not a cosine; divide by the product of lengths.
The cosine must lie between −1 and 1 for nonzero real Euclidean vectors.

(w1-s05)=
### 5. The scale factor uses the positive norm

$\|\mathbf u\|=\sqrt{9+16}=5$, so
$\widehat{\mathbf u}=(-3/5,0,4/5)^T$ and $\|-2\mathbf u\|=2\cdot5=10$.
Check the unit length: $9/25+16/25=1$. Zero's norm is zero, so normalization would
divide by zero; it has no unit direction. Revisit {ref}`norms <w1-geometry>` if the
negative multiplier produced a negative length.

(w1-s06)=
### 6. Follow each entry's index

A is $2\times3$, $a_{23}=6$, and

$$A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}\in\mathbb R^{3\times2}.$$

Trace is not defined for this rectangular A under the chapter's convention.
Adding $1+5$ would silently change that convention. Revisit {ref}`matrix definitions <w1-matrices>`.

(w1-s07)=
### 7. Entrywise arithmetic

$$A+B=\begin{bmatrix}3&2\\2&5\end{bmatrix},\qquad
2A-B=\begin{bmatrix}0&4\\7&7\end{bmatrix}.$$

Each position is independent. The lower-left entry in the second result is
$6-(-1)=7$. This is not a matrix product; no row-by-column summation is involved.

(w1-s08)=
### 8. Definitions can overlap

D is diagonal and symmetric; it is neither identity nor skew-symmetric.
K is skew-symmetric, but neither diagonal, identity, nor symmetric.
S is symmetric, but neither diagonal, identity, nor skew-symmetric.
Z is diagonal, symmetric, and skew-symmetric, but not the $2\times2$ identity.
Indeed $Z^T=Z=-Z$. A definition does not require that its label exclude all others.

## Standard applications

(w1-s09)=
### 9. Compare the target with the general form

$c\mathbf v+d\mathbf w=(c,c+d,d)^T$, so membership requires $y=x+z$.
For $(2,5,3)^T$, choose c=2,d=3; the middle coordinate is $2+3=5$.
For $(2,4,3)^T$, the required middle coordinate would be 5, not 4.
State both the coefficients for the successful case and the obstruction for the
failed one. {ref}`The plane example <w1-combinations>` shows why the condition is sufficient.

(w1-s10)=
### 10. The second direction is redundant

Because $(2,4)^T=2(1,2)^T$, the left side is $(c+2d)(1,2)^T$.
The target $(3,6)^T$ requires $c+2d=3$, giving all pairs
$(c,d)=(3-2t,t)$ for real t. The target $(3,7)^T$ is impossible because its second
entry is not twice its first. Two listed vectors need not give two different directions.

(w1-s11)=
### 11. Two computations of the same scalar

Directly, $\mathbf v+\mathbf w=(2,4,0)^T$, so
$\mathbf u^T(\mathbf v+\mathbf w)=2-8+0=-6$.
Separately, $\mathbf u^T\mathbf v=2+0-3=-1$ and
$\mathbf u^T\mathbf w=0-8+3=-5$. Their sum is −6.
This numerical check illustrates the identity; its general justification follows
from distributing real-number multiplication inside the finite sum.

(w1-s12)=
### 12. A total does not determine geometry

Both totals are 4. The dot product is 0 because no position has nonzero entries
in both vectors. Both norms are $\sqrt8=2\sqrt2$.
The difference is $(2,-2,2,-2)^T$ with norm 4; both vectors are nonzero and
perpendicular, so their angle is $90^\circ$.
The check $8+8-2\cdot0=16$ agrees with the squared distance.
Equal totals are only one scalar constraint, not a complete comparison of directions.

(w1-s13)=
### 13. Shapes settle the question

AB exists and is $2\times4$; BA and $A^TB$ are undefined because their inner sizes
are respectively 4 versus 2, and 2 versus 3. $B^TA^T$ exists and is $4\times2$.
Both $I_2A$ and $AI_3$ exist and equal A, with shape $2\times3$.
AB is rectangular, so its trace is not defined here.
Revisit the {ref}`shape rule <w1-products>` before attempting numerical multiplication.

(w1-s14)=
### 14. Compute and interpret by columns

$$MN=\begin{bmatrix}0&2\\4&-1\end{bmatrix},\qquad
NM=\begin{bmatrix}2&7&3\\0&-3&-2\\4&5&0\end{bmatrix}.$$

For example, $(MN)_{12}=2\cdot2+1(-1)+(-1)\cdot1=2$.
The first N column is $(1,0,2)^T$, so the first MN column must be
$1(2,0)^T+0(1,3)^T+2(-1,2)^T=(0,4)^T$, matching the result.
Both orders exist; their shapes differ, so they cannot be equal matrices.

(w1-s15)=
### 15. Count old and new stitches separately

$$H\mathbf x=\begin{bmatrix}12+4+2\cdot2\\12+2\cdot4+2\end{bmatrix}
=\begin{bmatrix}20\\22\end{bmatrix}.$$

Twenty old stitches are consumed and 22 new stitches produced, a net increase of 2.
The operation counts give neither their order nor all their placement details.
If you counted 24 consumed, you likely treated every decrease as two produced
stitches rather than two consumed ones. Revisit the {ref}`column interpretation <w1-products>`.

(w1-s16)=
### 16. Several summaries of one matrix

$$RS=\begin{bmatrix}3&3\\3&3\\3&3\end{bmatrix},\qquad
R\mathbf1_4=\begin{bmatrix}6\\6\\6\end{bmatrix},\qquad
R^T\mathbf1_3=\begin{bmatrix}6\\3\\6\\3\end{bmatrix}.$$

RS groups columns A/B and C/D for each of the three rows.
$R\mathbf1_4$ gives whole-row totals; $R^T\mathbf1_3$ gives whole-column totals.
The total is 18 either way, checking the sums. Grouping hides distinctions that
the original four-section records retained.

(w1-s17)=
### 17. Compare every corresponding entry

Symmetry requires $b=c$, with a,d arbitrary. Skew-symmetry requires
$a=d=0$ and $c=-b$. A matrix satisfying both has b=c and c=−b, so b=c=0;
the diagonal is also zero. Thus only the zero matrix is both over the reals.
Do not infer skew-symmetry from zero trace or zero diagonal alone.

(w1-s18)=
### 18. One construction, many possible answers

Choose $\mathbf w=(1,0,-1)^T$. Its dot product with $(2,-1,2)^T$ is $2-2=0$,
and its norm is $\sqrt2$. A unit choice is $(1,0,-1)^T/\sqrt2$.
There are many others: the requirement is $2w_1-w_2+2w_3=0$, or
$w_2=2w_1+2w_3$. Nonzero choices of the free coordinates give other directions.
A single example answers the construction request; it does not prove uniqueness.

## Synthesis

(w1-s19)=
### 19. An unchanged record need not mean an unchanged object

The total map is $J=[1\ 1\ 1\ 1]$. It returns 8 for both rows.
For $\mathbf d=\mathbf s-\mathbf r=(-2,2,-2,2)^T$, $J\mathbf d=0$.
The nonzero difference does not change that summary. It does change the section
record, and neither a whole-row total nor a section-count record proves the full
stitch order or fabric. Later we will call such invisible input directions a null space.

(w1-s20)=
### 20. Associativity preserves order

$$UD=\begin{bmatrix}2&1\\0&1\end{bmatrix},\qquad
DU=\begin{bmatrix}2&2\\0&1\end{bmatrix}.$$

They differ in the upper-right entry. Associativity changes parentheses in a
three-factor product, $(AB)C=A(BC)$; it does not exchange factors.
A single counterexample refutes a universal commutativity claim.

(w1-s21)=
### 21. Normalization is not distributive

$\|\mathbf u+\mathbf v\|=\sqrt2$, while $\|\mathbf u\|+\|\mathbf v\|=2$.
The normalized sum is $(1,1)^T/\sqrt2$, of length 1. The sum of normalized vectors
is $(1,1)^T$, of length $\sqrt2$. They are different vectors.
Computing the output's length is a quick way to catch an alleged unit vector
that has not actually been normalized.

(w1-s22)=
### 22. The transpose identifies the two parts

$$S=\begin{bmatrix}2&2\\2&4\end{bmatrix},\qquad
K=\begin{bmatrix}0&3\\-3&0\end{bmatrix},\qquad S+K=M.$$

For general square M, transposing the sum gives
$S^T=(M^T+M)/2=S$; transposing the difference gives
$K^T=(M^T-M)/2=-K$. Adding the two definitions returns M.
This exercise extends the lecture's definitions using only its transpose and
entrywise operations; it does not require a new physical stitch operation.

(w1-s23)=
### 23. Trace equality is weaker than matrix equality

Both products are square, although they may have different sizes:

$$
\operatorname{tr}(AB)=\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}b_{ji}
=\sum_{j=1}^{n}\sum_{i=1}^{m}b_{ji}a_{ij}
=\operatorname{tr}(BA).
$$

We changed the order of finite summation and commuted scalar products, not the
matrices. In Problem 14, trace(MN)=−1 and trace(NM)=$2-3+0=-1$, but the matrices
have different shapes and are not equal. An equal summary does not establish
equal objects—a familiar theme from the sampler.

(w1-s24)=
### 24. One output, two verified inputs

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
