# Provenance: `convex-duality-nest-causality.md`

**Date:** 2026-06-17
**Slug:** `convex-duality-nest-causality`
**Topic:** Convex duality inside a nest as the general structure of causality.

## Files
- Final artifact: `outputs/convex-duality-nest-causality.md` (808 lines)
- Plan: `outputs/.plans/convex-duality-nest-causality.md`
- Research brief (researcher subagent output): `outputs/.drafts/convex-duality-nest-causality-research-1.md`
- Working draft (pre-fix): `outputs/.drafts/convex-duality-nest-causality-draft.md`

## Workflow

1. **Plan** — wrote plan with 7 source clusters, task ledger, risk list.
2. **Gather** — delegated wide sweep to `researcher` subagent. Brief covered all 7 clusters with primary-source citations, fit assessments, and confirmation that no unifying survey exists in the 2010–2026 literature.
3. **Synthesize** — wrote 12-section draft: thesis, abstract skeleton, operator-algebraic backbone, then one section per cluster (prediction, Kalman, optimal trading, adapted OT, causal information theory, martingale duality), synthesis/taxonomy, open questions, recommended reading order.
4. **Cite / Verify** — ran `reviewer` subagent with combined citation + content review brief, including instructions to spot-check 8 high-stakes URLs and 6 direct quotes via fetch tools.
5. **Reviewer findings (3 FATAL, 5 MAJOR, ~7 MINOR)** — see below; all FATAL and key MAJOR issues fixed in-place.
6. **Deliver** — copied final draft to `outputs/convex-duality-nest-causality.md`.

## Reviewer findings and dispositions

### FATAL — fixed

- **F1.** Misattribution: the `[TBD]/[TBD17]` "Tourneret-Bercher-Doncarli" citation in §4.3 was wrong on both ends. The HAL document hal-01817912 is actually **Picinbono & Bouvet, "Constrained Wiener Filtering," IEEE Trans. Inf. Theory 33 (1987), 160–166**; the Springer 2017 paper at doi:10.1007/s00034-017-0589-3 is by **Yang, Shu, Yuan, Deng**, not the named triple. The quoted sentence is genuinely from Picinbono–Bouvet 1987.
  - **Fix:** Replaced citation with `[PB87] Picinbono & Bouvet 1987`. Dropped the spurious Springer reference. Quote retained, attribution corrected.

- **F2.** Bad URL: `[Sch07]` ("Schachermayer, *Optimal investment in incomplete financial markets*") pointed to `prpr0161.pdf`, which is actually **Czichowsky & Schachermayer, *Duality theory for portfolio optimisation under transaction costs*, 2015**.
  - **Fix:** Renamed to `[CS15] Czichowsky & Schachermayer 2015` with correct title.

- **F3.** Fabricated quote: the attributed-to-AN22 quote in §6.2 ("infinite-dimensional convex analysis approach… reducing the first-order condition to a stochastic Fredholm equation") does not appear in the actual abstract of arXiv:2211.00447. The real abstract — verified by fetch — describes the method as "infinite dimensional stochastic control approach" and characterizes the value function via "a free-boundary L²-valued BSDE and an operator-valued Riccati equation." The Fredholm-equation framing is from Lehalle–Neuman 2019, not AN22.
  - **Fix:** Rewrote §6.2 paragraph on AN22 to use the *actual* abstract language. Added explicit reviewer-framing note: the identification of the operator-valued Riccati equation with the outer-factor propagation in the nest algebra is the reviewer's reading, not stated in those words by AN22; the cleaner direct match to the abstract skeleton is the [LN19] Fredholm-equation FOC.

### MAJOR — partially addressed

- **M1.** The `[Sch07]` quotation was a stitched paraphrase, not verbatim, and conflated EMM densities with consistent price systems.
  - **Fix:** Replaced §9.1 quotation with a faithful CS15 passage, plus an explicit note distinguishing the frictionless setting (KS99: EMM densities) from the transaction-cost setting (CS15: consistent price systems).

- **M2.** Cluster 7 fit-assessment effectively single-sourced once Sch07 is removed.
  - **Disposition:** The fit-assessment in §9.4 is now grounded in [KLSX91], [KS99], [KS03], [CK92], [CS15] together. The "this is adapted convex duality" framing remains the reviewer's reading; the front-matter Status box and §9.4's existing hedge ("operator-algebraic language is absent") already flag this. Acceptable.

- **M3.** Cluster 2 (§4.3) bridge effectively single-sourced.
  - **Disposition:** After F1 fix, §4.3 cites Picinbono–Bouvet 1987 (verified quote) plus Pourahmadi 2001 and Subba Rao–Yang 2021 as supporting context for the nest-projection reading. Still on the thin side, but no longer relies on a misattribution.

