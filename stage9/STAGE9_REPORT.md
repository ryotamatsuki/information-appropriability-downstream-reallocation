# Stage 9 Report — Repository / Reproducibility Setup

## 1. Executive Verdict

**CONDITIONAL GO**

Exactly one infrastructure blocker remains: GitHub Actions jobs are created but fail before any runner is assigned. The available GitHub API shows both jobs with `runner_id: 0`, empty runner names, and zero steps. No repository code or workflow step executes, so this is classified as a CI infrastructure / runner-allocation blocker rather than a theory-verification failure.

## 2. Repository Status

Production reproducibility architecture is implemented on `stage9/reproducibility-setup` and exposed in PR #2. The PR is intentionally not merged.

## 3. Theory Freeze Verification

Stage 8 PR #1 is merged. Canonical freeze SHA: `ef588465430f618b56cf84445681752702c161e1`.

Freeze integrity: **PASS**. PR #2 changes 49 files and none is under `stage8/**`.

## 4. Freeze SHA

`ef588465430f618b56cf84445681752702c161e1`

## 5. Repository Architecture

Implemented:
- pinned Python environment;
- independent SymPy derivations;
- deterministic numerical regression;
- pytest regression suite;
- committed deterministic outputs and hashes;
- minimal LaTeX scaffold;
- Makefile one-command build;
- GitHub Actions workflow;
- reproducibility/freeze documentation;
- result-to-script-to-test-to-output verification matrix.

## 6. Dependency Environment

- Python 3.13.5
- SymPy 1.14.0
- pytest 9.0.2
- no NumPy/SciPy dependency required

## 7. Build System

GNU Make targets:
- `make verify`
- `make outputs`
- `make manuscript`
- `make all`
- `make clean`

## 8. Symbolic Verification Architecture

General-model and welfare scripts derive frozen formulas from objectives rather than hard-coding reported answers.

## 9. General-Model Verification

**PASS**

Reproduced:
- private FOC;
- private IFT derivative;
- coordinated FOC;
- condition (G);
- cross-route necessity;
- one-for-one reduction to `A_R>A_S`.

## 10. Welfare Verification

**PASS**

From the frozen utility/objectives, the implementation re-derives:
- demand;
- `e^P`;
- `e^C`;
- `e^W`;
- `e^P<e^C<e^W` under the frozen restrictions;
- widening private–coordinated and private–social effort gaps.

## 11. Numerical Verification

**PASS**

Deterministic seed: `20260828`.

10,000 admissible draws produced:
- 0 demand failures;
- 0 effort-positivity failures;
- 0 ordering failures;
- 0 widening-wedge failures.

100 direct objective-maximization cross-checks were performed. Maximum absolute direct-vs-closed-form effort error: approximately `1.188e-06`, below the frozen numerical tolerance `2e-06`.

## 12. Boundary Checks

**PASS — 5/5**

Smoke checks cover small `beta`, route shares near 0/1, a vanishing distribution-cost gap, and approach to the social-concavity boundary from the admissible side.

## 13. Tests

Local final suite: **18 passed, 1 skipped**.

The sole local skip is the Git-history freeze-integrity test because the isolated execution directory is not a Git checkout. That integrity condition is independently verified from the actual PR changed-file set.

## 14. Deterministic Outputs

**PASS**

Two successive local regenerations produced identical SHA256 hashes for all committed files in `outputs/`.

## 15. LaTeX Scaffold

**PASS**

`latexmk` cleanly compiles the scaffold. The generated PDF is a build artifact and is not committed. Section files contain headings/placeholders only; no manuscript prose was written.

## 16. Bibliography Status

**PASS**

`references.bib` is intentionally empty pending verified import from the Stage-6 literature ledger. No bibliographic metadata was fabricated.

## 17. Reproducibility Documentation

**PASS**

`docs/REPRODUCIBILITY.md` documents fresh setup, verification, output regeneration, manuscript compilation, clean build, expected outputs, and rollback handling.

## 18. Freeze Integrity Guard

**PASS in repository diff; CI execution blocked before runner allocation.**

The test compares `stage8/**` against the canonical freeze SHA. PR #2 independently confirms no Stage-8 file is changed.

## 19. CI Architecture

Two jobs are defined:
- `verification`: Python setup, dependency install, freeze/theory tests, output regeneration, generated-output diff check;
- `manuscript-build`: minimal LaTeX install and scaffold compilation.

