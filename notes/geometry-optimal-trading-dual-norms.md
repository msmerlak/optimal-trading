# The geometry of optimal trading: pairing, metric, flag

**Status:** internal research note, 2026-07-14. Companion to `tex/factorization-optimal-trading.tex` and `outputs/factorization-optimal-trading-extensions.md`. Candidate backbone for the Markowitz-of-cost companion (`papers/markowitz-of-cost.md`).
**Verification convention:** every displayed claim is tagged [derived], [checked] (hand-verified against a known special case), [validated] (numerical experiment), or [open].

---

## 1. Three primitives

The trading problem with risk and impact frictions is built from three independent objects.

**Pairing.** The P&L bilinear form
$$\langle u,\alpha\rangle \;=\; \E\!\int u_t\,\alpha_t\,dt$$
pairs trades (vectors) with signals (covectors). It is friction-free and model-free.

**Metric.** Frictions define a quadratic form on trades. With transient impact and quadratic position risk,
$$\|u\|_Q^2 \;=\; \gamma\,\E\langle u,Cu\rangle \;+\; \lambda\,\E\!\int x_t^2\,dt,
\qquad x={\textstyle\int}u,
\qquad q(\xi) \;=\; \gamma c_\beta|\xi|^{\beta-1} + \frac{\lambda}{\xi^2}.$$
The trade space $H_T$ is the completion of rates under $\|\cdot\|_Q$; for the rate this is $\dot H^{-\nu}\cap\dot H^{-1}$-type, $\nu=(1-\beta)/2$. The dual space $H_S$ of signals carries the tradeability norm $\|\alpha\|_*^2 = \E\langle\alpha,Q^{-1}\alpha\rangle$ with spectral weight $1/q(\xi)$. The unit balls $B_Q$ and $B_{Q^{-1}}$ are polar ellipsoids under the pairing. [derived; standard]

**Flag.** Adaptedness: the closed subspace $L^2_{\rm adap}\subset L^2(\Omega\times\R)$, and on $[0,T]$ the continuous nest $\{P_{[0,t]}\}$ behind it. The flag is metric-independent; all information structure lives here.

*Terminology.* "Flag" (finite chains of subspaces, linear algebra and Lie theory), "nest" (totally ordered complete families of closed subspaces, Ringrose 1965; Arveson 1975; Davidson, *Nest Algebras*, 1988), and "chain" (of orthoprojectors, Gohberg--Krein 1970) name the same structure in different communities. This note says flag for the finite-dimensional intuition; the paper and its citations say nest, which is the correct term for the continuous Hilbert-space setting.

The anticipative problem is pure metric duality: $v_{\rm ant}=\tfrac12\|\alpha\|_*^2$, attained by the Riesz map $u^\star = Q^{-1}\alpha$. The content of the factorization paper is the interaction of metric with flag.

## 2. Risk + impact in the dual: infimal convolution

The primal form is a sum $Q=A+B$ (impact + risk). The dual form is the infimal convolution (parallel sum):
$$\|\alpha\|_{Q^{-1}}^2 \;=\; \min_{\alpha_1+\alpha_2=\alpha}\;\|\alpha_1\|_{A^{-1}}^2+\|\alpha_2\|_{B^{-1}}^2 .$$
*Proof.* First-order condition $A^{-1}\alpha_1 = B^{-1}\alpha_2 =: z$; then $\alpha=(A+B)z$, and the objective equals $\langle z,(A+B)z\rangle = \langle\alpha,(A+B)^{-1}\alpha\rangle$. [derived]

The minimizer satisfies $z=u^\star$: the optimal split $\alpha_1 = Au^\star$, $\alpha_2 = Bu^\star$ equalizes the marginal trade across frictions. The signal is partitioned into a component monetized against impact and a component monetized against risk. In frequency the partition follows the crossover
$$\xi_c = (\lambda/\gamma c_\beta)^{1/(1+\beta)}$$
(risk dominates $q$ below $\xi_c$, impact above). [derived]

Two features of the dual weight $1/q$:

