# Stage 4-J Proposition Kill Table

| Claim | Desired status | Actual status | Analytic proof | Counterexample search | Benchmark survival | Disposition |
|---|---|---|---|---|---|---|
| B-P1 Selection-Induced Screening Reversal | Main | **PROVED** | Canonical symmetric-crossing family gives `1/2<c*<2/3`, `I'(c*)>0`, `dc*/drho>0`; fixed likelihood gives `dc_F*/drho<0` | 20k unrestricted affine audit confirms nonuniversality and positive region | Fails under fixed likelihood, type-observed, strategic-feedback-off, and additive deterministic output | **KEEP AS MAIN FOR STAGE 6 RE-KILL** |
| B-P2 Feedback-volume / decision-value divergence | Secondary | **PROVED as a corollary, not independent** | Along B-P1, higher `rho` raises `c`, lowers `1-c`, and raises `I(c)` | Unrestricted directions vary | Depends on same B-P1 mechanism | **BACKGROUND / ROBUSTNESS ONLY** |
| B-W1 Decentralized vs integrated screening | Welfare | **PROVED conditionally** | Canonical family yields exact `c_W*`; ordering condition derived | Both orderings appear numerically | Survives information only as ordinary welfare comparison; not main novelty | **SECONDARY** |
| Information-essentiality | Gate | **PROVED** | Type-observed benchmark gives `I_obs'(c)=-j(c)<=0`; fixed likelihood gives negative derivative | No contradiction found | Positive sign exists only with latent selected mixture | **PASS** |
| Generic-replacement impossibility | Gate | **PROVED for authorized strong additive analogue** | `H(c)=integral_c^1 v(z)dz`, so `H'(c)=-v(c)<=0` | Counterexamples impossible by identity | Cannot reproduce B-P1 | **PASS** |
| Global B-P1 for arbitrary affine feedback | Not authorized | **REJECTED** | No global sign theorem | 12,690 of 18,847 interior draws fail the B-P1 sign pattern | N/A | **KILL** |
| Universal private/social screening ordering | Not authorized | **REJECTED** | Ordering depends on `gamma,sigma` | Numerical audit includes both directions | N/A | **KILL** |
| B-P2 as independent headline contribution | Secondary | **REJECTED** | It is a direct corollary of B-P1 in the canonical family | N/A | No independent benchmark content | **KILL AS MAIN CLAIM** |

## Primary theorem statement entering any Stage 6

For the canonical family

`mu=1/2`, `0<t<1/2`,

`p_0(z)=1/2+t-2tz`,

`p_1(z)=1/2-t+2tz`,

and every positive `gamma=delta*rho*kappa*t^2`, the unique retailer equilibrium satisfies

`1/2<c*(gamma)<2/3`

and

`dc*/drho>0`.

In the otherwise identical fixed-likelihood benchmark preserving purchase probability and feedback volume,

`dc_F*/drho<0`

for every interior solution.

The sign reversal is impossible when purchaser type is observed and under the authorized nonnegative additive deterministic-output replacement.

## Scope warning

The theorem is not claimed for all affine feedback primitives. The exact witness and continuity argument establish a nonempty open parameter region in the unrestricted primitive space. Stage 6 must re-kill whether this equilibrium theorem is an obvious consequence of existing selection-effect, price/review, and review-driven-quality literatures.