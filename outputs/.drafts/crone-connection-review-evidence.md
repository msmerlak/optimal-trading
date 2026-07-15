# CRONE-connection review — evidence notes

## Paper claim under review
File: `papers/markowitz-of-cost-pnas.md`, §1.3(iii), line 67:

> "The half-order factorization was implicit in (11); the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new, and it makes contact with the CRONE / fractional-PID control tradition (18, 19), to our knowledge not previously connected to execution."

Central formula (paper, eq. 12): $u^\star_t = \lambda^{-1}\kappa_{1-\gamma}(D_+^\beta \zeta)(t)$, $\zeta_s = (D_-^\beta \bar\alpha(s,\cdot))(s)$, $\beta = (1-\gamma)/2$.

Refs cited:
- [18] Oustaloup A (1991) *La Commande CRONE* (Hermès).
- [19] Chen YQ, Petráš I, Xue D (2009), "Fractional order control — A tutorial", *Proc. American Control Conf.* 1397–1411.

## What CRONE is (from primary sources)

Sources consulted:
- Oustaloup et al., "The great principles of the CRONE control" (1993), doi:10.1109/icsmc.1993.384860
- Oustaloup et al., "Third generation CRONE control" (1993), doi:10.1109/icsmc.1993.384864
- Oustaloup et al., "From fractal robustness to the CRONE approach" (1998), https://www.esaim-proc.org/articles/proc/pdf/1998/03/proc-Vol5.15.pdf
- Sabatier et al., "CRONE Control: Principles, Extensions and Applications" (2013), doi:10.5890/jand.2013.08.001
- Lanusse et al., "CRONE control system design toolbox" (2013), doi:10.1098/rsta.2012.0149
- Lanusse, Oustaloup, Sabatier, "Fractional Order PID and First Generation CRONE Control System Design", doi:10.1007/978-94-017-9807-5_2

Key facts:
1. **CRONE = *Commande Robuste d'Ordre Non Entier*** ("Robust Control of Non-Integer Order"). Frequency-domain design methodology.
2. **Design object**: shape the open-loop transfer function so that its Nichols locus is (near the gain-crossover) a straight line whose slope is set by a fractional (non-integer) order $n$.
3. **Design objective**: robustness to gain variations of the plant — specifically, keep the closed-loop damping ratio (phase margin) constant as the plant gain varies. This is the "iso-damping" property. Oustaloup ESAIM 1998 derives it from a "fractal robustness" model where a fractional-order oscillator's damping depends only on the non-integer order.
4. **Three generations**:
   - Gen 1 (constant-phase controller): fractional real order in a band around crossover.
   - Gen 2 (variable-phase controller): tracks plant phase.
   - Gen 3 (complex non-integer order): open-loop Nichols locus is a straight line segment of arbitrary direction; used when the plant has a resonance.
5. **Implementation**: continuous-time fractional operator $s^n$ is approximated by a rational band-limited IIR filter — the "Oustaloup approximation" — over the design frequency band. All physical implementations are integer-order rational; the fractional order is a design abstraction.
6. **FOPID / PI$^\lambda$D$^\mu$ (Podlubny 1994, IEEE TAC 44:208–214)**: fractional generalization of PID with transfer function $K_p + K_i s^{-\lambda} + K_d s^{\mu}$. Two extra tuning parameters ($\lambda, \mu$) chosen by heuristics (rules of thumb, LMI, genetic programming; see Padula–Visioli 2010, Das et al. 2018).

## What the paper does

1. **Problem**: optimize $\mathbb{E}\int u_t\alpha_t\,dt - \tfrac{\lambda}{2}\mathbb{E}\iint G(|t-v|)u_tu_v\,dt\,dv$ over adapted $u$; $G(t)=c|t|^{-\gamma}$, $\gamma\in(0,1)$.
2. **Method**: filtration Wiener–Hopf factorization $C = C_-C_+$ of the impact operator; adapted FOC gives $u^\star = \lambda^{-1}C_+^{-1}P_+C_-^{-1}\alpha$.
3. **Fractional collapse**: $\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}$ factorizes as $c_\gamma(i\xi)^{-\beta}(-i\xi)^{-\beta}$, so $C_\pm^{-1}=c_\gamma^{-1/2}D_\pm^\beta$, giving $u^\star = \lambda^{-1}\kappa_{1-\gamma}D_+^\beta[P_+(D_-^\beta\alpha)]$, i.e., the diagonal $\zeta_s = D_-^\beta\bar\alpha(s,\cdot)|_s$ formula.
4. **Origin of the fractional order**: $\beta = (1-\gamma)/2$ is *derived* from the empirical impact-decay exponent $\gamma$. Not a design parameter.
5. **Object differentiated**: the trader's forecast curve $\bar\alpha(s,\cdot)$ — a two-argument stochastic process, adapted.

