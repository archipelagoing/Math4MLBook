> Current choice: the owner selected **shadows** for the textbook. The comparison below records the rationale; earlier statements that knitting/crochet remains primary are superseded.

# Colored Light versus Multiple Shadows — The Strongest Case for Each

2026-10-26 · Editorial comparison, not measured learning evidence
[Colored-light canon](../systems/colored-light/canon.md) · [Shadow canon](../systems/shadows/canon.md)
[Light rubric](../systems/colored-light/rubric.md) · [Shadow rubric](../systems/shadows/rubric.md)

## The shared commission

Prepare a student for an A across the actual five lectures. Both candidates must
teach the same mathematics, land in formal reasoning, and prepare the student to
handle unfamiliar problems. Neither earns credit merely for an attractive story.
Both are current references alongside the other systems. This document compares
only light and shadows; knitting/crochet remains the primary thread unless the
owner makes a separate choice. Development history is maintained separately.

## The most compelling case for colored light

**The hook:** “You can change what the light contains without changing what the
meter records.” Actual color science distinguishes spectra from color responses;
our four-band toy sensor makes that loss of information solvable by hand.

**The intellectual payoff:** The student stops treating a measurement as the
thing itself. Null space is no longer an empty algebraic term: it contains genuine
underlying differences the observer cannot distinguish. The same idea deepens
into calibration, physical gamut, inverse problems, SVD, and the difference between
variation in a record and truth about its source.

**The coherent journey:**

1. Adjust lamps: vector entries and combinations have a recognizable action.
2. Measure light: a matrix has a purpose, units, input, and output.
3. Find two spectra with the same readings: rank and null space answer a real question.
4. Restrict available lamps: span and physical feasibility are different questions.
5. Approximate a target: projection and residual determine the closest response.
6. Decompose the sensor: SVD describes which spectral distinctions survive.
7. Compare repeated readings: centered covariance/PCA summarizes variation.

**Its best exam-preparation contribution:** It makes students ask “which map?” and
“in which space?” A spectrum-to-sensor map can be surjective while a lamp-to-sensor
map is not; both fit the same scene. A square invertible calibration does not undo
the original loss of spectral information. These distinctions are frequent sources
of incorrect matrix reasoning.

**Its artistic advantage:** Spectral-bar diagrams, response arrows, lamp controls,
and paired readings could create a beautiful recurring visual language. The book's
hot pink/green accents can label lamps, while red/yellow retain their semantic roles.
But diagram hex colors must never pretend to reproduce actual spectral matching;
use labeled numerical records as the evidence.

**The strongest objection:** “I cannot actually see a spectrum.” The first lesson
must teach the difference between power-by-wavelength and a three-number response.
A computer display cannot prove the proposed real-world match. This adds a genuine
prerequisite before the mathematical payoff.

**Answer to that objection:** Start with four explicitly numbered band sliders and
three meters, not advanced colorimetry. Show A's two exact nonnegative spectra and
their identical readings. Cite real metamerism as motivation, while labeling the
exercise as a toy sensor. Never require perceptual judgments for exam reasoning.

## The most compelling case for multiple shadows

**The hook:** “Move the bead toward the screen. The shadow stays still. Look from
the side: the missing motion appears.” The student can imagine or demonstrate this
before knowing a matrix definition.

**The intellectual payoff:** Null space becomes a direction of invisibility;
independence becomes the question of whether another view sees something new.
Systems, rank, consistency, projection, and reconstruction become different views
of the same physical question. Adding measurements is visibly different from adding
independent information.

**The coherent journey:**

1. Locate a marked bead: coordinates have a physical reference.
2. Observe one screen: a rectangular matrix loses depth.
3. Add a second screen: a stacked system can recover the missing coordinate.
4. Compare inconsistent marks: least squares reconciles observations.
5. Make the screens nearly parallel: a weak measurement direction appears.
6. Decompose the view map: SVD gives a quantitative account of the geometry.
7. Compare point collections: PCA describes the dominant measured directions.

**Its best exam-preparation contribution:** It gives the student a reliable mental
check on dimensions and the four spaces. Input null vectors are invisible motions;
output left-null vectors detect incompatible observations. A 2-by-3 view is not the
same as a 3-by-3 orthogonal projector, and a 4-by-3 stacked view has a left inverse
without a two-sided inverse. These are concrete checks on exam answers.

**Its artistic advantage:** One bead, two labeled screens, dotted projection rays,
and a highlighted invisible direction can recur in every chapter. Animating a bead
along a null direction or making two views nearly parallel could reveal the idea
without paragraphs of explanation. Static before/after panels can do the same job.

**The strongest objection:** “Shadows do not reconstruct arbitrary objects.” True:
silhouettes and occlusion are more complicated than a linear point map.

