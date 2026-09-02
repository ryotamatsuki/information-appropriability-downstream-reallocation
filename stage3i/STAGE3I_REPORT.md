# Stage 3-I — Information-Specific Mechanism Architecture Reboot

Date: 2026-09-03

Starting canonical main: `58254d07eb40fe3afb6f9b42d0aee2f9541e9ec9`

Workflow: `research-paper-workflow` v1.1 @ `488e5ab06c207909296a7564eaf9066f7f94319c`

Template: `templates/STAGE_03_MECHANISM_SEARCH.md` @ `bf389fbb82254d9cc4d7aee068a12f81a90bdf5d`

## Canonical precondition

PR #5, Stage 6-R, is merged. Merge SHA: `58254d07eb40fe3afb6f9b42d0aee2f9541e9ec9`. Stage 6-R HEAD `81d29d9b8dec0297ac072bb1bfd9f783fd35e70e` had successful CI run `33686219447`.

No open PR and no pre-existing Stage 3/reboot branch was found at Stage 3-I start.

## Binding diagnosed deficiency

> The current model treats information as a monotone effort-generated common input but gives information no independent strategic state or response margin, so after label stripping the core game collapses to established cross-channel effort free riding and its private/system incentive wedge.

The old static architecture and P1–P4 contribution claims remain killed. Stage 3-I does not edit Stage 8, the stale manuscript, Stage 11, or Stage 6-R.

## Research question

What formal property of downstream-generated information creates equilibrium economics that ordinary costly sales/service effort cannot reproduce?

## Candidate search

Ten architecture families were hard-killed:

A. Persistent reusable information stock
B. Endogenous upstream adoption / implementation
C. Information ownership / access rights
D. Information portability under reallocation
E. Information acquisition versus disclosure
F. Bayesian precision / endogenous learning
G. Competing information producers
H. Diagnostic / informational diversity
I. Intertemporal appropriability / post-exit reuse
J. Retention for learning option value

The search used application-language, mechanism-stripped, and result/architecture queries for every family, spanning information economics, vertical relations, innovation, data economics, organizational learning, and dynamic experimentation.

## Executive verdict

Eight candidates fail before Stage 4. The main reasons are direct prior-art absorption or reduction to generic costly investment / information acquisition.

- A: KILL — persistence alone is a generic dynamic-stock extension and is strongly threatened by dynamic data/learning-asset work and service carry-over models.
- B: KILL — retailer information acquisition followed by an upstream product-quality response is already present in Hu et al. (2021), with broader vertical innovation precedents.
- C: KILL — data ownership/access and investment incentives are established by Jones–Tonetti and more directly by 2026 learning-asset work.
- D: KILL — Li–Zhang (2026, IJIO) directly models data portability changing ex-ante data collection incentives; Wang–Wang (2026) additionally treats post-exit continuity.
- E: KILL — Guo–Iyer and the 2026 vertical/horizontal acquisition-disclosure literature already solve the acquisition/sharing interaction.
- F: KILL — endogenous signal precision and upstream action are mature costly-information-acquisition objects.
- G: KILL — multiple downstream signal holders, correlated signals, acquisition/sharing and network information externalities already have close full models; the proposed version did not isolate a distinct result separate from H.
- I: KILL — post-exit reuse is directly threatened by the 2026 residual-control/learning-asset model and standard relationship-specific investment logic.

Two candidates survive to ranking:

1. H — **Diagnostic diversity under downstream concentration**.
2. J — **Retention for learning option value**.

Only H is selected as `PREFERRED`.

## Preferred architecture: H — Diagnostic diversity under downstream concentration

### Information-specific formal object

A multidimensional unknown product/problem state `theta` and downstream signals with distinct diagnostic loadings.

A minimal Gaussian representation is:

`theta ~ N(0, Sigma_0)`

`y_i = h_i' theta + epsilon_i`,

with signal precision increasing in downstream information effort/contact intensity.

The posterior precision matrix is

`P = Sigma_0^{-1} + sum_i tau_i h_i h_i'`.

The upstream producer chooses a product/design response after observing the signals. Under quadratic design loss, expected residual loss is proportional to `tr(P^{-1})`.

### New strategic arrow

`downstream reallocation -> source-specific information effort/exposure -> posterior precision matrix -> upstream design response -> downstream return -> information effort`.

This arrow is absent from the failed scalar free-riding architecture.

### Why information is essential

With heterogeneous diagnostic loadings, the economic value of a source depends on the direction of information it adds relative to the existing posterior. The marginal information value is not a scalar route benefit. Under quadratic loss,

`- d tr(P^{-1}) / d tau_i = h_i' P^{-2} h_i`.

