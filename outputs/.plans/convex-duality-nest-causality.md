# Literature Review Plan: Convex Duality Inside a Nest as the General Structure of Causality

**Slug:** `convex-duality-nest-causality`
**Date:** 2026-06-17

## Topic

Investigate the claim that **causality**, in problems of prediction, filtering,
control, optimization, and optimal transport, has a common abstract structure:
*convex duality constrained to live inside a nest* (a totally ordered chain of
closed subspaces / σ-algebras / projections). Survey the literature that
either explicitly states or implicitly uses this skeleton.

## Key questions

1. **Operator-algebra side.** What does the nest-algebras literature
   (Ringrose, Arveson, Davidson, Larson, Pitts, Power) say about the
   abstract structure: factorization, interpolation, distance formulae
   inside a nest?
2. **Prediction / filtering side.** Wiener–Hopf, Kolmogorov–Szegő spectral
   factorization, Kalman/innovations representation. Where is the convex-
   duality view stated explicitly, and where is "nest" only implicit
   (filtration)?
3. **Stochastic control & finance.** LQG separation, optimal trading with
   transient impact (Bouchaud–Gatheral, GP13, Lehalle–Neuman, Abi
   Jaber–Neuman), all with adapted controls. Survey explicit convex-duality
   treatments and the role of the filtration as nest.
4. **Adapted optimal transport / causal OT.** Backhoff–Beiglböck–Pammer–
   Schachermayer and follow-ups. Convex (Kantorovich) functional + causal
   constraint = adapted OT. Is this advertised as the same skeleton?
5. **Information theory.** Causal rate–distortion (Tatikonda, Tanaka, Charalambous),
   directed information (Massey, Kramer), sequential / online learning
   (Cesa-Bianchi–Lugosi). Convex duality + filtration constraint.
6. **Convex analysis / Bismut–Pliska / martingale duality.** Bismut's
   duality for adapted controls; the martingale-method duality in
   mathematical finance (Kramkov–Schachermayer, Karatzas–Shreve).
7. **Synthesizing references.** Are there any explicit programmatic
   statements of "convex duality on a nest" as a single research program?
   Maybe Hannan, Masani, Helson, Lowdenslager (multivariate prediction);
   maybe more recent operator-theoretic literature.

## Source types

- Foundational papers: Wiener–Hopf 1931, Kolmogorov 1941, Szegő 1921,
  Kalman 1960, Kailath 1968, Ringrose 1965, Arveson 1967/1975.
- Books: Davidson *Nest Algebras* 1988; Pourahmadi *Foundations of
  Time Series Analysis and Prediction Theory* 2001; Helson *Lectures on
  Invariant Subspaces*; Hida *Brownian Motion*.
- Modern operator-algebra: Pitts, Larson, Power, Solel — survey papers
  on nest algebras and their generalizations (CSL, free nest, subalgebras).
- Modern stochastic control / finance: Lehalle–Neuman 2019, Abi
  Jaber–Neuman 2022, Abi Jaber–Neuman–Tuschmann 2024, Cardaliaguet–
  Lehalle 2018.
- Adapted OT: Backhoff–Beiglböck–Pammer–Zalashko 2017+.
- Causal info theory: Tatikonda–Mitter 2009, Tanaka et al., Kramer 2003.
- Web search for recent surveys (2020–2026) that may state the unifying
  view.

## Expected sections of the final review

1. Introduction & framing
2. The abstract skeleton (Hilbert space + nest + convex functional)
3. Nest algebras and operator-theoretic factorization
4. Prediction & filtering: Wiener–Hopf, Kolmogorov–Szegő, Kalman
5. Stochastic control & optimal trading
6. Adapted / causal optimal transport
7. Causal information theory & online optimization
8. Convex duality in mathematical finance (martingale duality)
9. What unifies, what doesn't (taxonomy)
10. Open questions

## Task ledger

- [ ] T1 — alpha + web search: nest algebras + convex factorization
- [ ] T2 — alpha + web search: Wiener–Hopf / Kolmogorov–Szegő modern surveys
- [ ] T3 — alpha + web search: Kalman / innovations / Cholesky-as-WH
- [ ] T4 — alpha + web search: optimal trading + adapted controls
- [ ] T5 — alpha + web search: adapted/causal optimal transport
- [ ] T6 — alpha + web search: causal rate–distortion / directed information
- [ ] T7 — alpha + web search: martingale duality in math finance
- [ ] T8 — Delegate the wide T1–T7 sweep to `researcher` subagent
- [ ] T9 — Synthesize, draft to `outputs/.drafts/<slug>-draft.md`
- [ ] T10 — Run `reviewer` for citation/URL verification pass
- [ ] T11 — Run `reviewer` for review pass (unsupported claims, gaps)
- [ ] T12 — Fix FATAL issues, optional second verification pass
- [ ] T13 — Save `outputs/<slug>.md` and `outputs/<slug>.provenance.md`

## Verification log (running)

- (empty — populated during execution)

## Risks & blockers

- "Convex duality on a nest" is not a standard named programme.
  Most sources will be implicit. Risk of over-claiming a unifying narrative.
  Mitigation: explicitly mark synthesized framing as the reviewer's
  interpretation, not a stated programme.
- Nest-algebra literature (Arveson, Davidson, Pitts) is technical and
  may be paywalled. Mitigation: cite chapters in Davidson's book and
  the original Arveson JFA paper, and use survey articles where possible.
