# Stage 11 Referee Attack Ledger

Severity labels follow the canonical Stage 11 template: `FATAL`, `MAJOR BUT FIXABLE`, `MINOR`.

The initial hostile review was performed against the merged Stage 10 manuscript before manuscript repair. A fatal prior-art/whole-game absorption finding terminates bounded manuscript repair; later comments are retained because negative results are canonical research outputs.

## Referee A — novelty / mechanism

### RA-01 — Exact-prior-art / immediate-corollary attack
- **Attack:** The core private-versus-coordinated effort architecture is already present in dual-channel sales-effort free-riding models, and the positive coordinated sign is an immediate margin-ordering corollary of an already solved centralized objective.
- **Severity:** FATAL
- **Evidence:** Pu, Gong & Han (2017), *Electronic Commerce Research and Applications* 22, 1–12, DOI `10.1016/j.elerap.2016.11.002`. The publisher-indexed centralized objective contains route effort terms `(1-tau)s` and `tau s` weighted by route margins. With fixed prices its effort FOC is proportional to `(p_r-c)(1-tau)+(p_d-c)tau`. Their maintained online-lower-price case makes centralized effort fall with free riding; reversing the route-margin ordering makes it rise immediately. The frozen paper's one-for-one benchmark is `omega_S=1-tau`, `omega_R=tau`, equal marginal response, and coordinated sign `A_R>A_S`. The welfare benchmark sets common price and `c_S>c_R`, hence `p-c_R>p-c_S`, exactly the required route-margin reversal.
- **Can the paper answer now?:** No. The distinction “information improving an upstream product” is not represented by an additional strategic or state variable in the core model; after label stripping the effort spillover game is nested in the established free-riding architecture.
- **Required fix:** Reopen Stage 6 and conduct an exact whole-game/proposition-level absorption test against Pu et al. and the wider sales/service-effort free-riding literature. If an information-specific theorem survives only after changing the game, route that change through the earlier theory gates.
- **Does the fix reopen theory?:** YES if a new strategic architecture is required; the novelty audit itself reopens Stage 6.
- **Resolved?:** NO.

### RA-02 — Classic-result / relabeling attack
- **Attack:** Costly downstream effort that benefits another route, while the effort provider captures only its own-route return, is a standard cross-channel free-riding problem.
- **Severity:** FATAL
- **Evidence:** Bernstein, Song & Zheng (2009), DOI `10.1002/nav.20379`; Xing & Liu (2012), DOI `10.1016/j.ejor.2011.11.029`; Pu, Gong & Han (2017), DOI above; Sun & Liu (2023), DOI `10.1016/j.tre.2023.103285`. These papers explicitly study one retail route supplying costly service/sales effort from which another route benefits, decentralized effort under-provision, and centralized/contractual coordination.
- **Can the paper answer now?:** Not at the current frozen level. The upstream-product-improvement interpretation is economically suggestive but the core equations do not create a strategically distinct feedback beyond a common demand-enhancing effort spillover.
- **Required fix:** Stage 6 re-kill must determine whether a non-relabeling information-production distinction exists.
- **Does the fix reopen theory?:** Potentially YES.
- **Resolved?:** NO.

### RA-03 — Condition (G) built into the result
- **Attack:** In the general separable model, condition (G) is exactly the condition that the coordinated FOC's eta mixed partial is positive, so the positive coordinated comparative static is assumed as a sign restriction rather than derived from deeper primitives.
- **Severity:** MAJOR BUT FIXABLE only as exposition; contribution-grade repair may require theory reopening.
- **Evidence:** `code/symbolic/general_model.py` and equations in `02_equilibrium.tex` / `03_main_results.tex`: `deC/deta` has the sign of `A_S omega_S' D_S' + A_R omega_R' D_R'`; (G) is precisely positivity of this bracket. The one-for-one case reduces to `A_R>A_S`.
- **Can the paper answer now?:** It can honestly call P3 a local sign characterization, and the frozen welfare benchmark maps the sign to `c_S>c_R`. It cannot claim that the general theorem derives (G).
- **Required fix:** If the project survives Stage 6, narrow theorem language and make the primitive benchmark mapping explicit. A genuinely deeper theorem cannot be manufactured in Stage 11.
- **Does the fix reopen theory?:** NO for wording; YES for new theory.
- **Resolved?:** NO because RA-01 blocks manuscript repair.

