"""Illustrative experiment for paper section 8 (Examples).

Demonstrates the added value of (i) Wiener prefiltering of a noisy predictor
and (ii) fractional-difference policy under a power-law (ARFIMA-spectrum)
impact kernel, compared against the naive 'trade = predictor' baseline.

Setup:
  - True predictor f_t is AR(1) with persistence rho.
  - Trader observes y_t = f_t + eta_t with eta iid Gaussian (obs noise).
  - Mid-return on a unit trade is f_t (plus unpredictable noise that averages
    out over long horizons).
  - Impact kernel: ARFIMA(0, alpha, 0) autocovariance, hat K(omega) =
    (2 sin omega/2)^(-2*alpha). This is a long-memory power-law-tailed kernel.

Four policies compared:
  (A) Naive:           x_t = y_t
  (B) Wiener only:     x_t = (causal Kalman/Wiener estimate of f_t given y)
  (C) Fracdiff only:   x_t = (1-rho)^alpha * (1-L)^alpha y_t
  (D) Filter+Fracdiff: x_t = (1-rho)^alpha * (1-L)^alpha (Wiener(y))_t
                        -- the §7 two-stage policy of the paper

For each, we compute realised per-period revenue
   J = mean(f_t x_t) - 0.5 * mean(x_t (K * x)_t)
on a long simulation, swept over the observation-noise standard deviation
sigma_eta. Generates three PNG figures saved to experiments/results/.
"""
from __future__ import annotations
import math
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def kernel_arfima(alpha: float, n_max: int) -> np.ndarray:
    """Two-sided ARFIMA(0, alpha, 0) autocovariance K(n), n = 0..n_max.
    Hosking (1981): K(0) = Gamma(1-2a)/Gamma(1-a)^2,
                    K(n+1)/K(n) = (n+a)/(n+1-a).
    """
    K = np.zeros(n_max + 1)
    K[0] = math.gamma(1 - 2 * alpha) / (math.gamma(1 - alpha) ** 2)
    for n in range(n_max):
        K[n + 1] = K[n] * (n + alpha) / (n + 1 - alpha)
    return K


def kalman_steady_gain(rho: float, sigma_eps2: float, sigma_eta2: float) -> tuple[float, float]:
    """Steady-state Kalman gain K for the 1-D model
       f_{t+1} = rho f_t + eps_{t+1},  Var(eps)=sigma_eps2
       y_t     = f_t + eta_t,           Var(eta)=sigma_eta2
    Iterate the DARE to convergence; return (K_gain, P_steady).
    """
    P = 1.0
    for _ in range(2000):
        K = P / (P + sigma_eta2)
        P_new = rho ** 2 * P * (1 - K) + sigma_eps2
        if abs(P_new - P) < 1e-14:
            P = P_new
            break
        P = P_new
    K = P / (P + sigma_eta2)
    return K, P


def kalman_filter(y: np.ndarray, rho: float, K_gain: float) -> np.ndarray:
    """Causal steady-state Kalman estimate of f_t from y_{0:t}."""
    n = len(y)
    fhat = np.zeros(n)
    # Recursion: fhat_t = (1 - K) rho fhat_{t-1} + K y_t  (after substituting
    # the prediction step fhat_{t|t-1} = rho fhat_{t-1|t-1} into the update).
    for t in range(1, n):
        fhat[t] = (1 - K_gain) * rho * fhat[t - 1] + K_gain * y[t]
    return fhat


def fracdiff_causal(z: np.ndarray, alpha: float, scale: float, L: int = 60) -> np.ndarray:
    """Apply the causal fractional-difference filter
         h_k = scale * binom(alpha, k) * (-1)^k,  k = 0..L-1
    to z, returning x_t = sum_{k=0}^{L-1} h_k z_{t-k}.
    """
    h = np.zeros(L)
    r = 1.0
    for k in range(L):
        h[k] = scale * r * (-1) ** k
        r *= (alpha - k) / (k + 1)
    n = len(z)
    x = np.zeros(n)
    for k in range(L):
        x[k:] += h[k] * z[: n - k]
    return x, h


