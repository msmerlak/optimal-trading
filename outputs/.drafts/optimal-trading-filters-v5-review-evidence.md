# Evidence notes — optimal-trading-filters-v5

All paths relative to `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading`.
Run date 2026-08-17.

## 0. Artifact identification
- `arxiv/optimal-trading-filters-v5.tex` — 435 lines, mtime 2026-08-17 21:24, `git status` = modified (uncommitted).
- `arxiv/optimal-trading-filters-v5.pdf` — mtime before my run: 2026-07-29 22:31, i.e. **the committed PDF was stale relative to the tex**. My rebuild overwrote it (now shows as modified in git).
- Title: "Optimal Trading Filters: a Wiener--Hopf Approach", single author (Matteo Smerlak, CFM). Acknowledgements disclose AI assistance ("Claude Opus 4.8 and Fable 5").
- Structure: §1 Intro (1.1–1.4), §2 Wiener–Hopf solution (Assumption 1, Lemma 1, Thm 1, Assumption 2, Thm 2, §2.4 value), §3 Exact filters (rational; power-law/fractional; value of information), §4 Finite horizon (GK factorization, Prop 1, pure impact, impact surfing), §5 Conclusion, Appendix A proofs. 6 figures, 0 tables.

## 1. Build check (command run)
```
pdflatex -> bibtex -> pdflatex x2   (TeX Live, /Library/TeX/texbin)
```
- Result: rc=0, "Output written on optimal-trading-filters-v5.pdf (17 pages)".
- 0 undefined references, 0 undefined citations, 0 LaTeX errors.
- 2 Overfull \hbox warnings, at tex lines 422–423 (12.55pt) and 426–427 (2.50pt) — both in the appendix ("Ornstein–Uhlenbeck formulas" and "Power-law formulas" paragraphs).

## 2. Figures and bibliography
- All 6 `\includegraphics` targets exist in `arxiv/figures/`: fig_value_lambda, fig_speed_position, fig_filter_structure, fig_transfer_impulse, fig_causality_gap, fig_boundary_layer (both .png and .pdf).
- Bib: 33 entries in `arxiv/optimal-trading-filters.bib`; all cited keys resolve. Uncited entries: `AlfonsiSchiedSlynko2012`, `KalsiLyonsPerezArribas2020`.
- Cross-reference artifact: `\label{sec:value}` sits under an **unnumbered** `\subsubsection*`; `arxiv/optimal-trading-filters-v5.aux` line 97 resolves it to `{3.2}` — the same number as `sec:powerlaw` (line 91). So the in-text pointer "Section~\ref{sec:value}" (§2.4) points to §3.2, the parent subsection, not the value-of-information block.

