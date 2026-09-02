# Stage 4-H — Minimal Model Hard Kill Report

Canonical Stage 4 template: `templates/STAGE_04_MINIMAL_MODEL.md` @ `2fbba0381d3dd9be9ec203deb2c23c4008c3c040`.

Workflow: `research-paper-workflow` v1.1 @ `488e5ab06c207909296a7564eaf9066f7f94319c`.

Starting canonical main / Stage 3-I merge SHA: `864080c804eebf458ce733f9cb34b4396f9a939f`.

## Executive verdict

`GO`

Routing: `GO -> Stage 6 Novelty Re-Kill`.

The minimal diagnostic-diversity mechanism survives Stage 4 without feature accumulation. The result that survives is narrower than the Stage 3-I conjecture set: H-P1 survives; H-P2 is killed; H-P3 welfare threshold is not proved.

## Exact model

`theta ~ N(0,I_2)`.

`h_1=(1,0)'`, `h_2=(cos(phi),sin(phi))'`, `q=sin(phi)^2`.

`y_i=h_i' theta+epsilon_i` with precision `tau_i=e_i`.

Private payoffs:

`pi_1=b(1-eta)G-k_1e_1^2/2`,

`pi_2=b eta G-k_2e_2^2/2`.

Manufacturer chooses posterior mean design action. `G=2-tr(P^{-1})`.

System benchmark:

`W=B G-k_1e_1^2/2-k_2e_2^2/2`, baseline `B=b`.

## Bayesian solution

`D=1+e_1+e_2+q e_1e_2`.

`L=tr(P^{-1})=(2+e_1+e_2)/D`.

`G_1=(q e_2^2+2q e_2+1)/D^2`,

`G_2=(q e_1^2+2q e_1+1)/D^2`.

`G` is concave; own marginal values decline. Cross marginal-value interaction is

`G_12=2(1-q)(q e_1e_2-1)/D^3`.

## Equilibrium

The private game is a weighted strictly-concave potential game with

`Psi=G-k_1e_1^2/[2b(1-eta)]-k_2e_2^2/[2b eta]`.

Hence for interior `eta`, a unique positive Nash equilibrium exists. Boundary `eta` values give the corresponding one-node KKT solutions.

## Mechanism-off benchmark

At `q=0`, only total effort `E=e_1+e_2` matters:

`E(1+E)^2=b[(1-eta)/k_1+eta/k_2]`.

`L=1+1/(1+E)`.

Therefore

`L_eta=-E_eta/(1+E)^2`.

It is impossible for total equilibrium precision and design loss to rise together.

## Orthogonal benchmark and main theorem

At `q=1`:

`e_1(1+e_1)^2=b(1-eta)/k_1`,

`e_2(1+e_2)^2=b eta/k_2`.

Let

`a_1=(b/k_1)/[(1+e_1)(1+3e_1)]`,

`a_2=(b/k_2)/[(1+e_2)(1+3e_2)]`.

Then H-P1 holds iff

`1<a_2/a_1<[(1+e_2)/(1+e_1)]^2`.

Exact witness:

`b=1`, `eta=3/5`, `e_1=1/6`, `e_2=1/3`, `k_1=432/245`, `k_2=81/80`.

At this point

`d(e_1+e_2)/deta=5/108>0`,

`dL/deta=5/168>0`.

Strict inequalities and continuity imply an open positive-measure parameter region.

Under the same primitives at `q=0`, `E_eta>0` but `L_eta<0`. Thus the H-P1 divergence is unavailable when diagnostic diversity is switched off.

## Candidate proposition status

- H-P1 Volume/diversity divergence: `PROVED`.
- H-P2 Retention value collapsing under redundancy: `REJECTED`.
- H-P3 General welfare redundancy threshold: `CONJECTURE / NOT PROVED`.
- Supporting diagnostic-loss sign-switch existence in `q`: `PROVED` by endpoint signs and continuity for the exact witness.

## Numerical counterexample audit

Seed `20260903`; 10,000 raw draws; 10,000 feasible solves; zero solver failures.

H-P1 local sign pattern occurred in 585 draws. 9,415 draws are counterexamples to a global H-P1 statement, confirming the theorem must be regional.

For the exact witness, a numerical diagnostic gives one `L_eta=0` crossing at `q ~= 0.6595906712`, `phi ~= 54.3067 degrees`.

In a 2,000-draw endpoint subset, 155 cases showed a sign change in decentralized welfare response between `q=0` and `q=1`; this is not promoted to proof.

## Welfare

The system problem is strictly concave and unique. Under Option B, the system-optimal diagnostic portfolio is independent of `eta`, while the decentralized portfolio moves with route-specific appropriability.

At `q=1` and `B=b`, each private effort is strictly below its system counterpart for interior `eta`.

At `q=0`, system total effort also strictly exceeds private total effort under `B=b`.

No general welfare-threshold theorem in `phi` is claimed at Stage 4.

## Information-essentiality verdict

`PASS`.

The H-P1 theorem depends on the distinction between scalar total precision and posterior loss across multiple diagnostic dimensions. At `q=0`, posterior loss is monotone in total effort and the divergence is impossible. A generic scalar costly-service-effort model therefore cannot reproduce the proved H-P1 theorem without adding the multidimensional information structure.

## Prior-art escalation

Targeted Stage 4 searches re-opened Xiong–Li–Lang (2025), Myatt–Wallace (2019), Migrow–Squintani (2023), Board–Meyer-ter-Vehn (2024), and the Xu/Pu dual-channel free-riding family. Strong component overlap remains, but no inspected source was found to contain the derived H-P1 vertical reallocation / private information effort / posterior-diagnostic-diversity result as an exact theorem or immediate scalar corollary.

Formal novelty certification is deferred to Stage 6, as required by the workflow.

## Artifact audit

All Stage 4 additions are under `stage4h/**`. No Stage 8 freeze, stale manuscript, Stage 11, Stage 6-R, or workflow file is modified.

## Canonical Stage 4 verdict

`GO`

Exact next-stage contract:

Freeze the Stage 4-H model and the proved H-P1 result exactly as derived. Stage 6 must convert H-P1's exact inequalities, exact witness, mechanism-off impossibility result, and diagnostic-loss sign-switch into proposition-level search queries; re-open the closest correlated-signal, information-acquisition, network-learning, vertical-information, and dual-channel effort papers at model/proposition level; and return `GO / CONDITIONAL GO / NO-GO` without changing the Stage 4 model.
