# Defining Tradeability of a Signal

*Short note. Companion to `papers/info-thermodynamics-trading.md`. Proposes a layered definition of signal tradeability built from the spectral information-thermodynamic framework.*

---

## The question

Given a candidate alpha signal $\alpha_t$ and the market in which it is to be traded, what number (or numbers) should we attach to it to call it "tradeable"?

The answer must combine three ingredients that are usually treated separately:

- **Signal quality** — how much does $\alpha$ tell you about realized return $r$?
- **Frequency content** — at which timescales does the signal live?
- **Impact structure** — at which timescales is execution cheap?

A definition that uses only one of these is incomplete. Below is a layered definition: a hierarchy of refinements, each strictly more honest than the previous.

## Setup (recap)

- Signal $\alpha_t$, stationary, spectral density $S_\alpha(\omega)$.
- Realized return rate $r_t = \alpha_t + \xi_t$, $\xi$ independent stationary noise with spectral density $S_\xi(\omega)$.
- Trade rate $u_t$, stationary jointly Gaussian with $\alpha$, of the form $u_t = (K * \alpha)_t + \eta_t$ for causal $K$ and independent $\eta$.
- Impact kernel $G(\tau)$ with transfer function $\hat G(\omega)$. P&L rate
$$\dot \Pi(K) = \int \mathrm{Re}\,\hat K(\omega)\,S_\alpha(\omega)\,\frac{d\omega}{2\pi} - \tfrac12 \int \mathrm{Re}\,\hat G(\omega)\,S_u(\omega)\,\frac{d\omega}{2\pi}.$$

## Layer 0 — naive: signal quality alone

The reflexive answer (equity research, $R^2$, signal IC):
$$\mathcal{T}_0 \;:=\; I(\alpha; r) \;=\; -\tfrac12 \int \log\!\bigl(1 - q(\omega)\bigr)\,\frac{d\omega}{2\pi}, \qquad q(\omega) := \frac{S_\alpha(\omega)}{S_\alpha(\omega) + S_\xi(\omega)}.$$

**Why this is wrong (or at best half the answer).** A signal with $\mathcal{T}_0$ large but living at frequencies where impact is expensive (or shorter-lived than the impact decay) is untradeable. Conversely, a low-$\mathcal{T}_0$ signal at frequencies where impact is cheap and the signal persists long enough to trade against can be very tradeable. Layer 0 ignores both impact and timing.

## Layer 1 — spectral tradeability density

Define the **spectral tradeability density**
$$\boxed{\;\tau(\omega) \;:=\; T_{\mathrm{market}}(\omega) \cdot q(\omega) \;=\; \frac{S_\alpha(\omega)^2}{2\,\mathrm{Re}\,\hat G(\omega) \cdot \bigl(S_\alpha(\omega) + S_\xi(\omega)\bigr)}.\;}$$

Three factors, multiplicatively:

| factor | reads as | endogenous? |
|---|---|---|
| $S_\alpha(\omega)$ | how much signal is at this frequency | no (signal-side) |
| $1/\mathrm{Re}\,\hat G(\omega)$ | how cheap impact is at this frequency | no (microstructure) |
| $S_\alpha(\omega)/\bigl(S_\alpha(\omega)+S_\xi(\omega)\bigr)$ | how predictable return is at this frequency | no (data-generating process) |

All three are properties of the environment, not the trader. Integrating:
$$\mathcal{T}_1[\alpha, \xi, G] \;:=\; \int \tau(\omega)\,\frac{d\omega}{2\pi}.$$

**Properties.**

- Units: P&L per unit time (dollars/sec).
- $\mathcal{T}_1 = 0$ for pure-noise signal ($S_\alpha \equiv 0$).
- $\mathcal{T}_1 = 0$ for signal living entirely where $\mathrm{Re}\,\hat G \to \infty$.
- Monotone in signal quality and in impact cheapness.
- Reduces to $\sigma_\alpha^2 / (2\lambda)$ in the white-signal / instantaneous-impact limit (recovers `papers/info-thermodynamics-trading.md` §3).

**Caveat.** $\mathcal{T}_1$ is the band-by-band upper envelope. The true causal supremum $\sup_K \dot \Pi(K)$ may be strictly less because the band-optimal $K$ need not be causal. The two coincide whenever the spectral-factorization-derived $K^\star$ from the Wiener–Hopf optimization happens to match the band-decoupled optimum — a property that holds in some special cases (e.g., rational spectra with matching pole structures) but not in general.

## Layer 1.5 — Lehalle–Neuman: the impact-aware exact value

The honest finite, impact-respecting tradeability:
$$\boxed{\;\mathcal{T}_\infty[\alpha, \xi, G] \;:=\; \sup_{K \in H^2_+} \dot \Pi(K),\;}$$
i.e., the supremum over causal Gaussian linear policies, with $K$ in the Hardy space of causal transfer functions. For OU signal + exponential impact this is the standard Lehalle–Neuman optimum, with a closed form via spectral factorization.

Inequality: $\mathcal{T}_\infty \leq \mathcal{T}_1$, with equality whenever band-by-band decoupling preserves causality.

## Layer 2 — information-budgeted: tradeability as a curve

