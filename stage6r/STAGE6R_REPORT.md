# Stage 6-R — Dual-Channel Effort Free-Riding Exact Prior-Art Re-Kill

## Executive verdict

**Canonical verdict: `NO-GO`.**

**Routing/status: `CURRENT CONTRIBUTION BRANCH TERMINATED`.**

**Stage 3 pivot eligibility: YES, but only for a distinct information-specific strategic architecture.**

The frozen mathematics remain valid. The failure is novelty/mechanism-level.

Stage 6-R corrects one part of Stage 11: Pu, Gong & Han (2017) alone does not establish an admissible full-equilibrium immediate-corollary sign reversal. However, Xu, Tang, Lin & Lu (2022) directly generate the same qualitative pattern — decentralized effort falls with free riding while centralized effort rises when consumers prefer the online channel — in a richer dual-channel effort-free-riding model. The frozen P3 theorem then adds only a generic mixed-partial sign characterization, not a new strategic feedback. No information-specific formal mechanism remains after label stripping.

---

## 1. Canonical state

- Starting canonical main: `48894b15f3b235610f058641ed7fd89f9bbfd6bc`
- Stage 11 PR #4: merged
- Stage 11 merge SHA: `48894b15f3b235610f058641ed7fd89f9bbfd6bc`
- Stage 11 final HEAD: `a37dec97d2e3f6f4e72e3fb7076f1565482a837b`
- Stage 8 freeze SHA: `ef588465430f618b56cf84445681752702c161e1`
- Workflow v1.1 SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 6-R branch: `stage6/novelty-rekill-free-riding`

The rollback is logical, not historical. No reset to an old Stage-6 SHA occurred.

---

## 2. Frozen current equations

Private FOC:

`m_S omega_S D_S' g' = C'`.

Under local concavity:

`deP/deta < 0` because `omega_S'<0`.

Coordinated FOC:

`[A_S omega_S D_S' + A_R omega_R D_R'] g' = C'`.

Under local concavity:

`sign(deC/deta) = sign(A_S omega_S' D_S' + A_R omega_R' D_R')`.

Condition (G),

`A_R omega_R' D_R' > -A_S omega_S' D_S'`,

is exactly positivity of this coordinated mixed partial. Under one-for-one reallocation/equal route response it reduces to `A_R>A_S`.

This is mathematically correct, but it is primarily a sign characterization.

---

## 3. Pu, Gong & Han (2017): reproduction and correction

Bibliographic verification:

Xujin Pu, Lei Gong & Xiaohua Han (2017), “Consumer free riding: Coordinating sales effort in a dual-channel supply chain,” *Electronic Commerce Research and Applications* 22, 1–12. DOI `10.1016/j.elerap.2016.11.002`.

Publisher-verified centralized objective:

`Pi_C = (p_r-c)[a_r-beta_1 p_r + eps p_d + (1-tau)s] + (p_d-c)[a_d-beta_2 p_d + eps p_r + tau s] - eta_s s^2/2`.

The centralized decision variables are `p_r,p_d,s`.

Conditional effort FOC:

`eta_s s = (p_r-c)(1-tau) + (p_d-c)tau`.

Holding prices fixed would imply

`partial s / partial tau = (p_d-p_r)/eta_s`.

But this is **not** the full equilibrium derivative. The total derivative also contains endogenous price responses:

`eta_s ds/dtau = (p_d-p_r) + (1-tau)dp_r/dtau + tau dp_d/dtau`.

Pu's deterministic published result is that both decentralized and centralized sales effort decrease with free riding. The paper's motivating environment also has consumers inspect offline and buy online at a lower price.

Therefore Stage 6-R does **not** verify an admissible Pu baseline region giving `ds_D/dtau<0<ds_C/dtau` merely by imposing `p_d>p_r`.

Pu classification: **`STRUCTURALLY VERY CLOSE`**, not a stand-alone `ABSORBED — IMMEDIATE COROLLARY` finding.

---

## 4. Xu, Tang, Lin & Lu (2022): stronger result-level prior

Bibliographic verification:

