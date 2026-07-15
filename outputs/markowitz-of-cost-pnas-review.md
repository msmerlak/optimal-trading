# Peer Review — *Fractional Derivatives as the Markowitz Rule for Cost-Managed Trading*

**Artifact:** `papers/markowitz-of-cost-pnas.md` (local Markdown, PNAS-format position paper, ~4281 words, 21 references).
**Reviewer role:** simulated pre-submission tough-but-constructive review.

---

## Summary Assessment

A well-written PNAS-format position paper that frames signal-adaptive optimal execution against a power-law impact kernel as the temporal analog of Markowitz portfolio theory, with a filtration Wiener–Hopf factorization $C = C_-C_+$ + optional projection $P_+$ as the structural addition forced by adaptedness. The main technical claim (Theorem 1) states that on the whole line with a stationary adapted signal, the optimal trading rate is a fractional derivative of order $1-\beta$ of the trader's forecast curve, with a clean three-step interpretation (whiten anticausally → project onto past → causal derivative). The Markowitz framing is decorative but honest; the mathematical novelty is the filtration-adapted Wiener–Hopf identity (11) and its collapse to (12) for the power-law kernel.

The paper is at PNAS-position-paper polish level. The proofs in §5 are sketches — appropriate for the format, gappy for a research paper. **One critical technical issue** (Fourier sign convention in eq. (9) not matching the standard convention of ref 17 [Samko et al.]) will be caught by any mathematically literate referee and needs to be fixed before submission. **Two major issues** concern rigor gaps in Lemma 1's operator-domain setup and the unproven $O(T^{\beta-1})$ boundary-mode claim in §4.1. Minor issues are mostly reference and presentation matters.

Provisional recommendation: **accept with revisions**, contingent on fixing the sign convention and closing a small number of rigor gaps.

---

## Strengths

- **Clean structural framing.** The Markowitz correspondence in §1.1 and §3.1 is pedagogically clear and the paper resists overclaiming: §3.1 explicitly notes that no factorization of $\Sigma$ is required in Markowitz, so the WH+$P_+$ apparatus is *net-new* content forced by adaptedness rather than a temporal restatement of a Markowitz feature.
- **Central identity (11) $(P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1}$** is stated cleanly and located precisely in the landscape (nest-algebra outer factorization, Wiener causal-realization). This is the load-bearing operator-theoretic claim and it earns its keep.
- **Theorem 1** gives an explicit fractional-derivative closed form (12) for a stationary adapted signal on $\mathbb R$, which — to this reviewer's knowledge — is not available in the neighboring papers (Gatheral–Schied–Slynko constant-signal on interval; Neuman–Voß exponential-kernel Riccati; Abi Jaber–Neuman resolvent characterization for general propagators).
- **Wiener–Kolmogorov reading (§3.2)** correctly identifies the whiten–project–unwhiten architecture as structurally shared with classical linear prediction, and the "change of loss ⇒ change of whitening operator" observation is a genuinely useful conceptual reframing.
- **Ornstein–Uhlenbeck example (§2.7)** is a well-chosen sanity check: the anticausal Marchaud derivative on the exponential forecast tail collapses to $\theta^\nu\alpha_t$ pathwise, giving a Markov-signal closed form (15). I checked the Marchaud integral by hand: $\int_0^\infty(1-e^{-\theta h})h^{-\nu-1}dh = \theta^\nu\Gamma(1-\nu)/\nu$, giving $(D_-^\nu\bar\alpha(t,\cdot))(t) = \theta^\nu\alpha_t$. ✓
- **Discussion section** appropriately gestures at boundary corrections, temporary impact, multi-asset extension, and numerical implementation without overclaiming; each subsection is one paragraph and stays within its evidence.

## Critical Issues

**C1. Fourier sign convention in eq. (9) inconsistent with ref 17.**
Eq. (9) states $\hat C_\pm(\xi) = c_\beta^{1/2}(\pm i\xi)^{-\nu}$, with $\hat C_+$ analytic in the upper half-plane and (per eq. 10) $C_+$ *causal*. Under the standard Samko–Kilbas–Marichev convention (ref 17) with $\hat f(\xi) = \int e^{-i\xi t}f(t)dt$, the causal Riemann–Liouville integral $I_+^\nu$ has Fourier symbol $(-i\xi)^{-\nu}$ (not $(+i\xi)^{-\nu}$), and this is what is analytic in the upper half-plane. The paper's assignment $\hat C_+ = (+i\xi)^{-\nu}$ combined with "$C_+$ causal" is not simultaneously consistent with any standard Fourier sign convention.

The proof of Theorem 1, step (c), uses the symbol identity $\hat C(\xi)(i\xi)^\nu = c_\beta(-i\xi)^{-\nu}$, which is dimensionally correct but presupposes $D_+^\nu \leftrightarrow (i\xi)^\nu$, again the reverse of ref 17.

