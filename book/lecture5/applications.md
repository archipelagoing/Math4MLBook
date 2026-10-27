(w5-applications)=
# Dimensionality reduction and recommendations

<div class="chapter-kicker">Lecture 5 · Page 3 of 4 · Find directions, separate strengths, keep what matters</div>

A full SVD describes every direction. A smaller representation keeps the strongest ones. We first quantify what is lost, then examine the movie-rating example carefully: **compressing a complete matrix and predicting unknown entries are different problems**.

<nav class="lecture-path" aria-label="Lecture 5 learning path">
<a href="index.html"><span class="path-number">01</span><span>Eigenvalues & diagonalization</span></a>
<a href="svd.html"><span class="path-number">02</span><span>Singular value decomposition</span></a>
<a href="applications.html" aria-current="page"><span class="path-number">03</span><span>Reduction & recommendations</span></a>
<a href="cheatsheet.html"><span class="path-number">04</span><span>TL;DR cheat sheet</span></a>
</nav>

::::{div} page-roadmap

**Follow the lecture**

- {ref}`H · Dimensionality reduction with SVD <w5-reduction>`
- {ref}`I · Movie recommendations <w5-recommendations>`
- {ref}`J · The final in-class exercises <w5-in-class>`
::::

(w5-reduction)=
## H · Dimensionality reduction with SVD

::::{div} section-intro

**Learning goal:** Construct a truncated matrix, track dimensions, and calculate its approximation error.

<span class="source-label">Lecture PDF pages 27–33</span>
::::

:::{admonition} Definition · Truncation and low-dimensional coordinates
:class: definition

For a rank-$r$ matrix $R$ with ordered singular values and $0\le k\le r$, keep the first $k$ positive terms:

$$\boxed{R_k=U_k\Sigma_kV_k^T=\sum_{i=1}^k\sigma_i\mathbf u_i\mathbf v_i^T}.$$

$U_k$ is $m\times k$, $\Sigma_k$ is $k\times k$, $V_k$ is $n\times k$; the reconstructed $R_k$ remains $m\times n$.
For row records, $Z=RV_k=U_k\Sigma_k$ is an $m\times k$ coordinate table, and $ZV_k^T=R_k$ reconstructs the approximation. At $k=r$ the compact form is exact; at $k=0$ it is zero.

The factors store $k(m+n+1)$ numbers instead of $mn$; this saves space only when $k$ is small enough. Reduced representation size is different from the unchanged size of the reconstructed matrix.
:::

:::{admonition} Eckart–Young · Closest in a specified norm
:class: key-result

The truncated SVD minimizes $\|R-B\|_F$ over matrices $B$ of rank **at most** $k$, where $\|M\|_F^2=\sum_{ij}M_{ij}^2$. Its error is

$$\boxed{\|R-R_k\|_F^2=\sum_{i>k}\sigma_i^2}.$$

It is also optimal in the spectral norm, with $\|R-R_k\|_2=\sigma_{k+1}$ for $k<r$; this norm is the largest output length over unit inputs. When $k=r$, the error is zero. Ties at the cut can allow different equally good Frobenius approximations.
The squared Frobenius error formula follows because the unit outer products $\mathbf u_i\mathbf v_i^T$ are mutually orthogonal under the entrywise dot product. The global optimality theorem is stated here, not proved in full.
“Closest” therefore has a precise meaning; it does not guarantee the best semantic features or predictions on unseen data.
:::

```{figure} ../figures/lecture5/truncation.svg
:alt: A matrix has a full compact factorization with inner size r. Keeping only k columns of U and V and k diagonal entries gives a rank-k approximation with the original m by n outer size.

The factor blocks from pages 28–33, redrawn with the selected directions highlighted. Reduced coordinates are smaller; the reconstructed matrix keeps its original shape.
```

:::::{admonition} Worked example 5.11 · Keep one direction of the worked SVD
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · State the matrix and its leading factors</span>

Reuse the fully specified matrix

$$R=\begin{bmatrix}3&0\\4&5\end{bmatrix},\qquad
\sigma_1=3\sqrt5,\quad\mathbf u_1=(1,3)^T/\sqrt{10},\quad\mathbf v_1=(1,1)^T/\sqrt2.$$

