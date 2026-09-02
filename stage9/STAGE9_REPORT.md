# Stage 9 Report — Repository / Reproducibility Setup

## 1. Executive Verdict

**GO — READY FOR MERGE**

The GitHub-hosted runner-allocation failure has been resolved by rerunning the existing workflow. Final hosted run `33635911794` executed both jobs on `ubuntu-latest` and completed successfully. A single Stage 9 implementation defect was found after runner allocation in the generated manifest's Unicode serialization and fixed in commit `314ce17690c0264db5607212b97b2cd099e1b8b7`; no theory change was made.

## 2. Repository Status

Production reproducibility architecture is implemented on `stage9/reproducibility-setup` and exposed in PR #2. Final branch HEAD: `8c39cc32866eb8212bf804253a2ab0ff74012af3`. The PR remains intentionally open and is **READY FOR MERGE** pending the project's merge authorization.

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

Local final suite: **18 passed, 1 skipped**. The sole local skip is the Git-history freeze-integrity test because the isolated local execution directory is not a Git checkout.

Hosted final suite: **19 passed, 0 skipped**. The hosted full-history checkout executed the freeze-integrity test successfully.

## 14. Deterministic Outputs

**PASS**

Two successive local regenerations produced identical SHA256 hashes for all committed files in `outputs/`. In hosted run `33635911794`, `make outputs` completed and `git diff --exit-code -- outputs/` passed after the manifest serialization repair.

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

**PASS in the repository diff and hosted CI.**

PR #2 changes 49 files and none is under `stage8/**`. The hosted `verification` job checked out full history and included the freeze-integrity test in its **19 passed** pytest result. No Stage-8 file was modified.

## 19. CI Architecture

Two jobs are defined:
- `verification`: Python setup, dependency install, freeze/theory tests, output regeneration, generated-output diff check;
- `manuscript-build`: minimal LaTeX install and scaffold compilation.

The workflow uses official `actions/checkout@v7` and `actions/setup-python@v7`.

## 20. CI Result

**PASS — HOSTED CI VERIFIED**

Final hosted workflow run: `33635911794`  
Head SHA: `8c39cc32866eb8212bf804253a2ab0ff74012af3`  
Conclusion: **success**

Jobs:

- `verification`: job `100266613809`, runner `1000007174`, label `ubuntu-latest` — **success**
- `manuscript-build`: job `100266614130`, runner `1000007175`, label `ubuntu-latest` — **success**

The `verification` job executed checkout, Python 3.13.5 setup, pinned dependency installation, symbolic and welfare checks, pytest (**19 passed**), 10,000-draw numerical regression, deterministic output regeneration, and committed-output diff validation. The `manuscript-build` job executed LaTeX tooling installation and compiled the one-page scaffold successfully.

Historical runs `33173228843` and `33173509100` failed before runner assignment with `runner_id: 0`, empty runner names, and zero steps. On rerun attempt 3 of `33173509100`, hosted runners were assigned and the only failure was the genuine generated-manifest Unicode diff, which was fixed in `314ce17690c0264db5607212b97b2cd099e1b8b7`.

The runner-allocation failure is classified as a transient GitHub-hosted Actions scheduling/infrastructure issue. The same private repository, workflow, `ubuntu-latest` label, and read-only workflow permissions subsequently received hosted runners and passed; this is inconsistent with a persistent repository disablement, invalid label, unsupported image, or repository-code failure. GitHub's official incident history records Actions job-start and PR-triggered Actions disruptions during the same period.

## 21. Clean-Build Result

**PASS locally.**

`make all` succeeded from a clean-output rebuild, including symbolic/numerical verification, deterministic output generation, and LaTeX compilation.

## 22. Verification Matrix

**COMPLETE — all local and hosted CI gates pass.**

The matrix below records the analytical, numerical, deterministic-output, freeze-integrity, bibliography, and manuscript-build checks. Hosted CI execution is now verified by run `33635911794`.

## 23. Stage 9 Kill Tests

