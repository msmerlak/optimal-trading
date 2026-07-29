# Review Plan — optimal-trading-filters

## Artifact
- **Identifier**: `v2/optimal-trading-filters-v2.tex` (LaTeX source, ~487 lines)
- **Source type**: local LaTeX file (applied-math paper: optimal trading via Wiener–Hopf factorization)
- **Companion**: `v2/optimal-trading-filters.bib`, `v2/figures/*.png`, `v2/experiments/test_all_results.py`
- **State**: actively edited by the user; must read live from disk. Recently reformulated intro to position/N/μ form; §2 renamed "The stationary solution".

## Review focus (as requested)
1. **Readability** — does each section read linearly; is motivation present; are transitions clean; any deferred/forward-reference tangles.
2. **Symbols introduced in the right place** — every symbol defined at/before first use; no orphan or duplicated definitions; consistency after the recent N-vs-Q / μ-vs-α reformulation (known seam risk).
3. **Style / LLM giveaways** — throat-clearing, "not X but Y" negation-foils, empty intensifiers, rhetorical questions, "significance gavel", listy hedging, over-signposting, em-dash overuse, "rich tapestry"-type filler.
4. **Structure** — optimal ordering of sections/subsections; factor→predict→combine spine; appendix placement; whether §3/§4/§5 order serves the argument.

## Standard review criteria (secondary, this is a methods/theory paper)
- Novelty & positioning vs related work (AJN, NV, LN, GSS, Forde, GP).
- Claims validity — are theorems/props stated with hypotheses; is the sin(πβ/2) law and causality-gap claim supported.
- Empirical rigor — numerical verification suite (test_all_results.py); figures provenance.
- Reproducibility — code/figure availability statement; scripts present.
- Figures/tables — Table 1 notation; 5 figures; captions.
- Metrics — n/a (theory paper); check any quantitative claims trace to script/derivation.
- Related work completeness & fairness.

## Verification checks
- [ ] N vs Q consistency: §1 (N=N_-N_+) vs §2 (Q=Q_-Q_+); eq:symbol now n̂ — does §2.1 prose still call it q̂?
- [ ] μ vs α seam between intro (μ/N/position) and §2 (α/Q/rate).
- [ ] Every symbol in Table 1 used; every used symbol in Table 1.
- [ ] Cross-references resolve (compile: 0 undefined).
- [ ] Theorem/Prop/Lemma hypotheses present; proofs in appendices exist.
- [ ] Citations resolve (bibtex clean); attributions (LN2019, NV2022, OW2013, GSS2012) accurate.
- [ ] Figures exist on disk; captions match.
- [ ] Reproducibility statement + scripts exist.

## Method
- Lead-owned (single local file; delegation would add overhead). No subagents.
- Read full source from disk. Compile to confirm 0 errors / 0 undefined. Spot-check symbol first-use order by grep.
- Evidence → `outputs/.drafts/optimal-trading-filters-review-evidence.md`.
- Final → `outputs/optimal-trading-filters-review.md`.
