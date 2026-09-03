# Welfare and Integrated Screening

## Current trade surplus

With consumer utility normalized so purchase occurs iff `z>=c`, zero marginal cost, and price `c` treated as a transfer,

consumer surplus is

`CS(c)=integral_c^1 (z-c) dz = (1-c)^2/2`.

Retailer current profit is

`pi_R^0(c)=c(1-c)`.

Therefore

`CS(c)+pi_R^0(c)=(1-c^2)/2`,

which is exactly current total trade surplus. Price is not counted as a social loss.

## Integrated objective

Let `B>0` denote the social weight/value of correct upstream adaptation relative to the Bayes-risk reduction `I(c)`. Integrated welfare is

`W(c)=(1-c^2)/2 + delta*B*I(c)`.

The general FOC is

`-c + delta*B*I'(c)=0`.

The welfare effect is therefore not automatically aligned with the retailer's screening choice because the retailer faces current monopoly screening plus a private continuation stake `rho`, while the integrated decision internalizes trade surplus and total adaptation value.

## Canonical family

Let

`sigma := delta*B*kappa*t^2`.

Then

`W(c)=(1-c^2)/2 + sigma*c^2(1-c)`.

FOC:

`W'(c)=c[-1+sigma(2-3c)]`.

If `sigma<=1/2`, welfare is maximized at `c_W*=0`.

If `sigma>1/2`, the unique positive interior maximizer is

`c_W*=(2sigma-1)/(3sigma) = [2-1/sigma]/3`,

which lies in `(0,2/3)`.

The second derivative at the positive root is strictly negative.

## Retailer versus integrated screening

Retailer screening in the canonical family satisfies

`c_R*=[gamma-1+sqrt(gamma^2+gamma+1)]/(3gamma)`,

where `gamma=delta*rho*kappa*t^2`, and always lies in `(1/2,2/3)` for `gamma>0`.

When `sigma<=1/2`, `c_R*>c_W*=0`.

When `sigma>1/2`, the ordering is not globally fixed. Since

`c_W*>c_R*`

iff

`sigma > 1/[2-3c_R*]`,

the planner can screen either less or more than the retailer depending on the total adaptation value relative to private incentives and current trade surplus.

Thus a universal claim such as `rho<B => c_R*>c_W*` is false without additional restrictions.

## Exact witness

Using the main exact witness

`mu=1/2`, `t=3/10`, `kappa=20`, `delta=1`, `rho=25/27`,

and choosing `B=1`,

`gamma=5/3`, `sigma=9/5`.

Then

`c_R*=3/5`,

`c_W*=13/27`.

Hence

`c_R*>c_W*`.

This welfare ordering is exact but not claimed globally.

## B-W1 status

`PROVED` as a conditional ordering characterization in the canonical family, not as a universal direction.

The welfare result is secondary. Its economic content is more than a pure transfer identity, but it combines two familiar wedges: monopoly screening of current demand and partial appropriation of adaptation value. Stage 4-J does not treat B-W1 as the main contribution.