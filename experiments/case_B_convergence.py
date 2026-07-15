"""Convergence of operator-resolvent solution to closed form as FIR length L grows.

Tests the conjecture that the small gap in Case B is finite-truncation bias:
closed form h_k = (1-rho)^alpha * C(alpha,k) * (-1)^k has infinite support;
operator solver at finite L finds best length-L FIR, which differs from truncated
closed form. As L -> infinity both should converge.
"""
from __future__ import annotations
import math
import numpy as np
from closed_form_vs_operator import (
    autocorr_ar1, kernel_arfima, solve_normal_eqs, expected_revenue,
)


def binom_alpha(a, m):
    r = 1.0
    for k in range(m):
        r *= (a - k) / (k + 1)
    return r


def run(alpha=0.3, rho=0.7):
    sigma = 1.0
    M = 2000  # need very wide truncation for long-memory kernel
    K_half = kernel_arfima(alpha, M)
    K_arr = np.zeros(2 * M + 1)
    for i in range(2 * M + 1):
        K_arr[i] = K_half[abs(i - M)]
    C_f = lambda k: autocorr_ar1(rho, sigma, k)

    print(f"alpha={alpha}, rho={rho}")
    print(f"{'L':>5} {'||h_op-h_cf_trunc||_inf':>24} {'J_op':>10} {'J_cf_trunc':>12} {'gap':>10}")
    print("-" * 70)

    # We compare (i) operator solution at length L vs (ii) closed-form truncated at L.
    # As L grows, both should approach the same J value (the true infinite-L optimum).
    for L in [5, 10, 20, 40, 80, 160, 320]:
        h_cf = np.array([(1 - rho) ** alpha * binom_alpha(alpha, k) * (-1) ** k for k in range(L)])
        h_op = solve_normal_eqs(C_f, K_arr, L, M)
        J_op = expected_revenue(h_op, C_f, K_arr, M)
        J_cf = expected_revenue(h_cf, C_f, K_arr, M)
        diff_inf = float(np.max(np.abs(h_op - h_cf)))
        print(f"{L:>5} {diff_inf:>24.4e} {J_op:>10.6f} {J_cf:>12.6f} {J_op - J_cf:>10.4e}")


if __name__ == "__main__":
    run(alpha=0.3, rho=0.7)
    print()
    run(alpha=0.4, rho=0.5)
    print()
    run(alpha=0.2, rho=0.9)
