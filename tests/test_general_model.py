import sympy as sp
from symbolic.general_model import derive_general_model

def test_condition_g_bracket():
    r=derive_general_model(); AS,AR,wSp,wRp,DSp,DRp=sp.symbols('A_S A_R omega_S_prime omega_R_prime D_S_prime D_R_prime',real=True); assert sp.simplify(r['condition_G_bracket']-(AS*wSp*DSp+AR*wRp*DRp))==0
def test_cross_route_necessity():
    r=derive_general_model(); AS,wSp,DSp=sp.symbols('A_S omega_S_prime D_S_prime',real=True); assert sp.simplify(r['cross_route_off_bracket']-AS*wSp*DSp)==0
def test_one_for_one_reduction():
    r=derive_general_model(); AS,AR=sp.symbols('A_S A_R',real=True); rho,Dp=sp.symbols('rho D_prime',positive=True); assert sp.simplify(r['one_for_one_bracket']-rho*Dp*(AR-AS))==0
def test_private_ift_has_negative_mixed_partial_over_soc_form():
    r=derive_general_model(); assert sp.simplify(r['private_ift_derivative']-sp.factor(-r['private_mixed_partial']/r['private_soc']))==0
def test_coordinated_ift_has_negative_mixed_partial_over_soc_form():
    r=derive_general_model(); assert sp.simplify(r['coordinated_ift_derivative']-sp.factor(-r['coordinated_mixed_partial']/r['coordinated_soc']))==0
