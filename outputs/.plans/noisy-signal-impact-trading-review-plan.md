# Review Plan — noisy-signal-impact-trading

## Artifact identifier and source type

- **Artifact identifier:** `noisy-signal-impact-trading`
- **Source type:** Local Markdown research draft
- **Primary source path:** `papers/noisy-signal-impact-trading.md`
- **Derived slug:** `noisy-signal-impact-trading`
- **Review output:** `outputs/noisy-signal-impact-trading-review.md`
- **Evidence notes:** `outputs/.drafts/noisy-signal-impact-trading-review-evidence.md`

## Review criteria

1. **Novelty** — identify what is claimed as new vs pedagogical or already known in causal Wiener--Hopf / propagator execution literature.
2. **Empirical rigor** — check whether any empirical or numerical claims are made and whether supporting experiments exist.
3. **Baselines** — assess comparison to standard models such as Gârleanu--Pedersen, Gatheral/Schied/Slynko, Lehalle--Neuman, Abi Jaber--Neuman, and noisy-signal Wiener-filter baselines.
4. **Reproducibility** — inspect availability of equations, assumptions, runnable checks, scripts, dependencies, and result logs.
5. **Claims validity** — verify mathematical derivations where feasible, especially AR(1) × exponential scalar collapse, noisy-signal separation, power-law/fractional derivative claims, and no-dynamic-arbitrage statements.
6. **Figures/tables** — inspect all reported figures/tables for provenance and whether quantitative entries are supported.
7. **Metrics** — identify reported metrics or quantitative checks, their source, and whether they are reproducible.
8. **Related work** — check whether literature positioning is adequate and whether claims marked tentative should remain tentative.
9. **Writing quality** — assess clarity, scope control, definitions, notation consistency, and reviewer-facing framing.

## Verification checks needed

- **Claims:**
  - Re-derive or sanity-check key equations: objective (1), Legendre conjugate (2), causal Wiener--Hopf solution (6), AR(1) projection (7)--(12), Markov closure (12a--12c), OU/power-law constants (15b--15c), noisy Wiener filter (17)--(20).
  - Distinguish deterministic sequence optimization from stochastic filtering and ensure expectations/PSD notation are consistent.
  - Check whether positive definiteness of symmetrized propagator kernel is sufficient as stated for no dynamic arbitrage under the draft conventions.
- **Figures/tables:**
  - Identify all figures/tables and verify that entries are derivations, literature claims, or placeholders; flag unsupported quantitative values.
- **Reported metrics:**
  - Inspect any experiment logs or referenced scripts, especially `experiments/markov_closure_check.py` and `experiments/results/markov_closure_check.out` if cited by the artifact.
- **Data/code availability:**
  - Check for local experiment code and result files; record exact paths and whether commands were run in this review.
- **Linked artifacts/citations:**
  - Inspect local references and, where material, use paper/search tools for external claims. If network/citation verification is not performed, mark it as unverified rather than as a paper weakness.

## Execution log

- Created required directories: `outputs/`, `outputs/.plans/`, `outputs/.drafts/`.
- Proceeding directly to artifact inspection and evidence-note drafting.