The discarded singular value is $\sigma_2=\sqrt5$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Reconstruct using one outer product</span>

$$R_1=\sigma_1\mathbf u_1\mathbf v_1^T
=\frac32\begin{bmatrix}1&1\\3&3\end{bmatrix}
=\begin{bmatrix}3/2&3/2\\9/2&9/2\end{bmatrix}.$$

Its columns coincide, so it has rank $1$. Its shape is still $2\times2$.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check the discarded error</span>

$$R-R_1=\begin{bmatrix}3/2&-3/2\\-1/2&1/2\end{bmatrix}.$$

The squared entrywise norm is $9/4+9/4+1/4+1/4=5=\sigma_2^2$. The fraction of squared matrix norm retained is $45/(45+5)=90\%$. This is matrix approximation energy, not automatically centered statistical variance.
::::

::::{div} key-answer

One direction yields the optimal rank-at-most-one Frobenius approximation. Its squared error is $5$, so its Frobenius error is $\sqrt5$.
::::
:::::

:::{admonition} Shadow connection · What a smaller representation forgets
:class: connection

For $H(X,Y,Z)^T=(X,Y,Y,Z)^T$, the singular strengths are $\sqrt2,1,1$ with leading right direction $\mathbf e_Y$. Its rank-one approximation is

$$H_1=\begin{bmatrix}0&0&0\\0&1&0\\0&1&0\\0&0&0\end{bmatrix},\qquad H_1(X,Y,Z)^T=(0,Y,Y,0)^T.$$

It loses X and Z; $\|H-H_1\|_F^2=1^2+1^2=2$. At rank two, either tied unit-strength direction can be retained. This depends on the chosen measurement scaling; it does not reconstruct hidden geometry from arbitrary silhouettes.
:::

:::{admonition} Check your understanding
:class: checkpoint

If a 100×50 matrix is reduced to k=3 directions, what is the reconstructed matrix’s size? How many entries do its factors store?
:::

:::{dropdown} Check your reasoning

The reconstruction is still $100\times50$. Factors have sizes $100\times3$, $3\times3$ diagonal, $50\times3$ and store $300+3+150=453$ numbers, counting only the diagonal, instead of $5000$.
:::

::::{div} section-recap

**Takeaway:** Keep the strongest terms, preserve outer dimensions, sum the discarded squared strengths. Practice: Problems 19–21.
::::

(w5-recommendations)=
## I · Movie recommendations

::::{div} section-intro

**Learning goal:** Read user/item factors and distinguish an illustrative score from a validated missing-rating prediction.

<span class="source-label">Lecture PDF pages 34–40</span>
::::

A user-by-movie matrix records preferences: **rows are users, columns are films**. The first source picture gives the following data; a question mark means unobserved, never a rating of zero. The film names replace the posters so the example is readable without the image.

| User | Argo | Seven | Righteous Kill | Heat |
| --- | ---: | ---: | ---: | ---: |
| John | 5 | 1 | 3 | 5 |
| Tom | ? | ? | ? | 2 |
| Alice | 4 | ? | 3 | ? |

The motivating comparison is Alice liking a particular *Harry Potter* film and John liking *Fantastic Beasts*: a film-by-film description can miss shared preferences such as fantasy. A compact latent space may share information across films and reduce storage, but smaller size alone does not guarantee robustness or prevent overfitting. Learned singular directions also need not coincide with named genres.

:::{admonition} Model · One score is a weighted feature dot product
:class: definition

For a fully observed numerical matrix, truncated SVD gives $R_k=U_k\Sigma_kV_k^T$. User $i$ and item $j$ have $k$ coordinates, so

$$\widehat R_{ij}=\sum_{\ell=1}^k(U_k)_{i\ell}\sigma_\ell(V_k)_{j\ell}.$$

In a general latent-feature model, write instead $\widehat R=LWM^T$, where $L$ is $m\times k$ (users), $M$ is $n\times k$ (items), and diagonal $W$ is $k\times k$ (weights). Those factors need not have orthonormal columns or be an SVD. The source’s named-genre numbers below are this kind of **illustrative weighted feature model**.
:::

