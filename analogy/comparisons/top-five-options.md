# Five Original Analogy Options — Ranked Against This Course

2026-10-26 · [Exact lecture connections and cross-lens map](../course-map.md)

These are my five strongest additional options after developing knitting/crochet,
bacteria/viruses, the zodiac wheel, and pottery. The ranking is editorial judgment
about mathematical closeness, recognition, surprise, and continuity—not a measured
claim about learning effectiveness. Light and shadows have current system references; sound, mobile, and dance remain
candidates. This ranking is editorial judgment, not a record of selected primary threads. Knitting/crochet remains the established primary lens.

## 1. Finding one voice in a crowded room

**Recognizable scene:** Two people speak; microphones hear different mixtures.
You change gains, record waveforms, compare channels, and try to recover a voice.

**Why it is first:** The same sound mixture naturally raises the whole course's
question: what information survives a transformation, and what can be recovered?
Samples are vectors; microphone gains form a matrix; duplicate recordings lose
independent information; noise leads to least squares; stereo mid/side gives a
concrete basis change; SVD separates input directions, strengths, and output modes.
The resemblance is unusually close to an actual linear signal model.

**Permanent scene:** Short, aligned recording blocks, two sources, and declared
microphone channels. Use `y=A s+e` for an explicitly idealized instantaneous mixture.
Real delay/reverberation requires a different, possibly block/convolutional map;
clipping and nonlinear processing break the simple model.

**Surprise:** Cancellation can make a nonzero source combination disappear from a
particular recording. Recovering a loud sound is not the same as identifying a speaker.

