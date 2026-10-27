<!-- Included question groups; not a standalone reader page. -->

<!-- systems:start -->

(w2-p01)=
### Problem 1

For $L=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix}$, compute $L(3,7,8)^T$ by rows and by columns. Then recover the input from that output.

:::{dropdown} Hint

The output contains a first entry and successive differences.
:::

{ref}`Explained solution 1 <w2-s01>`.

```{include} solutions.md
:start-after: <!-- answer-01:start -->
:end-before: <!-- answer-01:end -->
```

(w2-p02)=
### Problem 2

Write the front-view matrix $O$ with $O(X,Y,Z)^T=(X,Y)^T$. Give its dimensions, compute $O(4,-1,7)^T$, and explain why this output cannot determine depth.

:::{dropdown} Hint

Which input coordinate contributes nothing?
:::

{ref}`Explained solution 2 <w2-s02>`.

```{include} solutions.md
:start-after: <!-- answer-02:start -->
:end-before: <!-- answer-02:end -->
```

(w2-p03)=
### Problem 3

Write $2x-y=5$, $x+3y=6$ as a matrix equation and column combination. Solve and check both equations.

:::{dropdown} Hint

Eliminate $x$ from the second row with a fraction, or eliminate $y$ by combining equations.
:::

{ref}`Explained solution 3 <w2-s03>`.

```{include} solutions.md
:start-after: <!-- answer-03:start -->
:end-before: <!-- answer-03:end -->
```

(w2-p04)=
### Problem 4

For $x+y=2$, compare the additional equations $2x+2y=4$, $2x+2y=5$, and $x-y=0$. Describe each row picture and solution set.

:::{dropdown} Hint

The second equation can repeat, contradict, or add a different line.
:::

{ref}`Explained solution 4 <w2-s04>`.

```{include} solutions.md
:start-after: <!-- answer-04:start -->
:end-before: <!-- answer-04:end -->
```

(w2-p05)=
### Problem 5

In variable order $(x,y,z)$, write the augmented matrix for $2z-x=4$, $y+3x=2$, $z=1$. Explain each zero, then solve.

:::{dropdown} Hint

Reorder terms, not variables: coefficient columns stay $x,y,z$.
:::

{ref}`Explained solution 5 <w2-s05>`.

```{include} solutions.md
:start-after: <!-- answer-05:start -->
:end-before: <!-- answer-05:end -->
```

(w2-p06)=
### Problem 6

A student replaces the first row of $x+y=2$, $x-y=0$ by zero, and reports $x=y$ as the full answer. Explain the error. Give the inverse operation for $R_2\leftarrow R_2-3R_1$.

:::{dropdown} Hint

Can each claimed operation be undone?
:::

{ref}`Explained solution 6 <w2-s06>`.

```{include} solutions.md
:start-after: <!-- answer-06:start -->
:end-before: <!-- answer-06:end -->
```

(w2-p07)=
### Problem 7

A front mark is $(2,3)$ and the matched side mark is $(3,9)$. Form the stacked augmented system and solve. What happens if only the front mark is available?

:::{dropdown} Hint

Stack the coordinates in order $X,Y,Y,Z$.
:::

{ref}`Explained solution 7 <w2-s07>`.

```{include} solutions.md
:start-after: <!-- answer-07:start -->
:end-before: <!-- answer-07:end -->
```

(w2-p08)=
### Problem 8

Front readings are $(2,2)$ and side readings are $(4,4)$. Show the row operation exposing inconsistency. Why is $(2,3,4)^T$ not a solution?

:::{dropdown} Hint

Compare the two equations for Y.
:::

{ref}`Explained solution 8 <w2-s08>`.

```{include} solutions.md
:start-after: <!-- answer-08:start -->
:end-before: <!-- answer-08:end -->
```

(w2-p09)=
### Problem 9

Classify each matrix as RREF, REF only, or neither: $A=\begin{bmatrix}2&1\\0&3\end{bmatrix}$, $B=\begin{bmatrix}0&1&2\\0&0&0\end{bmatrix}$, $C=\begin{bmatrix}0&0\\1&0\end{bmatrix}$, $D=\begin{bmatrix}1&2\\0&1\end{bmatrix}$.

:::{dropdown} Hint

Check zero rows, staircase, pivot values, and pivot columns in that order.
:::

{ref}`Explained solution 9 <w2-s09>`.