| Kill test | Result |
|---|---|
| 1 Freeze Integrity | PASS — repository diff and hosted full-history pytest |
| 2 Symbolic Reproduction | PASS |
| 3 Welfare Reproduction | PASS |
| 4 Condition G | PASS |
| 5 Cross-Route Necessity | PASS |
| 6 Determinism | PASS |
| 7 Numerical Regression | PASS — 10,000 draws; 100 direct optimizations; 5/5 boundaries |
| 8 Fresh/Clean Build | PASS locally; hosted output regeneration and manuscript build PASS |
| 9 Dependency Reproducibility | PASS |
| 10 Manuscript Scaffold | PASS — hosted compilation |
| 11 Bibliographic Integrity | PASS — empty placeholder by design; no fabricated entries |
| 12 CI | PASS — hosted run `33635911794`; both jobs received runners |
| 13 No Theory Drift | PASS |
| 14 Auditability | PASS |

## 24. Theory Drift Audit

**PASS**

No new theorem, mechanism, strategic variable, welfare friction, or substantive assumption was introduced. P3 remains MAIN; P2 supporting; P1 special-case robustness; P4 and the Stage-2 RRC branch remain killed.

## 25. Stage Verdict

**GO — READY FOR MERGE**

## 26. Routing / Status

**REPRODUCIBILITY READY — HOSTED CI VERIFIED.**

PR #2 is open, mergeable, and contains no Stage-8 changes. The final PR diff audit is complete. Leave PR #2 open unless merge authorization is explicit; once merged, the canonical next route is Stage 10 — Manuscript Drafting.

## 27. Stage 10 Contract

Stage 10 may begin only after Stage 9 is upgraded to GO and PR #2 is merged. Stage 10 may write manuscript prose in dependency order but may not change the frozen research question, mechanism, condition (G), theorem, welfare ordering, P4/RRC killed status, or novelty boundary.

# Canonical Stage 9 Handoff Record

Stage 9 verdict: **GO — READY FOR MERGE**

Repository: `ryotamatsuki/information-appropriability-downstream-reallocation`

Canonical theory freeze SHA: `ef588465430f618b56cf84445681752702c161e1`

Stage 8 theory freeze integrity: **PASS**

PR #2 changed files: **49**

Stage 8 paths changed: **0**

Final Stage 9 branch HEAD: `8c39cc32866eb8212bf804253a2ab0ff74012af3`

Stage 9 base implementation commit: `c11a3628aa28515a3462f35c218a8bf2339cad5a`

Stage 9 CI-recovery implementation commit: `314ce17690c0264db5607212b97b2cd099e1b8b7`

Hosted CI final run: `33635911794`

Hosted `verification`: **PASS** — job `100266613809`, runner `1000007174`, 19 passed, 0 skipped

Hosted `manuscript-build`: **PASS** — job `100266614130`, runner `1000007175`, LaTeX scaffold compiled

Numerical verification: **PASS** — 10,000 admissible draws; 0 demand, effort-positivity, ordering, and widening-wedge failures

Direct optimization: **PASS** — 100 cases; maximum absolute error `1.18792918258e-06 < 2e-06`

Boundary checks: **PASS — 5/5**

Deterministic generated outputs: **PASS**

Committed-output diff consistency: **PASS**

Bibliography integrity: **PASS** — empty placeholder intentionally retained pending verified import

Runner allocation: **PASS** — both hosted jobs assigned `ubuntu-latest` runners and executed steps

Historical runner blocker: **RESOLVED** — transient GitHub-hosted Actions scheduling/infrastructure failure

Theory changes introduced: **NONE**

Theory rollback required: **NO**

P1 status: **ROBUSTNESS / SPECIAL CASE ONLY**

P4 status: **KILLED**

Stage 9 PR: **#2 — OPEN / MERGEABLE / READY FOR MERGE**

What Stage 10 may change: manuscript prose, exposition, equation numbering, section integration, verified bibliography integration.

What Stage 10 may NOT change: frozen theory, players, timing, information structure, condition (G), theorem results, welfare ordering, killed claims, or novelty boundary.

Next route: **MERGE PR #2 ONLY WITH EXPLICIT AUTHORIZATION → STAGE 10 — MANUSCRIPT DRAFTING**
