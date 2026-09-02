# Information Appropriability under Downstream Reallocation

Theory-research project on how downstream reallocation changes incentives to produce noncontractible information that improves an upstream product across downstream routes.

## Project status

- Canonical theory: **THEORY FROZEN**
- Freeze SHA: `ef588465430f618b56cf84445681752702c161e1`
- Current workflow stage: **Stage 9 — Repository / Reproducibility Setup**
- Stage 9 status: **GO — READY FOR MERGE**; hosted CI run `33634955842` passed both required jobs; PR #2 remains open pending merge.

## Canonical mechanism

**Information Appropriability under Downstream Reallocation**

The frozen contribution candidate is a reallocation-induced information-incentive divergence: private information effort at the information-producing downstream node can fall while coordinated/socially desired information effort rises because reusable information becomes more valuable through an expanding alternative route.

The project does not claim that downstream feedback, user innovation, information externalities, retailer information, or endogenous channel structure are themselves new.

## Reproduction quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make all
```

See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for the full contract.

## Repository map

- `stage8/` — immutable canonical theory-freeze artifacts
- `code/` — symbolic and deterministic numerical verification
- `tests/` — regression and freeze-integrity checks
- `outputs/` — committed deterministic generated verification outputs
- `manuscript/` — LaTeX scaffold only; Stage 9 contains no manuscript prose
- `references/` — bibliography integrity placeholder pending verified import
- `stage9/` — reproducibility report, manifest, build log, verification matrix
- `docs/` — provenance, freeze attestation, reproducibility and theory-change policy

## Theory-change warning

Stage-8 theory is immutable at Stage 9. If implementation exposes a substantive theory inconsistency, do not repair the Stage-8 model in this branch. Follow [`docs/THEORY_CHANGE_POLICY.md`](docs/THEORY_CHANGE_POLICY.md) and roll back to the earliest affected stage.

## Provenance

The research seed is 「家電量販店と系列店 ～家電の流通についての分析～」, written by Ryota Matsuki for a university seminar competition in his third undergraduate year. It was **not** a graduation thesis. See [`docs/RESEARCH_PROVENANCE.md`](docs/RESEARCH_PROVENANCE.md).
