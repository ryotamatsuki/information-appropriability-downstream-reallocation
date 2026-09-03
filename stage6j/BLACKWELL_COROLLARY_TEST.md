# Blackwell-Corollary Test — Stage 6-J

## Frozen Stage 4-J family

Under

\[
q_0(c)=\frac12-tc,\qquad q_1(c)=\frac12+tc,
\]

higher `c` increases the separation of the two binary signal distributions. Conditional on receiving feedback, the experiment is therefore more informative as screening rises.

The conditional Bayes-risk reduction is

\[
J(c)=\kappa t^2c^2,
\]

while the probability of obtaining feedback is

\[
n(c)=1-c.
\]

Thus total ex ante information value is

\[
I(c)=n(c)J(c)=(1-c)\kappa t^2c^2.
\]

## Comparative-static logic

The retailer solves

\[
\max_c\; u(c)+\delta\rho I(c).
\]

At a regular interior optimum, a larger weight `ρ` raises `c` whenever

\[
I'(c)>0.
\]

Since

\[
I'(c)=-J(c)+(1-c)J'(c),
\]

the condition is

\[
(1-c)\frac{J'(c)}{J(c)}>1.
\]

With fixed conditional experiment quality, `J'(c)=0`, so the derivative is negative. Hence the Stage 4-J sign reversal follows once the improvement in conditional experiment quality is sufficiently elastic relative to the lost observation probability.

## Is this a standard Blackwell theorem?

No inspected single Blackwell/value-of-information theorem was verified to state the exact B-P1 equilibrium sign reversal. Standard information ordering establishes that a more informative experiment is weakly more valuable for a given decision problem; it does not by itself compare the value of a more informative but less frequently observed experiment.

However, after Stage 4-J has reduced the Bayesian problem to the scalar function `I(c)`, the remaining comparative static is elementary: a larger objective weight on `I(c)` moves the optimum toward regions where `I` is higher. The Blackwell improvement supplies an interpretation of why `J(c)` rises, but no further strategic interaction is required.

## Verdict

**BLACKWELL-COROLLARY RISK: HIGH / FAIL FOR MAIN-CONTRIBUTION NOVELTY.**

This is not recorded as literal exact prior art. It reinforces the conclusion that the theorem's economic content is a quantity-versus-quality tradeoff once the information value has been summarized by `J(c)`.

The binding Stage 6-J kill remains the stronger deterministic quantity-quality reduction, which reproduces B-P1 exactly without any Blackwell experiment.
