# Round 1 Review — `papers/noisy-signal-impact-trading.md`

Scope: scope discipline, internal consistency, exposition clarity, brief adherence.
Mode: **review-only, no edits applied.**

Note on inputs: the task pointed at `plan.md` and `progress.md` in the repo root; neither exists. The plan was read from `outputs/.plans/noisy-signal-impact-trading.md` as instructed in the task body. No `progress.md` was written (review-only).

---

## 1. Brief coverage (a)–(h)

| Brief item | Where covered | Verdict |
|---|---|---|
| (a) noisy predictor of return-on-trade (not position) | §2.2 explicitly distinguishes "return on trade, not on position"; §7 adds noise model $\tilde f = f + \eta$ | **Covered** |
| (b) persistent impact with general kernel | §2.1 propagator model, §2.4 PD assumption, general $K$ throughout §3–§4 | **Covered** |
| (c) stationary policy | §2.3 stationary causal filter ansatz; §1 explicit "infinite-horizon stationary" | **Covered** |
| (d) Legendre–Fenchel of quadratic cost → two norms | §3.1–§3.2; the two-norms interpretation is stated explicitly | **Covered** |
| (e) Wiener–Hopf on cost kernel | §4 (Wiener–Hopf factorisation of $K$, eq (6)) | **Covered** |
| (f) anticausal factor on AR(1) → constant in autocorrelation | §5, eq (10) gives the scalar $(1-\lambda\rho)/\sqrt{1-\lambda^2}$ | **Covered** (but see §2 below on the "constant depends on autocorrelation" subtlety — the constant depends on *both* $\rho$ and $\lambda$, which matches the brief's "constant depending on autocorrelation") |
| (g) causal fractional derivative = kernel innovation | §6.1 (exp kernel) and §6.2 (power-law → fractional derivative of order $(1-\beta)/2$) | **Covered** |
| (h) Wiener-filter the noisy predictor first | §7, esp. §7.3 separation principle and eq (20) | **Covered** |

All eight requested elements are present. (a) and (h) are the deepest novelty-claim items and are treated at appropriate depth.

---

## 2. Internal consistency — §5.4 limit cases (**BLOCKER**)

Equation (12): $x_t = \dfrac{1-\lambda\rho}{1-\lambda^2}(f_t - \lambda f_{t-1})$.

Direct substitution of the bullets in §5.4:

- $\lambda \to 0$: prefactor $= 1$, $x_t \to f_t$. ✓ matches text.
- $\rho \to 0$: prefactor $= \dfrac{1}{1-\lambda^2}$, **not** $\dfrac{1}{1+\lambda}$ as the paper claims. (At $\lambda=0.3$: 1.099 vs 0.769.) ✗
- $\rho \to \lambda$: prefactor $= \dfrac{1-\lambda^2}{1-\lambda^2} = 1$, **not** $\dfrac{1}{1+\lambda}$. ✗ Both bullets show the same (wrong) formula.
- Parenthetical "scalar $c$ reaches $(1-\lambda^2)^{-1/2}$ at $\rho=1$": actual value $\dfrac{1-\lambda}{1-\lambda^2} = \dfrac{1}{1+\lambda}$. The factor $(1-\lambda^2)^{-1/2}$ matches only the *anticausal scalar* in eq (10), not the full prefactor in eq (12). The paper is conflating §5.3's intermediate result with the final §5.4 prefactor. ✗

**Classification:** BLOCKER — three independent arithmetic errors in the keystone "limit cases" bullet, all in the section that the paper itself frames as the headline result. Equation (12) and §5.2/§5.3 derivations are correct; the bug is localised to the §5.4 limits bullet only.

---

## 3. Tentative / unsupported claims

- **§8.1 inline TODO + half-formula** ("$\lambda_W = \rho - \sigma^2/\sigma_\eta^2 \cdot (...)$ ... *TODO: state closed-form Wiener filter pole...*"). The TODO is flagged, but the surrounding sentence still asserts a partial formula that is itself not derived and not obviously correct. The expression `(...)` left in the formula is unprofessional for a "first complete draft." **FIX-NOW** — either complete the derivation or remove the half-formula and defer the result entirely to §10 (limitations) as an open computation.
- **Eq (22) substitution "$\rho_W$ = autocorrelation of filtered signal"**: stated as if exact, but the Wiener-filtered AR(1)+noise signal is **not itself AR(1)** in general (its spectrum is rational of higher order), so plugging $\rho_W$ into the AR(1)-derived formula (12) is a heuristic, not an exact identity. The paper does not flag this. **FIX-NOW** — add a one-line "heuristic substitution; exact form requires re-solving Wiener–Hopf for the filtered spectrum" caveat.
- **GP "aim-and-trade" limit**: §10 item 7 flags it as "tentative." §9 paragraph 1 does **not**: it says "Their 'aim-and-trade' strategy ... is the special case of (12) when the risk-aversion term is included." But the present paper has no risk-aversion term, so this is at best speculative. The two sections disagree on epistemic status. **FIX-NOW** — soften §9 sentence (e.g., "we conjecture / appears to be") so §9 and §10 agree.
- **§7.3 "Proof sketch"**: the certainty-equivalence appeal is correct for Gaussian linear-quadratic problems, but the sketch glosses over the fact that the LQ separation theorem requires the cost to be quadratic in the *state being estimated*, not just in the control. With propagator cost, the state being estimated is $f$ and the control is $x$, so it does go through; still, citing Kailath (1968) or analogous would strengthen this from "sketch" to a defensible result. **OPTIONAL**.

---

## 4. Figures and provenance

- Plan §"Figures and Calculations" labelled Fig 1 / Fig 2 as Mermaid diagrams and explicitly noted "may or may not materially help."
- The brief does not require figures.
- Paper has Table 1 (§8.3), which is content-bearing and consistent with the plan.
- **No provenance violation**: no quantitative plots or data figures are claimed, so there is nothing to source-back. **OK as is.**

---

## 5. Sources appendix

Every primary peer-reviewed/preprint reference has a working-looking direct URL (DOI, arXiv, SSRN, or publisher page). Books (Wiener 1949, Samko–Kilbas–Marichev 1993) have no URL, which is standard for monographs. Almgren–Chriss URL `www.risk.net/journal-of-risk/1506832/...` is a generic redirect that may be stale but is the canonical Risk.net link. **OK** — no blockers.

---

## 6. Abstract

The abstract covers: stationary setting ✓, propagator/general $K$ ✓, LF duality + two norms ✓, Wiener–Hopf factorisation ✓, AR(1) + exponential scalar result ✓, kernel-innovation interpretation ✓, power-law → fractional derivative ✓, noisy signal + two-stage Wiener prefilter ✓, separation principle under Gaussian linearity ✓. **Accurate and complete.** No fix needed.

---

## 7. Section ordering and length

- §8 "Examples" is the weakest section.
  - §8.1 mostly recapitulates §5 + §7 plus the broken `(...)` formula.
  - §8.2 (power-law + OU) **does** add a continuous-time fractional-derivative example that §6.2 only sketches in discrete time, and the $\beta=0$ ill-posedness note is useful.
  - §8.3 (Table 1) is the most valuable item in §8.
- **Recommendation (OPTIONAL):** collapse §8.1 to a one-paragraph cross-reference to §5+§7 and promote Table 1 to either §6 or §8 standalone. Not a blocker.
- §6.2 closing paragraph ("The AR(1) anticausal projection analysis from §5 extends analogously...") is hand-wavy. **NOTE / DEFER** — flagged in §10 item 5 already.

Other ordering: §1 → §11 flow is clean. Length is appropriate for a "note."

---

## 8. Markdown / LaTeX

- `\boxed{...}` in eq (6) and eq (12): braces balanced, render-safe.
- Eq (4)–(5) cluster is **muddled but not broken**: eq (5) is $\hat H = \frac{1}{\hat K}\cdot\frac{[\hat f/\hat K_-]_+}{\hat f}$, which divides the causal projection by $\hat f$ — this is not the standard Wiener–Hopf form for $\hat H$ and the role of $S_f$ that appears in eq (4) is dropped without comment. Eq (6) is the correct statement (as a relation between $\hat x$ and $\hat f$, not $\hat H$). Recommend dropping eq (5) or rederiving it cleanly. **FIX-NOW** (clarity, not arithmetic).
- Eq (8) partial-fraction is correct (verified by hand: $(-\lambda z + 1-\lambda\rho)(z-\rho) + \rho(1-\lambda\rho) = -\lambda z^2 + (1-\lambda\rho)z + \lambda\rho z - \rho(1-\lambda\rho) + \rho(1-\lambda\rho) = -\lambda z^2 + z$ ✓).
- Eq (9): $(1-\lambda\rho)(1 + \rho/(z-\rho)) = (1-\lambda\rho)\cdot z/(z-\rho)$ ✓.
- Eq (15) causal fractional derivative: dimensions and Gamma factor consistent with Samko et al. ✓.
- No broken `$`, no stray `\\`, no malformed tables.

---

## Summary

| # | Finding | Class |
|---|---|---|
| 1 | §5.4 "Limit cases" bullets give wrong prefactors for $\rho\to0$, $\rho\to\lambda$, and $\rho=1$; contradicts eq (12) | **BLOCKER** |
| 2 | §8.1 inline `(...)` half-formula for $\lambda_W$ under a "first complete draft" header | **FIX-NOW** |
| 3 | Eq (22) substitution $\rho_W$ presented as exact; actually heuristic (filtered AR(1) is not AR(1)) | **FIX-NOW** |
| 4 | §9 paragraph 1 asserts GP limit non-tentatively, contradicting §10 item 7 | **FIX-NOW** |
| 5 | Eq (5) divides causal projection by $\hat f$; muddled / probably redundant given eq (6) | **FIX-NOW** |
| 6 | §7.3 separation proof sketch could cite Kailath/Wiener for certainty equivalence | OPTIONAL |
| 7 | §8.1 largely recaps §5+§7; consider collapsing | OPTIONAL |
| 8 | §6.2 closing paragraph on "AR(1) analysis extends analogously" is hand-wavy (acknowledged in §10) | DEFER |
| 9 | Brief items (a)–(h) all covered; abstract accurate; sources OK; no figure/provenance issues | Correct |
| 10 | Eqs (7)–(12), (15), Table 1: algebra verified | Correct |

Recommendation: address items 1–5 before circulating. Item 1 alone undermines the headline §5 result's credibility even though eq (12) itself is right.