## 3. Numerical verification suite (command run)
`.venv/bin/python experiments/test_all_results.py` → exit 0, **9/9 PASS**. Header states it targets `v3/optimal-trading-filters-v3.tex`. Selected outputs:
- Check 1: Szegő integral Φ(θ) vs closed-form outer factors, rel err ≤ 1.2e-15 across exp / instantaneous / power-law / three-friction cases.
- Check 2: |n̂₊(ω)|² = n̂(ω) on the real axis, max rel ≤ 6.4e-16.
- Check 3: v = σ²θ/4Φ² equals σ²θ^{-β}/(4γc_β) for the power law, rel ≤ 1.7e-16.
- Check 4: v/v_ant = sin(πβ/2) by quadrature, θ-spread ≤ 7e-15, rel ≤ 4.4e-14 for β ∈ {0.2,0.4,0.5,0.6,0.8}. This is eq. (17) of the paper.
- Check 5: R(θ) sign law and θ* = κ−2m confirmed (λ=0 → θ*=2.0 with κ=2; λ=0.3 → 0.9435; λ=0.6 → 0.5554); power-law R>0 for all tested λ∈[0,1000], θ∈[0.5,4].
- Check 6: discrete adapted optimum (reverse-order Cholesky of the cost matrix) matches closed forms; power-law case shows grid error 0.109→0.066→0.039 under dt refinement (monotone but not converged — the paper's phrase "to the resolution of the grid" is accurate).
- Check 7: interior |u_fh − u_wl| ≤ 0.0163 vs boundary 0.5599 (rational kernel only; **no power-law boundary-layer test**).
- Check 9: exact LQ Riccati closed-loop poles for the Neuman–Voß configuration equal the paper's (b₁,b₂) to 3e-16. This substantiates the "recover the Neuman–Voß solution" claim at the level of stationary feedback gains.

## 4. Independent check of the appendix Gohberg–Krein power-law kernel (my own script, `/tmp/gk_check.py`)
Paper, eq. (24): `c_+(t,s) = (γc_β)^{1/2} ((T−s)/(T−t))^ν (t−s)^{ν−1}/Γ(ν)`, and appendix "Volterra factors on [0,T]": "direct integration of (24) gives ∫₀^T c₊(u,t)c₊(u,s)du = γ c_β |t−s|^{-β}".

Numerical quadrature of `((T−t)(T−s))^ν/Γ(ν)² ∫_{max(t,s)}^T (T−u)^{−2ν}(u−t)^{ν−1}(u−s)^{ν−1} du`, T=10, (t,s) ∈ {(0.3,0.7),(1,3),(4,4.5),(0.1,9)}, β ∈ {0.2,0.5,0.8}:
- The T- and (t,s)-dependence matches `|t−s|^{-β}` exactly (ratio constant to ~6 digits across all (t,s) for fixed β) → the terminal-anchoring structure of (24) is correct.
- The constant is `K(β) = Γ(β)sin(πν)/π` (β=0.2 → 1.389789; β=0.5 → 0.398942; β=0.8 → 0.114517), not 1.
- Therefore ∫ c₊c₊ = γ c_β K(β) |t−s|^{-β}, and numerically `c_β·K(β) = 1.0000000000` for all three β.
- Conclusion: the true identity is **∫ c₊(u,t)c₊(u,s)du = γ|t−s|^{-β}**, which is exactly the rate-variable friction kernel implied by the objective (γ/2 ∫∫ g(|t−s|)u_tu_s with g=|t|^{-β}). The prefactor `(γc_β)^{1/2}` in (24) is right; the **appendix sentence's stated result carries a spurious factor c_β**.

## 5. Internal algebra checks (by hand, cross-checked against the test suite)
- ν = (1−β)/2 from q̂ = γc_β|ω|^{β−1} = |q̂₊|²: consistent. β ∈ [0.2,0.6] ⇒ ν ∈ [0.2,0.4]: matches the text.
- n̂₊ ∝ (−iω)^{(1+β)/2} from n̂ = γc_β|ω|^{1+β}: consistent with eq. (16).
- sin(π·0.2/2)=0.309, sin(π·0.6/2)=0.809 — the text's "between a third and four-fifths" is right.
- Φ(θ) → √λ as θ→0 ⇒ v → 1/2λ (caption of Fig. 1): consistent.
- Var(μ)=σ²θ/2 for the OU convention used ⇒ Var(μ)=1 gives v = 1/2Φ²: consistent with the Fig. 1 caption and `experiments/fig_value_lambda.py` (line 27: gam,kap,beta,eta,lam = 1.0,2.0,0.5,0.5,0.5; line 56: floor = 1/(2(2κγ+λ))).
- Surfing threshold: κ−2m<0 ⟺ κ√(λ/A)>κ/2 ⟺ 4λ>2κγ+λ ⟺ λ>2κγ/3. The text's "past λ = 2κγ/3" is correct.
- Exponential GK inverse factors: C₊^{-1}C₋^{-1} = (κ+∂)(κ−∂)/(2γκ) = (κ²−∂²)/(2γκ), the inverse of the kernel γe^{−κ|t−s|} up to the Robin endpoint conditions. Ordering in eq. (23) is consistent.
- **Pure-risk limit of the surfing statistic**: with η=γ=0, n̂=λ, Φ=√λ, c₁=1/√λ, so eq. (25) gives R = (θ²/√λ)(1/√λ − 2/√λ) = −θ²/λ < 0. Test check 8 confirms numerically (λ=1,θ=0.7 → R=−0.49). But the contemporaneous covariance E[u_tα_t] = E[μ̇_tμ_t]/(λθ) = 0 for a stationary signal; the negative value is the *left-limit* covariance E[μ̇_tμ_{t−}] = −θVar(μ)/(λθ). So R is a one-sided (lag-one) statistic, and it is strictly negative in a model with **no transient impact at all**.

## 6. Figure provenance / reproducibility
- `experiments/fig_transfer_impulse.py` run from a clean temp dir: reproduces `arxiv/figures/fig_transfer_impulse.png` **byte-identical** (sha1 444a171102259beaabab62a898c9f63719f5e46e for both).
- `experiments/fig_filter_structure_v5.py` line 21: `OUT = os.path.join(os.path.dirname(__file__), "..", "v5", "figures")`. The directory `v5/` no longer exists (commit cc819a0 "rename v5->arxiv"); running the script from the repo would silently create a new `v5/figures` instead of updating `arxiv/figures`. Verified: running the copied script created `/tmp/v5/figures/fig_filter_structure.{png,pdf}`.
- `experiments/fig_value_lambda.py` (line 69), `fig_transfer_impulse.py` (line 104), `make_figures.py` (line 26) all save to a CWD-relative `figures/` — they must be run from the repo root and the outputs copied to `arxiv/figures/` by hand. No build script wires this.
- `fig_causality_gap` is produced by `experiments/make_figures.py` (line 194). **No script in `experiments/` writes `fig_boundary_layer`** (grep by name returns only v3/v4 LaTeX logs and the v3 tex); per `CHANGELOG.md` it was inherited from the v2 figure set.
- The tex contains **no data/code availability statement**; the acknowledgements mention only people and AI assistance. The numerical claims in the text ("checked numerically against the reverse-Cholesky factor"; "These signs match the discrete adapted optimum to the resolution of the grid"; "verified by direct kernel integration") are therefore not checkable by a reader of the arXiv version, although the supporting code exists in this repository.

## 7. Citation checks
- `NeumanVoss2022` — verified: Neuman & Voß, *Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact*, SIAM J. Financial Math. 13(2):551–575, 2022 (arXiv:2002.09549). https://arxiv.org/abs/2002.09549 — matches the bib (issue number absent, harmless). Note their signal is a **finite-variation** predicting signal; the OU signal used here is not of finite variation, so the "recovery" is of the stationary feedback gains (numerically confirmed, check 9), not a containment of their theorem.
- `GatheralSchiedSlynko2012` — verified to exist: Math. Finance 22(3):445–474, 2012 (SSRN 1531466). The in-text pointer `\citet[Ex.~2.30]{...}` for the U-shaped profile could **not** be verified (article not fetched); numbering "Example 2.30" is unusual for a journal article of that length.
- `GarleanuPedersen2013` (JF 68:2309–2340) and `GarleanuPedersen2016` (JET 165:487–516) both in bib; the aim-portfolio result at eq. (10) is attributed to the 2016 paper, whereas the aim portfolio is the headline object of the 2013 Journal of Finance paper (both are cited in §1.2, so this is an attribution nuance, not a missing reference).
- Uncited-but-present: `AlfonsiSchiedSlynko2012`, `KalsiLyonsPerezArribas2020`.

## 8. Writing / consistency observations (grep-verified line numbers)
- L52, L62: "a instantaneous" (should be "an instantaneous").
- L334: "optimal liquidiation" (typo).
- L87: "; The solution of ..." — capital after a semicolon.
- L44 (abstract) and L334: "Wiener-Hopf" hyphen vs "Wiener--Hopf" elsewhere; L44 "Obizhaeva-Wang" vs "Obizhaeva--Wang" style used for other author pairs.
- `booktabs`/`tabularx` are loaded but no table appears.
- Fig. 3 (`fig:structure`) caption: "The rational friction family, at fixed η=0.5, λ=1, θ=1. (a) ... the two moving-average rates b₁,b₂ against risk aversion λ" — λ is both declared fixed and swept. Script `fig_filter_structure_v5.py` confirms panel (a) sweeps λ ∈ [10^{-2},10^{1.3}] (line 43) and only panel (b) fixes λ=1 (line 56).
- Fig. 3 caption: "the fast rate stays near the resilience κ". Script output at λ=1: b₂ = 3.661 with κ = 2; the λ→0 limit is b₂ → √(κ²+2κγ/η) = √8 ≈ 2.83. "Near κ" is loose.

## 9. Scope statements the paper makes about its own limits (§5)
Quadratic costs only; explicit filters need a stationary Gaussian signal; one-dimensional asset (matrix WH left open); "sharp constants for the constraint boundary terms require additional work". These are accurate and match what the proofs deliver.

---

## 10. Revision pass (same day, after the review)

### 10.1 New numerical check written and run
`experiments/boundary_layer_powerlaw_check.py` (new). First version was unsafe: `dt=0.02, T=40, P=400` → n≈42,000 → ~14 GB dense matrix; it exhausted machine memory and was killed. **Rewritten with a hard `MAX_N=6000` cap, a printed per-matrix memory estimate, and `sys.exit` above the cap.** Safe run: n=401 (window) and n=4401 (padded, 155 MB), 2.5 s wall, 563 MB peak RSS (`/usr/bin/time -l`).

Result (β=0.5, ν=0.25, γ=1, η=λ=0, dt=0.05, T=20, pad=100; deterministic window problem):
```
d 0.5 -> 1.0: |dev| 0.07945 -> 0.05579   local slope -0.510
d 1.0 -> 2.0: |dev| 0.05579 -> 0.03472   local slope -0.684
d 2.0 -> 5.0: |dev| 0.03472 -> 0.01279   local slope -1.090
C d^-nu envelope (C fitted at d=0.5): CONSISTENT
```
Reading: the deviation stays **inside** the `C d^{-ν}` envelope but decays **faster** than `d^{-ν}` and is not a clean power law. Since Prop. 1 is an inequality, this is consistent with the proposition and shows the exponent is **not sharp**. It is a proxy: the test solves the deterministic (perfect-foresight) window problem, so it probes factor truncation, not the adapted projection. The power-law branch of Prop. 1 therefore remains **unverified as a rate**; it is now verified as an envelope in this proxy.

### 10.2 Manuscript edits applied to `arxiv/optimal-trading-filters-v5.tex` (all verified on disk, build re-run)
- **C1**: §4.3 retitled "Reversing rates and the lag-zero atom". Atom `c₁` now introduced first, with the correct criterion (outer factor bounded at high frequency). Added an explicit two-caution paragraph: `E[u*α]` does not exist contemporaneously with an atom (statistic is the left limit / lag-one regression), and `R<0` occurs in the impact-free Markowitz case (`R=−θ²/λ`), so a negative `R` is not per se an impact statement. Abstract sentence rewritten to "carries no instantaneous component: the trading rate has no lag-zero atom, so it produces neither block trades … nor a rate that reverses against its own forecast."
- **C2**: §2 preamble now defines `H_N` (completion of adapted processes in the friction norm) and states that it consists of adapted processes only when `η>0` or `λ>0`. Theorem 1 restated with that hypothesis, plus an explicit degenerate-case clause (`η=λ=0`: rate variable, dense domain, position only up to its non-stationary drift).
- **M1**: appendix identity corrected to `∫₀^T c₊(u,t)c₊(u,s)du = γ|t−s|^{−β}` (kernel of `G_T`), with the Beta-type integral written out and the constant justified by the displayed identity `c_β·Γ(β)sin(πν)/π = 1`.
- **M2**: Proposition renamed "Boundary-layer envelope"; bound restated in terms of `‖ζ‖_∞` with the `(γc_β)^{−1/2}` prefactor so it is dimensionally homogeneous; text now says it is a scaling argument and an envelope, not a sharp rate, and reports the numerical finding of §10.1. Appendix proof: weight deviation corrected to `1+O((t−s)/(T−t))`.
- **M3**: new `\paragraph{Code availability.}` listing the checks that are implemented, with an explicit `TODO: insert repository URL/DOI before posting` (no fabricated link). `experiments/fig_filter_structure_v5.py` output path fixed from `../v5/figures` (deleted dir) to `../arxiv/figures`; re-ran it — writes into `arxiv/figures`, output sha1 unchanged (`9093fc0e…`), and no stray `v5/` directory is created.
- **M4**: §3.1 now states that Neuman–Voß use a finite-variation signal, so neither setting contains the other, and that what coincides is the interior feedback law (their Riccati closed-loop poles = zeros `b₁,b₂` of `n̂₊`). Abstract narrowed accordingly.
- **M5**: Fig. 3 caption fixed (λ is swept in (a), fixed at 1 in (b)); "stays near κ" replaced by the exact `λ→0` limit `√(κ²+2κγ/η)`.
- **m1**: `\subsubsection*{The value of information}` → numbered `\subsubsection`; `.aux` now resolves `sec:value` to `3.2.1` (was `3.2`).
- **m2/m3**: "a instantaneous" ×2 → "an instantaneous"; "liquidiation" → "liquidation"; "; The solution" → ". Solving"; abstract and §4.1 dashes normalized to `Wiener--Hopf`, `Obizhaeva--Wang`.
- **m6**: `AlfonsiSchiedSlynko2012` now cited in the no-manipulation sentence (§1.1).
- **m7**: aim portfolio attributed to Gârleanu–Pedersen (2013) first, with the 2016 continuous-time version.

### 10.3 Post-revision verification (commands run)
- Rebuild `pdflatex → bibtex → pdflatex ×2`: **rc=0, 19 pages, 0 errors, 0 undefined refs/citations, 2 overfull hboxes** (`Output written on optimal-trading-filters-v5.pdf (19 pages, 491209 bytes)`).
- `experiments/test_all_results.py`: **9/9 PASS** again after the edits (the suite is independent of the tex, so this only confirms no code regression from the figure-path change).
- `experiments/fig_filter_structure_v5.py`: reruns into `arxiv/figures`, byte-identical output.
- Not addressed in this pass (still open): m8 (GSS "Ex. 2.30" pointer unverified), m10 (test suite still self-describes as targeting v3; the new boundary check is a standalone script, not wired into it), `fig_boundary_layer` still has no generating script, and the `TODO` repository URL must be filled before posting.

---

## 11. Second revision pass — remaining items (all except the repository URL)

### 11.1 `fig_boundary_layer` provenance restored
- `git log --all -S"fig_boundary_layer" -- '*.py'` returns nothing: no generating script ever existed in version control.
- New script `experiments/fig_boundary_layer.py` reconstructs it from the check-7 construction (η=0.5, γ=1, κ=2, λ=1, T=20, dt=0.05, pad P=20, deterministic signal `sin(0.6t)`), with the same `MAX_N` guard.
- Output: `b1=0.7726`, boundary-layer scale `3/b1=3.883`, interior deviation 0.01107 vs overall 0.55993. Regenerated PNG/PDF written into both `arxiv/figures/` and `figures/`; visually identical to the inherited v2 file (same curves, same amplitudes ≈±0.24), the only difference being the shading half-width (3.88 vs ≈3.35 in the old file, whose rule was undocumented). Caption updated to state the rule: three e-folds of the slowest rate `b₁`, plus the fact that the signal is a deterministic sinusoid.

### 11.2 Test suite retargeted at v5 and extended to the new claims
`experiments/test_all_results.py` docstring/banner now name `arxiv/optimal-trading-filters-v5.tex`. Four checks added; suite now **13/13 PASS** (7.9 s, 399 MB peak RSS):
- **Check 10 — lag-zero atom.** `c₁ = 1/√A` for exponential resilience with η=0 (rel ≤ 1.8e-14, three parameter sets); pure inventory risk (γ=0, *no impact*) gives `c₁ = 1/√λ` and `R(0.7) = −θ²/λ < 0` exactly — this is the check that pins C1's counterexample into the suite; and `1/|n̂₊|` decays with slope −1.0000 for η>0 and −0.7500 = −(1+β)/2 for the power law, so `c₁=0` in both. (First version of this check failed on a too-tight absolute tolerance — `1/|n̂₊(10⁷)| = 3.6e-6` for the power law — and was rewritten to test the decay exponent.)
- **Check 11 — Gohberg–Krein power-law factor.** `∫₀^T c₊(u,t)c₊(u,s)du = γ|t−s|^{−β}` at 9 (β,t,s) combinations, rel ≤ 1e-4, plus `c_β·Γ(β)sin(πν)/π = 1.000000000000`. This locks in the M1 fix.
- **Check 12 — U-shaped no-signal profile.** Solving `∫₀^T u(s)|t−s|^{−β}ds = const` numerically gives `u ∝ [t(T−t)]^{(β−1)/2}` with ratio constant to 1.4e-4 / 4.4e-4 / 7.2e-4 for β = 0.3 / 0.5 / 0.7. The paper's exponent is therefore correct as printed.
- **Check 13 — power-law boundary-layer envelope.** Deviation stays inside `C d^{−ν}` while local slopes are −0.68, −1.00, −2.13, all steeper than −ν = −0.25; the check asserts *both* (inside the envelope, and faster than the exponent), so it fails if the paper ever upgrades the envelope to a sharp rate without new analysis.

### 11.3 `GSS Ex. 2.30` pointer resolved
- Searched and fetched: the GSS 2012 abstract/description (SSRN 1531466; Math. Finance 22(3):445–474) is about measure-valued solutions and constrained trading times; no evidence of an "Example 2.30".
- The explicit closed form appears in Gatheral's lecture notes *Optimal order execution* (http://mathfinance.sns.it/wp-content/uploads/2010/12/Gatheral_Optim_Exec.pdf, "Example II: Linear market impact with power-law decay"): `u(s) = A[s(T−s)]^{±(1−γ)/2}` with the text "singular at t=0 and t=T", which forces the negative exponent, i.e. `(γ−1)/2` — matching the paper. Forde–Sánchez-Betancourt–Smith also refer to GSS for "the deterministic solution for the no-signal case `u₀(t)`".
- Action: the unverifiable numbered pointer was removed; the sentence now reads "the no-signal deterministic solution of \citet{GatheralSchiedSlynko2012}". The formula itself is independently confirmed by check 12.

### 11.4 Post-pass verification
- Rebuild: rc=0, **19 pages**, 0 errors, 0 undefined refs/citations, 2 overfull hboxes (`Output written … (19 pages, 482522 bytes)`).
- `experiments/test_all_results.py`: **13/13 PASS**.
- Remaining open item, by instruction: the `TODO: insert repository URL/DOI before posting` in the Code availability paragraph.
