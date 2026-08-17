"""
Verification of the two-information bound for one-step Gaussian trading
with return noise.

Setup:
    alpha ~ N(0, sigma_alpha^2)        # signal observed by trader
    xi    ~ N(0, sigma_xi^2)           # unpredictable return noise, indep of alpha
    r = alpha + xi                     # realized per-unit return
    u = a*alpha + s*eps,  eps ~ N(0,1) # randomized policy (sees alpha, not r)
    Pi  = u*r - 0.5*lambda*u^2

Three mutual informations:
    I_ar = 0.5*log(1 + sigma_alpha^2 / sigma_xi^2)     # signal quality
    I_ua = 0.5*log(1 + a^2 sigma_alpha^2 / s^2)         # extraction
    I_ur                                                # induced trade-return MI

Claims:
    (i)  1 - exp(-2 I_ur) = (1 - exp(-2 I_ua)) * (1 - exp(-2 I_ar)).
    (ii) Pi_max(I_ua, I_ar) = (sigma_r^2 / (2 lambda)) *
                              (1 - exp(-2 I_ua)) * (1 - exp(-2 I_ar))
                            = (sigma_r^2 / (2 lambda)) * (1 - exp(-2 I_ur)).
    (iii) Numerical sweep: no policy beats the envelope.
"""

import numpy as np

rng = np.random.default_rng(0)


def mi_gaussian(rho2):
    if rho2 >= 1.0:
        return np.inf
    return -0.5 * np.log1p(-rho2)


def run_policy(a, s, sigma_a, sigma_xi, lam, n=2_000_000):
    alpha = rng.normal(0.0, sigma_a, size=n)
    xi = rng.normal(0.0, sigma_xi, size=n)
    eps = rng.normal(0.0, 1.0, size=n)
    r = alpha + xi
    u = a * alpha + s * eps
    pnl = u * r - 0.5 * lam * u**2
    # empirical correlations
    rho_ua = np.corrcoef(u, alpha)[0, 1]
    rho_ar = np.corrcoef(alpha, r)[0, 1]
    rho_ur = np.corrcoef(u, r)[0, 1]
    return pnl.mean(), pnl.std() / np.sqrt(n), rho_ua, rho_ar, rho_ur


def envelope(I_ua, I_ar, sigma_r, lam):
    return (sigma_r**2 / (2 * lam)) * (1 - np.exp(-2 * I_ua)) * (1 - np.exp(-2 * I_ar))


def optimal_policy_at_fixed_I_ua(I_ua, sigma_a, lam):
    snr = np.expm1(2.0 * I_ua)
    c_opt = sigma_a**2 * snr / (lam**2 * (snr + 1) ** 2) if snr > 0 else 0.0
    s_opt = np.sqrt(c_opt)
    a_opt = np.sqrt(snr * c_opt) / sigma_a if sigma_a > 0 else 0.0
    return a_opt, s_opt


if __name__ == "__main__":
    lam = 1.0
    # vary signal quality and extraction independently
    print(f"{'sigma_a':>8} {'sigma_xi':>9} {'I_ar':>8} {'I_ua':>8} "
          f"{'env(theory)':>12} {'pnl(sim)':>11} {'+/-2se':>9} "
          f"{'rho_ur^2':>10} {'prod check':>12}")
    print("-" * 110)

    for sigma_a in [0.5, 1.0, 2.0]:
        for sigma_xi in [0.1, 1.0, 3.0]:
            sigma_r = np.sqrt(sigma_a**2 + sigma_xi**2)
            I_ar = mi_gaussian(sigma_a**2 / sigma_r**2)
            for I_ua in [0.1, 0.5, 2.0]:
                a, s = optimal_policy_at_fixed_I_ua(I_ua, sigma_a, lam)
                pnl_sim, se, rua, rar, rur = run_policy(
                    a, s, sigma_a, sigma_xi, lam, n=2_000_000
                )
                env_th = envelope(I_ua, I_ar, sigma_r, lam)
                # Check the product identity:
                #   1 - exp(-2 I_ur) =?= (1 - exp(-2 I_ua))*(1 - exp(-2 I_ar))
                lhs = rur**2
                rhs = (1 - np.exp(-2 * I_ua)) * (1 - np.exp(-2 * I_ar))
                print(
                    f"{sigma_a:>8.2f} {sigma_xi:>9.2f} {I_ar:>8.4f} {I_ua:>8.4f} "
                    f"{env_th:>12.6f} {pnl_sim:>11.6f} {2*se:>9.6f} "
                    f"{lhs:>10.6f} {rhs:>12.6f}"
                )

    print()
    print("Notes:")
    print("  env(theory) = (sigma_r^2 / 2 lambda) (1-exp(-2 I_ua))(1-exp(-2 I_ar))")
    print("  prod check  =                       (1-exp(-2 I_ua))(1-exp(-2 I_ar))")
    print("  rho_ur^2    = 1 - exp(-2 I_ur)  empirical; should match prod check.")

    # grid sweep: any policy beating the envelope?
    print()
    print("Grid sweep over 1000 random (a,s) policies, sigma_a=1, sigma_xi=2:")
    sigma_a, sigma_xi = 1.0, 2.0
    sigma_r = np.sqrt(sigma_a**2 + sigma_xi**2)
    I_ar = mi_gaussian(sigma_a**2 / sigma_r**2)
    violations = 0
    max_gap = -np.inf
    for _ in range(1000):
        a = rng.uniform(-2, 2)
        s = rng.uniform(0.05, 3.0)
        # analytic expected P&L (need not simulate)
        pnl_th = a * sigma_a**2 - 0.5 * lam * (a**2 * sigma_a**2 + s**2)
        I_ua = 0.5 * np.log1p(a**2 * sigma_a**2 / s**2)
        env_th = envelope(I_ua, I_ar, sigma_r, lam)
        gap = pnl_th - env_th
        if gap > 1e-10:
            violations += 1
        max_gap = max(max_gap, gap)
    print(f"  violations: {violations} / 1000")
    print(f"  max (pnl_th - envelope): {max_gap:.3e}  (expect <=0)")
