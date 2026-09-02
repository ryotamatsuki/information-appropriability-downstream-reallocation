# Stage 6-R — Whole-Game Absorption Matrix

Canonical base: `48894b15f3b235610f058641ed7fd89f9bbfd6bc`

Stage 8 freeze: `ef588465430f618b56cf84445681752702c161e1`

Date audited: 2026-09-03

## Bottom line

The Stage-11 Pu-only argument was too strong: Pu, Gong & Han (2017) endogenize both channel prices and explicitly report that centralized as well as decentralized sales effort falls with free riding in their deterministic baseline. The required `p_d > p_r` reversal was not verified as an admissible region of their published baseline. Pu is therefore **not** treated here as an exact/immediate-corollary kill by itself.

A stronger prior is Xu, Tang, Lin & Lu (2022, IJPE 249, 108506, DOI `10.1016/j.ijpe.2022.108506`). Their demand system assigns the retailer's effort benefit as `(alpha-beta)e` to the offline channel and `beta e` to the online channel, with `0 <= beta <= alpha`. Their author-uploaded full text reports that increasing `beta` lowers decentralized sales effort, while under centralized decision the effort rises with `beta` when consumers prefer the online channel and falls when they prefer the offline channel. Hence the headline qualitative divergence already occurs in a richer solved dual-channel free-riding model.

The frozen model does not introduce an information-specific strategic arrow that could distinguish its P3 theorem from this existing effort-reallocation architecture. `M` and `R` are not strategic choosers in P3, and `x=g(e)` is a monotone intermediate input without persistence, adoption, ownership, disclosure, or an upstream response choice.

## Matrix

| Dimension | Current frozen model | Pu et al. 2017 | Xu et al. 2022 | Equivalent? | Material difference? |
|---|---|---|---|---|---|
| Players | nominal `M,S,R`; only `S` chooses in P3 | manufacturer + offline retailer; both pricing roles, retailer effort | supplier + offline retailer; pricing/financing/returns plus retailer effort | Partly | Prior models are strategically richer; current P3 is not richer |
| Strategic choosers | one effort chooser in core theorem | prices + effort endogenous | prices + effort and financial terms endogenous | No | Difference weakens, rather than protects, current novelty |
| Effort producer | `S` | offline retailer | offline retailer | Yes | No |
| Effort cost | convex `C(e)` | quadratic | quadratic | Yes up to functional form | No |
| Reallocation/free-riding variable | `eta` shifts route weights | `tau` shifts effort-generated demand from offline to online | `beta` shifts effort-generated demand from offline `(alpha-beta)e` to online `beta e` | Yes at effort-benefit allocation level | No |
| Private appropriation | `S` internalizes own-route return only | retailer bears effort and loses sales to direct route | retailer bears effort and free-riding diverts effort-created demand online | Yes | No |
| Cross-route spillover | same effort-generated product improvement benefits both routes | offline effort benefits manufacturer online channel | offline effort benefits online channel | Yes | Information label differs, strategic spillover does not |
| Private objective | own-route marginal return minus effort cost | retailer payoff with own sales margin minus effort cost | retailer payoff with own sales/financing terms minus effort cost | Same economic wedge | Extra pricing/financing terms in priors |
| Coordinated objective | sum of both route returns minus effort cost | integrated two-channel profit | integrated two-channel profit | Yes | Prior models richer |
| Strategic feedback | `eta -> weights -> e -> route quantities`; no upstream response | free riding -> demands/prices/effort -> profits | free riding + channel preference -> demands/prices/effort -> profits | Current is simpler | No unique information feedback in current P3 |
| Headline private sign | `deP/deta < 0` | effort falls with free riding | decentralized effort falls with `beta` | Yes | Standard free-riding effect |
| Headline coordinated sign | positive iff weighted expanding-route return dominates | published baseline: effort falls with free riding | centralized effort rises with `beta` under online preference | Xu reproduces sign possibility | Pu alone does not |
| Joint sign reversal | `private down / coordinated up` | not in reported baseline | explicitly reported in numerical sensitivity for online-preference case | Yes qualitatively | Xu result is richer/parametric, but same economic sign pattern |
| Condition for positive coordinated sign | general condition (G); one-for-one gives `A_R>A_S` | not same condition; endogenous prices | online preference can flip centralized response | Same comparative-static logic, not same formula | Current condition is a generic mixed-partial sign characterization |
| Welfare | private < coordinated < social | decentralized vs centralized efficiency | decentralized vs centralized; system profit sensitivity | Component overlap | Current adds consumer-surplus benchmark, not a new strategic mechanism |
| Contractibility | effort assumed noncontractible | coordination contract studied | revenue-sharing/financing contract studied | Different | Noncontractibility is not active enough to create a new feedback in current P3 |
| Persistence/dynamics | none | none in baseline | none in core sensitivity | Yes | No information-specific state |
| Information-specific state | `x=g(e)` only | service/sales effort effect | service/sales effort effect | Reducible | `x` can be substituted out of static P3; no material strategic state |

## Strategic-feedback comparison

Frozen P3:

`eta -> {omega_S, omega_R} -> e -> x=g(e) -> {q_S,q_R}`.

There is no endogenous response by `M` or `R` to `x`.

Xu et al. 2022:

`beta -> {(alpha-beta)e, beta e} -> {offline demand, online demand} <-> prices -> e -> profits`.

The prior is strategically richer, yet already generates the same private-down / centralized-up sign pattern for an online-preference parameterization.

## Reverse-kill test

Strongest possible defense: information is a nonrival upstream product-improvement input rather than contemporaneous sales service.

Result: **FAIL** for the frozen P3 game. The frozen model contains no persistence, stock, adoption decision, information ownership, disclosure decision, upstream strategic response, or intertemporal reuse. The transformation `x=g(e)` can be absorbed into route benefit functions in the static theorem. Thus the institutional interpretation does not create a new equilibrium feedback.

## Whole-game verdict

- Pu et al. 2017: `STRUCTURALLY VERY CLOSE`; Stage-11 immediate-corollary claim not independently sustained after admissibility audit.
- Xu et al. 2022: `STRUCTURALLY VERY CLOSE` at full-game level and direct prior art for the **joint qualitative sign reversal** in a richer free-riding model.
- Frozen P3: no independently novel strategic mechanism survives label stripping. Its general condition (G) is a local mixed-partial sign condition rather than a new interaction theorem.

Canonical implication: **NO-GO for the current contribution set**, even though the exact general formula (G) is not verbatim prior art.