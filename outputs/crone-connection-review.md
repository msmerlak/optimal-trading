# Review: How similar is CRONE, really?

**Artifact reviewed.** `papers/markowitz-of-cost-pnas.md`, §1.3(iii) closing claim.
**Claim under review.**
> "The half-order factorization was implicit in (11); the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new, and it makes contact with the CRONE / fractional-PID control tradition (18, 19), to our knowledge not previously connected to execution."

**References involved.**
- [18] Oustaloup A (1991), *La Commande CRONE* (Hermès).
- [19] Chen, Petráš, Xue (2009), "Fractional order control — A tutorial", *Proc. American Control Conf.*, 1397–1411.

---

## Summary Assessment

The CRONE connection as currently phrased is **thematically real but mechanically superficial**. Both traditions produce control actions expressed through one-sided fractional derivatives of order in $(0,1)$, and both arrive at fractional orders determined by a fractional-response plant. Beyond that shared operator vocabulary, essentially nothing else transfers: design goal, derivation, the object being differentiated, the two-sided-plus-projection structure, and the meaning of "optimal" all differ. The claim "makes contact with the CRONE / fractional-PID control tradition" is defensible as a footnote acknowledgement of prior fractional-calculus use in control engineering, but it should not be read as a research bridge. The parenthetical "to our knowledge not previously connected to execution" is defensible: I found no prior work joining these two literatures.

**Verdict on the specific question.** Similarity is **substantial only at the level of the operator alphabet** (both use $D^n$, $n \in (0,1)$, in a linear map from an input to a control action); it is **superficial** at the level of derivation, structural composition, and optimality criterion.

---

## Strengths of the claim as written

- The claim is hedged ("makes contact with") and cites two legitimate reference points (Oustaloup's 1991 CRONE monograph; Chen–Petráš–Xue 2009 tutorial). It does not claim a formal reduction, isomorphism, or generalization.
- The parenthetical "to our knowledge not previously connected to execution" survives a targeted search: no prior work in the optimal-execution literature (Bouchaud, Gatheral, Neuman–Voß, Abi Jaber–Neuman, Forde–Sánchez-Betancourt–Smith, Jusselin–Rosenbaum) cites CRONE / Oustaloup / FOPID.
- The claim serves a legitimate rhetorical purpose: signalling to a control-theory audience that the object derived here (a fractional derivative of an adapted signal) has family resemblance to objects they already know.

## Critical Issues

None. The claim as written is not incorrect. What follows is a set of soft objections that a hostile reviewer with control-engineering expertise might raise.

## Major Issues

### M1. "Makes contact with" oversells the mechanical kinship

CRONE and the paper agree on very little beyond the alphabet:

| Aspect | CRONE / FOPID | This paper |
|---|---|---|
| Design goal | Iso-damping / phase-margin robustness to plant gain variations ($\mathcal{H}_\infty$-style) | LQ optimality against a specific propagator plant |
| Origin of fractional order | Design/tuning parameter chosen for a target open-loop Nichols shape | *Derived* $\beta = (1-\gamma)/2$ from Wiener–Hopf factorization of the impact-kernel Fourier symbol $|\xi|^{\gamma-1}$ |
| Object differentiated | Error signal $e(t) = r(t) - y(t)$ | Trader's forecast curve $\bar\alpha(s,\cdot)$ (a two-argument adapted process) |
| Operator form | One-sided $s^n$ (Laplace-domain); implemented as a rational band-limited IIR ("Oustaloup approximation") | Two-sided composition $D_+^\beta \circ P_+ \circ D_-^\beta$ with an anticausal factor and a filtration projection |
| Adaptedness | Feedback controllers are causal by construction; no explicit projection | The anticausal $D_-^\beta$ would use future signal values, so a conditional-expectation projection $P_+$ is essential; the projection between the two halves is the paper's distinctive object |

The paper's central operator is the projection-sandwiched product $D_+^\beta P_+ D_-^\beta$; nothing in CRONE has this shape. "Makes contact" reads as though a control theorist could pick up the paper and recognize it, which is only partially true.

### M2. The genuine kinship worth calling out is narrower

The one substantive alignment worth stating explicitly: **when the plant/kernel has fractional-order response, the optimal controller involves fractional derivatives whose order matches the plant exponent.** This is CRONE's founding observation (Oustaloup's "fractal robustness" derivation, ESAIM 1998) and it is what the paper's Wiener–Hopf argument confirms in a rigorous LQ setting with a specific plant.

A more defensible phrasing would be something like:

> "The explicit reduction is new. It shares with the CRONE / fractional-PID control tradition (18, 19) the observation that fractional-response plants beget fractional-order optimal controllers, though the exponent here is derived from the impact-kernel decay and the object differentiated is an adapted forecast curve rather than an error signal."

This is longer but harder to attack.

### M3. Risk of provoking a hostile control-engineering reviewer

A PNAS control-theory reviewer skimming §1.3(iii) may respond: "The authors invoke CRONE but their object is not a CRONE controller — it is a two-sided fractional Volterra operator with a filtration projection. CRONE is a robust-control design methodology, not a general fractional-operator library." Toning down the connection (as in M2) preempts this without weakening the paper.

## Minor Issues

### m1. FOPID origin is Podlubny 1994

For completeness, the fractional-PID (PI$^\lambda$D$^\mu$) form was introduced by Podlubny 1994 (*IEEE TAC* 44:208–214, 1999 published version), predating and separate from CRONE. Ref [19] (Chen–Petráš–Xue) covers this, so the citation is not wrong, but "CRONE / fractional-PID" combines two distinct traditions under one label. Consider "CRONE and fractional-PID control (18, 19)".

