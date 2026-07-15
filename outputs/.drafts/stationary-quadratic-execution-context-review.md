# Review: `stationary-quadratic-execution-context.md`

Scope: verify claims against the supporting research brief, spot-check top citations via Crossref/arXiv metadata, and flag positioning and style issues.

## FATAL — must fix before delivery

### F1. Reference [12] is misattributed
The literature review lists:
> Jusselin P, Rosenbaum M (2020) *A simple microstructural explanation of the concavity of price impact.* arXiv:2001.01860.

arXiv:2001.01860 is **Nadtochiy (2020)**, "A simple microstructural explanation of the concavity of price impact" (single author). It is not a Jusselin–Rosenbaum paper. The actual Jusselin–Rosenbaum paper on this topic is "No-arbitrage implies power-law market impact and rough volatility," *Mathematical Finance* 30(4):1309–1336 (2020), DOI 10.1111/mafi.12254 (arXiv:1805.07134).

The error is inherited from the research brief (§B), which uses the same wrong pairing. The in-text citation in §2.3 relies on this reference and must be repointed:
- If the intended source is Nadtochiy 2020, change the author to "Nadtochiy" and drop "Rosenbaum".
- If the intended source is Jusselin–Rosenbaum 2020, change the title and arXiv ID accordingly.
Either is defensible in §2.3, but the current combination cites a paper that does not exist.

## MAJOR — open questions / scope limits

### M1. §4.2 airfoil factorization claim lacks a source
The claim
> The Söhngen solution factorizes as u\*(t) = ω(t) × [regular signal-driven part] … the regular part converges to the translation-invariant solution of the whole-line singular integral equation
is load-bearing for the whole "interior asymptotic" framing (§4.3, §6, §7) and is stated without citation. The research brief explicitly flags this as an unsourced natural-consequence claim ("not sourced to a specific reference; if needed, a citation to Tricomi 1957 Ch. 4 or Söhngen's 1939 original will suffice, or the paper being reviewed should prove it directly," Gaps §). The document should either
- cite Tricomi 1957 Ch. IV explicitly for the factorization structure (which does appear there for the finite Hilbert transform inversion),
- cite the corresponding formula in Forde–Sánchez-Betancourt–Smith 2022 where the weight × regular-part decomposition appears in the execution context, or
- mark the T→∞ compact-interior convergence as a plausibility argument to be established in the paper itself.

As written, §4.2 asserts the decomposition and its limit as though standard; the "uniformly on compact interior subsets" convergence is genuinely nontrivial and is not in Tricomi 1957 in the form claimed.

### M2. Negative-literature claim is load-bearing but unverified
The paper's novelty positioning in §5 ("No prior paper combines: quadratic cost, transient (Volterra) impact, adapted stochastic signal, and stationary/whole-line horizon"), §3.2 ("appears not to have been solved in closed form"), and §6.1 rests on an exhaustive-negative search. The research brief itself qualifies this claim: "Have not directly verified whether any 2023–2025 preprint sets up a stationary whole-line signal-adaptive execution with transient impact" (Gaps §). Recommend either
- softening §5 to "we are not aware of a prior paper combining …" (the "we are not aware" hedge is already used implicitly but should be explicit), or
- documenting the arXiv/SSRN search that would substantiate the exhaustive claim.

The Gârleanu–Pedersen comparison (temp only, stationary, signal, quadratic) is verified against the standard reading of that paper and is safe.

### M3. §7 asserts "Wiener–Hopf factorization does not extend to nonlinear cost"
This is a definite negative claim about a research program. The brief does not support it; it merely notes concave impact is outside scope. A softer formulation ("Wiener–Hopf factorization is a Hilbert-space property tied to the quadratic form and does not obviously extend …") would match the evidence. As stated it invites counterexamples from nonlinear Riemann–Hilbert / factorization literature.

### M4. In-text citations missing from the Reference list
- §2.3: "Bouchaud 2010" and "Farmer et al." are cited without corresponding numbered entries. Either add references or drop the parenthetical.
- §3.2: "Cartea, Jaimungal & Sánchez-Betancourt 2022 and coauthors" is cited but has no entry. Add a reference or generalize the mention.
- §4.1: "Söhngen's 1939 airfoil equation" — brief explicitly kept this "cited via Tricomi 1957," which is fine, but the in-text mention could either be flagged as "(see Tricomi 1957 [26])" or given its own entry.

