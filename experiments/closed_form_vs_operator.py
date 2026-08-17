"""Closed-form Wiener-Hopf policy vs discrete operator-resolvent (normal equations).

This is the discrete-stationary analogue of the Abi Jaber-Neuman [AJN22] operator
approach: we numerically solve the discrete Wiener-Hopf / stationary normal equations
for the optimal causal FIR filter and compare to the closed-form prediction.

Two test problems:

(A) AR(1) signal x exponential kernel K(n) = lambda^|n|.
    Closed form (paper eq. 12):  h = (c, -c*lambda, 0, 0, ...)
    with c = (1-lambda*rho)/(1-lambda^2).

(B) AR(1) signal x ARFIMA(0,d,0) kernel with hat K(omega) = (2 sin(omega/2))^(-2*alpha).
    This kernel admits the spectral factorisation K_+(z) = (1 - z^{-1})^(-alpha),
    K_-(z) = (1 - z)^(-alpha). Closed-form prediction (paper eqs. 12c + 15c + 14):
      h_k = (1-rho)^alpha * C(alpha,k) * (-1)^k,   k >= 0
    i.e. the optimal causal filter is the fractional difference (1-z^{-1})^alpha
    rescaled by the Markov-closure constant (1-rho)^alpha.

We also report realised per-period revenue J = E[f x - 0.5 x (K*x)] for the
closed-form policy, the numerical-operator policy, and a naive alpha-chase
policy x_t = f_t. Theoretical optimum is computed in closed form for case (A).
"""
from __future__ import annotations
import math
import numpy as np
import json
import os


def autocorr_ar1(rho: float, sigma: float, k: int) -> float:
    """C_f(k) = E[f_t f_{t-k}] for AR(1) with persistence rho, innovation std sigma."""
    return (sigma ** 2) * (rho ** abs(k)) / (1.0 - rho ** 2)


def kernel_exp(lam: float, n: int) -> float:
    return lam ** abs(n)


def kernel_arfima(alpha: float, n_max: int) -> np.ndarray:
    """Autocovariance of the ARFIMA(0, alpha, 0) process: this gives the kernel
    K(n) corresponding to hat K(omega) = (2 sin(omega/2))^(-2*alpha).
    Closed form (Hosking 1981):
        K(0)   = Gamma(1-2*alpha) / Gamma(1-alpha)^2
        K(n+1) = K(n) * (n + alpha) / (n + 1 - alpha)
    """
    K = np.zeros(n_max + 1)
    K[0] = math.gamma(1 - 2 * alpha) / (math.gamma(1 - alpha) ** 2)
    for n in range(n_max):
        K[n + 1] = K[n] * (n + alpha) / (n + 1 - alpha)
    return K


def solve_normal_eqs(C_f, K_arr, L: int, M: int):
    """Solve the discrete stationary Wiener-Hopf normal equations for the optimal
    causal FIR filter h of length L.

    Objective per period:
      J(h) = sum_k h_k C_f(k) - 0.5 sum_{j,j'} h_j h_{j'} R(j - j')
    where R(d) = sum_m K(m) C_f(d + m) is the autocovariance of K*f.

    Setting dJ/dh_k = 0 gives the linear system  A h = c
    with A_{kj} = R(j - k)  and  c_k = C_f(k).

    Arguments:
      C_f  : callable, k -> autocovariance
      K_arr: array of length 2M+1, K_arr[i] = K(i - M) for i=0..2M
      L    : length of FIR filter
      M    : kernel truncation half-width

    Returns:
      h    : optimal causal FIR coefficients, length L.
    """
    # R(d) = sum_m K(m) C_f(d + m). Truncate |m| <= M.
    m_range = np.arange(-M, M + 1)
    # K_arr indexed by i in [0, 2M], i = m + M, so K(m) = K_arr[m+M]
    def R(d):
        s = 0.0
        for i, m in enumerate(m_range):
            s += K_arr[i] * C_f(d + m)
        return s

    A = np.zeros((L, L))
    for k in range(L):
        for j in range(L):
            A[k, j] = R(j - k)
    c = np.array([C_f(k) for k in range(L)])
    h = np.linalg.solve(A, c)
    return h


def expected_revenue(h: np.ndarray, C_f, K_arr, M: int) -> float:
    """E[f_t x_t - 0.5 x_t (K*x)_t] for x_t = sum_k h_k f_{t-k} under stationarity."""
    L = len(h)
    m_range = np.arange(-M, M + 1)
    # gain = sum_k h_k C_f(k)
    gain = sum(h[k] * C_f(k) for k in range(L))
    # cost = 0.5 sum_{j,k} h_j h_k R(j - k) with R(d) = sum_m K(m) C_f(d+m)
    def R(d):
        s = 0.0
        for i, m in enumerate(m_range):
            s += K_arr[i] * C_f(d + m)
        return s
    cost = 0.0
    for j in range(L):
        for k in range(L):
            cost += h[j] * h[k] * R(j - k)
    cost *= 0.5
    return gain - cost


