# Stage 9 Build Log

## Local validation environment

- Python: 3.13.5
- SymPy: 1.14.0
- pytest: 9.0.2
- latexmk: 4.86
- GNU Make: available

## Local validation

`make verify`: PASS, with the freeze-integrity test skipped only because the isolated working directory is not a Git checkout.

Final pytest result: **18 passed, 1 skipped locally**. The sole skip is the Git-history freeze-integrity test.

Deterministic numerical regression:
- 10,000 admissible draws
- zero demand failures
- zero effort-positivity failures
- zero effort-ordering failures
- zero widening-wedge failures
- 100 direct-optimization cross-checks
- max direct-vs-closed-form error ≈ `1.188e-06` < `2e-06`
- 5/5 boundary smoke tests passed

`make outputs`: PASS.

Two consecutive output regenerations produced identical file hashes: PASS.

`make manuscript`: PASS; one-page Stage-9 scaffold PDF generated locally.

`make all`: PASS in the isolated clean-output rebuild.

## Freeze integrity

PR #2 changed-file audit: PASS. No path under `stage8/**` is changed.

## Hosted GitHub Actions validation

Final hosted workflow run: `33634955842` (head `314ce17690c0264db5607212b97b2cd099e1b8b7`).

- `verification`: **PASS**; job `100263388675`; runner `1000007154`; label `ubuntu-latest`
- `manuscript-build`: **PASS**; job `100263388233`; runner `1000007153`; label `ubuntu-latest`
- Hosted pytest: **19 passed, 0 skipped**
- Hosted numerical command: `regression_checks.py --check --draws 10000` **PASS**
- Hosted output regeneration: **PASS**
- Hosted committed-output diff: **PASS**
- Hosted LaTeX scaffold compilation: **PASS**, one-page PDF generated
- Hosted full-history freeze-integrity check: **PASS**
- All workflow steps executed; neither job used `runner_id: 0`

## Runner-allocation diagnosis and repair

Runs `33173228843` and `33173509100` initially failed before runner assignment with zero steps. Rerun attempt 3 of `33173509100` obtained hosted runners and exposed one implementation issue: the generated manifest escaped the Unicode em dash while the committed output retained the literal character. Commit `314ce17690c0264db5607212b97b2cd099e1b8b7` added `ensure_ascii=False` to the generator. The subsequent final run passed.

The original runner failure is recorded as a transient GitHub-hosted Actions scheduling/infrastructure issue, not a theory or repository-code failure. No workflow verification was weakened.

## Final local/hosted status

- Theory changes: **NONE**
- Stage-8 files changed: **0**
- Stage 9 verdict: **GO — READY FOR MERGE**
- PR #2: **OPEN / MERGEABLE / READY FOR MERGE**
