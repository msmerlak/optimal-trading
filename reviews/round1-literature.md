# Round 1 Literature Review — `papers/noisy-signal-impact-trading.md`

Scope: literature positioning, citation accuracy, missing references, novelty inflation, and Sources-appendix URL/ID plausibility. No edits made to the draft.

Note on inputs: `plan.md` and `progress.md` referenced by the task do not exist in the repo root; review proceeds from the draft itself.

---

## 1. Per-citation accuracy

### [GP13] Gârleanu & Pedersen (2013), "Dynamic Trading with Predictable Returns and Transaction Costs," *JoF* 68(6):2309–2340.

- **Bibliographic data:** correct (journal, volume, pages, DOI `10.1111/jofi.12080`).
- **Attributed content — INCORRECT in §1 and §9.** The draft states that GP13 "resolves this tension in closed form when the impact decays exponentially and the signal follows an Ornstein–Uhlenbeck (OU) process," and in §9 says GP13 derives "a closed-form optimal policy for the exponential-decay impact + OU signal model." This misrepresents the GP13 model.
  - GP13 uses **quadratic instantaneous transaction costs** of the form $\tfrac{1}{2}\Delta x^\top \Lambda \Delta x$, **not** a transient/propagator impact kernel with exponential decay. There is no impact kernel $G(t)$ in GP13.
  - The "exponential decay" in GP13 is the **mean-reversion rate of the return-predicting factors** (multiple OU factors with different decay rates), not impact memory.
  - The "aim portfolio / trade-toward-the-aim" structure follows from a deterministic linear-quadratic problem whose optimal solution geometrically discounts future Markowitz portfolios.
- **Consequence:** §1's framing of GP13 as a transient-impact precedent for the current paper is misleading. The current paper's exponential-kernel + AR(1) result (eq. 12) is **not** the discrete-time GP13 solution; the two problems differ in cost structure. The claim in §9 that GP "aim-and-trade" is "the special case of (12) when the risk-aversion term is included" is wrong as stated — GP13 has no transient impact and (12) has no risk term and no position state, so neither nests the other. §10 item 7 already flags this recovery as "tentative"; that hedge should be strengthened or the claim removed.
- **Verdict:** bibliographic OK; **attribution incorrect**, needs rewrite.

### [Gat10] Gatheral (2010), "No-Dynamic-Arbitrage and Market Impact," *Quantitative Finance* 10(7):749–759.

- **Bibliographic data:** correct (DOI `10.1080/14697680903373692`).
- **Attributed content — partially correct but over-attributed.** Gatheral (2010) introduces the discrete propagator model with separable impact $h(v)\cdot G(t-s)$ and derives **no-dynamic-arbitrage constraints** that couple the instantaneous-impact function $h$ and the decay kernel $G$ (notably ruling out exponential decay with a non-linear $h$, and showing power-law decay $G(t)\sim t^{-\beta}$ is compatible). It does **not** state the result in the form "$\hat K(\omega)>0$ for all $\omega$ iff no dynamic arbitrage" used by the draft.
- The precise statement "**positive-definiteness of the symmetrised kernel** $K$ is equivalent to absence of price manipulation / dynamic arbitrage" is more accurately attributed to:
  - **Alfonsi, Schied & Slynko (2012)**, "Order book resilience, price manipulation, and the positive portfolio problem," *SIAM J. Financial Math.* 3(1), and
  - **Gatheral, Schied & Slynko (2012)**, "Transient linear price impact and Fredholm integral equations," *Math. Finance* 22(3):445–474.
- **Verdict:** Gat10 is the right citation for the no-dynamic-arbitrage *idea* and propagator framework; the specific PSD/no-arbitrage equivalence should also cite ASS12 / GSS12. The Bochner-theorem framing in §4.2 (used to obtain spectral factorisation) is the draft's own; Gat10 does not invoke Bochner in that form.

