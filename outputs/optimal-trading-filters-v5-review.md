# Internal review — *Optimal Trading Filters: a Wiener–Hopf Approach* (v5, arXiv-bound draft)

**Artifact:** `arxiv/optimal-trading-filters-v5.tex` (435 lines, mtime 2026-08-17 21:24, uncommitted) + `arxiv/optimal-trading-filters-v5.pdf` (17 pp after rebuild) + `arxiv/figures/`, `arxiv/optimal-trading-filters.bib`.
**Reviewer:** Feynman (lead-owned review; no subagents used — single 435-line source, delegation would have added overhead).
**Review date:** 2026-08-17.
**Evidence file:** `outputs/.drafts/optimal-trading-filters-v5-review-evidence.md`. **Plan:** `outputs/.plans/optimal-trading-filters-v5-review-plan.md`.

---

## Summary Assessment

The paper solves the stationary signal-adaptive optimal trading problem under a general propagator by factoring the friction operator along the filtration (Wiener–Hopf / Szegő on the line, Gohberg–Krein on `[0,T]`) and reading the adapted optimum off the one-sided factors: `x* = N₊⁻¹ P₊ N₋⁻¹ μ`. The core idea is right, well motivated, and — unusually for this literature — *explicit*: the optimum becomes a linear filter whose special cases are Markowitz, the aim portfolio, the exponential-resilience moving-average policies, and, for scale-free kernels, a fractional integral of the signal. The two genuinely new physical statements are the signal-independent causality gap `v/v_ant = sin(πβ/2)` and the "no impact surfing / no block trades under power-law impact" dichotomy driven by a lag-zero atom `c₁`.

Verification status is better than typical for a theory draft: the repository's own suite (`experiments/test_all_results.py`) passes 9/9, including Szegő-vs-closed-form factors (rel err ≤ 1e-15), the `sin(πβ/2)` gap by independent quadrature, and — importantly — an exact LQ-Riccati computation whose closed-loop poles reproduce the paper's `(b₁,b₂)` to 3e-16, which substantiates the Neuman–Voß recovery claim. I also reproduced one figure byte-for-byte from its script and independently re-derived the finite-horizon power-law Volterra factor.

Two substantive problems: (i) the "impact surfing" diagnostic `R(θ)` is strictly negative in the *frictionless-Markowitz* limit where there is no impact to surf, so the economic interpretation attached to `R<0` is not established by the mathematics; (ii) Theorem 1 asserts existence and uniqueness under Assumption (Friction) alone, while the appendix concedes the projected-inverse identity holds only on a dense domain precisely in the `η=λ=0` power-law case that §3.2 and §4 are built on. There is also a verified constant error in the appendix statement of the Gohberg–Krein kernel identity, and no code/data availability statement despite several "checked numerically" claims.

**Overall:** strong, publishable core with a clear expository contribution; needs one conceptual repair (surfing), one theorem-statement repair (existence/domain), and a set of small factual/caption/typo fixes before posting.

---

## Strengths

1. **The central identity is clean and correctly used.** Lemma 1 (`(P₊AP₊)⁻¹ = A₊⁻¹P₊A₋⁻¹`) plus the Szegő factor gives closed forms where the comparable literature (Neuman–Voß; Abi Jaber–Neuman et al.; Forde–Sánchez-Betancourt–Smith) returns implicit FBSDE/Fredholm characterizations. The framing "adaptedness = causality = Paley–Wiener analyticity" is the right one and is delivered without hand-waving about what the projection does.
2. **Verified recovery of a named baseline.** Check 9 of the test suite solves the continuous-time algebraic Riccati equation for the Neuman–Voß configuration and gets closed-loop poles equal to the paper's `b₁,b₂` to machine precision for three parameter sets. This is a real baseline check, not a stylistic claim of "consistency".
3. **The `sin(πβ/2)` result is a genuinely quotable finding**, dimensionless, signal-independent, and independently confirmed by quadrature at 5 values of β (θ-spread ≤ 7e-15). It also lands in an interpretable place: a third to four-fifths of perfect-foresight value retained over the empirical β range.
4. **The rational→fractional taxonomy is pedagogically excellent.** "Zero / one / two moving averages", the superposition-of-exponentials reading of `|t|^{-β}`, and the crossover-frequency picture in Fig. 4 make the operator algebra legible to a practitioner.
5. **Numerical hygiene in the supporting code.** The reverse-Cholesky discrete adapted optimum is an independent machinery from the frequency-domain formulas, and the power-law case is reported with its grid error shrinking monotonically (0.109→0.066→0.039) rather than being presented as converged.
6. **Honest scope section.** §5's three restrictions (quadratic costs, stationary Gaussian signal for explicit filters, one asset) accurately match what the proofs deliver.
7. **AI-assistance disclosure** is present in the acknowledgements — appropriate and increasingly expected.

