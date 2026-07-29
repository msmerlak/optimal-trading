# Provenance — execution-solution-methods

- **Date:** 2026-07-21
- **Run type:** Literature-accuracy review (not a lab/PI publication-corpus review). Object: `v2/optimal-trading-filters-v2.tex`.
- **Question:** Does the paper accurately represent existing solution methods for optimal trading with impact? Are any missing?

## Files
- Plan: `outputs/.plans/execution-solution-methods.md`
- Evidence log: `notes/execution-solution-methods-publications.md`
- Final review: `outputs/execution-solution-methods.md`
- This provenance: `outputs/execution-solution-methods.provenance.md`
- (No `-research-*.md` researcher files: gather was lead-owned; the sweep was narrow and the lead had full context on the object paper.)

## Method
- Lead-owned gather: `web_search` (6+4 queries across method families and candidate omissions) + `fetch_content` on arXiv abstracts (2409.12098, 2211.00447). One `alpha_ask_paper` on 2211.00447 failed ("fetch failed"); AJN's equation type resolved from its arXiv abstract instead.
- Verify: `reviewer` (user) subagent, fresh context, pressure-tested the cited draft. It returned 2 FATAL + 4 MAJOR/MINOR issues; all were addressed and re-verified on disk.

## Sources: consulted → accepted / rejected
**Accepted (used in findings):**
- GSS (Fredholm) — SSRN 1531466 / doi 10.1111/j.1467-9965.2011.00478.x ; SSRN 2183685
- GP (aim portfolio) — doi 10.1111/jofi.12080
- NV (FBSDE; "Cartea–Jaimungal among the first") — arXiv 2002.09549 (abs + pdf)
- LN (framework cites CJ 2013 AMF 20:512–547) — 1704.00847 ; Springer FS PDF
- AJN (free-boundary L²-BSDE + operator Riccati; "Volterra-type propagator") — arXiv 2211.00447v2 abstract
- AJNT (operator resolvents) — doi 10.1111/mafi.70025 ; SSRN 4759758
- **AJ–DC–Pham 2024 (constraints via multipliers + conditional expectations + stochastic Fredholm)** — arXiv 2409.12098 (abs + html)
- Cartea–Jaimungal disambiguation — repec apmtfi v20 (2013 "Modeling Asset Prices…") ; SSRN 2557457 (2016 order-flow) ; arXiv 2306.00621 (attributes signal-execution to CJ 2016)
- Signatures — arXiv 1905.00728 ; 2308.15135
- Frequency-domain LQ / Wiener–Hopf (econ) — MaRDI Q1109666 (Whiteman "Spectral utility…")
- Survey — MaRDI "Optimal Execution: A Review"

**Consulted, not load-bearing / context only:**
- Nonlinear Fredholm — arXiv 2503.04323 (out of LQ scope; noted as frontier)
- Politecnico thesis flagging AJ-2024 existence gap — politesi.polimi.it (single unrefereed thesis; hedged)
- Self-exciting/Hawkes execution; Cartea et al. stochastic-price-impact SIAM 2023 (21m1394473) — different model class

**Rejected / not pursued:** RL-execution repos beyond one boundary mention; VWAP-targeting CJ 2016 (different objective); market-impact estimation-via-Wiener-Hopf (Hawkes identification, different purpose).

## Verification status
- **FATAL (fixed & re-verified on disk):**
  - W1 — novelty overclaim ("does appear novel in execution") breaching the review's own scope → replaced with a hedged, strictly-negative search note. Confirmed absent (grep count 0).
  - W2 — wrong Cartea–Jaimungal citation metadata (fabricated title) → corrected to *Modeling Asset Prices for Algorithmic and High Frequency Trading* (AMF 20:512–547, 2013), with a "confirm 2013 vs 2016" flag. Confirmed present (grep).
- **MAJOR (addressed):**
  - W3 — "closest prior art to §4" superlative → "most directly parallel prior work we identified" (2 sites).
  - W4 — AI-1 / Recommendation 1 reordered to lead with AJN's actual object (free-boundary BSDE + operator Riccati); "Fredholm" presented as AJ–DC–Pham's variational form; symmetric-kernel argument demoted to a deterministic-case caveat.
  - W5 — single-source flags added (CJ "among the first" = NV/LN; Whiteman "a precedent" not "the ancestor"; Politesi one thesis); Forde table cell downgraded "accurate" → "consistent (not independently sourced)".
  - W6 — added a provenance note that §5 recovery claims are verified against the object paper's text, not the external literature.

## Unresolved gaps / caveats
- AJN's exact **theorem** wording not extracted from the body (paper-Q&A failed once); direction (BSDE + operator Riccati, not Volterra) is well supported by the abstract but the substitute phrasing for §1.4 should be checked against AJN's Theorem before editing the paper.
- Exact Cartea–Jaimungal reference (2013 framework vs 2016 order-flow) to be confirmed against NV's bibliography before adding to the paper's `.bib`.
- Novelty of Wiener–Hopf-for-execution is stated only as "no prior use surfaced in our (non-exhaustive) search" — not established.

## Bottom line
The paper's broad representation of prior methods is accurate; the actionable outputs are (1) fix the §1.4 AJN attribution, (2) cite Abi Jaber–De Carvalho–Pham 2024 for the §4 constraint machinery, (3) add Cartea–Jaimungal, (4) one boundary sentence for signature/frequency-domain-LQ methods.