### [BGPW04] Bouchaud, Gefen, Potters & Wyart (2004), "Fluctuations and Response in Financial Markets…," *QF* 4(2):176–190.

- **Bibliographic data:** correct. arXiv `cond-mat/0307332` is the correct preprint identifier.
- **URL caveat:** the IOPscience link in the Sources appendix (`iopscience.iop.org/article/10.1088/1469-7688/4/2/007`) is the *legacy* publisher URL. *Quantitative Finance* moved from IOP to Taylor & Francis around 2007. For 2004 issues the IOP link historically resolved but is brittle; the canonical modern DOI is `10.1080/14697680400000022`. Either keep IOP link with a note, or replace with the T&F DOI.
- **Attributed content — correct in substance.** BGPW04 is the standard citation for the propagator model and the empirically observed power-law decay $G(t)\sim t^{-\beta}$ with $\beta$ small. One small caveat: the empirical dataset in BGPW04 is **Paris Bourse stocks** (as the draft states) plus comparison with the model — the attribution is fine. Note that the **propagator decomposition** itself first appeared (in a related form) in Bouchaud, Gefen, Potters & Wyart's earlier preprints and is sometimes co-credited with Lillo–Farmer's "long-memory of order signs" work; mentioning Lillo & Farmer alongside would be standard.
- **Verdict:** correct; consider fixing the URL and (optionally) co-citing Lillo–Farmer.

### [LN19] Lehalle & Neuman (2019), "Incorporating Signals into Optimal Trading," *Finance and Stochastics* 23(2):275–311.

- **Bibliographic data:** correct (DOI `10.1007/s00780-019-00382-7`, arXiv `1704.00847`).
- **Attributed content — partially overstated.** LN19:
  - Treats a **Markovian signal** added to an Almgren–Chriss-style linear temporary + linear permanent + linear transient-with-exponential-decay impact model. Their transient kernel is essentially the **Obizhaeva–Wang exponential resilience kernel**, not "a general class of decay kernels including exponential" — they essentially specialise to exponential resilience. Generalisation to broader kernels in that line is done by subsequent papers (Neuman–Voß, Abi Jaber–Neuman, Forde–Sánchez-Betancourt).
  - They obtain an explicit closed-form optimal trading rate involving the signal and inventory through an ODE/Riccati system; "explicit singular strategy" is a fair description for the OU + exponential case but the singular-control extension (block trades at boundaries) is in **Neuman–Voß (2021/22)**, not LN19.
- **Verdict:** correct paper for "signal + transient (exponential) impact" precedent. The draft should soften "general class of decay kernels including exponential" to "linear transient impact with exponential resilience," and credit Neuman–Voß for the singular-control extension if that flavour is intended.

### [AJN24] arXiv `2403.10273` — claimed: Abi Jaber, Neuman & Tuschmann, "Optimal Portfolio Choice with Cross-Impact Propagators."

- **Bibliographic plausibility:** arXiv id is in the right range for March 2024. The title and author roster are consistent with the public record of Abi Jaber and Neuman's joint program (Tuschmann is a known collaborator). I cannot reach the network to confirm verbatim, but the citation is plausible and internally consistent.
- **Attributed content — broadly correct.** The cross-impact / matrix-valued Volterra-propagator extension with operator-resolvent solution is the line of work pursued by this group. The draft's statement that it "subsumes ours as the scalar, non-cross-impact case" is reasonable provided the AJN24 setup is finite-horizon with terminal liquidation (which the propagator-cross-impact papers typically are). The current draft is stationary infinite-horizon, so "subsumes" is not literally true — the problems differ at the horizon level. Suggest: "treats the matrix-valued cross-impact extension of the finite-horizon propagator model" rather than "subsumes ours."
- **Verdict:** likely correct citation; tighten the "subsumes" framing.

### [AN22] arXiv `2211.00447` — listed in Sources as "Abi Jaber & El Euch."

