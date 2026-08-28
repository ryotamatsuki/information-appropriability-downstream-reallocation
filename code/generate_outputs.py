"""Generate all committed deterministic Stage 9 outputs and their manifest."""
from __future__ import annotations
import hashlib,json,platform
from pathlib import Path
import sympy
from common.parameters import NUMERICAL_DRAWS,SEED
from symbolic.general_model import check_identities as check_general,render_results as render_general
from symbolic.welfare_model import check_identities as check_welfare,render_results as render_welfare
from numerical.regression_checks import assert_pass,run_checks,write_csv
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"outputs"
def sha256(path):
    h=hashlib.sha256(); h.update(Path(path).read_bytes()); return h.hexdigest()
def main():
    OUT.mkdir(exist_ok=True); check_general(); check_welfare(); symbolic=OUT/"symbolic_results.txt"; welfare=OUT/"welfare_results.txt"; numerical=OUT/"numerical_checks.csv"; symbolic.write_text(render_general(),encoding="utf-8"); welfare.write_text(render_welfare(),encoding="utf-8"); result=run_checks(NUMERICAL_DRAWS); assert_pass(result); write_csv(numerical,result)
    manifest={"notice":"GENERATED — DO NOT EDIT MANUALLY","python_version":platform.python_version(),"sympy_version":sympy.__version__,"seed":SEED,"files":{"numerical_checks.csv":{"generator":"code/generate_outputs.py","sha256":sha256(numerical)},"symbolic_results.txt":{"generator":"code/generate_outputs.py","sha256":sha256(symbolic)},"welfare_results.txt":{"generator":"code/generate_outputs.py","sha256":sha256(welfare)}}}; (OUT/"output_manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
if __name__=="__main__": main()
