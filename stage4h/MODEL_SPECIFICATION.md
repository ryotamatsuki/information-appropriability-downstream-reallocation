# Stage 4-H — Model Specification

Starting canonical main / Stage 3-I merge SHA: `864080c804eebf458ce733f9cb34b4396f9a939f`

Branch: `stage4/diagnostic-diversity-minimal-model`

Canonical mechanism: **Diagnostic Diversity under Downstream Concentration**.

## Players and timing

Players are upstream manufacturer `M` and downstream information producers `S_1,S_2`.

1. Exogenous reallocation parameter `eta in [0,1]` is realized.
2. `S_i` simultaneously choose information effort `e_i >= 0`.
3. Signals are generated and transmitted automatically/truthfully.
4. `M` observes the signals, forms a Bayesian posterior, and chooses product/design action `a`.
5. Payoffs realize.

No prices, contracts, disclosure, ownership, portability, bargaining, dynamics, entry, or channel-choice margin is introduced.

## State and signals

`theta ~ N(0,I_2)`.

`h_1=(1,0)'`, `h_2=(cos(phi),sin(phi))'`, with `phi in [0,pi/2]`.

`y_i=h_i' theta + epsilon_i` with conditionally independent Gaussian noise.

Write `q=sin(phi)^2 in [0,1]`.

## Normalization decision

Stage 4 uses **Option B**:

`tau_i = e_i`.

Reallocation enters only private appropriability:

`nu_1(eta)=1-eta`, `nu_2(eta)=eta`.

Reason: putting `eta` both in precision production `tau_i=nu_i e_i` and in private return `r_i=b_i nu_i` counts the same downstream reallocation twice and can mechanically generate the desired response. Option B isolates the strategic channel: reallocation changes who captures the return to generating a diagnostic signal, while the information technology itself is fixed.

## Bayesian design value

Posterior precision is

`P = I_2 + e_1 h_1 h_1' + e_2 h_2 h_2'`.

Manufacturer action is

`a*=E[theta | y_1,y_2]`.

Expected residual design loss is

`L(e_1,e_2,phi)=tr(P^{-1})`.

No-information loss is `L_0=2`; define design improvement `G=2-L`.

## Private payoffs

Baseline private payoff:

`pi_1=b(1-eta)G - k_1 e_1^2/2`,

`pi_2=b eta G - k_2 e_2^2/2`,

with `b,k_i>0`.

The only effect of `phi` is through posterior information geometry. No diversity premium is inserted directly into payoffs.

## System benchmark

Use

`W=B G - k_1 e_1^2/2 - k_2 e_2^2/2`,

with baseline `B=b` and no direct dependence of system design value on `eta`.

Thus reallocation affects decentralized information incentives, not the underlying system value of a given signal portfolio.

## Contribution switch

Mechanism ON: `phi>0` (`q>0`), non-collinear diagnostic directions.

Mechanism OFF: `phi=0` (`q=0`), `h_1=h_2`, retaining two effort choices and private reallocation incentives but removing diagnostic diversity.
