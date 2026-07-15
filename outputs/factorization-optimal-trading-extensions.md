# Extensions memo — "Optimal Trading Against a Signal: a Wiener–Hopf Approach"

**Artifact:** `tex/factorization-optimal-trading.tex` (post-review revision of 2026-07-14)
**Date:** 2026-07-14
**Purpose:** candidate extensions that deepen the paper's mathematical content, ranked by (payoff ÷ effort), with derivation sketches, verification status, and recommended sequencing.
**Provenance:** hand derivations this session; numerical validation in `experiments/extension_response_check.py` (new) and `experiments/review_factorization_check.py` (review session). Every quantitative claim below is tagged Derived / Validated / Conjectured.

---

## A. The second factorization: innovations filter, exact adapted value, and the cost of causality

**Status: derived this session; OU case checked analytically against the paper's own formulas. Recommended for inclusion in the current draft.**

The paper factorizes the cost operator; the signal admits a factorization of its own. For a stationary Gaussian signal with spectral density $S_\alpha = |\varphi_+|^2$ ($\varphi_+$ the canonical causal spectral factor, so $\alpha = \varphi_+(D)\dot W$ for the innovations $\dot W$), the whitening step of Theorem 1 becomes a Hardy-space projection:

$$\zeta = \Pi_+\!\bigl[\hat C_-^{-1}\varphi_+\bigr](D)\,\dot W,$$

with $\Pi_+$ the Riesz projection onto $H^2$ (causal part). The argument: $\hat C_-^{-1}\varphi_+ - \text{(causal part)}$ has its poles/singularities only in the analyticity region of the anticausal factor, so the forecast-replacement step of eq. (proj-cma) selects exactly the causal part. OU verification: $\bigl((i\xi)^\nu - \theta^\nu\bigr)/(\theta - i\xi)$ has the pole at $\xi = -i\theta$ cancelled, hence is anticausal; therefore $\Pi_+((i\xi)^\nu\varphi_+) = \theta^\nu\varphi_+$, recovering the paper's $\zeta_s = \theta^\nu\alpha_s$.

Three consequences, each a closed formula:

1. **Optimal trading filter.** $u^\star = \hat g(D)\dot W$ with transfer function
   $$\hat g(\xi) = \gamma^{-1}\,\hat C_+^{-1}(\xi)\,\Pi_+\!\bigl[\hat C_-^{-1}\varphi_+\bigr](\xi).$$
   The optimal rate is an explicit stationary linear filter of the signal innovations. Its spectrum $|\hat g|^2$ gives the autocorrelation and turnover of the optimal flow in closed form.
2. **Exact adapted value.**
   $$V_{\rm ad} = \frac{1}{4\pi\gamma}\bigl\|\Pi_+(\hat C_-^{-1}\varphi_+)\bigr\|_{L^2}^2, \qquad V_{\rm ant} - V_{\rm ad} = \frac{1}{4\pi\gamma}\bigl\|\Pi_-(\hat C_-^{-1}\varphi_+)\bigr\|_{L^2}^2.$$
   The causality gap is the anticausal remainder of the half-whitened spectral factor — an exact, frequency-resolved price of adaptedness. This upgrades the corrected §5.5 (which currently states only the anticipative upper bound) to a theorem. OU check: gap ratio $V_{\rm ad}/V_{\rm ant} = \sin(\pi\beta/2)$, matching the review-session computation.
3. **Limits.** As $\beta\to1$ (short-memory impact) the gap closes ($\sin\to1$): adaptedness costs nothing against near-local cost. As $\beta\to0$ (near-permanent impact) $V_{\rm ad}/V_{\rm ant}\to0$: causality destroys almost all value. Both follow from the OU formula; the general-kernel statement is Conjectured.

This closes the circle with Wiener 1949: the paper's three-step operator is the Wiener–Kolmogorov filter with the cost factor in place of the process spectral root, and extension A makes that identification computational rather than analogical.

**Effort:** low (all machinery exists in the paper). **Risk:** low.

---

## B. The signal-speed response function and the contrarian dichotomy

