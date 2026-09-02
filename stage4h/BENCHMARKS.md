# Stage 4-H — Benchmarks and Hard-Kill Comparisons

## 1. Mechanism OFF: phi=0 / q=0

Signals are collinear. The posterior depends only on `E=e_1+e_2`:

`L=1+1/(1+E)`.

The unique private equilibrium satisfies

`E(1+E)^2=b[(1-eta)/k_1+eta/k_2]`.

Thus

`sign(L_eta)=-sign(E_eta)`.

Consequently the H-P1 pattern — more aggregate precision but worse design accuracy — is impossible in the scalar/redundant benchmark.

This retains two downstream effort choices and reallocation of appropriability. What disappears is only diagnostic direction.

## 2. Maximum diversity: phi=pi/2 / q=1

The state dimensions separate:

`L=1/(1+e_1)+1/(1+e_2)`.

Private effort equations are independent cubic equations. Cost/productivity asymmetry can make reallocation toward the lower-cost node raise total precision while starving the other diagnostic dimension enough to increase total posterior loss. The exact H-P1 witness is recorded in `EQUILIBRIUM_DERIVATION.md`.

## 3. Boundary reallocation

At `eta=0`, `S_2` has zero private appropriability and chooses `e_2=0`; `S_1` solves a one-dimensional strictly concave problem.

At `eta=1`, `S_1` chooses `e_1=0`; `S_2` solves the analogous one-dimensional problem.

No interior-FOC claim is extended to these boundaries without the corresponding KKT interpretation.

## 4. Anti-Xu / generic service-effort benchmark

A scalar costly-effort/free-riding model can reproduce reallocation-driven changes in total effort, but it cannot reproduce H-P1 under the mechanism-off restriction because scalar posterior loss is a strictly decreasing function of total effort.

To reproduce the H-P1 divergence, the benchmark must add at least a multidimensional state and non-collinear diagnostic directions. That addition is exactly the H information-specific formal object.

## 5. H-P2 retention hard kill

The original Stage 3-I retention conjecture required a diagnostic-retention region to collapse as `phi -> 0`. This is false in the minimal model.

At `q=0`, a second collinear information producer can still add independent scalar precision. Moreover, for fixed total effort `E`, splitting production across two convex-cost nodes can reduce the cost of generating `E`.

For example, minimizing

`k_1 e_1^2/2 + k_2 e_2^2/2`

subject to `e_1+e_2=E` yields effective cost

`[k_1 k_2/(k_1+k_2)] E^2/2`,

which is strictly below the one-node cost `k_2 E^2/2` when both costs are finite.

Therefore retaining a diagnostically redundant node can have positive system value even at `phi=0`. A fixed retention cost could generate a positive retention region without diagnostic diversity.

Verdict: **H-P2 REJECTED**. It is not used to support Stage 4 GO.

## 6. Orthogonal versus redundant source interpretation

`q=0`: sources differ only in who produces scalar precision.

`q=1`: sources span distinct state dimensions.

H-P1 changes sign across these benchmarks under the same economic primitives, so the surviving result is not produced by cost asymmetry alone.
