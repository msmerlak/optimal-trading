"""Compare paper's bulk policy (P) vs user-proposed filtration W-H policy (U).

Setup: stationary OU signal, power-law propagator G(r) = c |r|^{-gamma}, gamma in (0,1).

Paper's policy (P) — Theorem 4.1 evaluated for OU in closed form:
    For OU, bar_alpha(t,s) = alpha_s for s<=t and e^{-theta(s-t)} alpha_t for s>t.
    The Riesz half-sum splits at s=t into causal and anticausal half:
        D^{1-gamma} bar_alpha(t,.)(t) = (1/(2 sin(pi gamma/2))) [D_+^{1-gamma} alpha_t + theta^{1-gamma} alpha_t]
    (the anticausal half collapses to theta^{1-gamma} alpha_t because the
    forecast curve on (t, inf) is alpha_t * e^{-theta(s-t)}, and
    D_-^{1-gamma} e^{-theta(.-t)}(t) = theta^{1-gamma}).
    Therefore:
        u^P_t = kappa_{1-gamma}/(2 sin(pi gamma/2)) * [D_+^{1-gamma} alpha_t + theta^{1-gamma} alpha_t]
              = 1/(4 c Gamma(1-gamma) sin^2(pi gamma/2)) * [D_+^{1-gamma} alpha_t + theta^{1-gamma} alpha_t]

User's policy (U) — proposed filtration Wiener-Hopf inversion (P_+ C P_+)^{-1}:
    u^U_t = kappa_{1-gamma} * D_+^beta * P_+ * D_-^beta alpha    where beta = (1-gamma)/2.
    For OU, P_+ D_-^beta alpha (s) = D_-^beta bar_alpha(s,.)(s) = theta^beta * alpha_s.
    Therefore:
        u^U_t = kappa_{1-gamma} * theta^beta * D_+^beta alpha_t
              = theta^beta / (2 c Gamma(1-gamma) sin(pi gamma/2)) * D_+^beta alpha_t

Cost: J(u) = E[ 0.5 int int G(|t-v|) u_t u_v dt dv  -  int u_t alpha_t dt ].

We compute realised per-unit-time cost J/T_window on a long simulated path and
compare J_P (paper) vs J_U (user) vs J_zero (do nothing) vs J_alpha (alpha-chase).
If the paper is correct, J_P should be the minimum.
"""
from __future__ import annotations
import numpy as np
from scipy.special import gamma as Gamma
from scipy.signal import fftconvolve


def gl_causal_weights(nu: float, K: int) -> np.ndarray:
    """Grünwald-Letnikov coefficients w_k = (-1)^k C(nu, k), k=0..K-1.
    Recurrence: w_0 = 1, w_k = w_{k-1} * (k-1-nu)/k.
    Then D_+^nu f[i] ~ dt^{-nu} * sum_{k=0}^{K-1} w_k f[i-k].
    """
    w = np.empty(K)
    w[0] = 1.0
    for k in range(1, K):
        w[k] = w[k-1] * (k - 1 - nu) / k
    return w


def gl_causal(f: np.ndarray, nu: float, dt: float, history: int) -> np.ndarray:
    """Discrete causal RL/GL derivative of order nu in (0,1)."""
    w = gl_causal_weights(nu, history)
    conv = fftconvolve(f, w, mode='full')[: len(f)]
    return conv * (dt ** (-nu))


def simulate_OU_fast(N: int, dt: float, theta: float, sigma: float, seed: int) -> np.ndarray:
    """Vectorized exact OU via cumulative AR(1)."""
    rng = np.random.default_rng(seed)
    a = np.exp(-theta * dt)
    s = sigma * np.sqrt((1 - np.exp(-2*theta*dt))/(2*theta))
    eps = rng.standard_normal(N)
    # AR(1) via lfilter
    from scipy.signal import lfilter
    alpha = lfilter([s], [1, -a], eps)
    # Replace initial value with stationary draw
    alpha[0] = rng.standard_normal() * sigma / np.sqrt(2*theta)
    return alpha