**Fix:** either (a) state the paper's Fourier convention explicitly at first use and note the departure from ref 17, or (b) flip the $\pm$ signs so that $\hat C_+ = c_\beta^{1/2}(-i\xi)^{-\nu}$ throughout, and update the proof of Theorem 1 correspondingly. This is a bookkeeping fix, but a referee will flag it and until it's fixed the reader has to guess the intended convention.

## Major Issues

**M1. Lemma 1 operator-domain setup is under-specified.**
§2.4 states $(P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1}$ on $L^2_{\rm adap}$. The proof in §5 shows this is a *left* inverse via the triangularity identities. Missing: (i) precise statement of which homogeneous Sobolev spaces the factors $C_\pm$, $C_\pm^{-1}$ are bounded between (the paper mentions $\dot H^{-\nu}\to\dot H^\nu$ but doesn't track the individual factors); (ii) verification that $P_+CP_+$ has closed range on the specified domain, so that the two-sided inverse exists; (iii) explicit statement of the nest-algebra outer factorization theorem from refs 15, 16 being invoked. A specialist can fill these in; a referee will ask.

**Fix:** in the proof of Lemma 1 add one paragraph pinning down the domain-codomain of $C_\pm^{\pm 1}$ and quoting the specific outer-factorization theorem (e.g., Arveson 1975 Theorem 4.4.2 or the Davidson §7 equivalent).

**M2. $O(T^{\beta-1})$ boundary-mode claim in §4.1 has no proof or citation.**
The paper asserts that on the interior region $[\varepsilon T, (1-\varepsilon)T]$, the two Söhngen–Tricomi boundary modes contribute an $O(T^{\beta-1})$ correction, and that this is subleading to the bulk term for stochastic signals with $\Theta(1)$ tradeability norm. The scaling is plausible on dimensional grounds — the modes $\phi_1(t) = (t(T-t))^{(\beta-1)/2}$ scale as $T^{\beta-1}$ on the interior — but the claim that this is *subleading* is not proven and no reference is given for the asymptotic. Since the whole point of the paper is that the stationary bulk formula subsumes the finite-horizon literature, this is the load-bearing asymptotic and it needs at least a citation or a one-line justification.

**Fix:** add a citation (or a short bound) showing that the KKT-coefficient scaling of the Söhngen–Tricomi modes against a $\Theta(1)$ tradeability-norm signal is compatible with the $O(T^{\beta-1})$ claim on interior regions.

**M3. Novelty positioning against ref 8 (Abi Jaber–Neuman) is not explicit enough.**
§1.2 describes (8) as "characterized as the solution of an operator-valued resolvent equation; closed forms are available only in specific specializations." §1.3 (ii) claims the current paper's identity (11) is new. This positioning is defensible but not decisive: (8) treats the general propagator case with an adapted signal on a bounded interval. A reader wanting to place the present paper's contribution needs a direct comparison. In one worked example (e.g., stationary Gaussian alpha on $\mathbb R$, power-law kernel), what does (8)'s resolvent framework reduce to, and does it match (12)? A single sentence or a one-line comparison would eliminate the ambiguity.

**Fix:** add one to two sentences to §1.3 comparing (12) directly to what (8)'s resolvent framework produces for a stationary adapted signal on $\mathbb R$ (or note that the whole-line stationary case is outside (8)'s bounded-horizon setup).

## Minor Issues

**m1. Constant $c_\beta$.** Verified: $c_\beta = 2\Gamma(1-\beta)\sin(\pi\beta/2)$ is the Fourier transform of $|t|^{-\beta}$ under the standard convention. ✓ Not an issue, just noting the check.

**m2. Equation label collision.** §3.2's parenthetical "(14)" refers to reference [14] (Wiener 1949), but the tag `(14)` is also used for the in-text OU equation. Reader can figure it out from context but it is momentarily confusing. Consider rewording "the Wiener–Kolmogorov linear predictor of a stationary process from its own past [14] has..." to make the bracket-form unambiguous.

**m3. Table 1 row ordering.** The "Value" row uses $\|P_+ C_-^{-1}\alpha\|_{L^2}^2$ notation before $C_-^{-1}$ has been introduced in a later row ("Structure forced by feasibility"). Consider reordering so Structure precedes Value, or add a footnote flagging that the Value row's execution entry uses the WH factors defined below.

**m4. §4.2 temporary-impact $\eta\to 0$ limit.** The claim "The $\eta\to 0$ limit recovers (12)" is a singular limit (losing high-frequency coercivity) and merits one clause acknowledging that the recovery holds under the spectral-decay hypothesis of §2.1. Currently reads as if the limit is automatic.

**m5. Reference cleanup.** Ref 8 marks "(2025)" plus arXiv ID; check current publication status. Refs 7, 10, 11 may still be provisional at submission. Ref 15 (Arveson 1975 nest algebras) cited in-text but the *specific* factorization theorem used is not named or numbered.

