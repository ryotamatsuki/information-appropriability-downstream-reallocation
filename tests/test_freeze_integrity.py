from pathlib import Path
import subprocess,pytest
from common.parameters import FREEZE_SHA
ROOT=Path(__file__).resolve().parents[1]
def _run(*args): return subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
def test_stage8_is_unchanged_from_freeze_commit():
    if not (ROOT/'.git').exists(): pytest.skip('freeze-integrity comparison requires an actual Git checkout; CI performs it')
    exists=_run('git','cat-file','-e',f'{FREEZE_SHA}^{{commit}}'); assert exists.returncode==0,exists.stderr
    diff=_run('git','diff','--exit-code',FREEZE_SHA,'--','stage8'); assert diff.returncode==0,diff.stdout+diff.stderr
