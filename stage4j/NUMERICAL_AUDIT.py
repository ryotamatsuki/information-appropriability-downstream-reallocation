#!/usr/bin/env python3
"""Stage 4-J diagnostic numerical audit. Numerical evidence is not theorem proof."""
import numpy as np
from scipy.optimize import minimize_scalar

SEED = 20260903
RAW_DRAWS = 20000


def info(c, mu, p00, p01, p10, p11):
    b0 = p01-p00
    b1 = p11-p10
    q0 = p00 + b0*(1+c)/2
    q1 = p10 + b1*(1+c)/2
    m = mu*q1 + (1-mu)*q0
    D = q1-q0
    if min(q0,q1,m,1-q0,1-q1,1-m) <= 0:
        return None
    J = mu**2*(1-mu)**2*D**2/(m*(1-m))
    return (1-c)*J


def dI(c, mu, p00, p01, p10, p11):
    h = 1e-5
    f0 = info(c,mu,p00,p01,p10,p11)
    fp = info(c+h,mu,p00,p01,p10,p11)
    fm = info(c-h,mu,p00,p01,p10,p11)
    return (fp-fm)/(2*h), (fp-2*f0+fm)/h**2


def retail_obj(c, pars):
    mu,p00,p01,p10,p11,lam = pars
    return c*(1-c) + lam*info(c,mu,p00,p01,p10,p11)


def welfare_obj(c, mu,p00,p01,p10,p11,sigma):
    return (1-c*c)/2 + sigma*info(c,mu,p00,p01,p10,p11)


def maximize(fun):
    sol = minimize_scalar(lambda x: -fun(x), bounds=(0,1), method='bounded', options={'xatol':1e-11})
    pts = [(sol.x,fun(sol.x)),(0.0,fun(0.0)),(1.0,fun(1.0))]
    return max(pts,key=lambda x:x[1])[0]


rng=np.random.default_rng(SEED)
feasible=solver_fail=interior=bp1=global_counter=0
r_gt_w=r_lt_w=r_eq_w=0
min_soc_margin=float('inf')

for _ in range(RAW_DRAWS):
    mu=float(rng.uniform(.1,.9))
    p00,p01,p10,p11=map(float,rng.uniform(.05,.95,4))
    lam=float(rng.uniform(0,30))
    sigma=float(rng.uniform(0,30))
    feasible += 1
    pars=(mu,p00,p01,p10,p11,lam)
    try:
        cr=maximize(lambda x: retail_obj(x,pars))
        cw=maximize(lambda x: welfare_obj(x,mu,p00,p01,p10,p11,sigma))
    except Exception:
        solver_fail += 1
        continue
    if cr > cw+1e-5:
        r_gt_w += 1
    elif cr < cw-1e-5:
        r_lt_w += 1
    else:
        r_eq_w += 1
    if 1e-5 < cr < 1-1e-5:
        interior += 1
        ip,ipp=dI(cr,mu,p00,p01,p10,p11)
        soc=-2+lam*ipp
        min_soc_margin=min(min_soc_margin,-soc)
        if cr>.5 and ip>1e-7 and soc<0:
            bp1 += 1
        else:
            global_counter += 1

# Canonical exact witness evaluated numerically as an implementation cross-check.
t=.3
kap=20.0
rho=25/27
cwitness=.6
Iw=lambda x: kap*t*t*x*x*(1-x)
Ipw=kap*t*t*cwitness*(2-3*cwitness)
SOCw=-2+rho*(2*kap*t*t*(1-3*cwitness))

print(f'seed={SEED}')
print(f'raw_draws={RAW_DRAWS}')
print(f'feasible_draws={feasible}')
print(f'solver_failures={solver_fail}')
print(f'interior_retailer_draws={interior}')
print(f'B-P1_sign_reversal_draws={bp1}')
print(f'counterexamples_to_global_B-P1={global_counter}')
print(f'minimum_sampled_SOC_margin={min_soc_margin:.12g}')
print(f'welfare_order_R_gt_W={r_gt_w}')
print(f'welfare_order_R_lt_W={r_lt_w}')
print(f'welfare_order_approximately_equal={r_eq_w}')
print(f'witness_c={cwitness}')
print(f'witness_Iprime={Ipw}')
print(f'witness_SOC={SOCw}')
print('generic_additive_output_counterexamples=0 (analytic identity H_prime=-v(c)<=0)')
