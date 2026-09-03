"""Stage 4-J exact symbolic verification.

Run with Python 3 + SymPy.  Raises AssertionError on any failed canonical identity.
"""
import sympy as sp

c, z = sp.symbols('c z', real=True)
mu, kappa, t, delta, rho, B = sp.symbols(
    'mu kappa t delta rho B', positive=True, real=True
)
a0, a1, b0, b1 = sp.symbols('a0 a1 b0 b1', real=True)

# General selected likelihood.
p0 = a0 + b0*z
p1 = a1 + b1*z
q0 = sp.integrate(p0, (z, c, 1)) / (1-c)
q1 = sp.integrate(p1, (z, c, 1)) / (1-c)
assert sp.simplify(q0 - (a0 + b0*(1+c)/2)) == 0
assert sp.simplify(q1 - (a1 + b1*(1+c)/2)) == 0

m = sp.expand(mu*q1 + (1-mu)*q0)
post1 = sp.cancel(mu*q1/m)
post0 = sp.cancel(mu*(1-q1)/(1-m))

# Bayes-risk identity.
R0 = kappa*mu*(1-mu)
R = kappa*(m*post1*(1-post1) + (1-m)*post0*(1-post0))
J = sp.cancel(R0-R)
J_closed = sp.cancel(
    kappa*mu**2*(1-mu)**2*(q1-q0)**2/(m*(1-m))
)
assert sp.cancel(J-J_closed) == 0

I = sp.cancel((1-c)*J_closed)
assert sp.cancel(sp.diff(I,c) - (-J_closed + (1-c)*sp.diff(J_closed,c))) == 0

# Canonical symmetric-crossing family.
subs_family = {
    mu: sp.Rational(1,2),
    a0: sp.Rational(1,2)+t,
    b0: -2*t,
    a1: sp.Rational(1,2)-t,
    b1: 2*t,
}
q0f = sp.simplify(q0.subs(subs_family))
q1f = sp.simplify(q1.subs(subs_family))
assert sp.simplify(q0f - (sp.Rational(1,2)-t*c)) == 0
assert sp.simplify(q1f - (sp.Rational(1,2)+t*c)) == 0

Jf = sp.factor(J_closed.subs(subs_family))
If = sp.factor(I.subs(subs_family))
assert sp.simplify(Jf - kappa*t**2*c**2) == 0
assert sp.simplify(If - kappa*t**2*c**2*(1-c)) == 0
Ipf = sp.factor(sp.diff(If,c))
Ippf = sp.factor(sp.diff(If,c,2))
assert sp.simplify(Ipf - kappa*t**2*c*(2-3*c)) == 0
assert sp.simplify(Ippf - 2*kappa*t**2*(1-3*c)) == 0

# Retailer FOC and exact root.
gamma = sp.symbols('gamma', positive=True, real=True)
Pi = c*(1-c) + delta*rho*If
F = sp.factor(sp.diff(Pi,c))
F_gamma = 1 + 2*(gamma-1)*c - 3*gamma*c**2
assert sp.simplify(F.subs(delta*rho*kappa*t**2, gamma) - F_gamma) == 0

cstar = (gamma-1 + sp.sqrt(gamma**2+gamma+1))/(3*gamma)
assert sp.simplify(F_gamma.subs(c,cstar)) == 0
assert sp.simplify(F_gamma.subs(c,sp.Rational(1,2)) - gamma/4) == 0
assert sp.simplify(F_gamma.subs(c,sp.Rational(2,3)) + sp.Rational(1,3)) == 0

# Fixed-likelihood benchmark.
Jbar = sp.symbols('Jbar', positive=True, real=True)
IF = (1-c)*Jbar
PiF = c*(1-c)+delta*rho*IF
FF = sp.diff(PiF,c)
assert sp.simplify(FF - (1-2*c-delta*rho*Jbar)) == 0
cF = (1-delta*rho*Jbar)/2
assert sp.simplify(FF.subs(c,cF)) == 0
assert sp.simplify(sp.diff(cF,rho) + delta*Jbar/2) == 0

# Exact rational witness.
witness = {
    t: sp.Rational(3,10),
    kappa: 20,
    delta: 1,
    rho: sp.Rational(25,27),
    c: sp.Rational(3,5),
}
assert sp.simplify(F.subs(witness)) == 0
assert sp.simplify(Ipf.subs(witness) - sp.Rational(27,125)) == 0
assert sp.simplify(sp.diff(Pi,c,2).subs(witness) + sp.Rational(14,3)) == 0

# Type-observed benchmark in canonical family.
jz = kappa*t**2*(2*z-1)**2
Iobs = sp.integrate(jz, (z,c,1))
assert sp.simplify(sp.diff(Iobs,c) + jz.subs(z,c)) == 0

# Welfare canonical family.
W = (1-c**2)/2 + delta*B*If
WF = sp.factor(sp.diff(W,c))
assert sp.simplify(WF + c*(1-delta*B*kappa*t**2*(2-3*c))) == 0
cw = (2*delta*B*kappa*t**2-1)/(3*delta*B*kappa*t**2)
assert sp.simplify(WF.subs(c,cw)) == 0

# Likelihood-ratio monotonicity numerator checks for the canonical family.
L1 = (sp.Rational(1,2)+t*c)/(sp.Rational(1,2)-t*c)
L0 = 1/L1
assert sp.factor(sp.diff(L1,c)) == 4*t/(2*c*t-1)**2
assert sp.factor(sp.diff(L0,c)) == -4*t/(2*c*t+1)**2

print('Stage 4-J symbolic verification: PASS')