---

## Critical Issues

### C1. The "impact surfing" diagnostic fires in a model with no impact
*(§4.3, eq. (25); abstract sentence "this solution never surfs its own impact")*

Surfing is defined as `E[u*_t α_t] < 0` and declared to mean "the trader sells into a still-positive signal while the price relaxes back from its earlier impact". But eq. (25) in the pure-inventory-risk limit (`η=γ=0`, `n̂=λ`, `Φ=√λ`, `c₁=1/√λ`) gives

> `R = (θ²/√λ)(1/√λ − 2/√λ) = −θ²/λ < 0` for every θ,

and the repository's check 8 confirms this numerically (λ=1, θ=0.7 → R = −0.49). In that model there is **no transient impact at all**, so nothing can be surfed. Meanwhile the contemporaneous covariance is exactly zero there: `E[u_tα_t] = E[μ̇_tμ_t]/(λθ) = 0` for a stationary signal. The negative number is the *left-limit / lag-one* covariance `E[μ̇_tμ_{t−}] = −θVar(μ)`, i.e. an artifact of signal mean reversion, not of impact.

Two consequences:
- `E[u*α]` is not well defined contemporaneously for an OU signal once the rate carries a lag-zero atom (`u*` is a distribution). The definition must be stated as a one-sided limit or a lag-h statistic — which is what the numerics actually measure.
- The mechanism sentence "it is nonzero only when the impact is finite at zero lag and no instantaneous cost smooths it" is false as written: `c₁ = lim 1/n̂₊` is nonzero whenever `n̂₊` tends to a finite constant, including the impact-free Markowitz case. `c₁ ≠ 0` diagnoses a *jump component in the position*, not impact finiteness.

**Recommended fix:** define surfing relative to a baseline that removes the mean-reversion term (e.g. `R(θ) + θ²/λ`, or the sign of `c₁` relative to the pure-risk reference), state the statistic as a left-limit, and rewrite the mechanism sentence around "the rate has an atom ⇔ the position jumps", with impact finiteness as the *additional* condition that makes the jump affordable. The power-law conclusion (`c₁=0`, no block, no reversal) survives any of these repairs; the exponential story needs the baseline correction to be an *impact* statement.

### C2. Theorem 1 claims existence/uniqueness in a generality the proof does not cover
*(§2.2, Theorem 1; Appendix, Lemma 1 paragraph)*

Theorem 1 states "Under Assumption (Friction) the maximizer of (1) exists, is unique, and equals …". Assumption (Friction) allows `η=γ=0` excluded only through `n̂>0` a.e., so the pure power-law case (`η=λ=0`, `n̂ = γc_β|ω|^{1+β}`) is formally inside the theorem. But the appendix then says the identity "holds on the dense domain of signals with `∫(1+ω²)S_α/q̂ dω < ∞`; any `η>0` or `λ>0` gives bounded inverses", and §3.2 itself shows the position is *non-stationary* in that regime. The proof paragraph offers strict convexity and invokes Lemma 1; it gives no coercivity/closedness argument, no specification of the Hilbert space (completion under `‖·‖_N`, in which elements need not be positions), and no verification that `x*` is admissible.