### m2. Chen–Petráš–Xue 2009 is a tutorial

Ref [19] is a tutorial paper, not a primary technical reference. For a claim about a "tradition", one primary reference (Oustaloup 1991 or Podlubny 1994/1999) plus one tutorial is fine.

### m3. Implementation-level footnote

If any reviewer asks how the paper's Marchaud derivatives connect to what CRONE actually implements: CRONE's fractional operators are always realized as band-limited rational IIR approximations (Oustaloup approximation), whereas the paper's Marchaud operators are exact in principle (approximated in §4.4 via Toeplitz/FFT). This is a real difference in operator status but not worth adding to the abstract; a footnote in §4.4 could observe it if the paper wants to strengthen the numerical section.

## Reproducibility and Verification

**Verification: PARTIAL.**

- Verified from primary sources (Oustaloup 1993 IEEE, 1998 ESAIM; Sabatier 2013; Lanusse 2013) that CRONE's design principle is frequency-domain iso-damping robustness, and that its fractional operators are one-sided Laplace-domain $s^n$ implemented as band-limited IIR approximations. Sources listed below.
- Verified from Podlubny 1994/1999 (IEEE TAC 44:208–214, via secondary tutorial descriptions) that FOPID has form $K_p + K_i s^{-\lambda} + K_d s^{\mu}$.
- Verified via targeted web searches (`"fractional order control" "optimal execution"`, `"CRONE" "trading"`, `"fractional PID" "market impact"`) that no prior work connects CRONE/FOPID to optimal execution.
- **Not verified**: I did not read Oustaloup's 1991 CRONE monograph in French, only English-language derivative literature. If the monograph contains a formal derivation that closely parallels the paper's Wiener–Hopf construction, this assessment would need revising; from the extensive derivative literature I read, this is unlikely.

## Inline Annotations

**Line 67 of `papers/markowitz-of-cost-pnas.md`.**

Current: "the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new, and it makes contact with the CRONE / fractional-PID control tradition (18, 19), to our knowledge not previously connected to execution."

Suggested (in decreasing order of change):

Option A (minimal): change "makes contact with" to "shares fractional-derivative operators with" — hedges the mechanistic claim.

Option B (medium): "the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new. It shares with the CRONE and fractional-PID control tradition (18, 19) the phenomenon that fractional-response plants beget fractional-order controllers, though the exponent here is derived from the impact-kernel decay rather than tuned for iso-damping robustness; to our knowledge these literatures have not previously been connected." — states the actual kinship and hedges the rest.

Option C (drop the CRONE nod): "the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new." — safest if you don't want to defend the connection at review.

I would recommend **Option B**: the acknowledgement is worth having (it broadens the audience and is factually true at the "fractional plants → fractional controllers" level), but the current phrasing is too suggestive of a research bridge that does not exist.

## Recommendation

**Accept the claim with minor phrasing revision (Option B above).** The connection is real at the level of shared operator vocabulary and shared "fractional plant → fractional controller" phenomenon, and the "not previously connected to execution" note survives the search. The current "makes contact with" phrasing is defensible but risks provoking a control-engineering reviewer who will correctly note that the paper's central operator ($D_+^\beta P_+ D_-^\beta$) is not a CRONE controller and that the derivation, loss, and design objective are all different. Rephrasing to state the actual kinship narrowly costs one sentence and removes the attack surface.

## Sources

- Sabatier J, Lanusse P, Melchior P, Oustaloup A (2013), "CRONE Control: Principles, Extensions and Applications", *J. Applied Nonlinear Dynamics*, doi:10.5890/jand.2013.08.001
- Lanusse P, Malti R, Melchior P (2013), "CRONE control system design toolbox for the control engineering community: tutorial and case study", *Phil. Trans. R. Soc. A* 371, doi:10.1098/rsta.2012.0149
- Oustaloup A, Sabatier J, Lanusse P (1993), "The great principles of the CRONE control", *Proc. IEEE SMC*, doi:10.1109/icsmc.1993.384860
- Oustaloup A, Mathieu B, Lanusse P (1993), "Third generation CRONE control", *Proc. IEEE SMC*, doi:10.1109/icsmc.1993.384864
- Oustaloup A, Sabatier J, Moreau X (1998), "From fractal robustness to the CRONE approach", *ESAIM: Proc.* 5:177–192, https://www.esaim-proc.org/articles/proc/pdf/1998/03/proc-Vol5.15.pdf
- Lanusse P, Oustaloup A, Sabatier J, "Fractional Order PID and First Generation CRONE Control System Design", in *Fractional Order Differentiation and Robust Control Design* (Springer 2015), doi:10.1007/978-94-017-9807-5_2
- Podlubny I (1999), "Fractional-order systems and PI$^\lambda$D$^\mu$-controllers", *IEEE Trans. Automat. Contr.* 44:208–214, doi:10.1109/9.739144 (originally 1994)
- Padula F, Visioli A (2011), "Tuning rules for optimal PID and fractional-order PID controllers", *J. Process Control* 21:69–81
- Das S et al. (2018), "Tuning guidelines for fractional order PID controllers: Rules of thumb", *Mechatronics*, https://www.sciencedirect.com/science/article/pii/S0957415818301612
- Evidence notes: `outputs/.drafts/crone-connection-review-evidence.md`
- Plan: `outputs/.plans/crone-connection-review-plan.md`
