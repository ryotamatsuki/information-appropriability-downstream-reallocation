# Stage 4-J Numerical Audit Report

Numerical work is diagnostic only and follows the analytical proof.

## Protocol

- Seed: `20260903`
- Raw draws: `20,000`
- Prior: `mu ~ U[0.1,0.9]`
- Four primitive endpoint feedback probabilities independently sampled from `U[0.05,0.95]`; each draw defines affine `p_0(z),p_1(z)`.
- Retailer continuation coefficient (`delta*rho*kappa` after numerical normalization `kappa=1`) sampled from `U[0,30]`.
- Social adaptation coefficient sampled independently from `U[0,30]` for diagnostic welfare ordering.
- Retailer and welfare objectives globally compared against both endpoints after bounded scalar optimization.
- Finite-difference derivatives are used only as diagnostics; theorem claims rely on exact algebra.

## Results

- Feasible draws: `20,000`
- Solver failures: `0`
- Interior retailer optima: `18,847`
- Draws satisfying the B-P1 local sign pattern (`c*>1/2`, `I'(c*)>0`, SOC): `6,157`
- Counterexamples to any unrestricted/global B-P1 claim among interior draws: `12,690`
- Minimum sampled SOC margin `-Pi_R''` among interior draws: approximately `0.2172345893`

The high counterexample count is important: Stage 4-J does **not** claim that arbitrary affine feedback technologies generate the screening reversal. The theorem is a parameter-region result, proved analytically using the canonical symmetric-crossing family and extended to an open neighborhood by continuity.

## Welfare diagnostics

With independently sampled private and social continuation coefficients:

- `c_R > c_W`: `18,842` draws
- `c_R < c_W`: `5` draws
- approximately equal / common boundary: `1,153` draws

This confirms that no unrestricted welfare ordering should be claimed. The analytic welfare result is therefore stated as a conditional ordering characterization.

## Exact witness implementation cross-check

For

- `t=3/10`
- `kappa=20`
- `rho=25/27`
- `delta=1`
- `c*=3/5`

numerical evaluation reproduces

`I'(c*)=27/125=0.216`,

and

`Pi_R''(c*)=-14/3`.

## Generic-replacement audit

No numerical search is needed to establish the generic additive-output result because

`H(c)=integral_c^1 v(z)dz`

implies exactly

`H'(c)=-v(c)<=0`

for every nonnegative `v`. Therefore generic additive-output counterexamples to the analytical impossibility result are zero by identity.

## Interpretation

The numerical audit supports three disciplined conclusions:

1. B-P1 exists on a substantial set of feasible affine signal technologies but is not universal.
2. The exact theorem witness is not a numerical artifact.
3. Global welfare ordering is false and is not promoted to a theorem.