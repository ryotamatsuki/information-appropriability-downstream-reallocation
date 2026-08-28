# Stage 9 Engineering Decision Log

Theory decisions are not made here.

- Environment: plain `venv`/`pip` contract with exact direct dependency pins; no Docker/Conda/Poetry/Nix stack.
- Python: 3.13.5, matching the local validation environment and CI contract.
- Symbolic engine: SymPy 1.14.0.
- Tests: pytest 9.0.2.
- Numerical checks: Python standard library only; no NumPy/SciPy dependency required.
- Numerical seed: `20260828`.
- Numerical regression: 10,000 admissible draws; dependency-free golden-section direct optimization on a deterministic subset.
- LaTeX: standard `article` scaffold compiled by `latexmk`; no journal class/template.
- Bibliography: empty verified ledger placeholder; no metadata reconstructed from memory.
- CI: separate verification and manuscript-build jobs.
- Official GitHub actions: `actions/checkout@v7` and `actions/setup-python@v7`.
- Freeze integrity: CI compares `stage8/**` against canonical freeze SHA.
