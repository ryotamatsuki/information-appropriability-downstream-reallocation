# Stage 4-H — Welfare and Private/System Benchmarks

Use

`W = B G - k_1 e_1^2/2 - k_2 e_2^2/2`,

with baseline `B=b`.

Because `G` is concave and effort costs are strictly convex, the system problem has a unique optimum.

## Reallocation and the system optimum

Under the Stage 4 Option-B normalization, `eta` affects private appropriability but not the information technology or system value `B`. Thus the system-optimal signal portfolio is independent of `eta`.

This is deliberate: the exercise isolates the private appropriability distortion caused by downstream reallocation.

## Orthogonal benchmark q=1

System FOCs are

`k_i e_i^S = B/(1+e_i^S)^2`,

or

`e_i^S(1+e_i^S)^2=B/k_i`.

Private equilibrium satisfies

`e_1^P(1+e_1^P)^2=b(1-eta)/k_1`,

`e_2^P(1+e_2^P)^2=b eta/k_2`.

With `B=b` and `eta in (0,1)`, monotonicity of `e(1+e)^2` implies

`e_i^P < e_i^S` for both nodes.

Hence reallocation changes the private diagnostic composition even though the system's preferred diagnostic portfolio does not move.

## Redundant benchmark q=0

System design gain depends only on `E=e_1+e_2`. Conditional on total effort, efficient cost allocation gives

`e_1/e_2 = k_2/k_1`.

The effective quadratic cost coefficient is

`K = k_1 k_2/(k_1+k_2)`.

System total effort satisfies

`E^S(1+E^S)^2 = B(1/k_1+1/k_2)`.

Private total effort satisfies

`E^P(1+E^P)^2 = b[(1-eta)/k_1+eta/k_2]`.

For `B=b` and interior `eta`, the RHS of the system equation is strictly larger, so `E^S>E^P`.

## Welfare along the private equilibrium path

The relevant decentralized welfare effect is

`dW(e^P(eta,q))/deta = grad_e W · de^P/deta`.

This derivative need not share the sign of `-L_eta` because changing private efforts also changes effort costs. The numerical audit finds robust examples where this welfare derivative has different signs at `q=0` and `q=1`, but Stage 4 does not obtain a general analytic threshold in `q`.

Therefore the original H-P3 welfare-threshold conjecture remains **CONJECTURE / NOT PROVED** and is not used to justify GO.

## Welfare conclusion

The proved welfare-relevant organizational wedge is narrower but clean: downstream reallocation distorts the decentralized diagnostic portfolio away from an `eta`-invariant system optimum. In the orthogonal benchmark, both privately chosen efforts are strictly below their system levels, and the composition response to `eta` can generate H-P1.
