# Lecture 6 · Source and assessment coverage

Date: 2026-10-27. Source: Erisa Terolli’s
`resources/lectures/WK6_PCA.pdf`, **all 39 PDF pages**.
All extracted text and all rendered pages were inspected, including image-only
sequences. `Week 6 Slides - PCA (1).pdf` is byte-for-byte identical: SHA-256
`d527cb8c56e1f455db6971c45775a5b9907015b3d20c597e60a39e292b8e430a`.
Both original files are preserved; they are one mathematical source, not two
separate lectures. Newly supplied Week 8 files are outside this task.

## Complete slide map

| PDF pages | Source substance retained | Textbook destination |
| --- | --- | --- |
| 1–4 | Title; 300×300×3=270000 RGB image dimensions, sample pixel channels, high-dimensional challenges, near-plane cloud | A, Example 6.1 and original dimensions diagram; portrait replaced by a pixel/vector schematic |
| 5 | Mean definition and {3,7,5}→5 | B, Example 6.2, column-mean and centering notation |
| 6 | Variance definition, sample m−1 denominator, deviations from mean 5, sum 8 and variance 4 | C, Example 6.3; sample standard deviation 2 made explicit |
| 7–8 | Paired covariance, units/sign/linear relationship, Cov(x,x)=Var(x), two-feature covariance matrix | D definition/formulas, Example 6.4, n×n Gram form and PSD explanation |
| 9–12 | Pizza/gym illustration and negative-correlation scatter; long and perpendicular short directions | E prose, complete declared toy dataset and pizza/gym figure |
| 13–14 | Re-express cloud in orthogonal axes, then keep one coordinate | E, Example 6.5 and three-stage figure; change of basis distinguished from discarding coordinates |
| 15 | Project centered data to orthogonal directions preserving variance; projected points and residual segments | F definition and original projection-objective diagram |
| 16–17 | Minimize average squared distance to k-subspace; unit-vector projection triangle; Pythagorean identity; maximize squared projection | F equivalent objectives and derivation, Example 6.6, labeled triangle |
| 18–19 | Sum squared projections over m rows/k orthonormal directions; choose long versus short axis for an elongated cloud | F equations/checkpoint and figure; orthonormality constraints explicit |
| 20 | Centered observations as rows, Xv as the score column | G row-score notation; H worked scores and n/k/m shape conventions |
| 21 | Quadratic form, spectral theorem, XᵀX=(m−1)C, same eigenvectors with different eigenvalue scales | G proof; 1/m objective factor retained in values, removed only in argmax reasoning |
| 22 | w=Qᵀv, unit norm preserved; weighted sum λⱼwⱼ² bounded by largest λ; top-k covariance eigenvectors | G Rayleigh proof and tie/sign caveats; marked-point Example 6.7 |
| 23–24 | Algorithm and full student table: (10,90),(6,80),(20,100), mean (12,90), centered rows, C=[52,70;70,100], roots 150,2, source vectors (5/7,1),(−7/5,1), normalized PC, three scores | H, Example 6.8 Steps 1–4; student-PCA diagram; exact values retained before rounding |
| 25–26 | Variance-retention quiz 50/75/90/99%; fraction 150/152≈98.7%; 90–95% heuristic; original variances 52,100 versus PC variances 150,2 | I, Example 6.9 and variance-budget redraw; reconstruction/error accounting developed explicitly |
| 27–32 | Six stages: raw scatter, centering, standardizing, eigendirections, projection, undo scaling/centering | J recipe, all six panels in original preprocessing diagram, numerical Example 6.10 |
| 33–34 | Empirical genetics PC plot, country-coded observations, Europe map reveal; Novembre et al. credit | K, Example 6.11 and original empirical figure extracted from p.34, with alt text and explanatory caption |
| 35 | Face≈mean+weighted eigenfaces, pixel-feature vectors, scores/storage, illustrative ~600-pixel faces, Turk/Pentland and LFW credit; connection to opening 270000-entry image | K definition, original extracted face illustration, Example 6.12 and storage practice |
| 36 | Outlier changes direction; linear PCA misses curved structure; low-variance direction can carry class signal | L, three-panel original redraw; Examples 6.13–6.14 and curve explanation |
| 37–39 | Top covariance eigenvectors, eigenvalues as retained variation, centering/scaling, linear/outlier cautions; closing and reference list | L synthesis/checkpoint, source notes, TL;DR and bibliography below |

