# Stage 11 — Robustness / Referee Attack Gate

## Executive verdict

**Canonical verdict: `NO-GO`**

**Routing/status: `REOPEN EARLIER STAGE / NO-GO`**

**Earliest required rollback: Stage 6 — Novelty Re-Kill.**

Stage 11 found an unresolved fatal prior-art / whole-game absorption problem. The current manuscript is mathematically coherent, but the main private-versus-coordinated effort architecture is too close to an already solved dual-channel sales-effort free-riding model to proceed directly to journal positioning. The fatal result is retained rather than repaired with new theory inside Stage 11.

---

## 1. Canonical state

- Starting post-Stage-10 `main`: `1564118776a225424e8efd040e68daf197ef023a`
- Stage 10 PR #3: merged
- Stage 10 final HEAD: `0118d08ac0cedc4386d527cbb78a7be372951bfd`
- Stage 8 freeze SHA: `ef588465430f618b56cf84445681752702c161e1`
- Workflow: `research-paper-workflow` v1.1
- Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 11 branch: `stage11/referee-attack`

No historical branch was deleted or rewritten. See `BRANCH_HYGIENE.md`.

---

## 2. Referee A — novelty and mechanism

### Verdict: REJECT — FATAL

The strongest attack is not that the current theorem is algebraically false. It is that the reduced-form game underlying the headline result is already present in the dual-channel sales-effort free-riding literature.

The critical source is:

Xujin Pu, Lei Gong & Xiaohua Han (2017), “Consumer free riding: Coordinating sales effort in a dual-channel supply chain,” *Electronic Commerce Research and Applications* 22, 1–12. DOI: `10.1016/j.elerap.2016.11.002`.

The publisher-indexed centralized objective includes the sales-effort terms

```text
(p_r-c)[... + (1-tau)s] + (p_d-c)[... + tau s] - eta_s s^2/2.
```

Holding channel prices fixed, the centralized effort FOC therefore has the structure

```text
eta_s s_C = (p_r-c)(1-tau) + (p_d-c)tau,
```

so

```text
ds_C/dtau = (p_d-p_r)/eta_s.
```

Pu et al. impose an economically natural online-lower-price environment, so their reported comparative static is that centralized as well as decentralized sales effort falls as free riding rises. But the solved objective already implies the opposite centralized sign immediately when the expanding route has the larger system margin.

The frozen paper's one-for-one benchmark is the same weighting architecture:

```text
omega_S = 1-h,
omega_R = h,
D_S' = D_R',
coordinated sign iff A_R > A_S.
```

Its welfare benchmark uses a common price with `c_S>c_R`, hence

```text
p-c_R > p-c_S,
```

which is exactly a larger expanding-route system margin. The frozen formulas give

```text
deP/dh = -m beta/k < 0,
deC/dh = beta(c_S-c_R)/k > 0.
```

Thus the headline sign reversal is not found verbatim as Pu et al.'s reported proposition, but it is an immediate parameter-ordering corollary of their already solved two-route effort-spillover architecture. Under the canonical whole-game test, that is a fatal novelty threat.

The broader free-riding literature reinforces the absorption concern:

- Bernstein, Song & Zheng (2009), “Free riding in a multi-channel supply chain,” DOI `10.1002/nav.20379`.
- Xing & Liu (2012), “Sales effort free riding and coordination with price match and channel rebate,” DOI `10.1016/j.ejor.2011.11.029`.
- Sun & Liu (2023), “Pricing and sales-effort coordination facing free riding behaviors between a brick-and-mortar retailer and a platform store owned by the manufacturer,” DOI `10.1016/j.tre.2023.103285`.

All study costly downstream effort whose benefits leak to another route and the resulting private/system coordination problem.

### Label-stripping result

The current paper interprets `e` as costly information production that generates `x=g(e)`, which improves an upstream product. That institutional interpretation is potentially meaningful. But in the frozen core theorem:

- the upstream producer `M` makes no strategic choice;
- product improvement has no separate state or dynamic law beyond `g(e)`;
- route demand responds to the common effort-generated input through `D_i(g(e))`;
- `eta` operates only through route weights;
- `S` pays the effort cost and internalizes its own-route return;
- the coordinated objective adds both route returns.

