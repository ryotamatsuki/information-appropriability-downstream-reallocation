"""Regression verification for P1, retained only as a Stage 4 special case."""
from __future__ import annotations
import argparse
import sympy as sp
STATUS="ROBUSTNESS / SPECIAL CASE ONLY"

def derive_special_case() -> dict[str, sp.Expr]:
    A,b,delta,m,beta,k,eta=sp.symbols("A b delta m beta k eta", positive=True)
    L=m*beta**2/k; delta_pi=(1-eta)*(L*(b+delta*eta)-A*delta); factor=sp.factor(delta_pi/(1-eta)); eta_R=sp.factor(sp.solve(sp.Eq(factor,0),eta)[0]); expected=sp.factor((A*delta/L-b)/delta)
    return {"L":L,"delta_pi":sp.factor(delta_pi),"interior_factor":factor,"eta_R":eta_R,"expected_eta_R":expected}

def check_identities() -> None:
    r=derive_special_case(); assert sp.simplify(r["eta_R"]-r["expected_eta_R"])==0

def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); args=parser.parse_args(); check_identities()
    if not args.check:
        r=derive_special_case(); print("GENERATED — DO NOT EDIT MANUALLY\nSTATUS = "+STATUS+"\nL: "+sp.sstr(r['L'])+"\nDeltaPi_M: "+sp.sstr(r['delta_pi'])+"\neta_R: "+sp.sstr(r['eta_R'])+"\nP1 is not the main contribution and is not promoted by Stage 9.")
if __name__ == "__main__": main()