- $1/q(\xi)\sim\xi^2/\lambda$ as $\xi\to0$: a DC forecast is a null direction of the tradeability norm. Under position risk the signal space is a quotient modulo constants; a permanent expected-price-change level has zero value rate. [derived]
- $1/q(\xi)\sim|\xi|^{1-\beta}/\gamma c_\beta$ as $\xi\to\infty$: fast signals are the valuable ones, without bound until a temporary-impact term $\eta$ saturates the weight at $1/\eta$ above $\xi_* = (\gamma c_\beta/\eta)^{1/(1-\beta)}$. [derived]

## 3. Adaptedness is the same algebra

Conjugating the constrained problem:
$$\Bigl(\tfrac12\|\cdot\|_Q^2+\iota_{L^2_{\rm adap}}\Bigr)^{*}(\alpha)
\;=\; \min_{n\in N}\;\tfrac12\|\alpha-n\|_{Q^{-1}}^2,
\qquad N=(L^2_{\rm adap})^{\perp}=\{n:\E_t[n_t]=0\ \text{a.e.}\},$$
by the standard identity $(F+\iota_V)^* = F^*\,\square\,\iota_{V^\perp}$. The adapted value is a squared distance in the dual from $\alpha$ to the annihilator of adapted trades. [derived]

Both dual-side structures are therefore infimal convolutions: risk/impact convolves over signal splits; adaptedness convolves over annihilator shifts. The trader may replace $\alpha$ by any $\alpha-n$ invisible to adapted strategies and takes the cheapest representative in the tradeability norm.

## 4. The factorization, geometrically

Any square root $Q=S^*S$ gives an isometry $(H_S,\|\cdot\|_*)\to L^2$ via $(S^*)^{-1}$. The causal--anticausal factorization $Q=C_-C_+$ is the choice, unique up to a diagonal phase, whose isometry fixes the annihilator:
$$C_-^{-1}N \;=\; N,$$
equivalent to $P_+C_-^{-1}P_+^\perp=0$ from Lemma 1 of the draft. With $N$ fixed, the dual distance reduces to a conditional expectation:
$$v_{\rm ad} \;=\; \tfrac12\,\mathrm{dist}_*^2(\alpha,N) \;=\; \tfrac12\bigl\|P_+C_-^{-1}\alpha\bigr\|_{L^2}^2 .$$
[derived; consistent with the validated Lemma 1 numerics in `experiments/review_factorization_check.py`]

Finite-dimensional reading: flag-compatible Cholesky, i.e. Gram–Schmidt of the friction metric with respect to the causal flag; Arveson's outer factorization is the continuous-nest version. The solution method is: straighten the metric and the flag simultaneously, then project.

*Iwasawa aside.* The precise group-theoretic statement behind "flag-compatible Cholesky": metrics form the symmetric space $\mathcal P = GL(n)/O(n)$ via $Q = g^*g$, and the Iwasawa decomposition $GL(n) = O(n)\cdot AN$ says the triangular (Borel) group $AN$ acts simply transitively on $\mathcal P$ — every metric has exactly one triangular square root relative to a chosen flag. The generic square root's rotation ambiguity ($K$ factor) is spent on triangularity, leaving diagonal phases: the uniqueness clause of Prop.~2. Arveson's theorem is the nest-indexed version (causal group acting transitively on positive invertible operators). One level up, matrix Wiener--Hopf is Birkhoff factorization of loop groups, with partial indices labelling the non-generic Birkhoff cells (Pressley--Segal, *Loop Groups*, 1986) — the obstruction relevant to the two-asset lead-lag extension. Untested speculation, recorded for completeness: kernel families are curves in $\mathcal P$; whether symmetric-space geodesics between kernels (e.g.\ exponential to power-law) induce anything meaningful on optimal filters is open. The finite-interval ordering error found in review (left- vs terminal-anchored factor) is, in this language, the statement that only one of the two flag-compatible triangularizations of $G_T$ fixes the annihilator of the *adapted* flag; the other fixes the reflected flag.

**Candidate lemma.** State $C_-^{-1}N=N$ as the defining property of the correct factor, replacing the operator identity as the primary formulation. This is sharper for the finite-interval case, where the reflection subtlety lives, and is the natural invariant statement for the nest-algebra setting. [open — to be written and proved against the $[0,T]$ case]

## 5. The causality gap is an angle

