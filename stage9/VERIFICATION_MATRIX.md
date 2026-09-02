# Stage 9 Verification Matrix

| Frozen result / gate | Analytical or repository source | Script / workflow | Test or evidence | Output / record | Status |
|---|---|---|---|---|---|
| private FOC | Stage 8 general-model objective | `code/symbolic/general_model.py` | hosted `make verify` and generated symbolic output | `outputs/symbolic_results.txt` | PASS |
| coordinated FOC | Stage 8 general-model objective | `code/symbolic/general_model.py` | hosted `make verify` and generated symbolic output | `outputs/symbolic_results.txt` | PASS |
| private IFT derivative | Stage 8 theorem/lemma | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| coordinated IFT derivative | Stage 8 theorem/lemma | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| condition (G) | Stage 8 Theorem 1 | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| cross-route necessity | Stage 8 Corollary 1 | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| one-for-one reduction | Stage 8 Corollary 2 | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| demand derivation | `stage8/WELFARE_FREEZE.md` | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| `e^P` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| `e^C` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| `e^W` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| effort ordering `e^P < e^C < e^W` | Stage 8 welfare restrictions | symbolic + numerical scripts | welfare tests + 10,000-draw regression | welfare/numerical outputs | PASS |
| widening `e^C-e^P` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| widening `e^W-e^P` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| P1 threshold | Stage 4 / Stage 8 robustness ledger | `code/symbolic/special_case.py` | `tests/test_special_case.py` | script check | PASS — special case only |
| 10,000 admissible draws | frozen benchmark restrictions | `code/numerical/regression_checks.py` | hosted `--check --draws 10000` | `outputs/numerical_checks.csv` | PASS |
| direct objective optimization | frozen benchmark objectives | `code/numerical/regression_checks.py` | 100 cases; tolerance `2e-06` | `outputs/numerical_checks.csv` | PASS |
| boundary checks | frozen admissible boundary smoke inputs | `code/numerical/parameter_checks.py` | 5/5 | `outputs/numerical_checks.csv` | PASS |
| deterministic output repeat | Stage 9 output contract | `code/generate_outputs.py` | two local regenerations; hosted regeneration | output manifest | PASS |
| clean output regeneration | Stage 9 output contract | `.github/workflows/ci.yml` | `make outputs` + `git diff --exit-code -- outputs/` | committed outputs | PASS |
| clean build | Stage 9 build contract | `Makefile` | local `make all`; hosted fresh checkout and separate jobs | build log | PASS |
| bibliography integrity | Stage 9 reference policy | `references/references.bib` | empty placeholder intentionally retained; no fabricated metadata; scaffold compiles | `references/README.md` | PASS |
| Stage-8 freeze integrity | canonical freeze SHA | `tests/test_freeze_integrity.py` | hosted full-history pytest + PR diff audit | PR #2 | PASS |
| hosted CI runner execution | Stage 9 infrastructure contract | `.github/workflows/ci.yml` | run `33634955842`; both jobs assigned `ubuntu-latest` runners | GitHub Actions logs | PASS |
| manuscript scaffold compilation | Stage 9 manuscript scaffold | `manuscript/main.tex` | hosted `make manuscript`; one-page PDF | build log | PASS |
| no theory drift | Stage 8 freeze policy | PR diff + Stage 9 audit | no `stage8/**` changes; no model/theorem changes | Stage 9 report | PASS |
