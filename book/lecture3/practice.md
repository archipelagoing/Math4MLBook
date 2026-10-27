<!-- Included question groups; not separate reader pages. -->

<!-- spaces:start -->

(w3-p01)=
### Problem 1

Classify these subsets of $\mathbb R^2$: the first quadrant; $\{(t,-3t)^T:t\in\mathbb R\}$; and $\{(x,y):x+y=2\}$. Justify each.

:::{dropdown} Hint

Check zero first, then a general combination or a negative scalar.
:::

```{include} solutions.md
:start-after: <!-- answer-01:start -->
:end-before: <!-- answer-01:end -->
```

(w3-p02)=
### Problem 2

Prove that $W=\{(x,y,z):x-2y+z=0\}$ is a subspace, and write every member with two real parameters.

:::{dropdown} Hint

Let y and z be arbitrary, then express x.
:::

```{include} solutions.md
:start-after: <!-- answer-02:start -->
:end-before: <!-- answer-02:end -->
```

(w3-p03)=
### Problem 3

The union of the x-axis and y-axis contains zero and is closed under scaling. Is it a subspace? Give a decisive test.

:::{dropdown} Hint

Add one vector from each axis.
:::

```{include} solutions.md
:start-after: <!-- answer-03:start -->
:end-before: <!-- answer-03:end -->
```

(w3-p04)=
### Problem 4

For $P=\begin{bmatrix}1&2\\0&1\\1&3\end{bmatrix}$, decide whether $(4,1,5)^T$ and $(4,1,6)^T$ belong to $C(P)$. Describe the entire column space by an equation.

:::{dropdown} Hint

Compare the third output with the first two.
:::

```{include} solutions.md
:start-after: <!-- answer-04:start -->
:end-before: <!-- answer-04:end -->
```

(w3-p05)=
### Problem 5

Find all vectors in the null space of $A=\begin{bmatrix}1&2&-1\\0&1&3\end{bmatrix}$. Give one special solution and check it.

:::{dropdown} Hint

Clear above the second pivot, then choose the third variable freely.
:::

```{include} solutions.md
:start-after: <!-- answer-05:start -->
:end-before: <!-- answer-05:end -->
```

(w3-p06)=
### Problem 6

Start with $x+y+z=0$. Compare adding $2x+2y+2z=0$ with adding $y-z=0$. How does each affect the invisible input freedom?

:::{dropdown} Hint

Distinguish a repeated condition from an independent condition.
:::

```{include} solutions.md
:start-after: <!-- answer-06:start -->
:end-before: <!-- answer-06:end -->
```

(w3-p07)=
### Problem 7

For a $4\times6$ matrix, state the ambient spaces of its four fundamental subspaces and the equation defining its left null space.

:::{dropdown} Hint

Count inputs and outputs before looking at any values.
:::

```{include} solutions.md
:start-after: <!-- answer-07:start -->
:end-before: <!-- answer-07:end -->
```

(w3-p08)=
### Problem 8

Supplied Recitation 2, Problem 2: for $A=\begin{bmatrix}1&3&1&2\\2&6&4&8\\0&0&2&4\end{bmatrix}$, find generating vectors for all four spaces and verify them. After Part J, identify their basis sizes.

:::{dropdown} Hint

Row 2 minus twice row 1 equals row 3. Retain original pivot columns.
:::

```{include} solutions.md
:start-after: <!-- answer-08:start -->
:end-before: <!-- answer-08:end -->
```

<!-- spaces:end -->

<!-- solutions:start -->

(w3-p09)=
### Problem 9

Solve $x+y+2z=4$, $2x+2y+4z=8$, $y-z=1$. Give a particular solution, a null direction, and the complete family.

:::{dropdown} Hint

The second equation is redundant; use the third equation to remove y.
:::

```{include} solutions.md
:start-after: <!-- answer-09:start -->
:end-before: <!-- answer-09:end -->
```

(w3-p10)=
### Problem 10

Find every solution of $x_1+2x_2+x_4=3$, $x_2+x_3-x_4=2$. State both free parameters explicitly.

:::{dropdown} Hint

