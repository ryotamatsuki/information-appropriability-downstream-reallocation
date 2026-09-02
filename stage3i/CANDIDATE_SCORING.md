# Stage 3-I — Candidate Scoring

## Ex-ante weights

| Dimension | Weight |
|---|---:|
| Proposition-level novelty | 25 |
| Information essentiality | 20 |
| Whole-game prior-art survival | 20 |
| Mechanism clarity | 10 |
| Minimal-model tractability | 10 |
| Welfare content | 5 |
| Institutional plausibility | 5 |
| Empirical bridge / testability | 3 |
| Journal-family relevance | 2 |
| **Total** | **100** |

Weights were fixed before final candidate ranking.

## Automatic caps

- fails service-effort replacement: maximum 40;
- close paper whole-game absorption: maximum 35;
- no independent theorem predicted: maximum 50;
- requires 3+ unrelated new ingredients: maximum 45.

## Scores

| Candidate | Novelty 25 | Info essentiality 20 | Prior-art survival 20 | Clarity 10 | Tractability 10 | Welfare 5 | Institution 5 | Empirical 3 | Journal 2 | Raw | Cap | Final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| A Persistent stock | 8 | 6 | 5 | 8 | 8 | 4 | 4 | 2 | 1 | 46 | generic-effort cap 40 + close-prior cap 35 | **35** |
| B Upstream adoption | 8 | 9 | 5 | 8 | 8 | 4 | 4 | 2 | 2 | 50 | close-prior cap 35 | **35** |
| C Ownership/access | 8 | 16 | 4 | 8 | 6 | 5 | 5 | 3 | 2 | 57 | close-prior cap 35 | **33** |
| D Portability | 6 | 17 | 3 | 9 | 8 | 5 | 5 | 3 | 2 | 58 | close-prior cap 35 | **32** |
| E Acquisition/disclosure | 5 | 18 | 2 | 8 | 8 | 5 | 4 | 2 | 2 | 54 | close-prior cap 35 | **30** |
| F Bayesian precision | 7 | 19 | 3 | 8 | 9 | 4 | 4 | 3 | 2 | 59 | close-prior cap 35 | **34** |
| G Competing producers | 8 | 13 | 5 | 7 | 6 | 4 | 4 | 3 | 2 | 52 | close-prior cap 35 | **35** |
| H Diagnostic diversity | 22 | 20 | 16 | 9 | 8 | 4 | 5 | 3 | 2 | **89** | none; conservative prior-art discount | **83** |
| I Post-exit reuse | 5 | 10 | 3 | 8 | 6 | 5 | 5 | 3 | 2 | 47 | close-prior/generic specific-investment caps | **30** |
| J Learning option retention | 18 | 20 | 13 | 8 | 5 | 5 | 5 | 3 | 2 | **79** | no formal automatic cap; dynamic-complexity/prior risk discount | **68** |

## Interpretation

### H — 83/100

H receives the highest score because the information object is indispensable to the game: the value of a source depends on its loading relative to the existing posterior, not simply the scalar amount of effort. The closest literatures contain correlated signals, information-acquisition design and experimentation, but no inspected single paper reproduces the full vertical downstream-reallocation / source-effort / multidimensional-diagnostic / upstream-design loop.

The 6-point discount from raw score reflects serious adjacent prior art and the fact that Stage 3 has not yet proved any new proposition.

### J — 68/100

J is genuinely information-specific and survives Xu, but needs at least uncertainty, dynamic learning and an endogenous retention/stopping margin. It also faces Board–Meyer-ter-Vehn and Gieczewski–Kosterina as strong experimentation/organization threats. It is retained only as a runner-up.

### Why no third candidate

The next numerical score is G, but its only plausible information-specific distinction is signal heterogeneity/correlation, which is the H architecture. Promoting G separately would violate the requirement that TOP candidates be genuinely different mechanism families. A weaker third candidate is therefore intentionally not selected.

## Ranking

1. `H — Diagnostic / informational diversity` — **83 — PREFERRED**
2. `J — Retention for learning option value` — **68 — TOP 3 / runner-up**
3. none promoted

All other candidates: `KILL`.