**Answer to that objection:** Use matched marked points in a transparent/open frame,
parallel rays, fixed axes, and a declared origin. The target is point coordinates,
not reconstructing any solid object from its outline. This narrowed scene is both
recognizable and mathematically honest.

## Head to head against the actual course

These are editorial judgments about the drafts, not experimental scores.
Exact pages are in [the course map](../course-map.md).

| Course demand | Colored light | Multiple shadows | Editorial edge |
| --- | --- | --- | --- |
| W1 vectors, combinations, matrix products | Source intensities and linear responses are direct; spectral versus response coordinates need introduction. | Point coordinates, rotations, and screen axes are familiar; adding points is explained as records/displacements. | Shadows for immediate spatial recognition; light for additive-mixture intuition. |
| W2 systems, elimination, inverse, determinant | Solve lamp settings; distinguish square calibration from rectangular sensing and physical feasibility. | Reconstruct a point from matched screens; distinguish missing depth from redundant equations. | Shadows for the simplest first hand calculation. |
| W3 spaces, rank, basis, complete solutions | A continuous family of distinct spectra shares a record; lamp gamut adds a useful constraint distinction. | Invisible depth and repeated views give immediate rank/nullity explanations. | Shadows for geometric clarity; light for the most surprising inverse ambiguity. |
| W4 projection, least squares, Gram–Schmidt | Fit a target unavailable from the lamp set; signal-space geometry must be declared. | Projection is already the scene; noisy shared-coordinate readings give a simple exact fit. | Shadows. |
| W5 eigenvectors versus singular vectors | A band filter is a same-space map; sensor SVD separates source/output directions. | Rotation/projector eigenstructure contrasts with rectangular observation SVD; view angle explains weak modes. | Both strong; shadows has the clearest near-redundancy demonstration. |
| Statistics/PCA topic-list bridge | Measured light/spectra offer high-dimensional variation and perceptual caveats. | Point clouds offer visible principal axes and an intuitive reconstructed approximation. | Shadows for a first diagram; light for extending to high-dimensional observations. |
| Recommendation subsection | Must introduce a separate viewer-by-scene rating table. | Must introduce a separate viewer-by-object rating table. | Tie; neither should disguise ratings as physical measurements. |
| Surprise and memorability | Same measured color can conceal different underlying spectra. | A hidden movement becomes visible only from another direction. | Light for surprise; shadows for an immediately imaginable demonstration. |
| Accessible presentation | Must avoid depending on color discrimination or a calibrated display. | Must avoid depending on stereoscopic vision or unlabeled depth cues. | Both require labels, patterns, captions, and numerical records. |
| Risk of misleading extension | Toy sensors mistaken for human vision; gamma, gamut, or perceived distance overlooked. | Silhouettes/perspective mistaken for linear matched-point reconstruction. | Different risks; both explicit in the canons/rubrics. |

## Two parallel five-minute teaching samples

These provide a concrete comparison before writing whole chapters.

**Light sample:** Present A from the light canon and two nonnegative spectra.
Have the student compute both outputs, subtract the spectra, identify a nonzero
null vector, and explain what cannot be recovered. Transfer: give a fresh 2-by-3
map and ask for a null direction without mentioning light.

**Shadow sample:** Present O from the shadow canon and two positions differing
only in Z. Have the student compute both outputs, describe all consistent points,
then add an independent view and explain what changed. Transfer: give the same
fresh 2-by-3 map used after the light sample.

For a fair comparison, match teaching time, mathematical difficulty, notation, and
feedback. Use equivalent but different-number problems, counterbalance lens order
when feasible, and record unaided reasoning and misconceptions. Repeating the same
question in sequence can measure practice effects instead of the analogy.

**Readiness evidence to collect:** Can the student locate input/output spaces,
compute rank/nullity, identify nonuniqueness, distinguish coordinate change from
information loss, and justify a projection or reconstruction without the metaphor?
No such learner evidence has been collected yet.

## The shared insight that connects both to every other lens

A stitch ledger can hide the arrangement of stitches. A population report can hide
infection status. A coarse chart can hide marker locations. A color response can
hide spectral differences. A shadow can hide depth.

The shared statement is exact: `A(x+v)=Ax` for `v∈N(A)`. Each lens supplies a
different physical reason and has its own feasible domain, units, and dimensions.
The map decides what can be distinguished; algebra explains the consequences.
That is a coherent cross-lens connection, not permission to equate different objects.

## Recommendation to take into the comparison

**If choosing one teaching backbone for this exam today, my provisional choice is
shadows.** It starts with less domain knowledge and directly supports the geometric
spine of Weeks 1–5, especially the four spaces and projection. **Light is the
stronger opening surprise and a particularly powerful second explanation of
nonunique observation.**

Both have a complete lecture route, checked numerical anchors, and separate rubrics.
The final choice should follow review of the paired teaching samples, not a claim
that editorial preference proves better student performance. Knitting/crochet remains
the existing primary thread until the owner chooses otherwise.
