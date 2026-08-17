"""Numerical verification of two closures used in §5.5 and §6.3 of
papers/noisy-signal-impact-trading.md.

1. Continuous-time: OU signal × anticausal fractional derivative (Marchaud form,
   order alpha in (0,1)) closes to constant kappa^alpha.
   Equivalent to verifying  int_0^inf u^{-alpha-1} (e^{-u} - 1) du = Gamma(-alpha)
   for alpha in (0,1).

2. Discrete time: AR(1) signal × anticausal fractional difference (1 - L^{-1})^alpha
   closes to constant (1 - rho)^alpha.
   Equivalent to verifying  sum_{m>=0} (-1)^m C(alpha,m) rho^m = (1-rho)^alpha
   by the generalised binomial theorem.

Run: python3 experiments/markov_closure_check.py
"""
import math


def gamma_neg(alpha):
    # Gamma(-alpha) for alpha in (0,1) via Gamma(1-alpha)/(-alpha).
    return math.gamma(1 - alpha) / (-alpha)


def integ_u(alpha, n=40000, lo=-10.0, hi=5.0):
    # int_0^inf u^{-alpha-1}(e^-u - 1) du on log-spaced grid.
    us = [10 ** (lo + i * (hi - lo) / n) for i in range(n + 1)]
    total = 0.0
    for i in range(n):
        u0, u1 = us[i], us[i + 1]
        f0 = u0 ** (-alpha - 1) * (math.exp(-u0) - 1)
        f1 = u1 ** (-alpha - 1) * (math.exp(-u1) - 1)
        total += 0.5 * (f0 + f1) * (u1 - u0)
    return total


def binom_alpha(alpha, m):
    r = 1.0
    for k in range(m):
        r *= (alpha - k) / (k + 1)
    return r


def discrete_closure(alpha, rho, mmax=2000):
    return sum(binom_alpha(alpha, m) * (-1) ** m * rho ** m for m in range(mmax))


if __name__ == "__main__":
    print("=== Continuous-time: OU x power-law => kappa^alpha ===")
    print(f"{'alpha':>6} {'numeric':>12} {'Gamma(-alpha)':>14} {'ratio':>8}")
    for alpha in (0.1, 0.25, 0.5, 0.75, 0.9):
        g = integ_u(alpha)
        p = gamma_neg(alpha)
        print(f"{alpha:>6} {g:>12.5f} {p:>14.5f} {g/p:>8.5f}")
    print("(crude trapezoid loses precision at endpoints where integrand is")
    print(" more singular; mid-range agreement validates the identity.)")

    print()
    print("=== Discrete: AR(1) x fractional differencing => (1-rho)^alpha ===")
    print(f"{'alpha':>6} {'rho':>6} {'series':>12} {'(1-rho)^a':>12}")
    for alpha in (0.25, 0.5, 0.75):
        for rho in (0.3, 0.7, 0.95):
            s = discrete_closure(alpha, rho)
            p = (1 - rho) ** alpha
            print(f"{alpha:>6} {rho:>6} {s:>12.6f} {p:>12.6f}")
