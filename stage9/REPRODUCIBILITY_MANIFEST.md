# Stage 9 Reproducibility Manifest

- Canonical freeze SHA: `ef588465430f618b56cf84445681752702c161e1`
- Stage 9 branch: `stage9/reproducibility-setup`
- Python: `3.13.5`
- SymPy: `1.14.0`
- pytest: `9.0.2`
- Deterministic seed: `20260828`
- Numerical draws: `10000`
- Direct-optimization cross-check cases: `100`
- Symbolic scripts: `code/symbolic/general_model.py`, `welfare_model.py`, `special_case.py`
- Numerical scripts: `code/numerical/parameter_checks.py`, `regression_checks.py`
- CI workflow: `.github/workflows/ci.yml`
- Build commands: `make verify`, `make outputs`, `make manuscript`, `make all`, `make clean`
- Output files: `symbolic_results.txt`, `welfare_results.txt`, `numerical_checks.csv`, `output_manifest.json`
- Manuscript build status: `LOCAL PASS / CI PENDING`
- CI run ID: `PENDING`
- Stage 9 implementation commit SHA: `PENDING`
- Stage 9 PR: `PENDING`
