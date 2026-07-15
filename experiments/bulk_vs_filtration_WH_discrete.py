"""Discrete AR(1) test: paper bulk shape (P) vs user W-H shape (U).

Signal:   alpha_n = rho * alpha_{n-1} + eps_n      (stationary AR(1), |rho|<1)
Kernel:   G(k) = c * |k|^{-gamma}, k>=1, with G(0) regularization
Objective J(u) = 0.5 * u^T G u  -  alpha^T u                  (minimize)

Both policies are scale-free shapes; we optimize the scalar gain analytically:
    u = lambda * shape,    J*(shape) = -0.5 * <alpha,shape>^2 / <shape, G shape>
Larger Sharpe^2 = -2 J* = better.

Shapes (continuous-limit derivation translated to discrete GL):
  (P) Paper: u^P_n = D_+^{1-gamma} alpha_n  +  (1-rho)^{1-gamma} alpha_n
            (causal half coming from realized past + anticausal half on the
             AR(1) forecast tail rho^k alpha_n, which sums to (1-rho)^{1-gamma} alpha_n)
  (U) User: u^U_n = (1-rho)^beta * D_+^beta alpha_n,    beta = (1-gamma)/2
            (filtration-WH: half-derivative on each-time's forecast, then
             causal half-derivative on the resulting past time series; for AR(1)
             the inner half collapses to (1-rho)^beta alpha_s.)
  (A) alpha-chase: u_n = alpha_n
  (W) numerically solved causal Wiener-FIR optimum  (gold standard)
"""
from __future__ import annotations
import numpy as np
from scipy.signal import fftconvolve


def gl_weights(nu: float, K: int) -> np.ndarray:
    """w_k = (-1)^k C(nu,k);  D_+^nu f[n] = sum_{k=0}^{K-1} w_k f[n-k]."""
    w = np.empty(K)
    w[0] = 1.0
    for k in range(1, K):
        w[k] = w[k-1] * (k - 1 - nu) / k
    return w


def causal_apply(f: np.ndarray, w: np.ndarray) -> np.ndarray:
    return fftconvolve(f, w, mode='full')[: len(f)]


def kernel_full(K: int, c: float, gamma: float, eta: float = 0.0) -> np.ndarray:
    """Symmetric kernel of length 2K+1; index K is lag 0.
    Diagonal G(0) = c + eta where eta is temporary-impact regularizer."""
    out = np.zeros(2*K+1)
    out[K] = c + eta
    for k in range(1, K+1):
        out[K+k] = c * k ** (-gamma)
        out[K-k] = c * k ** (-gamma)
    return out


def apply_kernel(u: np.ndarray, ker: np.ndarray) -> np.ndarray:
    return fftconvolve(u, ker, mode='same')


def evaluate(shape: np.ndarray, alpha: np.ndarray, ker: np.ndarray,
             idx: slice) -> tuple[float, float, float]:
    """Return (J*, sharpe, gain*) for u = lambda * shape on the window idx."""
    Gu = apply_kernel(shape, ker)
    a_s = float(alpha[idx] @ shape[idx])
    s_Gs = float(shape[idx] @ Gu[idx])
    if s_Gs <= 0:
        return 0.0, 0.0, 0.0
    gain = a_s / s_Gs
    Jstar = -0.5 * a_s**2 / s_Gs
    sharpe = a_s / np.sqrt(s_Gs)
    return Jstar, sharpe, gain


def wiener_causal(alpha_acf: np.ndarray, ker: np.ndarray, L: int) -> np.ndarray:
    """Solve discrete causal normal equations on a length-L FIR:
        sum_{m=0}^{L-1} R_uu(k-m) h_m = R_ua(k),  k=0..L-1
    where R_uu = ker (autocorrelation of u-kernel quadratic form, which is just
    the kernel itself viewed as a Toeplitz operator) and R_ua = alpha_acf
    (cross-correlation of u and alpha: for our cost u^T G u - alpha^T u, the
    optimal CAUSAL FIR satisfies the Wiener-Hopf normal equations
    G_{Toep,causal} h = alpha_acf_causal).
    """
    # Build LxL causal Toeplitz from ker
    K = (len(ker) - 1) // 2
    g = lambda k: ker[K + k] if abs(k) <= K else 0.0
    T = np.array([[g(i - j) for j in range(L)] for i in range(L)])
    b = alpha_acf[:L].copy()
    h = np.linalg.solve(T, b)
    return h


