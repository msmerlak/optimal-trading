# Review plan — optimal-trading-filters-v2

## Artifact
- Identifier: `v2/optimal-trading-filters-v2.tex` (+ compiled `optimal-trading-filters-v2.pdf`, 18 pp.)
- Source type: local LaTeX manuscript, applied math / quantitative finance paper
- Companion artifacts in-repo:
  - `v2/experiments/test_all_results.py` — numerical verification suite (9 checks)
  - `v2/experiments/fig1..fig5*.py` + `v2/figures/*` — figure-generation scripts (real computation)
  - `reviews/v2-style-review.md` — prior style-only review (subagent, this session)
  - `v2/notes/paper-outline-v2.md`, `v2/notes/causality-gap-exp-vs-powerlaw.md` — design notes
  - `experiments/nv_vs_stationary.py` — independent Neuman–Voß Riccati check

## Review criteria
1. Novelty: positioning vs Gatheral–Schied–Slynko, Forde–Sánchez-Betancourt–Smith,
   Neuman–Voß, Gârleanu–Pedersen, Abi Jaber–Neuman; what is genuinely new
   (projected-inverse identity use, sin(πβ/2) law, memory framing, flow-reversal threshold).
2. Empirical rigor: no market data used — check that the paper does not overclaim empirics;
   numerical verification quality.
3. Baselines: fairness of the Abi Jaber–Neuman computational comparison (O(n²) claim).
4. Reproducibility: are formulas verifiable from the paper alone; scripts exist but are not
   referenced/shipped with the paper.
5. Claims validity: each proposition against the in-repo numerical checks (9/9) and against
   known caveats found during drafting (position-filter L² claim at pure power-law λ=0).
6. Figures/tables: caption–content consistency, notation consistency, Table 1 provenance.
7. Related work: coverage and accuracy of attributions.
8. Writing quality: incorporate prior style review findings (titles, self-promotion tics).

## Verification checks
- Lemma 1 / Thm 1–2, Props 1–3: cross-check against `test_all_results.py` output (9/9 PASS).
- sin(πβ/2): Appendix C derivation vs quadrature (check 4) — verified this session.
- NV recovery: independent algebraic-Riccati poles vs b1,b2 (check 9) — machine precision.
- Table 1: provenance = reverse-order Cholesky discrete optimum (check 6 reproduces rows).
- Known unresolved issue to re-verify in the text: "position filter lies in L² for every
  kernel" (§2.3, line ~213) vs the λ=η=0 power-law divergence found numerically this session.
- Figures: regenerate-ability (scripts run), caption consistency with v2 notation.
- Data/code availability: no statement in paper — flag.
- Compile status: 0 errors, 0 undefined refs (checked this session).

## Method
Lead-owned review (full context held; style subagent already ran — reuse its report).
Evidence notes first, then single final review with inline annotations.
