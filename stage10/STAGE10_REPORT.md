# Stage 10 Report — Section-by-Section Paper Construction

## 1. Canonical baseline

- Starting main SHA: `89d3c27d95dc2a14ce7e603cc23de3e8555071b2`
- Stage 8 theory freeze SHA: `ef588465430f618b56cf84445681752702c161e1`
- Workflow: `ryotamatsuki/research-paper-workflow` v1.1
- Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Branch: `stage10/manuscript-drafting`
- PR: `#3 — Stage 10 — Section-by-Section Manuscript Draft`

Stage 10 was constructed in the canonical dependency order. Final manuscript presentation places the Introduction first.

## 2. Section map

| Section | File | Frozen inputs | Key content | Primary section commit | Verdict |
|---|---|---|---|---|---|
| Model | `manuscript/sections/01_model.tex` | model specification, assumption ledger, timing | M/S/R, reallocation, reusable information, private/coordinated objectives | `87d8c98847d2be0f72e288e176c0d09544484c6b` | PASS |
| Equilibrium | `manuscript/sections/02_equilibrium.tex` | propositions, proof map, symbolic outputs | private/coordinated FOCs, SOCs, IFT derivatives | `18681d342c09ff33bf1e623199c52df5838996e3` | PASS |
| Main results | `manuscript/sections/03_main_results.tex` | propositions, claim ledger, proof map | P3 divergence, condition (G), P2 structural corollaries, proofs | `779cb53312a990c9779e3914219d85c9a50499f7` | PASS |
| Welfare | `manuscript/sections/04_welfare.tex` | welfare freeze, proof map | `e^P,e^C,e^W`, strict ordering, widening wedges, local under-retention | `2747e33c1a0a5d601357239a0dd3be93517dec9c` + proof completion | PASS |
| Robustness | `manuscript/sections/05_robustness.tex` | robustness scope | nonlinear weights/learning/costs/demand; conditional scope | `49c16879221e984188786f470f156b3c719f7e10` | PASS |
| Institutional bridge | `manuscript/sections/06_institutional_bridge.tex` | institutional scope, prediction scope | bounded primitive interpretation and exactly five frozen predictions | `886b44100ea20e8529ec2db4471341c90d3004f6` | PASS |
| Related literature | `manuscript/sections/07_related_literature.tex` | literature boundary | proposition-level distinction from verified closest-literature subset | `0aa5a0465ea8478fbcd2069e66d7913669539767` | PASS |
| Introduction | `manuscript/sections/08_introduction.tex` | Sections 1–7, claim ledger | motivation, mechanism, P3, welfare, bounded contribution | `ec26dec9cbfa8777964c4dda16a3309bd335047b` | PASS |
| Discussion | `manuscript/sections/09_discussion.tex` | claim/robustness/prediction scope | scope, organizational interpretation, empirical content, abstractions | `c28bbce6944857e57236b99ac77735424ceb61cd` | PASS |
| Conclusion | `manuscript/sections/10_conclusion.tex` | frozen result hierarchy | mechanism, theorem, welfare, limited organizational lesson | `1d5472a005e2b33717167b946f79568f12a28d91` | PASS |

`manuscript/main.tex` contains the integrated title, abstract, final presentation order, and bibliography call. The working title remains **Information Appropriability under Downstream Reallocation** because no theory-preserving alternative was clearly superior.

## 3. Proposition and proof audit

Result hierarchy is unchanged:

- P3 — **MAIN**
- P2 — supporting structural result
- P1 — robustness / tractable special case only
- P4 — **KILLED**

The RRC, foreclosure, and strategic wholesale-pricing branches remain excluded.

The manuscript states and proves the private-effort sign, the main information-incentive divergence theorem under condition (G), cross-route necessity, the one-for-one special-case reduction, and the benchmark welfare ordering. The welfare proof was strengthened during Stage 10 so that the second strict inequality is shown algebraically rather than asserted after substitution. No theorem or assumption was added.

Proof completeness: **PASS**.

## 4. Bibliography and evidence audit

`references/references.bib` contains independently verified metadata only for papers actually cited in the manuscript:

- Guo (2009)
- Guo and Iyer (2010)
- Gambardella, Raasch and von Hippel (2017)
- Huang, Chen and Guan (2020)
- Hu et al. (2021)
- Pagnozzi, Piccolo and Reisinger (2021)

No bibliographic entry was fabricated. The manuscript uses the institutional material only to defend the frozen primitive and preserves the Stage 8 qualifier that institutional examples do not establish the full causal mechanism.

A Stage 10 CI gate now requires a nonempty `main.bbl` and fails on unresolved citations or cross-references. Bibliography/reference integrity: **PASS** on validation run `33640108804`.

## 5. Reproducibility and build audit

Validation run `33640108804` on the Stage 10 branch completed both jobs successfully:

- `verification` — PASS
- `manuscript-build` — PASS

The verification job executed the frozen symbolic models, welfare model, special case, 10,000-draw numerical regression, pytest, deterministic output regeneration, and output diff check.

Pytest: **19 passed**.

The manuscript job executed:

1. `make manuscript` — PASS;
2. bibliography/cross-reference integrity gate — PASS;
3. exact `make all` clean integration build — PASS;
4. post-`make all` bibliography/cross-reference gate — PASS;
5. generated-output diff check — PASS.

The initial Stage 10 manuscript run exposed a bibliography-path integration defect. It was fixed without theory change by making the BibTeX search path explicit through the Makefile and adding hard bibliography-resolution gates. No test was weakened.

## 6. Freeze and drift audit

Relative to starting main, Stage 10 changes manuscript sources, verified bibliography, the Stage 10 report, and build/CI plumbing needed for exact `make all` and bibliography-integrity checks. It does **not** change:

- `stage8/**`;
- `code/**`;
- `tests/**`;
- `outputs/**` as committed canonical content.

Stage 8 freeze integrity: **PASS**.

Substantive theory drift: **NONE**.

Novelty boundary: **PASS**. The manuscript does not claim novelty for generic information externalities, user innovation, retailer information, channel structure, RRC, omnichannel effects, P4, or unconditional sign reversal.

## 7. Target journal

No canonical target journal was specified in the frozen repository records inspected for Stage 10. The draft is therefore written as a field-journal-quality theory manuscript without outlet-specific formatting. This remains a presentation decision, not a theory blocker.

## 8. Remaining manuscript gaps

No Stage 10 blocker remains. Stage 11 may attack exposition, theorem presentation, literature positioning, welfare interpretation, and model assumptions, but may not treat unmotivated model expansion as the default repair.

## 9. Stage verdict

**FULL DRAFT READY FOR REFEREE GATE**

## 10. Next route

Leave PR #3 open for explicit merge authorization. After merge, proceed to **Stage 11 — Robustness / Referee Attack** under the canonical workflow.
