# Plan: Wiener–Hopf ↔ Riccati — A Note on the Connection

**Slug:** `wiener-hopf-riccati-connection`
**Date:** 2026-05-31
**Mode:** Direct search, lead-owned (no researcher subagents)

## Context

Workspace contains two related artifacts:

- `papers/noisy-signal-impact-trading.md` — paper deriving the stationary infinite-horizon optimal trading policy via **Wiener–Hopf factorisation** of the impact kernel $K$. AR(1) × exponential → scalar collapse; power-law → causal fractional derivative; noisy signal → two-stage Wiener prefilter + impact rule.
- `outputs/trading-duality-extensions.md` — companion note identifying the LQG separation principle as the parent of the noisy-signal result. Mentions that "the control half of LQG is usually a finite-dimensional Riccati equation. Here it is replaced by Wiener–Hopf factorisation in frequency domain — equivalent in the infinite-horizon stationary limit but more transparent."

This note expands that one sentence into a self-contained explanation of *how* Wiener–Hopf and Riccati are connected — when they coincide, when they diverge, how to convert between them, and which one to reach for in which situation.

## Objective

Produce a focused mathematical note (~5–8 pages) explaining the Wiener–Hopf ↔ Riccati relationship. Audience: a reader of the trading paper who knows LQG control or signal processing but has not seen the equivalence stated explicitly.

## Key Questions

1. **What does each method solve?** Crisp side-by-side statement of the problem each is the natural answer to (estimation/filtering, control, or both).
2. **Where do they coincide?** Stationary infinite-horizon LQG: spectral factorisation of the Hamiltonian system ↔ algebraic Riccati equation (ARE) ↔ Wiener–Hopf factorisation of the optimal closed-loop spectrum.
3. **The Kalman–Yakubovich–Popov (KYP) lemma** as the bridge: positive-real / spectral-factor / Riccati equivalence.
4. **Constructive conversions.**
   - State-space → Wiener–Hopf factor (via the stabilizing ARE solution → inner-outer factorisation).
   - Wiener–Hopf factor → state-space (rational spectral factor as $(A, B, C, D)$ realisation).
5. **Where they diverge.**
   - Non-rational kernels (Volterra, power-law) — Wiener–Hopf still works, Riccati becomes an *operator* Riccati (infinite-dimensional).
   - Time-varying / finite-horizon — Riccati ODE generalises cleanly; Wiener–Hopf less natural.
   - Non-Gaussian / non-quadratic — both break, but Riccati's robust extensions (min-max, $H^\infty$) live in the Krein-space Riccati framework.
6. **What this means for the trading paper specifically.**
   - The §5 scalar-collapse result reads as the "Riccati gain" of a 1-D LQG problem with state $f_t$ (AR(1)) and quadratic cost shaped by $K$.
   - The §7 separation principle is literally the LQG separation theorem applied to that 1-D problem.
   - For the matrix-Volterra case (Abi Jaber–Neuman–Tuschmann), operator Riccati and matrix Wiener–Hopf become the same object.
7. **Pedagogical pointers.** Where in standard texts the connection is stated.

## Evidence Needed

- KYP lemma / spectral factorisation ↔ Riccati equivalence: Anderson 1967, Willems 1971, Faurre 1976, Kucera 1972.
- Wiener–Hopf for stochastic LQG: Davis 1977, Kucera 1981, Lindquist–Picci 2015 (linear stochastic systems).
- Operator Riccati for Volterra control: recent work by Abi Jaber, Bouchaud–Schied, etc.
- The "Krein-space Riccati" link to $H^\infty$: Hassibi–Sayed–Kailath 1999.
- A canonical statement of the inner-outer / spectral factorisation construction via stabilising ARE: Zhou–Doyle–Glover *Robust and Optimal Control* (1996).

A few targeted `web_search` queries and one or two `fetch_content` calls to verify canonical references suffice. No PDF parsing.

## Scale Decision

**Direct search, lead-owned.** No researcher subagents.

Rationale:
- The math is standard; the synthesis is the value.
- External evidence needs are modest (~5 canonical references).
- The note must hold a single mathematical thread; delegation would fragment it.
- Not a "current landscape" question; mostly textbook material connected to the on-disk paper.

## Task Ledger

| ID | Owner | Task | Status |
|----|-------|------|--------|
| T0 | lead  | Re-read paper §5, §7 and companion note §1 for exact framing | DONE during planning |
| T1 | lead  | Web queries: KYP lemma / spectral factorisation ↔ Riccati | pending |
| T2 | lead  | Web queries: stochastic LQG via Wiener–Hopf (Davis, Kucera, Lindquist–Picci) | pending |
| T3 | lead  | Web queries: operator Riccati for Volterra control (Abi Jaber) | pending |
| T4 | lead  | Web queries: H∞ / Krein-space Riccati (Hassibi–Sayed–Kailath) | pending |
| T5 | lead  | Notes to `outputs/.drafts/wiener-hopf-riccati-connection-research-direct.md` | pending |
| T6 | lead  | Draft `outputs/.drafts/wiener-hopf-riccati-connection-draft.md` | pending |
| T7 | lead  | Cite → `-cited.md` | pending |
| T8 | lead  | Self-review → `-verification.md` | pending |
| T9 | lead  | Deliver to `outputs/wiener-hopf-riccati-connection.md` + provenance | pending |

## Verification Log

- (to be filled during execution)

## Decision Log

- 2026-05-31: Slug `wiener-hopf-riccati-connection`. Topic frames as mathematical explainer + connection-to-on-disk-paper. Output destination = `outputs/...md` (note, not paper-style).
- 2026-05-31: Direct mode. The work expands a one-sentence claim in the companion note; ~5–8 page result, no need for parallel research.
- 2026-05-31: Will explicitly use the AR(1) × exponential case as a worked example connecting (i) the §5 closed form, (ii) the corresponding 1-D Riccati equation, (iii) the spectral factor. This is a sanity check the reader can verify by hand.
- 2026-05-31: Avoid PDF parsing per workflow.

## Out of Scope

- New theorems beyond what's in standard references; this is a synthesis/explanation note.
- Numerical experiments (the AR(1) closed form vs operator solver test from yesterday is separate; this note will reference it where relevant).
- Detailed Krein-space machinery — mention the H∞/Krein connection and cite, but do not develop.
- Continuous-time vs discrete-time Riccati distinctions beyond stating them; the connection is the same structure.
