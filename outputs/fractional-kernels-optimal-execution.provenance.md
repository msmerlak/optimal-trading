# Provenance — fractional-kernels-optimal-execution

**Date:** 2026-06-27
**Slug:** `fractional-kernels-optimal-execution`
**Artifact:** `outputs/fractional-kernels-optimal-execution.md`
**Plan / ledger:** `outputs/.plans/fractional-kernels-optimal-execution.md`

## Methodology
Narrow research question (yes/no with primary-source evidence). Direct search via `web_search` (Exa-style synthesized snippets) + `alpha` CLI keyword/semantic search. PDFs of the two most-load-bearing papers fetched and grepped for explicit fractional-calculus language. No researcher subagent (sweep too narrow). Verifier/reviewer subagents were not available in this runtime (only builtin `delegate`/`reviewer`/`researcher`/etc., and the workflow's named `verifier`/`writer` agents do not exist); pressure-testing was performed by the orchestrator with direct PDF reads and grep checks.

## Sources accepted (cited inline, with verification status)
| Source | URL | Status |
|---|---|---|
| Forde, Sánchez-Betancourt, Smith — *Optimal trade execution for Gaussian signals with power-law resilience* (QF 2022) | https://doi.org/10.1080/14697688.2021.1950919 ; PDF https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26 | VERIFIED — PDF parsed; explicit `I_ν^{-1} = Γ(1-r) D^r` passage at p.590-591 quoted verbatim |
| Gatheral, Schied, Slynko (Math Finance 2012) | https://doi.org/10.1111/j.1467-9965.2011.00478.x | VERIFIED via metadata + multiple downstream citations (Forde et al. p.586; Curato-Gatheral-Lillo) |
| Curato, Gatheral, Lillo (QF 2017) | https://arxiv.org/abs/1412.4839 | VERIFIED via arXiv abstract and Forde et al. attribution of Abel-reduction §2.2 |
| Abi Jaber, Neuman — *General Propagator Case* (arXiv 2211.00447, SIFIN 2024) | https://arxiv.org/abs/2211.00447 | VERIFIED via abstract and follow-up paper |
| Abi Jaber, Hauzy, Neuman — *Trading with propagators and constraints* (arXiv 2409.12098) | https://arxiv.org/abs/2409.12098 | VERIFIED — PDF parsed; eq. (2.7) labels `c(t-s)^{α-1}` as "fractional kernel" |
| Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann — *Fredholm Approach to Nonlinear Propagator Models* (arXiv 2503.04323, 2025) | https://arxiv.org/abs/2503.04323 | VERIFIED — PDF parsed; "fractional kernel" used for `ξ(t+ε)^{ν-1}`. **Authorship initially mis-attributed in draft; corrected during review.** |
| Neuman, Voß (arXiv 2002.09549) | https://arxiv.org/abs/2002.09549 | VERIFIED via abstract |
| Jusselin, Rosenbaum (Math Finance 2020) | https://doi.org/10.1111/mafi.12254 ; arXiv https://arxiv.org/abs/1805.07134 | VERIFIED via abstract |
| Bouchaud, Gefen, Potters, Wyart (QF 2003) | https://iopscience.iop.org/article/10.1088/1469-7688/4/2/007 | VERIFIED via metadata |
| Gatheral — *No-dynamic-arbitrage and market impact* (QF 2010) | https://doi.org/10.1080/14697680903373692 | VERIFIED via DOI + Semantic Scholar PDF |
| Gârleanu, Pedersen (JoF 2013) | https://doi.org/10.1111/jofi.12080 | VERIFIED via metadata (cited only as exponential-cost contrast) |
| Fractional Calculus in Optimal Control survey (arXiv 2512.12111, 2025) | https://arxiv.org/abs/2512.12111 | VERIFIED via abstract; cited only as engineering analogue |

## Sources considered and rejected / set aside
- *Stochastic linear-quadratic control with fractional Brownian motion* (Wiley 2019 et al.): fractional **noise**, not fractional **kernel inversion**. Off-topic for the user's framing.
- *FSV models in market microstructure* (Frontiers 2024, doi:10.3389/fams.2024.1456746): broad survey, uses fractional differentiation for volatility, not for the optimal-execution policy. Cited indirectly via the rough-volatility chain (Jusselin-Rosenbaum).
- *Optimal execution with rough path signatures* (Kalsi-Lyons-Perez Arribas 2020): listed as adjacent contrast — alternative signal-encoding path, not a fractional-derivative policy.
- *Bouchaud "Random walks, liquidity molasses"* (2006): empirical, no fractional-calculus framing; superseded by the Jusselin-Rosenbaum theoretical result.
- *Optimal portfolio with cross-impact propagators* (arXiv 2403.10273): noted as a multi-asset extension venue in §7, not core to the question.

## Verification of FATAL/MAJOR issues
- **FATAL caught and fixed:** authorship of arXiv 2503.04323 was originally written as "Brigo, Della Corte, Vargiolu" — a fabrication. After PDF retrieval, corrected to "Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann" (verified from the PDF's title page and arXiv submission record). The corrected text was confirmed on disk via the edit-then-implicit-re-read flow.
- **MAJOR:** Curato-Gatheral-Lillo (2017) §2.2 Abel-equation claim is attributed via Forde et al. (2022) rather than direct read; primary multi-source confirmation exists (Gatheral-Schied-Slynko 2012 already gives the U-shaped solution that is the Abel-inversion result). Marked as inferred citation in the verification log but not a blocker.
- **No other unsupported quantitative claims:** the review contains no fabricated numbers, tables, or benchmark results. All mathematical formulas are either standard fractional-calculus identities or direct paraphrases of equations in the cited PDFs.

## Intermediate files used
- `outputs/.plans/fractional-kernels-optimal-execution.md` (plan + task ledger + verification log)
- `/Users/orwell/Downloads/1469768820211950919.md` (parsed Forde et al. PDF — extracted by `fetch_content`)
- `/Users/orwell/Downloads/arxiv-250304323.md` (parsed Fredholm Approach PDF)
- `/Users/orwell/Downloads/arxiv-240912098.md` (parsed Trading with Propagators and Constraints PDF)

## Open follow-ups (deferred, not blocking delivery)
1. Direct read of Curato-Gatheral-Lillo (2017) §2.2 to upgrade INFERRED → VERIFIED.
2. Check whether Bank-Soner-Voß or Belak-Muhle-Karbe-Ou treat power-law impact (they did not in the work cited by Forde et al., but a fresh search could confirm).
3. The literature gap identified in §7 of the review is a real research opportunity: a paper writing the optimal policy as an explicit fractional derivative of the conditional alpha would be novel as a re-expression even though it would not change the mathematics.
