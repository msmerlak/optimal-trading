# Evidence Notes — optimal-trading-filters review

Artifact: `v2/optimal-trading-filters-v2.tex` (read in full, 487 lines, from disk 2026-07-24).
Companions inspected: `v2/optimal-trading-filters.bib`, `v2/experiments/*.py`, `v2/experiments/TEST_RESULTS.md`, `v2/figures/*`.

## Compile / mechanical
- `pdflatex → bibtex → pdflatex ×2`: **0 errors, 0 undefined refs, 0 undefined citations, 0 overfull hboxes**, 19 pp.
- Notation Table 1 uses `tabularx` (X column) — fits within margins.

## Structure (as read)
- §1 Introduction: 1.1 gain–risk–cost (motivation-first), 1.2 adaptedness (position/N/μ), 1.3 causal factorization (factors **N**), 1.4 relation to earlier work.
- §2 The stationary solution: 2.1 Factorization of friction, 2.2 Prediction of signal, 2.3 The trading filter. Assumptions (Friction, Signal) formalized; Lemma stated generally `A=A_-A_+`.
- §3 Pure power-law impact: 3.1 fractional derivative, 3.2 impact surfing. (Switches to rate/Q/α because at λ=0 position is non-stationary.)
- §4 Finite-horizon factorization: 4.1 relaxation to stationary filter, 4.2 power-law factor, 4.3 general kernels.
- §5 Recovery: 5.1 rational frictions, 5.2 finite-horizon liquidation, 5.3 general propagators.
- §6 Concluding remarks. Appendices A, B, D, E.

## Reformulation (major recent change, now consistent)
- Primary formulation is **position/N/μ**: gain `E∫xμ`, cost `½⟨x,Nx⟩`, `eq:symbol` is `n̂ = ηω²+γĝω²+λ`. FOC `P_+NP_+x*=μ`. Filter `x*=π*Ẇ`, `π̂=n̂_+^{-1}[h]_+`, `h=ψ̂ n̂_-^{-1}`.
- **Rate/Q/α** used only in §3 (power-law λ=0), Q=N(-∂²)^{-1}, α=E_t∫μ. Table 1 documents both, plus ψ̂ (spectral factor of μ) and φ̂ (of α). Whitened forecasts shown equal in App A.
- α is **absent from the intro** (first α at §3 line 273). Consistent with earlier user request.

## Claims / results and their support
- Thm (general policy) `x*=N_+^{-1}P_+N_-^{-1}μ` — proof App A (present, triangular bookkeeping + strict convexity uniqueness).
- Thm (trading filter) `π̂=n̂_+^{-1}[h]_+`, value `v=(1/4π)‖[h]_+‖²` — proof App B (present, Itô isometry).
- OU: `Φ(θ)=n̂_+(iθ)`, `x̂*=μ̂/(Φ n̂_+)`, `v=σ²θ/4Φ²` — derived App B (contour argument, `‖ψ̂‖²=πσ²θ`).
- §3.1 fractional policy `u*=(1/γc_β)D_+^ν ζ`, `ν=(1-β)/2` — via `Q_±=(γc_β)^{1/2}I^ν_±`. `c_β=2Γ(1-β)sin(πβ/2)`.
- Prop (rate response) `R=(θ²/Φ)(1/Φ−2c_1)`, `c_1=1/√(2γκ+λ)` (exp) / 0 (power-law or η>0); `X=θ/Φ²>0`; threshold `θ*=κ−2m` — proof App D.
- Prop (boundary-layer decay) `|u^{T}-u*| ≤ C d(t)^{-ν}` (power-law) / `Ce^{-b₁d(t)}` (rational) — proof App E.
- §4.2 power-law Volterra factor `c_+(t,s)` — "verified by direct kernel integration `C_-C_+=G_T`".
- §5 recoveries: Markowitz `x=μ/λ`, `v=θσ²/4λ`; aim portfolio `u=a(aim−x)` (GP2016/2013, BSV2017); exp+risk `eq:ema` (LN2019 model); exp+temp+risk `eq:nv-filter` (NV2022); GSS U-shape / OW block-plus-continuous / Forde Fredholm (§5.2); general-propagator identification with AJN2025/AJNT2024/AJ-DC-Pham2024 via uniqueness (§5.3).

