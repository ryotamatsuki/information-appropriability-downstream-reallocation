# Stage 9 Verification Matrix

| Frozen result | Analytical source | Script | Test | Output | Status |
|---|---|---|---|---|---|
| private IFT derivative | Stage 8 Theorem/Lemma | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| condition (G) | Stage 8 Theorem 1 | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| cross-route necessity | Stage 8 Corollary 1 | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| one-for-one reduction | Stage 8 Corollary 2 | `code/symbolic/general_model.py` | `tests/test_general_model.py` | `outputs/symbolic_results.txt` | PASS |
| demand derivation | `stage8/WELFARE_FREEZE.md` | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| `e^P` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| `e^C` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| `e^W` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| effort ordering | Stage 8 welfare benchmark | symbolic + numerical scripts | welfare/numerical tests | welfare + numerical outputs | PASS |
| widening `e^C-e^P` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| widening `e^W-e^P` | Stage 8 welfare benchmark | `code/symbolic/welfare_model.py` | `tests/test_welfare_model.py` | `outputs/welfare_results.txt` | PASS |
| P1 threshold | Stage 4 / Stage 8 robustness ledger | `code/symbolic/special_case.py` | `tests/test_special_case.py` | script check | PASS — SPECIAL CASE ONLY |
| 10k admissible regression | frozen benchmark restrictions | `code/numerical/regression_checks.py` | `tests/test_numerical_checks.py` | `outputs/numerical_checks.csv` | PASS |
| direct optimization | frozen benchmark objectives | `code/numerical/regression_checks.py` | `tests/test_numerical_checks.py` | `outputs/numerical_checks.csv` | PASS |
| Stage-8 immutability | freeze SHA | Git diff in test | `tests/test_freeze_integrity.py` | CI log | PENDING CI |
