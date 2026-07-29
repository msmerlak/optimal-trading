# v3 Round-1 Review — Internal Consistency & Reproducibility

**Artifact:** `v3/optimal-trading-filters-v3.tex` (503 lines, 5 figures)
**Companions inspected:** `v3/optimal-trading-filters.bib`, `v3/figures/*.png`, `experiments/make_figures.py`, `experiments/rate_response_2ema.py`, `v2/experiments/test_all_results.py`
**Angle:** notation consistency, cross-reference/bibliography integrity, figure↔caption agreement, "causality gap" wording, reproducibility of the verification scripts.
**No files were edited.**

---

## Summary

The paper is in good internal shape. It compiles cleanly with **no undefined references, no undefined citations, and no overfull/underfull hboxes**. All 33 bibliography keys are used, and the two available verification scripts run to completion (`rate_response_2ema.py` exit 0; the v2 aggregate verifier passes 9/9). The core notation (μ vs α, N vs Q, Φ(θ)=n̂₊(iθ), ν=(1−β)/2, c_β) is internally consistent, and the "causality gap = ratio v/v_ant" convention is used consistently across abstract, §value, §power-law, figure caption, and conclusion.

Two issues rise to blocker level: (1) the value figure carries a **baked-in panel title that contradicts its own caption and the body text** ("fixed signal variance" vs "fixed appreciation variance"), and (2) the companion aggregate verifier named in the task (`experiments/test_all_results.py`) **does not exist in the v3 tree** — only a stale v2 copy exists, which mislabels a result that is now in the paper. The remainder are cheap notation/caption polish items.

---

## BLOCKERS

### B1 — Value figure: baked-in title contradicts caption and body text
- **Where:** Figure `fig:value` panel (a); source `experiments/make_figures.py:171`; caption `optimal-trading-filters-v3.tex:290`; body `:281`.
- **Evidence:**
  - `make_figures.py:171`: `ax[0].set_title("(a) value vs signal speed (fixed signal variance)")` — verified visually in `figures/fig_value.png` (title reads **"fixed signal variance"**).
  - Caption (`:290`): "Value rate $v(\theta)$ against signal speed **at fixed appreciation variance** (normalized to $\theta=1$)".
  - Body (`:281`): "**at fixed appreciation variance** a faster signal carries a proportionally larger expected return, $\mu=\theta\alpha$".
  - `rate_response_2ema.py` output header: "Value **at fixed appreciation variance** V=1: v(theta) = theta^2/(2 Phi^2)".
- **Which is correct:** the caption/text/script are correct. The normalization holds `Var(α)` (the appreciation innovation variance σ²) fixed — `v=σ²θ/4Φ²` with "σ² that of α" (`:266`). The figure's baked title "fixed **signal** variance" is the wrong label and must be regenerated to read "fixed appreciation variance."
- **Why blocking:** a reader-facing, in-figure contradiction of the caption and the physics; the whole speed-premium story of §value hinges on which variance is held fixed.

### B2 — `experiments/test_all_results.py` is absent from the v3 tree (reproducibility contract)
- **Where:** task-named companion `experiments/test_all_results.py`; acknowledgements (`:497`) "Verification scripts and figure code are available from the author"; abstract (`:41`) "All closed forms are checked against discretized adapted optima."
- **Evidence:**
  - `find . -name test_all_results.py` → only `./v2/experiments/test_all_results.py`; **not present under `experiments/`.**
  - The v2 copy runs and passes (`python v2/experiments/test_all_results.py` → `9/9 CHECKS PASSED`, EXIT=0), but its docstring says it verifies **`v2/optimal-trading-filters-v2.tex`** and it references v2 labels (`eq:N`, `eq:exp-factor`, `eq:nv-factor`) not present in v3.
  - Its check 4 prints `PASS 4. Causality-gap identity v/v_ant = sin(pi beta/2) (supplementary; not in paper)` — but in **v3 this IS in the paper** as `eq:sinlaw` (`:287`). So the only aggregate verifier is stale relative to v3.
- **Why blocking:** the paper asserts every closed form is checked and that verification scripts are available, but the aggregate verifier for v3 is not in the v3 experiment tree; the reproducibility claim is not backed in-repo. This is a packaging/repro gap, **not a demonstrated math error** — the underlying identities do pass under the v2 script.

---

## FIXES-WORTH-DOING-NOW

### F1 — Value figure panel (b): notation drift `v_ad` vs paper's `v`
- **Where:** `experiments/make_figures.py:177-178` → `figures/fig_value.png` panel (b); Table `tab:notation` (`:139`) defines `v, v_ant` (no `v_ad`); caption `:290` and `eq:sinlaw` use `v/v_{\rm ant}`.
- **Evidence:** `make_figures.py:177`: title `$v_{\rm ad}/v_{\rm ant}=\sin(\pi\beta/2)$`; `:178`: ylabel `$v_{\rm ad}/v_{\rm ant}$`. The paper never defines `v_ad`; the notation table (`:139`) and `eq:sinlaw` use plain `v`. Regenerate the panel with `v/v_ant` to match the paper symbol.