After stripping the information labels, this is the same effort-spillover / free-riding architecture. Stage 11 therefore cannot certify a proposition-level novelty distinction.

---

## 3. Referee B — assumptions, mathematics, robustness

### Verdict: MATHEMATICS PASS; CONTRIBUTION ATTACK SURVIVES

Independent inspection found no material algebraic disagreement between the manuscript and committed symbolic code.

### Condition (G)

The coordinated FOC is

```text
Phi_C = [A_S omega_S D_S' + A_R omega_R D_R'] g' - C'.
```

The mixed partial with respect to reallocation has sign determined by

```text
A_S omega_S' D_S' + A_R omega_R' D_R'.
```

Condition (G) is exactly positivity of this bracket. Under local concavity, it is therefore exactly the local sign condition for `deC/deta>0`.

This makes P3 mathematically correct, but the general theorem is primarily a sign characterization. Its deeper economic content must come from a primitive mapping of (G), not from the IFT itself. The one-for-one case supplies the mapping `A_R>A_S`, and the welfare benchmark supplies `c_S>c_R`; however, the Pu et al. objective shows that this weighted-margin logic already exists in the free-riding literature.

### Robustness

The general model is not limited to linear-quadratic forms. Nonlinear `omega_i`, `D_i`, `g`, and nonquadratic `C` are already allowed under the frozen local-concavity conditions. This attack is answered mathematically but does not cure the novelty problem.

### Noncontractibility

Noncontractibility is defensible as a scope primitive, not as a universal market condition. Relevant current IO work includes Bisceglia, Israel, Piccolo & Ramezzana (2026), “RPM and Vertical Integration With Upstream Competition and Noncontractible Efforts,” DOI `10.1111/joie.70026`. The existing free-riding literature also demonstrates that contracts can sometimes coordinate effort. The manuscript already avoids claiming that no contractual response exists.

### Boundary and proof status

P3 is stated for unique interior optima and the organizational retention implication is explicitly local. No global/corner theorem was found hiding behind local FOCs.

---

## 4. Referee C — welfare, institution, empirical content

### Verdict: NO INDEPENDENT FATAL ERROR; DOES NOT RESCUE NOVELTY

The welfare formulas are internally consistent:

```text
eP = m beta(1-h)/k,
eC = beta[(p-c_S)(1-h)+(p-c_R)h]/k,
eW = beta[a-c_S(1-h)-c_R h]/(k-beta^2).
```

Under the frozen restrictions, `eP<eC<eW` follows. The manuscript also distinguishes coordinated and social effort correctly.

The welfare result does not cure the main novelty attack because the positive coordinated sign itself maps to the same route-margin weighting already visible in prior free-riding models.

### Primary-source institutional re-check

Stage 11 independently found primary evidence supporting the narrow primitive “field/service/customer information can feed product improvement” across all five frozen example classes:

- **Appliances:** Panasonic Sustainability Data Book / VOC material states that customer voices from customer-care, sales partners, showrooms and service companies are analyzed and used for product development, functionality and quality improvement. Panasonic's HVAC site also documents concrete product changes from maintenance/service requests.
- **Automobiles:** Toyota's *Sustainable Management Report 2016* describes customer opinions gleaned from dealers and assistance centers being incorporated into design/manufacturing and better products/services.
- **Agricultural machinery:** John Deere's sustainability reporting states that warranty claims, connected-machine data, and dealer/customer feedback feed continuous product improvement, and that customer feedback drives process and product modifications.
- **Heavy equipment:** Caterpillar's current product-support descriptions explicitly make dealer/customer feedback an input into Continuous Product Improvement and product-group prioritization.
- **Medical devices:** Medtronic's sustainability reporting states that healthcare-professional feedback is integrated into product design; product pages also identify design changes influenced by customer feedback.

These sources support only the primitive. They do not establish the causal elasticity from route rents to effort and do not prove P3.

The Stage 10 manuscript does not currently show these primary citations, which would be a bounded evidence repair if the theory branch survived. Because the novelty failure is fatal, Stage 11 does not polish the stale manuscript before rollback.

### 2026 empirical frontier