**Status: derived and numerically validated this session (sub-percent at refined dt). Recommended for inclusion in the current draft; upgrades §5.1 from two examples to a theorem.**

For an OU signal with mean-reversion rate $\theta$, define the forward (execution-relevant) response $R(\theta) := \lim_{\Delta\to0}\E[x_{t+\Delta}-x_t\mid\alpha_t]/(\Delta\,\alpha_t)$. Two exact statements:

1. **Inner step (any admissible kernel).** $\zeta_s = \rho(\theta)\,\alpha_s$ with $\rho(\theta) = 1/\hat C_-(-i\theta)$ — the Laplace evaluation of the anticausal factor at the forecast decay rate. Checked against both kernels in the paper.
2. **Response formula.** Via the innovations filter of extension A, subtracting the $q=0$ atom (the loading on the contemporaneous innovation, which forward conditioning excludes):
   $$R(\theta) = \frac{\rho(\theta)}{\gamma}\Bigl[\frac{1}{\hat C_+(i\theta)} - 2c_1\theta\Bigr], \qquad c_1 = \lim_{\xi\to\infty}\frac{1}{-i\xi\,\hat C_+(\xi)}.$$

Checks (all in `experiments/extension_response_check.py`):
- Single exponential: reduces to $(\kappa^2-\theta^2)/2\kappa\gamma$ — the paper's eq. (exp-ou). Numerics: pred +0.75/−1.25, measured +0.72/−1.11 (O(dt·θ) bias).
- Power law: $c_1 = 0$, reduces to $\theta^{1-\beta}/c_\beta\gamma$ — the paper's eq. (ou).
- Two-exponential mixture ($\kappa_1{=}1,\kappa_2{=}4$, equal weights): predicted flip at $\theta^* = 2.5616$; measured single flip between 1.5 and 3; at $\theta=3$ predicted −0.4480 vs dt-refined measurement **−0.4479**.

**Refuted along the way:** the naive rational continuation $R = 1/\gamma\hat C(i\theta)$ (coincidentally correct for one exponential) predicts reentrant contrarian windows for mixtures; the numerics reject it decisively. The refutation and the correct formula are both recorded in the script.

**The dichotomy.** As $\theta\to\infty$, $1/\hat C_+(i\theta)\sim c_1\theta$, so the bracket $\sim -c_1\theta$:
- $c_1 > 0$ (kernels with $\hat C\sim\xi^{-2}$ tails — exponentials and finite mixtures, i.e. kernels with a kink at 0): every sufficiently fast signal is traded **contrarian**, with a single threshold $\theta^*$ (for two-exponential mixtures, $\theta^*$ solves $\theta^2 + (2\mu-\kappa_1-\kappa_2)\theta - \kappa_1\kappa_2 = 0$).
- $c_1 = 0$ (power-law cusp at 0, $\hat C\sim|\xi|^{\beta-1}$): $R(\theta) = \rho/\gamma\hat C_+(i\theta) > 0$ for all $\theta$ — **no contrarian regime at any signal speed**.

The high-frequency singularity structure of the kernel at lag 0 governs whether fast signals are traded with or against. A subtlety worth a remark in the paper: the contemporaneous-conditioning convention gives $R_{\rm bwd} = 1/[\gamma\hat C_+(i\theta)\hat C_-(-i\theta)] > 0$ always (validated numerically); the sign flip is a statement about forward, execution-relevant conditioning, and the distinction is exactly the white-noise content of $u^\star$ flagged in §5.1.

**Effort:** low–medium (general-kernel proof of the atom subtraction needs care for non-rational symbols with $c_1>0$; the $c_1=0$ class is already rigorous via the Marchaud representation). **Risk:** low.

---

## C. Equivalence with the Abi Jaber–Neuman stochastic Fredholm resolvent

**Status: conjectured, with a clear proof route.**