```{include} solutions.md
:start-after: <!-- answer-09:start -->
:end-before: <!-- answer-09:end -->
```

(w2-p10)=
### Problem 10

For the lecture matrix $B=\begin{bmatrix}1&3&0&0&3\\0&0&1&0&9\\0&0&0&1&4\\0&0&0&0&0\end{bmatrix}$, list pivot columns and explain why column 2 is allowed. If we now explicitly interpret column 5 as the constant column, solve for four unknowns.

:::{dropdown} Hint

An augmentation interpretation must be declared before interpreting variables.
:::

{ref}`Explained solution 10 <w2-s10>`.

```{include} solutions.md
:start-after: <!-- answer-10:start -->
:end-before: <!-- answer-10:end -->
```

(w2-p11)=
### Problem 11

Solve the slide system $x-2y=1$, $3x+2y=11$ by Gaussian elimination. Show REF and back substitution; verify.

:::{dropdown} Hint

The multiplier below the first pivot is 3.
:::

{ref}`Explained solution 11 <w2-s11>`.

```{include} solutions.md
:start-after: <!-- answer-11:start -->
:end-before: <!-- answer-11:end -->
```

(w2-p12)=
### Problem 12

Solve the slide system $x+2y+3z=6$, $2x+5y+2z=4$, $6x-3y+z=2$. Show each elimination and check uniqueness.

:::{dropdown} Hint

After clearing column 1, add 15 times row 2 to row 3.
:::

{ref}`Explained solution 12 <w2-s12>`.

```{include} solutions.md
:start-after: <!-- answer-12:start -->
:end-before: <!-- answer-12:end -->
```

(w2-p13)=
### Problem 13

Solve $2y=4$, $x+y=3$ using a row swap. Explain why swapping columns instead would require extra bookkeeping.

:::{dropdown} Hint

The first candidate is zero, but a lower entry in the same column is nonzero.
:::

{ref}`Explained solution 13 <w2-s13>`.

```{include} solutions.md
:start-after: <!-- answer-13:start -->
:end-before: <!-- answer-13:end -->
```

(w2-p14)=
### Problem 14

Find RREF for $\left[\begin{array}{cc|c}2&1&5\\6&4&16\end{array}\right]$. State the solution and check it.

:::{dropdown} Hint

Clear below, then above the second pivot, then normalize the first.
:::

{ref}`Explained solution 14 <w2-s14>`.

```{include} solutions.md
:start-after: <!-- answer-14:start -->
:end-before: <!-- answer-14:end -->
```

(w2-p15)=
### Problem 15

For $\left[\begin{array}{ccc|c}1&1&3&15\\0&1&1&6\\0&0&-1&-2\end{array}\right]$, answer separately: (a) is it REF? (b) what is the solution by back substitution? (c) what operations produce RREF?

:::{dropdown} Hint

Distinguish recognizing a form from solving and from computing another form.
:::

{ref}`Explained solution 15 <w2-s15>`.

```{include} solutions.md
:start-after: <!-- answer-15:start -->
:end-before: <!-- answer-15:end -->
```

(w2-p16)=
### Problem 16

Read all solutions from $\left[\begin{array}{ccc|c}1&2&0&3\\0&0&1&4\\0&0&0&0\end{array}\right]$. Name pivot/free variables and verify every parameter value.

:::{dropdown} Hint

The missing pivot column, not the position of a zero row alone, identifies freedom.
:::

{ref}`Explained solution 16 <w2-s16>`.

```{include} solutions.md
:start-after: <!-- answer-16:start -->
:end-before: <!-- answer-16:end -->
```

(w2-p17)=
### Problem 17

Read the complete solution of $\left[\begin{array}{cccc|c}1&2&0&-1&3\\0&0&1&4&5\\0&0&0&0&0\end{array}\right]$. How many free parameters are required?

:::{dropdown} Hint

There are four variable columns and pivots in columns 1 and 3.
:::

{ref}`Explained solution 17 <w2-s17>`.

```{include} solutions.md
:start-after: <!-- answer-17:start -->
:end-before: <!-- answer-17:end -->
```

(w2-p18)=
### Problem 18

The front mark is $(a,b)$ and side mark $(c,d)$. Use elimination on $H$ to state exactly when a solution exists, whether it is unique, and its coordinates. Explain why four readings need not be four independent constraints.

:::{dropdown} Hint

Subtract the two Y equations symbolically.
:::

