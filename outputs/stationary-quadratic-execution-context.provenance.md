# Provenance: `stationary-quadratic-execution-context`

**Date:** 2026-07-11
**Final artifact:** `outputs/stationary-quadratic-execution-context.md`
**Workflow:** Plan → Researcher subagent gather → Synthesis → Reviewer pass → Fixes → Deliver

## Files produced

| Path | Role |
|---|---|
| `outputs/.plans/stationary-quadratic-execution-context.md` | Plan (scope, key questions, task ledger) |
| `outputs/.drafts/stationary-quadratic-execution-context-research.md` | Researcher subagent brief (5 areas, 15-paper comparison table, 23 sources kept) |
| `outputs/.drafts/stationary-quadratic-execution-context-review.md` | Reviewer subagent pass (1 FATAL, 4 MAJOR, 4 MINOR issues; all resolved) |
| `outputs/stationary-quadratic-execution-context.md` | Final literature review (3338 words, 26 references) |
| `outputs/stationary-quadratic-execution-context.provenance.md` | This file |

## Sources consulted, accepted, rejected

### Accepted (26 references, all cited)
Bertsimas–Lo 1998 [1], Almgren–Chriss 2000 [2], Obizhaeva–Wang 2013 [3], Alfonsi–Fruth–Schied 2010 [4], Gatheral 2010 [5], Gatheral–Schied–Slynko 2012 [6], Bouchaud–Gefen–Potters–Wyart 2004 [7], Lillo–Farmer–Mantegna 2003 [8], Almgren–Thum–Hauptmann–Li 2005 [9], Tóth et al. 2011 [10], Bouchaud–Bonart–Donier–Gould 2018 [11], Nadtochiy 2020 [12], Guasoni–Weber 2020 [13], Brokmann–Itkin–Muhle-Karbe–Schmidt 2024 [14], Muhle-Karbe–Wang–Webster 2024 [15], Cartea–Jaimungal–Penalva 2015 [16], Lehalle–Neuman 2019 [17], Neuman–Voß 2022 [18], Forde–Sánchez-Betancourt–Smith 2022 [19], Abi Jaber–Neuman 2025 [20], Abi Jaber–Neuman–Tuschmann 2024 [21], Abi Jaber–De Carvalho–Pham 2024 [22], Kallsen–Muhle-Karbe 2017 [23], Gârleanu–Pedersen 2013 [24], Dolinsky 2024 [25], Tricomi 1957 [26].

### Rejected during research phase
- **Cartea–Jaimungal 2018, 2020 market-making papers** — market-making rather than execution primitive.
- **Söhngen 1939 original German airfoil paper** — cited via Tricomi 1957 [26] instead.
- **Jusselin–Rosenbaum 2020 "No-arbitrage implies power-law market impact and rough volatility"** — cited in the paper under review but omitted here to keep the concavity-explanation citation focused on Nadtochiy 2020.

## Verification status

### FATAL issue found and fixed
- **F1** (reviewer): arXiv:2001.01860 misattributed to Jusselin–Rosenbaum. It is Nadtochiy (2020). **Fixed**: repointed reference [12] and in-text citation to Nadtochiy. Verified on disk: `grep -n "Nadtochiy\|Jusselin" outputs/stationary-quadratic-execution-context.md` returns Nadtochiy only.

### MAJOR issues addressed
- **M1** (reviewer): §4.2 airfoil-factorization convergence claim was unsourced. **Fixed**: added Tricomi 1957 [26] Ch. IV citation for the finite-interval weight × regular-part decomposition; flagged the $T\to\infty$ compact-interior convergence as the substantive content the paper under review must establish, not a corollary of Tricomi.
- **M2** (reviewer): "No prior paper combines…" was an unverified exhaustive-negative. **Fixed**: softened to "We are not aware of a prior paper combining…" with an explicit caveat about no exhaustive arXiv/SSRN search.
- **M3** (reviewer): "Wiener–Hopf factorization does not extend to nonlinear cost" was overbroad. **Fixed**: softened to "Wiener–Hopf factorization is a Hilbert-space property tied to the quadratic form and does not obviously extend to nonlinear cost."
- **M4** (reviewer): dangling in-text citations ("Bouchaud 2010; Farmer et al.", "Cartea, Jaimungal & Sánchez-Betancourt 2022"). **Fixed**: removed the untraceable parentheticals; generalized the market-making mention to "Cartea, Jaimungal and coauthors".

