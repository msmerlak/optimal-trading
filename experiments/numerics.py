"""
Numerical experiments for the paper
'Optimal Trading with Noisy Signals and Persistent Impact'.

We verify, in the frequency domain, three theoretical claims:

  (1) For an AR(1) signal with autocorrelation rho and an exponential
      impact kernel K(n) = lam^|n|, the closed-form causal policy

          x_t = c * (f_t - lam * f_{t-1}),  c = (1 - lam*rho)/(1 - lam^2)

      attains the predicted per-period utility

          J* = 0.5 * sigma^2 * (1 - lam*rho)^2 / [(1 - lam^2)(1 - rho^2)].

      We compute J via FFT-based integration of the spectral density
      identity J(H) = E[f x] - 0.5 * E[x (K*x)] and confirm.

  (2) The causal policy strictly dominates the naive policy x_t = f_t
      (which pays unnecessary impact) and is itself dominated by the
      non-causal benchmark x = K^{-1}*f (which uses future information).

  (3) For a power-law kernel K(n) = (1 + |n|)^{-beta} (regularised at 0),
      numerical Wiener-Hopf factorisation K = K_+ K_- via the cepstrum
      yields a causal optimal filter whose impulse response decays like
      a causal fractional derivative of order (1-beta)/2.

All quantities are computed exactly (up to FFT grid discretisation), not
estimated from sample paths. Results, figures and a summary CSV are saved
under experiments/results/.

Run with:  python3 experiments/numerics.py
"""

from __future__ import annotations

import csv
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftshift, ifft, ifftshift

# ---------- output paths ----------
HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
RESULTS.mkdir(parents=True, exist_ok=True)


# ============================================================
# Generic spectral utilities
# ============================================================

