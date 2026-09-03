# Stage 3-J Model-Level Prior-Art Audit

Search cutoff: 2026-09-03.

This audit compares the mechanism-level architecture rather than titles or applications. `EXACT PRIOR ART` and `STRUCTURALLY VERY CLOSE` require model/proposition-level evidence when accessible.

## A — Rare-Event / Field-Failure Learning

### Strongest threats

1. Keller & Rady (2015), *Breakdowns*, Theoretical Economics — strategic experimentation with an unknown breakdown/failure environment and Poisson learning. Event and non-event histories update beliefs, and players' experimentation incentives depend on future informational value.
2. Keller & Rady (2010), *Strategic Experimentation with Poisson Bandits* — canonical multi-agent Poisson experimentation/free-riding architecture.
3. Bolton & Harris (1999), *Strategic Experimentation* — strategic information-production externality in experimentation.
4. Das, Klein & Schmid (2020) — asymmetric strategic experimentation with explicit equilibrium analysis.
5. Xu & Yang (2026), *Dynamic Pricing With Recommendation and Consumer Feedback*, RAND Journal of Economics — sales raise feedback arrival rates, feedback is good/bad/no-news, and commercial actions respond to and influence learning.

### Mapping

| Dimension | Candidate A | Closest experimentation family |
|---|---|---|
| latent state | safe/defective or failure rate | unknown payoff/failure environment |
| signal | state-dependent Poisson event/no-event | Poisson success/failure/breakdown/no-news |
| information action | monitoring/exposure effort | experimentation/action intensity |
| commercial activity | route exposure/reallocation | risky-action intensity / sales activity |
| posterior | Bayesian | Bayesian |
| continuation decision | redesign/recall/adaptation | continuation/experimentation/pricing |
| strategic feedback | info value affects monitoring | info value affects experimentation |

Direct relabeling/restriction: `PARTIAL`, but the proposed theorem space is strongly absorbed by the existing experimentation logic.

Classification: `STRUCTURALLY VERY CLOSE`.

Disposition: `KILL — IMMEDIATE COROLLARY`.

A new result would need a genuinely vertical appropriation feedback not reproduced by experimentation incentives. No minimal version satisfying the one-object rule was found.

---

## B — Endogenous Customer Selection / Endogenous Sampling

### Strongest threats

1. Acemoglu, Makhdoumi, Malekian & Ozdaglar (2022), *Learning From Reviews: The Selection Effect and the Speed of Learning*, Econometrica — customer purchasing is endogenous to beliefs; the type distribution of reviewers is selected; hence review likelihood depends on the selection rule and beliefs.
2. Hu, Sun, Zheng, Chen & Huang (2021), IJPE — retailer information acquisition/sharing, manufacturer encroachment, manufacturer quality and channel decisions.
3. Guan, Mantrala & Bian (2019), Journal of Retailing — strategic information management in a manufacturer-retailer channel with market-research information and endogenous quality/pricing decisions.
4. Shin & Zeevi (2024), Management Science — product quality, platform information sharing, manufacturer information acquisition and reviews.
5. Yan, Bian, Perera & Guan (2026), POM — review-driven learning with dynamic pricing and post-launch quality refinement.
6. Chen, Du & Lei (2024 online / 2025 issue), Marketing Science — review selection bias and strategic price response.
7. Wang et al. (2019), EJOR — two-period manufacturer-retailer game with reviews, quality and prices.
8. Li & Hitt (2008); Hu, Pavlou & Zhang (2017); later self-selection/review-bias work — selected-review component.

### Whole-game mapping against Acemoglu et al. (2022)

| Dimension | Candidate B | Acemoglu et al. |
|---|---|---|
| strategic downstream intermediary | retailer/dealer chooses commercial screening | absent as separate vertical player |
| customer heterogeneity | yes | yes |
| purchase selection | induced by retailer action and type | endogenous purchase decision |
| selected feedback likelihood | yes | yes |
| rational inference | upstream M conditions on selection rule | consumers learn from reviews |
| upstream adaptation | endogenous post-feedback action | no vertically separate manufacturer adaptation |
| feedback into initial intermediary action | adaptation value changes retailer screening incentives | no same vertical feedback loop |

Direct relabeling/restriction: `NO`.

### Whole-game mapping against Yan et al. (2026)

Yan et al. links review volume, learning, dynamic pricing and quality refinement, but the same firm controls commercial and quality decisions. It does not provide the vertical incentive wedge in which a downstream actor strategically changes the selected sample because it captures only part of an upstream adaptation benefit.

Direct relabeling/restriction: `PARTIAL`.

### Whole-game mapping against Hu et al. (2021)

Hu et al. has a strategic retailer and manufacturer quality/channel decisions, but information is intentionally acquired market research rather than a likelihood endogenously generated by ordinary customer selection. The selected-sample statistical object is absent.

Direct relabeling/restriction: `PARTIAL`.

Classification: strongest papers are `STRUCTURALLY VERY CLOSE` or `COMPONENT OVERLAP`; no verified `EXACT PRIOR ART` to the full loop.

Disposition: `PREFERRED`, but only for Stage-4 hard kill, not novelty certification.

---

## C — Upstream Attention × Downstream Information Acquisition

### Strongest threats

1. Chen & Suen (2023), *Competition for Attention and News Quality*, AEJ: Microeconomics — receiver attention allocation depends on providers' information quality, and providers choose quality anticipating attention; the feedback can produce a downward spiral.
2. Liang, Mu & Syrgkanis (2022), Econometrica — dynamic aggregation/sampling of diverse information sources.
3. Lipnowski, Mathevet & Wei (2020), AER: Insights — attention management and endogenous allocation of limited receiver attention.
4. Argenziano, Severinov & Squintani (2016) — costly information acquisition and communication.
5. Principal-expert costly information acquisition literature.

The intended loop `provider information investment -> receiver attention -> provider return -> information investment` is already explicitly present in the strongest prior.

Direct relabeling/restriction: `YES/PARTIAL` at the strategic-loop level.

Classification: `EXACT PRIOR ART / STRUCTURALLY VERY CLOSE` for the intended architecture family.

Disposition: `KILL — EXACT/WHOLE-GAME PRIOR ART`.

---

## D — Information Obsolescence / Endogenous Regime Relevance

### Strongest threats

1. Keller & Rady (1999), *Optimal Experimentation in a Changing Environment*, Review of Economic Studies — the payoff environment changes randomly, information can become stale, and experimentation trades current return against tracking the changing state; information traps and regime-dependent experimentation arise.
2. Foerster (2022) — learning about unobserved regime changes.
3. Cai (2019) and related dynamic information-acquisition work — time-varying uncertainty and acquisition.
4. Structural-break/change-point learning and stale-information literatures — statistical component.

A minimal one-agent version is already close to changing-environment experimentation. To create a separate downstream strategic interaction requires, at minimum, a regime process, strategic downstream refresh/acquisition and an upstream continuation action. That is too much simultaneous structure for this Stage-3 reboot.

Direct relabeling/restriction: `PARTIAL` for simple versions; a distinct vertical version is not directly absorbed but breaches complexity discipline.

Classification: `STRUCTURALLY VERY CLOSE` plus `COMPONENT OVERLAP`.

Disposition: `KILL — UNCONTROLLED COMPLEXITY`.

---

## Audit verdict

No exact full-game predecessor to B was verified in the inspected literature. A, C and D fail before Stage 4 for prior-art/immediate-corollary/complexity reasons. B alone has enough model-level distance to justify a minimal formal hard kill.