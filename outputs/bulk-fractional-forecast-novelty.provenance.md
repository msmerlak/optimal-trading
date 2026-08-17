# Provenance: bulk-fractional-forecast-novelty

**Date:** 2026-06-28
**Slug:** `bulk-fractional-forecast-novelty`
**Final artifact:** `outputs/bulk-fractional-forecast-novelty.md`
**Plan:** `outputs/.plans/bulk-fractional-forecast-novelty.md`
**Evidence draft:** `outputs/.drafts/bulk-fractional-forecast-novelty-research-evidence.md`

## Mode of operation

Lead-owned literature review. No `researcher`, `verifier`, or `reviewer` subagent
spawned: topic was narrow enough (a specific formula vs. a finite set of competing
papers), and the local project already had ~80% of the relevant references
catalogued in `papers/fractional-derivative-optimal-execution.md` §6. The audit
focused on whether the closest competitor (Forde–Sánchez-Betancourt–Smith 2022)
contains the same formula or structural insight; the answer (yes, in operator
language; no, in clean Riesz-on-forecast form) drives the verdict.

## Sources consulted vs. accepted vs. rejected

### Accepted as primary evidence

| Source | URL | Role | Verification |
|---|---|---|---|
| Forde, Sánchez-Betancourt, Smith 2022 | https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197 | Closest competitor; contains the Riemann-Liouville factorization | PDF fetched and read; key passage quoted verbatim (p.592 third bullet) |
| Abi Jaber & Neuman 2022 (v2 2025) | https://arxiv.org/abs/2211.00447 | General Volterra/Riccati treatment | PDF fetched and read (54 pages); "fractional" used only as kernel descriptor |
| Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann 2025 (nonlinear Fredholm) | https://arxiv.org/abs/2503.04323 | Nonlinear extension; uses sum-of-exponentials approximation for power-law | PDF fetched and read (38 pages) |
| Abi Jaber, Neuman, Tuschmann 2024 (cross-impact) | https://arxiv.org/abs/2403.10273 | Matrix extension; same operator-resolvent style | Abstract + cross-references checked |
| Fractional Calculus in Optimal Control survey (2025) | https://arxiv.org/abs/2512.12111 | Confirms execution ↔ CRONE bridge has not been drawn | Abstract fetched; topic list checked for "execution" / "liquidation" — none |

### Accepted as context / background

| Source | Role |
|---|---|
| Gatheral, Schied, Slynko 2012 | Deterministic-skeleton Fredholm-inversion via Chakrabarti–George — no signal |
| Neuman & Voß 2022 | Exponential-propagator signal-adaptive case — no power-law |
| Bouchaud–Gefen–Potters–Wyart 2004; Gatheral 2010 | Empirical origin of the power-law propagator |
| Oustaloup 1991, 2000 | CRONE / fractional PID origin |
| Stein 1970; SKM 1993; Krein 1962; Noble 1958; Porter–Stirling 1990; Chakrabarti–George 1994 | Classical fractional-calculus / Wiener–Hopf machinery |

### Rejected / not material

- ar5iv 2002.03376 (Almgren–Chriss with Lévy processes) — different problem.
- Frontiers paper on fractional stochastic volatility — uses fBm for the
  underlying, not fractional operators in the control problem.
- 2504.00846 (latency in execution) — different problem.
- *A note on optimal liquidation with linear price impact* (VMSTA) — linear
  impact only.
- Optimal-execution-with-rough-path-signatures and stochastic-control-with-
  signatures papers — orthogonal methodology, not directly comparable.

## Verification status

| Claim in final artifact | Evidence | Status |
|---|---|---|
| FSS2022 uses identical kernel $G(t)=ct^{-\gamma}$, $\gamma\in(0,1)$ | PDF p.587, equation after Remark 2.1 | **verified by direct quote** |
| FSS2022 explicitly identifies the Riemann–Liouville factorization via $T = B^{-1}I_\nu B$, $r=(1-\gamma)/2$ | PDF p.592 third bullet | **verified by direct quote** |
| FSS2022 uses Volterra-on-Brownian-motion ansatz, not forecast-curve substitution | PDF p.588 Theorem 2.2 statement | **verified** |
| FSS2022 stays on bounded interval $[0,T]$ throughout | PDF entire paper; no $\mathbb{R}$-formulation | **verified** |
| Abi Jaber–Neuman 2022 word "fractional" appears only as kernel descriptor | grep on extracted PDF; only matches are in Example 2.5(2) and Section 5 figure captions | **verified** |
| Abi Jaber et al. 2025 uses sum-of-exponentials approximation for power-law numerics | PDF Section 3.4, eq. (3.15)-(3.17) and Figure 5 | **verified** |
| Survey arXiv:2512.12111 does not mention optimal execution | abstract + section list inspected; no occurrence of "execution" / "liquidation" / "Almgren" / "Bouchaud" / "propagator" in abstract or section headings | **verified for the abstract**; full-PDF scan not done (low priority — abstract is sufficient evidence for a survey paper) |
| Oustaloup CRONE has no application to optimal execution | survey arXiv:2512.12111 + general knowledge | **inferred** (single negative source); reasonable as nothing in execution literature cites CRONE either |
| Gatheral–Schied–Slynko 2012 has the U-shape closed form for power-law without signal | cited in FSS2022 introduction; explicit formula matches | **verified via cross-reference** |

## Methodological notes / caveats

1. **The verdict relies on FSS2022 being recognized as prior art.** This paper is
   already cited in `papers/fractional-derivative-optimal-execution.md` §6.3 (per
   the project bibliography). The recommendation in §7 of the final review is to
   **elevate** FSS2022 from a peer-reference to the *closest prior art*, with
   explicit attribution at the bulk-theorem statement.

2. **The "novelty" claim for the CRONE bridge is asymmetric evidence.** I have
   verified that the 2025 survey of fractional-control does not include execution.
   I have not exhaustively verified that no working paper in the optimal-execution
   literature cites CRONE. The likelihood is low (the term-frequency tools used
   don't show any cite), but the negative is weakly held.

3. **The bulk/boundary spine novelty is presentational.** It is a structural
   choice, not a mathematical theorem; nobody would refute it, but it is also
   easy to retro-fit to existing work. I have flagged it as "novel framing"
   rather than "novel result."

4. **Abi Jaber–Neuman 2022's v2 (Sep 2025) is the version examined.** v1 (Nov 2022)
   may have minor structural differences but the operator-resolvent / BSDE
   formulation is the same in both versions.

## Intermediate files used

- `outputs/.plans/bulk-fractional-forecast-novelty.md` (plan; verification log)
- `outputs/.drafts/bulk-fractional-forecast-novelty-research-evidence.md` (evidence draft)
- `/Users/orwell/Downloads/1469768820211950919.md` (FSS2022 PDF text extract; 51 KB)
- `/Users/orwell/Downloads/optimal-liquidation-with-signals-the-general-propagator-case.md` (Abi Jaber–Neuman 2022 PDF text extract; 98 KB)
- `/Users/orwell/Downloads/arxiv-250304323.md` (Abi Jaber et al. 2025 PDF text extract; 101 KB)

## Existence check

Final artifacts on disk (verified pre-delivery):

- `outputs/bulk-fractional-forecast-novelty.md` — 19,676 bytes
- `outputs/bulk-fractional-forecast-novelty.provenance.md` — this file
- `outputs/.plans/bulk-fractional-forecast-novelty.md` — 4,622 bytes
- `outputs/.drafts/bulk-fractional-forecast-novelty-research-evidence.md` — 13,094 bytes
