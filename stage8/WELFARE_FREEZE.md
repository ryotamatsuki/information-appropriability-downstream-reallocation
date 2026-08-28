# Welfare Freeze

## Microfounded benchmark

Let consumer masses be `1-h(η)` and `h(η)` with `0<h(η)<1` and `h'(η)>0`.

Quasilinear utility:

`u(q,x) = (a+x)q - q²/2 - p q`.

Per-capita demand:

`d(x)=a+x-p`.

Aggregate route quantities:

`q_S=(1-h)d(x)`,

`q_R=h d(x)`.

Real distribution costs satisfy `c_S>c_R≥0`.

Margin mapping:

`b+m=p-c_S`,

`b+δ=p-c_R`,

so `δ-m=c_S-c_R>0`.

Tractable learning and effort cost:

`x=βe`,

`C(e)=ke²/2`.

## Parameter restrictions

- `a>p>c_S>c_R≥0`;
- `0<m<p-c_S`, equivalently `b=p-c_S-m>0`;
- `β>0`;
- `k>β²`;
- `0<h(η)<1` and `h'(η)>0`.

These imply positive baseline demand, positive interior benchmark efforts, positive relevant margins, and strict concavity of social welfare in effort.

## Effort levels

Private:

`e^P = mβ(1-h)/k`.

Coordinated:

`e^C = β[(p-c_S)(1-h)+(p-c_R)h]/k`.

Social:

`e^W = β[a-c_S(1-h)-c_R h]/(k-β²)`.

Under the frozen restrictions:

**`e^P < e^C < e^W`.**

## Widening wedges

`d(e^C-e^P)/dη = β h'(η)[(c_S-c_R)+m]/k > 0`.

Also `d(e^W-e^P)/dη > 0` because `c_S>c_R`, `m>0`, `h'>0`, and `k>β²`.

## Consumer surplus

With `d=A+βe`, `A=a-p>0`, aggregate consumer surplus is `CS=d²/2`.

## Organizational under-retention

The result is deliberately local and conditional. At an interior private retention-indifference point in the tractable retention block, `Δπ_M=0`, while the specialist's equilibrium payoff is positive and product improvement raises consumer surplus. Therefore welfare favors retention at that private indifference point. By continuity, provided the threshold has a genuine private non-retention side, a nonempty local region exists in which the manufacturer does not retain the information-producing capacity while social welfare favors retention.

No stronger global under-retention claim is frozen.
