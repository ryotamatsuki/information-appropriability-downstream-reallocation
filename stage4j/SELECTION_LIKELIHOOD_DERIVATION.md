# Selection-Likelihood and Bayesian-Value Derivation

## Selected type distribution

Because `z ~ U[0,1]` and purchase occurs iff `z>=c`,

`f(z | purchase,c)=1/(1-c)` on `[c,1]`.

Hence `E[z | purchase,c]=(1+c)/2`.

For the affine feedback primitive,

`ell_theta(1;c)=E[p_theta(z)|z>=c]`

`= alpha_theta + beta_theta(1+c)/2`.

Let

`q_theta(c) := ell_theta(1;c)`.

Then `ell_theta(0;c)=1-q_theta(c)`.

## Posterior

Let

`m(c)=mu*q_1(c)+(1-mu)*q_0(c)`.

After `y=1`,

`mu_1(c)=mu*q_1(c)/m(c)`.

After `y=0`,

`mu_0(c)=mu*(1-q_1(c))/(1-m(c))`.

If no purchase occurs, posterior remains the prior `mu`.

## Bayes risk and exact binary-experiment value

Prior Bayes risk under quadratic loss is

`R_0 = kappa*mu*(1-mu)`.

Expected posterior Bayes risk conditional on receiving feedback is

`R(c)=kappa*[m(c)*mu_1(c)(1-mu_1(c)) + (1-m(c))*mu_0(c)(1-mu_0(c))]`.

Direct simplification gives

`J(c)=R_0-R(c)`

`= kappa*mu^2*(1-mu)^2*[q_1(c)-q_0(c)]^2 / [m(c)*(1-m(c))]`.

Thus `J(c)>=0`, with equality exactly when the binary feedback experiment is uninformative (`q_1(c)=q_0(c)`) for an interior prior.

Because feedback arrives only after purchase,

`I(c)=(1-c)J(c)`.

Therefore

`I'(c)=-J(c)+(1-c)J'(c)`.

For any informative signal (`J(c)>0`),

`I'(c)>0` iff

`(1-c) J'(c)/J(c) > 1`.

This is the general selected-composition condition: the elasticity-like increase in conditional experiment value must more than offset the lost probability of obtaining a signal.

## Primitive derivative expression

Write

`Delta(c)=q_1(c)-q_0(c)`,

`Delta'(c)=(beta_1-beta_0)/2`,

`m'(c)=[mu*beta_1+(1-mu)*beta_0]/2`.

For `Delta(c) != 0`,

`J'(c)/J(c)`

`= 2 Delta'(c)/Delta(c) - m'(c)[1-2m(c)]/[m(c)(1-m(c))]`.

Therefore the exact primitive sign condition is

`(1-c){ 2 Delta'/Delta - m'(1-2m)/[m(1-m)] } > 1`.

No numerical approximation is needed for this condition.

## Canonical symmetric-crossing family

Take

`mu=1/2`,

`p_0(z)=1/2+t-2tz`,

`p_1(z)=1/2-t+2tz`,

with `0<t<1/2`.

Then

`q_0(c)=1/2-tc`,

`q_1(c)=1/2+tc`,

`m(c)=1/2`,

`Delta(c)=2tc`.

The posterior after `y=1` is `1/2+tc`; after `y=0` it is `1/2-tc`.

The exact conditional value becomes

`J(c)=kappa*t^2*c^2`.

Hence

`I(c)=kappa*t^2*c^2(1-c)`,

`I'(c)=kappa*t^2*c(2-3c)`,

`I''(c)=2*kappa*t^2*(1-3c)`.

Thus conditional experiment value rises with screening, while total ex-ante information value rises iff `0<c<2/3` and falls for `c>2/3`.

## Likelihood ratios

In the canonical family,

`Lambda_1(c)=[1/2+tc]/[1/2-tc]`, which is strictly increasing in `c`,

and

`Lambda_0(c)=[1/2-tc]/[1/2+tc]`, which is strictly decreasing in `c`.

Therefore larger `c` makes the purchase-contingent binary experiment more informative in the standard likelihood-ratio sense.

## Blackwell ordering

The canonical family is a symmetric binary experiment with accuracy `1/2+tc`. For `c_2>c_1>=0`, the experiment at `c_1` can be generated from the experiment at `c_2` by state-independent binary garbling. Hence purchase-contingent experiments are Blackwell ordered: higher screening improves conditional experiment quality. The nontrivial object is the ex-ante tradeoff between that improvement and the lower probability `1-c` of observing any feedback.