**Recommended fix:** add the admissible space explicitly (completion of adapted processes under the friction norm), split Theorem 1 into (a) `η>0` or `λ>0`: existence/uniqueness in `L²`-type spaces; (b) degenerate case: existence in the rate variable with the stated dense domain, and state the non-stationarity of the position as part of the theorem rather than as later commentary.

---

## Major Issues

### M1. Verified constant error in the appendix Gohberg–Krein identity
*(Appendix, "Volterra factors on `[0,T]`"; eq. (24))*

The appendix states that direct integration gives `∫₀^T c₊(u,t)c₊(u,s) du = γ c_β |t−s|^{−β}` "with the correct constant". I checked this numerically (T=10; (t,s) ∈ {(0.3,0.7),(1,3),(4,4.5),(0.1,9)}; β ∈ {0.2,0.5,0.8}):

- the `(t,s)`- and `T`-dependence match `|t−s|^{−β}` exactly (so the terminal-anchoring structure of (24) is right);
- the constant is `γ c_β K(β)` with `K(β) = Γ(β)sin(πν)/π` (1.389789, 0.398942, 0.114517 for the three β);
- and `c_β·K(β) = 1.0000000000` in all three cases.

So the correct identity is `∫ c₊c₊ = γ|t−s|^{−β}` — which is exactly the rate-variable friction kernel implied by the objective (`γ/2 ∬ g(|t−s|)u_tu_s` with `g=|t|^{−β}`). **The kernel (24) is correct; the appendix sentence carries a spurious factor `c_β`.** Since `c_β` ranges over 0.72–8.73 on the empirical β range, this is not a harmless typo for a reader trying to reuse the factor. Verification: `outputs/.drafts/...-evidence.md` §4.

### M2. Proposition 1 (boundary layer) is a heuristic, and its power-law branch is untested
*(§4.1, eq. (22); Appendix, Prop. 1 paragraph)*

- The proof is two sentences of scaling argument ("the truncation cuts the Marchaud tail at distance `d(t)`, contributing `d(t)^{−ν}`"), with no estimate of the neglected terms.
- The bound `|u^{*,T}_t − u*_t| ≤ C(β)‖α‖_∞ d(t)^{−ν}` is **dimensionally inhomogeneous**: `d(t)^{−ν}` carries time`^{−ν}`, so `C(β)` cannot depend "only on the kernel parameters" without a scale. Write it as `(d(t)/τ)^{−ν}` with `τ` an explicit kernel scale, or absorb `γ, c_β` into a named constant.
- The appendix claims the terminal-weight deviation is `1 + O(d(t)^{−1})`. The weight `((T−s)/(T−t))^ν` depends on `(t−s)/(T−t)`, so the natural statement is `1 + O((t−s)/(T−t))`; as written the claim of subdominance is unsupported.
- Numerically, the repository tests only the *rational* branch (check 7: interior deviation ≤ 0.0163 vs boundary 0.5599 at η=0.5, γ=1, κ=2, λ=1, T=20), and it tests a magnitude threshold, not a decay rate. The power-law `d^{−ν}` claim is currently unverified in either proof or numerics.

### M3. Reproducibility: numerical claims in the text are not checkable by a reader
The tex makes at least three verification claims — "checked numerically against the reverse-Cholesky factor of `e^{−κ|t−s|}`" (appendix), "These signs match the discrete adapted optimum to the resolution of the grid" (§4.3), "verified by direct kernel integration" (§4.2) — but there is **no code or data availability statement anywhere in the paper**. The supporting code exists (`experiments/test_all_results.py`, 9/9 PASS) and is good; none of it is reachable from the arXiv version. Add a one-line availability statement with a repository/DOI link, or drop the "checked numerically" phrasing.

