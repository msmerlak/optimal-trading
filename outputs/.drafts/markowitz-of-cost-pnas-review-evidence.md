# Evidence Notes — markowitz-of-cost-pnas

Direct inspection of `papers/markowitz-of-cost-pnas.md`. Word count: 4281.

## Word-count / format checks

- Significance statement: ~119 content words. **PNAS cap 120**: within limit (tight).
- Abstract: ~230 content words. **PNAS cap 250**: within limit.
- No equations in abstract. ✓
- No equations in significance. ✓
- Section headers correct order (Significance → Abstract → Intro → Body → Discussion → Materials & Methods → References). ✓
- Data availability line present. ✓
- Author/classification TBD marked. Expected at submission.

## Equations tagged 1–15. Cross-references checked:

- §3.2 cites (11) [Adapted inverse identity]: correct.
- §3.2 cites (13) [$\zeta_s$ definition]: correct.
- §2.7 uses equation (14) internally, and §3.2 references "(14)" — but there is ambiguity: (14) is used both for OU identity in-text and for reference [14] (Wiener book) in §3.2's "(14)". §3.2's "(14)" is the *reference* to Wiener's 1949 book. Potential reader confusion but format-standard.
- §4.2 cites (12) [bulk theorem statement]: correct.
- Symbol identity in proof of Thm 1 step (c): $\hat C(\xi)(i\xi)^\nu = c_\beta(-i\xi)^{-\nu}$. Dimensionally consistent: $|\xi|^{\beta-1} = |\xi|^{-2\nu}$, and $|\xi|^{-2\nu} = (i\xi)^{-\nu}(-i\xi)^{-\nu}$, so LHS = $c_\beta(-i\xi)^{-\nu}$. ✓

## Constant $c_\beta$

Paper: $c_\beta = 2\Gamma(1-\beta)\sin(\pi\beta/2)$.

Verify: $\int_{-\infty}^\infty |t|^{-\beta}e^{-i\xi t}dt = 2\int_0^\infty t^{-\beta}\cos(\xi t)dt$. Using $\int_0^\infty t^{s-1}\cos(\xi t)dt = |\xi|^{-s}\Gamma(s)\cos(\pi s/2)$ with $s = 1-\beta$: $= 2|\xi|^{\beta-1}\Gamma(1-\beta)\cos(\pi(1-\beta)/2) = 2|\xi|^{\beta-1}\Gamma(1-\beta)\sin(\pi\beta/2)$. ✓ Constant correct.

## OU calculation (equation 14 in-text)

$(D_-^\nu\bar\alpha(t,\cdot))(t) \stackrel{?}{=} \theta^\nu\alpha_t$ with $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s\ge t$.

Marchaud: $D_-^\nu f(s) = \frac{\nu}{\Gamma(1-\nu)}\int_0^\infty\frac{f(s)-f(s+h)}{h^{\nu+1}}dh$.

At $s=t$: $\frac{\nu\alpha_t}{\Gamma(1-\nu)}\int_0^\infty\frac{1-e^{-\theta h}}{h^{\nu+1}}dh$.

The integral evaluates to $\theta^\nu\Gamma(1-\nu)/\nu$ (integration by parts). Product = $\theta^\nu\alpha_t$. ✓

## Fourier sign convention — CRITICAL

Paper eq. (9): $\hat C_\pm(\xi) = c_\beta^{1/2}(\pm i\xi)^{-\nu}$, "$\hat C_+$ analytic in upper half-plane, $\hat C_-$ in lower half-plane".

Paper eq. (10): $C_+ = c_\beta^{1/2}I_+^\nu$ with "$C_+$ causal (kernel supported on $\{s\le t\}$)".

Under Fourier convention $\hat f(\xi) = \int e^{-i\xi t}f(t)dt$ (Samko et al., ref 17, standard):
- Causal $I_+^\nu$ has Fourier symbol $(-i\xi)^{-\nu}$ (not $(+i\xi)^{-\nu}$).
- $(-i\xi)^{-\nu}$ with principal branch is analytic in $\{\text{Im}(\xi)>0\}$ = upper half-plane.

So under Samko's convention: $\hat C_+ = c_\beta^{1/2}(-i\xi)^{-\nu}$, analytic in upper HP, $C_+$ causal.

Paper's formula (9) $\hat C_+ = (+i\xi)^{-\nu}$ conflicts with either the analyticity claim or the causality claim. This is a **sign-convention bug** that a mathematically literate referee will catch.

