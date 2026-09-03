# Generic Quantity–Quality Kill — Stage 6-J

## Purpose

Stage 4-J used the additive deterministic benchmark

\[
H(c)=\int_c^1 v(z)\,dz,
\]

which necessarily satisfies `H'(c)=-v(c)<=0`. Stage 6-J must test a stronger non-information analogue because an ordinary selection problem may change both the number and the average quality of selected units.

## Exact non-information reproduction

Delete:

- latent state `θ`;
- feedback `y`;
- Bayesian updating;
- Bayes risk;
- the manufacturer;
- all information terminology.

Let a selector choose `c`. Define deterministic selected quantity

\[
n(c)=1-c
\]

and deterministic average continuation quality/productivity

\[
q(c)=\kappa t^2c^2.
\]

Aggregate continuation output is

\[
Q(c)=n(c)q(c)
     =(1-c)\kappa t^2c^2.
\]

Therefore

\[
\boxed{Q(c)\equiv I(c)}.
\]

Let the selector maximize

\[
\widetilde\Pi(c)=c(1-c)+\delta\rho Q(c).
\]

Since `Q=I`,

\[
\widetilde\Pi(c)\equiv\Pi_R(c).
\]

Consequently the non-information model has exactly the same:

1. FOC;
2. SOC;
3. unique equilibrium;
4. formula for `c*(γ)`;
5. interval `1/2<c*<2/3`;
6. comparative static `dc*/dρ>0`;
7. exact witness;
8. open parameter region.

## Fixed-quality benchmark

Freeze average quality at `\bar q>0` while preserving selected quantity:

\[
Q_F(c)=(1-c)\bar q.
\]

Then

\[
Q_F'(c)=-\bar q<0.
\]

The selector's interior optimum is

\[
c_F^*(\rho)=\frac{1-\delta\rho\bar q}{2},
\]

so

\[
\boxed{\frac{dc_F^*}{d\rho}=-\frac{\delta\bar q}{2}<0}.
\]

Thus the **same sign reversal** as B-P1 is reproduced with no uncertainty or information.

## Why the Stage 4 benchmark was insufficient

The Stage 4 additive benchmark represented aggregate deterministic value as the integral of nonnegative individual contributions from all selected types. Under that restriction, removing a marginal selected type can never increase aggregate output.

But B-P1's own economics is a quantity–average-quality tradeoff. A generic deterministic analogue must therefore allow the average quality of the selected set to improve as the cutoff increases. Once this ordinary composition effect is permitted, the Bayesian information-value function is reproduced exactly.

No exotic complementarity, negative output, or pathological function is required. `n(c)=1-c` decreases smoothly and `q(c)=κt²c²` increases smoothly from zero.

## Information-specificity verdict

The fact that Stage 4-J obtains `q(c)=κt²c²` from a latent-mixture Bayesian experiment provides an interpretation and microfoundation for an increasing quality function. It does **not** make the equilibrium comparative static information-specific.

The theorem survives complete deletion of information while preserving an ordinary quantity–quality selection technology.

## Canonical verdict

\[
\boxed{\textbf{FAIL — EXACT GENERIC NON-INFORMATION REPRODUCTION}}
\]

This result alone satisfies the Stage 6-J NO-GO standard.
