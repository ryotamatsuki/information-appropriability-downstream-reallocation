# Belief Deletion Tests

For every candidate, posterior beliefs were replaced by (A) the true state observed publicly, (B) a fixed public score, or (C) a deterministic endogenous state following an analogous transition.

| Candidate | Public-state / deterministic-state replacement | Does intended theorem class survive? | Belief verdict |
|---|---|---:|---|
| K1 | public performance score drives allocation | YES | FAIL |
| K2 | reporting loses meaning if state is public | NO | PASS, but prior art binds |
| K3 | deterministic controlled state `x_{t+1}=G(x_t,a,e)` | YES | FAIL |
| K4 | deterministic data/productivity/capability stock | YES | FAIL |
| K5 | delegation-information problem changes if state is public | NO | PASS, but prior art binds |
| K6 | deterministic capability/relationship stock determines organization | YES | FAIL |
| K7 | deterministic project-quality/success state and R&D race | YES | FAIL |
| K8 | reputation/unknown competence is central | NO | PASS, but prior art binds |

## Key finding

K3 and K6 appeared promising because posterior beliefs could change current strategic actions and those actions could affect future observations. But this is not sufficient. Their proposed theorem classes—investment complementarity, organization traps, organizational-choice reversals—can be generated when the posterior is replaced by an endogenous physical/capability state.

The belief state therefore changes interpretation and transition semantics, but not the relevant best-response topology.

## What would have been sufficient

A survivor would need a result that specifically uses a Bayesian property such as:

- likelihood-ratio updating causing a best-response sign change that cannot be implemented by a deterministic state;
- posterior martingale restrictions interacting with strategic actions;
- inference about another strategic player's private information altering that player's future behavior;
- endogenous informativeness changing not merely the level but the strategic cross-derivative structure.

No K1–K8 candidate produced such a theorem before model construction without adding extra primitives.