def spectral_grid(N: int) -> np.ndarray:
    """Frequencies on [-pi, pi), shape (N,)."""
    return 2.0 * np.pi * (np.arange(N) - N // 2) / N


def utility_freq_domain(H: np.ndarray, S_f: np.ndarray, K_hat: np.ndarray) -> tuple[float, float, float]:
    """Per-period expected utility J(H) = E[f x] - 0.5 E[x (K*x)].

    All inputs are arrays on the spectral grid of length N.
    H is the (possibly complex) causal transfer function H_hat(omega).
    Returns (gain, cost, J = gain - cost).

    Uses J = mean over grid of [Re(H*) S_f - 0.5 |H|^2 K_hat S_f].
    Discrete sum of f_n / N approximates integral over [-pi, pi] / (2 pi).
    """
    gain = float(np.mean(np.real(np.conj(H)) * S_f))
    cost = float(0.5 * np.mean(np.abs(H) ** 2 * K_hat * S_f))
    return gain, cost, gain - cost


def cepstral_factorize(K_hat: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Wiener-Hopf factorisation K_hat = K+ * K- via the real cepstrum.

    Given K_hat real, positive, on the standard FFT grid (frequencies
    2*pi*k/N for k=0..N-1), returns (Kp_hat, Km_hat) on the same grid
    such that K_hat = Kp_hat * Km_hat and Kp_hat is the outer (causal,
    minimum-phase) factor.

    Construction: let c = real_cepstrum(K_hat) = ifft(log K_hat).
    Define
        c_+(0) = c(0)/2,  c_+(n>0) = c(n),  c_+(n<0) = 0  (causal part)
    Then K+_hat = exp(fft(c_+)).
    """
    log_K = np.log(K_hat)
    c = np.real(ifft(log_K))
    N = len(c)
    c_pos = np.zeros_like(c)
    c_pos[0] = c[0] / 2.0
    c_pos[1 : N // 2] = c[1 : N // 2]
    # n = N/2 is the Nyquist; treat symmetrically
    if N % 2 == 0:
        c_pos[N // 2] = c[N // 2] / 2.0
    Kp = np.exp(fft(c_pos))
    Km = K_hat / Kp
    return Kp, Km


def causal_projection(g_hat: np.ndarray) -> np.ndarray:
    """Project a function g_hat(omega) onto its causal part [g_hat]_+.

    In the time domain this zeroes out negative-lag coefficients of the
    inverse FFT of g_hat and halves the n=0 entry's anticausal share
    (which is zero for our use case since we only project rationals
    arising from spectral division).
    Operationally: take inverse FFT, zero out n < 0 (i.e. n = N//2 .. N-1
    in FFT ordering, treating n=N/2 conservatively), forward FFT.
    """
    N = len(g_hat)
    g_time = ifft(g_hat)
    g_caus = np.zeros_like(g_time)
    g_caus[0] = g_time[0]
    g_caus[1 : N // 2] = g_time[1 : N // 2]
    # Drop strictly anticausal entries (indices N//2 .. N-1 in FFT ordering
    # correspond to negative lags). The Nyquist bin is ambiguous; for our
    # smooth spectra it carries negligible mass and we drop it.
    return fft(g_caus)


# ============================================================
# Experiment 1: exponential kernel + AR(1) signal
# ============================================================

def exp_kernel_spectrum(lam: float, omega: np.ndarray) -> np.ndarray:
    """K_hat(omega) for K(n) = lam^|n|.

    Two-sided geometric: sum_n lam^|n| e^{-i omega n} = (1-lam^2)/(1-2 lam cos omega + lam^2).
    """
    return (1.0 - lam ** 2) / (1.0 - 2.0 * lam * np.cos(omega) + lam ** 2)


def ar1_spectrum(rho: float, sigma: float, omega: np.ndarray) -> np.ndarray:
    """S_f(omega) for AR(1) with autoreg rho, innovation std sigma."""
    return sigma ** 2 / (1.0 - 2.0 * rho * np.cos(omega) + rho ** 2)


def J_analytical_exp_ar1(lam: float, rho: float, sigma: float = 1.0) -> dict:
    """Closed-form utilities for AR(1) signal + exponential kernel."""
    c = (1.0 - lam * rho) / (1.0 - lam ** 2)
    # Causal optimum from eq (12): x_t = c (f_t - lam f_{t-1})
    J_causal = 0.5 * sigma ** 2 * (1.0 - lam * rho) ** 2 / ((1.0 - lam ** 2) * (1.0 - rho ** 2))
    # Non-causal benchmark: x = K^{-1} f  =>  H_hat = 1/K_hat
    # J_nc = 0.5 int S_f / K_hat dw/(2pi) = 0.5 sigma^2/(1-lam^2) (1-2 lam rho + lam^2)/(1-rho^2)
    J_nc = 0.5 * sigma ** 2 * (1.0 - 2.0 * lam * rho + lam ** 2) / ((1.0 - lam ** 2) * (1.0 - rho ** 2))
    # Naive H_hat = 1: J_naive = E[f^2] - 0.5 E[f (K*f)]
    # E[f^2] = sigma^2 / (1-rho^2)
    # E[f (K*f)] = int K_hat S_f dw/(2pi) = sigma^2 (1-lam^2)/[(1-lam rho)^2 - (lam-rho)^2 ... ]
    # use general identity: int K_hat S_f dw/(2pi) = sum_k K(k) R_f(k)
    # = sigma^2/(1-rho^2) * sum_k lam^|k| rho^|k| = sigma^2/(1-rho^2) * (1 + lam rho)/(1 - lam rho)
    # (geometric sum on both sides)
    Eff = sigma ** 2 / (1.0 - rho ** 2)
    EfKf = sigma ** 2 / (1.0 - rho ** 2) * (1.0 + lam * rho) / (1.0 - lam * rho)
    J_naive = Eff - 0.5 * EfKf
    return {"c": c, "J_causal": J_causal, "J_noncausal": J_nc, "J_naive": J_naive}


def numerical_exp_ar1(lam: float, rho: float, sigma: float = 1.0, N: int = 8192) -> dict:
    """Compute J(H) by FFT-grid quadrature for the three policies."""
    omega = 2.0 * np.pi * np.arange(N) / N  # standard FFT grid on [0, 2pi)
    S_f = ar1_spectrum(rho, sigma, omega)
    K_hat = exp_kernel_spectrum(lam, omega)

    # (a) Causal optimum from eq (12): H_hat(omega) = c (1 - lam e^{-i omega})
    c = (1.0 - lam * rho) / (1.0 - lam ** 2)
    H_causal = c * (1.0 - lam * np.exp(-1j * omega))
    g_caus, k_caus, J_caus = utility_freq_domain(H_causal, S_f, K_hat)

    # (b) Non-causal: H_hat = 1/K_hat
    H_nc = 1.0 / K_hat
    g_nc, k_nc, J_nc = utility_freq_domain(H_nc, S_f, K_hat)

    # (c) Naive H = 1
    H_naive = np.ones_like(omega)
    g_naive, k_naive, J_naive = utility_freq_domain(H_naive, S_f, K_hat)

    # (d) Numerical Wiener-Hopf: x_hat = K+^{-1} [f / K-]_+
    # Here "f" enters as the deterministic transfer function relating f to x.
    # For a generic stationary signal the causal optimal filter is
    #   H_hat = K+^{-1} * [ phi_f^+ / K_- ]_+  / phi_f^+   (Wiener case)
    # but for the *non-stochastic* control problem (deterministic FOC on the
    # realised f) the filter relating x to f is simply
    #   H_hat = K+^{-1} * [1/K_-]_+
    # Verify this matches H_causal up to numerical precision.
    Kp, Km = cepstral_factorize(K_hat)
    one_over_Km = 1.0 / Km
    proj = causal_projection(one_over_Km)
    H_wh = proj / Kp
    g_wh, k_wh, J_wh = utility_freq_domain(H_wh, S_f, K_hat)

    return {
        "c": c,
        "J_causal_analytical_formula": J_caus,
        "J_causal_via_WH_factorisation": J_wh,
        "J_noncausal_benchmark": J_nc,
        "J_naive": J_naive,
        "H_causal_impulse": np.real(ifft(H_causal))[: 8],
        "H_wh_impulse": np.real(ifft(H_wh))[: 8],
    }


def run_exp1() -> None:
    print("=" * 60)
    print("Experiment 1: exponential kernel + AR(1) signal")
    print("=" * 60)

    # Headline check at one parameter setting
    lam, rho, sigma = 0.5, 0.7, 1.0
    ana = J_analytical_exp_ar1(lam, rho, sigma)
    num = numerical_exp_ar1(lam, rho, sigma, N=8192)

    print(f"\n  Parameters: lam={lam}, rho={rho}, sigma={sigma}")
    print(f"  Predicted scalar c = (1-lam*rho)/(1-lam^2)        = {ana['c']:.6f}")
    print(f"  Numerical scalar c (from FFT H_causal[0])         = {num['H_causal_impulse'][0]:.6f}")
    print(f"\n  Closed-form J*_causal   = {ana['J_causal']:.6f}")
    print(f"  Numerical  J(H_causal)   = {num['J_causal_analytical_formula']:.6f}")
    print(f"  Numerical  J(H_WH)       = {num['J_causal_via_WH_factorisation']:.6f}")
    print(f"  (these three should agree to ~1e-6)")
    print(f"\n  J_noncausal benchmark   = {ana['J_noncausal']:.6f}  (analytical)")
    print(f"  J_noncausal benchmark   = {num['J_noncausal_benchmark']:.6f}  (numerical)")
    print(f"  J_naive (H=1)           = {ana['J_naive']:.6f}  (analytical)")
    print(f"  J_naive (H=1)           = {num['J_naive']:.6f}  (numerical)")
    print(f"\n  Causal/non-causal ratio  = {ana['J_causal']/ana['J_noncausal']:.4f}")
    print(f"  Causal/naive ratio       = {ana['J_causal']/ana['J_naive']:.4f}")
    print(f"\n  Causal impulse response (lags 0..3): {num['H_causal_impulse'][:4]}")
    print(f"  WH-numerical impulse     (lags 0..3): {num['H_wh_impulse'][:4]}")

    # Sweep over (lam, rho)
    lams = np.linspace(0.05, 0.9, 18)
    rhos = np.linspace(0.05, 0.9, 18)
    LAM, RHO = np.meshgrid(lams, rhos, indexing="ij")
    J_c = np.zeros_like(LAM)
    J_nc = np.zeros_like(LAM)
    J_na = np.zeros_like(LAM)
    err_formula_vs_wh = np.zeros_like(LAM)
    for i, lm in enumerate(lams):
        for j, rh in enumerate(rhos):
            ana_ij = J_analytical_exp_ar1(lm, rh, 1.0)
            num_ij = numerical_exp_ar1(lm, rh, 1.0, N=4096)
            J_c[i, j] = ana_ij["J_causal"]
            J_nc[i, j] = ana_ij["J_noncausal"]
            J_na[i, j] = ana_ij["J_naive"]
            err_formula_vs_wh[i, j] = abs(
                num_ij["J_causal_analytical_formula"] - num_ij["J_causal_via_WH_factorisation"]
            )

    max_abs_disagreement = float(err_formula_vs_wh.max())
    print(f"\n  Max |J_formula - J_WH| over (lam,rho) sweep: {max_abs_disagreement:.2e}")
    assert max_abs_disagreement < 1e-3, "Closed form and numerical WH should agree"

    # Save sweep CSV
    csv_path = RESULTS / "exp1_sweep.csv"
    with csv_path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["lambda", "rho", "J_causal", "J_noncausal", "J_naive", "causal_over_naive", "causal_over_nc"])
        for i, lm in enumerate(lams):
            for j, rh in enumerate(rhos):
                w.writerow([
                    f"{lm:.4f}",
                    f"{rh:.4f}",
                    f"{J_c[i, j]:.6f}",
                    f"{J_nc[i, j]:.6f}",
                    f"{J_na[i, j]:.6f}",
                    f"{(J_c[i, j] / J_na[i, j] if J_na[i, j] > 0 else float('nan')):.4f}",
                    f"{J_c[i, j] / J_nc[i, j]:.4f}",
                ])
    print(f"  saved sweep -> {csv_path}")

    # ---- Figure 1: utility comparison vs lam at fixed rho ----
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    rho_fixed = 0.5
    lam_grid = np.linspace(0.05, 0.9, 60)
    Jc = np.array([J_analytical_exp_ar1(l, rho_fixed)["J_causal"] for l in lam_grid])
    Jnc = np.array([J_analytical_exp_ar1(l, rho_fixed)["J_noncausal"] for l in lam_grid])
    Jna = np.array([J_analytical_exp_ar1(l, rho_fixed)["J_naive"] for l in lam_grid])
    ax = axes[0]
    ax.plot(lam_grid, Jnc, "k--", label="non-causal benchmark $K^{-1}f$")
    ax.plot(lam_grid, Jc, "b-", lw=2, label="causal optimum (eq 12)")
    ax.plot(lam_grid, Jna, "r-", label="naive $x=f$")
    ax.axhline(0, color="gray", lw=0.5)
    ax.set_xlabel(r"impact decay $\lambda$")
    ax.set_ylabel("per-period utility $J$")
    ax.set_title(rf"$\rho={rho_fixed}$ fixed, $\sigma=1$")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)

    # ---- Figure 1b: causal/naive ratio as heatmap ----
    ax = axes[1]
    ratio = J_c / np.where(J_na > 0, J_na, np.nan)
    im = ax.imshow(
        ratio,
        origin="lower",
        extent=(rhos[0], rhos[-1], lams[0], lams[-1]),
        aspect="auto",
        cmap="viridis",
    )
    ax.set_xlabel(r"signal autocorrelation $\rho$")
    ax.set_ylabel(r"impact decay $\lambda$")
    ax.set_title(r"utility ratio: causal optimum / naive $x=f$")
    fig.colorbar(im, ax=ax, label="ratio")
    fig.tight_layout()
    fig.savefig(RESULTS / "exp1_utility.png", dpi=140)
    plt.close(fig)
    print(f"  saved figure -> {RESULTS/'exp1_utility.png'}")

    # ---- Figure 2: impulse response check ----
    fig, ax = plt.subplots(figsize=(7, 4))
    lam_demo, rho_demo = 0.6, 0.4
    num_demo = numerical_exp_ar1(lam_demo, rho_demo, 1.0, N=2048)
    lags = np.arange(8)
    c_demo = (1 - lam_demo * rho_demo) / (1 - lam_demo ** 2)
    expected = np.zeros(8)
    expected[0] = c_demo
    expected[1] = -lam_demo * c_demo
    ax.stem(lags - 0.1, num_demo["H_causal_impulse"], linefmt="b-", markerfmt="bo", basefmt=" ", label="eq (12)")
    ax.stem(lags + 0.1, num_demo["H_wh_impulse"], linefmt="r-", markerfmt="rs", basefmt=" ", label="numerical Wiener-Hopf")
    ax.plot(lags, expected, "kx", ms=10, label="predicted (analytical)")
    ax.axhline(0, color="gray", lw=0.5)
    ax.set_xlabel("lag $k$")
    ax.set_ylabel(r"$H(k)$  (filter coefficient)")
    ax.set_title(rf"Optimal causal filter impulse response, $\lambda={lam_demo}$, $\rho={rho_demo}$")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(RESULTS / "exp1_impulse.png", dpi=140)
    plt.close(fig)
    print(f"  saved figure -> {RESULTS/'exp1_impulse.png'}")

    return {
        "headline_params": (lam, rho, sigma),
        "headline_analytical": ana,
        "headline_numerical": {k: v for k, v in num.items() if not isinstance(v, np.ndarray)},
        "max_disagreement_formula_vs_WH": max_abs_disagreement,
    }


# ============================================================
# Experiment 2: power-law kernel
# ============================================================

def powerlaw_kernel_time(beta: float, n_max: int) -> np.ndarray:
    """K(n) = (1 + |n|)^{-beta} for n in [-n_max, n_max].

    The +1 regularises the n=0 entry. Returns a length 2*n_max+1 symmetric
    array centred at index n_max.
    """
    n = np.arange(-n_max, n_max + 1)
    return (1.0 + np.abs(n)) ** (-beta)


def powerlaw_kernel_spectrum(beta: float, N: int) -> tuple[np.ndarray, np.ndarray]:
    """Build the spectrum K_hat of the symmetric, regularised power-law kernel.

    Uses a long truncation (N samples wide) and direct DFT of the time-domain
    kernel placed at the origin.
    Returns (omega, K_hat) on the standard FFT grid.
    """
    n_max = N // 2 - 1
    K_time = powerlaw_kernel_time(beta, n_max)
    # Place K(n=0) at index 0, K(n=k) at index k for k>0, K(n=-k) at index N-k
    K_padded = np.zeros(N)
    K_padded[0] = K_time[n_max]  # n=0
    for k in range(1, n_max + 1):
        K_padded[k] = K_time[n_max + k]
        K_padded[N - k] = K_time[n_max - k]
    K_hat = np.real(fft(K_padded))
    # Ensure strict positivity (small numerical floor)
    K_hat = np.maximum(K_hat, 1e-10 * K_hat.max())
    omega = 2.0 * np.pi * np.arange(N) / N
    return omega, K_hat


def run_exp2() -> None:
    print()
    print("=" * 60)
    print("Experiment 2: power-law kernel + AR(1) signal")
    print("=" * 60)

    rho = 0.5
    N = 8192
    betas = [0.3, 0.5, 0.7]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

    results = {}
    for beta in betas:
        omega, K_hat = powerlaw_kernel_spectrum(beta, N)
        S_f = ar1_spectrum(rho, 1.0, omega)
        Kp, Km = cepstral_factorize(K_hat)

        # Sanity check: Kp * Km should equal K_hat
        recon_err = float(np.max(np.abs(Kp * Km - K_hat)) / np.max(K_hat))

        # Optimal causal filter
        proj = causal_projection(1.0 / Km)
        H_wh = proj / Kp

        # Naive policy x = f and non-causal x = K^{-1} f
        H_naive = np.ones_like(omega)
        H_nc = 1.0 / K_hat

        _, _, J_wh = utility_freq_domain(H_wh, S_f, K_hat)
        _, _, J_naive = utility_freq_domain(H_naive, S_f, K_hat)
        _, _, J_nc = utility_freq_domain(H_nc, S_f, K_hat)

        # Impulse response of K+^{-1} alone (the "innovation operator")
        innov_hat = 1.0 / Kp
        innov_time = np.real(ifft(innov_hat))
        # Full optimal filter impulse response
        H_time = np.real(ifft(H_wh))

        print(f"\n  beta = {beta}")
        print(f"    factorisation error      max|Kp*Km - K_hat| / max K_hat = {recon_err:.2e}")
        print(f"    J(H_causal)              = {J_wh:.6f}")
        print(f"    J(non-causal benchmark)  = {J_nc:.6f}")
        print(f"    J(naive)                 = {J_naive:.6f}")
        print(f"    causal / non-causal      = {J_wh/J_nc:.4f}")
        print(f"    causal / naive           = {J_wh/J_naive:.4f}" if J_naive > 0 else
              f"    causal / naive           = +inf (naive has negative utility)")
        results[beta] = {
            "J_causal": J_wh,
            "J_noncausal": J_nc,
            "J_naive": J_naive,
            "factorisation_max_relerr": recon_err,
        }

        # Plot K+^{-1} impulse response: this is the "causal fractional derivative"
        # Theory: for K_hat ~ |omega|^{beta-1} near 0, K+ ~ (-i omega)^{(beta-1)/2},
        # so K+^{-1} ~ (-i omega)^{(1-beta)/2}. Its time-domain impulse response
        # decays like n^{-(1+(1-beta)/2)} = n^{-(3-beta)/2}.
        n_show = 120
        axes[0].plot(np.arange(n_show), innov_time[:n_show], label=rf"$\beta={beta}$")

        # Plot the full optimal filter
        axes[1].plot(np.arange(n_show), H_time[:n_show], label=rf"$\beta={beta}$")

    axes[0].set_yscale("symlog", linthresh=1e-3)
    axes[0].set_xscale("symlog", linthresh=1)
    axes[0].set_xlabel("lag $k$")
    axes[0].set_ylabel(r"$(K_+^{-1})_k$  (causal innovation kernel)")
    axes[0].set_title(r"$K_+^{-1}$ impulse response (causal fractional derivative)")
    axes[0].axhline(0, color="gray", lw=0.5)
    axes[0].legend(fontsize=9)
    axes[0].grid(alpha=0.3, which="both")

    axes[1].set_xlabel("lag $k$")
    axes[1].set_ylabel(r"$H^\star(k)$")
    axes[1].set_title(rf"Full optimal causal filter, AR(1) signal ($\rho={rho}$)")
    axes[1].axhline(0, color="gray", lw=0.5)
    axes[1].legend(fontsize=9)
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(RESULTS / "exp2_powerlaw_impulse.png", dpi=140)
    plt.close(fig)
    print(f"\n  saved figure -> {RESULTS/'exp2_powerlaw_impulse.png'}")

    # ---- Verify the predicted power-law tail of K+^{-1}: |h(n)| ~ n^{-(3-beta)/2} ----
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    for beta in betas:
        omega, K_hat = powerlaw_kernel_spectrum(beta, N)
        Kp, _ = cepstral_factorize(K_hat)
        innov_time = np.real(ifft(1.0 / Kp))
        n_range = np.arange(2, 200)
        h_abs = np.abs(innov_time[n_range])
        # Avoid log(0)
        valid = h_abs > 1e-12
        n_v = n_range[valid]
        h_v = h_abs[valid]
        # Fit slope in log-log
        slope, intercept = np.polyfit(np.log(n_v), np.log(h_v), 1)
        predicted = -(3.0 - beta) / 2.0
        print(f"    beta={beta}: empirical tail slope of |K+^-1| = {slope:.3f}, predicted = {predicted:.3f}")
        ax.loglog(n_v, h_v, "o", ms=3, label=rf"$\beta={beta}$ (slope {slope:.2f}, pred {predicted:.2f})")

    ax.set_xlabel("lag $n$")
    ax.set_ylabel(r"$|(K_+^{-1})_n|$")
    ax.set_title(r"Tail decay of causal innovation kernel")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(RESULTS / "exp2_tail_decay.png", dpi=140)
    plt.close(fig)
    print(f"  saved figure -> {RESULTS/'exp2_tail_decay.png'}")

    # Save summary CSV
    csv_path = RESULTS / "exp2_powerlaw_summary.csv"
    with csv_path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["beta", "J_causal", "J_noncausal", "J_naive", "causal_over_nc", "factor_err"])
        for beta, r in results.items():
            w.writerow([
                beta,
                f"{r['J_causal']:.6f}",
                f"{r['J_noncausal']:.6f}",
                f"{r['J_naive']:.6f}",
                f"{r['J_causal']/r['J_noncausal']:.4f}",
                f"{r['factorisation_max_relerr']:.2e}",
            ])
    print(f"  saved summary -> {csv_path}")

    return results


# ============================================================
# Run all
# ============================================================
if __name__ == "__main__":
    np.set_printoptions(precision=5, suppress=True)
    r1 = run_exp1()
    r2 = run_exp2()
    print()
    print("=" * 60)
    print("All experiments complete. Artifacts in experiments/results/")
    print("=" * 60)