def realized_cost(u: np.ndarray, alpha: np.ndarray, idx: slice,
                  dt: float, c: float, gamma_exp: float, K_lag: int) -> tuple[float, float, float]:
    """Compute J on the test window idx, with kernel truncated to K_lag steps.

    Quadratic part: 0.5 sum_t u_t * (sum_{v: |t-v|<=K_lag, v!=t} G(|t-v|*dt) u_v) dt^2
                  + 0.5 * G_diag * sum u_t^2 dt^2 (diagonal contribution from r in (0,dt))
    where G_diag := integral_0^{dt/2} G(r) dr * 2 / dt (lumped half-cell).
    Actually we use the simpler: include all lags k=1..K and use 2 * sum_{k>=1} G(k*dt) u_t u_{t-k} dt.
    Plus a diagonal regularization integral_0^{dt} c r^{-gamma} dr = c dt^{1-gamma}/(1-gamma)
    contributing 0.5 * sum u_t^2 * c dt^{1-gamma}/(1-gamma) * 1 (interpreting it as the
    cost of the same-bin self-impact integrated over a width dt).
    """
    N = len(u)
    # Symmetric kernel for off-diagonal, then add diagonal separately
    lags = np.arange(1, K_lag+1) * dt
    G_off = c * lags ** (-gamma_exp)
    full = np.concatenate([G_off[::-1], [0.0], G_off])  # zero at zero lag
    impact = fftconvolve(u, full, mode='same') * dt
    J_off = 0.5 * np.sum(u[idx] * impact[idx]) * dt
    # Diagonal r in (0, dt): integral c r^{-gamma} dr = c dt^{1-gamma}/(1-gamma)
    diag_coef = c * dt**(1 - gamma_exp) / (1 - gamma_exp)
    J_diag = 0.5 * np.sum(u[idx]**2) * diag_coef * dt  # times dt for time integration
    # Hmm the dimensional analysis here is delicate. The continuous quadratic is
    # 0.5 int int G(|t-v|) u_t u_v dt dv with G integrable near zero (gamma<1).
    # Discrete approximation with bin width dt: 0.5 sum_t sum_v G(|t-v|) u_t u_v dt^2
    # Off-diagonal (t != v): use values at t-v = k*dt, contribution G(k*dt) per pair, dt^2.
    # Diagonal (t == v): the integral over the single bin (t-dt/2, t+dt/2) x same is
    #   approx u_t^2 * int_{-dt/2}^{dt/2}int_{-dt/2}^{dt/2} G(|t'-v'|) dt' dv'
    #   For c r^{-gamma}, this 2D integral is finite for gamma<1 and equals
    #   c * dt^{2-gamma} * I(gamma) with I(gamma) some O(1) constant.
    # We approximate it by 2 * c * dt^{2-gamma}/((1-gamma)(2-gamma)) -- but for our
    # purposes (comparing two policies) any consistent diagonal regularization will do
    # as long as we apply the same one to all candidates.
    diag_2d = 2 * c * dt**(2 - gamma_exp) / ((1 - gamma_exp) * (2 - gamma_exp))
    J_diag = 0.5 * np.sum(u[idx]**2) * diag_2d
    J_quad = J_off + J_diag
    J_lin = -np.sum(u[idx] * alpha[idx]) * dt
    return J_quad, J_lin, J_quad + J_lin