Senyu Xu, Huajun Tang, Zhijun Lin & Jing Lu (2022), “Pricing and sales-effort analysis of dual-channel supply chain with channel preference, cross-channel return and free riding behavior based on revenue-sharing contract,” *International Journal of Production Economics* 249, 108506. DOI `10.1016/j.ijpe.2022.108506`.

Publisher metadata and an author-uploaded CC-BY full text were inspected.

Their model defines offline-channel preference `theta`, effort sensitivity `alpha`, free-riding coefficient `beta`, and `0<=beta<=alpha`.

The effort-created demand terms are:

- offline: `(alpha-beta)e`;
- online: `beta e`.

With `eta_current=beta/alpha`, these are exactly proportional to

`(1-eta_current)e` and `eta_current e`.

Thus the effort-benefit allocation is the frozen one-for-one reallocation architecture up to scale, while Xu et al. additionally endogenize prices, financing, return terms, and other margins.

Their full-text sensitivity analysis reports:

- decentralized sales effort falls with `beta`;
- centralized sales effort rises with `beta` when consumers prefer the online channel;
- centralized sales effort falls with `beta` when consumers prefer the offline channel.

Their figures separately analyze `theta=0.62` (offline-preference case) and `theta=0.35` (online-preference case), within the stated `theta in [0.3,0.7]` parameter exercise.

Hence a published, admissible model configuration already generates the qualitative headline pattern

`deD/dbeta < 0 < deC/dbeta`.

Evidence limitation: the `beta` sign reversal is established in Xu et al.'s numerical sensitivity analysis rather than as a standalone general analytic theorem in `beta`. This prevents classifying the frozen formula (G) as verbatim/exact prior art. It does not restore economic novelty because the frozen paper's additional statement is only the generic IFT condition for when that already-known sign pattern occurs.

Xu classification relative to literal P3 formula: **`STRUCTURALLY VERY CLOSE`**.

Xu result-level implication: **the economic sign-reversal contribution is already present.**

---

## 5. Whole-game absorption

The frozen core nominally contains `M,S,R`, but Stage 8 explicitly states that `M` is not an active strategic chooser in the core theorem. `R` also has no strategic action. `S` alone chooses effort.

Frozen strategic graph:

`eta -> route weights -> e -> x=g(e) -> route quantities`.

No upstream adoption, investment, quality, disclosure, ownership, or response decision follows `x`.

Consequently, `x=g(e)` can be absorbed into the route benefit functions for the static comparative-static theorem. Information has an institutional interpretation but no independent strategic state.

The closest free-riding models use the same fundamental wedge:

1. a downstream provider pays for costly effort;
2. some effort-created value is captured through another route;
3. private effort internalizes too little of the cross-route return;
4. centralized/integrated choice internalizes both channels;
5. changing the allocation of effort-created value changes the private/system effort incentives differently.

The current frozen game is strategically simpler than Xu et al., not richer.

**Whole-game verdict: contribution-grade absorption.**

---

## 6. Condition (G) hard test

Classification: **local mixed-partial sign condition / assumption equivalent to the desired coordinated sign under the stated concavity conditions.**

It is economically interpretable: the expanding route's increase in marginal system value must exceed the shrinking route's loss. But it does not add a strategic interaction beyond route-value weighting.

One-for-one `A_R>A_S` says that reallocating effort-created value toward the route with greater integrated marginal return raises integrated desired effort.

That is not sufficient proposition-level novelty after the free-riding literature re-kill.

---

## 7. Information-specific reverse-kill defense

Strongest defense considered:

> Information is reusable and improves an upstream product, unlike ordinary contemporaneous sales service.

This defense fails **within the frozen model** because P3 has none of the formal features that would make information strategically distinct:

- no persistent information stock;
- no intertemporal reuse/depreciation;
- no endogenous upstream adoption of information;
- no information ownership/access choice;
- no acquisition-versus-disclosure choice;
- no upstream design/quality response;
- no competing information producers;
- no information asymmetry generated by `x`.

Noncontractibility is a defensible primitive but does not create a new feedback; current 2026 IO work also explicitly studies noncontractible vertical effort.

Reverse-kill defense: **FAIL**.

---

## 8. Proposition disposition

### P3

Prior-art classification: **`STRUCTURALLY VERY CLOSE`** at literal theorem/formula level.

Contribution status: **KILLED**.

