(w2-elimination-page)=
# Elimination and echelon forms

Elimination replaces a coupled set of equations with a staircase of simpler ones.
The point is to expose what the equations determine, not merely to manufacture zeros.

<nav class="lecture-path" aria-label="Lecture 2 learning path">
<a href="index.html"><span class="path-number">01</span><span>Systems & modelling</span></a>
<a href="elimination.html" aria-current="page"><span class="path-number">02</span><span>Elimination & echelon forms</span></a>
<a href="practice.html"><span class="path-number">03</span><span>Exercises</span></a>
<a href="solutions.html"><span class="path-number">04</span><span>Solutions</span></a>
</nav>

## Before you begin

Know how to build an augmented matrix and perform the three
{ref}`elementary row operations <w2-row-operations>`. Keep fractions exact until
checking the result; decimals can conceal a zero or a contradiction.

:::{admonition} What you will understand
:class: key-result

1. Recognize REF and RREF, and identify pivots and free variables.
2. Carry out Gaussian elimination and back substitution.
3. Continue to RREF using Gauss–Jordan elimination when requested.
4. Distinguish unique, infinitely many, and no solutions from the reduced equations.
:::

::::{div} page-roadmap

**On this page**

- {ref}`2.5 · REF versus RREF <w2-ref>`
- {ref}`2.6 · Gaussian elimination <w2-gaussian>`
- {ref}`2.7 · Gauss–Jordan elimination <w2-jordan>`
- {ref}`2.8 · Read the solution set <w2-solutions>`
::::

(w2-ref)=
## 2.5 Row echelon form versus reduced row echelon form

::::{div} section-intro

**Learning goal:** Recognize the stopping forms and explain their extra conditions.

<span class="source-label">Lecture page 8</span>

When are the zeros arranged well enough to solve—and when can you read the answer directly?
::::


### A staircase, then a cleaner staircase

:::{admonition} Definition 2.2 · REF and RREF
:class: definition

A matrix is in **row echelon form (REF)** when:

1. All zero rows are below all nonzero rows.
2. In each successive nonzero row, the first nonzero entry (the **pivot**) lies
   strictly to the right of the pivot above it.
3. Entries below every pivot are zero.

It is in **reduced row echelon form (RREF)** when, in addition:

4. Every pivot is 1.
5. Every pivot is the only nonzero entry in its column—zeros above as well as below.

These definitions apply to rectangular matrices too, including augmented matrices.
:::

| Test | REF | RREF |
| --- | --- | --- |
| Zero rows at bottom; pivots step right | Required | Required |
| Zeros below pivots | Required | Required |
| Pivots equal 1 | Optional | Required |
| Zeros above pivots | Optional | Required |
| General solution method | Back substitution | Read pivot equations directly |

Every RREF matrix is in REF. The reverse does not follow. REF is not unique;
different legal choices can give different echelon matrices. RREF is unique for
a given matrix. We use that fact as a checking aid, without needing its proof here.

:::{admonition} Worked example 2.5 · Classify before calculating
:class: example

$$E=\left[\begin{array}{ccc|c}1&1&3&15\\0&1&1&6\\0&0&-1&-2\end{array}\right].$$

Its pivots occupy columns 1, 2, 3, stepping strictly right, with zeros below.
Thus $E$ is in **REF**. It is **not RREF**: the third pivot is $-1$, and there
are nonzero entries above pivots in columns 2 and 3. Turning $-1$ into 1 alone
would still not be enough; those entries above must also be cleared.

The lecture's displayed matrix is already RREF:

$$B=\begin{bmatrix}1&3&0&0&3\\0&0&1&0&9\\0&0&0&1&4\\0&0&0&0&0\end{bmatrix}.$$

The pivots are the 1s in columns **1, 3, 4**, and each is alone in its column.
The entries 3 in column 2 and 3,9,4 in column 5 are allowed: those are **nonpivot
columns**. A pivot need not sit on the main diagonal.

**Check:** inspect pivot columns, not every nonzero entry. $B$ is shown as an
ordinary matrix; without an augmentation bar we do not assume its last column
is a right-hand side.
:::

```{figure} ../figures/lecture2/echelon.svg
:name: fig-w2-echelon
:alt: REF matrix rows (1,1,3|15), (0,1,1|6), (0,0,-1|-2) have highlighted staircase pivots. RREF rows (1,0,0|5), (0,1,0|4), (0,0,1|2) have unit pivots and zeros above and below. Labels distinguish constants from variable columns.

REF exposes a staircase for back substitution. RREF also normalizes pivots and
clears above them. The augmented constant column stays attached throughout.
```


:::{admonition} Check your understanding
:class: checkpoint

Is $\begin{bmatrix}0&2&1\\0&0&3\\0&0&0\end{bmatrix}$ in REF? RREF? Does the first column of zeros prevent REF?
:::