### F2 — Stale comment in the (only) aggregate verifier
- **Where:** `v2/experiments/test_all_results.py` check-4 label.
- **Evidence:** prints "supplementary; not in paper" for the sin-law, which is now `eq:sinlaw` in v3. If this script is promoted/copied into `experiments/` for v3 (see B2), update the label and the v2 equation references so the verifier tracks the shipped paper.

---

## OPTIONAL

### O1 — Notation-table caption under-states where the rate variable is used
- **Where:** `tab:notation` caption (`:152`) vs §finite-horizon (`:375`).
- **Evidence:** caption says "the rate variable is used **for the scale-free kernel of Section 3**, where the position is non-stationary." But §4 also works in the rate: `:375` "On the window the working variable is again the rate, which carries the terminal constraint and the endpoint blocks." Consider "…for the scale-free kernel of §3 and on the finite horizon of §4."

### O2 — Cross-references need a 4th `pdflatex` pass to stabilize
- **Evidence:** after the task's sequence (`pdflatex; bibtex; pdflatex; pdflatex`), the 3rd pass still emitted `LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.` A 4th pass was clean (`stable now`). No undefined refs result, but the final PDF from a strict 3-pass build may carry slightly stale cross-refs (hyperref `.out` oscillation). Recommend one extra `pdflatex`.

### O3 — `rate_response_2ema.py`: discrete vs analytic agreement degrades at high θ, no PASS/FAIL tolerance
- **Evidence (EXIT=0):** at `eta=0.05, theta=6.0`: `R_analytic=+3.7274  R_discrete=+1.6985  (match 2.0e+00)`; at `eta=0` reference `theta=6.0`: `R_analytic=-7.0149  R_discrete(eta=1e-4)=-5.5874`. The script prints the raw absolute difference (labeled "match") but no tolerance verdict; the sign and threshold claims (θ*=κ−2m=+0.211, matching `eq:threshold` with κ=2,γ=1,λ=1) and `R>0` checks hold. The large high-θ gaps are grid-discretization artifacts of the check, not paper errors, but a short note ("discrete check is coarse for fast signals") would prevent misreading the printed numbers as a failed match.

### O4 — `fig:structure` panel (b): the Markowitz "spike" is only a small annotation
- **Where:** caption `:433` "the Markowitz limit is an instantaneous spike"; `make_figures.py:219` `ax[1].annotate("Markowitz: instantaneous ($\\delta$)", xy=(0.02, 6), fontsize=8, color="0.4")`.
- **Evidence:** the legend shows only three curves (exponential, temp+exp, power-law); the fourth "kernel" named in the caption is represented by a faint grey annotation, easy to miss. Acceptable (a δ cannot be plotted on log-log), but consider making the annotation more prominent or noting "(annotated)" so the caption's four items match what the eye finds.

---

## IGNORE / DEFER (verified consistent — no action)

- **Trading-filter figure, ω_c vs ω_\*** (task item iii): `figures/fig_trading_filter.png` panel (b) x-axis stops at ω=10 and marks **only** ω_c (dotted line ≈0.34, matching ω_c=(λ/γc_β)^{1/(1+β)}=0.341 for λ=0.5,γ=1,β=0.5). The caption (`:337`) promises **only** ω_c ("the risk crossover $\omega_c$ marking the edge of the plateau"); ω_\*=(γc_β/η)^{1/(1−β)}≈70 for η=0.3 is off-plot and correctly not drawn or promised. **Consistent — nothing to fix.**
- **"Causality gap = ratio v/v_ant"** (task item on wording): consistent everywhere — abstract "a causality gap $\sin(\pi\beta/2)$" (`:41`), §value "the ratio $v/v_{\rm ant}\le1$, the fraction … that survives" (`:281`), `eq:sinlaw` "$v/v_{\rm ant}=\sin(\pi\beta/2)$" (`:287`), figure caption (`:290`), conclusion "keeping a fraction $\sin(\pi\beta/2)$ of the value" (`:462`). The **difference** `v_ant − v` is deliberately named "shortfall" (`:281`), distinct from the "gap" (ratio); no leftover "gap = difference / retained fraction / complementary fraction" wording remains.
- **Bibliography:** `bibtex` exit 0, `.blg` shows 0 warnings; all 33 keys used. `LionsMagenes1972` is cited via `\citep[Ch.~1]{LionsMagenes1972}` (`:482`) — flagged as "not cited" only by a naïve regex that misses the optional `[…]` argument; it is genuinely used. No undefined citations.
- **Figure ↔ caption parameter labels** (spot-checked, all agree):
  - `fig:value`(a): 4 curves present (pure risk ∝θ², exp+risk, exp+temp+risk "saturates", power-law ∝θ^{1−β}) — matches caption's four regimes and the saturating exp+temp curve is shown. ✓ (title issue is B1.)
  - `fig:filter`(a) slopes: β=0.2→−0.6, 0.4→−0.7, 0.6→−0.8 = −(1+β)/2. ✓
  - `fig:surf`: θ*=κ (dotted at θ=2) and λ=2κγ/3 (dotted at ≈1.33) for κ=2,γ=1 — matches caption's "boundary meets the axes at θ=κ and λ=2κγ/3." ✓
  - `fig:bdry`: x-axis 0–20 = T=20; params (η=0.5,γ=1,κ=2,λ=1,T=20) match caption. ✓
  - `fig:structure`(a) b1→0 as λ→0, κ resilience line; (c) slopes β=0.2→−0.4,0.4→−0.3,0.6→−0.2 = (β−1)/2, matching caption. ✓
