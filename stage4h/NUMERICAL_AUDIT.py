#!/usr/bin/env python3
"""Diagnostic numerical audit for Stage 4-H. Numerical evidence is not theorem proof."""
import math
import numpy as np
from scipy.optimize import root, brentq

SEED=20260903
RAW_DRAWS=10000

def geom(e1,e2,q):
    D=1+e1+e2+q*e1*e2
    L=(2+e1+e2)/D
    m1=(q*e2**2+2*q*e2+1)/D**2
    m2=(q*e1**2+2*q*e1+1)/D**2
    m11=-2*(q*e2+1)*(q*e2**2+2*q*e2+1)/D**3
    m22=-2*(q*e1+1)*(q*e1**2+2*q*e1+1)/D**3
    m12=2*(1-q)*(q*e1*e2-1)/D**3
    return L,m1,m2,m11,m22,m12

def solve_eq(eta,q,b,k1,k2):
    x0=np.array([(b*(1-eta)/k1)**(1/3),(b*eta/k2)**(1/3)])
    def F(x):
        e1,e2=x
        _,m1,m2,_,_,_=geom(e1,e2,q)
        return np.array([k1*e1-b*(1-eta)*m1,k2*e2-b*eta*m2])
    def J(x):
        e1,e2=x
        _,_,_,m11,m22,m12=geom(e1,e2,q)
        return np.array([[k1-b*(1-eta)*m11,-b*(1-eta)*m12],[-b*eta*m12,k2-b*eta*m22]])
    sol=root(F,x0,jac=J,method='hybr',tol=1e-10)
    ok=sol.success and np.all(sol.x>=-1e-10) and np.linalg.norm(F(sol.x))<1e-8
    return np.maximum(sol.x,0),ok

def stats(e1,e2,eta,q,b,k1,k2,B=1.0):
    _,m1,m2,m11,m22,m12=geom(e1,e2,q)
    J=np.array([[k1-b*(1-eta)*m11,-b*(1-eta)*m12],[-b*eta*m12,k2-b*eta*m22]])
    ep=-np.linalg.solve(J,np.array([b*m1,-b*m2]))
    Eprime=float(ep.sum())
    Lprime=float(-(m1*ep[0]+m2*ep[1]))
    Wprime=float(np.array([B*m1-k1*e1,B*m2-k2*e2])@ep)
    return Eprime,Lprime,Wprime,float(np.linalg.det(J))

rng=np.random.default_rng(SEED)
feasible=fail=p1=p1_concentration=0
min_det=float('inf')
endpoint_subset=[]
for _ in range(RAW_DRAWS):
    eta=float(rng.uniform(.05,.95))
    phi=float(rng.uniform(0,math.pi/2))
    q=math.sin(phi)**2
    k1=float(10**rng.uniform(math.log10(.5),math.log10(3.0)))
    k2=float(10**rng.uniform(math.log10(.5),math.log10(3.0)))
    e,ok=solve_eq(eta,q,1.0,k1,k2)
    if not ok:
        fail+=1
        continue
    feasible+=1
    Ep,Lp,_,det=stats(*e,eta,q,1.0,k1,k2)
    min_det=min(min_det,det)
    if Ep>1e-7 and Lp>1e-7:
        p1+=1
        if eta>.5:
            p1_concentration+=1
    if len(endpoint_subset)<2000:
        endpoint_subset.append((eta,k1,k2))

welfare_switch=0
for eta,k1,k2 in endpoint_subset:
    e0,ok0=solve_eq(eta,0,1.0,k1,k2)
    e1,ok1=solve_eq(eta,1,1.0,k1,k2)
    if ok0 and ok1:
        W0=stats(*e0,eta,0,1.0,k1,k2)[2]
        W1=stats(*e1,eta,1,1.0,k1,k2)[2]
        welfare_switch += int(W0*W1 < -1e-8)

eta0=3/5
k1w=432/245
k2w=81/80

def witness_Lprime(q):
    e,ok=solve_eq(eta0,q,1.0,k1w,k2w)
    assert ok
    return stats(*e,eta0,q,1.0,k1w,k2w)[1]

qstar=brentq(witness_Lprime,0,1)
phi_star=math.degrees(math.asin(math.sqrt(qstar)))

print({
    'seed':SEED,
    'raw_draws':RAW_DRAWS,
    'feasible_draws':feasible,
    'solver_failures':fail,
    'H_P1_cases':p1,
    'H_P1_cases_eta_gt_half':p1_concentration,
    'counterexamples_to_global_H_P1':feasible-p1,
    'minimum_FOC_Jacobian_determinant':min_det,
    'welfare_endpoint_sign_switches_in_2000_draw_subset':welfare_switch,
    'exact_witness_q_crossing_numeric':qstar,
    'exact_witness_phi_crossing_degrees_numeric':phi_star,
})