From the distance formula,
$$\frac{v_{\rm ad}}{v_{\rm ant}} \;=\; \cos^2\angle\bigl(C_-^{-1}\alpha,\;L^2_{\rm adap}\bigr).$$
For an OU signal under pure power-law impact the angle is a kernel–signal invariant, independent of $\theta$ and $\sigma$:
$$\cos^2\angle \;=\; \sin(\pi\beta/2).$$
[checked — hand computation, consistent with the $\sin(\pi\beta/2)$ value ratio in the draft's §5.5]

With risk added, $C_-$ changes and the angle becomes $\theta$-dependent through $\theta/\xi_c$. Computing $\angle(\theta/\xi_c)$ for the combined symbol is a closed-form exercise via the Szegő representation of the factors. [open]

## 6. The contrarian dichotomy as a unit-ball statement

The innovation atom in $u^\star$ (draft §5.1) exists iff white-noise rates have finite cost, i.e. iff $\int q\,d\xi<\infty$ iff $G$ is bounded at the origin. Contrarian trading of fast signals occurs exactly when the trade-space unit ball contains singular (white-noise) directions. [derived from the validated response formula; see `experiments/extension_response_check.py`]

## 7. Flow response vs position response under risk

The flow response $R(\theta)$ stops being the right alignment diagnostic once positions are penalized.

- **Pure risk** ($\gamma\to0$): $q=\lambda/\xi^2$, $\hat Q_+=\sqrt\lambda/(-i\xi)$, $c_1=\lambda^{-1/2}>0$, and the response formula gives $R(\theta)=-\theta^2/\lambda<0$ at every speed. Direct check: the adapted optimal position is $x_t=\theta\alpha_t/\lambda$ (Markowitz-per-instant, aligned with the signal), so the flow $u=\theta\dot\alpha/\lambda$ has forward conditional mean $-\theta^2\alpha_t/\lambda$ — the position mean-reverts, and the flow conditionally points toward the exit. Aligned position, contrarian-looking flow. [checked — both routes agree]
- **Power-law impact + risk:** $q\sim\gamma c_\beta|\xi|^{\beta-1}$ at high frequency gives $c_1=0$, so the derivation gives $R(\theta)=1/\gamma\Phi(\theta)^2>0$ at all speeds, with $R\approx\theta^2/\lambda$ for slow signals. The sign difference against the pure-risk limit is carried entirely by the vanishing atom; the $\gamma\to0$ limit is non-uniform. [derived; **not yet numerically validated** — same failure mode the mixture experiment caught for the naive response conjecture, so a discrete check is required before this enters any draft]

The geometric fix is to measure alignment against a second covector: define a position response alongside the flow response. [open]

## 8. Next steps

1. Numerical check of the combined-kernel response sign: extend `experiments/extension_response_check.py` with a $\lambda/\xi^2$ term (discrete: add $\lambda\,L^\top L$ with $L$ the cumulative-sum matrix to the cost quadratic form). Cheap; decisive for §7.
2. Closed-form causality angle $\angle(\theta/\xi_c)$ for the risk+impact symbol via the Szegő formula. One session.
3. Write the $C_-^{-1}N=N$ lemma and re-derive the finite-interval factor choice from it; this subsumes the review's C1 fix into a positive statement.
4. If the Markowitz-of-cost companion proceeds, adopt §§1–4 here as its organizing frame: Markowitz is the flag-free special case ($N=\{0\}$); the execution literature is a catalogue of metrics against a fixed pairing and flag.

## Sources

- `tex/factorization-optimal-trading.tex` (current draft: Lemma 1, §5.1 response function, §5.5 innovations/value, §5.6 gain–risk–cost symbol)
- `outputs/factorization-optimal-trading-extensions.md` (extensions memo; derivations for the response formula and value)
- `experiments/review_factorization_check.py` (Lemma 1 order validation; finite-interval factor)
- `experiments/extension_response_check.py` (response formula validation; refuted naive continuation)
- `papers/markowitz-of-cost.md` (companion draft this geometry would organize)
- Arveson, "Interpolation problems in nest algebras", J. Funct. Anal. 20 (1975) — outer factorization on a nest
- Rockafellar, *Convex Analysis*, Princeton (1970) — conjugate of a sum, infimal convolution, $(F+\iota_V)^*$ calculus
