# Provenance: `adapted-convex-optimization-physics.md`

**Date:** 2026-06-17
**Slug:** `adapted-convex-optimization-physics`
**Topic:** Relation between adapted convex optimization (convex J on a Hilbert space subject to a nest/filtration constraint, solved via outer factorization inside the nest algebra) and physics.

## Files
- Final artifact: `outputs/adapted-convex-optimization-physics.md` (819 lines)
- Plan: `outputs/.plans/adapted-convex-optimization-physics.md`
- Research brief (researcher subagent output): `outputs/.drafts/adapted-convex-optimization-physics-research-1.md`
- Working draft (pre-fix): `outputs/.drafts/adapted-convex-optimization-physics-draft.md`

## Workflow

1. **Plan** — 8-cluster scope: causality/dispersion, FDT/Kubo, Wiener–Hopf physics origins, path-integral control, quantum filtering, stochastic thermodynamics & max caliber, JKO/adapted OT, Freidlin–Wentzell/MFT.
2. **Gather** — delegated wide sweep to `researcher` subagent. Brief covered all 8 clusters with primary-source citations and explicit "fit assessments."
3. **Synthesize** — wrote 13-section draft built around the abstract skeleton and its 8 physics instantiations, with side-by-side table mapping each cluster to (H, nest, J, factorization), recommended reading order, and open questions.
4. **Cite / Verify** — ran `reviewer` subagent with combined citation + content review brief; instructed to spot-check 6-8 URLs and 6+ direct quotations with explicit warning that the prior sister-document review had caught fabricated quotes.
5. **Reviewer findings (3 FATAL, 5 MAJOR, ~5 MINOR)** — see below; all FATAL and main MAJOR issues fixed in-place.
6. **Deliver** — copied final draft to `outputs/adapted-convex-optimization-physics.md`; verified existence on disk.

## Reviewer findings and dispositions

### FATAL — fixed

- **F1.** Wrong URL→paper mapping: arXiv:math-ph/0404070 is actually **Figotin & Schenker, *Spectral Theory of Time-Dispersive and Dissipative Systems* (2004)**, NOT Welters–Avniel–Johnson "Speed-of-light limitations in passive linear media" (which exists separately as *J. Math. Phys.* 52, 122003 (2011)). The bad mapping was inherited from the researcher brief.
  - **Fix:** Renamed citekey `[WAJ09]` → `[FS04]` Figotin–Schenker with correct authors and title. Added a note in the Sources entry recording that the brief originally misidentified this URL.

- **F2.** Fabricated quotation: the §3.4 "quote" attributed to arXiv:2604.17058 ("connect the real and imaginary parts of a causal response function through a Hilbert transform … requires Hardy-space projection") does NOT appear in the paper's abstract. Verified by direct fetch.
  - **Fix:** Replaced with a verbatim two-sentence excerpt from the actual abstract: "Kramers–Kronig (KK) relations are usually invoked for causal response functions, but their precise status for non-Markovian quantum memory kernels is less explicit. … we show that $\tilde{\mathcal K}(z)$ belongs to the operator-valued Hardy space $H^p_+$ and obeys KK or subtracted KK relations." Removed the "first physics-side statement" superlative (see M1).

- **F3.** Wrong title and author: the paper at arXiv:2604.17058 is **Kejun Liu (single author), *Kramers–Kronig Relations and Causality in Non-Markovian Open Quantum Dynamics: Kernel, State, and Effective Kernel* (2026)**, NOT "Yusef-Estrada et al., *Causality from Projection and Hardy-Space Analyticity of Non-Markovian Memory Kernels*." The brief invented both author triple and title.
  - **Fix:** Renamed citekey `[YE26]` → `[Liu26]`, correct title, correct single author. Updated all in-text references.

### MAJOR — fixed

- **M1.** "First physics-side statement … to the reviewer's knowledge" was an unsupported superlative.
  - **Fix:** Replaced with "the cleanest recent physics source we located," with an explicit disclaimer that this is not a priority claim (broader passive-media literature uses Herglotz / outer-function structure on the same upper half-plane).