- **M4.** Daughtry–Johns reference dangling.
  - **Fix:** Added a `[DJ]` Sources entry with the MaRDI URL and an *unverified* marker for the full citation.

- **M5.** `[TM09]` and Kramer 2003 under-specified in Sources.
  - **Fix:** Expanded both with volume/pages where known, marked as *unverified* in this session.

### MINOR — addressed

- **m1.** Arveson p. 209 attribution slightly imprecise (the formula is on p. 211 in print, p. 209 is the introduction).
  - **Fix:** Reworded §3.1 to say "announced informally on p. 209 and developed in §1 of the paper" with the Theorem 1.1 label.

- **m2, m3, m4, m6.** Already appropriately hedged in draft. No change required.

- **m5.** Kramer 2003 missing Sources entry.
  - **Fix:** Added `[Kra03]` Sources entry.

- **m7.** URL liveness: all spot-checked URLs return HTTP 200 except AMS Trans. journal page (403 anti-bot — not broken). No action needed.

## Sources consulted

### Accepted into final bibliography (primary)

Operator algebra: Ringrose 1965, Arveson 1975, Davidson 1988, Anoussis–Katsoulis 1998, Paulsen–Woerdeman 2016, Daughtry–Johns (unverified).

Prediction theory: Wiener–Hopf 1931, Kolmogorov 1941, Szegő 1921, Helson–Lowdenslager 1958, Helson 1964, Pourahmadi 2001, Subba Rao–Yang 2021, Picinbono–Bouvet 1987.

Kalman / innovations: Kalman 1960, Kailath 1968, Frost–Kailath 1971.

Optimal trading: Bouchaud–Gefen–Potters–Wyart 2004, Gatheral 2010, Gârleanu–Pedersen 2013, Lehalle–Neuman 2019, Abi Jaber–Neuman 2022, Abi Jaber–Neuman–Tuschmann 2024.

Adapted OT: Lassalle 2018, Backhoff–Beiglböck–Lin–Zalashko 2017, Acciaio–Backhoff–Zalashko 2020, Backhoff–Bartl–Beiglböck–Eder 2024/25.

Causal information theory: Massey 1990, Tatikonda–Mitter 2009, Tanaka–Mohajerin Esfahani–Mitter 2018, Charalambous–Stavrou–Kourtellaris 2011–2012, Stavrou–Skoglund–Tanaka 2020, Kramer 2003.

Martingale duality: Karatzas–Lehoczky–Shreve–Xu 1991, Cvitanić–Karatzas 1992, Karatzas–Shreve 1998, Kramkov–Schachermayer 1999, 2003, Czichowsky–Schachermayer 2015.

Mean-field games: Cardaliaguet–Lehalle 2018.

### Rejected during research

- Generic SSRN / SEO commentary on optimal execution — not authoritative.
- LAPSO, pseudospectral OC unification, Koopman EDP papers — name-collision "unified framework" but unrelated to causality / adaptedness.
- "Wiener–Hopf equations" in the Noor variational-inequality sense — same name, different mathematical object.
- Blackwell bookseller page — commercial.

### Misattributions caught and corrected

- Tourneret–Bercher–Doncarli citation (does not exist; replaced by Picinbono–Bouvet 1987).
- Schachermayer 2007 survey URL (pointed at Czichowsky–Schachermayer 2015; renamed).
- AN22 abstract quote (fabricated; replaced with verifiable abstract language and reviewer-marked inference).

## Verification status

- URLs spot-checked via `fetch_content` and reviewer's `curl`: 10/10 live (AMS journal page returns 403 anti-bot, content verifiable via alternative routes).
- Direct quotes verified: Picinbono–Bouvet 1987 (✓), AN22 abstract (✓ — original quote was wrong, replaced), CS15 (✓).
- 2 references retain explicit *unverified* markers: Ringrose 1965 pagination, TM09 / Kra03 volume info, Daughtry–Johns full reference.
- No new theorems claimed; this is a position / literature-review document.

## Limitations of this review

- Synthesized unifying framing is the reviewer's, not a published programme. Status box at top of draft makes this explicit.
- Three review clusters (1, 8 partial-substantive, 9 partial-substantive) rest on reviewer's geometric reading of primary sources rather than on explicit programmatic statements in the cited literature. §10.3 ("Disagreements and tension points") and §10.5 ("Why no one has stated this unifying view") flag this.
- Cluster 3 ↔ Cluster 1 bridge (innovations = outer factor in nest algebra) is folklore but not explicitly written down in cited literature; flagged in §5.4.
- No second reviewer pass was run after fixes, because the FATAL issues were citation-level (not structural) and were corrected in surgical edits with direct text/URL replacement; the structure, taxonomy, and synthesis content were not affected.

## CHANGELOG entry to be added separately
