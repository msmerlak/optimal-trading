"""Validate the gain/risk/propagator closed forms of
notes/wiener-hopf-propagator-risk.md before they enter the trading-filters paper.

Predictions (OU signal, rate theta, unit variance; own filtration):
  N(xi)      = gamma * C_hat(xi) * xi^2 + lambda
  Phi_N(th)  = N_+(i th)   (Szego formula)
  X(th)      = theta / Phi_N^2                      (position response, always > 0)
  R(th)      = (theta^2/Phi_N) [1/Phi_N - 2 c1],    c1 = lim 1/N_+ = [lam - 2 gam G'(0+)]^{-1/2}
Exponential kernel G = e^{-kappa|t|}:  N_+ = sqrt(A)(m - i xi)/(kappa - i xi),
  A = 2 kappa gamma + lambda, m = kappa sqrt(lambda/A);  flip at theta* = kappa - 2m;
  always-contrarian flow iff lambda >= 2 kappa gamma / 3.
Power-law kernel G = |t|^{-beta}: c1 = 0, R = theta^2/Phi_N^2 > 0.
Pure risk (gamma=0): X = theta/lambda, R = -theta^2/lambda.

Discrete: cost matrix Cmat = gamma*dt*G + lambda*dt^2*L^T L (L = lower-tri ones),
adapted FOC E_i[(Cmat u)_i] = alpha_i, solved by the validated UL (reverse-Cholesky)
factorization. Forward responses measured by lag-1 regression (innovation-safe):
  R_hat = Cov(u_i, alpha_{i-1})/Var,   X_hat = Cov(x_i, alpha_{i-1})/Var,  x = dt*L u.
"""
import numpy as np
from scipy.special import gamma as Gfun
from scipy import integrate

def phiN_powerlaw(theta, beta, gam, lam):
    cb = 2 * Gfun(1 - beta) * np.sin(np.pi * beta / 2)
    N = lambda t: gam * cb * np.abs(t) ** (1 + beta) + lam
    f = lambda t: np.log(N(t)) / (theta ** 2 + t ** 2)
    val, _ = integrate.quad(f, 0, np.inf, limit=400)
    return np.exp(theta / np.pi * val)

def solve_W(Cmat, theta, dt):
    n = Cmat.shape[0]
    Rev = np.eye(n)[::-1]
    Lr = np.linalg.cholesky(Rev @ Cmat @ Rev)
    U = Rev @ Lr @ Rev
    Cm, Cp = U, U.T
    Cmi, Cpi = np.linalg.inv(Cm), np.linalg.inv(Cp)
    Z = np.zeros((n, n))
    for s in range(n):
        Z[s, :s] = Cmi[s, :s]
        Z[s, s] = Cmi[s, s:] @ np.exp(-theta * dt * np.arange(n - s))
    return Cpi @ Z

def measure(n, dt, theta, gam, lam, kernel):
    idx = np.arange(n)
    lag = np.abs(idx[:, None] - idx[None, :]) * dt
    if kernel[0] == "exp":
        G = np.exp(-kernel[1] * lag)
    elif kernel[0] == "pow":
        beta = kernel[1]
        G = np.where(lag == 0, 2 * dt ** (-beta) / ((1 - beta) * (2 - beta)),
                     np.where(lag == 0, 1.0, lag) ** (-beta))
    else:  # no impact
        G = np.zeros((n, n))
    Ltri = np.tril(np.ones((n, n)))
    Cmat = gam * dt * G + lam * dt ** 2 * (Ltri.T @ Ltri)
    S = np.exp(-theta * lag)
    W = solve_W(Cmat, theta, dt)
    Wx = dt * (Ltri @ W)
    i = n // 2
    R = (W @ S)[i, i - 1] / S[i - 1, i - 1]
    X = (Wx @ S)[i, i - 1] / S[i - 1, i - 1]
    return R, X

def pred_exp(theta, kappa, gam, lam):
    A = 2 * kappa * gam + lam
    m = kappa * np.sqrt(lam / A)
    Phi = np.sqrt(A) * (m + theta) / (kappa + theta)
    return (theta ** 2 / Phi) * (1 / Phi - 2 / np.sqrt(A)), theta / Phi ** 2

