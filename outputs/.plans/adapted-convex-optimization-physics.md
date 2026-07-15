# Literature Review Plan: Adapted Convex Optimization and Physics

**Slug:** `adapted-convex-optimization-physics`
**Date:** 2026-06-17

## Topic

Survey the relation between the **adapted convex optimization** framework
discussed in prior work (`papers/adapted-convex-duality.md`,
`outputs/convex-duality-nest-causality.md`) — i.e., minimize a convex
functional on a Hilbert space subject to a nest/filtration constraint,
with the constructive solution requiring outer / Cholesky / Wiener–Hopf
factorization inside the nest algebra — and **physics**.

Where does this skeleton appear, explicitly or implicitly, in physics?

## Key questions

1. **Causality and dispersion relations.** Kramers (1927), Kronig (1926),
   Titchmarsh's theorem, Toll 1956. Causal linear response ⇔ Hardy-space
   analyticity in upper half plane ⇔ Hilbert transform relation between
   Re and Im of susceptibility. Is this *the same* spectral factorization
   that appears in Wiener–Hopf? Is "outer function" the right operator-
   theoretic identification of a causal passive susceptibility?
2. **Linear response & fluctuation–dissipation.** Kubo 1957, Callen–
   Welton 1951. The FDT relates dissipative response (imaginary part) to
   equilibrium fluctuations. Is the underlying object a quadratic convex
   form on adapted noise paths, with outer factor = causal impulse
   response?
3. **Wiener–Hopf in physics.** Original 1931 paper was on radiative
   transfer (the Milne problem). Subsequent: neutron transport
   (Wiener–Hopf, Case–Zweifel), spectral line formation in stellar
   atmospheres, surface impedance in electromagnetism, edge diffraction
   in optics, diffraction by half-planes (Sommerfeld), traffic / queueing
   (Lindley), random walks (Spitzer).
4. **Path integrals and stochastic control in physics.** Onsager–Machlup
   1953, Freidlin–Wentzell large-deviations action, Kappen 2005 / Todorov
   2009 / Theodorou (KL / path-integral control). Action = convex
   functional on path space, controls adapted to filtration, optimal
   control as Legendre transform of value function.
5. **Quantum filtering and continuous measurement.** Belavkin 1988+,
   Bouten–van Handel–James 2007. The quantum stochastic master equation
   is the quantum analogue of the Kalman filter; the "innovations
   process" is adapted to the measurement filtration. Is this an
   instance of nest-algebra outer factorization in a noncommutative
   $L^2$?
6. **Stochastic thermodynamics & maximum caliber.** Sekimoto, Seifert
   (review 2012), Jarzynski 1997, Crooks 1999, Pressé–Ghosh–Dixit–Dill
   (Rev. Mod. Phys. 2013) on maximum caliber. Convex (relative-entropy)
   optimization over adapted path measures.
7. **JKO scheme, Otto calculus, Wasserstein gradient flows.** Jordan–
   Kinderlehrer–Otto 1998: Fokker–Planck as gradient flow of free energy
   in Wasserstein-2 geometry. Convex variational problem on a metric
   space; adapted version connects to causal OT and stochastic
   thermodynamics.
8. **Large deviations & Freidlin–Wentzell.** Rate function as convex
   action; instanton/optimal-fluctuation paths as adapted minimizers.
9. **Bismut–Elworthy and stochastic mechanics.** Adjoint / dual
   approach in stochastic optimal control; relation to Hamilton-Jacobi.

## Source types

- Foundational physics papers: Kramers 1927, Kronig 1926, Toll 1956,
  Kubo 1957, Callen–Welton 1951, Onsager–Machlup 1953, Sommerfeld 1896.
- Math-physics: Titchmarsh 1937 *Introduction to the Theory of Fourier
  Integrals*; Krein on Wiener–Hopf; Carrier–Krook–Pearson.
- Modern surveys: Seifert 2012 (stoch. thermo., Rep. Prog. Phys.);
  Pressé et al. 2013 (Rev. Mod. Phys., max caliber); Bouten–van Handel–
  James 2007 (quantum filtering).
- Path-integral control: Kappen 2005, Todorov 2009, Theodorou 2011.
- arXiv 2010–2026 for connections people are drawing now (especially
  ML/AI ⇄ physics ⇄ optimal control).
- Causal OT in physics: any work using bicausal OT for entropy production
  / stochastic thermodynamics?

## Expected sections

1. Thesis & scope.
2. Causality and dispersion relations: Kramers-Kronig as adapted
   factorization in the frequency domain.
3. Linear response and FDT.
4. Wiener-Hopf's physics origins: radiative transfer, neutron transport,
   diffraction.
5. Path integrals and stochastic control in physics.
6. Quantum filtering & noncommutative nest algebras.
7. Stochastic thermodynamics & maximum caliber.
8. Wasserstein gradient flows and adapted OT in non-equilibrium physics.
9. Large deviations as adapted convex duality.
10. Synthesis: what physics literature already uses the skeleton, what is
    folklore, what is genuinely new.
11. Open questions and bridges to make explicit.

## Task ledger

- [ ] T1 — delegate wide sweep to `researcher` subagent
- [ ] T2 — synthesize into draft at `outputs/.drafts/<slug>-draft.md`
- [ ] T3 — `reviewer` pass (citations + content)
- [ ] T4 — fix FATAL issues
- [ ] T5 — copy to `outputs/<slug>.md` + write provenance

## Verification log

(empty)

## Risks

- The skeleton "adapted convex duality" is not a named programme in
  physics; will have to translate. Mitigation: explicitly mark the
  framing as the reviewer's, not a physics community label.
- Quantum filtering involves nontrivial operator-algebraic technicalities
  (von Neumann algebras, noncommutative $L^p$); risk of overstating the
  nest-algebra connection. Mitigation: cite Bouten–van Handel–James for
  the precise statements and avoid going beyond what they prove.