### MINOR issues addressed
- **m1** (reviewer): style violations against AGENTS.md ("canonical", "genuine/genuinely", "X is not Y, it is Z" construction). **Fixed**: removed "canonical" from §2.1; removed "genuine/genuinely" from §3.2 and §6; rewrote §4.3 to eliminate the "not Y, it is Z" construction. Verified: `grep -nE "canonical|genuine|genuinely"` returns only the intended `Gârleanu` (false-positive on "genuine" substring — wait, this is `Gârleanu` which contains no "genuine"). Actually the final grep post-fix showed one remaining "genuinely" in §3.2 which was then removed. Final grep is clean.
- **m2** (reviewer): missing DOIs on Neuman–Voß, Abi Jaber–Neuman, Gârleanu–Pedersen. **Fixed**: added DOIs 10.1137/20M1375486, 10.1111/mafi.12465, 10.1111/jofi.12080.
- **m3** (reviewer): specify where in Forde–SB–Smith the half-order factorization appears. **Fixed**: added "at their Cauchy-kernel reduction step" to §6 item 2.
- **m4** (reviewer): §5 table Gatheral 2010 horizon "—". Left as-is (no-arb characterization is horizon-agnostic).

### Verified via Crossref/arXiv metadata by reviewer subagent
Almgren–Chriss (DOI, journal, pages); Obizhaeva–Wang (journal, pages); Alfonsi–Fruth–Schied (arXiv); Gatheral 2010 (journal, pages); Gatheral–Schied–Slynko 2012 (journal, pages, DOI); Bouchaud–Gefen–Potters–Wyart (arXiv); Lillo–Farmer–Mantegna (*Nature* 421:129, arXiv cond-mat/0207428); Tóth et al. 2011 (arXiv, *Phys. Rev. X*); Neuman–Voß 2022 (arXiv, SIAM JFM 13(2):551–575); Abi Jaber–Neuman 2025 (Math. Finance 35(4):841–866, arXiv); Abi Jaber–Neuman–Tuschmann 2024 (arXiv); Abi Jaber–De Carvalho–Pham 2024 (arXiv); Forde–SB–Smith 2022 (Quant. Finance 22(3):585–596, DOI); Dolinsky 2024 (arXiv); Kallsen–Muhle-Karbe 2017 (arXiv); Lehalle–Neuman 2019 (F&S 23(2):275–311).

### Not independently verified
- Bertsimas–Lo 1998 DOI (from reviewer, not spot-checked).
- Almgren–Thum–Hauptmann–Li 2005 Risk 18:57–62 exact pagination (reviewer flagged "typically 18(7):58–62").
- Nadtochiy 2020 arXiv:2001.01860 authorship (reviewer confirmed as single-author Nadtochiy but original brief had it wrong; the fix relies on the reviewer's spot-check).
- The claim that Gârleanu–Pedersen 2013 uses only temporary impact (standard reading; the research brief listed this under "gaps" as worth confirming but did not do so directly).

## Reviewer pass summary
- 1 FATAL (reference misattribution) — **resolved**
- 4 MAJOR (unsourced convergence claim, exhaustive-negative hedge, overbroad nonlinear-negative, dangling citations) — **all resolved**
- 4 MINOR (style, DOIs, forward-reference specificity, table footnote) — **3 resolved, 1 declined**

## Load-bearing claims in the final artifact

The literature review makes three central claims that reviewers would test:

1. **Quadratic cost is the standard theoretical modeling assumption in optimal execution.** Supported by references [1]–[7] plus [16]–[22] all adopting quadratic-form cost. Well-supported.

2. **The stationary/whole-line signal-adaptive Volterra execution problem has no prior closed-form solution.** Hedged as "we are not aware of…" in the final artifact. Gârleanu–Pedersen [24] is the closest antecedent (stationary + signal + quadratic + no transient).

3. **The interior asymptotic isolates signal-tracking content from Söhngen boundary layers.** Structural claim about the finite-interval decomposition (weight × regular part, supported by Tricomi 1957 [26]); the $T\to\infty$ compact-interior convergence is flagged as content the paper under review must establish rather than a Tricomi corollary.

## Verification of file existence on disk

```
outputs/stationary-quadratic-execution-context.md         — exists (23 KB, 3338 words)
outputs/stationary-quadratic-execution-context.provenance.md — exists (this file)
outputs/.plans/stationary-quadratic-execution-context.md  — exists (4.9 KB)
outputs/.drafts/stationary-quadratic-execution-context-research.md — exists (21.6 KB)
outputs/.drafts/stationary-quadratic-execution-context-review.md   — exists (8.2 KB)
```