- **Author attribution — INCORRECT (high confidence).** arXiv `2211.00447` is "Optimal Liquidation with Signals: the General Propagator Case" by **Eduardo Abi Jaber and Eyal Neuman** (2022). Omar El Euch is not an author — his work is primarily on rough volatility (with Rosenbaum, Fukasawa). The cite-key `AN22` in §1 ("Abi Jaber & Neuman") is consistent with the correct authorship; only the Sources entry is wrong.
- **Attributed content:** "general propagator case" is the correct one-line summary. They treat optimal liquidation with a Markovian signal and a **general (positive-definite) propagator kernel** (covering exponential and power-law), and obtain the optimum via an operator Riccati / Fredholm equation. This is the closest precedent to the present draft's §4–§6 and should be discussed in more depth (see §3 of this review on novelty).
- **Verdict:** **fix author list to Abi Jaber & Neuman** in the Sources block; cite-key is fine.

### [AC01] Almgren & Chriss (2001).

- Bibliographic data correct. Used only as a side-note in §8.2 for permanent-impact ill-posedness; attribution is fine.

### [GSS12] Gatheral, Schied & Slynko (2012).

- Listed in Sources, **not cited anywhere in the body.** SSRN link plausible (`abstract_id=1531466`). The published version is in *Mathematical Finance* 22(3):445–474, DOI `10.1111/j.1467-9965.2011.00478.x` — adding the DOI would be a stronger pointer.
- This paper is the **direct precedent** for the unconstrained Fredholm equation $K\ast x = f$ used in §3.2 / eq. (3), and for the PSD-as-no-arbitrage equivalence relied on in §2.4. Currently uncited in §9 — see §3 below.

---

## 2. Missing references

The following works are highly relevant and should be cited (and in some cases discussed in §9):

1. **Forde, Sánchez-Betancourt, Smith (2022/23)**, "Optimal trade execution for Gaussian signals with power-law resilience," *Quantitative Finance* (and Oxford ORA preprint).
   - Solves a stationary/finite-horizon optimal-execution problem with **Gaussian (OU-type) signal** and **power-law resilience kernel** via a Wiener–Hopf / spectral approach. This is the single closest precedent to §6 of the draft (power-law kernel + causal fractional derivative). Currently unacknowledged. **Must be cited and explicitly compared.**

2. **Vodret, Mastromatteo, Tóth, Benzaquen**, "A Stationary Kyle Setup: Microfounding Propagator Models," SSRN `3733453` (later published in *J. Stat. Mech.*, 2021).
   - Stationary equilibrium with propagator-type impact; provides the microfoundation for the stationary trading regime the draft works in. Relevant context for §2.3.

3. **Gatheral, Schied & Slynko (2012)** — as above; the Fredholm framework is theirs. Should appear in §9, not just in Sources.

4. **Alfonsi, Schied & Slynko (2012)**, "Order book resilience, price manipulation, and the positive portfolio problem," *SIAM J. Financial Math.* 3(1):511–533.
   - The precise PSD ⇔ no-price-manipulation equivalence used in §2.4.

5. **Bouchaud, Bonart, Donier & Gould (2018)**, *Trades, Quotes and Prices*, Cambridge University Press — Chapters on impact propagators and optimal trading. This is the standard textbook treatment; cite as the practitioner/textbook reference for the propagator + optimal-trading material in §2.

6. **Obizhaeva & Wang (2013)**, "Optimal trading strategy and supply/demand dynamics," *J. Financial Markets* 16(1):1–32.
   - The original exponential-resilience LOB model whose continuous limit underlies LN19's transient kernel. Worth a one-line citation when introducing the exponential kernel in §5.

7. **Neuman & Voß (2022)**, "Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact," *SIAM J. Financial Math.* 13(2):551–575 (arXiv `2002.09549`).
   - Extends LN19 with signal + transient impact + singular control. Closer to the "singular strategy" claim attributed to LN19.

