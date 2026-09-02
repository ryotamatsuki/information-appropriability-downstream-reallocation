#!/usr/bin/env python3
"""Exact symbolic checks for Stage 4-H."""
import sympy as sp

e1,e2,q,T = sp.symbols("e1 e2 q T", positive=True)
D = 1+e1+e2+q*e1*e2
L = (2+e1+e2)/D
G = 2-L
m1 = sp.factor(sp.diff(G,e1))
m2 = sp.factor(sp.diff(G,e2))
m11 = sp.factor(sp.diff(m1,e1))
m22 = sp.factor(sp.diff(m2,e2))
m12 = sp.factor(sp.diff(m1,e2))

assert sp.simplify(m1-(q*e2**2+2*q*e2+1)/D**2)==0
assert sp.simplify(m2-(q*e1**2+2*q*e1+1)/D**2)==0
assert sp.simplify(m11+2*(q*e2+1)*(q*e2**2+2*q*e2+1)/D**3)==0
assert sp.simplify(m22+2*(q*e1+1)*(q*e1**2+2*q*e1+1)/D**3)==0
assert sp.simplify(m12-2*(1-q)*(q*e1*e2-1)/D**3)==0

# Mechanism-off q=0.
E=sp.symbols("E", positive=True)
assert sp.simplify(L.subs({q:0,e2:E-e1})-(E+2)/(E+1))==0

# Orthogonal q=1.
assert sp.simplify(L.subs(q,1)-(1/(1+e1)+1/(1+e2)))==0
assert sp.simplify(G.subs(q,1)-(e1/(1+e1)+e2/(1+e2)))==0

# Fixed-total-precision lemma.
x=sp.symbols("x", nonnegative=True)
D_T=sp.expand(D.subs({e1:x,e2:T-x}))
assert sp.simplify(D_T-(1+T+q*x*(T-x)))==0
assert sp.factor(sp.diff(D_T,x)) == -q*(-T+2*x)
assert sp.diff(D_T,x,2) == -2*q

# Exact H-P1 witness at q=1.
eta0=sp.Rational(3,5)
e10=sp.Rational(1,6)
e20=sp.Rational(1,3)
k10=sp.Rational(432,245)
k20=sp.Rational(81,80)
a1=(1/k10)/((1+e10)*(1+3*e10))
a2=(1/k20)/((1+e20)*(1+3*e20))
assert sp.simplify(e10*(1+e10)**2-(1-eta0)/k10)==0
assert sp.simplify(e20*(1+e20)**2-eta0/k20)==0
assert sp.simplify(a1-sp.Rational(35,108))==0
assert sp.simplify(a2-sp.Rational(10,27))==0
Eprime=sp.simplify(a2-a1)
Lprime=sp.simplify(a1/(1+e10)**2-a2/(1+e20)**2)
assert Eprime == sp.Rational(5,108)
assert Lprime == sp.Rational(5,168)
assert sp.simplify(a2/a1-sp.Rational(8,7))==0
assert sp.simplify(((1+e20)/(1+e10))**2-sp.Rational(64,49))==0

print("PASS")
print("L =", L)
print("G_e1 =", m1)
print("G_e2 =", m2)
print("G_e1e2 =", m12)
print("Exact witness d(total precision)/deta =", Eprime)
print("Exact witness d(loss)/deta =", Lprime)