Secondary reproducibility defects found in the figure pipeline:
- `experiments/fig_filter_structure_v5.py` writes to `../v5/figures`, a directory that no longer exists after the `v5 → arxiv` rename (commit cc819a0). Re-running it silently recreates `v5/figures` and does **not** update `arxiv/figures/fig_filter_structure.*`. Confirmed by execution.
- Other figure scripts save to a CWD-relative `figures/`, so they must be run from the repo root and copied by hand; nothing wires figures to `arxiv/figures/`.
- I found **no script that generates `fig_boundary_layer`** (`make_figures.py` generates `fig_causality_gap` at line 194 but has no `save(..., "fig_boundary_layer")`); per `CHANGELOG.md` the file was inherited from the v2 figure set. That figure currently has no reproducible provenance.
- Positive control: `experiments/fig_transfer_impulse.py` reproduces `arxiv/figures/fig_transfer_impulse.png` **byte-identical** (sha1 `444a171…`), so the pipeline is reproducible where the paths are current.

### M4. The Neuman–Voß "recovery" is narrower than the abstract implies
The abstract says "we recover the Neuman–Voß solution away from horizon boundaries". What is established (and numerically confirmed) is that the *stationary feedback gains* coincide: the ARE closed-loop poles equal `(b₁,b₂)`. Neuman–Voß (SIAM J. Financial Math. 13(2):551–575, 2022) work with a **finite-variation** predicting signal and a finite horizon; the OU signal used here is not of finite variation, so their theorem does not contain this paper's setting and vice versa. State the recovery at the level of the interior/stationary feedback law and note the signal-class difference, otherwise a referee from that community will read it as an overclaim.

### M5. Figure 3 caption contradicts the figure
Caption: "The rational friction family, at fixed `η=0.5`, `λ=1`, `θ=1`. (a) … the two moving-average rates `b₁,b₂` against risk aversion `λ`". Panel (a) sweeps `λ` over `[10^{-2},10^{1.3}]` (script line 43); only panel (b) fixes `λ=1` (line 56). Also "the fast rate stays near the resilience κ" is loose: at λ=1 the script prints `b₂=3.661` against `κ=2`, and the λ→0 limit is `√(κ²+2κγ/η) ≈ 2.83`.

---

## Minor Issues

- **m1.** `\label{sec:value}` sits under an unnumbered `\subsubsection*`; the `.aux` resolves it to `3.2`, the same number as `sec:powerlaw`. The §2.4 pointer "We will see in Section 3.2" therefore points at the parent subsection. Either number the subsubsection or reword the pointer.
- **m2.** Typos: "a instantaneous impact" (L52) and "a instantaneous part" (L62) → "an instantaneous"; "optimal liquidiation" (L334) → "liquidation"; "; The solution of (4) requires…" (L87) → lowercase after the semicolon, or make it a full stop.
- **m3.** Dash style: "Wiener-Hopf" in the abstract and in §4.1 vs "Wiener--Hopf" elsewhere; "Obizhaeva-Wang" in the abstract vs the en-dashed style used for every other author pair.
- **m4.** Two Overfull `\hbox` warnings remain, at tex lines 422–423 (12.55pt) and 426–427 (2.50pt), both in the appendix formula paragraphs. Everything else builds clean (17 pp, 0 undefined refs, 0 undefined citations).
- **m5.** `booktabs` and `tabularx` are loaded but the paper has no table.
- **m6.** Unused bib entries: `AlfonsiSchiedSlynko2012`, `KalsiLyonsPerezArribas2020`. Alfonsi–Schied–Slynko is actually relevant to the no-manipulation discussion in §1.1 and §4.3 — cite it or remove it.
- **m7.** The aim portfolio at eq. (10) is attributed to `GarleanuPedersen2016` (JET); the aim portfolio is the headline object of Gârleanu–Pedersen (2013, *Journal of Finance* 68:2309–2340), which is in the bib and cited in §1.2. Consider citing 2013 first at eq. (10).
- **m8.** `\citet[Ex.~2.30]{GatheralSchiedSlynko2012}` — the article exists (Math. Finance 22(3):445–474) but I could not verify an "Example 2.30" in it; that numbering is unusual for a 30-page article. Double-check the pointer, or cite the result without a numbered pointer.
- **m9.** The committed PDF in `arxiv/` was built 2026-07-29 from an earlier tex, i.e. it was **stale** relative to the 2026-08-17 source. My rebuild overwrote it (it now shows as modified in `git status`). Rebuild-and-commit before posting.
- **m10.** `experiments/test_all_results.py` still advertises itself as verifying `v3/optimal-trading-filters-v3.tex`. Retarget it at v5 and add the two v5-specific gaps (power-law boundary layer; the GK kernel identity of M1) so the suite covers the current claims.
- **m11.** Related work worth a sentence, given the framing: Curato–Gatheral–Lillo on optimal execution with transient impact, and the filtering/learning-with-signals line (e.g. Casgrain–Jaimungal). Flagged as a suggestion, not a verified omission — I did not audit those papers here.

