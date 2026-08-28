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

## GitHub Actions

Initial run: `33173228843`.

Jobs:
- verification — failure before runner assignment
- manuscript-build — failure before runner assignment

For both jobs GitHub reports:
- `runner_id: 0`
- empty `runner_name`
- `steps: []`

No workflow step ran, and no job log was generated. This is classified as an infrastructure / runner-allocation blocker, not a repository-code or theory-verification failure.
