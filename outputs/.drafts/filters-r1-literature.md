# Literature-accuracy review: `tex/optimal-trading-filters.tex` (r1)

Role: literature-accuracy and claims reviewer. Read-only pass; no repository files were modified.
Primary sources checked: full-text extraction of Forde–Sánchez-Betancourt–Smith (FSS), *Quant. Finance* 22(3):585–596 (`/Users/orwell/Downloads/1469768820211950919.md`); Gârleanu–Pedersen 2016 working-paper PDF (nbgarleanu.github.io); Neuman–Voß arXiv:2002.09549v3 full text; Abi Jaber–Neuman arXiv:2211.00447v2 full text; web verification of remaining bibliography and of nest-algebra factorization literature.

## Summary

The draft solves the adapted gain–risk–cost problem (temporary + transient-propagator + inventory-risk frictions, adapted signal) via a Wiener–Hopf factorization with the half-line projection replaced by the optional projection, obtaining explicit trading filters for stationary Gaussian signals and, on finite horizons, Gohberg–Krein-type terminal-anchored factors. It positions itself against GSS 2012, Lehalle–Neuman 2019, Neuman–Voß 2022, Abi Jaber–Neuman 2025, and FSS 2022, and claims to recover the Gârleanu–Pedersen aim rule, the NV solution in stationary form, and the FSS/GSS finite-horizon solutions.

Most characterizations of prior work check out against the primary sources, including all the FSS-specific claims in §7. Three claims do not survive scrutiny: the blanket Gohberg–Krein/Arveson factorization statement in §7 (false for continuous nests by Larson 1985), the parenthetical describing Neuman–Voß's objective (they already include running inventory risk), and the novelty sentence in §1.4 ("covers the three frictions jointly", "closed-form rather than characterized as a fixed point"), which overreaches relative to Abi Jaber–Neuman 2025, GP 2016 Prop. 2, and the uncited Abi Jaber–Neuman–Tuschmann cross-impact paper.

---

## BLOCKERS (false claims about prior work; novelty-undermining omissions)

### [B1] §7: "every strictly positive $G_T$ … factors as $G_T = C_-C_+$", attributed to Gohberg–Krein (1970) and Arveson (1975) — false at this generality
**Location:** §7, first paragraph; echoed by "the abstract setting is Arveson's factorization of positive operators on the nest of adapted subspaces" in §1.4.
The chain $\{P_{[0,t]}\}$ is a continuous (uncountable) nest. Larson, *Nest Algebras and Similarity Transformations*, Ann. of Math. 121 (1985) 409–427, proved: "a complete nest $\mathcal N$ is countable **if and only if** every positive invertible operator $T$ admits a factorization $T = A^*A$" with $A, A^{-1}$ in the nest algebra (zbMATH/MaRDI review of doi:10.2307/1971180; see also Anoussis, *Factorisation in nest algebras*, Proc. AMS 1997, doi:10.1090/s0002-9939-97-03430-8, which gives necessary-and-sufficient conditions precisely because unconditional factorization fails for continuous nests). Gohberg–Krein 1970 prove special factorization along continuous chains for operators of the form $I + K$ under regularity conditions on $K$, not for arbitrary strictly positive operators. Neither cited source supports "every strictly positive $G_T$ factors."
**Fix:** restrict the claim to the class actually used — e.g. $G_T = \eta I + K$ with $K$ a Hilbert–Schmidt/continuous-kernel integral operator (Gohberg–Krein special factorization), plus the explicitly exhibited factor \eqref{eq:gk-kernel} for the pure power-law case — and cite Larson 1985 or drop the universal quantifier. The paper's actual operators are fine; only the attribution is wrong.

