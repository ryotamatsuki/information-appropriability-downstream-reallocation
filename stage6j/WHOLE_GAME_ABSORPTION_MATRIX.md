# Whole-Game Absorption Matrix — Stage 6-J

## Stage 4-J game

- selector: retailer chooses cutoff `c`;
- heterogeneous latent participant type `z`;
- purchase iff `z>=c`;
- selected type emits state-dependent feedback;
- manufacturer observes `c,y` but not `z`;
- selected-mixture likelihood varies with `c`;
- manufacturer Bayesian-updates and chooses adaptation;
- retailer receives continuation stake `ρ` in adaptation value;
- equilibrium cutoff `c*(ρ)`;
- headline B-P1: `dc*/dρ>0` versus fixed-likelihood `dc_F*/dρ<0`.

| Dimension | Acemoglu et al. | Chen–Du–Lei | Yan et al. | Hu et al. 2021 |
|---|---|---|---|---|
| Strategic selector | consumer endogenous purchase, not separate seller cutoff | seller price | same firm price/quality | retailer information acquisition/sharing |
| Heterogeneous participant type | YES | YES / review selection | consumer heterogeneity/review metrics | consumer preference uncertainty |
| Participation threshold | endogenous consumer behavior | price-induced | sales/pricing | no commercial selected-sample cutoff |
| Selected-sample likelihood | YES | YES / selection bias | volume/valence learning | NO |
| Type latent to updater | selection effect yes | selection-bias mechanism | not B-P1 object | NO comparable object |
| Bayesian updater | future consumers/platform learning | consumers infer seller quality | firm + consumers update | manufacturer uses acquired info |
| Separate later action | no separate upstream adapter | price signaling / market decisions | quality refinement + later price | manufacturer quality/sales |
| Selector continuation stake parameter | NO | NO exact analogue verified | intrinsic same-firm continuation value | retailer strategic payoff but not B-P1 `ρ` |
| `dc*/dρ>0` | NO | NO verified | price can move either direction, but not same comparative static | NO |
| fixed-likelihood opposite-sign benchmark | NO | NO verified | NO verified | NO |
| Direct relabel to B-P1 | NO | PARTIAL | PARTIAL | PARTIAL |

## Whole-game verdict

**NO SINGLE-PAPER WHOLE-GAME ABSORPTION VERIFIED.**

However, whole-game non-absorption does not save the theorem because the proved vertical game is reducible before prior-art comparison:

1. the manufacturer can be integrated out exactly into `I(c)`;
2. a one-agent selector obtains the same theorem;
3. a deterministic quantity-quality continuation output `Q(c)=κt²c²(1-c)` reproduces the same theorem and benchmark reversal.

Thus the economically operative whole game is smaller than its institutional representation.

## Direct-relabelling answer

- To a single inspected prior paper: **NO**.
- To a generic one-agent quantity-quality selection problem: **YES, EXACTLY**.

This latter mapping is the binding Stage 6-J absorption result.
