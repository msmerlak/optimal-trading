# Mathematical Correctness Review: *Closed-Form Optimal Trading Against a Signal via Factorization of the Impact Cost Operator*

**Artifact.** `tex/factorization-optimal-trading.tex` (385 lines LaTeX, 14 pp PDF).

**Scope.** Mathematical correctness only. Every theorem, lemma, corollary, proposition, and intermediate derivation was re-derived from first principles.

---

## Summary Assessment

**Mathematics is essentially correct.** The core theoretical apparatus — the projected-inverse identity (Lemma 1), the closed-form Theorem 1, the fractional-derivative bulk formula (Cor 1), the boundary-deformed formula (Cor 2), the interior asymptotic (Prop 3), and the OU-signal reductions — is sound. All main theorem statements and final results hold as stated.

Two localized errors were found in intermediate expressions:

- **E1 (minor)**: an incorrect constant in one line of the appendix proof of Prop 3. The stated Marchaud tail bound has $\nu^{-1}$ where it should have $\Gamma(1-\nu)^{-1}$. Because Prop 3's statement uses a generic constant $C_1(\beta)$, the proposition itself is unaffected — only the arithmetic in the intermediate bound is wrong.

- **E2 (minor)**: an inconsistent intermediate expression in the §5.1 OU-signal step. Eq (exp-bulk) uses convention where $\zeta$ carries no square-root factor, but the next line evaluates $\zeta = (2\kappa)^{-1/2}(\kappa+\theta)\alpha$ with an extra $(2\kappa)^{-1/2}$. The stated final eq (exp-ou) and the sign-flip conclusion are correct; only the intermediate substitution is inconsistent with the convention it purports to use.

Neither error propagates to a main-theorem-level claim. Both are one-line fixes.

**Overall grade for mathematical correctness: A-.** No structural or foundational problems. Two typo-level intermediate-step errors that should be fixed for pedagogical honesty and to prevent puzzled readers.

---

## Strengths

- **Adapted FOC derivation is clean.** Gâteaux derivative + tower + $\alpha$-adaptedness give $\gamma\E_t[(Cu^\star)(t)] = \alpha_t$ with no fudging. Operator form $\gamma P_+ CP_+ u^\star = \alpha$ follows unambiguously.
- **Lemma 1 proof is compact and correct.** The two commutation identities $P_+^\perp C_+ P_+ = 0$ and $P_+ C_- P_+^\perp = 0$ are stated, then combined via a decomposition-and-cancellation argument. Splitting $C_-^{-1}u = P_+ C_-^{-1}u + P_+^\perp C_-^{-1}u$ and using that $C_-$ preserves $L^2_{\adap}^\perp$ closes the composition cleanly. All algebra re-checked.
- **eq (proj-cma)** commutation of $P_+$ with the deterministic anticausal operator on the argument variable is correctly cited (Hytönen et al. Prop 2.6.13) and correctly applied.
- **Theorem 1** = Lemma 1 + FOC. Follows directly.
- **Cor 1 (power-law bulk formula)** is a clean substitution of Marchaud fractional integrals. The distribution of the constant $c_\beta^{-1}$ between prefactor and $\zeta$-definition is internally consistent (both $c_\beta^{-1/2}$ factors absorbed into the outer prefactor; $\zeta$ carries no factor). This is a stylistic choice with no mathematical content.
- **OU signal reduction** correctly computes $(D_-^\nu\bar\alpha(t,\cdot))(t) = \theta^\nu\alpha_t$ via the elementary integral $\int_0^\infty(1-e^{-u})u^{-1-\nu}du = \Gamma(1-\nu)/\nu$. The $\nu\Gamma(1-\nu)^{-1}$ prefactor of Marchaud is cancelled cleanly, giving the clean scaling $\theta^\nu$. Independently re-derived.
- **Cor 2 (boundary-deformed formula)** is a valid inversion of the weight-conjugated Gohberg–Krein factors. $T^{-1} = c_\beta^{-1/2}B^{-1}D_+^\nu B$ follows from $(B^{-1}I_+^\nu B)^{-1} = B^{-1}D_+^\nu B$; composition gives the paper's expression.
- **Prop 3 (interior error) statement** is correctly framed with generic constants; the $d(t)^{-\nu}$ and $T^{-\nu}d(t)^{-\nu}$ scalings are dimensionally right and the KKT eigenfunction $\phi_1$ correctly bounded by $d(t)^{-\nu}(T/2)^{-\nu}$ in the interior.
- **Exponential factors** in §5.1 correctly reduce to first-order differential operators.
- **eq (exp-ou)** and the sign-flip statement at $\theta = \kappa$ hold when derived directly from Theorem 1 (independent of the intermediate typo E2 below).
- **§6 joint gain–risk–cost outlook** is technically sound: the position penalty gives Fourier symbol $\lambda\Sigma/\xi^2$, positivity and log-integrability of the joint symbol $\gamma\hat C + \lambda\Sigma/\xi^2$ both hold, so Prop 1 and Lemma 1 apply.
- **Log-integrability check for pure power-law**: correctly satisfied. This is what earlier flagged and led to the boundedness caveat added to §4 — the caveat itself is mathematically correct.
- **Standing-hypothesis / OU boundary at $\beta = 1/2$**: correctly derived. The paper's claim that OU satisfies the standing hypothesis only for $\beta > 1/2$ is verified by direct spectral computation.