## MINOR — polish

### m1. Style violations against AGENTS.md
- "canonical" (§2.1, §5 caption implicitly) — AGENTS.md flags "canonical" as an empty intensifier.
- "genuine novelty" (§6 header: "What is genuinely new"), "genuinely stationary" (§3.2), "genuinely transient" (§3.2), "Genuinely stationary" (§3.2) — AGENTS.md flags "genuine/genuinely" as an empty intensifier.
- §4.3: "The 'interior far from boundaries' framing is not an ad hoc modeling choice. It is the natural setting to isolate …" — this is the "X is not Y, it is Z" construction AGENTS.md prohibits. Rewrite as "The interior framing isolates the signal-tracking content of the strategy from the terminal-condition transients that dominate any finite-T Söhngen inversion."
- §2.1: "canonical mean-variance efficient frontier" — drop "canonical".

### m2. Citation polish
- Ref [2] Almgren–Chriss: Crossref gives print year 2001 for the DOI; conventional citation is 2000. Either is defensible. No change needed but note the discrepancy is real.
- Ref [9] Almgren–Thum–Hauptmann–Li 2005: "Risk 18:57–62" — typically cited as Risk 18(7):58–62. Verify against the Risk table of contents.
- Ref [18] Neuman–Voß 2022: verified as *SIAM J. Financial Math.* 13(2):551–575; add DOI 10.1137/20M1375486 for consistency with other entries.
- Ref [3] Obizhaeva–Wang 2013: consider adding SSRN 686168 or a DOI for parity with other propagator references.
- Ref [20] Abi Jaber–Neuman: verified *Math. Finance* 35(4):841–866, DOI 10.1111/mafi.12465 — consider adding the DOI in addition to the arXiv ID.
- Ref [24] Gârleanu–Pedersen: no DOI given; add doi:10.1111/jofi.12080 for consistency.

### m3. Section 6 item 2 hedging
"The half-order factorization was implicit in Forde–SB–Smith [19]; the explicit signal-adaptive fractional-derivative form appears to be new." Reasonable, but consider explicitly noting where in Forde–SB–Smith the half-order structure appears (their Cauchy-kernel reduction step) so the "implicit" claim is verifiable.

### m4. §5 table minor
Row "Gatheral 2010" has "Horizon: —"; the paper is set on a finite interval when concrete strategies are discussed. "—" is defensible for a no-arbitrage characterization, but a footnote might help.

## Review
- **Correct.** Almgren–Chriss (DOI, journal, pages), Obizhaeva–Wang (journal, pages), Alfonsi–Fruth–Schied (arXiv), Gatheral 2010 (journal, pages), Gatheral–Schied–Slynko 2012 (journal, pages, DOI), Bouchaud–Gefen–Potters–Wyart (arXiv), Lillo–Farmer–Mantegna (*Nature* 421:129, arXiv cond-mat/0207428 for the same data), Tóth et al. 2011 (arXiv, *Phys. Rev. X*), Neuman–Voß 2022 (arXiv, SIAM JFM 13(2):551–575), Abi Jaber–Neuman 2025 (Math. Finance 35(4):841–866, arXiv), Abi Jaber–Neuman–Tuschmann 2024 (arXiv), Abi Jaber–De Carvalho–Pham 2024 (arXiv), Forde–SB–Smith 2022 (Quant. Finance 22(3):585–596, DOI), Dolinsky 2024 (arXiv), Kallsen–Muhle-Karbe 2017 (arXiv), Lehalle–Neuman 2019 (F&S 23(2):275–311) — all verified via Crossref/arXiv metadata.
- **Fixed.** None (review-only).
- **Blocker.** F1 (misattributed reference [12]).
- **Note.** M1–M4 (unsourced airfoil decomposition, unverified negative-literature claim, overbroad WH-nonlinear negative, missing in-text references) and style items m1–m4.

The core positioning — quadratic cost is the standard theoretical assumption, stationary whole-line signal-adaptive Volterra execution is a gap, Gârleanu–Pedersen is the closest antecedent — is well-supported by the brief and by the verifiable citations. The paper's novelty claim in §6 stands *if* the exhaustive-negative claim in §5 is softened to "not aware of." Fix F1 and add hedges/citations for M1–M3.