Real traders do not have infinite information bandwidth. Latency, observed-data SNR, model capacity, tick quantization, and order-rate limits all upper-bound the directed-information rate $\dot I(\alpha \to u)$. The honest object is then a **curve, not a number**:
$$\boxed{\;\mathcal{T}(\dot I_{\max}) \;:=\; \sup_{K \in H^2_+,\ \dot I(\alpha \to u)\, \leq\, \dot I_{\max}}\; \dot \Pi(K).\;}$$

This is the rate-distortion-style tradeoff between information cost and P&L. Properties:

- Concave in $\dot I_{\max}$ (standard rate-distortion argument).
- $\mathcal{T}(0) = 0$.
- $\mathcal{T}(\infty) = \mathcal{T}_\infty$ from Layer 1.5.
- Slope at origin: $\mathcal{T}'(0) = $ frequency-weighted trading temperature
  $$\mathcal{T}'(0) = \int T_{\mathrm{market}}(\omega) q(\omega)^{\!\star}(\omega)\,\frac{d\omega}{2\pi},$$
  where the weight $q^\star$ is the optimal frequency allocation of the first marginal bit (water-filling-style; see Tanaka–Esfahani–Mitter 2018).

**This is the right definition of tradeability.** It tells you not just whether a signal is tradeable but **at what information bandwidth you have to operate** to capture a target fraction of the achievable alpha.

## Layer 3 — scalar summaries

If forced to one number, two are needed:

1. $\mathcal{T}_\infty$ — the **ceiling**: dollars per unit time achievable with infinite information bandwidth.
2. $\mathcal{T}'(0)$ — the **exchange rate**: marginal P&L per bit of directed information, at zero information budget.

Their ratio
$$\boxed{\;\dot I_{\mathrm{half}} \;:=\; \frac{\mathcal{T}_\infty}{2\,\mathcal{T}'(0)} \quad (\text{half-saturation info rate, ballpark})\;}$$
has units of bits per unit time and answers: *how much information bandwidth do I need to capture half the available alpha?* This is the natural way to compare signals across different markets, frequencies, and impact regimes.

## Why this is more than redefinition

The standard tradeability proxies in practice — $\mathrm{IC} \cdot \sqrt{\text{turnover}}$, Sharpe-after-cost, half-life-adjusted information ratio — are all **point estimates on the curve $\mathcal{T}(\dot I)$ at one specific operating point**. The framework above clarifies:

1. **Why those proxies sometimes disagree.** They sample different points on the same underlying curve; comparing them across signals tested at different turnover rates compares different points on different curves.

2. **What determines the right operating point.** The trader's actual information bandwidth — set by latency, market-data SNR, model capacity, and order-rate constraints. There is one curve per signal-and-market; the trader chooses where to sit on it.

3. **Falsifiable prediction.** Across a portfolio of signals tested in the same market under controlled directed-information budgets, the curves $\mathcal{T}(\dot I)$ should all be concave with the slope at origin matching the spectral integral $\int T_{\mathrm{market}}(\omega) q^\star(\omega) d\omega/(2\pi)$ within calibration constants. That is testable.

## Comparison with conventional definitions

| Conventional definition | What it is in the framework | What it misses |
|---|---|---|
| Information coefficient $\mathrm{IC}$ | $\rho_{\alpha,r}$, related to $\sqrt{\mathcal{T}_0}$ | impact, frequency content |
| Sharpe-after-cost (at fixed turnover $T$) | one point on $\mathcal{T}(\dot I)$, normalized by $\sqrt{\sigma_\Pi^2}$ | does not separate exogenous from endogenous |
| Signal-to-cost (Grinold/Kahn) | linear approximation to $\mathcal{T}_\infty$ near zero turnover | ignores impact decay structure |
| Capacity (AUM at which Sharpe halves) | quantile of $\mathcal{T}_\infty$ over portfolio scale | not signal-intrinsic; couples with size |
| Half-life-adjusted IR | proxy for $\int \tau(\omega) d\omega$ in OU regime | crude spectral approximation |

The Layer 1–2 definition unifies these as projections of a common object.

## What is conjectural in this note

- The Layer 2 curve $\mathcal{T}(\dot I)$ is well-defined as a supremum, but its closed form for OU+exponential under a directed-information budget requires the Tanaka–Esfahani–Mitter 2018 framework adapted to propagator impact. Not done.
- The slope-at-origin formula in Layer 2 is heuristic; the precise water-filling weight $q^\star$ would emerge from a Lagrangian on the directed-information constraint.
- The empirical claim in "Why this is more than redefinition" point 3 is a prediction, not a measurement.

## Cross-references

- `papers/info-thermodynamics-trading.md` §3, §4 — the one-step bounds underlying Layers 0 and 1.
- `papers/info-thermodynamics-trading.md` §6 — the spectral $T_{\mathrm{market}}(\omega)$ closed form for OU + exponential propagator.
- `papers/noisy-signal-impact-trading.md` — the stationary Wiener–Hopf computation against which $\mathcal{T}_\infty$ would be checked.
- Tanaka, Esfahani & Mitter 2018, *LQG Control with Minimum Directed Information* ([arXiv:1510.04214](https://arxiv.org/abs/1510.04214)) — the natural framework for Layer 2.
- Kim 2010, *Feedback Capacity of Stationary Gaussian Channels* — for the directed-information rate in stationary Gaussian channels.
