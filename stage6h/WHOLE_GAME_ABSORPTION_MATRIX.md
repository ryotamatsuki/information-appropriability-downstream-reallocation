# Stage 6-H Whole-Game Absorption Matrix

## Frozen Stage 4-H game

- Players: upstream Bayesian decision maker `M`, information producers `S1,S2`.
- State: two-dimensional Gaussian.
- Signals: source-specific diagnostic directions.
- Precision: privately chosen effort.
- Reallocation: exogenous `eta` changes source-specific private return weights.
- Upstream action: posterior mean.
- Main result: at `q=1`, aggregate precision can rise while posterior quadratic loss rises; impossible at `q=0`.

| Dimension | Stage 4-H | Habermacher 2025 | Moresi 2000 | Myatt-Wallace 2019 | Myatt-Wallace 2015 | Multitask benchmark |
|---|---|---|---|---|---|---|
| Multiple strategic information producers | yes | yes | yes | yes | yes | not necessarily information |
| Multidimensional payoff-relevant object | yes | yes, two states/attributes | yes, two quality components | no, scalar fundamental | primarily scalar demand shock | multiple tasks |
| Endogenous costly source effort | yes | yes | yes | yes | yes | yes |
| Exogenous parameter shifts private returns/influence | eta | authority/influence regime | expertise/auction structure | network centrality/coordination weights | market/strategic environment | incentive weights |
| Information composition endogenous | yes | yes | yes | yes, source mix | yes, source mix/publicness | effort composition |
| Common downstream/upstream Bayesian decision | one M | organization decisions | auction allocation/bids | own network actions | Cournot outputs | principal output/tasks |
| Exact total-precision-up / posterior-loss-up result | yes | not verified | not posterior-loss metric; higher research + worse allocation | not verified | not exact; quantity/use inefficiencies | generic effort-level/allocation divergence |
| Scalar/collinear impossibility theorem | yes | no direct counterpart verified | no | no | no | generic single-task benchmark |

## Single-prior-model absorption

No inspected single prior model reproduces every Stage 4-H player, information, timing and payoff object through direct relabeling or parameter restriction. Therefore:

`WHOLE-GAME EXACT ABSORPTION BY ONE PRIOR: NO`.

This does **not** imply novelty survival.

## Stronger result-level reduction

At the only benchmark where H-P1 is analytically proved, `q=1`, the posterior loss is

`L = 1/(1+e1) + 1/(1+e2)`

and therefore

`G = e1/(1+e1) + e2/(1+e2)`.

Private payoffs become

`pi_1 = b(1-eta) g(e1) - k1 e1^2/2`,

`pi_2 = b eta g(e2) - k2 e2^2/2`,

with `g(e)=e/(1+e)`.

Thus the two information producers are strategically independent at q=1. There is no full-game feedback between `S1` and `S2`; eta simply rotates independent incentive weights across two concave tasks.

The H-P1 inequalities are exactly the conditions under which the raw effort gain on one task exceeds the raw effort loss on the other, while the marginal-output-weighted gain is smaller than the marginal-output-weighted loss. This logic survives if the two diagnostic information dimensions are replaced by any two separable concave productive tasks.

Therefore the proved theorem is not protected by the absence of a single full-game predecessor. It is an immediate generic allocation result at a nested benchmark in which the putative strategic information interaction disappears.

## Whole-game verdict

- Literal whole-game prior identity: `NO`.
- Full-model-only interaction theorem: `NO` for the proved contribution, because H-P1 is proved at q=1 where cross-source interaction is zero.
- Component stitching required to describe the original labels: `YES`.
- Economic novelty survives label stripping: `NO`.

Canonical finding: `NO EXACT ABSORPTION, BUT CONTRIBUTION-GRADE ABSORPTION BY IMMEDIATE GENERIC REDUCTION`.