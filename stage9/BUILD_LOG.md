# Stage 9 Build Log

## Local validation environment

- Python: 3.13.5
- SymPy: 1.14.0
- pytest: 9.0.2
- latexmk: 4.86
- GNU Make: available

## Pre-PR local validation

`make verify`: PASS, with the freeze-integrity test skipped only because the isolated working directory is not a Git checkout. The same test is mandatory and non-skipped in GitHub Actions.

Pytest result after final symbolic identities: **18 passed, 1 skipped locally** (the one skip is freeze-integrity checkout-only).

Deterministic numerical regression:
- 10,000 admissible draws
- zero demand failures
- zero effort-positivity failures
- zero effort-ordering failures
- zero widening-wedge failures
- 100 direct-optimization cross-checks
- maximum absolute direct-vs-closed-form error: approximately `1.188e-06`
- 5/5 boundary smoke tests passed

`make outputs`: PASS.

`make manuscript`: PASS; generated one-page scaffold PDF in `manuscript/build/`.

`make all`: PASS in the isolated clean-output rebuild.

## CI

Pending PR creation and clean GitHub-hosted checkout validation.
