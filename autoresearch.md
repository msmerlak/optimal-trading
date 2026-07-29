# Autoresearch — Wiener–Hopf paper v3 (best of v1 + v2)

**Target (qualitative):** produce `v3/` = best of v1 and v2 in clarity, style, structuring, figure selection; rewritten afresh.
**Benchmark (acceptance):** clean LaTeX build (0 errors / 0 undefined refs / 0 undefined citations / 0 missing figures / 0 overfull hboxes) + rubric below.
**Environment:** local, current working directory.
**Files in scope:** `v3/optimal-trading-filters-v3.tex`, `v3/figures/*`, `v3/optimal-trading-filters.bib`.

## Design decisions (evidence-based, from reading both sources + viewing all figures)
- **Formulation:** position-primary (position responds to expected return μ — the familiar Markowitz/aim-portfolio picture), per user instruction; revert to trade/rate formulation (u, α, Q) only at λ=0, where the position is non-stationary (power-law). = v2 axis.
- **Structure:** v2's factor→predict→combine spine (§2.1/2.2/2.3), plus v1's fuller Wiener–Hopf method exposition (§1.3: Paley–Wiener causality, triangular/Cholesky analogy, prediction-vs-control), plus v1's keywords/JEL/MSC block.
- **Restored from v1 (dropped in v2):** the value of information (§2.4) + causality gap sin(πβ/2) — verified by the numerical suite (check #4).
- **Figures (5, best of both):** value+causality-gap (v1 fig_value), filter magnitude across frictions (v1 fig_trading_filter), impact surfing (v2 fig2, cleaner), finite-horizon boundary layer (v2 fig3), policy structure/memory by kernel (v1 fig_filter_structure).
- **Prose:** v2's polished, motivation-first register; formalized Assumptions; general Lemma (A=A₋A₊).

## Rubric result
- Clarity: WH method exposition fuller than v2; position formulation familiar; value-of-info restored. PASS.
- Style: v2 register (no throat-clearing / negation-foils); AGENTS cadence. PASS.
- Structure: factor→predict→combine + consequences; 6 sections, 15 subsections. PASS.
- Figures: 5 selected on evidence, well-distributed. PASS.
- Build: see baseline. PASS.

## Baseline (iteration 0)
- Build: 0 errors, 0 undefined, 0 bad cite, 0 missing fig, 0 overfull. 20 pp. → ACCEPT.
