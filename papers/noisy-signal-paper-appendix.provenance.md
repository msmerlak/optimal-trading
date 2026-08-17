# Provenance: appendix of definitions and proofs for `noisy-signal-impact-trading.md`

- **Date:** 2026-06-01
- **Rounds:** 1 direct-mode research round (lead-owned, no subagents)
- **Sources consulted:** 4
  - The paper itself: `papers/noisy-signal-impact-trading.md` (pre-patch, 596 lines)
  - Existing companion notes: `outputs/.drafts/trading-duality-extensions-cited.md`, `outputs/.drafts/wiener-hopf-riccati-connection-cited.md`
  - Existing experiment: `experiments/markov_closure_check.py` + output `experiments/results/markov_closure_check.out`
  - 3 web_search queries to confirm canonical statements of: Wiener–Hopf scalar spectral factorisation (arXiv:1603.01101); Frullani / Γ(−α)κ^α identity (hal-04611843, arXiv:2605.26153); Hosking 1981 fractional differencing (Hosking 1981 PDF; Granger–Joyeux 1980 Wiley DOI)
- **Sources accepted:** 0 new bibliography entries. All 8 appendix citations [Gat10], [Wiener49], [SKM93], [GJ80], [Hosking81], [AC01], [AJN22], [AJN24] resolve to the existing `## Sources` block in the main paper (entries #2, #14, #15, #16, #17, #7, #6, #5).
- **Sources rejected:** Doob, Hannan, Hoffman, Kalman 1960 — classical textbooks/papers, flagged in-text but not added to the paper's bibliography to preserve its existing reference scope.
- **Verification:** PASS WITH NOTES (4 MINOR presentation issues recorded in `outputs/.drafts/noisy-signal-paper-appendix-verification.md`).

## What was added to the paper

Inserted between §11 Conclusion and `## Sources`:

- **Appendix A. Definitions** — 9 formal definitions (A.1 signal/trade processes; A.2 admissible kernel; A.3 cost inner product; A.4 Hardy spaces and causal projections; A.5 outer spectral factor; A.6 causal Wiener filter; A.7 Marchaud anticausal fractional derivative; A.8 discrete fractional difference; A.9 kernel innovation).
- **Appendix B. Proofs** — 8 theorems matching the 8 load-bearing claims identified in the plan:
  - B.1 PD ⇔ no-dyn-arb (Bochner + Gatheral)
  - B.2 Legendre–Fenchel duality
  - B.3 Wiener–Hopf FOC and the boxed solution (6)
  - B.4 Szegő spectral factorisation
  - B.5 Markov-closure scalar identity (eq. 12c) — the only theorem original to this paper
  - B.6 Γ(−α)κ^α identity / OU × power-law closure (eq. 15b)
  - B.7 Generalised binomial / AR(1) × fractional-differencing closure (eq. 15c)
  - B.8 Denoise-then-trade separation principle (§7.3)
- **Cross-reference index** mapping each theorem to its main-text equation.

## On-disk verification of fixes / additions

| Check | Command | Result |
|---|---|---|
| Appendix A present | `grep "^## Appendix A. Definitions" papers/noisy-signal-impact-trading.md` | line 542 ✓ |
| Appendix B present | `grep "^## Appendix B. Proofs" papers/noisy-signal-impact-trading.md` | line 591 ✓ |
| Sources after appendix | `grep "^## Sources" papers/noisy-signal-impact-trading.md` | line 752 ✓ |
| Theorem count | `grep -c "Theorem B\."` | 14 (8 statements + cross-refs) ✓ |
| Definition count | `grep -c "Definition A\."` | 10 (9 defs + cross-ref) ✓ |
| Numerical sanity (15b, 15c) | `python3 experiments/markov_closure_check.py` | rerun, discrete matches to 6+ decimals; continuous within 0.5% mid-range ✓ |
| Line-count delta | `wc -l papers/noisy-signal-impact-trading.md` | 807 (was 596; +211) ✓ |

## Files written / modified

- **Modified:** `papers/noisy-signal-impact-trading.md` (596 → 807 lines; appendix inserted at line 542)
- **New:** `papers/noisy-signal-paper-appendix.md` (standalone cited appendix, mirror of `outputs/.drafts/noisy-signal-paper-appendix-cited.md`)
- **New:** `papers/noisy-signal-paper-appendix.provenance.md` (this file)
- **New:** `outputs/.plans/noisy-signal-paper-appendix.md`
- **New:** `outputs/.drafts/noisy-signal-paper-appendix-research-direct.md`
- **New:** `outputs/.drafts/noisy-signal-paper-appendix-draft.md`
- **New:** `outputs/.drafts/noisy-signal-paper-appendix-cited.md`
- **New:** `outputs/.drafts/noisy-signal-paper-appendix-verification.md`

## Plan

- `outputs/.plans/noisy-signal-paper-appendix.md`

## Research files

- `outputs/.drafts/noisy-signal-paper-appendix-research-direct.md` (search log + claim-to-source mapping)
