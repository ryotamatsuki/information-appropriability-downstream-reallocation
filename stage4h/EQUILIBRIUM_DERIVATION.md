# Stage 4-H — Equilibrium Derivation

Private FOCs for interior `eta in (0,1)` are

`k_1 e_1 = b(1-eta) G_1`,

`k_2 e_2 = b eta G_2`.

Because `G_i>0`, every interior-eta equilibrium has strictly positive efforts.

## Weighted potential and uniqueness

The game has weighted potential

`Psi = G - k_1 e_1^2/[2b(1-eta)] - k_2 e_2^2/[2b eta]`.

Each player's FOC is a positive multiple of the corresponding potential FOC. `G` is concave and the quadratic terms are strictly concave; hence `Psi` is strictly concave for `eta in (0,1)`. Therefore the Nash equilibrium exists and is unique. At `eta=0` or `1`, the node with zero appropriability chooses zero effort and the remaining one-dimensional problem is unique.

For general `q`, define the FOC residuals

`F_i = k_i e_i - b nu_i G_i`.

The implicit derivative is

`e_eta = - J_F^{-1} F_eta`,

with

`F_eta=(b G_1,-b G_2)'`.

This exact characterization is used for numerical counterexample search; no numerical derivative is treated as proof.

## Mechanism-off benchmark: q=0

Let `E=e_1+e_2`. Then

`G=E/(1+E)` and `G_1=G_2=1/(1+E)^2`.

Set

`A(eta)=b[(1-eta)/k_1 + eta/k_2]`.

The unique equilibrium obeys

`E(1+E)^2=A(eta)`,

`e_1=[b(1-eta)/k_1]/(1+E)^2`,

`e_2=[b eta/k_2]/(1+E)^2`.

Hence

`E_eta = b(1/k_2-1/k_1)/[(1+E)(1+3E)]`.

Posterior loss is

`L=1+1/(1+E)`,

so

`L_eta = - E_eta/(1+E)^2`.

Therefore in the scalar/redundant benchmark **total effort and design loss can never rise together**. If reallocation raises total effort, it strictly improves design accuracy.

## Orthogonal benchmark: q=1

The game separates:

`e_1(1+e_1)^2 = b(1-eta)/k_1`,

`e_2(1+e_2)^2 = b eta/k_2`.

Define

`a_1 = (b/k_1)/[(1+e_1)(1+3e_1)]`,

`a_2 = (b/k_2)/[(1+e_2)(1+3e_2)]`.

Then

`e_1,eta = -a_1`,

`e_2,eta = a_2`,

`E_eta = a_2-a_1`,

and

`L_eta = a_1/(1+e_1)^2 - a_2/(1+e_2)^2`.

### Proposition H-P1 — Volume/diversity divergence

At `q=1`, reallocation toward node 2 raises total equilibrium precision while worsening design accuracy iff

`1 < a_2/a_1 < [(1+e_2)/(1+e_1)]^2`.

This is an exact necessary-and-sufficient local condition at an interior equilibrium.

### Exact nonempty-region witness

Take

`b=1`, `eta=3/5`, `e_1=1/6`, `e_2=1/3`,

`k_1=432/245`, `k_2=81/80`.

The two FOCs hold exactly. Moreover

`a_1=35/108`, `a_2=10/27`,

so

`a_2/a_1=8/7`,

while

`[(1+e_2)/(1+e_1)]^2=64/49`.

Thus the strict H-P1 condition holds. Exactly,

`d(e_1+e_2)/deta = 5/108 > 0`,

and

`dL/deta = 5/168 > 0`.

Because the inequalities are strict and the unique equilibrium varies continuously with primitives, H-P1 holds on an open, positive-measure neighborhood of this witness.

For the same `b,k_1,k_2,eta` at `q=0`, `k_2<k_1` implies `E_eta>0` but the mechanism-off identity forces `L_eta<0`. Therefore the headline divergence disappears and reverses when diagnostic diversity is switched off.

## Diagnostic-redundancy sign switch

For the exact witness above, equilibrium and its local derivatives are continuous in `q`. Since `L_eta<0` at `q=0` and `L_eta>0` at `q=1`, at least one interior `q* in (0,1)` satisfies `L_eta=0`. A numerical diagnostic locates one crossing at approximately

`q*=0.6595906712`, equivalent to `phi*=54.3067 degrees`.

The existence of a crossing follows analytically by continuity; the numerical value is not claimed as a closed-form theorem or unique threshold.