---

## Reproducibility and Verification

| Check | Method | Result |
|---|---|---|
| LaTeX build | `pdflatex → bibtex → pdflatex ×2` | **PASS** — 17 pp, 0 errors, 0 undefined refs/citations, 2 overfull hboxes |
| Figures present | file existence in `arxiv/figures/` | **PASS** — all 6 (.png + .pdf) |
| Bibliography integrity | key diff tex↔bib | **PASS** — all cited keys defined; 2 unused entries |
| Analytical results suite | `.venv/bin/python experiments/test_all_results.py` | **PASS 9/9** (Szegő factors ≤1e-15; `sin(πβ/2)` ≤4e-14; discrete adapted optimum; NV Riccati poles 3e-16) |
| GK power-law kernel identity | my own quadrature (`/tmp/gk_check.py`) | **FAIL as stated in the appendix** — true constant is `γ`, not `γc_β` (`c_β·K(β)=1.0000000000`); kernel (24) itself is correct → M1 |
| Figure reproducibility (sample) | rerun `fig_transfer_impulse.py` in clean dir, sha1 compare | **PASS** — byte-identical |
| Figure pipeline paths | script inspection + execution | **FAIL** — `fig_filter_structure_v5.py` writes to non-existent `v5/`; no generator found for `fig_boundary_layer` → M3 |
| Power-law boundary-layer bound | searched suite + proof | **Verification: BLOCKED / NOT RUN** — no test exists; proof is a scaling sketch → M2 |
| Citation spot-checks | web | NV2022 **verified** (SIFIN 13(2):551–575, arXiv:2002.09549); GSS2012 exists, "Ex. 2.30" pointer **unverified** |
| Code/data availability in paper | grep tex | **ABSENT** → M3 |

Distinction between blocked checks and paper weaknesses: the only *blocked* item is the power-law boundary-layer constant (no test harness exists, and I did not build one) and the GSS "Ex. 2.30" pointer (article not fetched). Everything else above is a positive or negative result I actually executed.

---

## Inline Annotations

