# Stage 4-J Model Specification

## Canonical question

Can a downstream retailer's ordinary commercial screening choice change the selected-customer feedback likelihood faced by an upstream Bayesian manufacturer, and thereby change the retailer's own screening incentive through the manufacturer's later adaptation?

## Players and timing

1. Nature draws `theta in {0,1}`, with `Pr(theta=1)=mu in (0,1)`.
2. Retailer `R` chooses one screening action `c in [0,1]`.
3. One short-lived consumer has latent taste `z ~ U[0,1]` and purchases iff `z >= c`.
4. Conditional on purchase, feedback `y in {0,1}` is generated.
5. Manufacturer `M` observes `c`, purchase/no-purchase, and `y` if purchase occurs. `M` does not observe `z`. `M` knows the selection rule and updates rationally.
6. `M` chooses adaptation `a in [0,1]`.
7. Continuation payoffs are realized.

No disclosure, contracts, attention, Poisson learning, regime switching, firm-size heterogeneity, second strategic retailer, or endogenous information effort is used.

## Consumer screening and current profit

The consumer buys iff `z >= c`. Hence

- purchase probability: `1-c`;
- selected type distribution: `z | z>=c ~ U[c,1]`;
- retailer current profit under normalized zero marginal cost: `pi_R^0(c)=c(1-c)`.

## General feedback technology

For `theta in {0,1}`,

`Pr(y=1 | theta,z) = p_theta(z) = alpha_theta + beta_theta z`.

Primitive feasibility requires both endpoint probabilities to lie strictly inside `(0,1)`:

`0 < alpha_theta < 1`,

`0 < alpha_theta + beta_theta < 1`,

for each `theta`. Because the technology is affine in `z`, these endpoint restrictions are sufficient for all `z in [0,1]`.

## Selected likelihood

For a purchaser,

`ell_theta(1;c) = alpha_theta + beta_theta(1+c)/2`,

`ell_theta(0;c) = 1-ell_theta(1;c)`.

Thus

`d ell_theta(1;c)/dc = beta_theta/2`,

`d ell_theta(0;c)/dc = -beta_theta/2`.

A no-purchase event contains no information about `theta` because `z` and `theta` are independent and the purchase rule depends only on `z,c`.

## Manufacturer adaptation

Manufacturer loss is

`L_M(a,theta)=kappa(a-theta)^2`, `kappa>0`.

Therefore after any posterior `mu_y`, the unique optimal adaptation is

`a*(mu_y)=mu_y`.

## Retailer continuation stake

Retailer objective is

`Pi_R(c)=c(1-c)+delta*rho*I(c)`,

where `I(c)` is the ex-ante Bayes-risk reduction created by purchase-contingent feedback, `delta in (0,1]`, and `rho>=0` is the retailer's reduced-form stake in correct upstream adaptation. `rho` is not a novelty primitive.

## Canonical tractable family used for the primary theorem

The unrestricted affine model is retained for verification and numerical counterexample search. The analytical hard-kill theorem uses the following interior, symmetric, economically interpretable subfamily:

`mu=1/2`, `0<t<1/2`,

`p_0(z)=1/2+t-2tz`,

`p_1(z)=1/2-t+2tz`.

All primitive probabilities lie in `[1/2-t,1/2+t] subset (0,1)`. Low- and high-taste users react in opposite directions to the latent design-fit state. Because `z` is latent to `M`, pooling different customer types can cancel diagnostic content. Screening changes that mixture.

Under this family,

`ell_0(1;c)=1/2-tc`,

`ell_1(1;c)=1/2+tc`.

This family is not a boundary calibration. The exact witness later uses `t=3/10`, giving primitive feedback probabilities between `1/5` and `4/5`.

## Scope decision

The project-level reallocation parameter `eta` is deliberately omitted at Stage 4-J. The Stage 3-J contract requires the core selected-likelihood feedback to survive first. No additional route-share primitive is needed to establish or test the mechanism.