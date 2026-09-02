# Stage 3-I — Stage 4 Contract

Preferred candidate: **H — Diagnostic Diversity under Downstream Concentration**

Canonical Stage 3-I verdict: `GO`

Routing: `GO TO STAGE 4 — MINIMAL MODEL`

## 1. Stage 4 mission

Construct and solve the smallest model that can falsify the claim that heterogeneous downstream diagnostic information creates a strategic reallocation effect unavailable in scalar sales/service free-riding.

Stage 4 is a hard-kill stage. It must not optimize for preserving H.

## 2. Players

Exactly three strategic players unless algebra proves one downstream node can be treated parametrically without losing the mechanism:

- upstream manufacturer `M`;
- downstream node `S_1`;
- downstream node `S_2`.

Consumers are not strategic in the minimal model.

## 3. Exogenous reallocation parameter

Use one exogenous scalar `eta in [0,1]` representing downstream activity/exposure reallocation between `S_1` and `S_2`.

Do not endogenize channel structure in Stage 4.

A minimal exposure mapping may be

`nu_1(eta)=1-eta`, `nu_2(eta)=eta`

or another one-for-one normalization if required for interior effort.

## 4. Product/problem state

Use a two-dimensional unknown state

`theta in R^2`,

with Gaussian prior

`theta ~ N(0, Sigma_0)`.

Prefer `Sigma_0=I_2` in the baseline unless asymmetry is essential to the falsification test.

## 5. Downstream information production

Each node chooses information effort

`e_i >= 0`

at convex cost

`C_i(e_i)=k_i e_i^2/2`.

Node `i` generates a signal

`y_i = h_i' theta + epsilon_i`.

Use precision

`tau_i = nu_i(eta) e_i`

or the simplest alternative that preserves separate effort and exposure margins while delivering a well-defined interior solution.

The vectors `h_i` are the diagnostic directions.

## 6. Upstream response

Information transmission is automatic and truthful in Stage 4. Do not add disclosure or ownership choices.

After observing `y_1,y_2`, `M` chooses product/design action

`a in R^2`

to minimize quadratic mismatch

`E[||a-theta||^2 | y]`.

Thus

`a*=E[theta|y]`.

Posterior precision is

`P = Sigma_0^{-1} + sum_i tau_i h_i h_i'`.

Expected residual mismatch is

`L(e,eta)=tr(P^{-1})`.

## 7. Private downstream incentives

Use the smallest payoff mapping that gives each node a private return from upstream product-fit improvement and lets reallocation change appropriability.

A candidate normalization is

`pi_i = b_i w_i(eta) [L_0-L(e,eta)] - k_i e_i^2/2`.

If this creates an unwanted public-good duplicate-benefit interpretation, replace it with the closest route-specific return mapping that still depends on the common posterior and remains algebraically minimal.

Any change must be documented. Do not add prices/contracts to repair the payoff.

## 8. System benchmark

Define system value using the same design-improvement object, internalizing all relevant downstream/upstream value:

`W = B(eta)[L_0-L(e,eta)] - sum_i k_i e_i^2/2 + terms independent of e`.

Keep the welfare benchmark as sparse as possible.

## 9. Mechanism-on specification

Use non-collinear diagnostic directions. Preferred benchmark:

`h_1=(1,0)'`,

`h_2=(cos phi, sin phi)'`,

with

`phi in (0, pi/2]`.

`phi` is the diagnostic-diversity parameter.

This permits a continuous redundancy test rather than comparing unrelated models.

## 10. Mechanism-off benchmark

Set

`phi=0`,

so

`h_1=h_2`.

This is the redundant/collinear signal benchmark.

The two-node effort/free-riding architecture remains, but diagnostic diversity disappears.

Also compare, where useful, the scalar-state representation to the Stage 6-R label-stripped costly-effort benchmark.

## 11. Candidate propositions to test

### P1 — Volume/diversity divergence

Determine whether there exists a nonempty admissible parameter region in which increasing downstream concentration toward one node raises total equilibrium information effort/precision

`d(tau_1+tau_2)/d eta > 0`

while worsening expected design accuracy

`d L(e*(eta),eta)/d eta > 0`.

This must be an equilibrium result, not an imposed shift in `h_i` or social value.

### P2 — Diagnostic retention value

Add a minimal fixed retention cost only after the effort game is solved and only if necessary to state the institutional retention implication.

Test whether a commercially weak node can have positive system retention value because of its distinct diagnostic direction, and whether this region collapses continuously as `phi -> 0`.

Do not use a fixed cost to manufacture the main theorem.

### P3 — Redundancy/diversity comparative static

Characterize how the welfare effect of reallocation/concentration changes with `phi` or an equivalent signal-correlation measure.

Seek a genuine interaction condition, threshold or ranking that is unavailable at `phi=0`.

## 12. Required analytic checks

Stage 4 must:

1. derive Bayesian posterior and `L` exactly;
2. derive downstream FOCs/best responses;
3. establish existence/uniqueness or explicitly delimit multiplicity;
4. verify SOCs/Hessian conditions;
5. solve or characterize equilibrium under mechanism-on and mechanism-off cases;
6. check `phi -> 0` and `phi -> pi/2` limits;
7. check `eta -> 0,1` boundaries;
8. search numerically/symbolically for counterexamples to any proposed global proposition;
9. separate numerical conjecture from proof.

## 13. Primary hard-kill tests

Return `NO-GO` if any of the following holds:

- H-P1/P2/P3 survives essentially unchanged at `phi=0`;
- a scalar generic costly-effort/free-riding model reproduces the same headline result;
- the desired result follows only because the payoff directly assigns extra value to diagnostic diversity;
- no nonempty interior parameter region supports a nontrivial interaction result;
- the minimal game is insoluble without adding unrelated mechanisms;
- Xiong–Li–Lang (2025), Myatt–Wallace (2019), Migrow–Squintani (2023), or another newly found paper already solves the same full-game interaction/result.

## 14. Prohibited Stage 4 additions

Do not add:

- dynamics;
- retention/exit as an endogenous strategic choice before the core mechanism is solved;
- ownership/access rights;
- portability;
- disclosure;
- contracts;
- bargaining;
- strategic prices/wholesale prices;
- RRC/foreclosure;
- extra upstream firms;
- heterogeneous consumer types beyond what the Gaussian state already represents.

## 15. Stage 4 output contract

Stage 4 must return one canonical verdict:

- `GO` if a nontrivial diagnostic-diversity interaction theorem survives hard kill;
- `CONDITIONAL GO` only for one precisely identified algebra/prior-art blocker;
- `NO-GO` if the information-specific result collapses.

If `GO`, the next required step is not manuscript work. The solved proposition must first undergo Stage 6 novelty re-kill against the actual equation/result and the H closest-paper set.

Stage 12 remains unauthorized.