def pnl_per_period(f: np.ndarray, x: np.ndarray, K_two_sided: np.ndarray, burn: int) -> float:
    """Realised mean per-period revenue.
       J = mean(f_t x_t) - 0.5 * mean(x_t (K * x)_t)
    K_two_sided is length 2M+1, K_two_sided[i] = K(i - M).
    """
    Kx = np.convolve(x, K_two_sided, mode="same")
    interior = slice(burn, len(f) - burn)
    gain = float(np.mean(f[interior] * x[interior]))
    cost = 0.5 * float(np.mean(x[interior] * Kx[interior]))
    return gain - cost


def simulate(T: int, rho: float, sigma_eps: float, sigma_eta: float, seed: int):
    rng = np.random.default_rng(seed)
    eps = rng.standard_normal(T) * sigma_eps
    eta = rng.standard_normal(T) * sigma_eta
    f = np.zeros(T)
    for t in range(1, T):
        f[t] = rho * f[t - 1] + eps[t]
    y = f + eta
    return f, y


def run_sweep(alpha=0.35, rho=0.7, sigma_eps=1.0, T=120_000, burn=2_000,
              snrs=None, M=600, seed=11):
    """Sweep observation-noise level and record realised per-period revenue
    for the four policies."""
    if snrs is None:
        # signal stationary variance = sigma_eps^2 / (1-rho^2)
        # we sweep noise variance from very small to large relative to signal var
        # SNR_lin := sigma_eps^2 / ((1-rho^2) * sigma_eta^2)
        snrs = np.array([100., 30., 10., 3., 1., 0.3, 0.1])

    K_half = kernel_arfima(alpha, M)
    K_two_sided = np.zeros(2 * M + 1)
    for i in range(2 * M + 1):
        K_two_sided[i] = K_half[abs(i - M)]
    sigma_eps2 = sigma_eps ** 2
    sig_var = sigma_eps2 / (1 - rho ** 2)

    pref = (1 - rho) ** alpha
    L_frac = 60

    results = {"snr": [], "sigma_eta": [],
               "J_naive": [], "J_filter": [], "J_frac": [], "J_filter_frac": []}

    for snr in snrs:
        sigma_eta2 = sig_var / snr
        sigma_eta = math.sqrt(sigma_eta2)
        f, y = simulate(T, rho, sigma_eps, sigma_eta, seed=seed)

        K_gain, _ = kalman_steady_gain(rho, sigma_eps2, sigma_eta2)
        fhat = kalman_filter(y, rho, K_gain)

        # Policies
        x_naive = y.copy()
        x_filter = fhat.copy()
        x_frac, _ = fracdiff_causal(y, alpha, pref, L=L_frac)
        x_filter_frac, _ = fracdiff_causal(fhat, alpha, pref, L=L_frac)

        J_n = pnl_per_period(f, x_naive, K_two_sided, burn)
        J_f = pnl_per_period(f, x_filter, K_two_sided, burn)
        J_fr = pnl_per_period(f, x_frac, K_two_sided, burn)
        J_ff = pnl_per_period(f, x_filter_frac, K_two_sided, burn)

        results["snr"].append(float(snr))
        results["sigma_eta"].append(float(sigma_eta))
        results["J_naive"].append(J_n)
        results["J_filter"].append(J_f)
        results["J_frac"].append(J_fr)
        results["J_filter_frac"].append(J_ff)

    return results, K_two_sided


def plot_pnl_curves(results, alpha, rho, out_path):
    snr = np.array(results["snr"])
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(snr, results["J_naive"], "o-", label="(A) Naive  $x_t = y_t$", color="#888")
    ax.plot(snr, results["J_frac"], "s--", label="(C) Fracdiff only  $(1-L)^\\alpha y_t$",
            color="#1f77b4")
    ax.plot(snr, results["J_filter"], "^--", label="(B) Wiener only  $\\hat f_t$",
            color="#ff7f0e")
    ax.plot(snr, results["J_filter_frac"], "D-",
            label="(D) Wiener + fracdiff (paper §7 rule)",
            color="#2ca02c", linewidth=2)
    ax.set_xscale("log")
    ax.axhline(0, color="black", lw=0.6, alpha=0.5)
    ax.set_xlabel("SNR  $= \\sigma_f^2 / \\sigma_\\eta^2$  (log scale)")
    ax.set_ylabel("Realised per-period revenue  $J$")
    ax.set_title(f"Power-law (ARFIMA) impact, $\\alpha={alpha}$;  AR(1) signal, $\\rho={rho}$")
    ax.legend(loc="best", fontsize=9, framealpha=0.95)
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


