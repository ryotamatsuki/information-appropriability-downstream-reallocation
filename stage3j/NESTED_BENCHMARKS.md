# Stage 3-J Nested Benchmarks

The preferred B architecture must be tested against benchmarks that remove different arrows rather than merely simplify notation.

## B full model

Players: manufacturer `M`, retailer/dealer `R`, short-lived heterogeneous consumers.

State: binary payoff-relevant product state `theta` with common prior `mu_0`.

Consumers have private taste `z ~ F`. Retailer chooses screening/commercial action `c` (implemented by a price or cutoff). Purchase occurs for a selected set `Z(c,theta-independent current utility)`.

Purchasers generate feedback `y` with `Pr(y|theta,z)`. Because `z` is selected by `c`, the observed feedback likelihood is

`Pr(y|theta,c) = integral Pr(y|theta,z) dF(z | z in Z(c))`.

Manufacturer observes `c` and feedback and updates rationally to `mu_1(c,y)`, then chooses adaptation `a(mu_1)`. Retailer receives continuation payoff that depends on adaptation and therefore chooses `c` anticipating the induced likelihood and posterior action.

Full strategic loop:

`c -> selected z distribution -> Pr(y|theta,c) -> mu_1 -> a -> retailer continuation payoff -> c`.

## Benchmark B1 — Fixed-likelihood benchmark

Retain the same players, pricing/screening, review count and adaptation decision, but force

`Pr(y|theta,c) = Pr(y|theta)`.

Commercial screening can still change current demand/number of observations, but not the statistical composition/likelihood of each observation.

Purpose: removes the information-specific selection arrow while preserving vertical continuation incentives.

Primary Stage-4 requirement: the headline sign/threshold result must be unavailable or materially different here. If it survives unchanged, return `NO-GO`.

## Benchmark B2 — Strategic-feedback-off benchmark

Retain endogenous selected feedback and rational Bayesian updating, but remove manufacturer adaptation value from retailer continuation payoff; equivalently set the retailer's continuation share from correct adaptation to zero while keeping current commercial profit.

Purpose: keeps the information technology but removes the feedback `posterior/adaptation -> retailer initial screening`.

Primary requirement: the proposed strategic screening distortion must disappear. If not, it is merely the Acemoglu-type selection effect rather than a new vertical equilibrium interaction.

## Benchmark B3 — Integrated benchmark

An integrated decision maker chooses the screening action and adaptation to maximize joint channel value while correctly accounting for the selection-dependent likelihood.

Purpose: welfare benchmark. It identifies whether decentralized retailer screening is too selective or too inclusive because the retailer appropriates only part of the value of upstream learning/adaptation.

Do not assume the sign ex ante.

## Generic non-information benchmark

Replace feedback and posterior updating with deterministic task/productivity output while preserving the same current demand and continuation transfer structure.

Purpose: direct Stage-6H generic-replacement guardrail.

A Stage-4 main theorem that remains in this benchmark is not information-specific and must be killed.

## Other candidates

A mechanism-off: set failure likelihood independent of the latent state. The intended loop disappears, but established strategic-experimentation priors already dominate the full model.

C mechanism-off: make receiver attention fixed. The reciprocal attention-quality loop disappears, but Chen–Suen already supplies the full loop.

D mechanism-off: make regime observed/fixed. Obsolescence disappears. A distinct vertical theorem would still require too many additional primitives to reach Stage 4.