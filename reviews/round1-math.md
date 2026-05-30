# Round-1 Mathematical Review: `papers/noisy-signal-impact-trading.md`

Scope: derivations only. Each item below states a verdict (VERIFIED / INCORRECT / AMBIGUOUS / TENTATIVE), the supporting computation, and severity.

---

## 1. §2.2–2.3 — Symmetrised kernel and cost functional

**Verdict: AMBIGUOUS (minor; convention-dependent).**

Starting from the stated impact cost per step
$$C_t = \sum_{s\le t} G(t-s)\,x_s\,x_t,$$
the total cost is
$$\sum_t C_t = G(0)\sum_t x_t^2 + \sum_{s<t} G(t-s)\,x_s x_t.$$

The symmetric form $\tfrac12\sum_{s,t} K(t-s) x_s x_t$ with $K(n)=G(|n|)$ expands to
$$\tfrac12 G(0)\sum_t x_t^2 + \sum_{s<t} G(t-s)\,x_s x_t.$$

The two expressions differ by $\tfrac12 G(0)\sum_t x_t^2$. This is the standard "execution-at-mid" convention (Gatheral, Bouchaud): the trader pays only *half* of the instantaneous self-impact $G(0)$, the other half being the post-trade book displacement. The paper silently invokes this convention. The frequency-domain analysis that follows uses the symmetric form, so internal consistency is fine, but the passage from §2.2 ("expected cost") to §2.3 ("symmetrising") drops $\tfrac12 G(0)\sum x_t^2$ without comment.

**Severity:** minor / note. A one-sentence justification ("execution at mid means the agent pays half of the contemporaneous impact, hence $K(0)=G(0)$ in the symmetric form") would close this.

---

## 2. §3 — Legendre–Fenchel transform of $\phi(x)=\tfrac12\langle x,Kx\rangle$

**Verdict: VERIFIED.**