:::{dropdown} Check your reasoning

It is REF: pivots 2 and 3 occur in columns 2 and 3; the zero row is last. It is not RREF because pivots are not 1 and column 3 has a nonzero entry above its pivot. A zero first column is allowed.
:::

::::{div} section-recap

**Keep this:** REF is a staircase; RREF also makes each pivot a lone 1 in its column.

**Try it yourself:** {ref}`Problem 9 <w2-p09>` · {ref}`Problem 10 <w2-p10>`.
::::

(w2-gaussian)=
## 2.6 Gaussian elimination and back substitution

::::{div} section-intro

**Learning goal:** Choose nonzero pivots, eliminate below them, and solve upward.

<span class="source-label">Lecture pages 6–7 and 9–15</span>

How do repeated X terms become a system that can be solved from the bottom?
::::


### The multiplier that cancels an entry

With nonzero pivot $a$ and an entry $c$ below it, use

$$R_i\leftarrow R_i-\frac{c}{a}R_k.$$

The targeted entry becomes $c-(c/a)a=0$. In actual arithmetic, $a$ and $c$ are
entries of the **current** matrix, after preceding operations.

Work from left to right. If the next pivot position is zero, swap in a lower row
with a nonzero entry in that column. If none exists, skip that column and look
right; it can become a free-variable column. Once the staircase is formed, stop
if REF was requested, or back substitute if the task is to solve.

:::{admonition} Worked example 2.6 · The lecture's main system
:class: example

**Given:** $x+y+3z=15$, $x+2y+4z=21$, $x+y+2z=13$.

**Step 1: augment in the order $(x,y,z)$.**

$$M_0=\left[\begin{array}{ccc|c}1&1&3&15\\1&2&4&21\\1&1&2&13\end{array}\right].$$

**Step 2: clear below the first pivot.** Use the unchanged first row for both
$R_2\leftarrow R_2-R_1$ and $R_3\leftarrow R_3-R_1$:

$$M_1=\left[\begin{array}{ccc|c}1&1&3&15\\0&1&1&6\\0&0&-1&-2\end{array}\right].$$

For example, row 3 is $(1-1,1-1,2-3\mid13-15)$.
The entry below the second pivot is already zero, so **$M_1$ is REF**.

**Step 3: back substitute from the bottom.**

$$-z=-2\Rightarrow z=2,\qquad y+z=6\Rightarrow y=4,$$
$$x+y+3z=15\Rightarrow x=15-4-6=5.$$

**Step 4: check the original equations.**

$$5+4+3(2)=15,\quad5+2(4)+4(2)=21,\quad5+4+2(2)=13.$$

Thus $\mathbf x=(5,4,2)^T$. There is a pivot for every unknown and no
contradiction, so this is the unique solution.
:::

### A zero in the first position calls for a swap

For $2y=4$, $x+y=3$, write

$$\left[\begin{array}{cc|c}0&2&4\\1&1&3\end{array}\right]
\xrightarrow{R_1\leftrightarrow R_2}
\left[\begin{array}{cc|c}1&1&3\\0&2&4\end{array}\right].$$

Back substitution gives $y=2$, $x=1$. The swap repaired the pivot order; it did
not exchange the meanings of $x$ and $y$. Columns stayed in the declared order.

:::{admonition} Common pitfall · Do not divide by a zero pivot
:class: pitfall

A zero candidate means **look below or move right**, not “the system has no
solution.” Use fractions exactly, preserve earlier zeros, and write each row
operation beside the next matrix. Verify constants as carefully as coefficients.
:::


:::{admonition} Check your understanding
:class: checkpoint

In $\left[\begin{array}{cc|c}2&1&5\\6&4&16\end{array}\right]$, which multiple clears the 6? What row results?
:::

:::{dropdown} Check your reasoning

Use $R_2\leftarrow R_2-3R_1$, obtaining $[0,1\mid1]$. Then $y=1$ and $x=2$; the original second equation gives $6(2)+4(1)=16$.
:::

::::{div} section-recap

**Keep this:** Gaussian elimination clears below pivots; back substitution solves from bottom to top.

**Try it yourself:** {ref}`Problem 11 <w2-p11>` · {ref}`Problem 12 <w2-p12>` · {ref}`Problem 13 <w2-p13>`.
::::

(w2-jordan)=
## 2.7 Gauss–Jordan elimination: continue to RREF

::::{div} section-intro

**Learning goal:** Normalize pivots and eliminate above them without changing the solution.

<span class="source-label">Lecture pages 12–21</span>

What extra work lets the final matrix state each determined variable directly?
::::