Abi Jaber–Neuman (arXiv:2211.00447, Math. Finance 2025) characterize $u^\star$ as the solution of a linear stochastic Fredholm/Volterra equation of the second kind. The target theorem: the operator $\gamma^{-1}C_+^{-1}P_+C_-^{-1}$ is the explicit resolvent of that equation, i.e. substituting the paper's closed form into their fixed-point equation verifies it identically, and for the power-law kernel their abstract resolvent kernel equals the fractional-derivative composition. Proof route: their FOC coincides with eq. (foc); uniqueness on the common domain then forces equality; the content is translating between their $L^2([0,T])$-valued-process formulation and the paper's $L^2(\Omega\times[0,T])$ projected-operator formulation. Payoff: the contribution claim ("closed form for what was previously implicit") becomes a theorem rather than a comparison, and referees from that school get a bridge. **Effort:** medium. **Risk:** low (both objects solve the same strictly convex problem).

## D. Rough signals: the roughness–memory frontier

**Status: conjectured; machinery from A applies directly.**

For fractional-OU signals with Hurst $H$ (spectral factor $\varphi_+\sim(\theta-i\xi)^{-H-1/2}$-type), extension A's value formula converges iff the integral $\int|\xi|^{1-\beta}S_\alpha(\xi)\,d\xi$ does at high frequency, giving a finiteness frontier coupling signal roughness to impact memory: rougher signals (smaller $H$) require longer-memory impact (smaller $\beta$) for finite anticipative value, with the adapted value finite on a larger region (the projection regularizes). Deliverables: the frontier $H^*(\beta)$, the optimal filter for Riemann–Liouville signals (compare FSS §3.1, who compute the finite-horizon analog by Mathematica), and the behavior at the Jusselin–Rosenbaum no-arbitrage exponent relation. **Effort:** medium. **Risk:** medium (nonstationarity of RL signals needs the finite-interval, not whole-line, machinery). Candidate companion paper.

## E. Energy-space rigor

**Status: planned; required for a strong journal referee pass.**

Reformulate Lemma 1 and Theorem 1 on the completion of adapted processes under $\E\|u\|_C^2$ (the adapted subspace of the $\dot H^{-\nu}$-valued Gaussian-field dual used by FSS), replacing the standing spectral hypothesis of §2.1 by membership of $\alpha$ in the dual energy space. All operators in the projected-inverse identity become isomorphisms between the energy scale and its dual; the $\eta\to0$ temporary-impact limit becomes a statement about Mosco convergence of quadratic forms. **Effort:** medium–high. **Risk:** low (standard techniques; FSS Appendix has the function-space groundwork).

## F. Gain–risk–cost worked out: the three-regime filter

**Status: conjectured; §5.6 currently states only that the machinery applies.**

The joint symbol $\gamma c_\beta|\xi|^{\beta-1} + \eta + \lambda\Sigma/\xi^2$ has two crossover frequencies separating position-targeting (low $\xi$, risk-dominated), fractional trading (middle), and myopic signal-following (high $\xi$, temporary-impact-dominated). Factorization of the three-term symbol is non-rational but its asymptotics in each regime are computable, and the OU response function of extension B evaluates in closed form through $\rho(\theta)$ and $\hat C_+(i\theta)$ for the combined symbol. Deliverable: the three-regime optimal filter with matched asymptotics, and the risk-induced modification of the contrarian threshold. **Effort:** medium. **Risk:** medium. Candidate companion paper or long section.

## G. Kernel misspecification robustness

**Status: derivation route clear; low effort.**

By the envelope theorem the value loss from trading with a misspecified $\hat\beta \ne \beta$ is second order: $V(\beta) - V(\hat\beta;\beta) = \tfrac12 Q(\beta)(\hat\beta-\beta)^2 + O((\hat\beta-\beta)^3)$, with $Q$ computable from extension A's value formula by differentiating the filter (the first-order term vanishes at the optimum). For OU the coefficient $Q$ is an explicit integral. Same analysis for misspecified $\theta$. Practical payoff: quantifies how precisely $\beta$ (empirically $0.2$–$0.6$) must be estimated before estimation error dominates the causality gap. **Effort:** low. **Risk:** low. Fits as a short subsection of §5.4.

## H. Two-asset lead-lag cross-impact via matrix Wiener–Hopf