## Critical Issues

None. No error rises to a level that undermines the main theorems or breaks a corollary as stated.

## Major Issues

None. Both errors identified are minor intermediate-step typos.

## Minor Issues

### E1. Marchaud tail-bound constant in App Prop 3 proof (line 373)

The paper states
$$|(D_-^\nu f)(s) - (D_-^{\nu,[0,T]}f)(s)| \le \frac{2\|f\|_\infty}{\nu}(T-s)^{-\nu}.$$
Correct derivation:
$$\text{tail} = \frac{\nu}{\Gamma(1-\nu)}\int_{T-s}^\infty \frac{f(s)-f(s+r)}{r^{1+\nu}}\,dr,$$
$$|\text{tail}| \le \frac{\nu}{\Gamma(1-\nu)}\cdot 2\|f\|_\infty\cdot\int_{T-s}^\infty r^{-1-\nu}\,dr = \frac{\nu}{\Gamma(1-\nu)}\cdot 2\|f\|_\infty\cdot\frac{(T-s)^{-\nu}}{\nu} = \frac{2\|f\|_\infty}{\Gamma(1-\nu)}(T-s)^{-\nu}.$$

The $\nu$ from the integration cancels the Marchaud prefactor $\nu$, leaving $\Gamma(1-\nu)^{-1}$, not $\nu^{-1}$.

**Fix.** Replace `\tfrac{2\|f\|_\infty}{\nu}` with `\tfrac{2\|f\|_\infty}{\Gamma(1-\nu)}` on line 373.

**Impact.** None on the proposition statement (which uses generic $C_1(\beta)$). Fixes an internal arithmetic slip.

### E2. §5.1 intermediate OU step is inconsistent with eq (exp-bulk) convention (line 310)

Eq (exp-bulk) uses the convention:
$$\zeta_s := (\kappa-\partial_r)\bar\alpha(s,r)|_{r=s^+}, \qquad u^{exp}_t := \frac{1}{2\kappa\gamma}(\kappa+\partial_t)\zeta_t.$$
That is, both $(2\kappa)^{-1/2}$ factors from $C_\pm^{-1} = (2\kappa)^{-1/2}(\kappa\pm\partial_t)$ are absorbed into the outer $(2\kappa\gamma)^{-1}$ prefactor; the bare $\zeta$ carries no square-root factor. (This mirrors the convention in Cor 1 for the power-law case.)

The next line (line 310) then writes:
> "For OU $\alpha$ with mean reversion $\theta$: $\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$"

The $(2\kappa)^{-1/2}$ factor is extraneous under the convention just declared. Direct evaluation:
$$\zeta_s = (\kappa - \partial_r)\bar\alpha(s,r)|_{r=s^+} = (\kappa - \partial_r)[\alpha_s e^{-\theta(r-s)}]|_{r=s^+} = \kappa\alpha_s - (-\theta\alpha_s) = (\kappa+\theta)\alpha_s.$$