def run(gamma_exp: float = 0.4, theta: float = 1.0, sigma: float = 1.0,
        c: float = 1.0, dt: float = 0.02, T: float = 150.0,
        warmup: float = 20.0, K_history: int = 2000, K_lag_cost: int = 1500,
        n_seeds: int = 5):
    beta = (1 - gamma_exp) / 2
    sin_half = np.sin(np.pi * gamma_exp / 2)
    Gam = Gamma(1 - gamma_exp)
    kappa = 1.0 / (2 * c * Gam * sin_half)
    coef_P = 1.0 / (4 * c * Gam * sin_half ** 2)
    coef_U = (theta ** beta) / (2 * c * Gam * sin_half)
    theta_pow_full = theta ** (1 - gamma_exp)

    N = int(T / dt)
    idx_start = int(max(warmup, K_history * dt) / dt)
    idx = slice(idx_start, N - K_lag_cost - 10)

    print(f"gamma={gamma_exp}, theta={theta}, sigma={sigma}, c={c}")
    print(f"beta=(1-gamma)/2={beta:.3f}")
    print(f"coef_P (paper) = {coef_P:.6f}")
    print(f"coef_U (user)  = {coef_U:.6f}")
    print(f"theta^(1-gamma) = {theta_pow_full:.4f}")
    print(f"window: [{idx.start*dt:.1f}, {idx.stop*dt:.1f}] of T={T}")
    print()
    print(f"{'seed':>4}  {'J_zero':>10}  {'J_alpha':>10}  {'J_U (user)':>12}  {'J_P (paper)':>12}  {'gain U':>8}  {'gain P':>8}")

    rows = []
    for seed in range(n_seeds):
        alpha = simulate_OU_fast(N, dt, theta, sigma, seed)
        D_1mg = gl_causal(alpha, 1 - gamma_exp, dt, K_history)
        D_b   = gl_causal(alpha, beta,           dt, K_history)
        u_P = coef_P * (D_1mg + theta_pow_full * alpha)
        u_U = coef_U * D_b
        u_zero = np.zeros_like(alpha)
        # naive alpha-chase scaled to roughly match impact: u = alpha / G_diag for unit gain
        u_alpha = alpha.copy()

        _,_, J_zero  = realized_cost(u_zero,  alpha, idx, dt, c, gamma_exp, K_lag_cost)
        _,_, J_alpha = realized_cost(u_alpha, alpha, idx, dt, c, gamma_exp, K_lag_cost)
        _,_, J_U     = realized_cost(u_U,     alpha, idx, dt, c, gamma_exp, K_lag_cost)
        _,_, J_P     = realized_cost(u_P,     alpha, idx, dt, c, gamma_exp, K_lag_cost)

        T_win = (idx.stop - idx.start) * dt
        rows.append((seed, J_zero/T_win, J_alpha/T_win, J_U/T_win, J_P/T_win))
        print(f"{seed:>4}  {J_zero/T_win:>10.4f}  {J_alpha/T_win:>10.4f}  {J_U/T_win:>12.4f}  {J_P/T_win:>12.4f}"
              f"  {(J_zero-J_U)/T_win:>8.4f}  {(J_zero-J_P)/T_win:>8.4f}")

    arr = np.array(rows)
    means = arr[:, 1:].mean(axis=0)
    stds = arr[:, 1:].std(axis=0)
    print()
    print(f"means ± std (per unit time, over {n_seeds} seeds):")
    print(f"  J_zero  = {means[0]:+.4f} ± {stds[0]:.4f}")
    print(f"  J_alpha = {means[1]:+.4f} ± {stds[1]:.4f}")
    print(f"  J_U     = {means[2]:+.4f} ± {stds[2]:.4f}   (user W-H)")
    print(f"  J_P     = {means[3]:+.4f} ± {stds[3]:.4f}   (paper bulk)")
    print()
    if means[3] < means[2]:
        print(f"==> Paper's policy beats user's by {means[2]-means[3]:.4f} per unit time.")
    else:
        print(f"==> User's policy beats paper's by {means[3]-means[2]:.4f} per unit time.")
    return means, stds


if __name__ == "__main__":
    print("="*80)
    print("Test 1: gamma=0.4, theta=1.0")
    print("="*80)
    run(gamma_exp=0.4, theta=1.0)
    print()
    print("="*80)
    print("Test 2: gamma=0.6, theta=1.0")
    print("="*80)
    run(gamma_exp=0.6, theta=1.0)
    print()
    print("="*80)
    print("Test 3: gamma=0.4, theta=0.3 (slower mean reversion)")
    print("="*80)
    run(gamma_exp=0.4, theta=0.3)
    print()
    print("="*80)
    print("Test 4: gamma=0.4, theta=3.0 (faster mean reversion)")
    print("="*80)
    run(gamma_exp=0.4, theta=3.0)
