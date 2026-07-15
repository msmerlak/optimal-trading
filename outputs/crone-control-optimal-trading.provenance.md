# Provenance: outputs/crone-control-optimal-trading.md

**Date:** 2026-06-27
**Final artifact:** `outputs/crone-control-optimal-trading.md` (verified on disk)
**Plan:** `outputs/.plans/crone-control-optimal-trading.md` (verified on disk)
**Companions:** `outputs/fractional-kernels-optimal-execution.md`, `papers/fractional-derivative-optimal-execution.md`

## Workflow executed

1. Plan written to `outputs/.plans/crone-control-optimal-trading.md`.
2. Direct searches (no `researcher` subagent — topic narrow):
   - `web_search` × 5 queries: CRONE generations, fractional control
     finance, FOPID tuning, ORA implementation, fractional control of
     financial systems.
   - `fetch_content` × 8 URLs: spot-check of canonical CRONE refs,
     PID-trading paper, Quant.SE thread, MDPI fractional-financial-system
     paper, JAND CRONE review, IEEE 1993 SMC paper, MATLAB Central ORA.
3. `alpha` CLI was attempted; `alpha search` syntax adjusted but not
   re-run because the web_search results already covered every paper
   the alpha index would have surfaced (Forde et al., Abi Jaber–Neuman
   etc. already in the companion review).
4. Synthesis → `outputs/crone-control-optimal-trading.md`.
5. URL spot-check: 5/5 canonical sources resolved (one returned a thin
   cookie-walled body but the DOI is valid).
6. `reviewer` subagent dispatched; returned 0 FATAL, 7 MAJOR, 8 MINOR.
7. All MAJOR issues and the high-value MINOR issues (canonical DOIs)
   addressed via `edit` against the artifact; replacements verified by
   `grep`.
8. Provenance file (this document) written.

## Sources consulted vs. accepted vs. rejected

### Accepted (cited in artifact)

CRONE / fractional control:
- Oustaloup 1998, ESAIM Proc. — fractal robustness survey.
- Oustaloup–Mathieu 1993, IEEE SMC — third-generation CRONE.
- Sabatier–Lanusse–Melchior–Oustaloup 2013, JAND — review.
- Lanusse–Sabatier–Nelson Gruel–Oustaloup, second/third generation.
- Lanusse–Malti–Melchior 2013, Phil. Trans. R. Soc. A — toolbox tutorial.
- Lanusse–Oustaloup–Sabatier–Mathieu 2011, J. Vib. Control — Bode-optimal CRONE.
- Oustaloup–Levron–Mathieu–Nanot 2000, IEEE TCAS-I — ORA method.
- Tepljakov et al. 2018, ISA Trans. — FOPID tuning rules.
- Wang et al. 2019, Int. J. Robust Nonlin. Control — robust FOPID, fractional plant.
- MDPI 2020 — comparison of Oustaloup-filter variants.

Finance / control:
- Stehlík et al. 2023, J. Risk Financial Manag. — PID for trading.
- Quant.SE thread on PID controllers for trading.
- Dadras–Momeni 2010, Physica A — fractional sliding-mode for chaotic finance ODE.
- Tacha et al. 2023, Fractal Fract. — control of fractional chaotic financial system.
- Hu–Øksendal 2003, Infin. Dimens. Anal. — fractional white-noise calculus.
- Han–Pun–Wong 2019, Appl. Math. Finance — portfolio under rough fractional vol.
- Bäuerle–Desmettre 2018, arXiv:1809.10716 — portfolio in rough Heston.
- Sun et al. 2024, Front. Appl. Math. Stat. — FSV for microstructure.
- J. Math. Model. Finance — stochastic-fractional optimal control for portfolio.

Optimal execution (context only, full bibliography in companion):
- Gatheral–Schied–Slynko 2012, Math. Finance.
- Forde–Sánchez-Betancourt–Smith 2022, Quant. Finance.
- Abi Jaber–Neuman 2022 (arXiv:2211.00447).
- Jusselin–Rosenbaum 2020.

### Rejected / not used

- MDPI 2024 wind-energy CRONE (Investigation of Robust FO Control…) —
  on-topic for CRONE practice but adds nothing beyond Lanusse et al.;
  cut to keep the artifact focused.
- *Beyond the Waterbed Effect* (ACC 2018, Karbasizadeh et al.) — about
  non-linear reset within CRONE, tangential to the execution
  application; cut.
- Various per-application CRONE case studies (active suspension, BLDC
  micromotor) — engineering specifics, no transfer to trading.
- Frontiers FSV paper — *plant-side* fractional, kept only as a
  pointer; not used to justify any controller-side claim.

### URL verification status

- Spot-checked via `fetch_content`: 5 canonical CRONE / finance URLs
  resolved. Sagepub JVC link returned thin body (cookie wall) but the
  DOI is valid and confirmed indirectly via search-result metadata.
- Remaining URLs (~25) were captured directly from search-result
  panels and not re-fetched individually; format-checked for
  well-formedness only.

### Subagents invoked

- `reviewer` — 0 FATAL, 7 MAJOR, 8 MINOR. All MAJOR + high-value MINOR
  resolved.
- `verifier` — not available in current agent registry; URL verification
  performed inline via `fetch_content`.
- `researcher` — not invoked (topic narrow enough for direct search).

## Verification log

| Claim | Source(s) | Status |
|-------|-----------|--------|
| Three CRONE generations exist with the described frequency-domain templates | Sabatier–Lanusse 2013; Oustaloup–Mathieu 1993; ESAIM 1998 | verified via search snippets and JAND fetch |
| Fractal-robustness theorem (damping ratio depends only on non-integer order) | ESAIM 1998 PDF | verified via direct fetch of PDF abstract |
| ORA: $s^\alpha \approx \prod (1+s/\omega_z)/(1+s/\omega_p)$ | MATLAB Central #3802; MDPI 2020 (variants) | verified |
| Stehlík et al. PID-trading paper exists, uses integer-order PID | JRFM 2023 fetched | verified |
| No CRONE → trading application found | absence in 5 search queries; reviewer accepted with hedge | hedged in artifact |
| Companion-paper Theorems 4.1/5.1/6.1 referenced exist | grep of `papers/fractional-derivative-optimal-execution.md` | verified |
| Robustness transfer to execution (§4.1) | none — labelled proposed result; LTI caveat added per reviewer | conjecture, flagged |

## Files produced this run

- `outputs/.plans/crone-control-optimal-trading.md` — plan
- `outputs/crone-control-optimal-trading.md` — final cited literature review
- `outputs/crone-control-optimal-trading.provenance.md` — this file

No intermediate `*-research-*.md` files were created (researcher
subagent not invoked).
