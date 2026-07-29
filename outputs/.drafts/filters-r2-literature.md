# Round-2 Literature-Accuracy Verification — Optimal Trading Filters

**Scope:** Verify the Round-1 literature fixes only, in `tex/optimal-trading-filters.tex` / `.bib`. Read-only. Sources: FSS full text (`/Users/orwell/Downloads/1469768820211950919.md`), primary papers, and DOIs/arXiv below.

**Bottom line:** 6 of 7 checked fixes are now correct. One remaining false attribution (Larson 1985) and one method mislabel (operator-resolvent → Abi Jaber–Neuman 2025) still need correction.

---

## BLOCKERS (remaining/new false claims)

### B1 — §7 Larson 1985 does not support the factorization claim (false attribution)
Draft text (§7):
> "the cost operator restricted to $[0,T]$, written $G_T$, factors as $G_T = C_-C_+$ with $C_+$ a causal Volterra operator and $C_- = C_+^*$; unconditional factorization along a continuous chain requires such structure \citep{Larson1985}."

The claim is a **factorization** statement (not every positive operator factors along a continuous nest; structure such as $\eta I$ + nice operator is needed). Larson 1985 is about **similarity of nests**, not factorization. Its own abstract:
> "We use this to provide the following answer to a question posed by J. R. Ringrose … : Similar continuous nests on separable Hilbert space can fail to be unitarily equivalent (Theorem 2.2)." (Ann. Math. 121 (1985) 409–427, DOI 10.2307/1971180)

The paper answers Ringrose's *similarity* question via quasitriangularity; it contains no "factorization-requires-structure" or "countable-nest-iff-factorization" theorem. The task's framing ("countable-nest-iff-factorization") is a **different** result — that is the 2004 paper *Nests with the partial factorization property* (Proc. AMS, DOI 10.1090/s0002-9939-04-07446-5): "a nest N has the left (resp. right) partial factorization property … if and only if it is atomic (resp. countable)." Larson 1985 is not that source.

**Severity:** Blocker (cited source does not support the exact claim).
**Fix:** Cite the sources the paper already carries — `GohbergKrein1970` (triangular factorization of $I+$ Volterra with continuous/HS kernel) and/or `Arveson1975` — and, for the negative side (general positive operators fail to factor along a continuous chain), the concrete non-factorable-operator result (e.g. Kheifets, *Effective construction of a class of positive operators … which do not admit triangular factorization*, J. Funct. Anal. 2010) or the 2004 partial-factorization-property theorem. Remove or repurpose `Larson1985`.
**Source:** https://doi.org/10.2307/1971180 ; https://doi.org/10.1090/s0002-9939-04-07446-5 ; https://www.sciencedirect.com/science/article/pii/S0022123610004453

---

## FIXES STILL NEEDED

### F1 — §1.4 "operator-resolvent" wrongly attached to Abi Jaber–Neuman 2025
Draft text (§1.4):
> "general propagators through operator-resolvent and stochastic-Fredholm methods \citep{AbiJaberNeuman2025,AbiJaberNeumanTuschmann2024}"

Checked against the two abstracts:
- **AbiJaberNeuman2025** (arXiv:2211.00447): "By using an infinite dimensional stochastic control approach, we characterize the value function in terms of a solution to a free-boundary $L^2$-valued backward stochastic differential equation and an **operator-valued Riccati equation**." → its method is infinite-dimensional stochastic control + operator **Riccati** + BSDE. It does **not** use "operator resolvent" or "stochastic Fredholm."
- **AbiJaberNeumanTuschmann2024** (arXiv:2403.10273): "We solve the maximization problem explicitly **in terms of operator resolvents**, by reducing the corresponding first order condition to a coupled system of **stochastic Fredholm equations of the second kind**." → **both** "operator resolvent" and "stochastic Fredholm" describe the Tuschmann paper.

So "stochastic-Fredholm → Tuschmann" is correct, but "operator-resolvent → AbiJaberNeuman2025" is a mischaracterization: operator-resolvent is Tuschmann's language, and AJN2025's distinctive method (operator Riccati / infinite-dim stochastic control) is not represented.