Columns 3 and 4 are free after clearing column 2.
:::

```{include} solutions.md
:start-after: <!-- answer-10:start -->
:end-before: <!-- answer-10:end -->
```

(w3-p11)=
### Problem 11

Replace the second right side in Problem 9 by 9, leaving the first right side 4 and the third 1. Does a complete solution exist?

:::{dropdown} Hint

Compare twice the first equation with the second.
:::

```{include} solutions.md
:start-after: <!-- answer-11:start -->
:end-before: <!-- answer-11:end -->
```

(w3-p12)=
### Problem 12

Prove that any two solutions of $A\mathbf x=\mathbf b$ differ by a null vector. When is its nonempty solution set a subspace?

:::{dropdown} Hint

Apply A to the difference and test whether zero belongs.
:::

```{include} solutions.md
:start-after: <!-- answer-12:start -->
:end-before: <!-- answer-12:end -->
```

(w3-p13)=
### Problem 13

Compute the rank of $M=\begin{bmatrix}1&2&0\\0&1&1\\1&3&1\end{bmatrix}$ and give a null-space generator. Explain why three nonzero rows are insufficient evidence of rank 3.

:::{dropdown} Hint

Row 3 equals row 1 plus row 2.
:::

```{include} solutions.md
:start-after: <!-- answer-13:start -->
:end-before: <!-- answer-13:end -->
```

(w3-p14)=
### Problem 14

Find the rank of $A_\alpha=\begin{bmatrix}1&2&3\\0&\alpha&2\alpha\\0&0&\alpha-1\end{bmatrix}$ for every real $\alpha$. Show the exceptional cases, not just the determinant.

:::{dropdown} Hint

When a diagonal candidate is zero, inspect the other remaining entries.
:::

```{include} solutions.md
:start-after: <!-- answer-14:start -->
:end-before: <!-- answer-14:end -->
```

(w3-p15)=
### Problem 15

Supplied Recitation 2, Problem 3: the complete solution of $A\mathbf x=(2,4,4)^T$ is $(2,0,0)^T+c(1,1,0)^T+d(0,0,1)^T$. Find A, its row-space dimension, and exactly which right sides are attainable.

:::{dropdown} Hint

Use the particular solution and each null direction as separate matrix equations.
:::

```{include} solutions.md
:start-after: <!-- answer-15:start -->
:end-before: <!-- answer-15:end -->
```

(w3-p16)=
### Problem 16

Supplied Recitation 2 Problem 1 / Assignment 2 Problem 1: for $x+\beta y=1$, $x-2y-z=2$, $y+z=g$, identify the parameter requiring a row swap in the usual forward order, the parameter making A singular, its consistency condition, and the singular-case solution with $z=2$.

:::{dropdown} Hint

After subtracting row 1 from row 2, its y coefficient is −2−β. A lower y coefficient is still 1.
:::

```{include} solutions.md
:start-after: <!-- answer-16:start -->
:end-before: <!-- answer-16:end -->
```

<!-- solutions:end -->

<!-- basis:start -->

(w3-p17)=
### Problem 17

Test independence of (a) $(1,2)^T,(3,6)^T$; (b) $(1,2)^T,(2,1)^T$; and (c) the list in (b) with zero appended. Give a dependence relation whenever possible.

:::{dropdown} Hint

Test zero combinations, not whether the vectors look different.
:::

```{include} solutions.md
:start-after: <!-- answer-17:start -->
:end-before: <!-- answer-17:end -->
```

(w3-p18)=
### Problem 18

For $\mathbf v_1=(1,0)^T$, $\mathbf v_2=(0,1)^T$, $\mathbf v_3=(2,-1)^T$, determine the span and independence of the full list. Remove redundancy to give a basis.

:::{dropdown} Hint

Can the third vector be made from the first two?
:::

```{include} solutions.md
:start-after: <!-- answer-18:start -->
:end-before: <!-- answer-18:end -->
```

(w3-p19)=
### Problem 19

Let $S=\{(1,0,1)^T,(0,2,1)^T\}$. Test whether $(3,4,5)^T$ and $(3,4,6)^T$ lie in span(S), and describe that span with an equation.

