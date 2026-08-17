# Review plan — optimal-trading-filters-v5

Run date: 2026-08-17. Slug: `optimal-trading-filters-v5`.

## Artifact
- Primary: `arxiv/optimal-trading-filters-v5.tex` (LaTeX source, 435 lines, modified 2026-08-17 21:24; uncommitted per `git status`).
- Compiled: `arxiv/optimal-trading-filters-v5.pdf` (built 2026-07-29 22:31 — NOTE: PDF predates current tex, so PDF may be stale).
- Bibliography: `arxiv/optimal-trading-filters.bib`, `.bbl`.
- Figures: `arxiv/figures/*.{png,pdf}` (6 used in tex).
- Supporting: `experiments/*.py` (numerics + figure scripts), `RESULTS.md`, `CHANGELOG.md`, `reviews/`, prior versions `v1–v4`.
- Source type: local LaTeX manuscript (theory paper, quantitative finance / stochastic control), single author, arXiv-bound.

## Review criteria
1. Novelty and positioning vs Neuman–Voß, Abi Jaber et al., Forde et al., Lehalle–Neuman, Gârleanu–Pedersen.
2. Mathematical rigor: assumptions, statements of Lemma 1, Thms 1–2, Prop 1; proof completeness (appendix is compressed).
3. Claims validity: each headline claim traced to a proof step or numerical check.
4. Empirical/numerical rigor: do figures come from runnable scripts; are the "verified numerically" claims backed by artifacts in `experiments/`.
5. Baselines / recovery claims (Markowitz, aim portfolio, LN2019, NV2022, OW2013, GSS2012, FSS2022).
6. Reproducibility: figure scripts, seeds, data availability statement, code availability statement.
7. Figures/tables: existence, caption–content consistency, parameter consistency with text.
8. Related work coverage and citation accuracy.
9. Writing quality, notation consistency, typos.

## Verification checks
- V1: build the tex (pdflatex+bibtex) → errors/undefined refs/citations; confirm PDF is current or stale.
- V2: every `\includegraphics` target exists in `arxiv/figures/`; every `\ref`/`\citep` resolves.
- V3: figure parameter values in captions vs the generating scripts in `experiments/`.
- V4: numerical-verification claims in the text ("checked numerically against the reverse-Cholesky factor", "match the discrete adapted optimum to the resolution of the grid", "verified by direct kernel integration") → find and, where cheap, run the corresponding script.
- V5: run `experiments/test_all_results.py` if it exists and is self-contained.
- V6: internal consistency of formulas: Φ definition, sin(πβ/2) gap, ν=(1−β)/2, θ*=κ−2m, λ=2κγ/3 threshold, c_β, value formulas.
- V7: check bib entries for the key citations against external sources where a misattribution risk exists (e.g. Gârleanu–Pedersen 2013 vs 2016; Obizhaeva–Wang 2013).
- V8: check that stated empirical β range (0.2–0.6) and the derived ν∈(0.2,0.4) are consistent.
- V9: check statement of the code/data availability (none in tex → reproducibility gap).

## Deliverables
- Evidence: `outputs/.drafts/optimal-trading-filters-v5-review-evidence.md`
- Final: `outputs/optimal-trading-filters-v5-review.md`
