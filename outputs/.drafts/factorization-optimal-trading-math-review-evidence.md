# Math Evidence: factorization-optimal-trading-math

Every derivation in the paper checked below; ✓ = re-derived and matches paper, ✗ = discrepancy found.

## §2.2 Adapted first-order condition ✓

Objective: $J(u) = \E\int u\alpha - \tfrac{\gamma}{2}\E\iint G(|t-v|)u_tu_v$. Gâteaux derivative in adapted direction $\delta u\in L^2_{\adap}$:
$$dJ[\delta u] = \E\!\int(\alpha_t - \gamma(Cu)(t))\delta u_t\,dt.$$
Adaptedness of $\delta u$ + tower: $\E[\delta u_t\cdot X] = \E[\delta u_t\E_t[X]]$. So
$$dJ[\delta u] = \E\!\int\delta u_t\bigl\{\E_t[\alpha_t] - \gamma\E_t[(Cu)(t)]\bigr\}dt.$$
Setting $=0$ for all adapted $\delta u$ and using $\alpha$ adapted ⇒ $\E_t[\alpha_t]=\alpha_t$ gives $\gamma\E_t[(Cu^\star)(t)] = \alpha_t$. Operator form $\gamma P_+CP_+u^\star = \alpha$ follows since $(P_+X)_s = \E_s[X_s]$. **Matches eq (7)–(8).** ✓

## §3.3 Lemma 1 (projected-inverse identity) ✓

Claim: $(P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1}$ on $L^2_{\adap}$, with $C = C_-C_+$, $C_+$ causal Volterra, $C_-=C_+^*$.

*Sub-claim 1*: $C_+$ causal ⇒ $C_+u$ adapted whenever $u$ adapted (since $(C_+u)(t)$ uses only $u_s$ for $s\le t$, and $u_s\in\F_s\subset\F_t$). Hence $C_+^{-1}$ preserves $L^2_{\adap}$ and commutes with $P_+$ on adapted inputs, i.e., $P_+^\perp C_+P_+ = 0$. ✓

*Sub-claim 2*: adjoint: $P_+C_-P_+^\perp = (P_+^\perp C_+P_+)^* = 0$. Equivalently $P_+C_- = P_+C_-P_+$. ✓

*Composition verification*: for adapted $u$, let $v = C_+^{-1}P_+C_-^{-1}u$. Then $v$ is adapted (as $C_+^{-1}$ preserves adapted). Compute
$$P_+CP_+\,v = P_+C_-C_+v = P_+C_-\cdot(C_+v) = P_+C_-\cdot P_+C_-^{-1}u.$$
Split $C_-^{-1}u = P_+C_-^{-1}u + P_+^\perp C_-^{-1}u$. Since $C_-$ preserves the anticausal subspace, $C_-\cdot P_+^\perp C_-^{-1}u \in P_+^\perp$, so $P_+C_-\cdot P_+^\perp C_-^{-1}u = 0$. Therefore
$$P_+C_-\cdot P_+C_-^{-1}u = P_+C_-\cdot C_-^{-1}u = P_+u = u.$$
Hence $(P_+CP_+)(C_+^{-1}P_+C_-^{-1}u) = u$ for every adapted $u$. ✓

**Lemma 1 is correct.** The proof in §3.3 is compressed but valid. Appendix versions cover whole-line + finite-interval cases.

## §3.4 Theorem 1 ✓

Direct consequence of Lemma 1 and eq (foc-op). $u^\star = \gamma^{-1}(P_+CP_+)^{-1}\alpha = \gamma^{-1}C_+^{-1}P_+C_-^{-1}\alpha$. ✓

## eq (proj-cma) ✓

Claim: $(P_+C_-^{-1}\alpha)_s = (C_-^{-1}\bar\alpha(s,\cdot))(s)$.