- **Notation cross-checks:** μ vs α (α_t=E_t∫μ, α=μ/θ for OU), N vs Q=N(−∂²)⁻¹, q̂=n̂/ω², Φ(θ)=n̂₊(iθ), ν=(1−β)/2, c_β=2Γ(1−β)sin(πβ/2), Φ=√A(m+θ)/(κ+θ) → θ*=κ−2m — all internally consistent and consistent with `rate_response_2ema.py` (θ*=0.211).

---

## Commands run (evidence)

| Command | Result | Note |
|---|---|---|
| `pdflatex ×1; bibtex; pdflatex ×2` (in `v3/`) | all EXIT=0 | clean build |
| `grep -i undefined …-v3.log` | (empty) | no undefined refs/citations |
| `grep -c "Overfull \hbox" …-v3.log` | `0` | also 0 underfull |
| `cat …-v3.blg` warnings | `0` | bibtex clean |
| bib-key vs cite-key diff | all 33 used | `LionsMagenes1972` cited via `\citep[…]{}` |
| `python experiments/rate_response_2ema.py` | EXIT=0 | θ*=0.211 matches `eq:threshold`; value saturation V/2η matches text |
| `python v2/experiments/test_all_results.py` | EXIT=0, `9/9 PASSED` | but targets **v2** tex; stale check-4 label |
| `find . -name test_all_results.py` | only `v2/experiments/…` | **missing from v3 `experiments/`** (B2) |
| 4th `pdflatex` pass | `stable now` | 3-pass build leaves cross-refs unstable (O2) |

---

## Inline Annotations

> "(a) value vs signal speed (fixed signal variance)"  — `make_figures.py:171`, baked into `fig_value.png`
**[B1] BLOCKER:** Contradicts the caption ("at fixed appreciation variance", `:290`) and body ("at fixed appreciation variance… μ=θα", `:281`). The normalization fixes `Var(α)=σ²`; the correct label is "fixed appreciation variance." Regenerate the figure.

> "All closed forms are checked against discretized adapted optima." (abstract, `:41`) … "Verification scripts and figure code are available from the author." (`:497`)
**[B2] BLOCKER (reproducibility):** The aggregate verifier `experiments/test_all_results.py` is absent from the v3 tree; only `v2/experiments/test_all_results.py` exists, which verifies `optimal-trading-filters-v2.tex` and labels the sin-law as "not in paper" though v3 states it as `eq:sinlaw`. Ship a v3 verifier or clearly point to one.

> `ax[1].set_title(r"(b) cost of causality: $v_{\rm ad}/v_{\rm ant}=\sin(\pi\beta/2)$")` — `make_figures.py:177`
**[F1] FIX-NOW:** `v_{\rm ad}` is undefined in the paper; Table `tab:notation` and `eq:sinlaw` use plain `v`. Use `v/v_{\rm ant}`.

> "the rate variable is used for the scale-free kernel of Section~\ref{sec:fractional}, where the position is non-stationary." — `tab:notation` caption, `:152`
**[O1] OPTIONAL:** §4 (`:375`) also works in the rate variable ("the working variable is again the rate"). The caption under-states the rate variable's scope.

> "the Markowitz limit is an instantaneous spike." — `fig:structure` caption, `:433`
**[O4] OPTIONAL:** Panel (b) shows only three legend curves; the Markowitz item is a faint grey annotation (`make_figures.py:219`), not a plotted curve. Fine in principle (a δ is unplottable) but easy to miss.

> "with the risk crossover $\omega_c$ marking the edge of the plateau." — `fig:filter` caption, `:337`
**[OK]:** Verified consistent. Panel (b) marks only ω_c; ω_\*≈70 (η=0.3) is beyond the ω=10 axis and is correctly not promised.

> "The \emph{causality gap} is the ratio $v/v_{\rm ant}\le1$… The shortfall $v_{\rm ant}-v$ equals…" — `:281`
**[OK]:** "Gap = ratio" and "shortfall = difference" are used consistently and distinctly throughout (abstract, §value, `eq:sinlaw`, caption, conclusion). No leftover conflicting definitions.

---

## Sources

No external/web sources were consulted; this was an in-repo consistency/reproducibility audit. Local artifacts inspected:
- `v3/optimal-trading-filters-v3.tex`, `v3/optimal-trading-filters.bib`, `v3/optimal-trading-filters-v3.{log,blg}`
- `v3/figures/{fig_value,fig_trading_filter,fig_impact_surfing,fig_boundary_layer,fig_filter_structure}.png`
- `experiments/make_figures.py`, `experiments/rate_response_2ema.py`, `v2/experiments/test_all_results.py`