**Severity:** Major (method misattribution in the novelty paragraph).
**Fix:** e.g. "general propagators through infinite-dimensional stochastic-control and operator-Riccati methods \citep{AbiJaberNeuman2025} and operator-resolvent / stochastic-Fredholm methods \citep{AbiJaberNeumanTuschmann2024}." Any wording that stops attaching "operator-resolvent" specifically to AJN2025 resolves it.
**Source:** https://arxiv.org/abs/2211.00447 ; https://arxiv.org/abs/2403.10273

---

## NON-ISSUES (verified correct)

### N1 — §5.3 NV parenthetical "(infinite horizon, terminal penalty dropped)" is CORRECT
Neuman–Voß (2022) objective, eq. (2.6), verbatim:
> $J(u) = \E[\int_0^T (P_t-\kappa Y^u_t)u_t\,dt - \lambda\int_0^T u_t^2\,dt + X^u_T P_T - \varphi\int_0^T (X^u_t)^2\,dt - \varrho(X^u_T)^2]$
> "The fourth and fifth terms … implement a penalty $\varphi>0$ and $\varrho>0$ on her running and terminal inventory, respectively."

NV's objective **already contains a running inventory-risk term** $\varphi\int_0^T(X^u_t)^2dt$ (maps to the paper's $\lambda$ inventory penalty), plus temporary ($\lambda_{\rm NV}\!\int u^2$ → paper's $\eta$), transient (Obizhaeva–Wang exponential $\kappa,\gamma,\rho$), on a **finite** horizon with a **terminal** penalty $\varrho(X^u_T)^2$. So the paper's whole-line stationary three-friction problem is obtained from NV by (i) infinite horizon and (ii) dropping the terminal penalty — exactly what the reworded parenthetical states. The Round-1 fix is accurate. Also confirmed: NV solves via four coupled linear FBSDEs (eq. 5.3) by matrix exponentials ($S(t)=e^{Lt}$), feedback form affine in inventory $X$ and impact state $Y$ (Thm 3.2, eq. 3.6) — matching the draft's description.
**Source:** NV2022, https://spiral.imperial.ac.uk/server/api/core/bitstreams/97680184-89df-4ebe-a908-5576f5593d49/content (eqs. 2.6, 3.6, 5.3); DOI 10.1137/20m1375486

### N2 — §5.3 Gârleanu–Pedersen 2016 Prop. 2 (three-friction exponential, feedback form) is CORRECT
GP2016 §1.2 "Temporary and Persistent Transaction Costs," objective (16):
> $\max \E_t\int_t^\infty e^{-\rho(s-t)}\big(x_s^\top(Bf_s-(r_f+R)D_s+C\tau_s) - \tfrac{\gamma}{2}x_s^\top\Sigma x_s - \tfrac12\tau_s^\top\Lambda\tau_s\big)ds$

with $dD_t=-RD_t\,dt+C\,dx_t$ (exponential resilience $R$). This is three frictions: temporary ($\Lambda$), transient/persistent with exponential decay ($D$, resilience $R$), inventory risk ($\tfrac{\gamma}{2}x^\top\Sigma x$). **Proposition 2**, eq. (18):
> $\tau_t = \bar M_{\rm rate}\big(\bar M^{\rm aim}_f(f_t) + \bar M^{\rm aim}_D D_t - x_t\big)$

is the infinite-horizon feedback (aim-portfolio) solution. Prop. 1 is temporary-only (two-friction), Prop. 3 is purely persistent — so Prop. **2** is the correct pointer for the three-friction exponential case in feedback form.
**Source:** GP2016, https://nbgarleanu.github.io/DynamicPortfolioChoiceWithFrictions.pdf (eqs. 16, 18); DOI 10.1016/j.jet.2016.06.001

### N3 — §1.1 exponential-kernel Almgren–Chriss recovery is CORRECT
"$G(t)=e^{-\kappa|t|}$ … recovers the temporary and permanent costs of Almgren–Chriss in its fast- and slow-decay limits." Fast decay ($\kappa\to\infty$) → kernel → $\delta$, instantaneous (temporary) impact; slow decay ($\kappa\to 0$) → kernel → constant, permanent impact. Standard Obizhaeva–Wang resilience interpolation. Accurate.

### N4 — §1.1 propagator-decay citation (BGPW2004 + JusselinRosenbaum2020; LFM2003 dropped) is CORRECT
BGPW2004 (Quant. Finance 4:176–190, DOI 10.1080/14697680400000022) is the founding propagator paper — price as impact of all past trades via a power-law-decaying propagator. JusselinRosenbaum2020 (Math. Finance 30:1309–1336) derives power-law impact from no-arbitrage. Both support power-law temporal decay of the propagator; $\beta\in(0.2,0.6)$ "across markets" is a defensible spread. **Dropping LFM2003 is a genuine improvement**: Lillo–Farmer–Mantegna 2003 (Nature) is a *master curve for the price-impact function* (impact vs. order size / concavity), not the *temporal* decay exponent $\beta$ of the propagator kernel; it did not belong on this specific claim.
**Source:** https://doi.org/10.1080/14697680400000022

### N5 — §7 Chakrabarti–George / weighted Riemann–Liouville wording MATCHES FSS
Draft (§7): "the generalized Abel inversion of \citet{ChakrabartiGeorge1994} implementing the full inverse $G_T^{-1}$ and weighted Riemann–Liouville operators implementing the individual factors."
FSS confirms both halves:
- Full inverse: FSS solves $G_1 g_1 = h_1$ (the whole operator) "more explicitly from Chakrabarti and George (1994) … the explicit solution is given in equations (3.14a) and (3.14b)"; "$G_1^{-1}(f)$ for a general function $f$ has an explicit form." → Chakrabarti–George gives the **full inverse** $G_1^{-1}$ (≡ rescaled $G_T^{-1}$).
- Individual factors: FSS decomposes $G_1 = TT^*$ with $T = B^{-1} I_\nu B$, $B$ = multiplication by $t^{-(1-\nu)/2}$ (a weight), $I_\nu$ = Riemann–Liouville operator. → the factors are **weighted Riemann–Liouville operators**.
The draft's distinction is faithful. (The adjacent claim that FSS's left-anchored $G_T=\mathcal T\mathcal T^*$ appears on pp. 590–591 also checks out — the "Decomposing $G_1$" derivation is there.)
**Source:** FSS full text pp. 590–591 (`/Users/orwell/Downloads/1469768820211950919.md`); DOI 10.1080/14697688.2021.1950919