def simulate_pnl(h: np.ndarray, rho: float, sigma: float, K_arr: np.ndarray, M: int,
                 T: int, burn: int, seed: int) -> float:
    """Realised per-period revenue on a simulated AR(1) path."""
    rng = np.random.default_rng(seed)
    f = np.zeros(T)
    eps = rng.standard_normal(T) * sigma
    for t in range(1, T):
        f[t] = rho * f[t - 1] + eps[t]
    L = len(h)
    x = np.zeros(T)
    for k in range(L):
        x[k:] += h[k] * f[: T - k]
    # K convolution: kernel two-sided, indices -M..M
    kernel = K_arr  # length 2M+1
    # full convolution; align so that (K*x)[t] = sum_{m=-M}^M kernel[m+M] x[t-m]
    Kx = np.convolve(x, kernel, mode="same")  # mode='same' aligns center to center
    # mode='same' with kernel length 2M+1 (odd) puts kernel[M] at center -> correct.
    interior = slice(burn, T - burn)
    gain = float(np.mean(f[interior] * x[interior]))
    cost = float(0.5 * np.mean(x[interior] * Kx[interior]))
    return gain - cost


def run_case_A():
    """AR(1) x exponential kernel."""
    rho = 0.7
    lam = 0.5
    sigma = 1.0
    L = 25
    M = 200  # kernel truncation
    T = 200_000
    burn = 500
    seed = 42

    K_arr = np.array([kernel_exp(lam, m - M) for m in range(2 * M + 1)])
    C_f = lambda k: autocorr_ar1(rho, sigma, k)

    # Closed form
    c = (1 - lam * rho) / (1 - lam ** 2)
    h_closed = np.zeros(L)
    h_closed[0] = c
    h_closed[1] = -c * lam

    # Numerical operator-resolvent
    h_op = solve_normal_eqs(C_f, K_arr, L, M)

    # Closed-form theoretical expected revenue
    # J* = 0.5 * E[x_closed * f_t]  (since at optimum f = K*x => f*x = x*K*x)
    # E[x_closed f] = c * (C_f(0) - lam C_f(1)) = c * sigma^2 * (1 - lam rho)/(1 - rho^2)
    J_theory = 0.5 * c * sigma ** 2 * (1 - lam * rho) / (1 - rho ** 2)

    # Analytical expected revenue under each filter
    J_closed_anal = expected_revenue(h_closed, C_f, K_arr, M)
    J_op_anal = expected_revenue(h_op, C_f, K_arr, M)
    h_naive = np.zeros(L); h_naive[0] = 1.0
    J_naive_anal = expected_revenue(h_naive, C_f, K_arr, M)

    # Realised PnL on a simulated path
    J_closed_sim = simulate_pnl(h_closed, rho, sigma, K_arr, M, T, burn, seed)
    J_op_sim = simulate_pnl(h_op, rho, sigma, K_arr, M, T, burn, seed)
    J_naive_sim = simulate_pnl(h_naive, rho, sigma, K_arr, M, T, burn, seed)

    print("=" * 72)
    print(f"Case A: AR(1) x exponential kernel, rho={rho}, lambda={lam}")
    print("=" * 72)
    print(f"Closed-form coefficients (paper eq. 12):  c={c:.6f}")
    print(f"  h_closed[:5] = {h_closed[:5]}")
    print(f"  h_op[:5]     = {h_op[:5]}")
    print(f"  ||h_op - h_closed||_inf = {np.max(np.abs(h_op - h_closed)):.3e}")
    print(f"  ||h_op - h_closed||_2   = {np.linalg.norm(h_op - h_closed):.3e}")
    print()
    print("Expected revenue per period (analytical, stationary):")
    print(f"  theoretical J*       = {J_theory:.6f}")
    print(f"  closed-form policy   = {J_closed_anal:.6f}")
    print(f"  operator policy      = {J_op_anal:.6f}")
    print(f"  naive (x=f) policy   = {J_naive_anal:.6f}")
    print(f"  closed - op gap      = {abs(J_closed_anal - J_op_anal):.3e}")
    print(f"  PnL uplift vs naive  = {J_closed_anal - J_naive_anal:.6f}  "
          f"(ratio {J_closed_anal / J_naive_anal if J_naive_anal != 0 else float('nan'):.3f}x)")
    print()
    print(f"Realised revenue on simulated path (T={T}, burn={burn}):")
    print(f"  closed-form policy   = {J_closed_sim:.6f}")
    print(f"  operator policy      = {J_op_sim:.6f}")
    print(f"  naive (x=f) policy   = {J_naive_sim:.6f}")
    return {
        "rho": rho, "lambda": lam, "L": L, "T": T,
        "h_closed": h_closed.tolist(),
        "h_op": h_op.tolist(),
        "h_op_minus_closed_inf": float(np.max(np.abs(h_op - h_closed))),
        "J_theory": J_theory,
        "J_closed_analytical": J_closed_anal,
        "J_op_analytical": J_op_anal,
        "J_naive_analytical": J_naive_anal,
        "J_closed_simulated": J_closed_sim,
        "J_op_simulated": J_op_sim,
        "J_naive_simulated": J_naive_sim,
    }


