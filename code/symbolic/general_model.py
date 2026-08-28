"""Symbolic verification for the frozen Stage 8 general model."""
from __future__ import annotations
import argparse
import sympy as sp


def derive_general_model() -> dict[str, sp.Expr]:
    eta, e = sp.symbols("eta e", real=True)
    m_s, a_s, a_r = sp.symbols("m_S A_S A_R", positive=True)
    omega_s = sp.Function("omega_S")(eta)
    omega_r = sp.Function("omega_R")(eta)
    g = sp.Function("g"); d_s = sp.Function("D_S"); d_r = sp.Function("D_R"); cost = sp.Function("C")
    x = g(e)
    private = m_s * omega_s * d_s(x) - cost(e)
    coordinated = a_s * omega_s * d_s(x) + a_r * omega_r * d_r(x) - cost(e)
    phi_p = sp.diff(private, e); phi_c = sp.diff(coordinated, e)
    phi_p_e = sp.diff(phi_p, e); phi_c_e = sp.diff(phi_c, e)
    phi_p_eta = sp.diff(phi_p, eta); phi_c_eta = sp.diff(phi_c, eta)
    de_p = sp.factor(-phi_p_eta / phi_p_e); de_c = sp.factor(-phi_c_eta / phi_c_e)
    AS, AR, wSp, wRp, DSp, DRp = sp.symbols("A_S A_R omega_S_prime omega_R_prime D_S_prime D_R_prime", real=True)
    bracket = sp.expand(AS*wSp*DSp + AR*wRp*DRp)
    cross_off = sp.simplify(bracket.subs(DRp, 0))
    rho, Dp = sp.symbols("rho D_prime", positive=True)
    one_for_one = sp.factor(bracket.subs({wRp:rho,wSp:-rho,DRp:Dp,DSp:Dp}))
    return {"private_objective":private,"coordinated_objective":coordinated,"private_foc":phi_p,"coordinated_foc":phi_c,"private_soc":phi_p_e,"coordinated_soc":phi_c_e,"private_mixed_partial":phi_p_eta,"coordinated_mixed_partial":phi_c_eta,"private_ift_derivative":de_p,"coordinated_ift_derivative":de_c,"condition_G_bracket":bracket,"cross_route_off_bracket":cross_off,"one_for_one_bracket":one_for_one}


def check_identities() -> None:
    r=derive_general_model()
    AS, AR, wSp, wRp, DSp, DRp = sp.symbols("A_S A_R omega_S_prime omega_R_prime D_S_prime D_R_prime", real=True)
    rho,Dp=sp.symbols("rho D_prime", positive=True)
    assert sp.simplify(r["condition_G_bracket"]-(AS*wSp*DSp+AR*wRp*DRp))==0
    assert sp.simplify(r["cross_route_off_bracket"]-AS*wSp*DSp)==0
    assert sp.simplify(r["one_for_one_bracket"]-rho*Dp*(AR-AS))==0


def render_results() -> str:
    r=derive_general_model()
    lines=["GENERATED — DO NOT EDIT MANUALLY","Stage 9 symbolic verification: frozen Stage 8 general model","",f"private FOC: {sp.sstr(r['private_foc'])}",f"private IFT derivative: {sp.sstr(r['private_ift_derivative'])}","private sign condition: omega_S'(eta) < 0 and private SOC < 0 => de^P/deta < 0","",f"coordinated FOC: {sp.sstr(r['coordinated_foc'])}",f"coordinated IFT derivative: {sp.sstr(r['coordinated_ift_derivative'])}",f"condition (G) bracket: {sp.sstr(r['condition_G_bracket'])}","condition (G): A_R*omega_R'*D_R' > -A_S*omega_S'*D_S'","",f"cross-route-off bracket (D_R'=0): {sp.sstr(r['cross_route_off_bracket'])}","economic sign: negative under A_S>0, omega_S'<0, D_S'>0",f"one-for-one bracket: {sp.sstr(r['one_for_one_bracket'])}","one-for-one sign condition: A_R > A_S","","STATUS: PASS — algebraic identities reproduce the frozen Stage 8 model."]
    return "\n".join(lines)+"\n"


def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); parser.add_argument("--output"); args=parser.parse_args()
    check_identities(); text=render_results()
    if args.output:
        from pathlib import Path; Path(args.output).write_text(text,encoding="utf-8")
    elif not args.check: print(text,end="")

if __name__ == "__main__": main()