**m6. Style / AGENTS.md compliance.** No rhetorical questions found. No "X is not Y, it is Z" constructions found. No banned words. Style rules respected.

**m7. Data availability line** is present ("No empirical data are used in this paper"). Correct and minimal.

## Reproducibility and Verification

- **Empirical reproducibility:** N/A (no empirical work, correctly declared).
- **Mathematical reproducibility:** Proofs in §5 are sketches. A specialist can fill in the gaps using refs 13, 14, 15, 16, 17, 20, 21. Non-specialist readers will not be able to reconstruct the proofs from the paper alone; this is standard for PNAS position papers but is a limitation.
- **Numerical implementation:** §4.4 claims $O(N\log N)$ per time step via FFT. Standard for Toeplitz operations, no numerical results are shown or claimed. No implementation code is offered — appropriate for a theoretical position paper.
- **Verification performed by this reviewer:**
  - Constant $c_\beta = 2\Gamma(1-\beta)\sin(\pi\beta/2)$ (§1.1, §2.1): **Verified** by direct Fourier calculation of $\int_{-\infty}^\infty|t|^{-\beta}e^{-i\xi t}dt$.
  - OU identity $(D_-^\nu\bar\alpha(t,\cdot))(t) = \theta^\nu\alpha_t$ (§2.7 eq. 14): **Verified** by direct Marchaud integration.
  - Symbol identity $\hat C(\xi)(i\xi)^\nu = c_\beta(-i\xi)^{-\nu}$ (Proof of Theorem 1 step c): **Verified** by direct algebra with $2\nu = 1-\beta$.
  - Adjoint identity $C_+^\ast = C_-$: **Verified** from kernel-flip.
  - Fourier convention in eq. (9): **Failed** — inconsistent with ref 17 (see C1).
  - Word counts (Significance 119, Abstract 230): **Verified** within PNAS caps of 120 / 250.
  - PNAS format compliance: **Verified** section structure, missing equations in abstract/significance, data availability line present.

## Inline Annotations

- **§1.1 eq. (1):** cost functional. Symmetric quadratic in $u$, PSD constant $c_\beta$ implicit; correct.
- **§1.1 dual norms (3)–(4):** clean pedagogical setup for the Mahalanobis-value formula; also foreshadows the tradeability norm on signals.
- **§1.3 (ii) eq. (5):** the identity (5) is stated as the paper's main tool. Load-bearing.
- **§2.3 eq. (9):** *see C1 — Fourier sign convention issue.*
- **§2.4 Lemma 1:** *see M1 — operator-domain setup under-specified.*
- **§2.5 Theorem 1 / eq. (12):** central closed-form claim. Proof in §5 is a sketch.
- **§2.7 eq. (14):** OU pathwise identity — verified above.
- **§3.1 Table 1:** *see m3 — row ordering nit.*
- **§3.2:** Wiener–Kolmogorov reading. Structurally correct; "change of loss ⇒ change of whitening" is the useful takeaway.
- **§4.1:** *see M2 — $O(T^{\beta-1})$ boundary-mode claim needs support.*
- **§4.2:** *see m4 — $\eta\to 0$ limit is singular, note the spectral-decay hypothesis.*
- **§5 Proof of Lemma 1:** *see M1.*
- **§5 Proof of Theorem 1 step (c):** the symbol identity is correct up to sign convention (see C1).

## Recommendation

**Accept with revisions** for the PNAS position-paper format.

Required revisions before submission:
1. Fix the Fourier sign convention (C1). Either state the convention explicitly and note the departure from ref 17, or flip the $\pm$ signs throughout §2.3 and the proof of Theorem 1.
2. Tighten Lemma 1's operator-domain setup by one paragraph (M1).
3. Support the $O(T^{\beta-1})$ boundary-mode claim in §4.1 with a citation or a short bound (M2).
4. Add one to two sentences of direct comparison to ref 8's resolvent framework (M3).

Optional improvements: minor items m1–m7.

If the format is instead a full research paper (Math Finance, SIAM Journal on Financial Mathematics), the proofs in §5 need substantial expansion — currently sketch-level.

## Sources

- `papers/markowitz-of-cost-pnas.md` — the paper under review.
- `AGENTS.md` — workspace style rules (compliance checked).
- `CHANGELOG.md` — session history of prior refactoring (for context; no claims taken from it).
- References [17] Samko–Kilbas–Marichev (1993), [14] Wiener (1949), [13] Krein (1962), [15] Arveson (1975), [16] Davidson (1988), [21] Klenke (2014) — used implicitly to check the sign convention, the operator-domain claim, and the specific outer-factorization theorem needed. Not re-fetched externally for this review.

---

*Review artifact written to `outputs/markowitz-of-cost-pnas-review.md`. Evidence trace at `outputs/.drafts/markowitz-of-cost-pnas-review-evidence.md`. Plan at `outputs/.plans/markowitz-of-cost-pnas-review-plan.md`.*