**Weak spot:** SVD/PCA alone does not recover arbitrary independent speakers. Use a
known/calibrated A for inversion, distinguish orthogonality from independence, and
avoid claiming actual noise cancellation from an unvalidated toy projection.
The [DSP Guide's linear-system chapter](https://www.dspguide.com/CH5.PDF) supplies
the superposition foundation; the concrete microphone examples would need review.

## 2. Making the same color from different light

**Recognizable scene:** Shine colored lights on a white screen; adjust their
intensities; measure the result. Compare a measured spectrum with a three-channel
color record. Light, not paint mixing, is the anchor.

**Why it is second:** It connects linear combinations, measurement matrices, gamut,
rank, null spaces, inverse problems, and approximation to something instantly visible.
A sampled spectrum can have more coordinates than the color record; different
spectra can produce the same three responses. That is a memorable information-loss
story, not just “RGB is a vector.”

**Permanent scene:** Declared spectral samples, fixed linear sensor/matching
responses, and unclipped linear-light values. Distinguish display primaries, sensor
channels, and spectral wavelengths. Gamma-encoded image values are not linear light.

**Surprise:** The same recorded color need not mean the same spectrum. The
[PBRT color chapter](https://pbr-book.org/4ed/Radiometry,_Spectra,_and_Color/Color)
describes both additive tristimulus records and metameric spectra.

**Weak spot:** Perceptual distance is not automatically RGB Euclidean distance;
negative spectral power is not physical, and subtractive pigment mixing is a
different mechanism. Eigenmodes refer to a declared filter/map, not a color's personality.

## 3. Reconstructing an object from several shadows

**Recognizable scene:** Shine parallel light at marked points of an object and
observe their orthographic shadows on screens. Rotate the object, add another
view, and ask what depth information remains hidden.

**Why it is third:** Projection, null space, rank, consistency of views, rotations,
change of coordinates, and noisy reconstruction become visible. SVD identifies
which spatial directions the views preserve strongly, weakly, or not at all.

**Permanent scene:** Tracked point coordinates under declared orthographic views,
not arbitrary silhouette images. One view loses a coordinate; stacked independent
views can restore information. Use known point correspondence.

**Surprise:** Different 3D points can cast the same shadow; a second view helps
only if it contributes an independent measurement. The
[Scratchapixel orthographic derivation](https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/orthographic-projection-matrix.html)
supports the geometric setting.

**Weak spot:** Real perspective involves division; silhouettes/occlusion and unknown
correspondence add difficulties outside the simple linear point model. Rotating a
shadow picture does not generally recover the missing depth.

## 4. Balancing a hanging mobile, then watching it sway

**Recognizable scene:** Weights hang from bars at marked lever arms. Move a weight,
balance a bar, balance the connected structure, then gently disturb it.

**Why it is fourth:** Static force/torque equations offer concrete linear systems
in unknown masses with fixed geometry. Redundant observations explain rank and
null spaces. Small coupled oscillations supply eigen-directions and normal modes;
recorded motions supply SVD and PCA.

**Permanent scene:** Fixed geometry for equilibrium accounting; a separately stated
small-displacement mechanical model for motion. Distinguish a constraint matrix
from mass and stiffness matrices, and state any coordinate mass-weighting.

**Surprise:** An apparently complicated swaying motion can be assembled from a few
coordinated modes. [MIT's coupled-oscillator lecture](https://ocw.mit.edu/courses/res-8-009-introduction-to-oscillations-and-waves-summer-2017/mitres_8_009su17_lec6.pdf)
supports that mathematical mechanism; applying it to a specific mobile needs a derived model.

**Weak spot:** Moving lever arms and unknown weights together introduces products;
large rotations are nonlinear. Not every hanging mobile has the same symmetric
matrix or orthogonal modes in raw coordinates.

## 5. Learning a dance from motion-capture dots

**Recognizable scene:** Dots track wrists, elbows, knees, and feet. Record a pose,
change camera coordinates, compare two takes, and compress a long recording into
recurring motion patterns.

**Why it is fifth:** Coordinates, transformations, noisy observation, reconstruction,
and variation modes become bodily and familiar. A motion dataset also connects
naturally to the machine-learning end of the course.

**Permanent scene:** Aligned Cartesian marker records in a fixed unit/frame. Declare
whether rows mean frames or whole time-normalized takes. Do not silently switch
from joint positions to angles or from static poses to trajectories.

**Surprise:** A few data directions can summarize many recorded coordinates, but
an average or component direction need not itself be a physically possible pose.
[CMU's motion-capture database](https://mocap.cs.cmu.edu/) establishes the recording
context; [CMU research](https://www.cs.cmu.edu/~softagents/papers/p475-sukthankar.pdf)
uses PCA for pose reduction.

**Weak spot:** Joint constraints and rotations are not globally linear; alignment,
time warping, and missing markers matter. A leading PCA direction is not a universal
“basic dance move.” Eigenmodes require a stated linear map, not poetic labels.

## Comparison across the five actual lectures

Exact topic-level routes, including every current lens, are in the course map.
This table summarizes the through-line rather than replacing those destinations.

| Candidate | Week 1: vectors/maps | Week 2: systems/inverse | Week 3: spaces/rank/bases | Week 4: projections/fitting | Week 5: eigen/SVD | Exam statistics/PCA bridge |
| --- | --- | --- | --- | --- | --- | --- |
| Sound | Sample/gain/mix | Known-mixture unmixing | Lost source combinations, mid/side | Template fit, residual | Channel modes and strengths | Centered recording variation |
| Light | Spectra, brightness, sensor map | Match measured response | Same color, different spectra | Best attainable response | Filter/sensor modes | Variation across spectra/colors |
| Shadows | Points, rotations, views | Recover coordinates | Invisible depth, independent views | Fit noisy screen coordinates | Strong/weak view directions | Dominant point-cloud variation |
| Mobile | Loads, lever-arm coefficients | Balance equations | Redundant constraints, remaining freedom | Fit noisy loads/positions | Small-oscillation modes | Variation across measured trials |
| Dance | Marker poses, coordinate frames | Solve declared observation map | Hidden markers/directions, pose basis | Fit observed marker records | Linear-map modes, data SVD | Dominant recorded variation |

**My choice:** Sound for strongest overall continuity; light for the most surprising
null-space insight; shadows for the quickest geometric explanation. Mobile and
dance are strong alternatives whose physical constraints demand more explanation.
No option eliminates the need for formal proofs, exceptional cases, and exam transfer.