The next source example uses a different set of films. All its displayed ratings and factors are included below. Dashes indicate missing ratings, and “User m” is the last displayed user, not a third consecutive row in a complete dataset.

| User | The Notebook | Captain America | Seven | Forrest Gump |
| --- | ---: | ---: | ---: | ---: |
| User 1 | 5 | — | — | 5 |
| User 2 | — | 5 | — | 3 |
| … | … | … | … | … |
| User m | 1 | 5 | 5 | — |

**User-feature rows L**, in the order Drama, Thriller, Action, Fantasy:

| User | Drama | Thriller | Action | Fantasy |
| --- | ---: | ---: | ---: | ---: |
| User 1 | 0.7 | 0.2 | 0.1 | 0 |
| User 2 | 0 | 0.05 | 0.75 | 0.2 |
| User m | 0.4 | 0.3 | 0.2 | 0.1 |

**Diagonal weights:** $W=\operatorname{diag}(0.4,0.3,0.27,0.05)$.

**Movie-feature rows M**, using the same feature order:

| Movie | Drama | Thriller | Action | Fantasy |
| --- | ---: | ---: | ---: | ---: |
| The Notebook | 1.0 | 0 | 0 | 0 |
| Captain America | 0 | 0.1 | 0.7 | 0.2 |
| Seven | 0.5 | 0.5 | 0.1 | 0 |
| Forrest Gump | 0.98 | 0 | 0 | 0.03 |

Page 40 changes Captain America’s Fantasy entry from **0.2 to 0.9** while highlighting User 1’s missing score. Both source versions are recorded here; the calculation below is unaffected because that user’s Fantasy entry is zero.

:::::{admonition} Worked example 5.12 · The highlighted User 1 / Captain America entry
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Select matching feature rows</span>

Use $L_1=(0.7,0.2,0.1,0)$, $W=\operatorname{diag}(0.4,0.3,0.27,0.05)$ and $M_{\rm Captain}=(0,0.1,0.7,0.2)$. Match the same four feature positions in every factor.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Weight, multiply and sum</span>

$$\begin{aligned}
L_1WM_{\rm Captain}^T
&=0.7(0.4)(0)+0.2(0.3)(0.1)\\
&\quad+0.1(0.27)(0.7)+0(0.05)(0.2)\\
&=0+0.006+0.0189+0=0.0249.
\end{aligned}$$

Replacing the final 0.2 by the next slide’s 0.9 still gives a zero last term.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Check what the number represents</span>

This is a raw weighted feature score. These tables do not form a verified SVD or reproduce the displayed ratings: for example, User 1 / The Notebook gives $0.7(0.4)(1)=0.28$, not the observed $5$. No conversion to the 1–5 rating scale or fitting procedure is supplied.
::::

::::{div} key-answer

The arithmetic gives $0.0249$ as an illustrative feature score. It is not an established prediction of a 1–5 rating.
::::
:::::

```{figure} ../figures/lecture5/recommendation-flow.svg
:alt: A user by movie table with unknown entries leads to user feature rows, diagonal weights and movie feature rows. Matching rows yield a scalar weighted score. Unknown entries require fitting and evaluation rather than zero filling.

Read one score by matching a user row to a movie row through the feature weights. The complete numeric source tables appear above; the diagram summarizes their roles.
```

:::{admonition} Pitfall · Missing is not zero
:class: pitfall

Ordinary SVD requires an actual numerical matrix; it does not infer unknown ratings automatically. Filling blanks with zero changes the problem. A possible editorial extension is to fit factors only on observed entries $\Omega$, with regularization:

$$\min_{L,M}\sum_{(i,j)\in\Omega}\big(R_{ij}-(LM^T)_{ij}\big)^2
+\gamma(\|L\|_F^2+\|M\|_F^2),\qquad \gamma\ge0.$$

This is a separate learning problem, not an application of Eckart–Young to unknown data. Held-out observed ratings are needed to evaluate prediction quality. No such validation is supplied in the slides, and latent factors need not be identifiable as specific genres.
:::

:::{admonition} Check your understanding
:class: checkpoint

