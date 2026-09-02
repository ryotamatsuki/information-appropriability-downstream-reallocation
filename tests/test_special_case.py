import sympy as sp
from symbolic.special_case import STATUS,derive_special_case
def test_p1_threshold_regression_only():
    r=derive_special_case(); assert sp.simplify(r['eta_R']-r['expected_eta_R'])==0; assert STATUS=='ROBUSTNESS / SPECIAL CASE ONLY'
