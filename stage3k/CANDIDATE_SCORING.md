# Candidate Scoring

Weights were fixed before final ranking:

| Dimension | Weight |
|---|---:|
| Strong generic-replacement survival | 20 |
| Player-essentiality | 20 |
| Belief-state essentiality | 15 |
| Proposition-level novelty | 15 |
| Whole-game prior-art survival | 10 |
| Strategic-feedback integrity | 10 |
| Tractability | 5 |
| Welfare content | 3 |
| Institutional/empirical relevance | 2 |

Total = 100.

Automatic caps were applied exactly as specified by the Stage 3-K prompt.

| ID | Raw score before cap | Binding cap | Final score | Final verdict |
|---|---:|---:|---:|---|
| K1 | 48 | 25 — generic contest replacement | 25 | KILL — STRONG GENERIC REPLACEMENT |
| K2 | 63 | 30 — whole-game prior-art family | 30 | KILL — EXACT/WHOLE-GAME PRIOR ART |
| K3 | 68 | 25 — strong deterministic-state replacement | 25 | KILL — STRONG GENERIC REPLACEMENT |
| K4 | 56 | 25 — generic data/productivity replacement | 25 | KILL — STRONG GENERIC REPLACEMENT |
| K5 | 67 | 30 — delegation-learning prior art | 30 | KILL — EXACT/WHOLE-GAME PRIOR ART |
| K6 | 72 | 25 — belief not essential / generic organizational-investment analogue | 25 | KILL — BELIEF NOT ESSENTIAL |
| K7 | 58 | 25 — R&D/contest replacement | 25 | KILL — STRONG GENERIC REPLACEMENT |
| K8 | 70 | 30 — extremely close 2026 prior | 30 | KILL — EXACT/WHOLE-GAME PRIOR ART |

## Ranking logic

Raw scores are informative only for deciding which failed architectures deserved deeper inspection. They do not override the hard gates.

Initial TOP 3 by research promise before binding caps:

1. K6 — Integration / Channel Organization × Information Production
2. K8 — Reliability / Reputation Learning × Endogenous Reliance
3. K3 — Upstream Action Changes Future Signal Technology

After model-level prior-art inspection, K8 was removed because Lukyanov–Vlasova (2026) is too close. K2 was examined as the communication alternative but also failed prior-art distance.

Deep-dive TOP 2:

1. K6
2. K3

Both fail the strong generic / compression gates.

Preferred candidate: **NONE**.

No `STAGE4_CONTRACT.md` is created.