FOC of $\langle f,x\rangle - \tfrac12\langle x,Kx\rangle$ in $x$: $f = Kx$, so $x^* = K^{-1}f$ (assuming $K$ invertible, which is guaranteed by §2.4's $\hat K(\omega)>0$). Substituting back:
$$\langle f, K^{-1}f\rangle - \tfrac12\langle K^{-1}f, K\,K^{-1}f\rangle = \tfrac12\langle f, K^{-1}f\rangle.$$
Equations (2), (3) are correct.

---

## 3. §4.1 — Causal Wiener–Hopf solution

**Verdict: AMBIGUOUS in derivation, VERIFIED in final formula (6).**

The user's concern is right: the objective is $\langle f,x\rangle-\tfrac12\langle x,K*x\rangle$, *not* an MMSE problem. The correct FOC under causality is "the causal projection of the residual vanishes":
$$[K*x - f]_+ = 0,\quad x\text{ causal}.$$
Writing $K=K_+K_-$, set $y=K_+ x$ (causal). Then $K_- y = f \pmod{\text{anticausal}}$, i.e. $y = [f/K_-]_+$, giving
$$\hat x = \hat K_+^{-1}\bigl[\hat f/\hat K_-\bigr]_+,$$
which is equation (6). So (6) is correct.

However, the *intermediate* equations (4)–(5) are wrong/garbled. Equation (4) reads
$$\hat K\,\hat H\,S_f = [S_f/\hat K_-]_+,$$
which is the MMSE-Wiener structure (signal covariance $S_f$ appearing as a weight), not the projection FOC of the quadratic. For an AR(1) signal $\hat f(z)=\sigma/(1-\rho z^{-1})$ we have $S_f = |\hat f|^2$, and $[S_f/\hat K_-]_+$ is *not* the same object as $[\hat f/\hat K_-]_+$ — the answers happen to coincide up to a constant only because $S_f$ further factors. Equation (5) introduces $1/\hat f$ on the right but this only makes sense in a deterministic (transfer-function) view of $\hat f$, which is inconsistent with the spectral-density view used in (1) and (4).

**Severity:** blocker for clarity; the displayed derivation does not justify the (correct) boxed formula (6). Suggest deleting (4)–(5) and replacing with the two-line FOC-projection derivation above.

---

## 4. §5.1 — Spectral factors of $K(n)=\lambda^{|n|}$

**Verdict: VERIFIED.**

Two-sided $z$-transform:
$$\sum_{n\in\mathbb Z} \lambda^{|n|} z^{-n} = \frac{1}{1-\lambda z^{-1}} + \frac{\lambda z}{1-\lambda z} = \frac{1-\lambda^2}{(1-\lambda z^{-1})(1-\lambda z)}.$$
Factor with pole at $z=\lambda$ inside the unit disk: $\hat K_+(z)=\sqrt{1-\lambda^2}/(1-\lambda z^{-1})$, impulse response $\sqrt{1-\lambda^2}\,\lambda^n$ for $n\ge0$ (causal, stable). The other factor $\hat K_-(z)=\sqrt{1-\lambda^2}/(1-\lambda z)$ has pole at $z=1/\lambda$ outside the unit disk and expands in non-negative powers of $z$ (anticausal). Product $=\hat K(z)$. ✓

---

## 5. §5.2–5.3 — Partial-fractions identity

**Verdict: VERIFIED.**

Check
$$(-\lambda z + 1 - \lambda\rho)(z-\rho) + \rho(1-\lambda\rho)$$
$$= -\lambda z^2 + \lambda\rho z + (1-\lambda\rho)z - \rho(1-\lambda\rho) + \rho(1-\lambda\rho)$$
$$= -\lambda z^2 + [\lambda\rho + 1 - \lambda\rho]z = -\lambda z^2 + z. \;\checkmark$$
Equation (7) also checks: $(1-\lambda z)\sigma /[(1-\rho z^{-1})\sqrt{1-\lambda^2}] = \sigma z(1-\lambda z)/[(z-\rho)\sqrt{1-\lambda^2}]$. ✓

---

## 6. §5.3 — Is $-\lambda z$ anticausal?

**Verdict: VERIFIED (and consistent with the paper's $z$-convention).**

Convention: $\hat f(z)=\sum_n f_n z^{-n}$ (the paper uses $\hat f(z)=\sigma/(1-\rho z^{-1})$, expanding to $\sigma\sum_{n\ge0}\rho^n z^{-n}$, i.e. coefficient of $z^{-n}$ is $f_n$ — standard causal convention with $z^{-1}$ as the lag operator). Hence $z^{+1}$ corresponds to $\delta_{t+1}$ (a strictly future sample) and is anticausal; $\rho/(z-\rho)=\rho z^{-1}/(1-\rho z^{-1})$ expands in strictly positive lags and is causal. Both classifications in §5.3 are correct and consistent with the rest of the paper.

---

## 7. §5.4, eq. (12) — limit checks

**Verdict: INCORRECT (in the limit-case statements; the boxed formula (12) itself is correct).**

Formula: $x_t = \dfrac{1-\lambda\rho}{1-\lambda^2}(f_t-\lambda f_{t-1})$.

* $\lambda\to 0$: prefactor $\to 1$, gives $x_t=f_t$. ✓ Matches paper.
* $\rho\to 0$: prefactor $\to 1/(1-\lambda^2)$. The paper states $1/(1+\lambda)$. **Wrong.** $1/(1-\lambda^2) = 1/[(1-\lambda)(1+\lambda)]$, not $1/(1+\lambda)$.
* $\rho\to\lambda$: prefactor $=(1-\lambda^2)/(1-\lambda^2)=1$, giving $x_t = f_t-\lambda f_{t-1}$. The paper states "same formula" $\tfrac1{1+\lambda}(f_t-\lambda f_{t-1})$. **Wrong.**
* $\rho\to 1$: prefactor $=(1-\lambda)/(1-\lambda^2) = 1/(1+\lambda)$. The paper states $c\to(1-\lambda^2)^{-1/2}$. **Wrong.**

All three "non-trivial" limit statements in §5.4 contain algebra errors, even though the master formula they are checking is correct.

**Severity:** minor mathematically (the headline result is right) but a **blocker for credibility** — these are exactly the sanity checks a careful reader will compute. Fix the three limits.

---

## 8. §6.2 — Power-law kernel exponent

**Verdict: VERIFIED (with a definitional caveat to flag).**

If $\hat K(\omega)\sim C|\omega|^{\beta-1}$ for $|\omega|\ll1$, then $|\hat K_+(\omega)|^2=\hat K(\omega)$ gives $|\hat K_+(\omega)|\sim |\omega|^{(\beta-1)/2}$, and the outer (causal) factor is $\hat K_+(\omega)\sim C_+(-i\omega)^{(\beta-1)/2}$ (the unique choice analytic in the upper half-plane). Hence $\hat K_+^{-1}\sim (-i\omega)^{(1-\beta)/2}$ with $(1-\beta)/2\in(0,\tfrac12)$ for $\beta\in(0,1)$. ✓

**Caveat the user flagged:** the *summed* symmetric kernel $\sum_n |n|^{-\beta}$ converges only for $\beta>1$. The paper instead needs $K$ to be a *positive-definite tempered distribution* with $\hat K(\omega)\sim|\omega|^{\beta-1}$ locally integrable at zero — which is fine for $\beta\in(0,1)$, matching the Bouchaud-style empirical range. The paper conflates "kernel" (an $\ell^1$ sequence in §2) with "positive-definite distribution" (necessary in §6.2) without comment. Worth one explanatory sentence: in the power-law regime $K$ is defined via its spectrum, not via $\ell^1$ summation, and $\hat K\in L^1_{\rm loc}$ suffices.

Note also that *causal* propagators $G(t)\sim t^{-\beta}$ with $\beta\in(0,1)$ are *not* square-summable; the symmetrised $K(n)=G(|n|)$ inherits this. Section 2.4's "$\hat K(\omega)>0$" condition needs to be reinterpreted distributionally in this regime.

**Severity:** minor / note; the exponent computation itself is correct.

---

## 9. §7.3 — Separation principle (proof sketch)

**Verdict: VERIFIED in principle (Gaussian-linear case), with a small but standard subtlety.**

Let $x$ be adapted to the noisy-observation filtration $\mathcal F^{\tilde f}$. Since $x_t$ is $\mathcal F_t^{\tilde f}$-measurable, the tower property gives
$$\mathbb E[f_t x_t] = \mathbb E\bigl[\mathbb E[f_t\mid\mathcal F_t^{\tilde f}]\,x_t\bigr] = \mathbb E[\hat f_t^W\, x_t],$$
where $\hat f^W:=\mathbb E[f\mid\mathcal F^{\tilde f}]$ is — under joint Gaussianity — the causal Wiener filter output. The cost $\tfrac12\mathbb E[x_t(K*x)_t]$ involves only $x$ (which is $\mathcal F^{\tilde f}$-measurable and $K$ is deterministic), so it is unchanged. Hence the noisy-observation objective equals the clean-signal objective with $f$ replaced by $\hat f^W$, and the clean-signal Wiener–Hopf machinery applies to $\hat f^W$.

Two caveats worth mentioning explicitly:
1. The reduction uses linearity of expectation and adaptedness; full Gaussianity is only needed to identify $\mathbb E[f\mid\mathcal F^{\tilde f}]$ with the *linear* Wiener filter. The paper says this but could be tighter.
2. The argument requires that the admissible class includes "all causal linear functions of $\tilde f$"; under that restriction (which is what the paper actually optimises over, being a quadratic-in-$H$ problem), Gaussianity is unnecessary — the result is exact for any second-order stationary $(f,\eta)$.

**Severity:** none.

---

## 10. §8.1 eq. (22) — Re-applying (12) with $\rho_W$ from the filtered signal

**Verdict: INCORRECT as a general statement (heuristic at best).**

Formula (12) was derived under the specific structural assumption that $\hat f(z)=\sigma/(1-\rho z^{-1})$, i.e. $f$ is **AR(1)**. The key reduction (eq. 9) uses the single pole at $z=\rho$ inside the unit disk to convert the partial-fraction tail back into $z/(z-\rho)=\hat f(z)\sqrt{1-\rho^2}/\sigma$ (up to constant). If one replaces $\hat f$ by a filtered process $\hat f^W$ whose transfer function has *both* a pole and a zero (the causal Wiener filter for AR(1)+white-noise is ARMA(1,1), with pole at $\rho$ and a zero $\lambda_W\ne 0$), the analogous calculation of $[\hat f^W/\hat K_-]_+$ does **not** collapse to a scalar multiple of $\hat f^W$.

Concretely, write $\hat f^W(z) = \alpha (1-\lambda_W z^{-1})/(1-\rho z^{-1})$. Then
$$\hat f^W(z)/\hat K_-(z) = \alpha(1-\lambda_W z^{-1})(1-\lambda z)/[\sqrt{1-\lambda^2}(1-\rho z^{-1})],$$
which expands into a $z$-polynomial plus a causal tail; the causal projection retains the *constant*, the *causal pole* at $\rho$, **and** a term proportional to $z^{-1}\lambda\lambda_W$ from the cross-product. The resulting causal part is no longer proportional to $\hat f^W(z)$, so $\hat K_+^{-1}\cdot[\hat f^W/\hat K_-]_+$ is **not** of the form $c\cdot(\hat f^W_t-\lambda\hat f^W_{t-1})$. The "$\rho_W$" substitution is not justified.

What *is* true: the correct formula has the structure $\hat x(z)=\hat K_+^{-1}(z)\,[\hat f^W(z)/\hat K_-(z)]_+$ (eq. 20, which is fine), and for AR(1)+white-noise observation noise this can be worked out in closed form — but the answer is *not* obtained by substituting the autocorrelation of $\hat f^W$ into (12). The paper's own TODO ("derivation is standard but lengthy") implicitly acknowledges this gap.

**Severity:** **blocker** for §8.1 as written, and a presentational risk for the abstract/introduction sentence "first denoise via the Wiener filter, then apply the impact-adjusted causal rule" — the *operator structure* (20) is correct, but the *closed-form formula* (22) with $\rho_W$ inserted into the AR(1) constant is not. Either:
* (a) derive the actual ARMA-input closed form (a short partial-fractions exercise, not just a substitution), or
* (b) demote (22) to a clearly labeled heuristic / leading-order approximation and not present it as the result.

---

## Summary

| # | Section | Verdict | Severity |
|---|---|---|---|
| 1 | §2.2–2.3 symmetrisation | AMBIGUOUS | minor (convention note) |
| 2 | §3 Legendre–Fenchel | VERIFIED | — |
| 3 | §4.1 W–H derivation steps (4)–(5) | AMBIGUOUS (final (6) correct) | blocker for clarity |
| 4 | §5.1 spectral factors | VERIFIED | — |
| 5 | §5.2 partial fractions | VERIFIED | — |
| 6 | §5.3 anticausality of $-\lambda z$ | VERIFIED | — |
| 7 | §5.4 limit checks | INCORRECT (algebra) | blocker for credibility |
| 8 | §6.2 power-law exponent | VERIFIED w/ caveat | minor (definitional note) |
| 9 | §7.3 separation principle | VERIFIED | — |
| 10 | §8.1 eq. (22) with $\rho_W$ | INCORRECT | **blocker** |

**Blockers to address before the next round:**
1. §8.1 eq. (22): not a valid consequence of (12); either compute the ARMA case properly or demote to heuristic.
2. §5.4 limit-case constants: three of the four stated limits are algebraically wrong; the master formula (12) is fine but the verification text contradicts it.
3. §4.1 eqs. (4)–(5): displayed derivation does not justify the (correct) boxed (6); replace with the two-line projection-FOC argument.

**Minor notes:**
- §2.2→§2.3: half-impact convention should be stated.
- §6.2: clarify that for $\beta\in(0,1)$ the symmetric kernel is a positive-definite distribution, not an $\ell^1$ sequence.
