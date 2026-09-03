# Stage 4-J — Endogenous Customer-Selection Minimal Model Hard Kill

## Executive verdict

**GO**

Route: **GO TO STAGE 6 — NOVELTY RE-KILL**.

Candidate B survives the Stage 4 mathematical and benchmark hard kills. The survival claim is narrow: endogenous commercial screening can change a latent customer mixture and therefore the Bayesian experiment faced by a separate upstream adapter, producing an equilibrium screening comparative-static sign that reverses relative to a fixed-likelihood volume benchmark and cannot be reproduced by the authorized nonnegative additive deterministic-output analogue.

This is not a novelty certification. Targeted prior-art escalation identifies a high-risk synthesis threat from Chen–Du–Lei, Yan et al. (2026), Acemoglu et al. (2022), and vertical retailer-information/manufacturer-quality models.

## Exact model

- State: `theta in {0,1}`, prior `mu`.
- Consumer type: `z~U[0,1]`.
- Retailer screening: `c in [0,1]`; purchase iff `z>=c`.
- Feedback: `Pr(y=1|theta,z)=alpha_theta+beta_theta z`.
- Manufacturer observes `c`, purchase, and feedback if purchase, but not `z`; manufacturer knows the selection mechanism.
- Manufacturer adaptation under quadratic loss: `a*=posterior mean`.
- Retailer: `Pi_R(c)=c(1-c)+delta*rho I(c)`.

## General selected-sample Bayesian experiment

`q_theta(c)=ell_theta(1;c)=alpha_theta+beta_theta(1+c)/2`.

Let

`m(c)=mu q_1(c)+(1-mu)q_0(c)`.

Posterior after positive feedback:

`mu_1(c)=mu q_1(c)/m(c)`.

Posterior after negative feedback:

`mu_0(c)=mu[1-q_1(c)]/[1-m(c)]`.

Prior Bayes risk:

`R_0=kappa mu(1-mu)`.

Conditional feedback information value:

`J(c)=kappa mu^2(1-mu)^2 [q_1(c)-q_0(c)]^2/[m(c)(1-m(c))]`.

Ex-ante information value:

`I(c)=(1-c)J(c)`.

Mechanism decomposition:

`I'(c)=-J(c)+(1-c)J'(c)`.

The first term is lost feedback volume. The second is the selected-composition change in experiment value.

## Canonical theorem family

Set

`mu=1/2`, `0<t<1/2`,

`p_0(z)=1/2+t-2tz`,

`p_1(z)=1/2-t+2tz`.

Then

`q_0(c)=1/2-tc`,

`q_1(c)=1/2+tc`,

`J(c)=kappa t^2 c^2`,

`I(c)=kappa t^2 c^2(1-c)`,

`I'(c)=kappa t^2 c(2-3c)`.

Define

`gamma=delta rho kappa t^2`.

Retailer FOC:

`F(c;gamma)=1+2(gamma-1)c-3gamma c^2=0`.

For every `gamma>0`, there is exactly one positive root:

`c*(gamma)=[gamma-1+sqrt(gamma^2+gamma+1)]/(3gamma)`.

Moreover

`F(1/2)=gamma/4>0`,

`F(2/3)=-1/3<0`,

so

`1/2<c*(gamma)<2/3`.

Therefore

`I'(c*)>0`

and, under the regular SOC,

`dc*/drho>0`.

## B-P1 — Selection-Induced Screening Reversal

**PROVED.**

In the full endogenous-likelihood model, a larger retailer stake in correct upstream adaptation raises equilibrium screening in the canonical family.

In the fixed-likelihood benchmark, preserve purchase probability and current profit but set `J(c)=bar J>0`. Then

`I_F(c)=(1-c)bar J`,

`c_F*(rho)=[1-delta rho bar J]/2`

for an interior solution, and

`dc_F*/drho=-delta bar J/2<0`.

Hence the comparative-static sign reverses.

## Exact witness

Choose

`mu=1/2`, `t=3/10`, `kappa=20`, `delta=1`, `rho=25/27`.

Primitive feedback probabilities are

`p_0(z)=4/5-(3/5)z`,

`p_1(z)=1/5+(3/5)z`,

and remain in `[1/5,4/5]`.

Then

`gamma=5/3`,

`c*=3/5`,

`I'(c*)=27/125>0`,

`Pi_R''(c*)=-14/3<0`.

All feasibility and sign restrictions are strict. Local uniqueness plus continuity yields a nonempty open parameter neighborhood in the unrestricted affine model.

## Benchmark kills

### Fixed likelihood

Feedback volume remains `1-c`, but conditional experiment value is fixed. Result: `dc_F*/drho<0`. B-P1 does not survive.

### Type observed

When `M` observes `z`, ex-ante information value is additive:

`I_obs(c)=integral_c^1 j(z)dz`, `j(z)>=0`.

Therefore

`I_obs'(c)=-j(c)<=0`.

The positive composition effect disappears.

### Strategic feedback off

At `rho=0`, retailer screening is uniquely `c=1/2`. Bayesian learning remains available to `M`, but no vertical screening response remains.

### Information deleted

If `ell_1=ell_0`, then `J=I=0` and retailer chooses `c=1/2`.

