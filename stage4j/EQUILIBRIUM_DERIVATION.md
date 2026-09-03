# Retailer Equilibrium Derivation

## General model

Retailer objective:

`Pi_R(c)=c(1-c)+delta*rho*I(c)`.

Interior FOC:

`1-2c + delta*rho*I'(c)=0`.

SOC:

`-2 + delta*rho*I''(c) < 0`.

For any regular interior solution,

`dc*/drho = -delta*I'(c*) / [-2+delta*rho*I''(c*)]`.

Thus under the SOC the comparative-static sign equals the sign of `I'(c*)`.

Existence is automatic because `Pi_R` is continuous on compact `[0,1]`. Global uniqueness is not asserted for unrestricted affine feedback primitives.

## Canonical family

Let

`gamma := delta*rho*kappa*t^2 > 0`.

Because `I(c)=kappa*t^2*c^2(1-c)`, retailer profit is

`Pi_R(c)=c(1-c)+gamma*c^2(1-c)`.

FOC:

`F(c;gamma)=1+2(gamma-1)c-3gamma*c^2=0`.

The roots have product `-1/(3gamma)<0`, so exactly one root is positive. Since

`F(0)=1>0`,

`F(1)=-1-gamma<0`,

the unique positive root lies in `(0,1)` and is the unique global maximizer on `[0,1]`.

Closed form:

`c*(gamma)=[gamma-1+sqrt(gamma^2+gamma+1)]/(3gamma)`.

## Exact location of equilibrium

At `c=1/2`,

`F(1/2;gamma)=gamma/4>0`.

At `c=2/3`,

`F(2/3;gamma)=-1/3<0`.

Therefore for every `gamma>0`,

`1/2 < c*(gamma) < 2/3`.

Since `I'(c)=kappa*t^2*c(2-3c)`, it follows immediately that

`I'(c*)>0` for every `gamma>0`.

## Comparative static in retailer continuation stake

`partial F/partial rho = delta*kappa*t^2*c(2-3c)>0` at equilibrium.

The derivative of the FOC with respect to `c` is

`F_c=2(gamma-1)-6gamma*c`.

Because the positive root is the crossing from positive to negative and the other root is negative, `F_c(c*)<0`.

Hence

`dc*/drho = -F_rho/F_c >0`.

This is the full-model side of B-P1.

## Exact witness

Choose

`mu=1/2`, `t=3/10`, `kappa=20`, `delta=1`, `rho=25/27`.

Then

`gamma=delta*rho*kappa*t^2=5/3`.

The unique equilibrium is

`c*=3/5`.

At this point,

`I'(3/5)=27/125>0`.

The retailer FOC holds exactly:

`1-2(3/5) + (25/27)(27/125)= -1/5+1/5=0`.

The SOC is

`Pi_R''(3/5)=-14/3<0`.

Primitive feedback probabilities are

`p_0(z)=4/5-(3/5)z`,

`p_1(z)=1/5+(3/5)z`,

so every primitive feedback probability lies between `1/5` and `4/5`: the witness is not near a probability boundary.

The selected feedback probabilities at the equilibrium are

`q_0=8/25`, `q_1=17/25`.

## Open parameter region

At the exact witness, feasibility, the interior conditions, `I'(c*)>0`, and the SOC all hold strictly. Equilibrium is locally unique because `F_c != 0`. All relevant objects are continuous in the primitive parameters. The implicit-function theorem therefore gives a nonempty open neighborhood of the witness in the unrestricted affine primitive space in which the same sign result holds. B-P1 is not knife-edge.

## Corners

In the canonical family with `gamma>0`, neither boundary is optimal because `F(0)>0` and `F(1)<0`; the equilibrium is always interior. At `rho=0`, the model collapses to the current-profit problem and `c*=1/2`.