- **Abstract, last sentence** — "never surfs its own impact or generates block trades": correct for the power law under the paper's own statistic, but the contrast with the exponential case inherits C1; qualify or repair the definition first.
- **Abstract, "we recover the Neuman–Voß solution"** — narrow to the stationary/interior feedback law (M4). Also: the abstract mixes "I show" and "we recover"; pick one voice.
- **§1.1, eq. (1)** — the objective takes linear impact and quadratic costs as given, with no permanent-impact term. One sentence saying permanent impact is omitted because it contributes a strategy-independent term for round-trip-neutral policies (or that it is simply excluded) would preempt a referee question.
- **§1.2, eq. (4)** — the two forms `E_t[(Nx*)_t] = μ_t` and `P₊NP₊x* = μ` are asserted as equivalent for adapted variations; a half-line of justification (variation over adapted perturbations + tower property) is cheap and would close the gap.
- **§2.2, Theorem 1** — see C2 (space, admissibility, degenerate case).
- **§2.2, Lemma 1 proof (appendix)** — "the reverse composition is the identity by positivity of `P₊AP₊` on the adapted subspace" is doing real work in one clause; for unbounded factors this needs injectivity + range statements, not just positivity.
- **§2.4 / Fig. 1** — the caption's `v = 1/2Φ(θ)²` at `Var(μ)=1` is internally consistent with `v = σ²θ/4Φ²` under the paper's OU convention (`Var(μ)=σ²θ/2`); checked. Consider stating that conversion in the caption — it is the step that inverted the value story in the project's own history (`CHANGELOG.md`, 2026-07-28).
- **§3.1, "All three frictions"** — `b₁²b₂² = λκ²/η`, `b₁²+b₂² = κ²+(2κγ+λ)/η` are confirmed against the exact ARE poles (check 9). Good; consider stating explicitly that these are the NV closed-loop poles, since that is the cleanest form of the recovery claim.
- **§3.2, eq. (16)** — the non-stationarity discussion (`S_μ = o(|ω|^β)` needed at the origin) is one of the sharpest passages in the paper. Keep it; it is also the natural place to move the domain caveat from C2.
- **§3.2 value-of-information subsubsection** — label/cross-reference bug (m1).
- **§4.1, eq. (21)** — "`α^eff = α + Σ_k ξ_k e_k`" is stated for "one multiplier per linear position constraint" and then, parenthetically, "a process-valued multiplier for the pathwise constraint `x_T=0`". The pathwise case is not a finite sum; either give the process-valued form or explicitly defer it (§5 already admits "sharp constants … require additional work", but this is a structural, not a constants, gap).
- **§4.1, Prop. 1 / eq. (22)** — see M2 (dimensions, untested power-law branch).
- **§4.2, eq. (24) + appendix** — kernel correct, stated constant wrong (M1).
- **§4.3, eq. (25)** — see C1. Also state explicitly that `R` is measured in the numerics as a lag-one regression, since the continuum object does not exist pointwise.
- **§5** — accurate limits section; add the domain caveat (C2) and, if M3 is addressed, the availability statement here.
- **Fig. 3 caption** — parameter contradiction (M5).
- **Fig. 4 caption** — "roll off as `ω^{-1}` under the instantaneous cost": consistent with `|H| = 1/√n̂ ~ 1/(√η ω)`; checked, no change needed.
- **Fig. 5 caption** — `sin(πβ/2)` band consistent with the quadrature check (0.309 at β=0.2, 0.809 at β=0.6); no change needed.

---

## Recommendation

**Major revision before posting — the core result stands; three items must be fixed first.**

Blocking, in order:
1. **C1** — repair the surfing definition/mechanism (baseline-corrected statistic, one-sided limit, "atom ⇔ jump" mechanism). This touches the abstract.
2. **C2** — restate Theorem 1 with an explicit admissible space and split off the degenerate `η=λ=0` case.
3. **M1** — fix the `c_β` constant in the appendix GK identity (kernel (24) itself is fine).

Then: M2 (dimensionally correct boundary bound + either a numerical test or an explicit "heuristic" label), M3 (availability statement; fix `fig_filter_structure_v5.py` output path; recover or regenerate `fig_boundary_layer`), M4 (narrow the NV claim), M5 (Fig. 3 caption), and the minor list. Rebuild and commit the PDF (m9) and retarget the test suite at v5 (m10).

With those changes I would expect this to be well received: it is an unusually explicit, checkable contribution to a literature dominated by implicit characterizations.

---

## Sources

**Primary artifact and repository evidence (local):**
- `arxiv/optimal-trading-filters-v5.tex`, `arxiv/optimal-trading-filters-v5.pdf`, `arxiv/optimal-trading-filters-v5.aux`, `arxiv/optimal-trading-filters.bib`, `arxiv/figures/*`
- `experiments/test_all_results.py` (9/9 PASS), `experiments/fig_transfer_impulse.py`, `experiments/fig_filter_structure_v5.py`, `experiments/fig_value_lambda.py`, `experiments/fig_speed_position.py`, `experiments/make_figures.py`
- `RESULTS.md`, `CHANGELOG.md`, `git log` (commits `cc819a0`, `3191d39`, `5bba42a`)
- My independent check script: `/tmp/gk_check.py` (Gohberg–Krein power-law kernel constant)
- Evidence notes: `outputs/.drafts/optimal-trading-filters-v5-review-evidence.md`