### Strong generic deterministic output

For any nonnegative type-dependent deterministic continuation productivity `v(z)`,

`H(c)=integral_c^1 v(z)dz`,

so

`H'(c)=-v(c)<=0`.

The authorized strong additive output replacement cannot reproduce `dc*/drho>0`.

**Generic-replacement verdict: PASS.**

## Likelihood ratio and Blackwell structure

In the canonical family,

`Lambda_1(c)=(1/2+tc)/(1/2-tc)` increases in `c`, while the negative-feedback likelihood ratio decreases reciprocally. The purchase-contingent binary experiment becomes more informative as screening increases and is Blackwell ordered. The theorem is therefore a strategic quantity-versus-experiment-quality interaction rather than a nonmonotone experiment-order effect.

This clarity is also the strongest hostile-referee risk: a Stage 6 referee may argue the result is an immediate consequence of standard experiment ordering plus endogenous screening.

## B-P2

As `rho` rises in the B-P1 region, `c*` rises, feedback volume `1-c*` falls, and total information value `I(c*)` rises. This is **PROVED as a direct corollary** but is **BACKGROUND / ROBUSTNESS ONLY**, not an independent contribution.

Any global or opposite-direction B-P2 claim is rejected.

## Welfare — B-W1

Integrated welfare is

`W(c)=(1-c^2)/2 + delta B I(c)`.

In the canonical family, define `sigma=delta B kappa t^2`.

If `sigma<=1/2`, `c_W*=0`.

If `sigma>1/2`,

`c_W*=(2sigma-1)/(3sigma)`.

The ordering between retailer and integrated screening is parameter dependent. For the exact B-P1 witness with `B=1`,

`c_R*=3/5`,

`c_W*=13/27`,

so `c_R*>c_W*`.

B-W1 is **PROVED conditionally** and kept secondary. A universal welfare ordering is rejected.

## Numerical audit

Seed: `20260903`.

- Raw draws: `20,000`
- Feasible: `20,000`
- Solver failures: `0`
- Interior retailer optima: `18,847`
- B-P1 local sign-pattern draws: `6,157`
- Counterexamples to an unrestricted/global B-P1 claim: `12,690`
- Minimum sampled SOC margin: approximately `0.2172345893`

The theorem is therefore correctly stated as a parameter-region result rather than global across arbitrary affine feedback primitives.

## Targeted prior-art escalation

Strongest threats:

1. **Chen–Du–Lei (Marketing Science 2024/2025)** — price can mitigate review-selection bias and make reviews more informative. `STRUCTURALLY VERY CLOSE`.
2. **Yan–Bian–Perera–Guan (POM 2026)** — review-driven learning, dynamic pricing, and post-launch quality refinement; introductory price can move in either direction. `STRUCTURALLY VERY CLOSE`.
3. **Acemoglu et al. (Econometrica 2022)** — canonical selected-review learning mechanism. `COMPONENT OVERLAP / STRUCTURALLY VERY CLOSE` on the statistical object.
4. **Hu et al. (IJPE 2021)** — retailer information acquisition and manufacturer quality incentives. Strongest vertical-IO component threat.

No single inspected prior was verified to reproduce the full Stage 4-J game plus the B-P1 continuation-stake sign reversal against the fixed-likelihood volume benchmark.

Immediate-corollary verdict at Stage 4: **NOT KILLED, BUT HIGH NOVELTY RISK**.

## Hard-kill answers

1. Well-defined equilibrium? **YES**.
2. Unique relevant equilibrium? **YES in theorem family**.
3. B-P1 true? **YES**.
4. Open parameter set? **YES**.
5. Extreme signal parameters required? **NO**; witness uses `[1/5,4/5]`.
6. Uses endogenous likelihood composition? **YES**.
7. Disappears under fixed likelihood? **YES**.
8. Fixed benchmark preserves feedback volume? **YES**.
9. Disappears under strong deterministic replacement? **YES**.
10. Disappears when purchaser type observed? **YES**.
11. Vertical comparative static disappears at `rho=0`? **YES**.
12. More than 'better customers give better signals'? **YES mathematically; Stage 6 must test novelty**.
13. More than generic quantity-quality tradeoff? **PASS against authorized additive analogue, but Stage 6 risk remains**.
14. Immediate corollary of Acemoglu et al.? **Not verified**.
15. Immediate corollary of vertical information acquisition? **Not verified**.
16. Single prior reproduces full loop? **Not verified**.
17. B-P2 independently valuable? **NO**.
18. B-W1 more than underappropriation? **Only conditionally; secondary**.
19. Probability restrictions nonpathological? **YES for exact witness/open neighborhood**.
20. Enough theory for Stage 6? **YES, narrowly B-P1**.

## Artefact audit requirement

Only `stage4j/**` may differ from the starting base. Historical theory and manuscript remain frozen.

## Canonical verdict

**GO**

## Routing

**GO TO STAGE 6 — NOVELTY RE-KILL**

Stage 6 receives B-P1 unchanged, the exact witness, and all benchmark maps. Stage 6 must specifically test whether B-P1 is already known or an obvious synthesis of endogenous review selection, price-induced review informativeness, review-driven quality refinement, and vertical information incentives.