Compute: $(P_+X)_s = \E_s[X_s]$. So
$$(P_+C_-^{-1}\alpha)_s = \E_s\!\left[\int k(s,r)\alpha_r\,dr\right] = \int k(s,r)\E_s[\alpha_r]\,dr = \int k(s,r)\bar\alpha(s,r)\,dr = (C_-^{-1}\bar\alpha(s,\cdot))(s),$$
by conditional Fubini and definition of $\bar\alpha$. ✓ Kernel $k$ supported on $r\ge s$ (anticausal), matching paper's cited Hytönen et al. Prop 2.6.13.

## §3.5 eq (value) ✓

Value at $u^\star$: standard convex Legendre duality gives $V(\alpha) = \tfrac{1}{2\gamma}\langle\alpha, C_+^{-1}P_+C_-^{-1}\alpha\rangle$. Since $(C_+^{-1})^* = C_-^{-1}$ and $P_+^2 = P_+$:
$$\langle\alpha, C_+^{-1}P_+C_-^{-1}\alpha\rangle = \langle C_-^{-1}\alpha, P_+C_-^{-1}\alpha\rangle = \|P_+C_-^{-1}\alpha\|^2 + \langle P_+^\perp C_-^{-1}\alpha, P_+C_-^{-1}\alpha\rangle = \|P_+C_-^{-1}\alpha\|^2.$$
✓

**Signal-engineering claim** in §5.5: value weights the forecast spectrum by $|\xi|^{1-\beta}$. Strictly, $\|\hat C_-^{-1}\|^2 = c_\beta^{-1}|\xi|^{1-\beta}$; the $P_+$ complicates the full spectral identity, but the physical weighting is correct. Semi-heuristic but defensible.

## §3.1 Prop 1 (Wiener–Hopf) — classical ✓

Log-integrability + positivity ⇒ symbol factors with one-sided analytic factors (Szegő / Wiener–Hopf). Standard.

## §3.2 Prop 2 (Gohberg–Krein) — classical ✓

Compact positive perturbation of identity on $L^2([0,T])$ ⇒ Volterra outer factorization. Standard (Arveson 1975; Porter–Stirling 1990).

## §4 opening — power-law factors

### Whole-line factors ✓
$\hat C(\xi) = c_\beta|\xi|^{\beta-1}$. Writing $|\xi|^{\beta-1} = |\xi|^{-2\nu} = (i\xi)^{-\nu}(-i\xi)^{-\nu}$ with standard branches gives $\hat C_+(\xi) = c_\beta^{1/2}(-i\xi)^{-\nu}$ (analytic in upper half-plane), $\hat C_-(\xi) = c_\beta^{1/2}(i\xi)^{-\nu}$. Time-domain: $(-i\xi)^{-\nu}$ is the Fourier symbol of $\Gamma(\nu)^{-1}(t-\cdot)_+^{\nu-1}$, i.e., causal Riemann–Liouville integral. Matches eq (16). ✓

### Log-integrability of pure power-law ✓
$\log\hat C = \log c_\beta + (\beta-1)\log|\xi|$. Integrand against $(1+\xi^2)^{-1}$:
- $\log c_\beta/(1+\xi^2)$ integrable (constant × Cauchy).
- $\log|\xi|/(1+\xi^2)$: near 0, $\int_0^1|\log\xi|d\xi<\infty$; at $\infty$, $\log|\xi|/\xi^2$ integrable.

So log-integrability holds. **Boundedness caveat correctly notes** that the factors are unbounded on $L^2$ (symbols diverge at 0 or ∞); identity holds on the dense domain fixed by the standing spectral hypothesis. ✓

### Finite-interval factors ✓
Volterra kernel $k(s,t)$ and weight-conjugated form: consistent with $G_T = TT^*$. Check: $T = c_\beta^{1/2}B^{-1}I_+^\nu B$, $T^* = c_\beta^{1/2}BI_-^\nu B^{-1}$, so $TT^* = c_\beta B^{-1}I_+^\nu B\cdot BI_-^\nu B^{-1} = c_\beta B^{-1}I_+^\nu B^2 I_-^\nu B^{-1}$. ✓

## §4.1 Cor 1 (bulk formula) ✓

