# Information-Thermodynamic Bound on Alpha Capture in Optimal Execution

*Working paper draft. The one-step Gaussian results (§3, §4) are fully derived and numerically verified. The continuous-time stationary OU + exponential-propagator result (§6) is analytical; the spectral envelope is closed form, but the tightness (whether a causal filter attains it) is conjectural. Existing-literature placement (§2) is verified.*

---

## 1. Question

Optimal-execution literature (Almgren–Chriss, Obizhaeva–Wang, Lehalle–Neuman) computes the strategy that maximizes signal P&L minus impact cost. **How much of that P&L can be attributed to information about the signal, in a quantifiable thermodynamic sense?**

In a trading context, two distinct informations matter:

- $I(\alpha; r)$ — how much the signal $\alpha$ tells you about the **actual return** $r$. This is a property of the data-generating process (signal quality, $R^2$-style).
- $I(u; \alpha)$ — how much the trader's order $u$ uses the signal $\alpha$. This is a property of the trading policy (extraction efficiency).

The bound we develop separates these cleanly:
$$
\mathbb{E}[\Pi] \;\leq\; \frac{\sigma_r^2}{2\lambda}\,\bigl(1 - e^{-2I(u;\alpha)}\bigr)\bigl(1 - e^{-2I(\alpha;r)}\bigr) \;=\; \frac{\sigma_r^2}{2\lambda}\bigl(1 - e^{-2I(u;r)}\bigr),
$$
in direct analogy with the generalized second law of information thermodynamics (Sagawa–Ueda 2010; Touzo–Marsili–Zagier 2021 for Glosten–Milgrom).

---

## 2. Existing literature

### 2.1 What is covered

- **Sagawa & Ueda 2010** ([PRL 104, 090602](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.090602)) — generalized Jarzynski under feedback control:
  $$\langle W \rangle - \Delta F \geq -k_B T \langle I \rangle.$$
  Each bit of measurement information allows at most $k_B T \ln 2$ of work.

