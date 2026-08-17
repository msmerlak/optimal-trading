"""
Verification of the information-thermodynamic bound for one-step Gaussian trading.

Setup:
    alpha ~ N(0, sigma^2)         # signal observed by trader
    u = a*alpha + s*eps           # randomized policy, eps ~ N(0,1) indep
    Pi(u, alpha) = u*alpha - 0.5*lambda*u^2     # net P&L (signal minus quadratic impact)
    I(u; alpha) = 0.5 * log(1 + a^2 sigma^2 / s^2)

Claim (to verify):
    For fixed mutual information I, the maximum expected net P&L is
        Pi_max(I) = (sigma^2 / (2*lambda)) * (1 - exp(-2*I))
    with linear small-I expansion
        Pi_max(I) ~ (sigma^2/lambda) * I,
    identifying T_trading = sigma^2/lambda as the "market temperature."
"""

import numpy as np
rng = np.random.default_rng(0)


def expected_pnl_and_mi(a, s, sigma=1.0, lam=1.0, n=2_000_000):
    """Monte Carlo: return (E[Pi], analytic MI) for a given linear-Gaussian policy."""
    alpha = rng.normal(0.0, sigma, size=n)
    eps = rng.normal(0.0, 1.0, size=n)
    u = a * alpha + s * eps
    pnl = u * alpha - 0.5 * lam * u**2
    if s > 0:
        snr = (a * sigma) ** 2 / s**2
        mi = 0.5 * np.log1p(snr)
    else:
        mi = np.inf
    return pnl.mean(), pnl.std() / np.sqrt(n), mi


def pi_max_analytic(I, sigma=1.0, lam=1.0):
    """Closed-form upper envelope: Pi_max(I) = (sigma^2 / 2 lambda) (1 - e^{-2I})."""
    return (sigma**2 / (2 * lam)) * (1.0 - np.exp(-2.0 * I))


def optimize_at_fixed_mi(I_target, sigma=1.0, lam=1.0):
    """For fixed SNR = exp(2I)-1, optimize s analytically. Recovers Pi_max."""
    snr = np.expm1(2.0 * I_target)
    # parametrize: s^2 = c, a = sqrt(SNR * c) / sigma  -> a*sigma = sqrt(SNR*c)
    # E[Pi] = sigma*sqrt(SNR*c) - 0.5*lam*c*(SNR+1)
    # optimum: c = sigma^2 SNR / (lam^2 (SNR+1)^2)
    c_opt = sigma**2 * snr / (lam**2 * (snr + 1) ** 2) if snr > 0 else 0.0
    s_opt = np.sqrt(c_opt)
    a_opt = np.sqrt(snr * c_opt) / sigma if sigma > 0 else 0.0
    pnl_opt = sigma * np.sqrt(snr * c_opt) - 0.5 * lam * c_opt * (snr + 1)
    return a_opt, s_opt, pnl_opt


if __name__ == "__main__":
    sigma, lam = 1.0, 1.0
    T_trading = sigma**2 / lam
    print(f"market temperature  T = sigma^2/lambda = {T_trading}")
    print(f"perfect-info benchmark sigma^2/(2lambda) = {sigma**2/(2*lam):.6f}")
    print()
    print(f"{'I':>8} {'a*':>10} {'s*':>10} "
          f"{'Pi_max(theory)':>16} {'Pi (sim)':>14} {'+/- 2se':>10} "
          f"{'T*I (tangent)':>14}")
    print("-" * 100)

    for I_target in [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0]:
        a_opt, s_opt, pnl_th = optimize_at_fixed_mi(I_target, sigma, lam)
        pnl_sim, se, mi_check = expected_pnl_and_mi(a_opt, s_opt, sigma, lam, n=5_000_000)
        pnl_envelope = pi_max_analytic(I_target, sigma, lam)
        tangent = T_trading * I_target
        print(f"{I_target:>8.2f} {a_opt:>10.4f} {s_opt:>10.4f} "
              f"{pnl_envelope:>16.6f} {pnl_sim:>14.6f} {2*se:>10.6f} "
              f"{tangent:>14.6f}")

    print()
    print("Check: Pi_max(I) <= T*I for all I, with equality only at I -> 0.")
    print()

    # Sweep many (a, s) on a grid and confirm none beats the envelope
    print("Grid sweep: any (a,s) policy beating Pi_max(I)?")
    a_grid = np.linspace(0.05, 3.0, 30)
    s_grid = np.linspace(0.05, 3.0, 30)
    violations = 0
    max_gap = 0.0
    for a in a_grid:
        for s in s_grid:
            snr = (a * sigma) ** 2 / s**2
            I = 0.5 * np.log1p(snr)
            pnl_th = sigma**2 * a - 0.5 * lam * (a**2 * sigma**2 + s**2)
            envelope = pi_max_analytic(I, sigma, lam)
            gap = pnl_th - envelope
            if gap > 1e-10:
                violations += 1
            max_gap = max(max_gap, gap)
    print(f"  grid points checked: {len(a_grid)*len(s_grid)}")
    print(f"  violations:          {violations}")
    print(f"  max (Pi - envelope): {max_gap:.3e}   (expect <=0 modulo numerical noise)")