def run(gamma: float = 0.4, rho: float = 0.9, c: float = 1.0, eta: float = 1.0,
        N: int = 60_000, burn: int = 5_000, K_hist: int = 1_000,
        L_wiener: int = 200, seed: int = 0, verbose: bool = True) -> dict:
    beta = (1 - gamma) / 2

    # Simulate AR(1)
    rng = np.random.default_rng(seed)
    eps = rng.standard_normal(N).astype(np.float64)
    from scipy.signal import lfilter
    alpha = lfilter([1.0], [1.0, -rho], eps)

    # GL derivatives
    w_full = gl_weights(1 - gamma, K_hist)
    w_half = gl_weights(beta,      K_hist)
    D_full = causal_apply(alpha, w_full)
    D_half = causal_apply(alpha, w_half)

    # Build policy shapes
    u_P     = D_full + (1 - rho) ** (1 - gamma) * alpha
    u_U     = (1 - rho) ** beta * D_half
    u_alpha = alpha.copy()

    # Wiener gold-standard causal FIR (apply to alpha)
    ker = kernel_full(K_hist, c, gamma, eta=eta)
    # AR(1) autocorrelation: R(k) = rho^|k| / (1 - rho^2)
    R = np.array([rho ** k / (1 - rho ** 2) for k in range(L_wiener)])
    # The cost is 0.5 u^T G u - alpha^T u; OPTIMAL causal FIR for u_n = sum h_k alpha_{n-k}:
    # normal eq:  sum_m h_m * sum_k G(k-?)*R(?) ... cleaner: directly minimize over h.
    # Cross term:  alpha^T u = sum_n alpha_n sum_k h_k alpha_{n-k}  ~ sum_k h_k R(k)
    # Quad term:   0.5 u^T G u = 0.5 sum_n sum_k sum_m h_k h_m alpha_{n-k} alpha_{n-m} G(?)
    # In expectation (stationary): per unit time = 0.5 sum_{k,m} h_k h_m * sum_l G(l) R(k-m-l)
    #                                            = 0.5 h^T M h    where  M_{km} = (G * R)(k-m)
    # Cross per unit time = sum_k h_k R(k).
    # So h* = M^{-1} R.
    R_full = np.array([rho ** abs(k) / (1 - rho ** 2)
                       for k in range(-2*L_wiener, 2*L_wiener + 1)])
    GR = np.convolve(ker, R_full, mode='same')
    cen = len(GR) // 2
    M = np.array([[GR[cen + (i - j)] for j in range(L_wiener)] for i in range(L_wiener)])
    # Tikhonov regularize ill-conditioned Toeplitz
    ridge = 1e-8 * np.trace(M) / L_wiener
    h_star = np.linalg.solve(M + ridge * np.eye(L_wiener), R)
    u_W = causal_apply(alpha, h_star)

    # Evaluate on test window (avoid burn-in and edge)
    idx = slice(burn, N - K_hist - L_wiener - 10)
    Tn = idx.stop - idx.start
    results = {}
    for name, shape in [('alpha', u_alpha), ('U (user W-H)', u_U),
                        ('P (paper bulk)', u_P), ('W (Wiener gold)', u_W)]:
        J, S, g = evaluate(shape, alpha, ker, idx)
        results[name] = dict(J_per_step=J / Tn, sharpe2_per_step=(S ** 2) / Tn, gain=g)

    if verbose:
        print(f"gamma={gamma}, rho={rho}, c={c}, beta={beta:.3f}, N={N}")
        print(f"{'policy':>18}  {'-2J*/T':>12}  {'gain*':>10}")
        print('-' * 50)
        for name, r in results.items():
            print(f"{name:>18}  {-2*r['J_per_step']:>12.6f}  {r['gain']:>10.4f}")
    return results


if __name__ == "__main__":
    for gamma in [0.3, 0.5, 0.7]:
        for rho in [0.7, 0.9, 0.98]:
            print("=" * 60)
            run(gamma=gamma, rho=rho)
            print()