## Structural comparison

| Aspect | CRONE / FOPID | This paper |
|---|---|---|
| Design goal | Iso-damping / phase-margin robustness to plant gain variations | LQ optimality against a specific plant (propagator model) |
| Where fractional order comes from | Design choice (tuning parameter chosen for a target frequency-domain shape) | Derived: $\beta = (1-\gamma)/2$ from Wiener–Hopf factorization of the impact-kernel symbol $|\xi|^{\gamma-1}$ |
| What is differentiated | Error signal $e(t) = r(t) - y(t)$ | Forecast curve $\bar\alpha(s,\cdot)$ (conditional expectation of future signal) |
| Operator form | One-sided $s^n$ (Laplace), causal by construction; implemented as band-limited rational IIR | Two-sided composition $D_+^\beta \circ P_+ \circ D_-^\beta$; anticausal factor $D_-^\beta$ is essential |
| Adaptedness | Standard feedback controllers act on realized error, causal by construction; no explicit projection | Anticausal $D_-^\beta$ would use future signal values → must be replaced by conditional expectation $P_+$; the projection between the two half-derivatives is the "operator signature" of the filtration constraint |
| Loss/norm | $\mathcal{H}_\infty$-shaping in frequency domain | $L^2$ LQ minimization over adapted schedules |
| Tuning | Heuristic (rules of thumb, LMI, GA) | None — closed-form derivation |
| Physical implementation | Oustaloup rational IIR approximation | Marchaud integral (exact); FFT/Toeplitz implementation on discrete grid |

## Prior connections between fractional control and optimal execution

Search for prior work: `"fractional order control" "optimal execution"`, `"CRONE" "trading"`, `"fractional PID" "market impact"` — no hits. Optimal-execution literature uses fractional operators (Forde–Sánchez-Betancourt–Smith 2022, ref [11]; Jusselin–Rosenbaum 2020, ref [3]; Bouchaud propagator community) but never cites CRONE. The paper's "to our knowledge not previously connected" is defensible.

## What is shared

- Both use one-sided (Riemann–Liouville / Marchaud) fractional derivatives of order in $(0,1)$.
- Both produce a linear map from an input signal to a control action mediated by fractional operators.
- In CRONE's "fractal robustness" derivation (Oustaloup 1998) the fractional order matches a fractional-power plant model; here $\beta$ matches the fractional-integral impact operator $C$. In both, the fractional exponent of the controller is a function of a fractional exponent of the plant/kernel — this is the closest genuine kinship.

## What is not shared

- The two-sided decomposition $D_+^\beta \circ P_+ \circ D_-^\beta$ with a projection in the middle has no CRONE analog. This is arguably the most distinctive object in the paper.
- CRONE is a robustness-first design methodology; the paper is a Bayes/LQ optimization. Different loss, different derivation, different meaning of "optimal".
- CRONE fractional order is a tuning parameter; the paper's is a derived quantity from empirical propagator physics.
- FOPID is applied to error feedback; the paper's operator acts on the *forecast curve*, an object controllers do not have (no forecast → adapted projection structure).

## Assessment

The claim "makes contact with the CRONE / fractional-PID tradition" is **thematically true but mechanically thin**:

- **Superficial**: shared use of $D^n$ with $n\in(0,1)$; shared observation that fractional plants beget fractional controllers.
- **Substantial**: essentially none at the level of derivation, decomposition, projection, or optimality criterion. The paper's central object (two Marchaud halves separated by an adapted projection) is not a CRONE object.

A tougher reviewer could object that "makes contact with" oversells a shared operator vocabulary as a research bridge. A defensive rewrite would say something like "shares with the CRONE / fractional-PID tradition (18, 19) the use of one-sided fractional operators in control, though the exponent here is derived from the impact-kernel decay rather than chosen for iso-damping robustness."

The claim about no prior connection between fractional-order control and optimal execution is defensible from the search results.
