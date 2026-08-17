# Plan: CRONE control literature → insights for optimal trading

**Slug:** `crone-control-optimal-trading`
**Date:** 2026-06-27

## Motivation

The companion paper `papers/fractional-derivative-optimal-execution.md` argues
that optimal execution under power-law (propagator) impact is the
execution-theoretic instance of Oustaloup's CRONE / fractional-PID control
principle: "control of systems with power-law memory uses fractional-order
derivatives of the error signal." That claim was asserted from one
2025 survey (arXiv:2512.12111). This review hardens it by reading the
CRONE engineering literature directly and extracting:

1. What CRONE actually is and the three generations (CRONE-1, -2, -3).
2. Stability and robustness theorems with fractional-order controllers that
   could carry over to execution / market-impact control.
3. Tuning rules for $\gamma$ (memory exponent) and how they map to the
   power-law impact exponent in finance.
4. FFT / Oustaloup-recursion implementations of fractional differentiators
   that could replace Nyström / FBSDE numerical schemes in execution.
5. Adaptive / robust CRONE results relevant to mis-specified $\gamma$ in
   propagator models.
6. Any existing direct application of fractional-order control to finance,
   markets, or optimal trading specifically.

## Key questions

- Q1. What are the formal CRONE design theorems (gain/phase margin under
  fractional-order open-loop) and which generation is closest to the
  execution Fredholm setting?
- Q2. Are there explicit results on optimal control of systems with
  Volterra power-law kernels (the "memory $G(t)=ct^{-\gamma}$" object)?
- Q3. Tuning of the memory order in CRONE-3: what does "robust to
  gain variations" mean, and is its finance analogue robustness to
  impact-strength $c$?
- Q4. Numerical realization: Oustaloup recursive approximation, Carlson,
  Matsuda. What is the standard truncation error for $D^\gamma$ on
  $[0,T]$?
- Q5. Any existing fractional-order control applications to economics,
  market making, portfolio optimization, or order execution?
- Q6. What CRONE results are missing in the finance literature that
  would meaningfully transfer?

## Source types

- Primary: Oustaloup books / chapters (CRONE 1991, 1995), CRONE survey
  papers (e.g. Sabatier, Lanusse), recent fractional-control surveys.
- Engineering journals: IEEE TAC, Automatica, ISA Transactions,
  Fractional Calculus and Applied Analysis, Nonlinear Dynamics.
- Cross-disciplinary: arXiv math.OC, q-fin.TR, eess.SY.
- Time period: 1991–2026, prioritize 2015–2026 for surveys and any
  finance applications.

## Expected sections

1. Background on CRONE (1, 2, 3 generations) — what each generation
   robustifies.
2. Mathematical core: fractional integrator/differentiator, Bode's
   ideal cut-off, Oustaloup recursion.
3. Direct overlaps with the propagator-impact / fractional-execution
   problem.
4. Existing finance applications of fractional-order control.
5. Transferable insights and gap list for optimal trading.
6. Open questions / proposed follow-up experiments.

## Task ledger

| ID | Task | Owner | Status |
|----|------|-------|--------|
| T1 | Web search: CRONE generations, key papers, robust fractional control | self | pending |
| T2 | Web search: fractional-order control applications to finance/markets | self | pending |
| T3 | alpha paper search: "fractional order control finance", "Oustaloup CRONE optimal trading", "fractional PID portfolio" | self | pending |
| T4 | alpha paper deep read: 2512.12111 survey (Section on control), at least one Oustaloup-authored chapter or survey | self | pending |
| T5 | Cross-check: any q-fin paper citing Oustaloup or CRONE | self | pending |
| T6 | Synthesize: map CRONE concepts → execution concepts | self | pending |
| T7 | Verifier pass: every URL and citation | verifier subagent | pending |
| T8 | Reviewer pass: FATAL/MAJOR/MINOR triage | reviewer subagent | pending |
| T9 | Deliver `outputs/crone-control-optimal-trading.md` + provenance | self | pending |

## Verification log

(empty — to be populated as findings are confirmed or downgraded)

## Decisions / scoping notes

- Treat the deep-research skill's full provenance/multi-batch flow as
  optional. Topic is narrow (CRONE ↔ optimal execution) so direct
  searching plus targeted alpha reads should suffice; only escalate to
  a `researcher` subagent if breadth explodes.
- Do not fabricate finance applications of CRONE if none exist; the
  honest finding "no direct application yet" is the most likely
  outcome and is the headline gap.
