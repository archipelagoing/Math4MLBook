(w3-cheatsheet)=
# TL;DR cheat sheet

<div class="chapter-kicker">Lecture 3 · Page 4 of 4 · Spaces, freedom, and coordinates</div>

**Choose the question first:** a set test, a homogeneous solve, a membership test,
a pivot count, or a coordinate conversion. Use the recipes below, then check in
the original data.

<nav class="lecture-path" aria-label="Lecture 3 learning path">
<a href="index.html"><span class="path-number">01</span><span>Spaces & subspaces</span></a>
<a href="solutions-rank.html"><span class="path-number">02</span><span>Complete solutions & rank</span></a>
<a href="basis.html"><span class="path-number">03</span><span>Independence, span & basis</span></a>
<a href="cheatsheet.html" aria-current="page"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

## 1 · Definitions and method choices

| Question | Test / recipe |
| --- | --- |
| Subspace? | Zero belongs; every $\lambda\mathbf v+\mu\mathbf w$ stays inside |
| Column-space or span membership? | Put generators in columns; solve $V\mathbf c=\mathbf b$ |
| Null space? | Solve $A\mathbf x=0$; one special vector per free variable |
| Complete solution? | Check consistency; find $\mathbf x_p$; add all null directions |
| Independent columns? | $N(V)=\{0\}$; pivot in every column |
| Basis? | Independent **and** spanning the named space |
| Dimension? | Count vectors in a basis, not coordinates of an ambient record |
| Change of basis? | Columns are the new basis; multiply to reconstruct, solve to find coefficients |

:::{admonition} Complete solution and rank
:class: key-result

$$\mathbf x=\mathbf x_p+\sum_{j=1}^{n-r}t_j\mathbf s_j,\quad t_j\in\mathbb R,
\qquad r=\operatorname{rank}(A).$$

This requires consistency. Compare $\operatorname{rank}(A)$ with
$\operatorname{rank}([A\mid\mathbf b])$: unequal means no solution; equal means
$n-r$ free variables. A consistent system is unique exactly when $r=n$.
:::

## 2 · Four spaces: where, how, and how many

| Space | Ambient space | Basis recipe | Dimension |
| --- | --- | --- | --- |
| $C(A)$ | $\mathbb R^m$ | Original pivot columns | r |
| $N(A)$ | $\mathbb R^n$ | Special solutions of $A\mathbf x=0$ | n−r |
| $C(A^T)$ | $\mathbb R^n$ | Nonzero echelon rows | r |
| $N(A^T)$ | $\mathbb R^m$ | Special solutions of $A^T\mathbf y=0$ | m−r |

A left-null vector gives a consistency condition: if $A^T\mathbf y=0$, then any
achievable $\mathbf b$ must have $\mathbf y^T\mathbf b=0$.

## 3 · One short solve that connects the ideas

:::::{admonition} Worked example 3.16 · From equations to spaces
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Reduce the augmented system</span>

Given
$A=\begin{bmatrix}1&2&0\\0&1&1\end{bmatrix}$ and $\mathbf b=(4,3)^T$,
use $R_1\leftarrow R_1-2R_2$:

$$\left[\begin{array}{ccc|c}1&0&-2&-2\\0&1&1&3\end{array}\right].$$
::::

::::{div} worked-step

<span class="step-label">Step 2 · Choose the free coordinate and state all answers</span>

Set $x_3=t$. Then $x_1=-2+2t$, $x_2=3-t$:

$$\mathbf x=(-2,3,0)^T+t(2,-1,1)^T.$$

Check $(-2+2t)+2(3-t)=4$ and $(3-t)+t=3$ for every $t$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Read the spaces and their dimensions</span>

Two pivots give rank 2 and one null direction.
$N(A)=\operatorname{span}\{(2,-1,1)^T\}$.
The **original** first two columns $(1,0)^T,(2,1)^T$ form a basis of
$C(A)=\mathbb R^2$. The reduced rows $(1,0,-2)^T,(0,1,1)^T$ generate the row
space in $\mathbb R^3$. The left null space is $\{0\}$ because $m-r=0$.
::::

::::{div} key-answer

**Keep this result:** One computation gives consistency, the complete family, rank, and bases for the four spaces.
::::
:::::

## 4 · Coordinate-conversion recipe

:::{admonition} Declare the ordered basis and conversion direction
:class: key-result

For an ordered basis of $\mathbb R^n$, set $B=[\mathbf b_1\ \cdots\ \mathbf b_n]$:

$$\mathbf x_E=B[\mathbf x]_{\mathcal B},\qquad
[\mathbf x]_{\mathcal B}=B^{-1}\mathbf x_E,\qquad
[\mathbf x]_{\mathcal C}=C^{-1}B[\mathbf x]_{\mathcal B}.$$

**Steps:** write columns in order → identify given coordinates → choose the
correct direction → calculate → reconstruct to check. For a proper subspace's
rectangular basis matrix, solve for coefficients instead of using an inverse.
:::

:::{admonition} Avoid these lost marks
:class: pitfall

- Zero in a set does not prove closure. A translated solution set is generally affine.
- Use original pivot columns for the column-space basis, not columns of RREF.
- A nonpivot variable is free only after consistency is established.
- A spanning list may be dependent; an independent list may fail to span the target.
- Membership in span(S) need not mean membership in the listed set S.
- A tilted basis changes coordinates, not the point. Coefficient lengths are not
  physical lengths unless the basis is orthonormal.
:::

**Check independence from the examples:** attempt the
{ref}`mixed readiness check <w3-readiness>` without this page, then diagnose the
first missed step. See {ref}`source notes <w3-source-notes>` for slide/support mapping.