Does the best low-rank approximation of a zero-filled ratings table have to predict the missing ratings best?
:::

:::{dropdown} Check your reasoning

No. It minimizes reconstruction error for a table whose zeros you supplied, including treating missing entries as actual zero targets. That objective differs from fitting observed ratings and evaluating unknown ones.
:::

::::{div} section-recap

**Takeaway:** Know whether you are reconstructing known numbers or estimating missing ones. Practice: Problems 22–24.
::::

(w5-in-class)=
## J · The final in-class exercises

::::{div} section-intro

**Learning goal:** Carry out the two closing source problems and check their answers directly.

<span class="source-label">Lecture PDF pages 41–44</span>
::::

The reference/closing pages are followed by two additional exercises. They belong to the chapter: both original matrices and fully explained solutions are reproduced here.

:::::{admonition} Worked example 5.13 · Final eigenvalue exercise · All eigenvectors
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Solve the characteristic equation</span>

$$A=\begin{bmatrix}3&1\\4&6\end{bmatrix},\qquad
\det(A-\lambda I)=(3-\lambda)(6-\lambda)-4
=\lambda^2-9\lambda+14=(\lambda-7)(\lambda-2).$$

Thus the eigenvalues are $7$ and $2$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Find each complete eigenspace</span>

At $7$, $-4v_1+v_2=0$, so $E_7=\operatorname{span}\{(1,4)^T\}$. At $2$, $v_1+v_2=0$, so $E_2=\operatorname{span}\{(1,-1)^T\}$. All eigenvectors are the nonzero multiples in these spaces.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Verify against the original matrix</span>

$A(1,4)^T=(7,28)^T=7(1,4)^T$ and $A(1,-1)^T=(2,-2)^T=2(1,-1)^T$. Also $7+2=\operatorname{tr}A=9$ and $7\cdot2=\det A=14$.
::::

::::{div} key-answer

$\lambda=7$ with $\mathbf v=t(1,4)^T$, and $\lambda=2$ with $\mathbf v=s(1,-1)^T$, for nonzero real $t,s$.
::::
:::::

:::::{admonition} Worked example 5.14 · Final SVD exercise · Keep the minus sign
:class: example

::::{div} worked-step

<span class="step-label">Step 1 · Compute the Gram eigenvalues</span>

$$A=\begin{bmatrix}4&0\\3&-5\end{bmatrix},\qquad
A^TA=\begin{bmatrix}25&-15\\-15&25\end{bmatrix}.$$

$\det(A^TA-\mu I)=(25-\mu)^2-225=(\mu-40)(\mu-10)$.
Thus $\sigma_1=2\sqrt{10}$, $\sigma_2=\sqrt{10}$.
::::

::::{div} worked-step

<span class="step-label">Step 2 · Choose ordered right singular directions</span>

For $40$, $v_1+v_2=0$ gives $\mathbf v_1=(1,-1)^T/\sqrt2$. For $10$, $v_1-v_2=0$ gives $\mathbf v_2=(1,1)^T/\sqrt2$. Their squared lengths are one and their dot product is zero.
::::

::::{div} worked-step

<span class="step-label">Step 3 · Compute left directions from those exact choices</span>

$$\mathbf u_1=\frac{(4,8)^T/\sqrt2}{2\sqrt{10}}=(1,2)^T/\sqrt5,\qquad
\mathbf u_2=\frac{(4,-2)^T/\sqrt2}{\sqrt{10}}=(2,-1)^T/\sqrt5.$$

Hence $U=\frac1{\sqrt5}\begin{bmatrix}1&2\\2&-1\end{bmatrix}$,
$V=\frac1{\sqrt2}\begin{bmatrix}1&1\\-1&1\end{bmatrix}$, and $\Sigma=\operatorname{diag}(2\sqrt{10},\sqrt{10})$.
::::

::::{div} worked-step

<span class="step-label">Step 4 · Verify the signs by reconstruction</span>

$$U\Sigma V^T
=2\begin{bmatrix}1&-1\\2&-2\end{bmatrix}+\begin{bmatrix}2&2\\-1&-1\end{bmatrix}
=\begin{bmatrix}4&0\\3&-5\end{bmatrix}.$$