The slides use “Gaussian elimination” for a reduction that continues to RREF.
To distinguish the endpoints, we call the forward-to-REF stage **Gaussian
elimination**, and the continuation that clears above pivots **Gauss–Jordan
elimination**. Match the form requested in the question.

:::{admonition} Worked example 2.7 · Finish the same system
:class: example

Start from $M_1$ in Example 2.6; no need to repeat the forward stage.

**Step 1: normalize the third pivot**, $R_3\leftarrow-R_3$:

$$M_2=\left[\begin{array}{ccc|c}1&1&3&15\\0&1&1&6\\0&0&1&2\end{array}\right].$$

**Step 2: clear above that pivot**, using $R_1\leftarrow R_1-3R_3$ and
$R_2\leftarrow R_2-R_3$:

$$M_3=\left[\begin{array}{ccc|c}1&1&0&9\\0&1&0&4\\0&0&1&2\end{array}\right].$$

**Step 3: clear above the second pivot**, $R_1\leftarrow R_1-R_2$:

$$M_4=\left[\begin{array}{ccc|c}1&0&0&5\\0&1&0&4\\0&0&1&2\end{array}\right].$$

The coefficient block is $I_3$. The equations now read $x=5,y=4,z=2$, agreeing
with back substitution. **Check the endpoint:** unit staircase pivots, zeros above
and below, and no contradiction. The original-equation check still applies.
:::

Working from the rightmost pivot upward is convenient: a lower pivot row already
has zeros in earlier pivot columns, so clearing above it preserves those columns.
Different legal operation orders may produce different intermediate matrices,
but the same RREF and solution set.

:::{admonition} Key result 2.2 · Choose an endpoint deliberately
:class: key-result

**Find REF:** stop at a valid staircase. **Solve by Gaussian elimination:** form
REF, then back substitute. **Find RREF:** normalize pivots and clear above them too.
Back substitution and Gauss–Jordan are alternative finishing methods; doing both
is useful for learning or checking, not a requirement of every problem.
:::


:::{admonition} Check your understanding
:class: checkpoint

Is $M_3$ above RREF? Which single operation completes it?
:::

:::{dropdown} Check your reasoning

No: the 1 in row 1, column 2 is above the second pivot. $R_1\leftarrow R_1-R_2$ removes it and updates 9 to 5.
:::

::::{div} section-recap

**Keep this:** RREF adds unit pivots and zeros above; it expresses the same solutions more directly.

**Try it yourself:** {ref}`Problem 14 <w2-p14>` · {ref}`Problem 15 <w2-p15>`.
::::

(w2-solutions)=
## 2.8 Read the whole solution set

::::{div} section-intro

**Learning goal:** Identify consistency and parameterize all free variables.

<span class="source-label">Lecture page 8 and 21; contrasting solution cases added</span>

What do pivots and zero rows tell us about what the measurements really determine?
::::


### Check contradictions before counting free variables

:::{admonition} Key result 2.3 · The three possibilities over the real numbers
:class: key-result

After reduction of $[A\mid\mathbf b]$:

| What you see | What it means |
| --- | --- |
| A row $[0\;\cdots\;0\mid c]$, $c\ne0$ | **No solution:** it requires $0=c$ |
| No contradiction; every variable column has a pivot | **One solution** |
| No contradiction; at least one variable column has no pivot | **Infinitely many solutions:** choose free real parameters |

A **pivot variable** corresponds to a pivot in a coefficient column. Other
variables are **free**. A pivot in the augmented constant column signals a
contradiction, not a new variable. A zero row $[0\;\cdots\;0\mid0]$ says $0=0$.
:::

:::{admonition} Worked example 2.8 · A family, not a single guess
:class: example

Suppose reduction gives

$$\left[\begin{array}{ccc|c}1&2&0&3\\0&0&1&4\\0&0&0&0\end{array}\right].$$

1. **Test consistency.** No contradictory row appears.
2. **Locate pivots.** Columns 1 and 3 determine $x$ and $z$; $y$ is free.
3. **Introduce a parameter:** let $y=t\in\mathbb R$. Then $x=3-2t$ and $z=4$.
4. **State all solutions:**

   $$\mathbf x=\begin{bmatrix}3-2t\\t\\4\end{bmatrix}
   =\begin{bmatrix}3\\0\\4\end{bmatrix}
   +t\begin{bmatrix}-2\\1\\0\end{bmatrix},\qquad t\in\mathbb R.$$

5. **Check completeness.** Substitution gives $(3-2t)+2t=3$ and $z=4$ for every
   $t$. Conversely, any solution has some value $y=t$ and must have the displayed
   $x$ and $z$. Thus no solutions are omitted.

The set is a line in unknown-coordinate space. Writing only $(3,0,4)$ would give
one member and conceal the freedom.
:::

### Redundant and contradictory are different

