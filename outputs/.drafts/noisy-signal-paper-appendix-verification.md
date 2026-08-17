# Self-verification: noisy-signal-paper-appendix

Run: direct-mode (lead-owned), single local artifact.

## Checks performed

1. **File integrity.**
   - `wc -l papers/noisy-signal-impact-trading.md` → 807 (was 596; +211 lines for appendix).
   - `grep -c "Theorem B\."` → 14 occurrences (8 statements + 6 cross-refs/proofs of B.5 referenced in B.7). ✓
   - `grep -c "Definition A\."` → 10 occurrences (9 definitions + 1 cross-ref). ✓
   - Section ordering preserved: §1 … §11 Conclusion → Appendix A → Appendix B → Sources. ✓

2. **Numerical sanity.**
   - Re-ran `python3 experiments/markov_closure_check.py` → discrete identity (15c) matches to 6+ decimals across (α, ρ) ∈ {0.25,0.5,0.75} × {0.3,0.7,0.95}. Continuous identity (15b) within 0.5% in the mid-range, with explicit caveat in B.6 about the crude quadrature. ✓

3. **Citation discipline.**
   - All references in the appendix are already in the paper's bibliography (Gat10, Wiener49, SKM93, GJ80, Hosking81, AC01, AJN22, AJN24). No new bibliography entries added.
   - Two textbook references (Doob, Hannan, Hoffman, Kalman 1960) are flagged in-text as "classical, not in bibliography". This is acceptable for a self-contained appendix on standard machinery; no FATAL issue.

4. **Cross-reference consistency.**
   - Every theorem statement names the section/equation in the main text it proves.
   - The cross-reference index at the end of Appendix B lists all 8 theorems with their main-text anchors.

5. **No invented results.**
   - No new numerical claims, benchmarks, tables, or empirical results were added.
   - Both numerical "sanity" footnotes (B.6, B.7) point to the existing `experiments/markov_closure_check.py` and its existing output file `experiments/results/markov_closure_check.out`.

## FATAL findings
None.

## MAJOR findings
None. All proofs are standard textbook material applied to the paper's specific objects; the only step that is original to this paper is Theorem B.5 (Markov-closure scalar identity), which follows directly from §5.5 of the main text.

## MINOR findings
- **M1.** Theorem B.4 references Hoffman's *Banach Spaces of Analytic Functions* and Theorem B.5 references Doob and Hannan as classical reference points that are not in the bibliography. This is flagged in-text. A future revision could add formal entries; not a blocking issue.
- **M2.** Theorem B.6's integration-by-parts step writes the algebra terse — the sign-cancellation `(-1)·(-1)` is shown but could be tighter. The end result $\Gamma(-\alpha)\kappa^\alpha$ is correct and matches Samko–Kilbas–Marichev §5 and the numerical check.
- **M3.** Theorem B.3 uses "wide-sense" projection terminology in the non-Gaussian case but the rest of the paper does not always distinguish strict vs. wide-sense; consistent with the paper's existing register (§5.5 makes the same distinction).
- **M4.** Theorem B.5 statement uses `[K_-^{-1} * f]_+(t)` to denote the causal projection of an anticausal-filtered process. This matches main-text §5.5 notation eq. (12c) exactly.

## On-disk verification of the integration
- `grep "^## Appendix A. Definitions" papers/noisy-signal-impact-trading.md` → matches on line 542. ✓
- `grep "^## Appendix B. Proofs" papers/noisy-signal-impact-trading.md` → matches on line 591. ✓
- `grep "^## Sources" papers/noisy-signal-impact-trading.md` → matches on line 752 (appendix lives before bibliography, as planned). ✓
- Tail of the file unchanged: bibliography entries 1–18 intact (visual spot-check of last 60 lines).

## Verdict
PASS WITH NOTES (M1–M4 are presentational minor issues only).