### RA-04 — Market-size / free-riding effect attack
- **Attack:** `e^P` falls because the effort provider's own-route coefficient shrinks; that is the same mechanical free-riding/market-footprint channel already studied in dual-channel models.
- **Severity:** FATAL as a novelty attack when combined with RA-01.
- **Evidence:** Pu et al. report that offline-store sales effort falls as the free-riding rate rises; Xing & Liu and Sun & Liu report the same qualitative force. Murry (2018), DOI `10.1016/j.ijindorg.2018.03.010`, also finds that greater dealer competition reduces relationship-specific dealer advertising.
- **Can the paper answer now?:** The cross-route reusable-information interpretation explains the application, but the frozen reduced form does not generate a distinct strategic interaction.
- **Required fix:** Stage 6 whole-game re-kill.
- **Does the fix reopen theory?:** Potentially YES.
- **Resolved?:** NO.

### RA-05 — No-new-mechanism attack
- **Attack:** The manuscript combines a shrinking own-route return with a standard effort spillover and calls the combination information appropriability; the full strategic architecture may not differ from existing dual-channel effort-free-riding models.
- **Severity:** FATAL
- **Evidence:** Same exact architecture mapping as RA-01 plus the free-riding literature above.
- **Can the paper answer now?:** No proposition-level distinction survives the label-stripping test with sufficient confidence for submission preparation.
- **Required fix:** Stage 6 re-kill before any journal positioning.
- **Does the fix reopen theory?:** Potentially YES.
- **Resolved?:** NO.

## Referee B — assumptions / mathematics / robustness

### RB-01 — Noncontractibility / alternative-contract attack
- **Attack:** If effort or its return can be compensated, the appropriability wedge may be mitigated or eliminated.
- **Severity:** MINOR for validity; important scope condition.
- **Evidence:** Xing & Liu (2012) and Sun & Liu (2023) design coordination contracts for sales-effort free riding. Bisceglia, Israel, Piccolo & Ramezzana (2026), DOI `10.1111/joie.70026`, studies vertical organization with noncontractible efforts and explicitly treats margin allocation as an incentive instrument.
- **Can the paper answer now?:** Yes as a scope assumption. The manuscript already states effort is noncontractible and labels contracting responses as outside-model interpretations.
- **Required fix:** If revived, cite the contracting/noncontractible-effort literature and avoid policy claims that presume an unmodeled contract.
- **Does the fix reopen theory?:** NO for scope clarification; YES if contracts become endogenous.
- **Resolved?:** YES for mathematical validity.

### RB-02 — Functional-form attack
- **Attack:** The result may be an artifact of linear-quadratic demand/cost.
- **Severity:** MINOR
- **Evidence:** The frozen general IFT model allows nonlinear `omega_i`, `D_i`, `g`, and nonquadratic `C`; the LQ form is confined to welfare.
- **Can the paper answer now?:** Yes.
- **Required fix:** None.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** YES.

### RB-03 — Interiority / corner / boundary attack
- **Attack:** FOC comparative statics may fail at `e=0` or route-share boundaries.
- **Severity:** MINOR
- **Evidence:** P3 is explicitly stated for unique interior optima with SOCs. Boundary tests are in the verified Stage 9 infrastructure; organizational retention is explicitly local.
- **Can the paper answer now?:** Yes, provided no global language is introduced.
- **Required fix:** None before Stage 6 routing.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** YES.

### RB-04 — P2 overreach attack
- **Attack:** Cross-route reuse is only necessary for a positive coordinated response inside the maintained separable model, not universally.
- **Severity:** MINOR
- **Evidence:** The manuscript already states “within the separable model.”
- **Can the paper answer now?:** Yes.
- **Required fix:** None.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** YES.

### RB-05 — Numerical-not-proof attack
- **Attack:** 10,000 draws cannot prove the theorem.
- **Severity:** MINOR
- **Evidence:** Analytic IFT and symbolic identities provide the proof; numerical regression is explicitly a diagnostic/reproducibility gate.
- **Can the paper answer now?:** Yes.
- **Required fix:** None.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** YES.

### RB-06 — Proof / notation inconsistency attack
- **Attack:** Frozen notation or derivative signs may differ between code and manuscript.
- **Severity:** MINOR
- **Evidence:** Direct inspection of `general_model.py`, `welfare_model.py`, and the manuscript shows formula consistency.
- **Can the paper answer now?:** Yes, subject to current-head CI.
- **Required fix:** Re-run CI on the Stage 11 PR.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** PENDING CI.

## Referee C — welfare / institution / empirical content

### RC-01 — Welfare-is-mechanical attack
- **Attack:** `eC>eP` and `eW>eC` may merely reflect adding more positive benefits to the objective.
- **Severity:** MINOR for correctness; it limits contribution weight.
- **Evidence:** `welfare_model.py` independently re-derives the ordering. The first wedge is margin appropriability; the second is consumer-surplus value. Both are mathematically correct under the frozen restrictions.
- **Can the paper answer now?:** Yes as a benchmark, but welfare cannot rescue RA-01.
- **Required fix:** None for correctness.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** YES.

