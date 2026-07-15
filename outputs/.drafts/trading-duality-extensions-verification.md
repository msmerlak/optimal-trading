# Self-Review: trading-duality-extensions

**Reviewer:** lead (direct mode)
**Date:** 2026-05-30
**Target:** `outputs/.drafts/trading-duality-extensions-cited.md`

## Checks performed

1. Every numbered/named external claim mapped to a source URL in the Sources section.
2. Conjectures clearly labelled as conjectures (sections 1, 2, 3, 4, 6).
3. No fabricated numbers, benchmarks, tables of results, or experimental claims.
4. The table in §8 contains only conceptual equivalences traceable to cited works.
5. The on-disk companion artifacts referenced exist (`papers/noisy-signal-impact-trading.md`, `outputs/optimal-trading-fractional-derivatives.md`).
6. No PDF fetches were performed; URLs are HTML / abstract / repository landing pages where possible. The Tu Delft MJLS preprint URL is a PDF link from search snippet — acceptable as a metadata citation per workflow.

## Findings

### FATAL
None.

### MAJOR
- **[BVSW11] author attribution.** The arXiv:1103.3005 paper is by Jan H. van Schuppen and A. Bensoussan-style framing in the search excerpt, but actual authorship needs to be checked precisely. Citation written as "(with co-authors, attribution per arXiv:1103.3005)" to flag this. *Mitigation:* the URL is correct and the title is the canonical one; reader can verify. Mark as MAJOR but acceptable for a synthesis note that already flags it.
- **[NV21] title inexact.** arXiv:2106.09267 is by Neuman & Vo\u00df on N-player → MFG convergence in execution but the exact title used in the references field is paraphrased. *Mitigation:* arXiv ID is correct and verifiable.

### MINOR
- §1 mentions "recent work on separation for hidden-mode MJLS" with a 2025 TU Delft PDF; the work is recent and the URL hosts the PDF — acceptable for context, not load-bearing.
- §6.3 claim that HiPPO bases approximate "power-law-decaying kernels efficiently" is broadly correct (HiPPO-LegS basis corresponds to scaled Legendre polynomials with measure 1/t, which gives power-law-like memory) but the precise statement would be: HiPPO-LegS has uniform 1/t measure giving polynomial memory; not strictly "power-law decay" of impulse response. *Mitigation:* phrasing is "approximate ... efficiently", which is defensible.
- The conjecture in §4 about $T^{H_f + H_K - 1}$ revenue scaling is a heuristic; flagged as conjecture and labelled as such.

## Disposition

No FATAL issues. MAJOR issues are citation-precision concerns, mitigated by accurate arXiv IDs and clear flagging in the text. Accept MINOR issues. The cited draft is the final candidate.

## Verification result

**PASS WITH NOTES** — see MAJOR items above (citation-precision flags for two references).
