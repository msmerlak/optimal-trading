# Plan: Implications, Generalizations, Connections — Optimal Trading via Wiener–Hopf Duality

**Slug:** `trading-duality-extensions`
**Date:** 2026-05-30
**Mode:** Direct search, lead-owned (no researcher subagents)

## Context (from on-disk artifacts)

Two prior artifacts in this workspace anchor the ideas to be extended:

1. `papers/noisy-signal-impact-trading.md` — paper draft establishing:
   - Stationary infinite-horizon optimal trading as a frequency-domain QP.
   - Cost = squared norm induced by impact kernel $K$; dual norm induced by $K^{-1}$ on signals (Legendre–Fenchel).
   - Wiener–Hopf factorisation $K = K_+ K_-$ to enforce causality.
   - AR(1) × exponential closed form; power-law kernel ⇒ causal fractional derivative of signal.
   - Noisy-observation case: clean two-stage decomposition (Wiener prefilter then impact-adjusted rule). Separation principle in the Gaussian-linear regime.

2. `outputs/optimal-trading-fractional-derivatives.md` — literature review covering rough volatility, Volterra propagators, multi-asset cross-impact, RL for execution, market making under rough vol, etc.

## Objective

Write a separate, self-contained companion note that explores **what these ideas imply, how they generalize, and what they connect to** — both within mathematical finance and outside it. This is reflective synthesis, not a new survey or replication.

## Key Questions

1. **Generalizations within the same framework**
   - Multi-asset / vector signals: does $K = K_+ K_-$ become matrix spectral factorisation? When is it tractable?
   - Non-stationary / finite-horizon: relation between Wiener–Hopf factorisation and the operator Riccati equations of Abi Jaber–Neuman.
   - Beyond Gaussian: when does the separation principle (denoise → trade) break, and how does it degrade?
   - Constraints (position limits, no-shorting, inventory penalties): conjugate duality formulation.
   - Robust/ambiguity-averse versions: minimax over signal spectra or kernel families.

2. **Connections to control & signal processing**
   - LQG separation principle / Kalman–Bucy: optimal trading separation is a direct instance.
   - Wiener filtering, innovations representation, Kolmogorov–Szegő theory.
   - $H^\infty$ / minimax filtering when signal spectrum is uncertain.
   - Linear-quadratic mean-field control when many agents share signals (crowding).

3. **Connections to information theory & estimation**
   - Mutual information between signal and trades; rate-distortion view of the impact cost.
   - Predictive information / past–future mutual information as the natural "alpha capacity".
   - Connection to Bayesian filtering of Volterra-driven hidden states.

4. **Connections to fractional calculus & rough volatility**
   - Power-law kernel ⇒ causal fractional derivative is *the* bridge to the rough-volatility / fractional-finance literature reviewed in the other artifact.
   - Implications for hedging under rough volatility (Volterra Heston): the same Wiener–Hopf logic should govern the optimal hedge rate.
   - Microstructural origin (Hawkes-process limits, Jaisson–Rosenbaum) of why power-law kernels appear.

5. **Connections to machine learning**
   - Causal fractional derivative as a learnable filter: linear interpretation of certain temporal convolutional / state-space models.
   - When deep RL for execution (e.g., Micheli–Monod 2024) should recover the Wiener–Hopf solution as a sanity check.
   - Signature methods as a nonparametric replacement for the linear-Gaussian assumption.

6. **Implications and open puzzles**
   - When is the closed-form rule a useful baseline vs misleading? (e.g., regime shifts, non-stationary impact.)
   - Does the AR(1)×exponential constant $\lambda \rho$ have a market-microstructure interpretation (information horizon × liquidity decay)?
   - Practical implications for live trading: which inputs are robustly estimable?

## Evidence Needed

- Primary mathematical anchors already on disk; no replication required.
- Light external evidence for:
  - LQG separation principle textbook statement (Kalman 1960; Wonham; Åström).
  - Wiener–Hopf factorisation references (Kolmogorov, Krein, Gohberg).
  - Matrix spectral factorisation for vector signals (Youla, Anderson).
  - Predictive information / past–future mutual information (Bialek–Nemenman–Tishby 2001).
  - Rate-distortion link to quadratic costs (Cover & Thomas; Berger).
  - Hawkes-process microfoundation of power-law impact (Bacry–Mastromatteo–Muzy; Jaisson–Rosenbaum 2015).
  - Signature methods in trading (Lyons; Kalsi–Lyons–Perez Arribas).
  - $H^\infty$ filtering basics (Hassibi–Sayed–Kailath).
- A few well-targeted `web_search` and alpha CLI queries to confirm canonical references; no PDFs fetched.

## Scale Decision

**Direct search, lead-owned.** No researcher subagents.

Rationale:
- The task is synthesis/extension of two artifacts already on disk, not new-landscape coverage.
- The author of the note must hold the thread of the existing duality/Wiener–Hopf framing; this is hard to delegate without losing coherence.
- External evidence needs are modest: confirming canonical references for ~7 connections.

## Task Ledger

| ID | Owner | Task | Status |
|----|-------|------|--------|
| T0 | lead  | Read both on-disk artifacts and extract the precise structural claims to extend | DONE (partial read; full re-read during drafting) |
| T1 | lead  | Web/alpha queries: matrix Wiener–Hopf / spectral factorisation references | pending |
| T2 | lead  | Queries: LQG separation principle, innovations, Kolmogorov–Szegő | pending |
| T3 | lead  | Queries: predictive information, rate–distortion / quadratic Gaussian | pending |
| T4 | lead  | Queries: Hawkes microfoundation of power-law impact (Bacry–Muzy, Jaisson–Rosenbaum) | pending |
| T5 | lead  | Queries: signature methods in optimal execution / trading | pending |
| T6 | lead  | Queries: $H^\infty$ / minimax filtering, robust control connections | pending |
| T7 | lead  | Write notes to `outputs/.drafts/trading-duality-extensions-research-direct.md` | pending |
| T8 | lead  | Draft `outputs/.drafts/trading-duality-extensions-draft.md` | pending |
| T9 | lead  | Cite → `outputs/.drafts/trading-duality-extensions-cited.md` | pending |
| T10| lead  | Self-review → `outputs/.drafts/trading-duality-extensions-verification.md` | pending |
| T11| lead  | Deliver to `outputs/trading-duality-extensions.md` + provenance sidecar | pending |

## Verification Log

- (to be filled during execution)

## Decision Log

- 2026-05-30: Slug chosen as `trading-duality-extensions`. Topic is "implications, generalizations, connections" — `extensions` captures it concisely.
- 2026-05-30: Direct mode chosen (lead-owned). Subagents would fragment the conceptual thread; modest external evidence suffices.
- 2026-05-30: Output destination = `outputs/trading-duality-extensions.md` (note, not paper-style draft). Paper draft lives elsewhere.
- 2026-05-30: Avoid PDF parsing per workflow; use abstracts, HTML pages, search snippets.

## Out of Scope

- New theorems or proofs beyond what the existing draft establishes (sketches only; clearly labelled as conjecture where unproven).
- Numerical experiments (covered by `experiments/`).
- Re-doing the fractional-derivative literature review (already exists).