### [B2] §5.3: "The stationary counterpart (terminal penalty replaced by running inventory risk)" — mischaracterizes Neuman–Voß's objective
**Location:** §5.3, second sentence.
NV 2022 eq. (2.6) (arXiv:2002.09549v3): $J(u) = \mathbb E[\int_0^T(P_t-\kappa Y_t^u)u_t\,dt - \lambda\int_0^T u_t^2\,dt + X_T^uP_T - \phi\int_0^T (X_t^u)^2 dt - \varrho(X_T^u)^2]$, with the paper's own gloss: "The fourth and fifth terms in (2.6) implement a penalty $\phi > 0$ and $\varrho > 0$ on her **running and terminal** inventory, respectively." NV already have running inventory risk; the parenthetical implies they do not. What the stationary problem actually changes: infinite horizon, terminal penalty dropped, stationary regime.
**Fix:** rewrite the parenthetical, e.g. "(infinite horizon, terminal penalty dropped)". Separately, note that the abstract's "reduces, in the stationary regime, to a two-moving-average filter" reads as a limit statement about NV's finite-horizon solution; the draft solves the stationary analogue but does not prove the $T\to\infty$ limit of NV's time-varying feedback coefficients. Either prove convergence or say "stationary analogue."

### [B3] §1.4 novelty sentence: "the adapted optimum here is closed-form rather than characterized as a fixed point, covers the three frictions jointly" — overreaches relative to prior work
**Location:** §1.4, final paragraph.
Three problems:
1. **Abi Jaber–Neuman 2025 covers the three frictions jointly.** Their objective (2.6) contains temporary impact $\lambda$, a general Volterra propagator (explicitly including power-law $t^{-\beta}$, $0<\beta<1/2$), a **running inventory penalty** $\phi\int (Q_t^u)^2 dt$, terminal penalty $\varrho$, and a progressively measurable signal — on a finite horizon. And they state: "the problem can be solved explicitly despite the path-dependency of the model … the optimal strategy $u^*$ is explicitly given by the solution to a linear Volterra equation … Both $a$ and $B$ are given explicitly" (arXiv:2211.00447v2, §2). Calling their result "characterized as a fixed point" while calling one's own "closed-form" is contestable — their solution is an explicit Volterra/resolvent formula, as is NV's ("can be solved explicitly in terms of the matrix exponential function"). The defensible distinctions are: infinite-horizon stationarity, transfer-function/filter closed forms with no operator discretization, joint whole-line treatment, and the contrarian/response analysis. State those instead.
2. **GP 2016 Proposition 2** already solves the three-friction problem for the exponential kernel (temporary $\Lambda$ + persistent distortion $D$ with resiliency $R$ + risk $\gamma\Sigma$ + signals, infinite discounted horizon, explicit feedback). §5.3 credits only NV for the exponential three-friction case; GP2016 Prop. 2 should be acknowledged there (NV themselves adopt "the price impact model from Gârleanu and Pedersen [20]").
3. **Missed closest prior work:** Abi Jaber, Neuman, Tuschmann, *Optimal Portfolio Choice with Cross-Impact Propagators* (arXiv:2403.10273; SIAM J. Fin. Math.), whose abstract reads "We solve the maximization problem explicitly in terms of operator resolvents, by reducing the problem to … stochastic Fredholm equations" — a portfolio-choice (not pure liquidation) formulation with temporary + transient + risk + signal. Note also that the draft's descriptor "general propagators via stochastic Fredholm equations \citep{AbiJaberNeuman2025}" actually fits this paper better than 2211.00447, whose method is an operator-valued Riccati equation plus an $L^2$-valued free-boundary BSDE (the phrase "stochastic Fredholm" appears in their discussion of GSS/FSS, not as their own method). Either cite 2403.10273 or re-describe 2211.00447's method.
No prior "Wiener–Hopf / spectral-factorization optimal execution" paper surfaced in the searches (queries listed under Sources); the method claim itself appears safe. The overclaim is confined to the "three frictions jointly" and "fixed point" contrasts.

---

## FIXES WORTH DOING NOW (imprecise attributions)

