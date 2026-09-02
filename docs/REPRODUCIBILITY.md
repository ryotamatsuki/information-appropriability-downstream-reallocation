# Reproducibility

Canonical theory freeze SHA: `ef588465430f618b56cf84445681752702c161e1`.

## Requirements

- Python 3.13.5
- GNU Make
- `latexmk` plus a standard LaTeX installation containing `article`, `amsmath`, `amssymb`, and `amsthm`
- Python packages pinned in `requirements.txt`

## Fresh setup

```bash
git clone <repository-url>
cd information-appropriability-downstream-reallocation
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Verify

```bash
make verify
```

This runs symbolic identity checks, the deterministic 10,000-draw numerical regression, pytest, and the Stage-8 freeze-integrity guard when executed inside an actual Git checkout.

## Regenerate outputs

```bash
make outputs
```

Committed generated outputs live in `outputs/`. CI regenerates them and fails if `git diff --exit-code -- outputs/` is nonzero.

## Compile manuscript scaffold

```bash
make manuscript
```

Stage 9 contains headings/placeholders only; no manuscript prose is authorized yet.

## Clean build

```bash
make all
```

`make all` removes generated artifacts, reruns verification, regenerates outputs, and compiles the LaTeX scaffold.

## Expected outputs

- `outputs/symbolic_results.txt`
- `outputs/welfare_results.txt`
- `outputs/numerical_checks.csv`
- `outputs/output_manifest.json`
- `manuscript/build/main.pdf` (build artifact; not committed)

## Troubleshooting

A dependency/build/path problem is a Stage-9 infrastructure issue. A mismatch between code-derived formulas and the frozen Stage-8 theory is a **theory verification failure** and must not be repaired by silently changing the theory; follow the rollback policy.

## Hosted CI validation

Final hosted workflow run: `33634955842` on branch `stage9/reproducibility-setup`, head `314ce17690c0264db5607212b97b2cd099e1b8b7`.

- `verification`: **PASS** — hosted runner; pytest `19 passed, 0 skipped`; symbolic/welfare/numerical checks; output regeneration; committed-output diff
- `manuscript-build`: **PASS** — hosted runner; LaTeX tooling installation and scaffold compilation
- Stage-8 freeze integrity: **PASS** — full-history checkout and PR diff audit
- Stage 9 verdict: **GO — READY FOR MERGE**