def run_case_B(alpha: float = 0.3, rho: float = 0.7):
    """AR(1) x ARFIMA-spectrum kernel (power-law).

    Closed-form prediction: h_k = (1-rho)^alpha * binom(alpha, k) * (-1)^k.
    """
    sigma = 1.0
    L = 30
    M = 1000  # kernel is long-memory; need wide truncation
    T = 200_000
    burn = 1000
    seed = 123

    # Kernel autocovariance from Hosking 1981 formula, then symmetrise to two-sided
    K_half = kernel_arfima(alpha, M)  # length M+1, K_half[n] = K(n) for n>=0
    K_arr = np.zeros(2 * M + 1)
    for i in range(2 * M + 1):
        K_arr[i] = K_half[abs(i - M)]
    C_f = lambda k: autocorr_ar1(rho, sigma, k)

    # Closed-form filter
    def binom_alpha(a, m):
        r = 1.0
        for k in range(m):
            r *= (a - k) / (k + 1)
        return r
    h_closed = np.zeros(L)
    pref = (1 - rho) ** alpha
    for k in range(L):
        h_closed[k] = pref * binom_alpha(alpha, k) * (-1) ** k

    # Numerical operator solution
    h_op = solve_normal_eqs(C_f, K_arr, L, M)

    # Analytical and simulated revenue
    J_closed_anal = expected_revenue(h_closed, C_f, K_arr, M)
    J_op_anal = expected_revenue(h_op, C_f, K_arr, M)
    h_naive = np.zeros(L); h_naive[0] = 1.0
    J_naive_anal = expected_revenue(h_naive, C_f, K_arr, M)

    J_closed_sim = simulate_pnl(h_closed, rho, sigma, K_arr, M, T, burn, seed)
    J_op_sim = simulate_pnl(h_op, rho, sigma, K_arr, M, T, burn, seed)
    J_naive_sim = simulate_pnl(h_naive, rho, sigma, K_arr, M, T, burn, seed)

    print()
    print("=" * 72)
    print(f"Case B: AR(1) x ARFIMA-spectrum kernel, rho={rho}, alpha={alpha}")
    print(f"        (kernel hat K(omega) = (2 sin omega/2)^(-2*alpha))")
    print("=" * 72)
    print(f"Closed-form prefactor (1-rho)^alpha = {pref:.6f}")
    print(f"  h_closed[:6] = {h_closed[:6]}")
    print(f"  h_op[:6]     = {h_op[:6]}")
    print(f"  ||h_op - h_closed||_inf = {np.max(np.abs(h_op - h_closed)):.3e}")
    print(f"  ||h_op - h_closed||_2   = {np.linalg.norm(h_op - h_closed):.3e}")
    print()
    print("Expected revenue per period (analytical, stationary):")
    print(f"  closed-form policy   = {J_closed_anal:.6f}")
    print(f"  operator policy      = {J_op_anal:.6f}")
    print(f"  naive (x=f) policy   = {J_naive_anal:.6f}")
    print(f"  closed - op gap      = {abs(J_closed_anal - J_op_anal):.3e}")
    print()
    print(f"Realised revenue on simulated path (T={T}, burn={burn}):")
    print(f"  closed-form policy   = {J_closed_sim:.6f}")
    print(f"  operator policy      = {J_op_sim:.6f}")
    print(f"  naive (x=f) policy   = {J_naive_sim:.6f}")
    return {
        "alpha": alpha, "rho": rho, "L": L, "M": M, "T": T,
        "h_closed": h_closed.tolist(),
        "h_op": h_op.tolist(),
        "h_op_minus_closed_inf": float(np.max(np.abs(h_op - h_closed))),
        "J_closed_analytical": J_closed_anal,
        "J_op_analytical": J_op_anal,
        "J_naive_analytical": J_naive_anal,
        "J_closed_simulated": J_closed_sim,
        "J_op_simulated": J_op_sim,
        "J_naive_simulated": J_naive_sim,
    }


if __name__ == "__main__":
    out = {}
    out["caseA_exponential"] = run_case_A()
    out["caseB_arfima_alpha=0.3"] = run_case_B(alpha=0.3, rho=0.7)
    out["caseB_arfima_alpha=0.4"] = run_case_B(alpha=0.4, rho=0.5)
    out["caseB_arfima_alpha=0.2_rho=0.9"] = run_case_B(alpha=0.2, rho=0.9)

    os.makedirs("experiments/results", exist_ok=True)
    with open("experiments/results/closed_form_vs_operator.json", "w") as f:
        json.dump(out, f, indent=2)
    print()
    print("Saved JSON: experiments/results/closed_form_vs_operator.json")
