"""Deterministic admissible-parameter generation and boundary smoke checks."""
from __future__ import annotations
import random
from dataclasses import dataclass
from common.parameters import SEED

@dataclass(frozen=True)
class Params:
    a:float; p:float; c_s:float; c_r:float; m:float; beta:float; k:float; h:float; h_prime:float

def generate_admissible(n:int,seed:int=SEED)->list[Params]:
    rng=random.Random(seed); out=[]
    for _ in range(n):
        c_r=rng.uniform(0.0,2.0); c_s=c_r+rng.uniform(0.05,2.0); p=c_s+rng.uniform(0.2,3.0); a=p+rng.uniform(0.2,5.0); m=rng.uniform(0.01,0.95*(p-c_s)); beta=rng.uniform(0.05,2.0); k=beta*beta+rng.uniform(0.2,6.0); h=rng.uniform(0.01,0.99); hp=rng.uniform(0.05,1.5); out.append(Params(a,p,c_s,c_r,m,beta,k,h,hp))
    return out

def boundary_cases()->dict[str,Params]:
    base=Params(5.0,3.0,2.0,1.0,0.4,1.0,3.0,0.5,1.0)
    return {"beta_small":Params(**{**base.__dict__,"beta":1e-8}),"h_near_zero":Params(**{**base.__dict__,"h":1e-8}),"h_near_one":Params(**{**base.__dict__,"h":1-1e-8}),"cost_gap_small":Params(**{**base.__dict__,"c_r":base.c_s-1e-8}),"social_concavity_near_boundary":Params(**{**base.__dict__,"k":base.beta**2+1e-5})}