**Fix.** Replace line 310 with: "For OU $\alpha$ with mean reversion $\theta$: $\zeta_s = (\kappa+\theta)\alpha_s$".

**Impact.** The final eq (exp-ou) is correct as stated. Substituting the correct intermediate $\zeta_s = (\kappa+\theta)\alpha_s$ into eq (exp-bulk):
$$u^{exp}_t = \frac{1}{2\kappa\gamma}(\kappa+\partial_t)(\kappa+\theta)\alpha_t = \frac{\kappa+\theta}{2\kappa\gamma}(\kappa+\partial_t)\alpha_t = \frac{\kappa+\theta}{2\kappa\gamma}\bigl[(\kappa-\theta)\alpha_t + \sigma\dot W_t\bigr].$$
Matches eq (exp-ou) exactly. Conditional expectation $\frac{\kappa^2-\theta^2}{2\kappa\gamma}\alpha_t$ and sign flip at $\theta = \kappa$ unaffected.

Substituting the paper's currently-stated intermediate $\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$ would produce $u^{exp}_t = (2\kappa)^{-1/2}$ × (the stated eq exp-ou), i.e., an off-by-$(2\kappa)^{-1/2}$ inconsistency. A reader tracing the derivation line-by-line hits a contradiction; only readers who trust the final result and skip the intermediate step are unaffected.

### m1. Signal-engineering claim in §5.5 is semi-heuristic

The claim "the tradeable value $V(\alpha) = \frac{1}{2\gamma}\E|\zeta|^2$ weights the forecast spectrum by $|\xi|^{1-\beta}$" is exactly right when $P_+$ is dropped ($\|C_-^{-1}\alpha\|^2 = \int c_\beta^{-1}|\xi|^{1-\beta}S_\alpha$), but $P_+$ complicates the exact spectral identity. The physical intuition is correct and standard for filter-theory audiences. Not an error; flagging as a slight abstraction the reader should be aware of.

## Reproducibility and Verification

Not applicable in the empirical-reproducibility sense (no experiments in the paper). Verifications performed:

- **Adapted FOC**: re-derived Gâteaux calculation. ✓
- **Lemma 1**: re-derived commutation identities and full composition check. ✓
- **eq (proj-cma)**: conditional Fubini verification. ✓
- **Value formula**: convex-Legendre + adjoint identity re-derived. ✓
- **Power-law WH factors**: symbol computation $|\xi|^{\beta-1} = (i\xi)^{-\nu}(-i\xi)^{-\nu}$ verified. ✓
- **Log-integrability of pure power-law**: verified integrable near 0 and ∞. ✓
- **Cor 1 substitution algebra**: verified. ✓
- **OU $(D_-^\nu\bar\alpha)(t) = \theta^\nu\alpha_t$**: re-derived via integration by parts of $\int_0^\infty(1-e^{-u})u^{-1-\nu}du = \Gamma(1-\nu)/\nu$. ✓
- **OU conditional expectation $\theta^{2\nu} = \theta^{1-\beta}$**: verified. ✓
- **Standing hypothesis for OU at $\beta > 1/2$**: verified by direct spectral integral. ✓
- **Cor 2 inversion of weight-conjugated factors**: verified. ✓
- **Prop 3 KKT eigenfunction bound $|\phi_1(t)| \le d(t)^{-\nu}(T/2)^{-\nu}$**: verified. ✓
- **Prop 3 Marchaud tail bound**: re-derived, found constant discrepancy (E1). ✗
- **Exp factors**: Fourier convention + $\hat\partial_t = -i\xi$ check. ✓
- **eq (exp-bulk) internal consistency**: found the OU-step inconsistency (E2). ✗
- **eq (exp-ou) final form**: independently re-derived. ✓
- **Sign flip at $\theta = \kappa$**: verified. ✓
- **§5.2 crossover frequency**: verified. ✓
- **§5.3 multi-asset diagonalization**: verified. ✓
- **§6 position-Fourier-symbol $1/\xi^2$**: verified. ✓
- **§6 joint symbol log-integrability**: verified. ✓
- **App symbol identity $CD_+^\nu = c_\beta I_-^\nu$**: verified. ✓
- **App Cor 1 proof Steps (a)/(b)/(c)**: re-derived all three. ✓