### N6 — Changed/new bib entries are all bibliographically correct
- `AbiJaberNeuman2025` — *Mathematical Finance* **35**(4):841–866, 2025; arXiv:2211.00447. Confirmed by HAL (hal-03835948v2: "Mathematical Finance, 2025, 35 (4), pp.841-866") and MaRDI (published 30 Sept 2025), DOI 10.1111/mafi.12465. ✓
- `AbiJaberNeumanTuschmann2024` — *Optimal Portfolio Choice with Cross-Impact Propagators*, arXiv:2403.10273, 2024. Confirmed (submitted 15 Mar 2024; authors Abi Jaber, Neuman, Tuschmann). ✓ (Note: now also published in Math. Finance, DOI 10.1111/mafi.70025, 2025 — optional to update; citing the 2024 arXiv preprint is not an error.)
- `Larson1985` — Ann. Math. **121**:409–427, 1985. Bibliographically correct (Ann. of Math. (2) 121 (1985), no. 3, 409–427; MR794368; DOI 10.2307/1971180). The *entry* is fine; only the *use* is wrong (see B1).
- `Wiener1949` — publisher "Technology Press of MIT and John Wiley." Correct: the 1949 original was co-published by the Technology Press of MIT and John Wiley & Sons (Google Books: "Technology Press of the Massachusetts Institute of Technology, 1949"; the volume was distributed by Wiley). ✓
**Source:** https://hal.science/hal-03835948v2 ; https://arxiv.org/abs/2403.10273 ; https://doi.org/10.2307/1971180 ; https://books.google.com/books/about/Extrapolation_Interpolation_and_Smoothin.html?id=TGsGAQAAIAAJ

