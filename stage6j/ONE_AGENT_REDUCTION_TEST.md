# One-Agent Reduction Test — Stage 6-J

## Frozen vertical representation

Stage 4-J describes:

1. retailer chooses screening cutoff `c`;
2. selected customers generate feedback;
3. manufacturer updates rationally;
4. manufacturer chooses posterior-mean adaptation;
5. retailer receives fraction `ρ` of the adaptation benefit.

After solving the manufacturer's quadratic-loss decision, the full continuation value available to the retailer is summarized by the scalar Bayes-risk reduction `I(c)`.

The retailer therefore solves

\[
\max_c\; c(1-c)+\delta\rho I(c).
\]

## Remove the manufacturer

Delete the upstream player entirely. Give a single selector direct continuation utility `δρI(c)` from the value of the selected experiment:

\[
\max_c\; c(1-c)+\delta\rho I(c).
\]

The optimization problem is literally identical.

Nothing changes in:

- FOC;
- SOC;
- equilibrium `c*`;
- exact witness;
- `dc*/dρ`;
- fixed-likelihood benchmark;
- B-P1 sign reversal.

## Strategic-substance test

The manufacturer does not choose an action that feeds strategically back to information production beyond the already-integrated scalar value of correct adaptation. Its posterior-mean action is a unique mechanical best response conditional on information. Once expected loss reduction is calculated, no distinct manufacturer strategy remains in the retailer's equilibrium problem.

Therefore:

\[
\boxed{\text{B-P1 does not require M–R strategic interaction.}}
\]

The separate manufacturer is institutionally meaningful, but not theorem-essential.

## Consequence for novelty

B-P1 cannot be defended as a new vertical-interaction theorem. At most it could survive as a one-agent endogenous-information-selection theorem.

But the stronger generic quantity-quality test then removes information as well: replace `I(c)` with deterministic continuation output `Q(c)=κt²c²(1-c)` and the theorem remains unchanged.

Hence neither Route A nor Route B from the Stage 6-J survival standard survives:

- Route A (new endogenous-information theorem): fails generic non-information reproduction.
- Route B (genuinely vertical interaction): fails exact one-agent reduction.

## Verdict

\[
\boxed{\textbf{FAIL — ONE-AGENT REDUCTION EXACT}}
\]

Upstream M is **not strategically substantive for B-P1**.
