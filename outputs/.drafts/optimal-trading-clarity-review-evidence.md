# Evidence Notes — Clarity & Structure Review

Artifact: `v2/optimal-trading-filters-v2.tex` (474 lines) → `v2/optimal-trading-filters-v2.pdf` (18 pp.)
Reviewer read the full source from disk; ran compile + reference audits. Scope: clarity/structure only.

## Mechanical audit (commands run)
- `pdflatex ×3 + bibtex`: **errors=0, undefined refs=0, multiply-defined=0, undefined citations=0**; "Output written … (18 pages)".
- Label/ref audit: **"refs with no matching label" = EMPTY** → every `\ref`/`\eqref` resolves. No dangling cross-references (important given the recent §2 and §4 restructuring).
- Orphan labels (defined, never `\ref`'d), confirmed by direct grep (count=0 each):
  `eq:N, eq:fractional, eq:phi, eq:exp-factor, eq:nv-factor, eq:nv-filter, eq:bdry-decay, def:mr, tab:notation`.
- Figures: `fig:filter, fig:value, fig:surf, fig:bdry` — each referenced exactly once and discussed in place. (fig2 kink/cusp was dropped earlier; numbering is contiguous in output.)
- Hyphenation: `Wiener--Hopf` (en-dash) ×3 in body; `Wiener-Hopf` (hyphen) ×1 in **abstract** (line 36).
- μ usage: `\mu`=13, `\mu_t`=5 (expected return E_t[−α̇]); `\mu^\star`=9 (nonanticipativity multiplier); `\mu_k`=3 (position-constraint multiplier). → base letter μ carries THREE distinct meanings.

## Structure skeleton (from source)
- §1 Introduction: 1.1 gain–risk–cost problem / 1.2 adaptedness constraint / 1.3 causal factorization (+roadmap) / 1.4 relation to earlier work. Notation table (`tab:notation`) floats after §1.4.
- §2 The interior solution: 2.1 setup & factorization / 2.2 projected inverse & general policy (Lem, Thm, duality Remark) / 2.3 mean-reverting signals / 2.4 stationary trading filter.
- §3 Pure power-law impact: 3.1 fractional-derivative policy / 3.2 value of anticipation / 3.3 impact surfing.
- §4 Finite-horizon factorization: intro (challenge+framework) / 4.1 relaxation to stationary filter (Prop boundary) / 4.2 power-law factor / 4.3 general kernels.
- §5 Recovery of earlier solutions: 5.1 rational frictions / 5.2 finite-horizon power-law.
- §6 Concluding remarks. Appendices A–E (all proofs). Acknowledgements + bib.

## Observations (paraphrased evidence)
### Strengths
- Notation convention stated explicitly (caption `tab:notation`): "Operators are italic capitals and carry no argument; kernels are lowercase Latin; a hat denotes the Fourier transform; filters are lowercase Greek." Table groups symbols by role (Operators/Kernels/Symbols/Filters/Processes/Scalars).
- §1.3 ends with an explicit section-by-section roadmap ("Section~\ref{sec:interior} establishes… Section~\ref{sec:fractional} collects…").
- α vs μ distinction handled deliberately: §1.1 defines α = expected remaining appreciation, μ_t=E_t[−α̇] = expected return; notation table flags both; §5.1 Markowitz uses μ (position∝return), §3.1 uses α (rate∝appreciation). This subtle two-signal split is maintained consistently.
- §3 opener lists the three peculiarities mapping 1:1 to §3.1–3.3. §4 intro states the challenge before the machinery. Good local signposting.
- Lemma/Theorem statements self-contained; every proof deferred to a named appendix (A–E), main text gives one-line intuition ("triangular bookkeeping", "three steps with a clear reading").
- §4 (recently reorganized) cleanly separates: general existence/framework (intro) → interior approximation theorem (4.1) → pure power-law explicit factor (4.2) → general GK equations (4.3). No interleaving.
- §5 opens with an explicit "two groups" framing (rational vs power-law-finite-horizon).
- Abstract's "Contrary to classical rational filters … always captures a fixed fraction sin(πβ/2)" is now BACKED by the §3.2 remark showing the exponential/rational fraction is timescale-dependent (θ/κ) → abstract–body consistency on this contrast.

### Issues
- **μ overloading** (MAJOR clarity): μ = return AND μ*, μ_k = multipliers. Both meanings co-occur (Remark duality eq:multiplier uses μ*; §5.1 Markowitz uses μ=return). Disambiguated only by super/subscript.
- **§1.4 dense/front-loaded** (MAJOR structure): 3 paragraphs before the method. Para 2 = detailed Abi Jaber–Neuman comparison ("stochastic Volterra equation of the second kind", "Neumann expansion of the inverse Volterra operator"); para 3 = O(n²) cost argument. Both require concepts (Volterra factors, resolvent series) not yet introduced.
- **Abstract nits** (MINOR): (a) "Wiener-Hopf" hyphen vs body en-dash; (b) "reduces to a fractional derivative" attributed to "power-law transient impact" without the **pure** (η=λ=0) qualifier the clean reduction requires — body §3.1 is careful ("temporary cost alone… Power-law impact is the opposite extreme"); (c) omits the §5 recovery/unification (previews §3 consequences but not that the method reproduces Markowitz/aim/Neuman–Voß/GSS/Forde); (d) "and possibly inventory risk" slightly awkward.
- **§2.3 forward-dependency seam** (MINOR): the OU value v=σ²θ/4Φ² stated in §2.3 (Mean-reverting) is proved in App B via the stationary-filter machinery introduced only in §2.4 (uses ‖φ̂‖²=πσ²/θ). Artifact of the recent reorder that put mean-reverting before the stationary filter.
- **`tab:notation` never referenced** (MINOR): the table is never pointed to from the text; a reader hitting heavy notation isn't directed to it.
- **Orphan equation labels** (MINOR hygiene): eq:N, eq:fractional, eq:phi, eq:exp-factor, eq:nv-factor, eq:nv-filter, eq:bdry-decay, def:mr never cross-referenced — harmless, prunable.
- **Power-law content split across §3, §4.2, §5.2** (MINOR structure): thematically organized (peculiarities / finite-horizon / recovery), so a reader tracking "the power-law case" jumps sections. Defensible but noted.

## Inspected sources
- `v2/optimal-trading-filters-v2.tex` (full read).
- `v2/optimal-trading-filters-v2.pdf` (compiled, 18 pp.).
- `v2/optimal-trading-filters-v2.log` (compile diagnostics).
- Audit commands: label/ref comm, per-label grep counts, hyphen/μ greps (this session).