For $x+y=2$ and $2x+2y=4$, subtract twice row 1 from row 2 to get $[0,0\mid0]$.
The family is $(2-t,t)$, $t\in\mathbb R$. Change the second constant to 5 and
the same operation gives $[0,0\mid1]$: no solution. In two dimensions these are
coincident lines versus distinct parallel lines.

Return to $H$: its repeated Y equation reduces to a zero row when readings agree,
yet all three coordinate columns still have pivots, so the point is unique.
With the front view alone, the missing Z pivot makes depth free. With conflicting
Y readings, a constant-column pivot records inconsistency.

:::{admonition} ML connection · Exact fitting comes before approximate fitting
:class: connection

A linear model also writes predictions as $A\mathbf x$, with rows for observations
and columns for adjustable coefficients. Solving $A\mathbf x=\mathbf b$ asks whether
the predictions can match every target exactly. Redundant observations may add
no new constraint; conflicting ones can prevent an exact fit. Least squares will
later define a best approximation. Elimination here does not silently replace an
inconsistent exact problem with that different objective.
:::


:::{admonition} Check your understanding
:class: checkpoint

Can a system with four equations and three unknowns have a unique solution and a zero row after reduction?
:::

:::{dropdown} Check your reasoning

Yes. The consistent stacked-view system $H$ is exactly this case. Every variable column has a pivot; the fourth equation is redundant. Count pivot columns rather than zero rows alone.
:::

::::{div} section-recap

**Keep this:** First test consistency; then identify pivots and parameterize every remaining variable.

**Try it yourself:** {ref}`Problem 16 <w2-p16>` · {ref}`Problem 17 <w2-p17>` · {ref}`Problem 18 <w2-p18>`.
::::

(w2-readiness)=
## Synthesis and exam readiness

The connected route is **coordinates → predicted readings → simultaneous
constraints → equivalent simpler equations → solution set → original-data check**.
Rows describe constraints; columns describe contributions. Elimination simplifies
the description while retaining the same possible inputs.

| Skill to demonstrate unaided | Independent practice |
| --- | --- |
| Multiply by rows and explain the column combination | {ref}`1 <w2-p01>`, {ref}`2 <w2-p02>` |
| Translate systems and build augmented matrices | {ref}`3 <w2-p03>`, {ref}`5 <w2-p05>` |
| Justify legal operations and spot information loss | {ref}`6 <w2-p06>` |
| Recognize REF/RREF and choose the requested endpoint | {ref}`9 <w2-p09>`, {ref}`10 <w2-p10>`, {ref}`15 <w2-p15>` |
| Reduce, back substitute, and verify | {ref}`11 <w2-p11>`–{ref}`14 <w2-p14>` |
| Interpret unique, infinite, and inconsistent cases | {ref}`7 <w2-p07>`, {ref}`8 <w2-p08>`, {ref}`16 <w2-p16>`–{ref}`18 <w2-p18>` |

Before moving on, check that you can:

- [ ] Reproduce a new elimination with every row operation and right side correct.
- [ ] Explain why REF need not have unit pivots and why RREF may have nonpivot columns.
- [ ] Handle a zero pivot candidate without dividing by zero.
- [ ] Give all solutions with parameters, rather than one convenient example.
- [ ] Distinguish redundancy from contradiction and verify in the original system.

**Independent rehearsal:** try Problems 12, 15, and 18 without notes; then check
the explanations. A wrong arithmetic step calls for a careful row-by-row retry;
a wrong solution classification calls for revisiting Section 2.8. This is an
editorial readiness check, not an official exam cutoff or a grade guarantee.

(w2-source-notes)=
## Sources, additions, and next steps

This chapter develops Erisa Terolli's CS 556 Week 2 slides,
`resources/lectures/WK2_SLE_Inverse_Determinants.pdf`, **PDF pages 1–21**
(page numbers count from the first PDF page). The difference matrix (p. 3),
two-variable system (p. 4), three-plane system (p. 5), main elimination system
(pp. 6–7, 9–21), and displayed RREF matrix (p. 8) are retained. Progressive slide
reveals are combined into complete worked sequences. Missing steps, original
checks, contrasting solution cases, diagrams, and shadow constructions are
editorial additions; the formal definitions clarify that row scaling must be nonzero.

The slides' reduction through RREF is retained; our terminology distinguishes
Gaussian forward elimination from the Gauss–Jordan continuation. These are
algorithmic stages, not different solution sets.

**Scope:** this is the requested systems-of-equations chapter. Determinants and
inverses on PDF pages 22–36 are not yet taught here. Week 3 will give names—rank,
null space, independence—to the freedom and redundancy we can already detect.
The source audit and verification record are in the repository's
`authoring/lecture2-coverage.md` and `authoring/lecture2-review.md`.