### [F1] §7: "the Abel-type inversions of \citet{ChakrabartiGeorge1994} implementing $C_\pm^{-1}$" — wrong operator
FSS use Chakrabarti–George to invert the **full two-sided** generalized Abel operator in one shot: "We can read off the solution to (18) more explicitly from Chakrabarti and George (1994) … the explicit solution is given in equations (3.14a) and (3.14b)" — i.e. C–G implements $G_T^{-1}$, not the individual factors. The factor inversions in FSS are done via weighted Riemann–Liouville operators: "$T = B^{-1}I_\nu B$ … so $I_\nu^{-1} = \Gamma(1-r)D^r$" (p. 591). Reword to "with the Abel-type inversion of Chakrabarti and George (1994) implementing $G_T^{-1}$ (equivalently, weighted Riemann–Liouville inversions implementing the factors)". Also consider crediting Porter–Stirling (1990, Ex. 9.2) as FSS's source for the $TT^*$ decomposition.

### [F2] §1.1: "the exponential kernel $G(t)=e^{-\kappa|t|}$ underlies the resilience models of \citet{ObizhaevaWang2013} and the Almgren–Chriss line"
Almgren–Chriss 2001 has temporary + permanent linear impact and no propagator; the exponential kernel underlies Obizhaeva–Wang, and recovers the AC cost structure only in the $\kappa\to\infty$ / $\kappa\to0$ limits. Reword (e.g. "…of Obizhaeva and Wang (2013), and interpolates to the Almgren–Chriss temporary/permanent costs in its fast- and slow-decay limits").

### [F3] §1.1: Lillo–Farmer–Mantegna 2003 cited for power-law time decay of propagators
LFM 2003 (*Master curve for price-impact function*, Nature 421:129–130) is about the concave shape of instantaneous impact versus volume, not the temporal decay exponent of $G$. The $\beta\in(0.2,0.6)$ decay claim should rest on BGPW 2004 (and, if desired, Brokmann–Sérié–Kockelkoren–Bouchaud 2015 or Bouchaud et al., *Trades, Quotes and Prices*, 2018); Jusselin–Rosenbaum 2020 is a theoretical consistency argument, fine as a supporting cite.

### [F4] §5.2: GP2016 rate formula holds at zero discount
GP2016 Prop. 1(iv): $\bar M^{\rm rate} = a/\lambda = \tfrac12(\sqrt{\rho^2 + 4\gamma/\lambda} - \rho)$, "for a patient agent with $\rho \approx 0$ … the trading rate is approximately $\sqrt{\gamma/\lambda}$"; aim $= \gamma^{-1}\Sigma^{-1}B(I + a/\gamma\,\Phi)^{-1}$, which in one dimension equals the Markowitz position times $a'/(a'+\theta)$ with $a' = \sqrt{\gamma/\lambda}$ — exactly the draft's \eqref{eq:gp} — but only at $\rho = 0$. Add "(zero discount rate)" to "This is the continuous-time solution of \citet{GarleanuPedersen2016}". The 2013-vs-2016 split itself is correct (see NI-4).

### [F5] §1.2: \citet{LehalleNeuman2019} cited for the myopic rule $u_t = \alpha_t/\eta$
LN2019's temporary-cost problem (their §3) has a finite horizon and terminal penalty, so their optimal rate is not the pure myopic rule; the myopic rule under temporary cost alone is elementary. Either drop the citation or attach it to the broader point (signal-adaptive trading under temporary cost) rather than the specific formula.

### [F6] Bib entry `AbiJaberNeuman2025`
Published: *Mathematical Finance* 35(4):841–866, 2025 (doi:10.1111/mafi.12465; HAL hal-03835948v2). Add volume/pages; the `note = {arXiv:2211.00447}` can stay.

---

## OPTIONAL

