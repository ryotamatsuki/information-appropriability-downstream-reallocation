# Stage 6-H Benchmark / Prior-Art Map

| Result | Scalar/collinear q=0 | Orthogonal q=1 | Full 0<q<1 | Prior-art status |
|---|---|---|---|---|
| Total-effort response | determined by aggregate E equation | sum of two independent scalar effort responses | implicit equilibrium | incentive-driven effort reallocation is standard |
| Posterior-loss response | `L=1+1/(1+E)`; opposite sign to E response | `L=1/(1+e1)+1/(1+e2)` | multidimensional posterior geometry | trace posterior covariance is standard A-optimality |
| H-P1 divergence | impossible | possible and proved region | continuity implies local sign transition for exact witness, not a full theorem | q=1 result reduces to generic separable concave task allocation |
| Diagnostic sign switch | absent | endpoint positive for witness | at least one crossing exists by continuity | secondary mathematical result only |
| Private/system wedge | standard underinvestment/appropriation wedge | private task weights differ from system weights | implicit | not retained as novelty claim |

## Benchmark interpretation

### q=0

This benchmark has only one payoff-relevant aggregate information dimension. The impossibility `E_eta>0 => L_eta<0` is correct but economically elementary: if useful output is a monotone function of one aggregate input, more of the aggregate cannot worsen that output.

### q=1

This is the benchmark where H-P1 is actually proved. It eliminates cross-source interaction:

`G(e1,e2)=g(e1)+g(e2)`, `g(e)=e/(1+e)`.

Hence H-P1 is not a full-model-only result. It arises in a nested benchmark where each source is an independent concave task.

### 0<q<1

The full model contains a genuine cross-information term and `G_12` need not vanish. Stage 4 did not prove a general H-P1 theorem in this interior region. Stage 6 is prohibited from creating a new theorem. Therefore the full-model strategic interaction cannot rescue the frozen contribution.

## Prior-art interpretation

- Optimal design: supplies the standard posterior-trace / directional-allocation geometry.
- Multitask incentives: supplies the standard incentive-induced effort-level versus effort-allocation distortion.
- Habermacher/Moresi/Myatt-Wallace: show that information specialization, concentration, acquisition quantity, and decision/allocation quality are already established economic margins.

The novelty gate therefore fails not because q=0 or q=1 is literally copied from one paper, but because the only proved headline result is unavailable as a new full-model interaction theorem.