Consequence in proof (step c): symbol identity $\hat C(\xi)(i\xi)^\nu = c_\beta(-i\xi)^{-\nu}$ is used, which corresponds to $D_+^\nu$ having symbol $(i\xi)^\nu$ (opposite of Samko convention, but consistent with paper's (9)). So the paper is internally self-consistent under its own inverted convention, but doesn't match ref 17's convention. Either state the FT convention explicitly or reverse the $\pm$ signs.

## Adjoint claim $C_+^\ast = C_-$

Kernel of $C_+$ is $k_+(t,s) = (t-s)^{\nu-1}/\Gamma(\nu)$ for $s\le t$, zero else. Adjoint kernel is $k_+(s,t)$ = $(s-t)^{\nu-1}/\Gamma(\nu)$ for $t\le s$ = anticausal RL integral kernel = kernel of $C_-$. ✓ under real $L^2$ inner product.

## Lemma 1 proof — completeness

§5 proof: verifies $C_+^{-1}P_+C_-^{-1}$ is a left inverse of $P_+CP_+$ on $L^2_{\rm adap}$, notes injectivity from strict convexity. Standard argument; the triangularity identities $P_+^\perp C_+ P_+ = 0$ and $P_+ C_- P_+^\perp = 0$ are the causality facts that drive the identity. Rigor gap: doesn't formally verify $P_+CP_+$ has closed range (needed for the *inverse* to be defined everywhere on the target space), and doesn't state precise domain-codomain of the operators as maps between homogeneous Sobolev spaces. For a research paper this needs expansion; for a PNAS position paper it is at the edge of acceptable.

## Theorem 1 proof — completeness

Three-step proof. Step (a) uses conditional Fubini (cited ref 21 Klenke). Step (b) is a tower-property argument. Step (c) uses the symbol identity + $I_-^\nu D_-^\nu = \mathrm{id}$ on $H^\nu$ (cited ref 17, §5.3 Thm 5.3). Uniqueness from strict convexity. Admissibility from PSD spectral hypothesis. This is a complete sketch; a specialist could fill in.

## §4.1 Boundary corrections

Claim: on interior $[\varepsilon T, (1-\varepsilon)T]$, two Söhngen–Tricomi boundary modes contribute $O(T^{\beta-1})$. This asymptotic scaling is asserted without proof or citation. Söhngen–Tricomi modes $(t(T-t))^{(\beta-1)/2}$: on the interior they are of order $T^{(\beta-1)/2}\cdot T^{(\beta-1)/2} = T^{\beta-1}$ per mode. So the scaling is plausible on dimensional grounds. But the claim that these are *subleading* to the bulk term for stochastic signals with $\Theta(1)$ tradeability norm requires comparing $O(T^{\beta-1})$ against $O(1)$ (or larger) contribution from the bulk term — a heuristic argument that needs at least a citation.

## §4.2 Temporary impact

Claim: modified symbol $M(\xi) = c_\beta|\xi|^{\beta-1} + \eta/\gamma$ is Krein-factorizable, giving one-sided factors; crossover frequency $\xi_\ast = (\gamma c_\beta/\eta)^{1/(1-\beta)}$; $\eta\to 0$ limit recovers (12).

Krein factorization requires $\log M \in L^1(\frac{d\xi}{1+\xi^2})$: for the additive combination $|\xi|^{\beta-1}+\text{const}$, this is satisfied (log has integrable tails). ✓

The $\eta\to 0$ limit is singular (loses high-frequency coercivity) but formally recovers the pure power-law symbol. Under the spectral decay hypothesis of §2.1 this should be justifiable. No proof provided; treated as a discussion-section observation.

## §4.3 Multi-asset

One-sentence claim: cross-impact $\mathbf K(t) = |t|^{-\beta}\mathbf A$ with symmetric PD $\mathbf A$ diagonalizes and reduces to scalar case per eigenvector. This is correct for the simple tensor-product kernel; a paper on cross-impact (ref 9) uses this and richer kernels. Treated appropriately as a gesture.

## §4.4 Numerical implementation

Toeplitz + FFT for fractional derivatives. Textbook. Uncontroversial. No experimental results shown or claimed.

## Reference gaps

- Ref 8 (Abi Jaber–Neuman): the paper's characterization "closed forms are available only in specific specializations" needs to be verified against the actual (8) content. The current paper's stationary-adapted closed form (12) sits outside (8)'s framework, which uses bounded horizon and operator-resolvent characterization. Direct comparison in one worked example (e.g., stationary Gaussian alpha on the whole line) would strengthen the novelty claim.
- Refs 7, 10, 11: some volume/page info may still be provisional at submission.
- Ref 15 (Arveson 1975 nest algebras): correct citation but the specific theorem used ("outer factorization in a nest algebra") is not named or numbered in-text.
- Ref 13 (Krein 1962): §2.3 says "which factorizes classically via Krein's theorem (13)". Krein's theorem here refers to the outer factorization of a positive-definite continuous function on the line via its log. Fine.

## Novelty vs. related work

Closest neighbors:
- (6) Gatheral–Schied–Slynko: constant signal, bounded interval, Fredholm/Söhngen–Tricomi.
- (7) Neuman–Voß: exponential kernel, general signal, Riccati closed form.
- (8) Abi Jaber–Neuman: general propagator, general signal, resolvent characterization; closed forms only in specializations.
- (11) Forde–Sánchez-Betancourt–Smith: constant signal on interval, half-order RL factorization observation.

Current paper: **stationary adapted signal on $\mathbb R$, power-law kernel, closed form via filtration Wiener–Hopf.** Claimed novel: (i) the identity (11) as a filtration operator identity, (ii) reduction of the closed form to a fractional derivative of the forecast curve (12). Position in the landscape looks defensible; the WH factorization on the adapted subspace does not appear explicitly in (6–11). The Markowitz analogy is decorative pedagogy, not a novel technical claim, but is honest as framing.

## Sources inspected

- `papers/markowitz-of-cost-pnas.md` (this artifact).
- Cross-references to `CHANGELOG.md` and `AGENTS.md` in workspace (style rules, prior refactoring decisions).
- No external network searches performed for this review (paper is a self-contained mathematical position piece; primary sources are the cited references, which I have not re-fetched).