Thus two sources with the same amount of effort can have very different marginal values depending on redundancy/complementarity.

Replacing `y_i` with ordinary sales/service effort removes the posterior, signal loading, covariance/rank and Bayesian design response. The same game no longer exists.

### Minimal nonmechanical observation

With a two-dimensional state, orthogonal signal loadings and fixed total precision `T`, posterior loss contains terms of the form

`1/(1+tau_1) + 1/(1+tau_2)`.

For `tau_1 + tau_2 = T`, balanced precision strictly dominates complete concentration for `T>0`. This is not yet the paper's contribution; it is the primitive diagnostic-complementarity force to be embedded in decentralized information effort and downstream reallocation at Stage 4.

The Stage 4 contribution must come from the interaction between this information geometry and private appropriation/reallocation—not from the convexity fact by itself.

### Candidate propositions for Stage 4 hard kill

P1. There can be an admissible region in which downstream reallocation toward one node increases aggregate information effort/observations but worsens upstream design accuracy because unique diagnostic coverage is lost.

P2. A low-volume downstream node can have positive system retention value solely because its signal is diagnostically complementary, even when its standalone commercial contribution is below its retention cost; this retention region must collapse when signals become collinear/redundant.

P3. The welfare effect of downstream concentration can change sign with signal redundancy/correlation: concentration is less costly, and may be efficient, when sources are sufficiently redundant, but is inefficient when the disappearing source spans a sufficiently distinct diagnostic direction.

These are conjectures to kill-test, not verified theorems.

## Closest prior-art threats to H

- Xiong, Li & Lang (2025), *Games and Economic Behavior*, “Pricing and information acquisition in networks”: a monopolist chooses information acquisition from networked consumers with correlated preferences; correlation changes optimal target-group size. Strong component-level threat, but no downstream intermediary effort/appropriation and no upstream product-design response to a vector of dealer-generated diagnostics.
- Myatt & Wallace (2019), *Journal of Economic Theory*, “Information acquisition and use by networked players”: costly signals differ in clarity/correlation and strategic network interactions affect acquisition/use. Strong information-geometry threat; different players/objectives and no vertical reallocation/product-design game.
- Migrow & Squintani (2023), *JPE Micro*, “The Design of Information Acquisition and Sharing”: correlated information acquisition/sharing in multidivisional organizations. Strong incentive-design component overlap, but not downstream reallocation into an upstream design problem.
- Board & Meyer-ter-Vehn (2024), *AER*, “Experimentation in Networks”: network density crowds out experimentation and total information can fall. Dynamic learning/network threat; different feedback network.
- Gao, Xie & Zhou (2015), *Journal of Operations Management*: supplier-network technological diversity is empirically associated with novel information sharing and buyer innovation. Institutional/empirical overlap, not a solved theory game.

No single inspected paper was found that reproduces the proposed H full game by relabeling/normalization. This is not proof of novelty; it is sufficient only for a Stage 3 `GO TO MINIMAL MODEL`, subject to Stage 4 and later novelty re-kill.

## Runner-up: J — Retention for learning option value

J passes the information-essentiality and Anti-Xu tests because uncertainty and future signal arrival create an experimentation option absent from sales/service effort. However, it requires a dynamic stopping/retention problem in addition to learning and is strongly threatened by the strategic experimentation literature, including Board–Meyer-ter-Vehn (2024) and Gieczewski–Kosterina (2024). It is less minimal and more referee-vulnerable than H.

J is retained as a recorded alternative, not sent to Stage 4.

## Institutional plausibility

Primary-source evidence supports the factual premise that downstream/field networks generate diagnostically useful information for product improvement. Toyota documents systems that route customer/dealer feedback and field information into design, engineering and quality functions, including regional technology offices and rapid field investigation. Caterpillar's 2026 field-follow role explicitly links telemetry, dealer/customer feedback, engineering and product teams. Bosch field-data guidance describes using field failures to estimate reliability and derive design changes. These sources support plausibility only; they do not establish theoretical novelty.

## Canonical Stage 3-I verdict

`GO`

Routing:

`GO TO STAGE 4 — MINIMAL MODEL`

Preferred candidate:

`H — Diagnostic diversity under downstream concentration`

## Stage 4 contract summary

Stage 4 must solve one minimal two-node Gaussian-quadratic information game and its mechanism-off benchmark. It must not add ownership, bargaining, disclosure, dynamics, endogenous entry, contracts, or additional firms.

Primary hard-kill condition:

If the headline reallocation/retention result survives essentially unchanged when `h_1 = h_2` (diagnostic diversity switched off), or if a scalar generic effort/free-riding benchmark can reproduce it, terminate H.

Stage 12 remains unauthorized.