### N7 — §1.4 novelty claim itself is not an overclaim
"the present treatment addresses the three frictions jointly on the whole line in the stationary regime, in closed transfer-function form, and adds the rate-response analysis of §6." The cited execution works (GSS, LN, NV, BSV, AJN2025, Tuschmann, FSS) are finite-horizon or general-propagator but not whole-line stationary closed transfer-function; the claim is appropriately scoped. The one prior work that *does* do stationary three-friction (exponential only, feedback form), GP2016, is explicitly credited in §5.3 — so no unacknowledged prior art. The only defect in this paragraph is the method label in F1.

---

## Inline Annotations

> "general propagators through operator-resolvent and stochastic-Fredholm methods \citep{AbiJaberNeuman2025,AbiJaberNeumanTuschmann2024}"

**[F1] MAJOR:** "operator-resolvent" is the Tuschmann (2024) paper's own term ("we solve … in terms of operator resolvents, by reducing … to … stochastic Fredholm equations"). AbiJaberNeuman2025's abstract instead says its method is "infinite dimensional stochastic control … [an] operator-valued Riccati equation." Do not attach operator-resolvent to AJN2025.

> "unconditional factorization along a continuous chain requires such structure \citep{Larson1985}."

**[B1] BLOCKER:** Larson 1985 is a *similarity*-of-nests paper (answers Ringrose's question: similar continuous nests can fail to be unitarily equivalent). It contains no factorization theorem. Replace with `GohbergKrein1970`/`Arveson1975` (already in the bib) and, for the negative direction, the non-factorable-positive-operator result or the countable/partial-factorization theorem (Proc. AMS 2004).

> "(infinite horizon, terminal penalty dropped)"  [§5.3, Neuman–Voß]

**[N1] VERIFIED:** NV's eq. (2.6) already carries a running inventory penalty $\varphi\int_0^T (X^u_t)^2 dt$ and a terminal penalty $\varrho(X^u_T)^2$; the stationary three-friction problem = NV with $T\to\infty$ and $\varrho\to0$. Parenthetical is accurate.

> "for the exponential kernel the three-friction problem is also solved in feedback form by \citet[Prop.~2]{GarleanuPedersen2016}"

**[N2] VERIFIED:** GP2016 Prop. 2 (eq. 18) gives the aim-portfolio feedback solution for temporary + exponential-resilience persistent impact + quadratic risk, infinite horizon. Correct proposition number.

---

## Sources
- Abi Jaber–Neuman 2025 (general propagator): https://arxiv.org/abs/2211.00447 ; https://hal.science/hal-03835948v2 ; DOI 10.1111/mafi.12465
- Abi Jaber–Neuman–Tuschmann 2024 (cross-impact): https://arxiv.org/abs/2403.10273 ; DOI 10.1111/mafi.70025
- Neuman–Voß 2022: https://spiral.imperial.ac.uk/server/api/core/bitstreams/97680184-89df-4ebe-a908-5576f5593d49/content ; DOI 10.1137/20m1375486
- Gârleanu–Pedersen 2016: https://nbgarleanu.github.io/DynamicPortfolioChoiceWithFrictions.pdf ; DOI 10.1016/j.jet.2016.06.001
- Forde–Sánchez-Betancourt–Smith 2022 (FSS): local full text `/Users/orwell/Downloads/1469768820211950919.md` ; DOI 10.1080/14697688.2021.1950919
- BGPW 2004: https://doi.org/10.1080/14697680400000022
- Larson 1985: https://doi.org/10.2307/1971180
- Nests with the partial factorization property (2004): https://doi.org/10.1090/s0002-9939-04-07446-5
- Non-factorable positive operators (J. Funct. Anal. 2010): https://www.sciencedirect.com/science/article/pii/S0022123610004453
- Wiener 1949: https://books.google.com/books/about/Extrapolation_Interpolation_and_Smoothin.html?id=TGsGAQAAIAAJ