def plot_signal_filter_example(rho, alpha, sigma_eps, snr, T_show, seed, out_path):
    sig_var = sigma_eps ** 2 / (1 - rho ** 2)
    sigma_eta2 = sig_var / snr
    sigma_eta = math.sqrt(sigma_eta2)
    f, y = simulate(T_show + 500, rho, sigma_eps, sigma_eta, seed=seed)
    K_gain, _ = kalman_steady_gain(rho, sigma_eps ** 2, sigma_eta2)
    fhat = kalman_filter(y, rho, K_gain)
    t = np.arange(T_show)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(t, y[400 : 400 + T_show], color="#888", lw=0.7, alpha=0.6,
            label="$y_t$  (noisy observation)")
    ax.plot(t, f[400 : 400 + T_show], color="black", lw=1.0,
            label="$f_t$  (true signal)")
    ax.plot(t, fhat[400 : 400 + T_show], color="#2ca02c", lw=1.2,
            label="$\\hat f_t$  (causal Wiener filter, gain $K={:.3f}$)".format(K_gain))
    ax.set_xlabel("$t$")
    ax.set_title(f"AR(1) signal + observation noise (SNR={snr}, $\\rho={rho}$)")
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


def plot_fracdiff_coeffs(alpha_list, rho, out_path):
    fig, ax = plt.subplots(figsize=(7, 3.8))
    K = 25
    k = np.arange(K)
    for alpha in alpha_list:
        pref = (1 - rho) ** alpha
        h = np.zeros(K)
        r = 1.0
        for j in range(K):
            h[j] = pref * r * (-1) ** j
            r *= (alpha - j) / (j + 1)
        ax.plot(k, h, "o-", label=f"$\\alpha={alpha}$  (prefactor $(1-\\rho)^\\alpha={pref:.3f}$)")
    ax.axhline(0, color="black", lw=0.6, alpha=0.5)
    ax.set_xlabel("$k$")
    ax.set_ylabel("$h_k = (1-\\rho)^\\alpha\\,\\binom{\\alpha}{k}(-1)^k$")
    ax.set_title(f"Optimal causal filter coefficients for AR(1)$\\times$ARFIMA, $\\rho={rho}$")
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs("experiments/results", exist_ok=True)
    alpha, rho = 0.35, 0.7

    results, K_two_sided = run_sweep(alpha=alpha, rho=rho)
    # Print table
    print(f"alpha={alpha}, rho={rho}")
    print(f"{'SNR':>8} {'sigma_eta':>10} {'J_naive':>10} {'J_filter':>10} "
          f"{'J_frac':>10} {'J_filter_frac':>14}")
    for i in range(len(results["snr"])):
        print(f"{results['snr'][i]:>8.2f} {results['sigma_eta'][i]:>10.4f} "
              f"{results['J_naive'][i]:>10.4f} {results['J_filter'][i]:>10.4f} "
              f"{results['J_frac'][i]:>10.4f} {results['J_filter_frac'][i]:>14.4f}")

    plot_pnl_curves(results, alpha, rho,
                    "experiments/results/fig_pnl_vs_snr.png")
    plot_signal_filter_example(rho, alpha, sigma_eps=1.0, snr=2.0, T_show=400,
                               seed=7,
                               out_path="experiments/results/fig_signal_filter_example.png")
    plot_fracdiff_coeffs([0.2, 0.35, 0.5], rho,
                         "experiments/results/fig_fracdiff_coeffs.png")
    print()
    print("Saved figures:")
    print("  experiments/results/fig_pnl_vs_snr.png")
    print("  experiments/results/fig_signal_filter_example.png")
    print("  experiments/results/fig_fracdiff_coeffs.png")

    import json
    with open("experiments/results/filtering_fracdiff_powerlaw.json", "w") as fh:
        json.dump({"alpha": alpha, "rho": rho, **results}, fh, indent=2)