- **[O1]** `Wiener1949` publisher: the 1949 book was published by the Technology Press of MIT and John Wiley; "MIT Press" (founded 1962) is anachronistic. Common but easily fixed.
- **[O2]** `Krein1962`: could note the original, Uspekhi Mat. Nauk 13 (1958); the AMS Transl. (2) 22:163–288 citation as given is correct and standard.
- **[O3]** `GohbergKrein1970`: add "Translations of Mathematical Monographs, Vol. 24" for precision.
- **[O4]** Candidate additional citations found during search, none obligatory beyond B3.3: Alfonsi–Schied (infinite-dimensional Riccati characterization for completely monotone kernels, deterministic case — discussed at length in AJN's intro as the deterministic predecessor); Neuman–Voß-adjacent *Fredholm Approach to Nonlinear Propagator Models* (arXiv:2503.04323, nonlinear transient impact); Grinold, *A Dynamic Model of Portfolio Management* (JOIM 2006 — practitioner one-signal aim-type rule predating GP2013); Passerini–Vázquez (*Optimal trading with alpha predictors*, J. Investment Strategies 2016 — linear costs, so different frictions); Fouque–Jaimungal-line *Optimal Trading with Signals and Stochastic Price Impact* (arXiv:2101.10053).
- **[O5]** `WienerHopf1931`: optionally add "Phys.-Math. Klasse" to the Sitzungsberichte reference; pages 696–706 are correct.

---

## NON-ISSUES (verified against sources)

- **[NI-1] FSS Theorem 2.2 "solved coefficient-wise on the Wiener chaos."** Verified. FSS posit $\hat u_t = \bar u(t) + \int_0^t k(v,t)dW_v$ for a Gaussian Volterra signal $\xi_t = \bar\xi(t) + \int_0^t K_\xi(u,t)dW_u$ and match chaos levels 0 and 1: "Then we see that this is zero for all $t\in[0,T]$ a.s. if and only if $-K_\xi(u,t) = \int_u^T k(u,v)(G(|t-v|) - G(T-v))\,dv$ [and] $-\bar\xi(t) = \int_0^T(G(|t-v|)-G(|T-v|))\bar u(v)\,dv$" (pp. 589), yielding "Fredholm integral equations of the first kind" per $u$ fixed. The theorem number (2.2) is correct. The draft's claim that \eqref{eq:finiteT} expands to these systems is structurally consistent (FSS's martingale $M_t$ in their Theorem 2.1 FBSIE, $\xi_t + \mathbb E_t[\int_0^T G(|t-v|)u_v dv] = M_t$, is exactly the draft's process-valued multiplier for $X_T=0$); the expansion itself is the draft's own derivation, not checkable against FSS beyond this consistency.
- **[NI-2] FSS $G_T = TT^*$ factor is left-anchored; pp. 590–591; used to invert in full.** Verified. FSS (from Porter–Stirling Ex. 9.2): "$G_1$ can be decomposed as $G_1 = TT^*$, where $T$ is the Volterra-type operator … $\kappa(s,t) = c_\nu (t/s)^{(1-\gamma)/2}(t-s)^{-\frac12(1+\gamma)}$" — the weight $(t/s)^\nu$ is anchored at the origin (left endpoint), the exponent $-\frac12(1+\gamma) = \nu - 1$ matches the draft's kernel, and they use it for full inversion: "$TT^*g_1 = h_1$ … has solution $g_1 = T^{*-1}(T^{-1}h_1)$", with no projection between factors. The page range 590–591 is correct (the bullet spans both pages). The reflection relation ($R\,C_+R = T^*$, hence $R(C_-C_+)R = TT^*$) is as the draft states.
- **[NI-3] GSS 2012 Ex. 2.30 attribution for $u^*(t)\propto[t(T-t)]^{(\beta-1)/2}$.** Corroborated by FSS's own two citations: "from Example 2.30 in Gatheral et al. (2012), we know that $G_1^{-1}(1)(s) = c_\gamma (s(1-s))^{-\frac12(1-\gamma)}$" and "$u_0(t) = c_1 (t(T-t))^{-\frac12(1-\gamma)}$ … (see Example 2.30 in Gatheral et al. 2012, Curato et al. 2017)". With $\gamma_{\rm FSS} = \beta$, the exponent $-\frac12(1-\gamma) = (\beta-1)/2$. (The markdown extraction drops the fraction bars; the U-shape fixes the sign.)
- **[NI-4] Gârleanu–Pedersen 2013/2016 split.** No misattribution. GP2013 (J. Finance 68:2309–2340, doi:10.1111/jofi.12080) is discrete-time ("trade partially towards the current aim"); GP2016 (JET 165:487–516) is the continuous-time model ("We show how portfolio choice can be modeled in continuous time with transitory and persistent transaction costs…", "extending the findings of Gârleanu and Pedersen (2013) to continuous time"). The specific rate/aim formulas match GP2016 Prop. 1(iv) at $\rho=0$ (see F4 for the discount-rate qualifier).
- **[NI-5] Neuman–Voß mechanism description.** Verified: FOC is "a coupled system of linear forward backward stochastic differential equations" in $(X, Y, u, Z)$ (their Lemma 5.2, four equations), solved via the matrix exponential $S(t) = e^{Lt}$ of a $4\times4$ matrix (their (3.1)–(3.2)), with optimal rate "in linear feedback form" affine-linear in inventory $X$ and impact state $Y$ (Theorem 3.2). "Temporary cost with exponential-resilience transient impact on a finite horizon" is accurate. Only the parenthetical in B2 is wrong.
- **[NI-6] Wiener–Hopf history.** All checked: WH1931 *Über eine Klasse singulärer Integralgleichungen*, Sitzungsber. Preuss. Akad. Wiss. Berlin, 696–706 (half-line convolution equations — correct as "originally for convolution equations on a half-line"); Krein, AMS Transl. (2) 22:163–288 (1962); Noble 1958 Pergamon title exact; Wiener 1949 for spectral-factor prediction/innovations and Whittle 1963 for prediction-and-regulation — standard and correctly characterized; Arveson 1975, *Interpolation problems in nest algebras*, JFA 20:208–233 (venue/pages verified against the journal scan) — the paper does contain nest-algebra factorization results, so citing it as "the abstract setting" is fine once B1's universal quantifier is fixed.
- **[NI-7] Remaining bibliography.** Verified correct: Markowitz 1952 (JF 7:77–91); Merton 1971 (JET 3:373–413); Almgren–Chriss 2001 (J. Risk 3:5–39; note FSS's own reference list misprints 5–50, the draft is right); Obizhaeva–Wang 2013 (JFM 16:1–32); BGPW 2004 (QF 4:176–190); Gatheral 2010 (QF 10:749–759); LFM 2003 (Nature 421:129–130 — biblio data correct, citation-fit issue is F3); Jusselin–Rosenbaum 2020 (Math. Fin. 30:1309–1336); GSS 2012 (Math. Fin. 22:445–474); Lehalle–Neuman 2019 (Finance Stoch. 23(2):275–311, per Springer); Neuman–Voß 2022 (SIAM J. Fin. Math. 13(2):551–575, per researchr/DOI 10.1137/20M1375486); Bank–Soner–Voß 2017 (MAFE 11(2):215–239, per FSS refs); FSS 2022 (QF 22(3):585–596, per the extraction header); Samko–Kilbas–Marichev 1993; Lions–Magenes 1972; Chakrabarti–George 1994 (Appl. Math. Lett. 7(2):87–90, title exact per FSS refs).
- **[NI-8] FSS scope descriptor in §1.4** ("power-law resilience with Gaussian signals on a finite horizon") is accurate; FSS have zero temporary impact in the main theorem (temporary added in their §3.2 as a second-kind Fredholm equation) and explicitly defer inventory penalties: "One can in principle add additional penalty terms … but our optimal solution is already rather complicated to compute, so we leave the details of this for future works."

---

## Questions for Authors

- **[Q1]** For \eqref{eq:gk-kernel}: what computation verifies "$C_-C_+ = G_T$ exactly, including the constant"? The FSS/Porter–Stirling constant $c_\nu$ and the draft's $(\gamma c_\beta)^{1/2}/\Gamma(\nu)$ normalization should be reconciled explicitly (an appendix line or a script reference would suffice).
- **[Q2]** Does the two-EMA filter \eqref{eq:nv-filter} arise as the $T\to\infty$, $\varrho\to0$ limit of NV's $v_i(T-t)$ coefficients (eigenvalues of their $4\times4$ matrix $L$ vs. the roots $b_1,b_2,\kappa$)? If yes, one paragraph would convert B2's "stationary analogue" caveat into a genuine recovery statement.
- **[Q3]** Abi Jaber–Neuman's admissible power-law range is $0<\beta<1/2$; the draft's covers empirical $\beta\in(0.2,0.6)$. If the draft's whole-line theory covers $\beta\in(0,1)$, that is a concrete point of superiority worth stating in §1.4 instead of the "fixed point" contrast.

## Verdict

The FSS-facing claims (§7) are accurate in every detail checked against the full text, and the GP attribution is correct including the discrete/continuous split. Revision risk is concentrated in three places: one mathematically false attribution (B1, straightforward to repair by scoping), one false description of a prior paper's objective (B2, one-line fix), and a novelty paragraph whose two differentiators are contestable against AJN 2025 / GP2016 / AJN-Tuschmann (B3, requires rewriting the positioning sentence and one added citation). None threatens the paper's core results; all three would draw fire from referees who know this literature (Neuman, Abi Jaber, and Schied groups are the obvious reviewer pool). Confidence: high on B1–B3 and F1–F6 (each verified against primary text or published reviews); moderate on the completeness of the missed-prior-work search.

## Revision Plan

1. **B1:** Rescope the §7 factorization claim to $\eta I + K$ / explicitly-exhibited factors; cite Gohberg–Krein for the $I+K$ theory and (optionally) Larson 1985 for why the restriction is needed.
2. **B2:** Rewrite the NV parenthetical; decide between proving the $T\to\infty$ limit (Q2) or consistently saying "stationary analogue" in abstract and §5.3.
3. **B3:** Rewrite the §1.4 novelty sentence around the actual differentiators (whole-line stationarity, transfer-function closed forms, filter/contrarian structure, kernel generality per Q3); add GP2016 Prop. 2 to §5.3's credit line; cite arXiv:2403.10273 or fix the "stochastic Fredholm" descriptor for 2211.00447.
4. **F1–F5:** Apply the wording fixes (C–G inversion target, Almgren–Chriss/exponential-kernel sentence, LFM citation, GP zero-discount qualifier, LN myopic-rule cite).
5. **F6, O1–O3:** Bib data updates.

---

## Inline Annotations

> "every strictly positive $G_T$ (the cost operator restricted to $[0,T]$) factors as $G_T = C_-C_+$ with $C_+$ a causal Volterra operator and $C_- = C_+^*$" (§7, citing Gohberg–Krein 1970, Arveson 1975)

**[B1] BLOCKER:** False for the continuous chain $\{P_{[0,t]}\}$. Larson (Ann. Math. 121, 1985, 409–427): a complete nest is countable iff every positive invertible operator factors as $A^*A$ with $A, A^{-1}$ in the nest algebra. Gohberg–Krein's factorization theorems require $I+K$ form with regularity on $K$. Restrict the statement to the operators actually used.

> "The stationary counterpart (terminal penalty replaced by running inventory risk) is explicit." (§5.3)

**[B2] BLOCKER:** NV's objective (2.6) already contains $-\phi\int_0^T (X_t^u)^2\,dt$: "a penalty $\phi>0$ and $\varrho>0$ on her running and terminal inventory, respectively" (arXiv:2002.09549v3, §2). The stationary problem drops the terminal penalty and the horizon, not adds inventory risk.

> "the adapted optimum here is closed-form rather than characterized as a fixed point, covers the three frictions jointly, and exposes the filter structure that practitioners implement." (§1.4)

**[B3] BLOCKER:** Abi Jaber–Neuman 2025 cover temporary + general propagator (incl. power-law) + running and terminal inventory penalties with signals, and state the problem "can be solved explicitly … $u^*_t = a_t + \int_0^t B(t,s)u^*_s\,ds$" with $a, B$ explicit; GP2016 Prop. 2 solves the exponential three-friction case in feedback form. "Covers the three frictions jointly" is not a differentiator, and "characterized as a fixed point" undersells solutions their authors call explicit. Replace with the stationary/whole-line/transfer-function differentiators.

> "general propagators via stochastic Fredholm equations \citep{AbiJaberNeuman2025}" (§1.4)

**[B3] (cont.):** 2211.00447's method is an operator-valued Riccati equation plus an $L^2$-valued free-boundary BSDE; "stochastic Fredholm equations" is the stated method of the uncited Abi Jaber–Neuman–Tuschmann cross-impact paper (arXiv:2403.10273: "We solve the maximization problem explicitly in terms of operator resolvents, by reducing the problem to … stochastic Fredholm equations"). Cite the latter or re-describe the former.

> "with the Abel-type inversions of \citet{ChakrabartiGeorge1994} implementing $C_\pm^{-1}$." (§7)

**[F1] FIX:** C–G's formula (their (3.14a)–(3.14b), as used by FSS) inverts the full two-sided Abel operator $G_T$, not the one-sided factors; FSS invert the factors via $T = B^{-1}I_\nu B$ and Riemann–Liouville derivatives (p. 591). Also consider crediting Porter–Stirling (1990, Ex. 9.2) for the $TT^*$ decomposition FSS use.

> "the exponential kernel $G(t)=e^{-\kappa|t|}$ underlies the resilience models of \citet{ObizhaevaWang2013} and the Almgren–Chriss line \citep{AlmgrenChriss2001}." (§1.1)

**[F2] FIX:** Almgren–Chriss has temporary + permanent impact and no propagator; it is recovered from the exponential kernel only in the $\kappa\to\infty$/$\kappa\to0$ limits.

> "Empirical propagators decay as power laws $G(t) = |t|^{-\beta}$ with $\beta\in(0.2,0.6)$ across markets \citep{LilloFarmerMantegna2003,BouchaudGefenPottersWyart2004,JusselinRosenbaum2020}" (§1.1)

**[F3] FIX:** LFM 2003 is the impact-vs-volume master curve, not temporal propagator decay. Rest the decay range on BGPW 2004 (plus, e.g., Brokmann et al. 2015 or Bouchaud et al. 2018); JR 2020 is theoretical support.

> "trade at speed $\sqrt{\lambda/\eta}$ toward an aim that discounts the Markowitz position by the persistence factor $a/(a+\theta)$. This is the continuous-time solution of \citet{GarleanuPedersen2016}" (§5.2)

**[F4] FIX (minor):** Verified against GP2016 Prop. 1(iv) — $\bar M^{\rm rate} = \frac12(\sqrt{\rho^2+4\gamma/\lambda}-\rho)$, aim $=\gamma^{-1}\Sigma^{-1}B(I + a/\gamma\,\Phi)^{-1}$, which reduces to the draft's formulas exactly at $\rho=0$. Add "(zero discount)". The 2013 = discrete / 2016 = continuous attribution is correct.

> "the adapted optimum is the myopic rule $u_t = \alpha_t/\eta$ — conditional expectation passes through a pointwise equation at no cost \citep{LehalleNeuman2019}." (§1.2)

**[F5] FIX (minor):** LN2019 §3 has a terminal penalty and finite horizon, so their formula is not the bare myopic rule; either drop the cite or attach it to the general temporary-cost signal problem.

> "the stochastic Fredholm equation that \citet{FordeSanchezSmith2022} solve coefficient-wise on the Wiener chaos for Gaussian Volterra signals (their Theorem 2.2)" (§7)

**[NI-1] VERIFIED:** matches FSS's derivation (chaos levels 0 and 1 matched termwise; family of first-kind Fredholm equations; Theorem number correct).

> "The time reflection of \eqref{eq:gk-kernel} is the left-anchored outer factor $G_T = TT^*$ used by \citet[pp.~590--591]{FordeSanchezSmith2022} to invert $G_T$ \emph{in full}, where factor order is immaterial" (§7)

**[NI-2] VERIFIED:** FSS kernel $\kappa(s,t) = c_\nu(t/s)^{(1-\gamma)/2}(t-s)^{-(1+\gamma)/2}$ is origin-anchored; they compute $g_1 = T^{*-1}(T^{-1}h_1)$ with no intervening projection; page range correct.

> "the U-shaped profile $u^\star(t) \propto [t(T-t)]^{(\beta-1)/2}$ of \citet[Ex.~2.30]{GatheralSchiedSlynko2012}" (§7)

**[NI-3] VERIFIED** via FSS's citations of the same example and formula ($\gamma_{\rm FSS}=\beta$).

> "characterizing the optimum through four coupled linear FBSDEs solved by matrix exponentials, in feedback form on the inventory and the impact state" (§5.3)

**[NI-5] VERIFIED** against NV Lemma 5.2 (system in $X, Y, u, Z$), eq. (3.2) ($S(t)=e^{Lt}$), and Theorem 3.2 (feedback affine-linear in $X$ and $Y$).

> "verified by direct kernel integration ($C_-C_+ = G_T$ exactly, including the constant)" (§7)

**[Q1]:** show or reference the computation; the constant convention differs from FSS/Porter–Stirling's $c_\nu$, and a skeptical reader will want the reconciliation.

---

## Sources

- FSS 2022 full text extraction: `/Users/orwell/Downloads/1469768820211950919.md` (from https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197)
- Gârleanu–Pedersen 2016 (working-paper version with identical propositions): https://nbgarleanu.github.io/DynamicPortfolioChoiceWithFrictions.pdf ; published record: https://doi.org/10.1016/j.jet.2016.06.001 (JET 165:487–516)
- Gârleanu–Pedersen 2013: https://doi.org/10.1111/jofi.12080
- Neuman–Voß 2022: https://arxiv.org/abs/2002.09549 (v3 full text); https://doi.org/10.1137/20m1375486 ; pages 551–575 per https://researchr.org/publication/NeumanV22
- Abi Jaber–Neuman 2025: https://arxiv.org/html/2211.00447v2 (full text); https://doi.org/10.1111/mafi.12465 ; Math. Finance 35(4):841–866 per https://hal.science/hal-03835948v2
- Abi Jaber–Neuman–Tuschmann, cross-impact propagators: https://arxiv.org/abs/2403.10273
- Larson 1985: https://doi.org/10.2307/1971180 ; countability-iff-factorization statement per https://portal.mardi4nfdi.de/wiki/Item:Q1084648 ; see also https://doi.org/10.1090/s0002-9939-97-03430-8 (Factorisation in nest algebras, Proc. AMS 1997)
- Arveson 1975 journal scan (JFA 20:208–233): https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-arveson/1970s/1975_Interpolation_problems_in_nest_algebras.pdf
- Lehalle–Neuman 2019 (Finance Stoch. 23:275–311): https://link.springer.com/article/10.1007/s00780-019-00382-7
- Passerini–Vázquez: https://arxiv.org/abs/1501.03756 ; Grinold 2006: https://joim.com/wp-content/uploads/emember/downloads/richard_grinold.pdf ; nonlinear Fredholm propagators: https://arxiv.org/pdf/2503.04323 ; Fouque–Jaimungal-line signals + stochastic impact: https://doi.org/10.48550/arxiv.2101.10053
- Missed-prior-work search queries run (no prior Wiener–Hopf execution treatment found): "optimal trading signal transaction costs Wiener-Hopf OR spectral factorization filter", "infinite horizon stationary optimal trading transient price impact propagator signal explicit filter", "optimal execution fractional derivative trading rate power-law propagator signal".