n, dt = 400, 0.04
print("=== exponential + risk, kappa=2, gamma=1 ===")
for lam, ths in ((0.5, (0.3, 1.5)), (4.0, (0.5, 2.0))):
    A = 2 * 2 * 1 + lam
    tstar = 2 - 2 * 2 * np.sqrt(lam / A)
    print(f"lambda={lam}: theta* = {tstar:+.4f}" + ("  (always contrarian)" if tstar < 0 else ""))
    for th in ths:
        Rp, Xp = pred_exp(th, 2.0, 1.0, lam)
        Rm, Xm = measure(n, dt, th, 1.0, lam, ("exp", 2.0))
        print(f"  theta={th}:  R={Rm:+.4f} (pred {Rp:+.4f})   X={Xm:+.4f} (pred {Xp:+.4f})")

print("\n=== pure risk, gamma=0, lambda=1, theta=0.7 (pred R=-0.49, X=+0.70) ===")
Rm, Xm = measure(n, dt, 0.7, 0.0, 1.0, ("none",))
print(f"  R={Rm:+.4f}   X={Xm:+.4f}")

print("\n=== power-law + risk, beta=0.5, gamma=1 ===")
cb = 2 * Gfun(0.5) * np.sin(np.pi / 4)
for lam, ths in ((0.0, (1.0,)), (1.0, (0.5, 2.0))):
    for th in ths:
        if lam == 0:
            Rp = th ** 0.5 / cb
            Xp = float("nan")  # position nonstationary at lam=0
        else:
            Phi = phiN_powerlaw(th, 0.5, 1.0, lam)
            Rp, Xp = th ** 2 / Phi ** 2, th / Phi ** 2
        Rm, Xm = measure(n, dt, th, 1.0, lam, ("pow", 0.5))
        print(f"  lambda={lam} theta={th}:  R={Rm:+.4f} (pred {Rp:+.4f})   X={Xm:+.4f} (pred {Xp:+.4f})")

print("\n=== dt refinement, exp+risk lambda=0.5 theta=1.5 (pred R=%+.4f, X=%+.4f) ===" % pred_exp(1.5, 2.0, 1.0, 0.5))
for (nn, ddt) in ((400, 0.04), (800, 0.02), (1600, 0.01)):
    Rm, Xm = measure(nn, ddt, 1.5, 1.0, 0.5, ("exp", 2.0))
    print(f"  n={nn} dt={ddt}:  R={Rm:+.4f}   X={Xm:+.4f}")


# ---------------- NV three-friction check (temporary + resilient + risk) ----------------
# N = eta xi^2 + 2 kappa gamma xi^2/(kappa^2+xi^2) + lambda;
# N_+ = sqrt(eta)(b1 - i xi)(b2 - i xi)/(kappa - i xi);
# prediction X = theta/Phi^2, R = theta^2/Phi^2 (no atom: temporary cost regularizes).
# Validated 2026-07-18: eta=.5,gam=1,kap=2,lam=1,th=1 (n=800,dt=.02):
#   b1=0.7726 b2=3.6610 Phi=1.9474; X meas +0.2711 vs pred +0.2637; R meas +0.2406 vs pred +0.2637.
def nv_check(n=800, dt=0.02, th=1.0, eta=0.5, gam=1.0, kap=2.0, lam=1.0):
    idx = np.arange(n); lag = np.abs(idx[:, None] - idx[None, :]) * dt
    G = np.exp(-kap * lag); Lt = np.tril(np.ones((n, n)))
    C = gam * dt * G + lam * dt ** 2 * (Lt.T @ Lt) + eta * np.eye(n)
    S = np.exp(-th * lag)
    W = solve_W(C, th, dt); Wx = dt * (Lt @ W); i = n // 2
    R = (W @ S)[i, i - 1] / S[i - 1, i - 1]
    X = (Wx @ S)[i, i - 1] / S[i - 1, i - 1]
    s2 = kap ** 2 + (2 * kap * gam + lam) / eta; p2 = lam * kap ** 2 / eta
    z1 = (s2 - np.sqrt(s2 ** 2 - 4 * p2)) / 2; z2 = (s2 + np.sqrt(s2 ** 2 - 4 * p2)) / 2
    Phi = np.sqrt(eta) * (np.sqrt(z1) + th) * (np.sqrt(z2) + th) / (kap + th)
    return R, X, th / Phi ** 2

if __name__ == "__main__":
    R, X, pred = nv_check()
    print(f"\n=== NV three-friction check ===\n  R={R:+.4f}  X={X:+.4f}  pred X = R/th^2... = {pred:+.4f}")