{ref}`Explained solution 18 <w2-s18>`.

```{include} solutions.md
:start-after: <!-- answer-18:start -->
:end-before: <!-- answer-18:end -->
```

<!-- systems:end -->

<!-- determinants:start -->

(w2-p19)=
### Problem 19

A square matrix has determinant $-5$. You multiply row 1 by 3, then swap rows 1 and 2. What is the new determinant? Explain both effects.

:::{dropdown} Hint

Scale one row, then flip the sign once.
:::

{ref}`Explained solution 19 <w2-s19>`.

```{include} solutions.md
:start-after: <!-- answer-19:start -->
:end-before: <!-- answer-19:end -->
```

(w2-p20)=
### Problem 20

Compute $\det(D)$ for $D=\begin{bmatrix}1&2&3\\3&1&2\\0&0&1\end{bmatrix}$ by (a) row-1 Laplace expansion and (b) row-3 expansion. Why should both agree?

:::{dropdown} Hint

Row 3 has two zero terms. Keep the checkerboard signs.
:::

{ref}`Explained solution 20 <w2-s20>`.

```{include} solutions.md
:start-after: <!-- answer-20:start -->
:end-before: <!-- answer-20:end -->
```

(w2-p21)=
### Problem 21

A 2D linear map has determinant $-3$. Find the image area of a region of area 4 and state what happens to orientation. What is the area of a triangle with edge columns $\begin{bmatrix}1&2\\3&1\end{bmatrix}$?

:::{dropdown} Hint

Areas use absolute values; triangles take half the parallelogram area.
:::

{ref}`Explained solution 21 <w2-s21>`.

```{include} solutions.md
:start-after: <!-- answer-21:start -->
:end-before: <!-- answer-21:end -->
```

<!-- determinants:end -->

<!-- inverses:start -->

(w2-p22)=
### Problem 22

Find the inverse of $C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$ by the 2×2 shortcut, then solve $C\mathbf x=(5,3)^T$. Check.

:::{dropdown} Hint

Check $ad-bc$ before swapping or negating entries.
:::

{ref}`Explained solution 22 <w2-s22>`.

```{include} solutions.md
:start-after: <!-- answer-22:start -->
:end-before: <!-- answer-22:end -->
```

(w2-p23)=
### Problem 23

For $S=\begin{bmatrix}1&2\\2&4\end{bmatrix}$, test invertibility. Classify $S\mathbf x=(3,6)^T$ and $S\mathbf x=(3,7)^T$, giving all solutions when possible.

:::{dropdown} Hint

The second row is twice the first; compare right sides.
:::

{ref}`Explained solution 23 <w2-s23>`.

```{include} solutions.md
:start-after: <!-- answer-23:start -->
:end-before: <!-- answer-23:end -->
```

(w2-p24)=
### Problem 24

Find $C^{-1}$ for $C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$ by Gauss–Jordan on $[C\mid I]$. Show the operations on both blocks and verify the result.

:::{dropdown} Hint

Swap rows; clear below; normalize; clear above.
:::

{ref}`Explained solution 24 <w2-s24>`.

```{include} solutions.md
:start-after: <!-- answer-24:start -->
:end-before: <!-- answer-24:end -->
```

(w2-p25)=
### Problem 25

For $Q=\begin{bmatrix}1&2&1\\4&4&5\\6&7&7\end{bmatrix}$, compute the minors, cofactor matrix, adjugate, determinant, and inverse. Show why $C_{12}$ is positive even though $M_{12}$ is negative.

:::{dropdown} Hint

Use the sign grid before transposing. Expand the determinant using cofactors.
:::

{ref}`Explained solution 25 <w2-s25>`.

```{include} solutions.md
:start-after: <!-- answer-25:start -->
:end-before: <!-- answer-25:end -->
```

(w2-p26)=
### Problem 26

A square $3\times3$ matrix has only two pivots. State its determinant, whether an inverse exists, and whether $A\mathbf x=0$ has a nonzero solution. Can you classify $A\mathbf x=\mathbf b$ without knowing $\mathbf b$?

:::{dropdown} Hint

Use the equivalent tests, then distinguish homogeneous from inhomogeneous systems.
:::

{ref}`Explained solution 26 <w2-s26>`.

```{include} solutions.md
:start-after: <!-- answer-26:start -->
:end-before: <!-- answer-26:end -->
```

<!-- inverses:end -->