## Inline Annotations

| Location | Object | Verification |
|---|---|---|
| §2.2 eq (7) | Adapted FOC | ✓ Re-derived |
| §2.2 eq (8) | Operator FOC | ✓ Trivial from (7) |
| §3.3 Lemma 1 | Projected-inverse identity | ✓ Full re-derivation |
| §3.4 Theorem 1 | Closed form | ✓ Lemma 1 + FOC |
| §3.4 eq (proj-cma) | Commutation | ✓ Conditional Fubini |
| §3.5 eq (value) | Value formula | ✓ Convex duality |
| §3.1 Prop 1 | WH factorization | ✓ Classical |
| §3.2 Prop 2 | GK factorization | ✓ Classical (Arveson) |
| §4 eq (16) | Whole-line power-law factors | ✓ Symbol calc |
| §4 boundedness caveat | Unbounded $C_\pm^{-1}$ | ✓ Correct diagnosis |
| §4 eq (17)–(18) | Volterra kernel + weight conj | ✓ $TT^*$ consistency |
| §4.1 Cor 1 | Bulk formula | ✓ Substitution |
| §4.1 eq (21) | OU signal | ✓ Marchaud integral |
| §4.2 Cor 2 | Finite-interval formula | ✓ Factor inversion |
| §4.3 Prop 3 | Interior error statement | ✓ Correct scalings |
| App Prop 3 proof (L373) | Marchaud tail constant | ✗ **E1**: $\nu^{-1} \to \Gamma(1-\nu)^{-1}$ |
| §5.1 eq (exp-bulk) | Exp bulk formula | ✓ Correct under Option B convention |
| §5.1 line 310 | OU intermediate $\zeta$ | ✗ **E2**: extraneous $(2\kappa)^{-1/2}$ |
| §5.1 eq (exp-ou) | Exp OU final | ✓ Correct |
| §5.1 sign flip | $\theta = \kappa$ | ✓ |
| §5.2 crossover $\xi_*$ | Frequency scaling | ✓ |
| §5.3 multi-asset | Diagonalization | ✓ |
| §6 joint operator | $\gamma\hat C + \lambda\Sigma/\xi^2$ | ✓ Sound extension |
| App symbol identity | $CD_+^\nu = c_\beta I_-^\nu$ | ✓ Verified |
| App Cor 1 proof | Steps (a)/(b)/(c) | ✓ Verified |
| App Cor 2 proof | Factor inversion | ✓ Verified |

## Recommendation

**Accept on mathematical grounds** with two one-line fixes:

1. Line 373 (App Prop 3 proof): change `\tfrac{2\|f\|_\infty}{\nu}` to `\tfrac{2\|f\|_\infty}{\Gamma(1-\nu)}`.
2. Line 310 (§5.1): change `$\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$` to `$\zeta_s = (\kappa+\theta)\alpha_s$`.

Neither fix changes any headline result. Both prevent a reader who traces the derivations line-by-line from encountering a numerical inconsistency.

No other mathematical changes needed. The main theorems, corollaries, and propositions all hold as stated.

## Sources

- Primary: `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/tex/factorization-optimal-trading.tex` (read in full for previous review pass; targeted re-reads for this pass of §5.1 lines 305–315 and Appendix line 373).
- Standard references used implicitly during verification:
  - Samko, Kilbas, Marichev (1993), *Fractional Integrals and Derivatives*: Marchaud definitions, $I_-^\nu D_-^\nu = \mathrm{id}$ on $H^\nu(\R)$ (§5.3 Thm 5.3), and standard integrals.
  - Hytönen, van Neerven, Veraar, Weis (2016), Prop 2.6.13: conditional-expectation commutation with deterministic operators.
  - Klenke (2014), Thm 14.16: conditional Fubini.
  - Standard Wiener–Hopf / Arveson outer-factorization theory.
- Evidence notes with full derivations: `outputs/.drafts/factorization-optimal-trading-math-review-evidence.md`.
- Plan: `outputs/.plans/factorization-optimal-trading-math-review-plan.md`.
