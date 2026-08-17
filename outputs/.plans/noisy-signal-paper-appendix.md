# Plan: Appendix of Definitions and Proofs for `papers/noisy-signal-impact-trading.md`

## Objective

Add a self-contained appendix to `papers/noisy-signal-impact-trading.md` that:

1. Collects formal definitions used implicitly in the main text (propagator, cost norm, Hardy spaces, causal/anticausal projection, Wiener–Hopf factorisation, stationary admissible policy, etc.).
2. Provides proofs (or full proof sketches with citations) for the load-bearing claims that the main text states without proof:
   - **L1** Cost norm is positive definite ⇔ propagator $G$ has nonneg spectral density (§2.4).
   - **L2** Legendre–Fenchel duality between the trade-cost norm and the position-Sharpe norm (§3).
   - **L3** Wiener–Hopf first-order condition and existence/uniqueness of the causal optimum (§4).
   - **L4** Spectral factorisation $S = K_- K_+$ with $K_\pm$ outer in $H^2_\pm$ (§4.2).
   - **L5** AR(1) scalar-collapse identity $[K_-^{-1} f]_+(t) = \hat K_-^{-1}(\rho)\, f_t$ (§5.5, eq. 12c).
   - **L6** Power-law × OU constant $\kappa^{(1-\beta)/2}$ via Frullani / $\Gamma(-\alpha)\kappa^\alpha$ (§6.3, eq. 15b).
   - **L7** Discrete fractional differencing × AR(1) constant $(1-\rho)^\alpha$ via generalised binomial (§6.3, eq. 15c).
   - **L8** Separation principle: optimal policy with noisy signal = Wiener-filter denoise ∘ deterministic optimal policy (§7.3).

## Key Questions

- Which load-bearing claims in the paper are stated without proof and require an appendix entry?
- For each, is the proof short enough to include, or should we give a self-contained sketch with a citation to a standard reference?
- Are there standard references (Wiener 1949; Bode–Shannon 1950; Hannan 1970; Hosking 1981; Granger–Joyeux 1980; Abi Jaber–Neuman 2022) that should be cited verbatim for the spectral-factorisation, Wiener-filter, and fractional-differencing results?

## Evidence Needed

- The current text of `papers/noisy-signal-impact-trading.md` (already on disk).
- The two companion notes already drafted:
  - `outputs/.drafts/trading-duality-extensions-cited.md`
  - `outputs/.drafts/wiener-hopf-riccati-connection-cited.md`
- Standard reference statements for: Wiener–Hopf factorisation in $H^2$; Paley–Wiener; Plancherel; Frullani integral $\int_0^\infty s^{-\alpha-1}(e^{-\kappa s}-1)\,ds = \Gamma(-\alpha)\kappa^\alpha$; generalised binomial series for $(1-x)^\alpha$.
- The Markov-closure check script `experiments/markov_closure_check.py` and its output for numerical sanity references.

## Scale Decision

**Direct, lead-owned.** This is a narrow extension task on a single local artifact, not a literature survey. No researcher subagents. Expected tool budget: read the paper, do at most 2–3 targeted web searches for canonical citation/form of standard identities (Frullani; Wiener filter; Hosking 1981 ARFIMA), then write the appendix.

## Task Ledger

| ID | Task | Owner | Status |
|----|------|-------|--------|
| T1 | Read full paper to enumerate every unproven load-bearing statement | lead | pending |
| T2 | Targeted web/code search: confirm canonical statements of (i) Wiener–Hopf scalar factorisation, (ii) Frullani / Γ(−α)κ^α identity, (iii) Hosking 1981 binomial expansion | lead | pending |
| T3 | Draft Appendix A (Definitions) and Appendix B (Proofs) covering L1–L8 | lead | pending |
| T4 | Self-citation sweep: every appendix lemma must reference the equation/section in the main text it supports, and every external lemma must cite a reference already in the paper's Sources or add one | lead | pending |
| T5 | Numerical sanity rerun of `experiments/markov_closure_check.py` to back the appendix's two worked constants | lead | pending |
| T6 | Append the new appendix to `papers/noisy-signal-impact-trading.md`, verify on disk | lead | pending |
| T7 | Self-review (FATAL/MAJOR/MINOR) and write provenance | lead | pending |

## Verification Log

- (empty — to fill during execution)

## Decision Log

- 2026-06-01: Treat as direct/lead-owned. The job is to formalize what is already in the paper plus standard textbook results; no new research is required beyond canonical-statement spot-checks.
- 2026-06-01: Will append the appendix as `## Appendix A` and `## Appendix B` after §11 Conclusion but before `## Sources`, to keep the bibliography last.
- 2026-06-01: Avoid PDF fetches per workflow guardrails; standard identities cited from textbook/Wikipedia/online HTML sources only.

## Deliverables

- `outputs/.plans/noisy-signal-paper-appendix.md` (this file)
- `outputs/.drafts/noisy-signal-paper-appendix-research-direct.md`
- `outputs/.drafts/noisy-signal-paper-appendix-draft.md` (appendix text only, draft)
- `outputs/.drafts/noisy-signal-paper-appendix-cited.md` (appendix text with inline citations)
- `outputs/.drafts/noisy-signal-paper-appendix-verification.md` (self-review)
- Edited `papers/noisy-signal-impact-trading.md` with the appendix inserted
- `papers/noisy-signal-paper-appendix.provenance.md` provenance sidecar