Reason: exact qualitative sign reversal is already generated by Xu et al. 2022, while the frozen generalization supplies no new strategic primitive and condition (G) is the generic sign condition.

### P2

Prior-art classification: **`ABSORBED — IMMEDIATE COROLLARY`** at the reduced-form effort-allocation level.

Contribution status: **KILLED AS CONTRIBUTION**, retained as mathematically valid support.

### P1

Prior-art classification: **`COMPONENT OVERLAP`**.

Status unchanged: robustness/tractable special case only.

### P4

**KILLED, unchanged.**

RRC, foreclosure and strategic wholesale-pricing branches remain killed.

---

## 9. Welfare / retention

`eP<eC` is the standard underinternalization/free-riding wedge.

The additional `eC<eW` benchmark is mathematically valid but arises from consumer-surplus/product-value benefits beyond vertically coordinated profit. No independent strategic novelty was found.

Widening private/coordinated and private/social gaps remain valid but are driven by the same route-value reweighting.

The local retention implication is adjacent to established service-channel/free-riding/channel-structure logic, including Bernstein, Song & Zheng (2009). It does not rescue the contribution.

---

## 10. 2026 frontier check

- Bisceglia et al. (2026), DOI `10.1111/joie.70026`: noncontractible vertical efforts are an established IO primitive; this weakens noncontractibility as a rescue argument.
- Haque et al. (2026), DOI `10.1016/j.ejor.2026.08.015`: persistent service carry-over creates a genuinely distinct dynamic state and strategic encroachment response. This is precisely the kind of formal structure absent from the frozen static model.
- Shi, Zhang & Xie (2026), DOI `10.1016/j.iref.2026.105252`: downstream complaints can propagate to upstream supplier innovation empirically. This supports institutional plausibility but not theorem novelty.

---

## 11. Search and evidence counts

- serious prior-art candidates retained: **20**;
- current-pass full/model-level inspections: **8**;
- strongest initial threat: Pu et al. 2017;
- strongest final result-level prior: **Xu et al. 2022**.

See `SEARCH_LOG.md` and `PRIOR_ART_LEDGER.md`.

---

## 12. Killed and surviving claims

Killed contribution-grade claims:

- P3 as a novel information-appropriability sign-reversal mechanism;
- P2 as a novel cross-route-reuse theorem;
- welfare wedge as an independent primary novelty claim;
- retention implication as an independent novelty claim.

Surviving non-contribution results:

- frozen mathematics remain internally valid;
- institutional primitive “downstream field/customer information can improve upstream product/innovation” remains plausible;
- existing manuscript/code remain reproducible but are stale as a submission candidate because novelty failed.

**Surviving contribution set: EMPTY.**

---

## 13. Revised maximum novelty statement

No submission-grade novelty statement survives for the current frozen model.

The maximum accurate research-record statement is:

> The project derives a general static characterization of when downstream reallocation can make private and integrated effort move in opposite directions, but Stage 6-R finds that the underlying cross-route effort-appropriability mechanism and the qualitative sign reversal are already present in dual-channel free-riding theory; the information interpretation does not create an additional strategic state in the frozen model.

This is a negative-result statement, not a paper contribution claim.

---

## 14. Diagnosed deficiency

**The current model treats information as a monotone effort-generated common input but gives information no independent strategic state or response margin, so after label stripping the core game collapses to established cross-channel effort free riding and its private/system incentive wedge.**

---

## 15. Theory-change control

- theory modified: **NO**
- Stage 8 modified: **NO**
- manuscript modified: **NO**
- code/tests modified: **NO**
- Stage 11 modified: **NO**

No attempt was made to add dynamics, contracts, upstream strategic choices, persistence, bargaining, or additional players.

---

## 16. Final Stage 6-R verdict

**Canonical verdict: `NO-GO`.**

**Routing/status: `CURRENT CONTRIBUTION BRANCH TERMINATED`.**

Stage 12 Journal Positioning remains **NOT AUTHORIZED**.

A Stage 3 pivot is eligible only if it searches for a distinct architecture in which information itself becomes economically essential through a formal state, decision, ownership/access margin, upstream response, intertemporal mechanism, or strategic interaction. Stage 6-R does not select or build that model.