# Stage 4-H — Bayesian Information Geometry

Let `q=sin(phi)^2`.

With `h_1=(1,0)'` and `h_2=(cos(phi),sin(phi))'`, posterior precision is

`P = I_2 + e_1 h_1h_1' + e_2 h_2h_2'`.

Its determinant is

`D = 1 + e_1 + e_2 + q e_1 e_2`.

The exact posterior loss is

`L = (2+e_1+e_2)/D`.

Therefore

`G = 2-L`.

## Marginal information values

`G_1 = (q e_2^2 + 2q e_2 + 1)/D^2`,

`G_2 = (q e_1^2 + 2q e_1 + 1)/D^2`.

Both are strictly positive.

Own curvature:

`G_11 = -2(qe_2+1)(q e_2^2+2q e_2+1)/D^3 < 0`,

`G_22 = -2(qe_1+1)(q e_1^2+2q e_1+1)/D^3 < 0`.

Cross information interaction:

`G_12 = 2(1-q)(q e_1 e_2 - 1)/D^3`.

Thus marginal information values are substitutes when `q e_1 e_2<1`, complements when `q e_1 e_2>1`, and independent at `q=1`. The sign is not interpreted as the paper contribution by itself.

## Concavity

The Hessian of `G` is negative semidefinite at `q=0` and negative definite for `q>0`. Its determinant equals

`4q K / D^5`,

where

`K = q^2 e_1^2 e_2^2 + 2q^2 e_1^2 e_2 + 2q^2 e_1 e_2^2 + 3q^2 e_1e_2 + q e_1^2 + q e_1e_2 + q e_1 + q e_2^2 + q e_2 - q + e_1 + e_2 + 2`.

For `q in [0,1]` and nonnegative efforts, `K>0` because the only negative term is `-q` while `2-q>=1` and every other term is nonnegative.

## Fixed-total-precision lemma

Fix `e_1+e_2=T`. Then the numerator of `L` is fixed and

`D = 1+T+q e_1(T-e_1)`.

For `q>0`, this denominator is uniquely maximized at

`e_1=e_2=T/2`,

so balanced diagnostic precision uniquely minimizes posterior loss. At `q=0`, `D=1+T`, so composition is irrelevant.

This is a primitive information-geometry lemma only. It is not the Stage 4 contribution.

## Endpoint benchmarks

At `q=0`:

`L = 1 + 1/(1+e_1+e_2)`.

Only total scalar precision matters.

At `q=1`:

`L = 1/(1+e_1) + 1/(1+e_2)`,

`G = e_1/(1+e_1) + e_2/(1+e_2)`.

The two diagnostic directions are orthogonal and the learning problem separates by state dimension.
