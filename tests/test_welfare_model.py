import sympy as sp
from symbolic.welfare_model import derive_welfare_model,frozen_formulas
def sym(expr,name): return next(s for s in expr.free_symbols if s.name==name)
def test_demand_derivation():
    r=derive_welfare_model(); d=r['demand']; e=sym(d,'e'); a=sym(d,'a'); p=sym(d,'p'); beta=sym(d,'beta'); assert sp.simplify(d-(a+beta*e-p))==0
def test_effort_formulas_match_freeze():
    r=derive_welfare_model(); f=frozen_formulas()
    for key in ('eP','eC','eW'): assert sp.simplify(r[key]-f[key])==0
def test_social_concavity_expression():
    r=derive_welfare_model(); expr=r['social_second_derivative']; beta=sym(expr,'beta'); k=sym(expr,'k'); assert sp.simplify(expr-(beta**2-k))==0
def test_eC_minus_eP_positive_at_admissible_point():
    r=derive_welfare_model(); expr=r['gap_eC_eP']; values={'a':5,'p':3,'c_S':2,'c_R':1,'m':sp.Rational(2,5),'beta':1,'k':3,'h':sp.Rational(1,2)}; sub={s:values[s.name] for s in expr.free_symbols if s.name in values}; assert float(sp.N(expr.subs(sub)))>0
def test_widening_eC_eP_identity():
    r=derive_welfare_model(); expr=r['d_gap_eC_eP_deta']; hp=sym(expr,'h_prime'); cS=sym(expr,'c_S'); cR=sym(expr,'c_R'); m=sym(expr,'m'); beta=sym(expr,'beta'); k=sym(expr,'k'); assert sp.simplify(expr-beta*hp*((cS-cR)+m)/k)==0
def test_widening_eW_eP_identity():
    r=derive_welfare_model(); expr=r['d_gap_eW_eP_deta']; hp=sym(expr,'h_prime'); cS=sym(expr,'c_S'); cR=sym(expr,'c_R'); m=sym(expr,'m'); beta=sym(expr,'beta'); k=sym(expr,'k'); assert sp.simplify(expr-beta*hp*((cS-cR)/(k-beta**2)+m/k))==0
def test_eW_minus_eC_positive_decomposition_identity():
    r=derive_welfare_model(); assert sp.simplify(r['gap_eW_eC']-r['gap_eW_eC_positive_form'])==0