Both $U^TU$ and $V^TV$ equal $I_2$. A different simultaneous sign choice for a pair is valid if it preserves this product.
::::

::::{div} key-answer

This is a verified SVD of the original matrix, including its negative bottom-right entry.
::::
:::::

:::{admonition} Check your understanding
:class: checkpoint

How can two correct SVD answers have different signs?
:::

:::{dropdown} Check your reasoning

A positive singular value’s left and right vectors can both be negated, leaving the outer product unchanged. Compare orthogonality, ordered singular values and reconstruction, rather than insisting on one set of signs.
:::

::::{div} section-recap

**Takeaway:** Check the original map, not just the intermediate Gram matrix. Then attempt fresh mixed Problems 25–28.
::::

(w5-practice-applications)=
## Practice · Reduction and recommendations

Try these before opening the answers. Write the method and its check, not just the final vector.

```{include} practice.md
:start-after: <!-- applications:start -->
:end-before: <!-- applications:end -->
```

(w5-readiness)=
## Can you do this unaided?

Close the examples and attempt **Problems 25–28 in 25 minutes**. This is an editorial rehearsal, not an official exam time limit. Score each problem out of 4: **1** for a justified method and its conditions, **2** for correct calculation/reasoning, **1** for verification or interpretation. An editorial target is **14/16 with no unresolved conceptual error**. Use the diagnostic links to revise and retry fresh values; this threshold is not the course’s A cutoff.

- Can you find entire eigenspaces and decide whether they give a basis?
- Can you normalize, order and pair singular directions, including zero cases?
- Can you compute a truncated reconstruction and its discarded error?
- Can you explain why a missing-rating problem needs an additional model and validation?

```{include} practice.md
:start-after: <!-- mixed:start -->
:end-before: <!-- mixed:end -->
```

(w5-source-notes)=
## Source notes and next study step

This chapter develops **all 44 PDF pages** of Erisa Terolli’s CS 556
`WK5_Matrix_Decomposition.pdf`, including the handwritten page 22 and the final exercises on pages 43–44. Title pages and progressive reveals are combined; full problem data, readable tables, original labeled diagrams and working are included so no slide deck is needed alongside the website.

Matrix entries follow the rendered pages, because PDF extraction changes their order. The first two products are `[2,−1;1,2](2,3)=(1,8)` and `[2,1;2,3](1,2)=(4,8)`. The last exercises are `[3,1;4,6]` and `[4,0;3,−5]`. The source’s “0 eigenvectors” rotation means no **real** eigenvectors, and the stretch has two independent directions but infinitely many nonzero multiples. General diagonalization needs independence, not orthonormality. Symmetric matrices admit an orthonormal choice; arbitrary repeated-eigenvalue vectors need not be perpendicular. Full/compact SVD shapes and rectangular Gram products are distinguished explicitly.

The named-genre tables are reproduced with their numbers and the 0.2→0.9 change in Captain America’s Fantasy feature. They illustrate weighted factor scoring, not a verified SVD or a validated rating prediction. The earlier John/Tom/Alice table retains its observed scores and missing entries; poster art is replaced by readable film names. That source picture credits Di Noia and Ostuni (2015), *Recommender Systems and Linked Open Data*, chapter DOI 10.1007/978-3-319-21768-0_4. The slide’s Eckart–Young reference is preserved in the repository’s source audit; the norm and rank conventions used here are stated in Part H.

The complete numerical SVD on Page 2 develops **Linear_Algebra_Worksheet-1.pdf, Problem 14**; Practice 5 uses **Problem 13**. Other teaching examples, diagrams, counterexamples, precision fixes, the observed-entry objective and fresh mixed practice are editorial additions. Shadows use the established calibrated matched-point maps; film preferences are a different dataset, not world coordinates.

The exam topic list also requires statistics and PCA. Those are **not taught by this deck**; they now have a full destination in {ref}`Lecture 6 <w6-index>`. Uncentered approximation energy here is not automatically statistical variance. Use {ref}`the cheat sheet <w5-cheatsheet>` to rehearse these lecture methods, then return to earlier chapters for any failed prerequisite.
