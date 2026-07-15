"""Test the conjectured signal-speed response function R(theta) for the
adapted gain-cost problem (extension B of the extensions memo).

Setup: discrete grid, OU signal with rate theta (Markov => exact conditional
expectations), kernel G = sum_j w_j exp(-kappa_j |t|). Adapted optimum via the
verified UL (reverse-Cholesky) formula u = C_+^{-1} P_+ C_-^{-1} alpha
(validated to machine precision against direct coefficient matching in
review_factorization_check.py, Check B). Response measured as
R_hat = Cov(u_t, alpha_t)/Var(alpha_t) at the grid center.

REFUTED initial conjecture: R(theta) = 1/C_hat(i theta) (rational continuation
xi^2 -> -theta^2). Coincidentally correct for a single exponential; for the
two-exponential mixture it predicts a reentrant sign pattern +,-,+,- which the
numerics reject (measured: single flip, +,+,-,-).

VALIDATED corrected formula (derived via the innovations filter
g_hat = gamma^{-1} C_+^{-1} Pi_+[C_-^{-1} phi_+], atom subtracted at q=0):
  R_fwd(theta) = gamma^{-1} rho(theta) [ 1/C_hat_+(i theta) - 2 c1 theta ],
  rho(theta)   = 1/C_hat_-(-i theta),
  c1           = lim_{xi->inf} 1/(-i xi C_hat_+(xi))  (derivative loading).
Single exponential: rho=sqrt(2k)/(k+th), bracket=(k-th)/sqrt(2k) => (k^2-th^2)/2k. OK
Power law: c1=0 => R = theta^{1-beta}/c_beta > 0, no flip. OK
Mixture: C_hat_+ = sqrt(2W)(mu - i xi)/[(k1 - i xi)(k2 - i xi)], W = w1 k1 + w2 k2,
  mu^2 = (w1 k1 k2^2 + w2 k2 k1^2)/W, c1 = 1/sqrt(2W):
  R = (k1+th)(k2+th)[(k1+th)(k2+th) - 2 th (mu+th)] / [2 W (mu+th)^2],
  single flip at th* solving th^2 + (2 mu - k1 - k2) th - k1 k2 = 0.
Backward/contemporaneous convention instead satisfies
  R_bwd = 1/[C_hat_+(i theta) C_hat_-(-i theta)] > 0 (no flip; loads on the
  contemporaneous innovation).
"""
import numpy as np

def build(n, dt, theta, kernels):
    """kernels: list of (w, kappa). Returns Cmat, S (OU corr), dt."""
    idx = np.arange(n)
    lag = np.abs(idx[:, None] - idx[None, :]) * dt
    Cmat = sum(w * np.exp(-k * lag) for w, k in kernels) * dt
    S = np.exp(-theta * lag)  # unit-variance OU correlation
    return Cmat, S

def response(n, dt, theta, kernels):
    Cmat, S = build(n, dt, theta, kernels)
    # UL factorization: C = C_- C_+, C_+ lower triangular (reverse Cholesky)
    Rev = np.eye(n)[::-1]
    Lr = np.linalg.cholesky(Rev @ Cmat @ Rev)
    U = Rev @ Lr @ Rev            # upper; Cmat = U U^T
    Cm, Cp = U, U.T               # C_- = U (anticausal), C_+ = U^T (causal)
    Cmi = np.linalg.inv(Cm)
    Cpi = np.linalg.inv(Cp)
    # Z = P_+ C_-^{-1}: OU-Markov projection E_s[alpha_j] = e^{-theta(j-s)dt} alpha_s
    Z = np.zeros((n, n))
    for s in range(n):
        Z[s, :s] = Cmi[s, :s]
        tail = Cmi[s, s:] @ np.exp(-theta * dt * np.arange(n - s))
        Z[s, s] = tail
    W = Cpi @ Z                   # u = W alpha
    i = n // 2
    # Backward/contemporaneous regression: conditions on alpha_i, which contains
    # the slice innovation that discrete u_i may load on -> backward convention.
    R_bwd = (W @ S)[i, i] / S[i, i]
    # Forward/execution-relevant regression: on alpha_{i-1}, orthogonal to the
    # slice-i innovation -> Ito/forward convention (continuum R(theta)).
    R_fwd = (W @ S)[i, i - 1] / S[i - 1, i - 1]
    return R_fwd, R_bwd

def pred_single(theta, kappa):
    return (kappa**2 - theta**2) / (2 * kappa)

def pred_mix_naive(theta, k1, k2, w1, w2):
    """REFUTED rational-continuation conjecture (kept for the record)."""
    mu2 = (w1 * k1 * k2**2 + w2 * k2 * k1**2) / (w1 * k1 + w2 * k2)
    return (k1**2 - theta**2) * (k2**2 - theta**2) / (2 * (w1 * k1 + w2 * k2) * (mu2 - theta**2))

def pred_mix(theta, k1, k2, w1, w2):
    """Corrected forward response via innovations filter (validated)."""
    W = w1 * k1 + w2 * k2
    mu = np.sqrt((w1 * k1 * k2**2 + w2 * k2 * k1**2) / W)
    pref = (k1 + theta) * (k2 + theta) / (2 * W * (mu + theta) ** 2)
    bracket = (k1 + theta) * (k2 + theta) - 2 * theta * (mu + theta)
    return pref * bracket

def pred_mix_bwd(theta, k1, k2, w1, w2):
    W = w1 * k1 + w2 * k2
    mu = np.sqrt((w1 * k1 * k2**2 + w2 * k2 * k1**2) / W)
    return ((k1 + theta) * (k2 + theta)) ** 2 / (2 * W * (mu + theta) ** 2)

n, dt = 400, 0.04   # horizon 16

print("=== single exponential kappa=2 (calibration; known R=(k^2-th^2)/2k) ===")
for theta in (1.0, 3.0):
    rf, rb = response(n, dt, theta, [(1.0, 2.0)])
    print(f"theta={theta}:  R_fwd={rf:+.4f}  (pred {pred_single(theta,2.0):+.4f})   R_bwd={rb:+.4f}  (bwd pred {(2.0+theta)**2/4:+.4f})")

print("\n=== mixture w1=w2=0.5, kappa1=1, kappa2=4  (mu=2) ===")
th_star = (-(2 * 2 - 1 - 4) + np.sqrt((2 * 2 - 1 - 4) ** 2 + 4 * 1 * 4)) / 2
print(f"corrected prediction: single flip at theta* = {th_star:.4f}")
for theta in (0.5, 1.5, 3.0, 5.0):
    rf, rb = response(n, dt, theta, [(0.5, 1.0), (0.5, 4.0)])
    print(f"theta={theta}:  R_fwd={rf:+.4f}  (pred {pred_mix(theta,1,4,.5,.5):+.4f}, naive {pred_mix_naive(theta,1,4,.5,.5):+.4f})"
          f"   R_bwd={rb:+.4f}  (pred {pred_mix_bwd(theta,1,4,.5,.5):+.4f})")

print("\n=== dt refinement, mixture theta=3.0 (pred %+.4f) ===" % pred_mix(3.0,1,4,.5,.5))
for (nn, ddt) in ((400, 0.04), (800, 0.02), (1600, 0.01)):
    rf, rb = response(nn, ddt, 3.0, [(0.5, 1.0), (0.5, 4.0)])
    print(f"n={nn} dt={ddt}:  R_fwd={rf:+.4f}")
