# Stage 6-H Optimal-Design Threat

## Finding

The Stage 4 loss criterion

`L = tr(P^{-1})`

is a standard Bayesian A-optimal-design criterion: A-optimality minimizes the trace of posterior covariance, equivalently average posterior variance under linear-Gaussian quadratic-loss settings.

Relevant mathematical-design literature includes Alexanderian, Petra, Stadler & Ghattas and subsequent A-optimal sensor-allocation work. This literature establishes that measurement directions/weights, not merely a scalar count or sum of precisions, determine posterior risk.

Classification: `COMPONENT OVERLAP`, not full economic-game absorption.

## Stronger threat at q=1

At orthogonal directions:

`P = diag(1+e1, 1+e2)`

so

`L = 1/(1+e1)+1/(1+e2)`.

This is a separable symmetric convex loss in the directional precision vector and a separable concave information benefit

`G = e1/(1+e1)+e2/(1+e2)`.

Therefore, for a fixed total precision, a more uneven directional allocation raises L. This is a direct majorization/Jensen consequence and does not require a new information-economics theorem.

The project does not claim that this geometry is new. The Stage-6 problem is whether private reallocation combined with this geometry creates new economics.

## Corollary assessment

At q=1 private reallocation does not interact strategically across sources. It simply changes two independent coefficients:

`b(1-eta)` and `b eta`.

Thus:

1. standard incentive comparative statics determine `e1_eta<0<e2_eta`;
2. sufficiently low `k2` makes the raw gain in e2 exceed the loss in e1, so total effort rises;
3. diminishing marginal value `1/(1+e)^2` means shifting effort toward an already-high-precision direction can reduce total useful information, so L rises.

No nonseparable Bayesian interaction is required for H-P1 at the proved benchmark.

## Verdict

`OPTIMAL-DESIGN COROLLARY TEST: FAIL FOR NOVELTY`.

Optimal design alone does not reproduce the decentralized equilibrium, so it is not `EXACT PRIOR ART`. But once combined with the elementary independent incentive responses in the frozen q=1 game, H-P1 is an immediate result of standard concavity/majorization logic. The information geometry is real; it is not a new economic mechanism.