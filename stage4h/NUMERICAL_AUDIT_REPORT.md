# Stage 4-H — Numerical Audit Report

Purpose: counterexample search / positive-measure region mapping / analytic consistency only.

Seed: `20260903`.

Parameter ranges:

- `eta ~ Uniform(0.05,0.95)`;
- `phi ~ Uniform(0,pi/2)`;
- `q=sin(phi)^2`;
- `b=B=1`;
- `k_1,k_2` independently log-uniform on `[0.5,3]`.

Raw draws: **10,000**.

Feasible solved draws: **10,000**.

Solver failures: **0**.

Tolerance for FOC residual: `1e-8`; sign classification buffer: `1e-7`.

Minimum sampled FOC-Jacobian determinant: **0.4924026293**.

## H-P1 region mapping

Draws satisfying

`d(e_1+e_2)/deta > 0`

and

`dL/deta > 0`:

**585 / 10,000**.

All 585 sampled H-P1 cases occurred with `eta>0.5`, consistent with interpreting the local comparative static as further concentration toward node 2.

Counterexamples to any global H-P1 claim: **9,415 / 10,000**.

Therefore H-P1 is explicitly a parameter-region proposition, not a global theorem.

The exact analytical witness, rather than this frequency, proves nonemptiness. The random audit only shows the region is not numerically knife-edge under the stated sampling design.

## Exact-witness redundancy crossing diagnostic

For

`b=1`, `eta=3/5`, `k_1=432/245`, `k_2=81/80`,

the numerical root of `dL/deta=0` along the unique equilibrium is

`q ~= 0.6595906712`,

or

`phi ~= 54.30671159 degrees`.

Analytical work proves at least one crossing exists by continuity from opposite endpoint signs. The numerical value is diagnostic only and uniqueness of the crossing is not claimed.

## Welfare diagnostic

For the first 2,000 random parameter draws, the sign of

`dW(e^P(eta,q))/deta`

at `q=0` versus `q=1` differed in **155** cases.

This motivates but does not prove a welfare redundancy threshold. H-P3 remains `CONJECTURE / NOT PROVED`.

## Boundary/consistency audit

- `q=0` mechanism-off formulas recover the scalar total-effort representation.
- `q=1` formulas recover two independent one-dimensional information problems.
- `eta -> 0` and `eta -> 1` correctly send the zero-appropriability node's effort to zero.
- No sampled singular equilibrium Jacobian occurred.

Numerical evidence is not used as proof of H-P1, H-P2, or H-P3.