The workflow uses official `actions/checkout@v7` and `actions/setup-python@v7`.

## 20. CI Result

**NOT FEASIBLE — INFRASTRUCTURE BLOCKER**

Initial run: `33173228843`.

Both `verification` and `manuscript-build` were marked failure before runner assignment. GitHub reports `runner_id: 0`, empty runner names, and `steps: []` for both jobs. Therefore no workflow step executed and no code-level CI failure was observed.

## 21. Clean-Build Result

**PASS locally.**

`make all` succeeded from a clean-output rebuild, including symbolic/numerical verification, deterministic output generation, and LaTeX compilation.

## 22. Verification Matrix

**COMPLETE**, with CI runner execution recorded as the sole unresolved infrastructure item.

## 23. Stage 9 Kill Tests

| Kill test | Result |
|---|---|
| 1 Freeze Integrity | PASS |
| 2 Symbolic Reproduction | PASS |
| 3 Welfare Reproduction | PASS |
| 4 Condition G | PASS |
| 5 Cross-Route Necessity | PASS |
| 6 Determinism | PASS |
| 7 Numerical Regression | PASS |
| 8 Fresh/Clean Build | PASS locally |
| 9 Dependency Reproducibility | PASS |
| 10 Manuscript Scaffold | PASS |
| 11 Bibliographic Integrity | PASS |
| 12 CI | WARNING — runner allocation unavailable |
| 13 No Theory Drift | PASS |
| 14 Auditability | PASS |

## 24. Theory Drift Audit

**PASS**

No new theorem, mechanism, strategic variable, welfare friction, or substantive assumption was introduced. P3 remains MAIN; P2 supporting; P1 special-case robustness; P4 and the Stage-2 RRC branch remain killed.

## 25. Stage Verdict

**CONDITIONAL GO**

## 26. Routing / Status

**REPRODUCIBILITY READY EXCEPT FOR ONE CI INFRASTRUCTURE BLOCKER.**

Do not merge PR #2 automatically. Resolve or explicitly accept the GitHub Actions runner-allocation blocker, rerun CI, and then re-evaluate Stage 9 for GO.

## 27. Stage 10 Contract

Stage 10 may begin only after Stage 9 is upgraded to GO and PR #2 is merged. Stage 10 may write manuscript prose in dependency order but may not change the frozen research question, mechanism, condition (G), theorem, welfare ordering, P4/RRC killed status, or novelty boundary.

# Canonical Stage 9 Handoff Record

Stage 9 verdict: **CONDITIONAL GO**

Repository: `ryotamatsuki/information-appropriability-downstream-reallocation`

Canonical theory freeze SHA: `ef588465430f618b56cf84445681752702c161e1`

Theory freeze integrity: **PASS**

Repository architecture: **READY**

Python environment: **3.13.5**

Dependency lock: **PASS**

Symbolic verification: **PASS**

Numerical verification: **PASS**

Welfare verification: **PASS**

General theorem verification: **PASS**

Cross-route necessity verification: **PASS**

P1 special-case verification: **PASS — ROBUSTNESS / SPECIAL CASE ONLY**

P4 status: **KILLED**

Deterministic outputs: **PASS**

Clean build: **PASS locally**

Manuscript scaffold: **PASS**

Bibliography integrity: **PASS**

CI: **NOT FEASIBLE — runner-allocation infrastructure blocker**

CI run: `33173228843`

Freeze-integrity guard: **PASS by actual PR diff; CI execution unavailable**

Verification matrix: **COMPLETE**

Reproducibility manifest: **COMPLETE**

Theory changes introduced: **NONE**

Theory rollback required: **NO**

One precise blocker: **GitHub Actions jobs fail before runner assignment (`runner_id=0`, no runner name, zero steps), so clean hosted CI cannot currently execute.**

Stage 9 branch: `stage9/reproducibility-setup`

Stage 9 implementation commit: `c11a3628aa28515a3462f35c218a8bf2339cad5a`

Stage 9 PR: **#2 — Stage 9 — Repository and Reproducibility Setup**

What Stage 10 may change: manuscript prose, exposition, equation numbering, section integration, verified bibliography integration.

What Stage 10 may NOT change: frozen theory, players, timing, information structure, condition (G), theorem results, welfare ordering, killed claims, or novelty boundary.

Next route: **RESOLVE/ACCEPT THE SINGLE CI INFRASTRUCTURE BLOCKER → RERUN STAGE 9 CI → GO/MERGE → STAGE 10.**