## Representation and precision decisions

- Slides define sample variance/covariance using m−1, although variance is labeled
  σ². The textbook uses s² for this sample convention, defines standard deviation,
  and contrasts the m denominator. The reconstruction objective remains averaged
  by m: sample discarded variance, total SSE and average squared error are distinct.
- Data are m×n with row observations and column features. Mean is a column vector;
  centering subtracts 1μᵀ. Covariance is XᵀX/(m−1), not XXᵀ/(m−1).
- Directions/loadings, per-observation scores and reconstructed original-unit
  vectors are separately named and sized. Orthogonality, unit length, mean restoration,
  optional scale restoration, training preprocessing, rank bounds, ties, sign
  freedom, constant features and zero-total-variance fractions are explicit.
- The source’s student eigenvectors are retained as written and as equivalent
  integer directions. Exact scores are (−10,−100,110)/√74; correctly rounded values
  are approximately (−1.1625,−11.6248,12.7872). Display truncation in the slide is
  not treated as different source data. The reconstruction SSE is exactly 4,
  average squared error 4/3 and discarded sample variance 2.
- Source pages 21–22 describe the same optimizer under positive rescaling, not
  equality of differently normalized objective values. Top-direction uniqueness
  is qualified for signs and tied roots. Zero covariance/uncorrelated scores are
  not equated with statistical independence.
- The 90–95% selection suggestion is a heuristic, not a universal task guarantee
  or official grade cutoff. Standardization changes the fitting metric; undoing
  it does not generally preserve unweighted Euclidean perpendicularity.
- The image/scatter/preprocessing/failure SVGs use explicitly declared schematics
  and toy coordinates because no source scatter arrays are supplied. They retain
  the geometric mechanisms, not invented claims of empirical replication.
- The genetics and eigenface PNGs are unchanged embedded images extracted from
  the supplied PDF. Captions preserve credits and distinguish interpretation from
  unavailable raw-data reproduction. Their illustrative formulas are also typeset
  independently in the textbook; screenshots do not replace mathematical exposition.

## Architecture and practice blueprint

| Page | Ordered parts | Worked examples and practice |
| --- | --- | --- |
| 1 · Statistics & PCA geometry | A–E, source 1–14 | Examples 6.1–6.5, Problems 1–8 |
| 2 · Compute principal components | F–I, source 15–26 | Examples 6.6–6.9, Problems 9–16 |
| 3 · Scaling, applications & pitfalls | J–L, source 27–39 | Examples 6.10–6.14, Problems 17–24 and mixed 25–28 |
| 4 · TL;DR | Review | Statistics, shape table, formulas/conditions, seven-step method, fresh Example 6.15 |

Twelve part goals/source ranges/checkpoints/takeaways, fifteen numbered highlighted
examples, seven original SVGs plus two credited source images, and 28 integrated
questions with nearby explained solutions, specific diagnosis and revision/retry
links. The four mixed tasks have fresh data (not copied worked arrays), no hints,
and editorial 25-minute/16-point guidance. They do not establish official exam
rules, a grading cutoff or an actual student outcome.

Mean, variance, standard deviation, covariance and PCA in `MidtermTopics.md` now
have source-based teaching, independent practice and a local mixed check in Week 6.
The centered-SVD relation connects to Week 5. No new comprehensive HW/practice-exam
question audit is claimed; cumulative blueprint/mock work and existing Lecture 2
fresh-variant tasks remain open.

## Source bibliography

Recorded from source page 39; not a claim to have fetched or independently
replicated the cited external sources:

- Stanford CS168: `https://web.stanford.edu/class/cs168/l/l7.pdf` and
  `https://web.stanford.edu/class/cs168/l/l8.pdf`.
- Source video: `https://www.youtube.com/watch?v=g-Hb26agBFg&t=1121s`.
- Turk, M. and Pentland, A. “Eigenfaces for recognition.” Journal of Cognitive
  Neuroscience 3.1 (1991), 71–86.
- Novembre, J. et al. “Genes mirror geography within Europe.” Nature 456.7218
  (2008), 98–101.
- Huang, G. B., Ramesh, M., Berg, T. and Learned-Miller, E. Labeled Faces in the
  Wild. University of Massachusetts Amherst Technical Report 07-49 (2007).
- Deisenroth, M. P., Faisal, A. A. and Ong, C. S. Mathematics for Machine Learning.
  Cambridge University Press (2020).