## Numerical verification (`experiments/test_all_results.py`)
- Ran it: **9/9 CHECKS PASSED** (freq-domain closed forms vs time-domain reverse-Cholesky discretization; rel err ~1e-16 to 1e-14).
- Checks tie to: Szegő Φ, `|n̂_+|²=n̂`, X/v/response algebra, **causality gap v/v_ant=sin(πβ/2)** (check #4), R & threshold, discrete adapted optimum, boundary layer, Markowitz limit, NV Riccati poles = b₁,b₂.
- **STALENESS**: check #4 and `TEST_RESULTS.md` reference `eq:sinlaw`, `prop:vant`, `eq:sin` — grep confirms these labels are **absent from the current paper** (value-of-anticipation/causality-gap section was removed). `TEST_RESULTS.md` header says "8/8" but script now runs 9. The math still holds; the artifact is out of sync with the shipped paper.

## Symbol introduction order
- `c_β`: FIRST used line 162 (§2.1, `n̂∼γc_β|ω|^{1+β}`); DEFINED line 291 (§3.1, `c_β=2Γ(1-β)sin(πβ/2)`). Not in Table 1. ~4 pages out of order. **Genuine defect.**
- `m`, `A`: used in Prop response (§3.2) and defined again in §5.1 `eq:exp-factor`; each self-contained, mild redundancy.
- `σ`: OU innovation scale (§2.3, §5) vs `σ_r` stochastic vol (§2.2 moving average) — shared letter, context-clear.
- `e_k` in `eq:finiteT` (`α^eff=α+Σξ_k e_k`) — constraint directions, not explicitly defined.
- `Φ`, `h`, `h_α`, `ψ̂`, `φ̂`, `ρ_k`, `ν`, `b₁,b₂` — all defined at/near first use. Table 1 covers most.

## Figures
- Referenced: `fig1_filter_magnitude` (fig:filter), `fig4_impact_surfing` (fig:surf), `fig5_boundary_layer` (fig:bdry) — all exist. No dangling `\ref`.
- ORPHANED on disk: `fig2_kink_cusp.{png,py}`, `fig3_value_of_information.{png,py}`, `exp_kernel_anticipation_fraction.py` — leftovers from removed material. Figure files now non-contiguous (1,4,5).

## Style / LLM-giveaway scan
- Phrase scan: only "rather than" ×3. **None** of: Moreover, Furthermore, Importantly, Note that, In particular, crucially, delve, leverage, rich, In summary, It is worth/important.
- No negation-foils (`is not … but/it`). No rhetorical questions. Motivation-first intro.
- Em-dashes `---`: 31 across 19 pp (~1.6/pg) — moderate; a few could be commas/colons.
- Applied-math register consistent; no promotional tone.

## Acknowledgements (line 482)
- "Research and write-up were assisted by Claude models (**Opus 4.8 and Fable 5**) with the **Feynman harness**." — model names are non-standard/unverifiable (real Claude line: Opus 4/4.1; "Opus 4.8"/"Fable 5" not recognized). "Verification scripts and figure code are **available from the author**" — no public link.

## Attribution accuracy (verified earlier this session against primary sources)
- LN2019: transient(exp)+OU+risk model; explicit solution is risk-free φ=0 singular finite-horizon (generalizes OW). Paper states this correctly.
- NV2022: temporary+transient+risk, absolutely continuous (η>0). Paper's `eq:nv-filter` attribution correct.
- OW2013, GSS2012, GP2013/2016, AJN2025, AJ-DC-Pham2024 — attributions specific and consistent with titles.

## Sources
- `/Users/orwell/.../optimal-trading/v2/optimal-trading-filters-v2.tex`
- `/Users/orwell/.../optimal-trading/v2/optimal-trading-filters.bib`
- `/Users/orwell/.../optimal-trading/v2/experiments/test_all_results.py` (ran: 9/9 pass)
- `/Users/orwell/.../optimal-trading/v2/experiments/TEST_RESULTS.md`
- `/Users/orwell/.../optimal-trading/v2/figures/` (fig1–fig5 png)
- LN2019 arXiv:1704.00847; NV2022 arXiv:2002.09549 (model definitions confirmed).