:::{dropdown} Hint

Write the output of coefficients a,b before choosing numbers.
:::

```{include} solutions.md
:start-after: <!-- answer-19:start -->
:end-before: <!-- answer-19:end -->
```

(w3-p20)=
### Problem 20

From $(1,1,0)^T,(0,1,1)^T,(1,2,1)^T$, select a basis of their span, give its dimension, and describe the span by a coordinate equation.

:::{dropdown} Hint

The third vector is a sum of the first two.
:::

```{include} solutions.md
:start-after: <!-- answer-20:start -->
:end-before: <!-- answer-20:end -->
```

(w3-p21)=
### Problem 21

A $5\times4$ matrix has rank 3. Give the dimensions of all four fundamental subspaces and state whether it has full row rank or full column rank.

:::{dropdown} Hint

Use m=5, n=4 and distinguish the two nullities.
:::

```{include} solutions.md
:start-after: <!-- answer-21:start -->
:end-before: <!-- answer-21:end -->
```

(w3-p22)=
### Problem 22

For the ordered basis $\mathcal B=((2,1)^T,(1,-1)^T)$, convert $[\mathbf u]_{\mathcal B}=(2,-1)^T$ to natural coordinates, and convert $\mathbf v_E=(4,-1)^T$ to B coordinates. Check both directions.

:::{dropdown} Hint

Place the basis vectors in columns; keep the two given vectors distinct.
:::

```{include} solutions.md
:start-after: <!-- answer-22:start -->
:end-before: <!-- answer-22:end -->
```

(w3-p23)=
### Problem 23

Let $B=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, $C=\begin{bmatrix}1&0\\1&1\end{bmatrix}$ be ordered basis matrices. Convert $[\mathbf x]_{\mathcal B}=(2,-1)^T$ to C coordinates, and check through natural coordinates.

:::{dropdown} Hint

Use C inverse times B, in that order.
:::

```{include} solutions.md
:start-after: <!-- answer-23:start -->
:end-before: <!-- answer-23:end -->
```

(w3-p24)=
### Problem 24

Can $B=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$ serve as a basis matrix for a subspace? Find coordinates of $(2,-1,1)^T$ and decide whether $(2,-1,0)^T$ has coordinates in that basis.

:::{dropdown} Hint

A basis of a proper subspace can have a rectangular column matrix.
:::

```{include} solutions.md
:start-after: <!-- answer-24:start -->
:end-before: <!-- answer-24:end -->
```

<!-- basis:end -->

<!-- mixed:start -->

(w3-p25)=
### Problem 25

For $S=\{(x_1,x_2,x_3):x_1-x_2=0\}$, decide whether it is a subspace, justify your decision, select a basis, and state its dimension.

```{include} solutions.md
:start-after: <!-- answer-25:start -->
:end-before: <!-- answer-25:end -->
```

(w3-p26)=
### Problem 26

For $A=\begin{bmatrix}1&2&1\\0&1&1\\1&3&2\end{bmatrix}$ and $\mathbf b=(5,3,9)^T$, determine both coefficient and augmented rank and give the complete solution, if one exists.

```{include} solutions.md
:start-after: <!-- answer-26:start -->
:end-before: <!-- answer-26:end -->
```

(w3-p27)=
### Problem 27

For $(1,1,0)^T,(0,1,2)^T,(1,2,2)^T$, give a nontrivial zero combination, a basis of the span and its dimension, and decide whether $(2,1,-2)^T$ belongs to that span.

```{include} solutions.md
:start-after: <!-- answer-27:start -->
:end-before: <!-- answer-27:end -->
```

(w3-p28)=
### Problem 28

For the ordered basis $\mathcal B=((2,1)^T,(-1,1)^T)$ and $[\mathbf x]_{\mathcal B}=(-1,3)^T$, construct the basis matrix, find natural coordinates, compute its inverse, and verify the round trip.

```{include} solutions.md
:start-after: <!-- answer-28:start -->
:end-before: <!-- answer-28:end -->
```

<!-- mixed:end -->