Shi, Zhang & Xie (2026), “From complaints to creativity: How consumer complaints drive supplier innovation,” DOI `10.1016/j.iref.2026.105252`, provides recent empirical evidence that downstream consumer complaints can propagate to upstream supplier innovation. This strengthens plausibility of the information-flow primitive but does not restore novelty of the frozen theorem.

---

## 5. Referee D — field fit and exposition

### Verdict: REJECT AT CURRENT CONTRIBUTION

The current paper is written carefully and largely stays inside the Stage 8 claim boundary. The problem is contribution magnitude after label stripping.

The core theorem has one substantive chooser, exogenous route weights, and a separable coordinated objective. `M` is a label for where the common product improvement is used rather than an active strategic player in P3. Once the same weighted-effort externality is recognized in prior dual-channel free-riding models, Stage 12 journal positioning would be premature.

Current 2026 theory also reinforces that noncontractible vertical effort and direct-channel free-riding remain active literatures rather than a vacant field. Relevant sources include Bisceglia et al. (2026), DOI `10.1111/joie.70026`, and Haque et al. (2026), “Supplier encroachment and retail service effort: The role of carry-over effect and strategic inventory,” DOI `10.1016/j.ejor.2026.08.015`.

---

## 6. Consolidated severity

See `REFEREE_ATTACK_LEDGER.md` for attack-level details.

- Total attack classes: **18**
- FATAL: **5**
- MAJOR BUT FIXABLE: **3**
- MINOR: **10**

The five FATAL labels are different canonical attack classes but principally trace to one underlying defect: **the current main result is absorbed at the reduced-form/whole-game level by established cross-channel effort-free-riding theory, and condition (G) does not generate an independently deeper theorem.**

---

## 7. Bounded repairs

No manuscript repair was implemented after the fatal novelty finding.

This is intentional. Adding citations, clarifying (G), or adding institutional footnotes would improve presentation but would not answer the fatal whole-game absorption attack. Adding contracts, dynamics, active upstream choices, or other mechanisms would violate Stage 11 theory-change control.

See `FIX_LEDGER.md`.

---

## 8. Mathematical / reproducibility verification

Direct source audit before the Stage 11 PR:

- private FOC: consistent with frozen model;
- coordinated FOC: consistent;
- IFT sign formulas: consistent;
- condition (G): algebraically consistent;
- P2 cross-route-off result: consistent;
- one-for-one reduction: consistent;
- welfare ordering: consistent;
- widening wedge formulas: consistent;
- coordinated/social distinction: consistent;
- Stage 8 frozen files: untouched;
- manuscript/code/tests/outputs: untouched by Stage 11.

Hosted current-head CI is required on the Stage 11 PR. The CI result is operational verification only and cannot override the fatal novelty verdict.

**Hosted CI status at report creation: PENDING.**

---

## 9. Theory-change implications

The correct rollback is **Stage 6 — Novelty Re-Kill**, because the fatal issue is newly resolved prior art against the already-solved theorem rather than an algebraic failure.

Stage 6 must explicitly compare the frozen model against at least:

1. Pu, Gong & Han (2017), including the centralized effort objective and decentralized retailer effort;
2. Xing & Liu (2012);
3. Bernstein, Song & Zheng (2009);
4. Sun & Liu (2023);
5. Murry (2018);
6. Chen (2019);
7. Bisceglia et al. (2026);
8. the August 2026 Haque et al. service-effort/encroachment frontier;
9. relevant feedback-to-innovation evidence including Shi, Zhang & Xie (2026).

The Stage 6 test must ask whether the information-specific interpretation creates any non-relabeling player/objective/strategy/timing/allocation/feedback difference and any theorem unavailable as an immediate corollary of the dual-channel effort-spillover models.

If not, terminate the current contribution branch.

If yes only after changing the strategic architecture, route to the earliest affected theory stage rather than editing Stage 8 or the manuscript in place.

---

## 10. Final Stage 11 verdict

**Canonical verdict: `NO-GO`.**

**Routing/status: `REOPEN EARLIER STAGE / NO-GO`.**

**Next canonical route: Stage 6 — Novelty Re-Kill.**

Stage 12 Journal Positioning is **not authorized** on the present contribution.