**External sources consulted:**
- Neuman & Voß, *Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact*, SIAM J. Financial Math. 13(2):551–575 (2022) — https://arxiv.org/abs/2002.09549
- Gatheral, Schied & Slynko, *Transient Linear Price Impact and Fredholm Integral Equations*, Math. Finance 22(3):445–474 (2012) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1531466 ; https://openalex.org/W1929167035
- Gârleanu & Pedersen, *Dynamic Trading with Predictable Returns and Transaction Costs*, J. Finance 68:2309–2340 (2013); *Dynamic portfolio choice with frictions*, J. Econ. Theory 165:487–516 (2016) — as recorded in `arxiv/optimal-trading-filters.bib`

---

## Revision Log (2026-08-17, applied after this review)

The manuscript was revised in the same session; the review text above is preserved as written, and this section records what changed and what was verified. Full detail: `outputs/.drafts/optimal-trading-filters-v5-review-evidence.md` §10.

**Addressed in `arxiv/optimal-trading-filters-v5.tex`:**

| Item | Status | What changed |
|---|---|---|
| C1 surfing | **Fixed** | §4.3 retitled "Reversing rates and the lag-zero atom"; atom criterion corrected to "outer factor bounded at high frequency"; explicit caution that `E[u*α]` is a left limit and that `R<0` also holds in the impact-free Markowitz case (`R=−θ²/λ`); abstract rewritten |
| C2 existence | **Fixed** | `H_N` defined in §2; Theorem 1 hypothesis narrowed to `η>0` or `λ>0`, with an explicit degenerate `η=λ=0` clause in the rate variable |
| M1 constant | **Fixed** | Appendix identity now `∫c₊c₊ = γ\|t−s\|^{−β}`, with the Beta-type integral and the displayed constant identity `c_β·Γ(β)sin(πν)/π = 1` |
| M2 boundary layer | **Partly fixed** | Renamed "Boundary-layer envelope"; bound restated with `‖ζ‖_∞` and `(γc_β)^{−1/2}` (dimensionally homogeneous); labelled a scaling envelope, not a rate; appendix weight deviation corrected to `1+O((t−s)/(T−t))`. New numerical check written and run (below) — envelope consistent, exponent **not** sharp |
| M3 reproducibility | **Partly fixed** | `Code availability` paragraph added with an explicit `TODO: repository URL/DOI` (no fabricated link); `fig_filter_structure_v5.py` output path fixed to `../arxiv/figures`. `fig_boundary_layer` still has no generating script |
| M4 NV claim | **Fixed** | §3.1 states the finite-variation-signal difference and narrows the claim to the interior feedback law; abstract narrowed |
| M5 Fig. 3 caption | **Fixed** | λ swept in (a), fixed at 1 in (b); "near κ" replaced by the exact `λ→0` limit `√(κ²+2κγ/η)` |
| m1, m2, m3, m6, m7 | **Fixed** | Numbered subsubsection (label now resolves to 3.2.1); typos and dashes; Alfonsi–Schied–Slynko cited; aim portfolio attributed to GP2013 first |
| m8, m10, `fig_boundary_layer` provenance, `TODO` URL | **Open** | Left for the author |

**New evidence produced during the revision.** `experiments/boundary_layer_powerlaw_check.py` (new script) tests the power-law branch of Prop. 1 on the deterministic window problem (β=0.5, ν=0.25, γ=1, η=λ=0, dt=0.05, T=20, pad=100):

```
d 0.5 -> 1.0: |dev| 0.07945 -> 0.05579   local slope -0.510
d 1.0 -> 2.0: |dev| 0.05579 -> 0.03472   local slope -0.684
d 2.0 -> 5.0: |dev| 0.03472 -> 0.01279   local slope -1.090
C d^-nu envelope (C fitted at d=0.5): CONSISTENT
```

The deviation stays inside the `C d^{−ν}` envelope but decays faster than `d^{−ν}`. Since Prop. 1 is an inequality this is consistent with it, and it shows the exponent is not sharp. The test solves the deterministic (perfect-foresight) window problem, so it probes factor truncation rather than the adapted projection: **the power-law branch remains unverified as a rate**.

