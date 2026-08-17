# Provenance — unified-trading-execution.md

**Date:** 2026-06-27
**Reviewer trigger:** §5.4 W–H scope concern in
`papers/fractional-derivative-optimal-execution.md` (reviewer round 1,
finance/finance M3).

## Sources cited and verification status

| # | Source | URL / ID | Verified | Note |
|---|---|---|---|---|
| 1 | Abi Jaber & Neuman 2022, *Optimal Liquidation with Signals: General Propagator* | arXiv:2211.00447; DOI 10.1111/mafi.12465 | abstract retrieved via `alpha_get_paper`, web search confirms | execution-only precursor; stochastic Fredholm |
| 2 | Abi Jaber, Neuman & Tuschmann 2024, *Optimal Portfolio Choice with Cross-Impact Propagators* | arXiv:2403.10273 | abstract retrieved via `alpha_get_paper`; "we provide an implementation of the solutions to the optimal portfolio choice problem **and to the associated optimal execution problem**" confirmed verbatim | **strongest unified treatment**; matrix Volterra propagator |
| 3 | Bouchard, Fukasawa, Herdegen & Muhle-Karbe 2018, *Equilibrium Returns with Transaction Costs* | arXiv:1707.08464; HAL hal-01569408v3 | web search abstract confirmed | equilibrium FBSDE; quadratic TC |
| 4 | Cartea, Jaimungal & Penalva 2015, *Algorithmic and High-Frequency Trading* | Cambridge UP ISBN 978-1-107-09114-6 | publisher page confirmed via web | textbook; HJB unification |
| 5 | Forsyth, Kennedy, Tse & Windcliff 2012, *Optimal trade execution: a mean-quadratic-variation approach* | DOI link via ScienceDirect | abstract confirmed via web | MQV reformulation |
| 6 | Gârleanu & Pedersen 2013, *Dynamic Trading with Predictable Returns and Transaction Costs* | DOI 10.1111/jofi.12080 | DOI page confirmed | linear-quadratic, multi-signal; "aim portfolio" |
| 7 | Gârleanu & Pedersen 2016, *Dynamic Portfolio Choice with Frictions* | https://nbgarleanu.github.io/DynamicPortfolioChoiceWithFrictions.pdf | author's site PDF; abstract confirmed | transitory + persistent costs; continuous-time limit |
| 8 | Moreau, Muhle-Karbe & Soner 2017, *Trading with Small Price Impact* | Math. Finance 27(2); arXiv:1402.5304; DOI 10.1111/mafi.12098 | abstract confirmed via web | small-impact asymptotic; execution/portfolio link |
| 9 | Webster 2023, *Handbook of Price Impact Modeling* | DOI 10.1201/9781003316923; CRC Press | publisher page + author site confirmed | practitioner unified treatment |

## Indirect / cited-in-passing (not central to the synthesis)

- Almgren & Chriss 2000/2001 — standard execution reference.
- Obizhaeva & Wang 2013, J. Financial Markets 16 — exponential-resilience execution.
- Gatheral, Schied & Slynko 2012 — Fredholm execution with general kernel.
- Forde, Sánchez-Betancourt & Smith 2022, Quant. Finance 22 — Gaussian Volterra signal + power-law execution.
- Neuman & Voß 2020, arXiv:2002.09549 — temporary + transient execution.
- Benzaquen et al. 2017; Mastromatteo et al. arXiv:1702.03838 *Trading Lightly* — cross-impact execution.
- Collin-Dufresne, Daniel & Sağlam 2014 — GP-style portfolio with multiple signals.
- Bertsimas & Lo 1998 — execution origin.
- Lorenz & Almgren 2011 — adaptive execution.

## Searches performed

1. `alpha_search` mode=both, query: "Unified framework optimal portfolio trading and execution with price impact, predictable signals, terminal inventory constraint and stationary signal-tracking limit" → 0 hits (alpha index sparse on this exact angle).
2. `web_search` × 3 queries on portfolio + execution + TC unification → GP 2013/2016, *Trading Lightly*, Wiley/NBER copies, *Equilibrium Returns*, *Trading with Small Price Impact*.
3. `web_search` × 4 queries on Moreau–Muhle-Karbe–Soner; on Volterra propagator stochastic control; on AJN/AJNT; on Cartea–Jaimungal book → all confirmed.
4. `web_search` × 3 queries on Webster handbook, AJNT 2024 details, Forsyth MQV → all confirmed.
5. `alpha_get_paper 2403.10273` section=abstract → abstract text retrieved verbatim, supporting the central "unified" claim.

## Limitations / caveats

- No direct full-text inspection of the Gârleanu–Pedersen 2016 paper
  beyond the public PDF abstract; the claim that the "persistent cost"
  in GP 2016 is structurally identical to an exponential propagator is
  based on the abstract + author summary + my prior knowledge of the
  paper, not a full-text re-read in this session.
- No full-text inspection of Cartea–Jaimungal–Penalva 2015; the
  unification claim is based on the publisher's chapter list and
  standard knowledge.
- Abi Jaber–Neuman–Tuschmann 2024 was confirmed only via abstract;
  the specific claim about how their resolvent framework specializes
  to both portfolio choice and execution rests on their own abstract
  language ("optimal portfolio choice problem **and to the associated
  optimal execution problem**") and §4 / §5 of the paper, which the
  user should verify before citing in a publication-ready version.
- The meta-cost-functional in §3 of the artifact is synthetic
  (Feynman's framing), not lifted from any single paper. It is intended
  as a pedagogical organizing device, not a literal published equation.
- The Webster handbook is a practitioner book; specific page or
  chapter citations would require physical or licensed access.

## What is NOT in this review

- Reinforcement-learning unifications (e.g. Cartea–Jaimungal RL papers,
  Jaimungal & Wang). Out of scope for the structural-unification angle.
- Singular-control / impulse-control unifications under proportional or
  fixed costs (Kallsen–Muhle-Karbe, Bichuch–Shreve). Different cost
  structure than the quadratic / propagator setting.
- Game-theoretic / multi-agent unifications beyond Bouchard et al. 2018.
- Robust / model-uncertain unifications (Glasserman–Xu, Bayraktar–
  Cohen). Adjacent but separate research program.

## Files

- `outputs/unified-trading-execution.md` — main review (verified on disk).
- `outputs/unified-trading-execution.provenance.md` — this file.
- `outputs/.plans/unified-trading-execution.md` — plan.