$C_+^{-1}P_+C_-^{-1} = c_\beta^{-1/2}D_+^\nu\cdot P_+\cdot c_\beta^{-1/2}D_-^\nu = c_\beta^{-1}D_+^\nu P_+ D_-^\nu$. Then $u^\star = \gamma^{-1}c_\beta^{-1}D_+^\nu(P_+D_-^\nu\alpha)_t$. Denoting $\zeta_s := (P_+D_-^\nu\alpha)_s = (D_-^\nu\bar\alpha(s,\cdot))(s)$ (by proj-cma), get $u^\star_t = \gamma^{-1}c_\beta^{-1}(D_+^\nu\zeta)(t)$. ✓ Matches eq (bulk) exactly.

## OU signal (eq 21) ✓

For OU $d\alpha_t = -\theta\alpha_t dt + \sigma dW_t$: $\E_t[\alpha_{t+r}] = \alpha_t e^{-\theta r}$ for $r\ge 0$, so $\bar\alpha(t, t+r) = \alpha_t e^{-\theta r}$ for $r\ge 0$.

Anticausal Marchaud at $t$ uses only $r\ge 0$:
$$(D_-^\nu\bar\alpha(t,\cdot))(t) = \frac{\nu}{\Gamma(1-\nu)}\int_0^\infty\frac{\alpha_t - \alpha_t e^{-\theta r}}{r^{1+\nu}}dr = \frac{\nu\alpha_t}{\Gamma(1-\nu)}\int_0^\infty\frac{1-e^{-\theta r}}{r^{1+\nu}}dr.$$

Substituting $u = \theta r$, $du = \theta dr$: $\int = \theta^\nu\int_0^\infty(1-e^{-u})u^{-1-\nu}du$. Integration by parts: $\int_0^\infty(1-e^{-u})u^{-1-\nu}du = \frac{\Gamma(1-\nu)}{\nu}$.

Therefore $(D_-^\nu\bar\alpha(t,\cdot))(t) = \frac{\nu\alpha_t}{\Gamma(1-\nu)}\cdot\theta^\nu\cdot\frac{\Gamma(1-\nu)}{\nu} = \theta^\nu\alpha_t$. ✓

For the conditional expectation of the outer step: $\E[(D_+^\nu\alpha)(t)|\alpha_t]$. Stationary OU: $\E[\alpha_{t-r}|\alpha_t] = e^{-\theta r}\alpha_t$. Same integral gives $\theta^\nu\alpha_t$. Combined: $\gamma^{-1}c_\beta^{-1}\theta^{2\nu}\alpha_t = \gamma^{-1}c_\beta^{-1}\theta^{1-\beta}\alpha_t$ since $2\nu = 1-\beta$. ✓

**Standing hypothesis for OU**: at high $\xi$, OU spectrum $\sim|\xi|^{-2}$, so $(1+|\xi|^{2(1-\beta)+\epsilon})S_\alpha \sim |\xi|^{-2\beta+\epsilon}$ requires $\beta>(1+\epsilon)/2$, i.e., $\beta > 1/2$. ✓

## §4.2 Cor 2 (finite interval) ✓

Invert $T = c_\beta^{1/2}B^{-1}I_+^\nu B$: $T^{-1} = c_\beta^{-1/2}B^{-1}(I_+^\nu)^{-1}B = c_\beta^{-1/2}B^{-1}D_+^\nu B$. Similarly $(T^*)^{-1} = c_\beta^{-1/2}BD_-^\nu B^{-1}$. Compose $u^\star = \gamma^{-1}T^{-1}P_+(T^*)^{-1}\alpha^{eff}$:
$$= \gamma^{-1}c_\beta^{-1/2}B^{-1}D_+^\nu B\cdot P_+\cdot c_\beta^{-1/2}BD_-^\nu B^{-1}\alpha^{eff}$$
$$= \gamma^{-1}c_\beta^{-1}B^{-1}D_+^\nu BP_+BD_-^\nu B^{-1}\alpha^{eff}. ✓$$