- **Touzo, Marsili & Zagier 2021** (J. Stat. Mech. P033407, [arXiv:2010.01905](https://arxiv.org/abs/2010.01905)) — for the Glosten–Milgrom microstructure model, the informed trader's gain satisfies
  $$\mathbb{E}[G] \leq T_{\mathrm{market}} \cdot H[Y],$$
  with $T_{\mathrm{market}}$ derived from the noise-trader fraction and $H[Y]$ the entropy of the asset's fundamental value. The market-maker's pricing policy is identified with the optimal work-extraction protocol of a Szilárd engine.

- **Ducuara, Skrzypczyk, Buscemi, Sidajaya & Scarani 2023** (PRL 131, 197103, [arXiv:2209.15429](https://arxiv.org/abs/2209.15429)) — extends TMZ21 with a finite-horizon upper bound formulated in expected-utility language.

- **Tatikonda & Mitter 2009** (IEEE Trans. IT, *The Capacity of Channels with Feedback*) — directed-information formulation of Gaussian channel capacity with feedback.

- **Tanaka, Esfahani & Mitter 2018** ([arXiv:1510.04214](https://arxiv.org/abs/1510.04214), *LQG Control with Minimum Directed Information*) — minimizes directed information from plant output to control input subject to LQG performance. The closest existing analogue to the trading problem here.

- **Kim 2010** (IEEE Trans. IT, *Feedback Capacity of Stationary Gaussian Channels*) — spectral closed form for stationary Gaussian feedback capacity.

### 2.2 What is uncovered

None of TMZ21 / DSBSS23 covers **continuous-time optimal execution with propagator-type market impact**. They work the GM microstructure model, with discrete time, binary fundamental value, and bid–ask spread as the cost mechanism.

The propagator-impact setting (Lehalle–Neuman, Obizhaeva–Wang) is the natural arena for continuous-time, continuous-signal trading and is where the adapted-convex / Fredholm-equation machinery from this project lives. **No paper I have located applies a Sagawa–Ueda / TMZ21 information-thermodynamic bound to this setting**, and none separates signal quality $I(\alpha;r)$ from extraction efficiency $I(u;\alpha)$ as we do in §4.

The Tanaka–Esfahani–Mitter LQG-with-directed-information machinery is structurally adjacent and the appropriate tool for stationary continuous-time. To my knowledge it has not been applied to optimal trade execution either.

---

## 3. One-step Gaussian model — full derivation (single-information)

### 3.1 Setup

- Signal $\alpha \sim \mathcal{N}(0, \sigma_\alpha^2)$, observed by the trader.
- Return per unit traded $r = \alpha$ (**no return noise yet** — added in §4).
- Trade chosen via randomized linear-Gaussian policy:
  $$u = a \alpha + s\,\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0,1),\ \varepsilon \perp \alpha.$$
- Net P&L: $\Pi = u r - \tfrac12 \lambda u^2 = u \alpha - \tfrac12 \lambda u^2$.
- Mutual information (Gaussian channel formula):
  $$I(u;\alpha) = \tfrac12 \log\!\Big(1 + \frac{a^2 \sigma_\alpha^2}{s^2}\Big).$$

### 3.2 Expected P&L

$$\mathbb{E}[\Pi] = a\sigma_\alpha^2 - \tfrac12 \lambda(a^2\sigma_\alpha^2 + s^2). \tag{1}$$

### 3.3 Envelope at fixed information

Let $\mathrm{SNR} := a^2\sigma_\alpha^2 / s^2 = e^{2I} - 1$, parametrize $s^2 = c$, $a = \sqrt{\mathrm{SNR}\cdot c}/\sigma_\alpha$. Then
$$\mathbb{E}[\Pi] = \sigma_\alpha\sqrt{\mathrm{SNR}\cdot c} - \tfrac12 \lambda c (\mathrm{SNR}+1).$$
Maximize over $c$:
$$c^\star = \frac{\sigma_\alpha^2 \mathrm{SNR}}{\lambda^2 (\mathrm{SNR}+1)^2}, \qquad \mathbb{E}[\Pi]^\star = \frac{\sigma_\alpha^2 \mathrm{SNR}}{2\lambda(\mathrm{SNR}+1)}.$$
Using $\mathrm{SNR}+1 = e^{2I}$:
$$\boxed{\;\Pi_{\max}(I) = \frac{\sigma_\alpha^2}{2\lambda}\,\bigl(1 - e^{-2I}\bigr).\;} \tag{2}$$

### 3.4 Trading temperature

Tangent at $I = 0$:
$$\Pi_{\max}(I) = T_\alpha \cdot I - T_\alpha I^2 + O(I^3), \qquad T_\alpha := \frac{\sigma_\alpha^2}{\lambda}. \tag{3}$$

So the linear-in-information bound $\mathbb{E}[\Pi] \leq T_\alpha\, I(u;\alpha)$ is the direct analogue of TMZ21's $\mathbb{E}[G] \leq T \cdot H[Y]$, with $T_\alpha = \sigma_\alpha^2/\lambda$ playing the role of TMZ21's market temperature.

### 3.5 Limits

- $I \to \infty$: $\Pi_{\max} \to \sigma_\alpha^2/(2\lambda)$, recovering the deterministic optimum $u^\star = \alpha/\lambda$.
- $I \to 0$: $\Pi_{\max} \to 0$.
- Marginal value of a bit: $d\Pi_{\max}/dI|_{I=0} = T_\alpha$.

### 3.6 Numerical verification (script: `experiments/info_thermo_trading_one_step.py`)

Across 7 values of $I$ from 0.05 to 4.0, Monte Carlo $\mathbb{E}[\Pi]$ matches the envelope (2) within sampling SE. A 900-point grid sweep over $(a, s)$ finds zero policies that beat the envelope.

```
       I    Pi_max(theory)    Pi (sim)    +/- 2se     T*I (tangent)
    0.05         0.047581    0.047860    0.000269      0.050000
    0.10         0.090635    0.090755    0.000363      0.100000
    0.25         0.196735    0.196598    0.000503      0.250000
    0.50         0.316060    0.316112    0.000589      0.500000
    1.00         0.432332    0.432589    0.000626      1.000000
    2.00         0.490842    0.490490    0.000631      2.000000
    4.00         0.499832    0.500045    0.000633      4.000000
```

---

## 4. Two-information bound: separating signal quality from extraction efficiency

### 4.1 Setup

Add an unpredictable return-noise component:
- Signal $\alpha \sim \mathcal{N}(0, \sigma_\alpha^2)$, observed by trader.
- Return $r = \alpha + \xi$, with $\xi \sim \mathcal{N}(0, \sigma_\xi^2)$ independent of $\alpha$. Total variance $\sigma_r^2 = \sigma_\alpha^2 + \sigma_\xi^2$.
- Trader sees only $\alpha$ at decision time; chooses $u = a\alpha + s\varepsilon$, $\varepsilon \perp (\alpha, \xi)$.
- P&L: $\Pi = u r - \tfrac12 \lambda u^2$.

Three mutual informations:
$$
I_{\alpha r} := I(\alpha; r),\quad
I_{u\alpha} := I(u; \alpha),\quad
I_{ur} := I(u; r).
$$

Since the trader's policy depends only on $\alpha$ (not on $r$ or $\xi$ directly), the chain $r - \alpha - u$ is Markov.

### 4.2 Expected P&L is unchanged

Because $u \perp \xi$, $\mathbb{E}[u\xi] = 0$:
$$\mathbb{E}[\Pi] = \mathbb{E}[u\alpha] + \mathbb{E}[u\xi] - \tfrac12\lambda \mathbb{E}[u^2] = a\sigma_\alpha^2 - \tfrac12\lambda(a^2\sigma_\alpha^2 + s^2),$$
exactly as in (1). The return noise does not change the expected P&L for a given policy. **What it changes is the interpretation of the information bound.**

### 4.3 Correlation chain identity (Gaussian Markov chain)

For jointly Gaussian variables on the chain $r - \alpha - u$ with $u, \xi \perp$ and $\alpha = r - \xi$:
$$
\rho_{u,r} = \frac{\mathrm{Cov}(u,r)}{\sigma_u \sigma_r} = \frac{a \sigma_\alpha^2}{\sigma_u \sigma_r} = \underbrace{\frac{a\sigma_\alpha}{\sigma_u}}_{\rho_{u,\alpha}} \cdot \underbrace{\frac{\sigma_\alpha}{\sigma_r}}_{\rho_{\alpha,r}}.
$$
Squaring and using $1 - e^{-2I} = \rho^2$ for Gaussians:
$$
\boxed{\;1 - e^{-2I_{ur}} \;=\; \bigl(1 - e^{-2I_{u\alpha}}\bigr)\,\bigl(1 - e^{-2I_{\alpha r}}\bigr).\;} \tag{4}
$$

### 4.4 Two-factor envelope

The §3 derivation extends. Maximize $\mathbb{E}[\Pi]$ over $(a, s)$ at fixed $I_{u\alpha}$. Result is still (2) but rewriting in terms of $\sigma_r$ via $\sigma_\alpha^2 = \sigma_r^2 (1 - e^{-2I_{\alpha r}})$ gives
$$
\boxed{\;\Pi_{\max} \;=\; \frac{\sigma_r^2}{2\lambda}\,\bigl(1 - e^{-2I_{u\alpha}}\bigr)\bigl(1 - e^{-2I_{\alpha r}}\bigr) \;=\; \frac{\sigma_r^2}{2\lambda}\bigl(1 - e^{-2I_{ur}}\bigr). \;} \tag{5}
$$

The two equivalent forms come from (4). Define the **return-referenced market temperature**
$$T_r := \frac{\sigma_r^2}{\lambda}.$$

### 4.5 Asymptotic readings

- **Low signal quality** ($I_{\alpha r} \to 0$, $\sigma_\alpha \ll \sigma_\xi$): $\Pi_{\max} \approx \frac{\sigma_\alpha^2}{\lambda}\,(1 - e^{-2I_{u\alpha}})$, recovering (2). The bound is set by predictable variance $\sigma_\alpha^2$; the unpredictable $\sigma_\xi^2$ is invisible to the trader and cannot be captured.
- **High signal quality** ($I_{\alpha r} \to \infty$, $\sigma_\xi \to 0$): the second factor saturates at 1, and the bound reduces to $T_r \cdot (1 - e^{-2I_{u\alpha}})/2 = T_\alpha (1 - e^{-2I_{u\alpha}})/2$. (Same as §3.)
- **Both small** (low signal, low extraction): $\Pi_{\max} \approx \frac{4}{\lambda}\,\sigma_\alpha^2 I_{\alpha r} I_{u\alpha}$... wait, $\sigma_\alpha^2 = \sigma_r^2 \cdot (1 - e^{-2I_{\alpha r}}) \approx 2 \sigma_r^2 I_{\alpha r}$ for small $I_{\alpha r}$. So
$$\Pi_{\max} \approx \frac{\sigma_r^2}{2\lambda} \cdot 2I_{u\alpha} \cdot 2I_{\alpha r} = \frac{2\sigma_r^2}{\lambda} I_{u\alpha} I_{\alpha r}.$$
**Bilinear in the two informations** — doubling either signal quality or extraction efficiency doubles expected P&L, only if the other is small.

### 4.6 Data-processing reading

The single-information form $\Pi_{\max} = (\sigma_r^2/2\lambda)(1 - e^{-2I_{ur}})$ uses **trade–return mutual information** directly. The product form makes the data-processing inequality on the Markov chain $r - \alpha - u$ explicit: $I_{ur} \leq \min(I_{u\alpha}, I_{\alpha r})$, so each factor in the product is in $[0, 1]$, and the trader is bottlenecked by the smaller of "how much can the signal tell me" and "how much do I use of it."

### 4.7 Numerical verification (script: `experiments/info_thermo_trading_two_info.py`)

Verified across 27 parameter combinations $(\sigma_\alpha, \sigma_\xi, I_{u\alpha})$:

- **Product identity (4).** Empirical $\rho_{u,r}^2$ matches the product $(1-e^{-2I_{u\alpha}})(1-e^{-2I_{\alpha r}})$ within sampling noise. Representative rows ($\lambda = 1$):

| $\sigma_\alpha$ | $\sigma_\xi$ | $I_{\alpha r}$ | $I_{u\alpha}$ | $\rho_{u,r}^2$ (sim) | product (theory) |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.1 | 2.308 | 2.000 | 0.9719 | 0.9720 |
| 1.0 | 1.0 | 0.347 | 2.000 | 0.4913 | 0.4908 |
| 1.0 | 3.0 | 0.053 | 2.000 | 0.0976 | 0.0982 |
| 2.0 | 3.0 | 0.184 | 0.500 | 0.1944 | 0.1945 |

- **Two-factor envelope (5).** Monte Carlo P&L matches theory across the same 27 rows within sampling SE.

- **Grid sweep** (1000 random $(a,s)$ policies, $\sigma_\alpha=1$, $\sigma_\xi=2$): 0 violations of the envelope.

---

## 5. Aside: Gibbs / MaxCal policy is not envelope-attaining

In the MaxCal / entropy-regularized formulation (`notes/fluctuation-theorems-trading.md` §4), the trader samples from
$$dQ^\star(u|\alpha) \propto e^{-\beta J(u,\alpha)} d\mu_0(u), \quad \mu_0 = \mathcal{N}(0, \sigma_u^2).$$
This yields Gaussian policy with $a = \beta s^2$, $s^{-2} = \beta\lambda + \sigma_u^{-2}$, parametrized by $\beta$.

This corresponds to a *specific point* on the envelope (2) (or, equivalently, (5)) per choice of $\beta$. The Gibbs sampler traces a one-parameter sub-curve in the $(I_{u\alpha}, \Pi)$ plane and **only attains the envelope in the joint limit $\beta \to \infty$, $\sigma_u \to \infty$** (deterministic-policy limit). For finite $\beta$ it wastes information. The envelope-attaining policy is the direct §3.3 optimizer, which is *not* a Gibbs sampler at any finite $\beta$.

This observation is not explicit, to my knowledge, in the entropy-regularized-RL-for-execution literature.

---

## 6. Stationary continuous-time: OU signal + exponential propagator

### 6.1 Setup

- **Signal:** OU process,
  $$d\alpha_t = -\gamma \alpha_t\, dt + \sqrt{2\gamma}\, \sigma_\alpha\, dW^\alpha_t.$$
  Stationary variance $\mathbb{E}[\alpha_t^2] = \sigma_\alpha^2$; spectral density
  $$S_\alpha(\omega) = \frac{2\gamma \sigma_\alpha^2}{\omega^2 + \gamma^2}.$$
- **Return-noise:** independent stationary Gaussian process $\xi_t$ with spectral density $S_\xi(\omega)$ (in the bandlimited-white limit, $S_\xi \to \sigma_\xi^2$ const over the band of interest).
- **Realized return rate:** $r_t = \alpha_t + \xi_t$, with $S_r(\omega) = S_\alpha(\omega) + S_\xi(\omega)$.
- **Trade rate:** $u_t$ jointly Gaussian with $\alpha$; for stationary linear-Gaussian policies, $u_t = (K * \alpha)_t + \eta_t$ for some causal kernel $K$ and independent stationary noise $\eta_t$ with spectrum $S_\eta(\omega)$. Spectrum $S_u(\omega) = |\hat K(\omega)|^2 S_\alpha(\omega) + S_\eta(\omega)$.
- **Impact:** exponential decay kernel $G(\tau) = \lambda e^{-\rho \tau} \mathbf{1}_{\tau \geq 0}$, transfer $\hat G(\omega) = \lambda / (\rho + i\omega)$,
  $$\mathrm{Re}\,\hat G(\omega) = \frac{\lambda \rho}{\omega^2 + \rho^2}.$$
- **P&L rate** for stationary jointly Gaussian processes:
  $$\dot{\mathbb{E}}[\Pi] = \mathbb{E}[u_t r_t] - \tfrac12 \mathbb{E}\!\int u_t\, G(t-s)\, u_s\, ds = \int \mathrm{Re}\,\hat K(\omega) S_\alpha(\omega)\,\frac{d\omega}{2\pi} - \tfrac12 \int \mathrm{Re}\,\hat G(\omega) S_u(\omega)\,\frac{d\omega}{2\pi}.$$
  (The $\xi$ contribution vanishes since $u \perp \xi$.)

### 6.2 Spectral trading temperature

Define
$$\boxed{\;T_{\mathrm{market}}(\omega) := \frac{S_\alpha(\omega)}{2\,\mathrm{Re}\,\hat G(\omega)}.\;}$$

For OU + exponential propagator, substituting:
$$T_{\mathrm{market}}(\omega) = \frac{2\gamma \sigma_\alpha^2 / (\omega^2 + \gamma^2)}{2\lambda \rho / (\omega^2 + \rho^2)} = \frac{\gamma \sigma_\alpha^2}{\lambda \rho} \cdot \frac{\omega^2 + \rho^2}{\omega^2 + \gamma^2}. \tag{6}$$

Limits:
$$T_{\mathrm{market}}(0) = \frac{\rho\, \sigma_\alpha^2}{\lambda\, \gamma}, \qquad T_{\mathrm{market}}(\infty) = \frac{\gamma\, \sigma_\alpha^2}{\lambda\, \rho}, \qquad \frac{T_{\mathrm{market}}(\infty)}{T_{\mathrm{market}}(0)} = \frac{\gamma^2}{\rho^2}.$$

The ratio $\gamma/\rho$ controls which frequencies are "hot." If $\rho \gg \gamma$ (impact decays fast, signal slow), low frequencies are cold and high frequencies are hot — the trader has cheap access to fast bets but the signal lives mostly at low frequency. If $\rho \ll \gamma$ (impact long-lived, signal fast), the reverse: low frequencies are hot but the signal lives at high frequency. Either mismatch wastes thermodynamic budget.

### 6.3 Spectral signal-quality density

Define the spectral analogue of $I_{\alpha r}$ density:
$$q(\omega) := \frac{S_\alpha(\omega)}{S_\alpha(\omega) + S_\xi(\omega)} \in [0, 1]. \tag{7}$$
This is the local "fraction of return-variance at frequency $\omega$ that is predictable from the signal."

### 6.4 Spectral two-factor envelope (conjecture)

**Conjecture.** For any causal jointly-Gaussian policy in the propagator model of §6.1,
$$
\boxed{\;\dot{\mathbb{E}}[\Pi] \;\leq\; \int T_{\mathrm{market}}(\omega) \cdot q(\omega) \cdot \bigl(1 - e^{-2\, dI_{u\alpha}(\omega)}\bigr)\,\frac{d\omega}{2\pi}, \;} \tag{8}
$$
where $dI_{u\alpha}(\omega) = \tfrac12 \log\bigl(1 + |\hat K(\omega)|^2 S_\alpha(\omega)/S_\eta(\omega)\bigr)$ is the spectral density of the directed-information rate from $\alpha$ to $u$ at frequency $\omega$.

**Derivation sketch.** Apply §4.4 band-by-band. At each frequency the contribution is bounded by the one-step envelope $T_{\mathrm{market}}(\omega) \cdot q(\omega) \cdot (1 - e^{-2\,dI})$; integrate. The subtlety is causality on $K$. The bound (8) treats each frequency independently and so represents an upper bound on the *causal* optimum; tightness would require the band-optimal $|\hat K(\omega)|$ to assemble into a causal transfer function. **I have not proved this is automatic.**

**Unconstrained envelope.** Letting $dI_{u\alpha} \to \infty$ at every frequency (extraction efficiency saturating, ignoring information cost):
$$\dot{\mathbb{E}}[\Pi]^{\mathrm{max,unc}} = \int T_{\mathrm{market}}(\omega) q(\omega) \frac{d\omega}{2\pi}.$$
For OU signal and bandlimited-white noise $S_\xi(\omega) = \sigma_\xi^2$ over relevant band, this integral has a closed form via partial fractions. With $S_\alpha = 2\gamma \sigma_\alpha^2/(\omega^2 + \gamma^2)$ and $S_\xi = \sigma_\xi^2$:
$$q(\omega) = \frac{2\gamma \sigma_\alpha^2}{2\gamma \sigma_\alpha^2 + \sigma_\xi^2 (\omega^2 + \gamma^2)} = \frac{A}{\omega^2 + B^2},$$
with $A = 2\gamma\sigma_\alpha^2/\sigma_\xi^2$ and $B^2 = \gamma^2 + 2\gamma\sigma_\alpha^2/\sigma_\xi^2 = \gamma^2 + A$.

So
$$T_{\mathrm{market}}(\omega) q(\omega) = \frac{\gamma\sigma_\alpha^2}{\lambda\rho} \cdot \frac{\omega^2 + \rho^2}{\omega^2 + \gamma^2} \cdot \frac{A}{\omega^2 + B^2}.$$
Partial fractions of $(\omega^2 + \rho^2) / [(\omega^2 + \gamma^2)(\omega^2 + B^2)]$:
$$\frac{\omega^2 + \rho^2}{(\omega^2 + \gamma^2)(\omega^2 + B^2)} = \frac{1}{B^2 - \gamma^2}\!\left[\frac{\rho^2 - \gamma^2}{\omega^2 + \gamma^2} - \frac{\rho^2 - B^2}{\omega^2 + B^2}\right].$$
Integrate using $\int (\omega^2 + a^2)^{-1} d\omega/(2\pi) = 1/(2a)$:
$$\int \frac{(\omega^2 + \rho^2)}{(\omega^2+\gamma^2)(\omega^2+B^2)} \frac{d\omega}{2\pi} = \frac{1}{B^2 - \gamma^2}\!\left[\frac{\rho^2 - \gamma^2}{2\gamma} - \frac{\rho^2 - B^2}{2B}\right] = \frac{1}{2}\frac{B(\rho^2-\gamma^2) - \gamma(\rho^2-B^2)}{\gamma B (B^2-\gamma^2)}.$$

Simplify using $B^2 - \gamma^2 = A$:
$$= \frac{B\rho^2 - B\gamma^2 - \gamma\rho^2 + \gamma B^2}{2\gamma B \cdot A} = \frac{\rho^2(B-\gamma) + \gamma B(B - \gamma)}{2\gamma B A} = \frac{(B-\gamma)(\rho^2 + \gamma B)}{2\gamma B A}.$$

Then
$$\dot{\mathbb{E}}[\Pi]^{\mathrm{max,unc}} = \frac{\gamma\sigma_\alpha^2}{\lambda\rho} \cdot A \cdot \frac{(B-\gamma)(\rho^2 + \gamma B)}{2\gamma B A} = \frac{\sigma_\alpha^2}{2\lambda\rho} \cdot \frac{(B-\gamma)(\rho^2 + \gamma B)}{B}. \tag{9}$$

Sanity checks:
- **No return noise** ($\sigma_\xi \to 0$, $A \to \infty$, $B \to \infty$): leading behavior $B - \gamma \approx B$, $\rho^2 + \gamma B \approx \gamma B$, so
  $\dot \Pi^{\mathrm{max,unc}} \to \sigma_\alpha^2 \gamma / (2\lambda\rho) \cdot 1 = \sigma_\alpha^2 \gamma / (2\lambda\rho)$. *No*: let me recompute. $(B-\gamma)(\rho^2+\gamma B)/B \to (B)(\gamma B)/B = \gamma B \to \infty$. So $\dot \Pi^{\mathrm{max,unc}} \to \infty$? That's wrong: the unconstrained $\dot \Pi$ should be finite even with perfect signal.

  The issue: I removed the information-cost penalty entirely. With perfect signal and **no impact cost on the trade rate as it grows**, the trader trades infinitely fast. But the impact cost integrand $\tfrac12 \int \mathrm{Re}\,\hat G(\omega) S_u(\omega) d\omega/(2\pi)$ should grow with $|\hat K|^2$. So the unconstrained-over-extraction calculation is only an upper bound; the true unconstrained-over-$K$ optimum is finite and given by the standard Lehalle–Neuman spectral solution.

  The right reading: **(9) is the unconstrained envelope when extraction efficiency saturates at every frequency** (i.e., information cost zero). The fact that it diverges as $\sigma_\xi \to 0$ shows that the bound is loose in the perfect-signal limit; the true optimum is bounded by the impact cost, not by information.

- **Trivial signal** ($\sigma_\alpha \to 0$, $A \to 0$, $B \to \gamma$): $(B - \gamma) \to 0$, so $\dot \Pi^{\mathrm{max,unc}} \to 0$. Good.

- **Equal time scales** ($\rho = \gamma$): (9) becomes $\sigma_\alpha^2/(2\lambda\gamma) \cdot (B-\gamma)(\gamma^2 + \gamma B)/B = \sigma_\alpha^2/(2\lambda) \cdot (B-\gamma)(\gamma + B)/B = \sigma_\alpha^2/(2\lambda) \cdot (B^2 - \gamma^2)/B = \sigma_\alpha^2/(2\lambda) \cdot A/B$.

  In the perfect-signal limit ($A \to \infty$, $B = \sqrt{\gamma^2 + A} \sim \sqrt A$), $A/B \to \sqrt A \to \infty$ — same divergence.

The divergence at $\sigma_\xi \to 0$ tells us the unconstrained-over-extraction envelope (9) is genuinely the *information-saturated upper bound*, not the impact-optimal solution. To get a finite, useful bound we have to include either (i) a directed-information budget on $K$ (Tanaka–Esfahani–Mitter), or (ii) the standard impact-cost optimization (Lehalle–Neuman) — which trade information against impact cost endogenously.

### 6.5 What this gives us

The closed form (6) for $T_{\mathrm{market}}(\omega)$ and the integral (9) for the information-saturated envelope are both clean and correct (modulo the §6.4 conjecture about frequency decoupling under causality). What's missing:

1. **The right finite envelope.** The bound should be tightened by including either an explicit MI budget on $K$ or the impact-cost term that constrains $K$. The MI-budget version is the natural extension of (5); the impact-cost version recovers Lehalle–Neuman.

2. **Tightness of the band-by-band bound under causality.** Needs verification. The OU+exponential setting is the standard test bed because both kernels are first-order rational and spectral factorization is closed form.

3. **Numerical check.** I would compare a specific causal one-pole filter $\hat K(\omega) = k_0/(\kappa + i\omega)$ as policy and check that its $(I, \dot\Pi)$ point lies below the envelope. (Script `experiments/info_thermo_trading_OU_propagator.py` was drafted for this but hung during sweep; deferring.)

---

## 7. Honest assessment

### 7.1 What is solid

- **Two-factor product bound (5).** Algebraically correct, numerically verified across 27 parameter combinations, 1000-policy grid sweep clean. Separates signal quality from extraction efficiency in the cleanest possible way.
- **One-step envelope (2).** Same status: derived and verified.
- **Trading temperatures.** $T_\alpha = \sigma_\alpha^2/\lambda$, $T_r = \sigma_r^2/\lambda$ — well-defined, dimensionally correct, with clear small-information slope interpretation.
- **Spectral $T_{\mathrm{market}}(\omega)$ for OU + exponential propagator (6).** Closed form, dimensionally consistent.
- **MaxCal-policy clarification (§5).** Gibbs sampler is sub-envelope, not envelope-attaining.

### 7.2 What is conjectural

- The frequency-decoupled spectral bound (8), specifically the claim that band-by-band optimization respects causality without loss. Plausible by analogy with Tanaka–Esfahani–Mitter 2018 but not proved in this note.
- The unconstrained-extraction envelope (9) is correct as derived but is information-saturated, not impact-optimal — diverges as $\sigma_\xi \to 0$. The genuinely useful bound needs the MI-vs-impact tradeoff.

### 7.3 What is known and adjacent

- Directed-information / LQG-with-information-constraints (Tatikonda–Mitter, Tanaka et al.) supplies the technique. Applying it to propagator-impact execution is a contained exercise.

### 7.4 What would make this a paper

1. Prove (8) rigorously by reducing to Tanaka–Esfahani–Mitter 2018's rate-distortion-with-causality framework.
2. Compute the impact-cost-aware envelope for OU + exponential, recovering Lehalle–Neuman at zero MI cost and the §3 deterministic limit at infinite MI.
3. Numerical experiment: causal filter with bounded directed-information rate, plot $(\dot I, \dot \Pi)$ tradeoff curve.
4. Practical reading: real execution constraints (latency, signal-to-noise, market data bandwidth, quantization) all translate into bounded MI between $\alpha$ and $u$. The two-factor bound (5) tells you which of *signal quality* or *information bandwidth* binds first.

### 7.5 What would falsify the picture

If the conjecture (8) is wrong, the most likely failure mode is that causality on $K$ binds nontrivially and the directed-information bound is loose compared to one involving the Wiener–Hopf factorization of the impact kernel. That would couple information theory to the adapted-convex skeleton from `papers/adapted-convex-duality.md` and the outer factorization explicitly — more interesting, not less.

---

## 8. Sources

- **Sagawa, T. & Ueda, M. (2010)**, *Generalized Jarzynski Equality under Nonequilibrium Feedback Control*, Phys. Rev. Lett. **104**, 090602. <https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.090602>
- **Touzo, L., Marsili, M. & Zagier, D. (2021)**, *Information thermodynamics of financial markets: the Glosten–Milgrom model*, J. Stat. Mech. P033407. <https://arxiv.org/abs/2010.01905>
- **Ducuara, A. F., Skrzypczyk, P., Buscemi, F., Sidajaya, P. & Scarani, V. (2023)**, *Maxwell's Demon Walks into Wall Street*, Phys. Rev. Lett. **131**, 197103. <https://arxiv.org/abs/2209.15429>
- **Tatikonda, S. & Mitter, S. K. (2009)**, *The Capacity of Channels with Feedback*, IEEE Trans. Inf. Theory **55**(1), 323.
- **Tanaka, T., Esfahani, P. M. & Mitter, S. K. (2018)**, *LQG Control with Minimum Directed Information*, IEEE Trans. Autom. Control **63**(1), 37. <https://arxiv.org/abs/1510.04214>
- **Kim, Y.-H. (2010)**, *Feedback Capacity of Stationary Gaussian Channels*, IEEE Trans. Inf. Theory **56**(1), 57.
- **Massey, J. L. (1990)**, *Causality, feedback and directed information*, Proc. ISITA.
- **Cover, T. M. & Pombra, S. (1989)**, *Gaussian feedback capacity*, IEEE Trans. Inf. Theory **35**, 37.
- **Lehalle, C.-A. & Neuman, E. (2019)**, *Incorporating signals into optimal trading*, Finance Stoch. **23**, 275.

## 9. Cross-references in this workspace

- `notes/maxcal-fluctuation-theorems.md` — Sagawa–Ueda derivation.
- `notes/fluctuation-theorems-trading.md` — first-pass attempt that motivated this thread; §6.3 of that note is what this document delivers.
- `papers/noisy-signal-impact-trading.md` — stationary Wiener–Hopf calculation for trading; baseline against which the §6 conjecture would be checked.
- `papers/adapted-convex-duality.md` — operator-algebraic backbone.
- `experiments/info_thermo_trading_one_step.py` — verification script for §3.
- `experiments/info_thermo_trading_two_info.py` — verification script for §4 (two-information bound).
- `experiments/info_thermo_trading_OU_propagator.py` — draft script for §6 numerical check (deferred; sweep hangs, needs simplification).
