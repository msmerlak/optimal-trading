All 6 fixes plus the 5 style sites landed and verified (the earlier zero counts were shell-escaping artifacts). Every fix is confirmed against live file content.

## Summary

All six enumerated fixes applied within scope; paper builds clean (21 pp, 0 errors / 0 undefined / 0 overfull), verifier passes 9/9, figure regenerated with corrected labels. Nothing staged in git.

**Changed files**
- `v3/optimal-trading-filters-v3.tex` — Fix 1 (sign: "reverses **above** the threshold", was "below"); Fix 2 (one sentence after eq:vant: eq:vant is position-referred/finite for λ>0, rate-referred form used at λ=0, cross-ref to App. B for eq:sinlaw); Fix 3a–e (five math/abstract-noun subjects converted to property/passive/process-noun); Fix 4 (notation caption broadened to include the finite horizon §5); plus one break-fix rewording of the "squared gain" clause to clear an overfull hbox my Fix 3d introduced.
- `experiments/make_figures.py` — Fix 5 (panel-a title "fixed signal"→"fixed **appreciation** variance"; panel-b title+ylabel `v_{\rm ad}`→`v/v_{\rm ant}`).
- `experiments/test_all_results.py` — **new** Fix 6 (v3-aligned copy of the v2 verifier: docstring/header retarget v3; check #4 relabeled from "supplementary; not in paper" to "eq:sinlaw, in paper" with rate-referred v_ant note; run path updated).
- `v3/figures/fig_value.png` — regenerated and copied.

**Commands run**
- `pdflatex ×2` (post-fix, after an initial bibtex cycle) → exit 0, `Output written … (21 pages)`, 0 errors / 0 undefined / 0 overfull.
- `python experiments/make_figures.py` → exit 0; PNG title text visually confirmed correct.
- `python experiments/test_all_results.py` → exit 0, **9/9 PASSED** (check #5 independently confirms Fix 1: `R(below)>0, R(above)<0`).
- `python experiments/rate_response_2ema.py` → exit 0; saturation limits print as expected.

**Surprises**
- Fix 2 referenced `\ref{app:ou}`; the actual appendix label is `app:B` — caught and corrected before the build, so no undefined ref shipped.
- Fix 3d's rewording pushed one inline-math line 16pt overfull; resolved with a minor, meaning-preserving clause rewrite ("the squared gain is …").

**Left undone / residual risk**
- Appendix B (line 490) still cross-references `\eqref{eq:vant}` for the power-law ratio, even though eq:vant is the position form that diverges at λ=0; the appendix prose ("Referred to the rate, the same argument…" at line 484) makes the rate-referred intent clear, and my new body sentence now routes the reader correctly. I left the appendix `\eqref` untouched to avoid widening scope beyond the enumerated list — flagging it as an optional tightening for the author.