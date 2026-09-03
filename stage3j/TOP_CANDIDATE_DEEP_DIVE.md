# Stage 3-J TOP Candidate Deep Dive

## Preferred candidate

B — Endogenous Customer Selection / Endogenous Sampling.

## Core distinction

The model must not treat downstream information as an exogenous signal whose precision is chosen directly. The downstream commercial decision must change the **statistical likelihood of feedback** by selecting which customer types enter the observed sample.

This is the minimal information-specific object:

`commercial screening c -> F(z | purchase,c) -> Pr(y | theta,c)`.

The manufacturer knows `c` and updates rationally. There is no behavioral-bias or naive-inference assumption.

## Minimal strategic architecture

### Players

- upstream manufacturer `M`;
- downstream retailer/dealer `R`;
- continuum or mass of short-lived consumers, each with private taste `z`.

### State

Binary product state `theta in {0,1}` with prior `mu_0`.

Interpretation may be product fit/quality dimension relevant to a later redesign. Stage 4 must use the most neutral label possible until the algebra works.

### First-period screening

`R` chooses one scalar commercial action `c`, preferably a price or purchase cutoff. Consumers buy when a simple utility condition holds, producing a selected distribution

`F_c(z) = F(z | purchase under c)`.

### Feedback

Only purchasers generate feedback `y`.

Feedback probability depends on both the state and consumer type:

`Pr(y=1 | theta,z)`.

Therefore the likelihood faced by `M` is

`ell_theta(y;c) = integral Pr(y | theta,z) dF_c(z)`.

The key derivative is not mechanically imposed signal precision; it is how ordinary screening changes the likelihood ratio

`ell_1(y;c)/ell_0(y;c)`.

### Bayesian adaptation

`M` observes the screening rule and feedback, updates correctly, and chooses a minimal adaptation action `a`. A binary adaptation threshold or quadratic posterior-matching action is preferred depending on tractability.

### Vertical feedback

`R` earns a continuation share from `M`'s adaptation outcome. Hence `R` chooses `c` anticipating how its current customer selection changes the informational basis of `M`'s later adaptation.

Full loop:

`c -> selected customer distribution -> selected-feedback likelihood -> posterior -> M adaptation -> R continuation value -> c`.

## Why this is not Acemoglu et al. (2022)

Acemoglu et al. already establishes that reviews are selected because customer purchase decisions depend on current information, and this selection changes learning speed. Candidate B cannot claim that selection effect.

The proposed new strategic object is a separate vertical actor `R` that chooses the commercial screening rule and internalizes only its private share of a subsequent `M` adaptation benefit. Thus the selection rule itself is an equilibrium strategic response to the value of upstream learning.

If Stage 4 cannot make this extra arrow matter, B is killed.

## Why this is not Hu et al. (2021)

Hu et al. supplies a retailer-manufacturer information-acquisition/quality architecture, but information acquisition is an explicit strategic research/sharing choice. Candidate B instead makes an ordinary commercial action alter the endogenous likelihood through selected customers. If Stage 4 effectively introduces a separate information-acquisition effort, it has drifted back into the absorbed family and must stop.

## Why this is not Yan et al. (2026)

Yan et al. connects reviews, dynamic pricing, learning and product-quality refinement. Candidate B must retain a vertical incentive wedge: the downstream selector and upstream adapter are distinct decision makers. If the two can be integrated without changing the headline result, the strategic contribution is too weak.

## Candidate propositions for Stage 4

### B-P1 — Selection-feedback comparative-static divergence

There exists a parameter region in which increasing the downstream actor's continuation stake in correct upstream adaptation changes the equilibrium screening action in the opposite direction, or across a different threshold, from the identical fixed-likelihood benchmark.

The theorem must be caused by `d ell_theta(y;c)/dc`, not by a direct continuation-profit term alone.

### B-P2 — Volume/informativeness divergence, secondary only

There may exist a region where the commercial action increases expected feedback volume while reducing expected posterior decision value because selected customer composition becomes less informative. Keep only if the result is an equilibrium implication of the vertical feedback and not simply the Acemoglu selection effect.

### B-W1 — Decentralized versus integrated screening

The retailer's equilibrium screening differs from integrated screening because it captures only part of the learning/adaptation surplus. Stage 4 must solve the direction; do not assume over- or under-screening.

## Minimum empirical implication

Holding the number of reviews/feedback observations fixed, downstream commercial screening should change the predictive content of feedback for later manufacturer adaptation through the composition of customers who generated it.

A generic effort model cannot produce this likelihood-composition prediction.

## Fatal Stage-4 attacks

1. If B-P1 survives with `ell_theta(y;c)` held fixed, kill.
2. If a deterministic multi-task/output analogue produces B-P1, kill.
3. If the manufacturer adaptation stage is only cosmetic and can be integrated out without changing retailer screening incentives, kill.
4. If a close review-selection or vertical information paper directly nests the solved minimal game, kill.
5. If tractability requires contracts, disclosure, two strategic channels or behavioral inference simultaneously, kill.

## Deep-dive verdict

`PREFERRED — GO TO ONE MINIMAL STAGE-4 HARD KILL`.