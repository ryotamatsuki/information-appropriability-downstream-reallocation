# Canonical Model Specification

## Players / economic actors

- `M`: upstream producer. It benefits from downstream-generated information through upstream product improvement. It is not an active strategic chooser in the core comparative-static theorem.
- `S`: information-producing downstream node. It chooses costly, noncontractible information effort `e`.
- `R`: alternative downstream route. Its relative activity increases as downstream allocation shifts away from `S`.
- Consumers: explicit only in the welfare benchmark.

## Canonical notation normalization

To avoid collision with the old seminar-paper parameter `s` (a cross-price coefficient), Stage 8 renames the Stage-7 activity weights:

- Stage 7 `s(η)` → canonical `ω_S(η)`;
- Stage 7 `r(η)` → canonical `ω_R(η)`.

## General model

Product improvement:

`x = g(e)`.

Route activity / quantities:

`q_S = ω_S(η) D_S(x)`,

`q_R = ω_R(η) D_R(x)`.

Primitive monotonicities:

- `ω_S'(η) < 0`;
- `ω_R'(η) > 0`;
- `D_S'(x) > 0`;
- `D_R'(x) > 0`;
- `g'(e) > 0`.

In the canonical separable formulation, `D_i`, `g`, `m_S`, `A_S`, and `A_R` have no direct `η` dependence; `η` operates through the route-activity weights.

Effort cost is `C(e)`, with sufficient convexity / objective concavity to yield the claimed unique interior optima.

Private payoff:

`π_S(e,η) = m_S ω_S(η) D_S(g(e)) - C(e)`.

Coordinated benchmark objective:

`J(e,η) = A_S ω_S(η) D_S(g(e)) + A_R ω_R(η) D_R(g(e)) - C(e)`.

## Core friction

**Incomplete appropriability of noncontractibly produced downstream information.**

`S` directly internalizes only the return tied to its own shrinking downstream footprint, while the product-improvement information can create value through the expanding alternative route.

No RRC, foreclosure, strategic wholesale pricing, bargaining, service-utility mechanism, dynamics, uncertainty, or additional players are part of the canonical model.