- **M2.** "**No physics paper unifies all eight clusters under one banner**" stated as a hard universal negative; the brief itself disclaimed exhaustiveness.
  - **Fix:** Status block, §1, and §11.4 all rewritten to "In this survey we did not find a physics paper unifying all eight clusters under one banner; the search was not exhaustive (see §11.4)." Added explicit caveat in §11.4 listing what was not searched (Belavkin's collected works, Barchielli–Gregoratti, Powers/Muhly on continuous nests, math-finance filtration literature).

- **M3.** §7.2 claimed non-demolition condition "guarantees a genuine nest of mutually commuting projections" — not supported by cited sources.
  - **Fix:** §7.2 rewritten to say the non-demolition condition "makes the measurement-output process compatible with conditional expectation" and that "the resulting measurement subalgebras form a commutative chain on which the conditioning is classical," with explicit hedge that "the precise operator-algebraic statement … is the reviewer's reading; the cited sources develop the theory in martingale and reference-probability terms."

- **M4.** "No source explicitly invokes Arveson-style nest-algebra factorization in the noncommutative-L² setting of quantum filtering" — hard universal negative.
  - **Fix:** §7.3 and §11.3 both hedged to "*In this survey we did not locate a source explicitly invoking …*" with reference to the exhaustiveness caveat in §11.4 and an explicit acknowledgement that Powers / Muhly / Belavkin's collected works were not searched.

- **M5.** [vH05] attribution: arXiv:math-ph/0508006 has two authors, Bouten & van Handel, not van Handel alone.
  - **Fix:** Renamed citekey `[vH05]` → `[BvH05]`, updated body text to "Bouten & van Handel's lecture notes."

### MINOR — addressed

- **m1.** Bertini quote (§10.3) was sourced to the 2015 RMP review but is actually verbatim from the 2001 foundational paper (cond-mat/0104153).
  - **Fix:** Reworded paragraph to attribute the quote to the foundational 2001 paper "summarized in the 2015 RMP review."

- **m2.** Gralak quote was stitched from non-adjacent sentences in his §2.
  - **Fix:** Replaced direct quotation with an honest paraphrase in §3.3 that summarizes what Gralak says without reconstructing a quote.

- **m3.** Several quotes unverified in reviewer's session due to 403s and PDF stubs (Toll 1956, PGLD 2013, Bach–Dürr, Kubo, Meister–Speck, Hoffmann-Jørgensen, Gupta–Hota, Dixit, Grafke).
  - **Disposition:** Quotes retained but tagged in this provenance file as *unverified in the reviewer's spot-check*. These should be re-verified in a future pass when full-text access is available. The Grafke quote in particular should be checked against the body of the paper (the abstract uses "least unlikely realization" rather than "most likely trajectory").

- **m4.** Bouten–van Handel–James 2007, van Handel notes, EoM-WH page, Seifert 2012 — quotes verified clean by reviewer.

- **m5.** Citekeys `[GP04]` and `[CW89]` cited in §5.3 body but missing from Sources.
  - **Fix:** Added both to the Wiener–Hopf in physics Sources subsection.

## Sources consulted

### Accepted into final bibliography (primary)

Causality/dispersion: Toll 1956, Titchmarsh 1937, Hoffmann-Jørgensen 2014, Figotin–Schenker 2004, Gralak 2020, Monticone et al. 2020, Liu 2026.

FDT: Kubo 1957, Kubo 1966, Callen–Welton 1951.

Wiener–Hopf in physics: Milne 1921, Hopf 1932, Hopf 1934, EoM "Wiener–Hopf equation," Lawrie–Abrahams 2022, Meister–Speck 1980, Ganapol–Pomraning 2004, Cassell–Williams 1989, Gohberg–Fel'dman 1974, Bart–Gohberg–Kaashoek–Ran 2008.

Path-integral control: Onsager–Machlup 1953, Bach–Dürr 1978, Kappen 2005 (×2), Todorov 2009, Dvijotham–Todorov 2011, Theodorou et al. 2010, Theodorou–Todorov 2012.

Quantum filtering: Belavkin 1988, 1992, Bouten–van Handel–James 2007, Bouten–van Handel notes 2005, Wiseman–Milburn 2010, Gupta–Hota 2015.

Stochastic thermodynamics & max caliber: Seifert 2012, Crooks 1998, Pressé–Ghosh–Lee–Dill 2013, Dixit et al. 2018.

JKO / adapted OT: Jordan–Kinderlehrer–Otto 1998, Acciaio–Backhoff–Zalashko 2020, Backhoff-Veraguas–Källblad–Robinson 2025, Eckstein–Pammer 2024, Beiglböck–Pammer–Schrott 2025.

Large deviations: Touchette 2009, Grafke et al. 2021, Bouchet et al. 2023, Bertini et al. 2015 (foundational 2001 paper).

### Rejected during research

- Scribd copy of Toll paper (superseded by APS abstract + INSPIRE).
- Generic IOP captcha link (superseded by ResearchGate / UMD mirrors).
- Duplicate Wiseman–Milburn listings on Cambridge.org variants.
- MaRDI duplicates of JKO.
- Wikipedia "Kubo formula" (kept as fallback but not quoted).

### Misidentifications caught and corrected

- arXiv:math-ph/0404070 misattributed to Welters–Avniel–Johnson (correct: Figotin & Schenker 2004) — corrected.
- arXiv:2604.17058 given wrong title and invented author triple (correct: Liu 2026) — corrected.
- arXiv:2604.17058 direct quotation fabricated — replaced with verbatim abstract excerpt.
- vH05 lecture notes credited to single author (correct: Bouten & van Handel) — corrected.
- Bertini quote sourced to 2015 RMP but actually from 2001 cond-mat paper — corrected.

## Verification status

- 8/8 URLs spot-checked by reviewer via `curl`: all resolve (Toll APS 403 = anti-bot, content verifiable via INSPIRE).
- Direct quotes verified: BvHJ 2007 (✓), Bouten-vanH notes (✓), EoM-WH (✓), Seifert 2012 (✓), Liu 2026 (✓ — original quote was fabricated, replaced with real abstract text).
- Unverified-in-this-session quotes (no FATAL evidence against them, but flagged in this provenance): Toll 1956 body, PGLD 2013, Kubo 1957, Bach–Dürr 1978, Meister–Speck 1980, Hoffmann-Jørgensen 2014, Gupta–Hota 2015, Dixit 2018, Grafke 2021. These match the brief's reported text but should be re-verified before any publication-level use.
- Several Sources entries retain explicit *unverified* markers: Welters–Avniel–Johnson alternative paper details, exact MFT 2015 RMP citation, WAJ year.

## Limitations of this review

- The unifying framing (eight physics clusters as instances of one adapted-convex skeleton) is the reviewer's reading, not a programme present in any single source. Flagged in the Status box and §11.
- §11.4's exhaustiveness caveat lists four cluster-relevant literatures NOT searched: Belavkin's collected works, Barchielli–Gregoratti, Powers/Muhly on noncommutative nests, math-finance filtration-projection (Kallianpur, Bismut). Any of these could change the "unifying paper not found" conclusion.
- Cluster 9 (adapted OT in physics) found a genuine literature gap: no physics paper applies bicausal/adapted Wasserstein gradient flow to entropy production or non-equilibrium fluctuations. This is the cleanest cross-discipline opening identified.
- No second reviewer pass run after fixes (fixes were citation-level + hedging-level, not structural).

## Pattern note

This is the **second** literature-review session in which the reviewer pass caught fabricated quotations and misattributed URLs inherited from the researcher subagent's brief. The pattern: researcher generates a content-dense brief with plausible-looking quotations that were never actually verified against the source URL. Recommendation for future work: instruct researcher subagent to either (a) fetch and quote verbatim with line numbers, or (b) paraphrase explicitly rather than producing direct-quote marks. The reviewer pass is doing the verification work that should happen at the gather stage.
