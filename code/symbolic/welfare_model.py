"""Symbolic derivation of the frozen Stage 8 welfare benchmark."""
from __future__ import annotations
import argparse
import sympy as sp


def derive_welfare_model() -> dict[str, sp.Expr]:
    q,e,h,hp=sp.symbols("q e h h_prime", real=True)
    a,p,c_s,c_r,m,beta,k=sp.symbols("a p c_S c_R m beta k", positive=True)
    x=beta*e; utility=(a+x)*q-q**2/2-p*q
    utility_foc=sp.diff(utility,q); d=sp.simplify(sp.solve(sp.Eq(utility_foc,0),q)[0])
    private_obj=m*(1-h)*d-k*e**2/2
    margin=(p-c_s)*(1-h)+(p-c_r)*h
    coordinated_obj=margin*d-k*e**2/2
    consumer_surplus=sp.simplify(d**2/2)
    social_obj=consumer_surplus+margin*d-k*e**2/2
    pf=sp.diff(private_obj,e); cf=sp.diff(coordinated_obj,e); wf=sp.diff(social_obj,e)
    e_p=sp.simplify(sp.solve(sp.Eq(pf,0),e)[0]); e_c=sp.simplify(sp.solve(sp.Eq(cf,0),e)[0]); e_w=sp.factor(sp.solve(sp.Eq(wf,0),e)[0])
    gap_cp=sp.factor(e_c-e_p); gap_wc=sp.factor(e_w-e_c); gap_wp=sp.factor(e_w-e_p)
    positive_gap_wc=sp.factor(beta*(k*(a-p)+beta**2*((p-c_s)*(1-h)+(p-c_r)*h))/(k*(k-beta**2)))
    d_cp=sp.factor(sp.diff(gap_cp,h)*hp); d_wp=sp.factor(sp.diff(gap_wp,h)*hp)
    return {"utility":utility,"utility_foc":utility_foc,"demand":d,"private_objective":private_obj,"coordinated_objective":coordinated_obj,"social_objective":social_obj,"consumer_surplus":consumer_surplus,"private_foc":pf,"coordinated_foc":cf,"social_foc":wf,"eP":e_p,"eC":e_c,"eW":e_w,"gap_eC_eP":gap_cp,"gap_eW_eC":gap_wc,"gap_eW_eC_positive_form":positive_gap_wc,"gap_eW_eP":gap_wp,"d_gap_eC_eP_deta":d_cp,"d_gap_eW_eP_deta":d_wp,"social_second_derivative":sp.diff(social_obj,e,2)}


def frozen_formulas() -> dict[str, sp.Expr]:
    h=sp.symbols("h", real=True); a,p,c_s,c_r,m,beta,k=sp.symbols("a p c_S c_R m beta k", positive=True)
    return {"eP":m*beta*(1-h)/k,"eC":beta*((p-c_s)*(1-h)+(p-c_r)*h)/k,"eW":beta*(a-c_s*(1-h)-c_r*h)/(k-beta**2)}


def check_identities() -> None:
    r=derive_welfare_model(); f=frozen_formulas()
    for key in ("eP","eC","eW"): assert sp.simplify(r[key]-f[key])==0
    h,hp=sp.symbols("h h_prime", real=True); a,p,c_s,c_r,m,beta,k=sp.symbols("a p c_S c_R m beta k", positive=True)
    assert sp.simplify(r["d_gap_eC_eP_deta"]-beta*hp*((c_s-c_r)+m)/k)==0
    assert sp.simplify(r["d_gap_eW_eP_deta"]-beta*hp*((c_s-c_r)/(k-beta**2)+m/k))==0
    assert sp.simplify(r["social_second_derivative"]-(beta**2-k))==0
    assert sp.simplify(r["gap_eW_eC"]-r["gap_eW_eC_positive_form"])==0


def render_results() -> str:
    r=derive_welfare_model()
    lines=["GENERATED — DO NOT EDIT MANUALLY","Stage 9 symbolic verification: frozen Stage 8 welfare benchmark","",f"utility FOC: {sp.sstr(r['utility_foc'])}",f"demand: {sp.sstr(r['demand'])}",f"private FOC: {sp.sstr(r['private_foc'])}",f"coordinated FOC: {sp.sstr(r['coordinated_foc'])}",f"social FOC: {sp.sstr(r['social_foc'])}",f"eP: {sp.sstr(r['eP'])}",f"eC: {sp.sstr(r['eC'])}",f"eW: {sp.sstr(r['eW'])}","",f"eC-eP: {sp.sstr(r['gap_eC_eP'])}",f"eW-eC: {sp.sstr(r['gap_eW_eC'])}",f"eW-eC positive decomposition: {sp.sstr(r['gap_eW_eC_positive_form'])}",f"d(eC-eP)/deta: {sp.sstr(r['d_gap_eC_eP_deta'])}",f"d(eW-eP)/deta: {sp.sstr(r['d_gap_eW_eP_deta'])}",f"social objective second derivative: {sp.sstr(r['social_second_derivative'])}","","sign restrictions: a>p>c_S>c_R>=0, 0<m<p-c_S, beta>0, k>beta^2, h'>0","ordering under frozen restrictions: eP < eC < eW","STATUS: PASS — frozen welfare formulas are re-derived from objectives."]
    return "\n".join(lines)+"\n"


def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); parser.add_argument("--output"); args=parser.parse_args()
    check_identities(); text=render_results()
    if args.output:
        from pathlib import Path; Path(args.output).write_text(text,encoding="utf-8")
    elif not args.check: print(text,end="")

if __name__ == "__main__": main()
