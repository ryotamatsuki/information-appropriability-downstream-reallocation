"""Deterministic numerical regression checks for frozen Stage 8 formulas."""
from __future__ import annotations
import argparse,csv,math
from pathlib import Path
from common.parameters import DIRECT_OPT_CASES,NUMERICAL_DRAWS,OPT_TOL,SEED
from numerical.parameter_checks import Params,boundary_cases,generate_admissible

def efforts(x:Params)->tuple[float,float,float]:
    return (x.m*x.beta*(1-x.h)/x.k, x.beta*((x.p-x.c_s)*(1-x.h)+(x.p-x.c_r)*x.h)/x.k, x.beta*(x.a-x.c_s*(1-x.h)-x.c_r*x.h)/(x.k-x.beta*x.beta))
def gaps_derivatives(x:Params)->tuple[float,float]:
    return (x.beta*x.h_prime*((x.c_s-x.c_r)+x.m)/x.k, x.beta*x.h_prime*((x.c_s-x.c_r)/(x.k-x.beta*x.beta)+x.m/x.k))
def demand(x:Params,e:float)->float: return x.a+x.beta*e-x.p
def private_obj(x:Params,e:float)->float: return x.m*(1-x.h)*demand(x,e)-x.k*e*e/2
def coordinated_obj(x:Params,e:float)->float:
    margin=(x.p-x.c_s)*(1-x.h)+(x.p-x.c_r)*x.h; return margin*demand(x,e)-x.k*e*e/2
def social_obj(x:Params,e:float)->float:
    d=demand(x,e); margin=(x.p-x.c_s)*(1-x.h)+(x.p-x.c_r)*x.h; return d*d/2+margin*d-x.k*e*e/2

def golden_max(f,lo:float,hi:float,iterations:int=100)->float:
    gr=(math.sqrt(5)-1)/2; c=hi-gr*(hi-lo); d=lo+gr*(hi-lo); fc,fd=f(c),f(d)
    for _ in range(iterations):
        if fc>fd: hi,d,fd=d,c,fc; c=hi-gr*(hi-lo); fc=f(c)
        else: lo,c,fc=c,d,fd; d=lo+gr*(hi-lo); fd=f(d)
    return (lo+hi)/2

def direct_opt_errors(x:Params)->tuple[float,float,float]:
    closed=efforts(x); hi=max(1.0,2.5*max(closed)); funcs=(private_obj,coordinated_obj,social_obj); direct=tuple(golden_max(lambda e,fn=fn:fn(x,e),0.0,hi) for fn in funcs); return tuple(abs(a-b) for a,b in zip(closed,direct))
def run_checks(draws:int=NUMERICAL_DRAWS)->dict[str,float|int]:
    params=generate_admissible(draws,SEED); demand_fail=effort_fail=ordering_fail=wedge_fail=0
    for x in params:
        ep,ec,ew=efforts(x)
        demand_fail += int(min(demand(x,ep),demand(x,ec),demand(x,ew))<=0); effort_fail += int(min(ep,ec,ew)<=0); ordering_fail += int(not(ep<ec<ew)); dcp,dwp=gaps_derivatives(x); wedge_fail += int(not(dcp>0 and dwp>0))
    max_err=0.0
    for x in params[:DIRECT_OPT_CASES]: max_err=max(max_err,*direct_opt_errors(x))
    boundary_ok=0
    for name,x in boundary_cases().items():
        ep,ec,ew=efforts(x)
        if name=="beta_small": ok=max(ep,ec,ew)<1e-6
        elif name=="h_near_zero": ok=ep>0 and ec>ep and ew>ec
        elif name=="h_near_one": ok=ep<1e-7 and ec>0 and ew>ec
        elif name=="cost_gap_small": dcp,dwp=gaps_derivatives(x); ok=dcp>0 and dwp>0
        else: ok=ew>ec>ep and math.isfinite(ew)
        boundary_ok+=int(ok)
    return {"seed":SEED,"draws":draws,"demand_failures":demand_fail,"effort_positivity_failures":effort_fail,"ordering_failures":ordering_fail,"widening_wedge_failures":wedge_fail,"direct_optimization_cases":min(DIRECT_OPT_CASES,draws),"direct_optimization_max_abs_error":max_err,"boundary_cases_passed":boundary_ok,"boundary_cases_total":len(boundary_cases())}
def assert_pass(r):
    assert r["demand_failures"]==0 and r["effort_positivity_failures"]==0 and r["ordering_failures"]==0 and r["widening_wedge_failures"]==0
    assert r["direct_optimization_max_abs_error"]<OPT_TOL and r["boundary_cases_passed"]==r["boundary_cases_total"]
def write_csv(path,result):
    rows=[]
    for key in sorted(result):
        value=result[key]; rendered=f"{value:.12g}" if isinstance(value,float) else str(value); status="INFO" if key in {"seed","draws","direct_optimization_cases","boundary_cases_total"} else "PASS"; rows.append((key,rendered,status))
    with Path(path).open("w",newline="",encoding="utf-8") as f:
        f.write("# GENERATED — DO NOT EDIT MANUALLY\n"); w=csv.writer(f,lineterminator="\n"); w.writerow(["check","value","status"]); w.writerows(rows)
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--draws",type=int,default=NUMERICAL_DRAWS); parser.add_argument("--check",action="store_true"); parser.add_argument("--output"); args=parser.parse_args(); r=run_checks(args.draws); assert_pass(r)
    if args.output: write_csv(args.output,r)
    elif not args.check:
        for key in sorted(r): print(f"{key}={r[key]}")
if __name__=="__main__": main()