**Status: exploratory.**

Non-symmetric cross-impact with a lead-lag (odd-in-time) component gives a non-Hermitian $2\times2$ matrix symbol. The Daniele–Khrapkov class (symbols of the form $a(\xi)I + b(\xi)J$ with $J^2 = \Delta^2 I$) admits explicit factorization and plausibly covers the two-asset lead-lag parameterization; partial indices control existence, consistent with the corrected §5.3 remark. Payoff: the closed-form optimal pair-trading rate under asymmetric cross-impact, a phenomenon (lead-lag arbitrage under impact) with no current closed form. **Effort:** high. **Risk:** high. Separate paper.

## Discussion-level addition: the spectrum of optimal flow

From extension A, $S_{u^\star}(\xi) = |\hat g(\xi)|^2$. For any signal with finite spectral mass at $\xi=0$, the power-law-kernel optimal flow spectrum vanishes as $|\xi|^{1-\beta}$ at low frequency: cost-optimal flow is anti-persistent at long horizons, in tension with the long-range persistence of empirical order flow. The reconciliation (empirical flow aggregates metaorder splitting across agents rather than single-agent optimality) deserves one paragraph and connects to Jusselin–Rosenbaum. **Effort:** trivial (one derivation, one paragraph).

---

## Recommended sequencing

| Ext. | Action | Rationale |
|---|---|---|
| A | Fold into current draft (new §5 or expanded §5.5) | Derived; upgrades two discussion claims to theorems; fixes the weakest sections found in review (M1/M2) at their root |
| B | Fold into current draft (upgrade §5.1) | Derived + validated; adds a new phenomenon (contrarian dichotomy, threshold formula) at low cost |
| G | Short subsection of §5.4 | Low effort, practitioner-relevant |
| flow spectrum | One paragraph in §5.5 | Trivial given A |
| C, E | Journal-version rigor pass | Referee-proofing; no new phenomena |
| D, F | Companion papers | Real scope; each has its own arc |
| H | Exploratory notebook first | High risk; test Khrapkov applicability before committing |

## Verification ledger

| Claim | Status | Provenance |
|---|---|---|
| $\Pi_+((i\xi)^\nu\varphi_+^{\rm OU}) = \theta^\nu\varphi_+$ | Derived (pole-cancellation) | this memo, §A |
| $V_{\rm ad}/V_{\rm ant} = \sin(\pi\beta/2)$ (OU) | Derived | review session, hand computation |
| $\rho(\theta) = 1/\hat C_-(-i\theta)$ | Derived; checked both kernels | this memo, §B |
| $R(\theta) = \gamma^{-1}\rho\,[1/\hat C_+(i\theta) - 2c_1\theta]$ | Derived + **numerically validated** (mixture θ=3: −0.4480 vs −0.4479) | `experiments/extension_response_check.py` |
| $R = 1/\gamma\hat C(i\theta)$ (rational continuation) | **Refuted** (mixture numerics) | same script |
| Contrarian dichotomy ($c_1>0$ vs $c_1=0$) | Derived from the validated formula; general-kernel proof pending | this memo, §B |
| C, D, E, F, G, H formulas | Conjectured / planned | not run |

## Sources

- `tex/factorization-optimal-trading.tex` (current draft)
- `experiments/extension_response_check.py`, `experiments/review_factorization_check.py` (this project)
- Forde, Sánchez-Betancourt, Smith, Quant. Finance 22(3), 2022. https://doi.org/10.1080/14697688.2021.1950919
- Abi Jaber, Neuman, "Optimal liquidation with signals: the general propagator case", arXiv:2211.00447. https://arxiv.org/abs/2211.00447
- Jusselin, Rosenbaum, Math. Finance 30, 2020 (no-arbitrage and power-law impact exponents)
- Wiener, *Extrapolation, Interpolation and Smoothing of Stationary Time Series*, MIT Press, 1949
- Daniele–Khrapkov matrix Wiener–Hopf class: Khrapkov, PMM 35 (1971); Daniele, IEEE Trans. AP 26 (1978) — to be re-verified before use in H