## §4.3 Prop 3 (interior error) — statement ✓, proof constant ✗

**Statement is correct** (asymptotics + generic constants $C_1(\beta), C_2(\beta)$).

**Proof error in appendix** (line 373): the Marchaud tail bound is stated as
$$|(D_-^\nu f)(s) - (D_-^{\nu,[0,T]}f)(s)| \le \frac{2\|f\|_\infty}{\nu}(T-s)^{-\nu}.$$
Correct derivation:
$$\text{tail} = \frac{\nu}{\Gamma(1-\nu)}\int_{T-s}^\infty\frac{f(s)-f(s+r)}{r^{1+\nu}}dr$$
$$\left|\text{tail}\right| \le \frac{\nu}{\Gamma(1-\nu)}\cdot 2\|f\|_\infty\int_{T-s}^\infty r^{-1-\nu}dr = \frac{\nu}{\Gamma(1-\nu)}\cdot 2\|f\|_\infty\cdot\frac{(T-s)^{-\nu}}{\nu} = \frac{2\|f\|_\infty}{\Gamma(1-\nu)}(T-s)^{-\nu}.$$

The $\nu$ from the integration cancels the $\nu$ in Marchaud's prefactor. Paper's $\nu^{-1}$ should be $\Gamma(1-\nu)^{-1}$.

**Impact**: the constant is absorbed into $C_1(\beta)$ in the proposition statement, so the theorem is unaffected. But the appendix derivation is numerically wrong at the intermediate step.

**KKT eigenfunction bound**: $\phi_1(t) = [t(T-t)]^{(\beta-1)/2}$. $d(t) = \min(t, T-t)$. For $t \le T/2$: $d(t) = t$, $T-d(t) = T-t \ge T/2$. So $|\phi_1(t)| = t^{(\beta-1)/2}(T-t)^{(\beta-1)/2} = t^{-\nu}(T-t)^{-\nu} \le t^{-\nu}(T/2)^{-\nu} = d(t)^{-\nu}(T/2)^{-\nu}$. ✓

## §5.1 Exponential kernel ✓ operator setup, ✗ intermediate OU step

**Factors ✓**: $\hat C(\xi) = 2\kappa/(\kappa^2+\xi^2) = \sqrt{2\kappa}/(\kappa-i\xi)\cdot\sqrt{2\kappa}/(\kappa+i\xi)$. Upper-half-plane factor $\hat C_+(\xi) = \sqrt{2\kappa}/(\kappa-i\xi)$; time-domain $C_+$ is causal exp convolution. Inverse in Fourier: $\hat C_+^{-1}(\xi) = (\kappa-i\xi)/\sqrt{2\kappa}$, i.e., operator $(2\kappa)^{-1/2}(\kappa+\partial_t)$ (with Fourier convention $\hat{\partial_t f} = -i\xi\hat f$). ✓

**eq (exp-bulk) — INTERNAL INCONSISTENCY ✗**

Paper defines: $\zeta_s = (\kappa-\partial_r)\bar\alpha(s,r)|_{r=s^+}$ (without $(2\kappa)^{-1/2}$).
Paper defines: $u^{exp}_t = \frac{1}{2\kappa\gamma}(\kappa+\partial_t)\zeta_t$.

But the actual application of Theorem 1 is
$$u^\star = \gamma^{-1}C_+^{-1}P_+C_-^{-1}\alpha = \gamma^{-1}(2\kappa)^{-1/2}(\kappa+\partial_t)\cdot P_+\cdot(2\kappa)^{-1/2}(\kappa-\partial_r)\alpha.$$
If we let $\zeta_s := (P_+ C_-^{-1}\alpha)_s$, then
$$\zeta_s = (2\kappa)^{-1/2}(\kappa-\partial_r)\bar\alpha(s,r)|_{r=s^+}.$$
This carries the factor $(2\kappa)^{-1/2}$ that eq (exp-bulk) omits.