8. (Optional) **Lillo & Farmer (2004)**, "The long memory of the efficient market," *Studies in Nonlinear Dynamics & Econometrics* 8(3) — empirical companion to BGPW04 on long-memory order-flow.

---

## 3. Novelty inflation / over-attribution

The draft is generally restrained in novelty claims (Abstract calls itself a "pedagogical entry point"; §1 says derivations are "deliberately elementary"). However, the following items risk reading as more novel than they are:

1. **§4 (Wiener–Hopf for stationary trading) is not new.** The causal Wiener–Hopf solution for the stationary version of the propagator problem (eq. 6) is, at the operator level, the same construction used in Gatheral–Schied–Slynko (2012) and Abi Jaber–Neuman (2022), and the explicit stationary Wiener–Hopf form appears in Forde–Sánchez-Betancourt (Gaussian signal + power-law resilience). The draft should explicitly say in §4 or §9 that "the causal Wiener–Hopf solution (6) is standard; our contribution is the explicit AR(1)+exponential reduction in §5 and the noisy-signal separation in §7." Without this acknowledgement, a reader of §4 alone would infer the W–H setup is original.

2. **§3.2 ("two-norms" Legendre–Fenchel viewpoint) is presentational, not new.** The cost-norm / dual-norm pair is standard in convex optimisation and implicit in GSS12's Fredholm formulation. The framing is a nice pedagogical reorganisation but should not be marketed as a result. Current §3.2 reads as a definition/observation, which is appropriate — keep it that way.

3. **§5 AR(1)+exponential reduction (eq. 12).** This *is* genuinely a clean closed form, but its content overlaps the discrete-time Obizhaeva–Wang / LN19 optimal trading rate. The draft should verify (and acknowledge) the overlap. A direct one-line comparison "(12) agrees with the stationary limit of LN19's optimal control with risk term set to zero and exponential resilience parameter $\lambda$" would be valuable — and is the natural cross-check.

4. **§7 (Wiener-filter + W–H separation).** The draft's hedging in §9 ("does not appear to have been explicitly connected to the Wiener–Hopf trading framework in the form of equation (20)") is appropriately careful. The certainty-equivalence / separation argument is classical (LQG); the new content is the *composition* with the kernel W–H factorisation. This is the most defensible novelty claim in the paper. **Suggestion:** state it more crisply in the Abstract and Introduction as the paper's primary contribution, since §5–§6 are largely re-derivations.

5. **§1 ("a different—and deliberately elementary—path").** Fine as positioning, but the implicit contrast with [LN19, AJN24, AN22] as "operator-valued Riccati or Fredholm equation rather than giving a closed-form recipe" understates that those papers also give closed-form recipes in special cases (OU + exponential; OU + power-law via Mittag-Leffler). Adjust the contrast to "we obtain the AR(1)+exponential closed form via a frequency-domain argument that bypasses the Riccati/Fredholm machinery."

---

## 4. Sources appendix — formatting and URL/ID plausibility

| # | Item | Issue |
|---|---|---|
| 1 | GP13 | DOI correct. The lhpedersen.com preprint URL is plausible but author preprint links rot; consider the SSRN id `1597052` as a more durable mirror. |
| 2 | Gat10 | DOI correct. SSRN id `1292353` is the right one. OK. |
| 3 | BGPW04 | IOP URL is the legacy publisher path and may not resolve; T&F DOI `10.1080/14697680400000022` is the canonical modern link. arXiv id correct. |
| 4 | LN19 | DOI correct; arXiv `1704.00847` correct. OK. |
| 5 | AJN24 | arXiv `2403.10273` plausible and consistent with the claimed title/authors. Confirm with the live arXiv abstract before submission. |
| 6 | AN22 | arXiv id `2211.00447` plausible. **Authors listed as "Abi Jaber & El Euch" — incorrect.** Should be **Abi Jaber & Neuman**. Title should be "Optimal Liquidation with Signals: the General Propagator Case." |
| 7 | AC01 | URL is the risk.net journal landing page (may require login). DOI for this issue is unstable; SSRN `53501` (preprint) is a common fallback. Otherwise OK. |
| 8 | GSS12 | SSRN id correct. **Add the published DOI `10.1111/j.1467-9965.2011.00478.x`** (*Mathematical Finance* 22(3):445–474). |
| 9 | Wiener (1949) | OK as bibliographic anchor; no URL needed. |
| 10 | Samko–Kilbas–Marichev (1993) | OK. |