### RC-02 — Coordinated-versus-social conflation
- **Attack:** The manuscript may call vertical coordination socially optimal.
- **Severity:** MINOR
- **Evidence:** Sections 1, 4, 8, and 9 explicitly distinguish `eC` from `eW`.
- **Can the paper answer now?:** Yes.
- **Required fix:** None.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** YES.

### RC-03 — Institutional source attack
- **Attack:** The manuscript names five environments without displaying primary-source citations for the field/service-information → product-improvement primitive.
- **Severity:** MAJOR BUT FIXABLE
- **Evidence:** Stage 11 re-verification found primary corporate evidence for all five categories: Panasonic VOC/product-improvement documentation; Toyota's dealer/customer-feedback-to-design/manufacturing system; John Deere reports that dealer/customer feedback drives product improvement; Caterpillar describes dealer/customer feedback feeding Continuous Product Improvement; Medtronic reports customer feedback integrated into product design.
- **Can the paper answer now?:** Yes with verified citations, but manuscript repair is not justified while RA-01 is fatal.
- **Required fix:** If Stage 6 revives the project, add primary-source citations and retain the qualifier that these sources establish only the primitive.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** Evidence verified; manuscript citation fix deferred because branch is NO-GO.

### RC-04 — Empirical/falsifiability attack
- **Attack:** Prediction 4 concerns upstream infrastructure investment, which is not an endogenous action in the model.
- **Severity:** MINOR
- **Evidence:** The section labels the five items “interpretation and falsifiability predictions,” but only effort and coordinated value are direct model objects.
- **Can the paper answer now?:** Yes by keeping prediction 4 explicitly interpretive if the project survives.
- **Required fix:** Wording only if revived.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** Bounded issue, superseded by RA-01.

## Referee D — contribution / field fit / exposition

### RD-01 — Current-frontier omission
- **Attack:** The Stage 10 Related Literature omits several frozen or newly relevant closest papers, including Murry (2018), Chen (2019), Bisceglia et al. (2026), and the extensive dual-channel free-riding literature; current 2026 work also studies supplier free-riding on retailer service effort.
- **Severity:** MAJOR BUT FIXABLE as literature coverage.
- **Evidence:** Murry 2018 DOI `10.1016/j.ijindorg.2018.03.010`; Chen 2019 DOI `10.1111/iere.12355`; Bisceglia et al. 2026 DOI `10.1111/joie.70026`; Haque et al. 2026 DOI `10.1016/j.ejor.2026.08.015`; Shi, Zhang & Xie 2026 DOI `10.1016/j.iref.2026.105252`.
- **Can the paper answer now?:** Literature can be expanded, but doing so does not resolve the fatal absorption finding.
- **Required fix:** Stage 6 must re-open these sources before manuscript reconstruction.
- **Does the fix reopen theory?:** NO for citations; YES if novelty boundary changes.
- **Resolved?:** NO.

### RD-02 — Contribution magnitude / economics field fit
- **Attack:** With `M` inactive in the core theorem and reallocation entering only through separable route weights, the main theorem is a one-decision comparative-static sign characterization. Once mapped to prior free-riding models, it is too thin to proceed to journal positioning as a distinct field-theory contribution.
- **Severity:** FATAL
- **Evidence:** RA-01 through RA-05 plus the exact sign-characterization structure of (G).
- **Can the paper answer now?:** No without establishing a nonabsorbed proposition or strategic architecture.
- **Required fix:** Reopen Stage 6 first. If no proposition-level distinction survives, terminate or pivot through Stage 3/4 rather than adding features in Stage 11.
- **Does the fix reopen theory?:** Potentially YES.
- **Resolved?:** NO.

### RD-03 — Claim-inflation / exposition attack
- **Attack:** Calling (G) “economically restrictive rather than automatic” can obscure that it is exactly the local coordinated-sign condition in the general model.
- **Severity:** MINOR relative to the fatal novelty problem.
- **Evidence:** `08_introduction.tex` and the IFT formula.
- **Can the paper answer now?:** Yes with narrower wording if revived.
- **Required fix:** Exposition only after Stage 6.
- **Does the fix reopen theory?:** NO.
- **Resolved?:** Deferred.

## Consolidated initial counts

- Total attack classes recorded: **18**
- FATAL: **5** (`RA-01`, `RA-02`, `RA-04`, `RA-05`, `RD-02`)
- MAJOR BUT FIXABLE: **3** (`RA-03`, `RC-03`, `RD-01`)
- MINOR: **10**

The five FATAL labels form one underlying fatal cluster: **whole-game/reduced-form absorption by the established dual-channel effort-free-riding literature plus the resulting lack of an independently nontrivial P3 contribution**. They are retained separately because the canonical checklist requires distinct attack classes, but they should not be interpreted as five unrelated defects.
