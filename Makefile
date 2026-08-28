PYTHON ?= python
FREEZE_SHA := ef588465430f618b56cf84445681752702c161e1

.PHONY: verify outputs manuscript all clean

verify:
	PYTHONPATH=code $(PYTHON) code/symbolic/general_model.py --check
	PYTHONPATH=code $(PYTHON) code/symbolic/welfare_model.py --check
	PYTHONPATH=code $(PYTHON) code/symbolic/special_case.py --check
	PYTHONPATH=code $(PYTHON) code/numerical/regression_checks.py --check --draws 10000
	$(PYTHON) -m pytest -q

outputs:
	PYTHONPATH=code $(PYTHON) code/generate_outputs.py

manuscript:
	cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex

all: clean verify outputs manuscript

clean:
	rm -f outputs/symbolic_results.txt outputs/welfare_results.txt outputs/numerical_checks.csv outputs/output_manifest.json
	rm -rf manuscript/build .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