Formatting: numbering is consistent; mixing of DOI/arXiv/SSRN is fine. No broken arXiv ID *patterns* detected (all six arXiv ids follow valid formats for their eras).

---

## Review

- **Correct:** Gat10, BGPW04, LN19, AC01 are bibliographically accurate. The §7 "denoise then trade" separation is the paper's most defensible novelty and is appropriately hedged.
- **Blocker:** §1 and §9 misattribute the GP13 model as "exponential-decay impact + OU signal." GP13 uses **quadratic instantaneous transaction costs** with multi-factor OU return predictors; there is no transient impact kernel. The §9 claim that (12) is GP "aim-and-trade with risk added" is incorrect as stated. **This must be rewritten** — it is the main framing of the paper and currently rests on a wrong premise.
- **Blocker:** Sources entry for arXiv `2211.00447` lists "Abi Jaber & El Euch"; the correct authorship is **Abi Jaber & Neuman**. Fix author list and add the correct title ("Optimal Liquidation with Signals: the General Propagator Case").
- **Note (high priority):** §9 omits **Forde, Sánchez-Betancourt et al.** on Gaussian-signal + power-law resilience — the closest direct precedent to §6 — and omits **Gatheral, Schied & Slynko (2012)** for the Fredholm form $K\ast x=f$ underlying §3. Both should be cited and discussed.
- **Note:** §2.4's PSD ⇔ no-dynamic-arbitrage equivalence is more precisely Alfonsi–Schied–Slynko (2012) / Gatheral–Schied–Slynko (2012); Gat10 alone is insufficient.
- **Note:** §9 description of LN19 ("general class of decay kernels including exponential" + "explicit singular strategy") overstates LN19, which is specifically about exponential resilience; the singular-control extension belongs to Neuman–Voß (2022).
- **Note:** §9 description of AJN24 as "subsumes ours" is not literal — AJN24 is finite-horizon cross-impact, the draft is stationary scalar. Soften to "treats the matrix-valued cross-impact extension."
- **Note:** Missing references that should be added: Forde–Sánchez-Betancourt; Vodret–Mastromatteo–Tóth–Benzaquen (SSRN `3733453`); Gatheral–Schied–Slynko (2012); Alfonsi–Schied–Slynko (2012); Bouchaud–Bonart–Donier–Gould (2018); Obizhaeva–Wang (2013); Neuman–Voß (2022); optionally Lillo–Farmer (2004).
- **Note:** Sources URL fixes: BGPW04 prefer T&F DOI `10.1080/14697680400000022`; GSS12 add DOI `10.1111/j.1467-9965.2011.00478.x`; AC01 consider adding SSRN preprint as durable fallback.
- **Note:** Novelty framing — §4's Wiener–Hopf solution (eq. 6) should be explicitly labelled "standard"; the contributions to claim are (a) the scalar-anticausal reduction in §5 (after cross-checking against LN19 / Obizhaeva–Wang), (b) the power-law fractional-derivative form in §6 (after comparison with Forde–Sánchez-Betancourt), and (c) the W–H ∘ Wiener-filter composition in §7. Recommend re-anchoring the Introduction around (c) since (a) and (b) overlap existing literature more than the current framing admits.

No edits applied to the draft, per review-only scope.