*Incident note (process, not paper):* the first version of that script allocated a dense 42,000² matrix (~14 GB) and had to be killed after exhausting machine memory. It was rewritten with a hard `MAX_N=6000` cap, a printed memory estimate, and a refusal path; the safe run took 2.5 s at 563 MB peak RSS.

**Post-revision verification (commands run):**
- `pdflatex → bibtex → pdflatex ×2`: rc=0, **19 pages**, 0 errors, 0 undefined refs/citations, 2 overfull hboxes.
- `experiments/test_all_results.py`: **9/9 PASS** after the edits.
- `experiments/fig_filter_structure_v5.py`: now writes into `arxiv/figures`, output byte-identical (sha1 `9093fc0e…`), no stray `v5/` directory created.

**Recommendation after revision:** the two critical items and the verified constant error are resolved in the source. Remaining before posting: fill the repository URL, decide whether to keep Prop. 1's exponent as an envelope or prove a sharp rate, restore provenance for `fig_boundary_layer`, retarget the test suite at v5, and check the `GSS Ex. 2.30` pointer.

### Second revision pass (all remaining items except the repository URL)

| Item | Status | What changed / what was verified |
|---|---|---|
| `fig_boundary_layer` had no generator | **Fixed** | `git log -S` confirmed no script ever existed. New `experiments/fig_boundary_layer.py` rebuilds it from the check-7 construction (η=0.5, γ=1, κ=2, λ=1, T=20, dt=0.05, pad 20, signal `sin(0.6t)`), with the `MAX_N` guard; prints `b1=0.7726`, scale `3/b1=3.883`, interior deviation 0.01107 vs overall 0.55993. Regenerated figure matches the inherited one curve-for-curve; only the shading half-width differs (3.88 vs ≈3.35, whose rule was undocumented). Caption now states the rule and that the signal is a deterministic sinusoid |
| Test suite still targeted v3 | **Fixed** | Retargeted to `arxiv/optimal-trading-filters-v5.tex` and extended from 9 to **13 checks, 13/13 PASS** (7.9 s, 399 MB peak) |
| — check 10 | new | Lag-zero atom: `c₁=1/√A` for exp+risk (rel ≤ 1.8e-14); **pure risk (γ=0, no impact) gives `c₁=1/√λ` and `R=−θ²/λ<0`** — C1's counterexample is now regression-tested; `1/\|n̂₊\|` decays with slope −1.0000 (η>0) and −0.7500 = −(1+β)/2 (power law) |
| — check 11 | new | `∫c₊c₊ = γ\|t−s\|^{−β}` at 9 (β,t,s) points, rel ≤ 1e-4, plus `c_β·Γ(β)sin(πν)/π = 1.000000000000` — locks in the M1 fix |
| — check 12 | new | `u ∝ [t(T−t)]^{(β−1)/2}` for the no-signal power-law program, ratio constant to 1.4e-4 / 4.4e-4 / 7.2e-4 (β = 0.3/0.5/0.7) |
| — check 13 | new | Power-law boundary-layer **envelope**: deviation inside `C d^{−ν}` while local slopes are −0.68, −1.00, −2.13; asserts both conditions, so it fails if the envelope is ever upgraded to a sharp rate without new analysis |
| **m8** `GSS Ex. 2.30` pointer | **Fixed** | No evidence of an "Example 2.30" in GSS 2012 (SSRN 1531466 / Math. Finance 22(3)). The closed form is in Gatheral's lecture notes *Optimal order execution* ("Example II", explicitly "singular at t=0 and t=T", forcing the negative exponent), and FSS 2022 cite GSS for the no-signal `u₀`. The numbered pointer was removed; the formula itself is now independently confirmed by check 12 |
| Repository URL | **Open by instruction** | `TODO: insert repository URL/DOI before posting` remains in the Code availability paragraph |

Post-pass verification: rebuild rc=0, **19 pages**, 0 errors, 0 undefined refs/citations, 2 overfull hboxes; `test_all_results.py` **13/13 PASS**.
