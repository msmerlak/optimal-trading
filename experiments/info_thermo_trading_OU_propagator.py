"""
Stationary OU signal + exponential propagator impact.

Goals:
    1. Compute T_market(omega) := S_alpha(omega) / (2 Re G_hat(omega)) in closed form.
    2. Compute the spectral unconstrained-information envelope
         dot Pi_envelope = int  T_market(omega) * q(omega)  d omega/(2 pi)
       where q(omega) = S_alpha/(S_alpha + S_xi) is spectral signal quality.
       (This is the upper bound when extraction efficiency e(omega) -> 1 at every freq.)
    3. Compare numerically against a specific causal filter (one-pole low-pass) policy.

Setup:
    alpha: OU, stationary variance sigma_a^2, mean-reversion rate gamma.
       S_alpha(w) = 2 gamma sigma_a^2 / (w^2 + gamma^2)
    xi: bandlimited white noise (we use OU with very large rate, gamma_xi >> gamma).
       S_xi(w) = 2 gamma_xi sigma_xi^2 / (w^2 + gamma_xi^2)
    G(tau) = lambda exp(-rho tau) 1_{tau>=0}
       G_hat(w) = lambda / (rho + i w)
       Re G_hat(w) = lambda rho / (w^2 + rho^2)

So:
    T_market(w) = [2 gamma sigma_a^2 / (w^2 + gamma^2)]
                  / [2 lambda rho / (w^2 + rho^2)]
                = gamma sigma_a^2 (w^2 + rho^2) / [lambda rho (w^2 + gamma^2)]

    Unconstrained spectral envelope (all info captured, no impact cost optimization):
       This is an upper bound — actual L-N solution is lower because impact cost
       is nonzero at the unconstrained optimum.

    Better envelope: Pi_max(omega) per Hz = T_market(w) * q(w) * 1
       integrated. We compute this numerically.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def S_alpha(w, gamma, sigma_a):
    return 2 * gamma * sigma_a**2 / (w**2 + gamma**2)


def S_xi(w, gamma_xi, sigma_xi):
    return 2 * gamma_xi * sigma_xi**2 / (w**2 + gamma_xi**2)


def Re_G_hat(w, lam, rho):
    return lam * rho / (w**2 + rho**2)


def T_market(w, gamma, sigma_a, lam, rho):
    return S_alpha(w, gamma, sigma_a) / (2 * Re_G_hat(w, lam, rho))


def spectral_quality(w, gamma, sigma_a, gamma_xi, sigma_xi):
    Sa = S_alpha(w, gamma, sigma_a)
    Sx = S_xi(w, gamma_xi, sigma_xi)
    return Sa / (Sa + Sx)


def spectral_envelope(gamma, sigma_a, gamma_xi, sigma_xi, lam, rho,
                       w_max=1e3, n_w=20000):
    """Integrate T_market * quality over frequencies (unconstrained-extraction envelope)."""
    w = np.linspace(-w_max, w_max, n_w)
    dw = w[1] - w[0]
    T = T_market(w, gamma, sigma_a, lam, rho)
    q = spectral_quality(w, gamma, sigma_a, gamma_xi, sigma_xi)
    # envelope per unit freq (Hz): T * q
    integrand = T * q
    return np.sum(integrand) * dw / (2 * np.pi)


def closed_form_T_at(w, gamma, sigma_a, lam, rho):
    """T_market(w) = gamma sigma_a^2 (w^2 + rho^2) / (lambda rho (w^2 + gamma^2))."""
    return gamma * sigma_a**2 * (w**2 + rho**2) / (lam * rho * (w**2 + gamma**2))


if __name__ == "__main__":
    # baseline parameters
    gamma = 1.0
    sigma_a = 1.0
    lam = 1.0
    rho = 1.0
    gamma_xi = 100.0  # near-white return noise
    sigma_xi = 1.0

    # check closed form vs computed T_market
    w_test = np.array([0.0, 0.5, 1.0, 2.0, 10.0])
    T_num = T_market(w_test, gamma, sigma_a, lam, rho)
    T_cf = closed_form_T_at(w_test, gamma, sigma_a, lam, rho)
    print("Closed-form check T_market(w):")
    for wi, tn, tc in zip(w_test, T_num, T_cf):
        print(f"  w={wi:>5.2f}  T(numeric)={tn:.6f}  T(closed-form)={tc:.6f}")
    print()

    # Sweep impact memory rho vs signal memory gamma
    print("Sweep rho/gamma; envelope = integral T_market(w) q(w) dw/(2pi)")
    print(f"{'gamma':>8} {'rho':>8} {'sigma_xi':>10} {'T(0)':>10} "
          f"{'T(inf)':>10} {'envelope':>12}")
    print("-" * 70)
    for gamma in [0.1, 1.0, 10.0]:
        for rho in [0.1, 1.0, 10.0]:
            for sigma_xi in [0.5, 2.0]:
                T0 = closed_form_T_at(np.array([0.0]),
                                       gamma, sigma_a, lam, rho)[0]
                Tinf = gamma * sigma_a**2 / (lam * rho)  # lim w->inf
                env = spectral_envelope(
                    gamma, sigma_a, gamma_xi, sigma_xi, lam, rho
                )
                print(f"{gamma:>8.2f} {rho:>8.2f} {sigma_xi:>10.2f} "
                      f"{T0:>10.4f} {Tinf:>10.4f} {env:>12.6f}")

    # Plot spectral picture for a representative case
    gamma, rho, sigma_xi = 1.0, 1.0, 1.0
    w = np.linspace(-10, 10, 2000)
    Sa = S_alpha(w, gamma, sigma_a)
    Sx = S_xi(w, gamma_xi, sigma_xi)
    ReG = Re_G_hat(w, lam, rho)
    T = T_market(w, gamma, sigma_a, lam, rho)
    q = spectral_quality(w, gamma, sigma_a, gamma_xi, sigma_xi)

    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0, 0].plot(w, Sa, label="S_alpha(w)")
    axes[0, 0].plot(w, Sx, label="S_xi(w)", linestyle="--")
    axes[0, 0].set_title("Signal vs return-noise spectra")
    axes[0, 0].legend()
    axes[0, 0].set_xlabel("omega")

    axes[0, 1].plot(w, ReG, color="C2")
    axes[0, 1].set_title("Re G_hat(w)  (real part of impact transfer)")
    axes[0, 1].set_xlabel("omega")

    axes[1, 0].plot(w, T, color="C3")
    axes[1, 0].set_title("T_market(w) = S_alpha / (2 Re G_hat)")
    axes[1, 0].set_xlabel("omega")

    axes[1, 1].plot(w, q, label="quality q(w)")
    axes[1, 1].plot(w, T * q / T.max(), label="T*q (normalized)",
                     linestyle="--")
    axes[1, 1].set_title("Spectral signal quality and integrand")
    axes[1, 1].legend()
    axes[1, 1].set_xlabel("omega")

    fig.tight_layout()
    out = "experiments/info_thermo_trading_OU_propagator.png"
    fig.savefig(out, dpi=120)
    print(f"\nSaved spectral plots to {out}")
