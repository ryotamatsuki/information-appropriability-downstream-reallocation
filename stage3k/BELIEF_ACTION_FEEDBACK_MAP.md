# Belief-Action Feedback Map

This file writes each candidate as a minimal feedback system before any algebra.

## K1

`e_i -> y_i -> mu_i -> x_i(mu) -> future rent_i -> e_i`

Reduced-form test: posterior allocation can be replaced by a noisy performance score and prize schedule. The belief state is not indispensable to the strategic topology.

## K2

`s_i -> report_i -> mu -> allocation -> future reputation/rent -> report_i`

The feedback is genuinely informational, but it is a standard repeated reputational communication topology. Novelty risk is binding before Stage 4.

## K3

`mu_t -> a_t^M -> e_{t+1}^S -> f(y_{t+1}|theta,a,e) -> mu_{t+1}`

Candidate-specific issue: `a` changes the downstream information technology. But replacing `mu` by a deterministic state and `f` by a controlled state transition preserves the same strategic chain.

## K4

`mu_t -> a_t^M -> c_t^R -> participation/data_t -> mu_{t+1}`

This is a strategic version of the data-feedback loop. A deterministic analogue `quality_t -> price/participation -> data/productivity_{t+1} -> quality_{t+1}` preserves the topology.

## K5

`mu_t -> delegation_t -> e_t^S -> signal -> mu_{t+1} -> delegation_{t+1}`

Belief and players can be essential, but Aghion–Tirole and later delegation-learning papers already occupy the mechanism family.

## K6

`mu_t -> organization_t -> e_t^R -> signal -> mu_{t+1} -> organization_{t+1}`

Strongest surviving topology initially. Yet a deterministic analogue `capability_t -> organization_t -> investment_t -> capability_{t+1}` has the same feedback network. To make belief essential would require an additional inference/commitment interaction not present in the minimal candidate.

## K7

`e_1,e_2 -> signals -> mu -> future allocation/rents -> e_1,e_2`

This maps naturally to an innovation contest/R&D race with project-quality signals and future prizes.

## K8

`provider action -> outcome -> reputation mu(r_i) -> client reliance/effort -> test precision -> future outcome/reputation`

This topology is directly threatened by Lukyanov–Vlasova (2026), where reputation changes client implementation effort and hence the informativeness/exposure of future tests.

## Topology success requirement

A candidate was required to have both:

1. a belief-dependent best response; and
2. an action-dependent future experiment.

That requirement alone was insufficient. The full topology also had to fail under deterministic-state replacement and player removal. None of K1–K8 passed all tests.