Two equivalent presentations:
- **Option A** (analogous to Cor 1's placement of $c_\beta^{-1/2}$): put both prefactors inside as $\zeta_s := (2\kappa)^{-1/2}(\kappa-\partial_r)\bar\alpha$ and $u^{exp}_t = \gamma^{-1}(2\kappa)^{-1/2}(\kappa+\partial_t)\zeta_t$. Full prefactor $\gamma^{-1}(2\kappa)^{-1}$. ✓
- **Option B** (analogous to Cor 1's actual form): distribute — bare $\zeta$ carries no factor, outer holds all of $\gamma^{-1}(2\kappa)^{-1} = (2\kappa\gamma)^{-1}$: $\zeta_s := (\kappa-\partial_r)\bar\alpha$ and $u^{exp}_t = \frac{1}{2\kappa\gamma}(\kappa+\partial_t)\zeta_t$. ✓

Paper's eq (exp-bulk) uses Option B. But the very next line (OU evaluation) writes
> "$\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$"

This has an extraneous $(2\kappa)^{-1/2}$ that would be Option A. Substituted directly into eq (exp-bulk) it produces
$$\frac{1}{2\kappa\gamma}(\kappa+\partial_t)(2\kappa)^{-1/2}(\kappa+\theta)\alpha_t = \frac{\kappa+\theta}{(2\kappa)^{3/2}\gamma}(\kappa+\partial_t)\alpha_t,$$
which is $(2\kappa)^{-1/2}$ times the paper's stated eq (exp-ou). **Contradiction** with the correct eq (exp-ou).

**Fix**: line 310 should read $\zeta_s = (\kappa+\theta)\alpha_s$ (no $(2\kappa)^{-1/2}$), matching eq (exp-bulk)'s Option B. Direct check:
$(\kappa-\partial_r)\bar\alpha(s, r)|_{r=s^+} = (\kappa-\partial_r)[\alpha_s e^{-\theta(r-s)}]|_{r=s^+} = \kappa\alpha_s - (-\theta\alpha_s) = (\kappa+\theta)\alpha_s$. ✓

Then eq (exp-ou): $\frac{1}{2\kappa\gamma}(\kappa+\partial_t)(\kappa+\theta)\alpha_t = \frac{\kappa+\theta}{2\kappa\gamma}(\kappa+\partial_t)\alpha_t = \frac{\kappa+\theta}{2\kappa\gamma}[(\kappa-\theta)\alpha_t + \sigma\dot W_t]$. ✓ matches paper.

**Impact**: eq (exp-ou) itself is correct; the intermediate step has a typo. Final sign-flip statement $\theta = \kappa$ is unaffected: $\E[u^{exp}_t|\alpha_t] = \frac{\kappa+\theta}{2\kappa\gamma}(\kappa-\theta)\alpha_t = \frac{\kappa^2-\theta^2}{2\kappa\gamma}\alpha_t$. ✓

## §5.2 Temporary impact ✓

Modified symbol $M(\xi) = c_\beta|\xi|^{\beta-1} + \eta/\gamma$ (dividing FOC by $\gamma$). Crossover: $c_\beta|\xi_*|^{\beta-1} = \eta/\gamma \Rightarrow |\xi_*|^{1-\beta} = \gamma c_\beta/\eta \Rightarrow \xi_* = (\gamma c_\beta/\eta)^{1/(1-\beta)}$. ✓

High-frequency limit: $M\to \eta/\gamma$, $M^{-1}\to\gamma/\eta$, so $u^\star\approx\alpha/\eta$ (dropping the $\gamma^{-1}$ since original problem had $\gamma$ in Hessian: with full symbol $\gamma M = \gamma c_\beta|\xi|^{\beta-1}+\eta$, high-freq limit $\gamma M\to\eta$, so $u^\star = \alpha/(\gamma M)\to\alpha/\eta$). ✓

## §5.3 Multi-asset diagonalization ✓

Cross-impact $\mathbf{K}(t) = |t|^{-\beta}\mathbf{A}$, $\mathbf{A} = Q\Lambda Q^\top$. In rotated basis $\tilde u = Q^\top u$, $\tilde\alpha = Q^\top\alpha$: $i$-th component has scalar impact symbol $\Lambda_{ii}c_\beta|\xi|^{\beta-1}$. FOC: $\gamma\Lambda_{ii}c_\beta|\xi|^{\beta-1}\tilde u_i = \tilde\alpha_i$. Bulk formula with prefactor $\gamma^{-1}\Lambda_{ii}^{-1}c_\beta^{-1}$. ✓

## §6 Joint gain–risk–cost ✓

$x_t = \int_{-\infty}^t u_s ds$ gives $\hat x(\xi) = \hat u(\xi)/(-i\xi) = i\hat u/\xi$. Quadratic $\int|x|^2 = \int|\hat u|^2/\xi^2$, symbol $\xi^{-2}$. With matrix penalty $\lambda\Sigma$: total symbol $\gamma\hat C(\xi) + \lambda\Sigma/\xi^2$. ✓

Log-integrability of $\gamma c_\beta|\xi|^{\beta-1} + \lambda\Sigma/\xi^2$:
- Near 0: dominated by $\lambda/\xi^2\to\infty$; $\log\to -2\log|\xi|$; integrable against $(1+\xi^2)^{-1}$.
- Near ∞: dominated by $\gamma c_\beta|\xi|^{\beta-1}\to 0$; $\log\to(\beta-1)\log|\xi|$; integrable.

So Prop 1 applies to the joint symbol; Lemma 1 gives a closed-form joint optimum. ✓ Outlook is technically sound.

## Appendix: symbol identity $CD_+^\nu = c_\beta I_-^\nu$ ✓

$\hat C(\xi) = c_\beta|\xi|^{\beta-1} = c_\beta(i\xi)^{-\nu}(-i\xi)^{-\nu}$. Symbol of $D_+^\nu$ is $(-i\xi)^\nu$. So $\hat C\cdot(-i\xi)^\nu = c_\beta(i\xi)^{-\nu}$, which is the symbol of $c_\beta I_-^\nu$. ✓

## Appendix: Cor 1 proof ✓

Steps (a)/(b)/(c) all check out; conditional Fubini + $I_-^\nu D_-^\nu = \mathrm{id}$ on $H^\nu(\R)$ + adaptedness at $s=t$ give $\bar\alpha(t,t) = \alpha_t$. All valid.

## Notation-consistency grep ✓

`\kappa_{1-\beta}` fully removed after the notation cleanup (0 hits). `\kappa` now used only for exponential decay rate. Volterra kernel renamed to $k(s,t)$. ✓

---

## Summary of errors

| # | Location | Error | Severity | Downstream impact |
|---|---|---|---|---|
| E1 | App Prop 3 proof (line 373) | Marchaud tail bound $\frac{2\|f\|_\infty}{\nu}$ should be $\frac{2\|f\|_\infty}{\Gamma(1-\nu)}$ (the $\nu$ from integration cancels the Marchaud prefactor $\nu$, leaving $\Gamma(1-\nu)^{-1}$). | Minor (constant only) | None — absorbed into $C_1(\beta)$ in the proposition statement. |
| E2 | §5.1 line 310 | Intermediate OU step writes $\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$; extra $(2\kappa)^{-1/2}$ inconsistent with eq (exp-bulk)'s convention (Option B: bare $\zeta$, all prefactors outside). | Minor typo | Final eq (exp-ou) is correct. Only the intermediate step is inconsistent. |

## Sources
- `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/tex/factorization-optimal-trading.tex` (read in full previously; targeted re-reads for §5.1 lines 305–315 and App line 373 confirmed).
- Standard references implicitly used:
  - Samko–Kilbas–Marichev (1993), *Fractional Integrals and Derivatives*: Marchaud definitions, $I^\nu D^\nu = \mathrm{id}$ on $H^\nu(\R)$.
  - Hytönen–van Neerven–Veraar–Weis (2016), Prop 2.6.13: conditional-expectation commutation.
  - Klenke (2014), Thm 14.16: conditional Fubini.
