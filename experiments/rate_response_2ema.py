"""Rate response and impact surfing in the 2-EMA case (exponential kernel,
temporary cost + transient impact + risk).

Question: does the fast-signal "impact pumping" (rate reversal / surfing) of the
eta=0 exponential kernel survive when a temporary cost eta>0 is added (the
Neuman-Voss / two-moving-average filter)?

Analytics (OU signal, own filtration, exponential kernel g=e^{-kappa|t|}):
  n_hat(w)  = eta w^2 + 2 kappa gamma w^2/(kappa^2+w^2) + lambda
  n_hat_+   = sqrt(eta) (b1 - i w)(b2 - i w)/(kappa - i w),
      b1^2+b2^2 = kappa^2 + (2 kappa gamma + lambda)/eta,   b1^2 b2^2 = lambda kappa^2/eta
  Phi(theta)= n_hat_+(i theta) = sqrt(eta)(b1+theta)(b2+theta)/(kappa+theta)
  c1 = lim_{|w|->inf} 1/n_hat_+ = 0   (any eta>0)   [ = 1/sqrt(2 kappa gamma+lambda) at eta=0 ]
  R(theta) = (theta^2/Phi)(1/Phi - 2 c1) = theta^2/Phi^2 > 0   for every theta   (eta>0)
  X(theta) = theta/Phi^2 > 0
Value at fixed appreciation variance Var(alpha)=V:  v(theta) = theta^2 V / (2 Phi^2).
  eta=0:  Phi -> sqrt(2 kappa gamma+lambda),  v ~ theta^2         (fast signals valuable, surf)
  eta>0:  Phi ~ sqrt(eta) theta,              v -> V/(2 eta)       (SATURATES; no surf)
  crossover at theta ~ a = sqrt(lambda/eta)  (the aim-portfolio rate).

Discrete check: reverse-Cholesky adapted optimum with Cmat = eta*I + gamma*dt*G
+ lambda*dt^2 L^T L; forward responses by lag-1 regression (innovation-safe).
"""
import numpy as np
from scipy.special import gamma as Gfun


def b1b2(eta, gam, kap, lam):
    S = kap ** 2 + (2 * kap * gam + lam) / eta        # b1^2 + b2^2
    P = lam * kap ** 2 / eta                           # b1^2 b2^2
    disc = np.sqrt(max(S * S - 4 * P, 0.0))
    b1 = np.sqrt((S - disc) / 2)
    b2 = np.sqrt((S + disc) / 2)
    return b1, b2


def Phi_2ema(theta, eta, gam, kap, lam):
    b1, b2 = b1b2(eta, gam, kap, lam)
    return np.sqrt(eta) * (b1 + theta) * (b2 + theta) / (kap + theta)


def R_analytic(theta, eta, gam, kap, lam):
    """Rate response. c1=0 for eta>0 (2-EMA); c1=1/sqrt(A) for eta=0 (surfing)."""
    if eta > 0:
        Phi = Phi_2ema(theta, eta, gam, kap, lam)
        c1 = 0.0
    else:
        A = 2 * kap * gam + lam
        m = kap * np.sqrt(lam / A)
        Phi = np.sqrt(A) * (m + theta) / (kap + theta)
        c1 = 1.0 / np.sqrt(A)
    return (theta ** 2 / Phi) * (1 / Phi - 2 * c1)


def value_fixed_var(theta, eta, gam, kap, lam, V=1.0):
    Phi = Phi_2ema(theta, eta, gam, kap, lam) if eta > 0 else \
        np.sqrt(2 * kap * gam + lam) * (kap * np.sqrt(lam / (2 * kap * gam + lam)) + theta) / (kap + theta)
    return theta ** 2 * V / (2 * Phi ** 2)


# ---- discrete reverse-Cholesky solver (temporary cost added) ----
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


def measure_2ema(n, dt, theta, eta, gam, kap, lam):
    idx = np.arange(n)
    lag = np.abs(idx[:, None] - idx[None, :]) * dt
    G = np.exp(-kap * lag)
    Ltri = np.tril(np.ones((n, n)))
    Cmat = eta * np.eye(n) + gam * dt * G + lam * dt ** 2 * (Ltri.T @ Ltri)
    S = np.exp(-theta * lag)
    W = solve_W(Cmat, theta, dt)
    Wx = dt * (Ltri @ W)
    i = n // 2
    R = (W @ S)[i, i - 1] / S[i - 1, i - 1]
    X = (Wx @ S)[i, i - 1] / S[i - 1, i - 1]
    return R, X


if __name__ == "__main__":
    gam, kap = 1.0, 2.0
    lam = 1.0
    n, dt = 500, 0.03

    print("=" * 74)
    print(f"2-EMA case: exponential kernel, gamma={gam}, kappa={kap}, lambda={lam}")
    print("At eta=0 (1-EMA) the rate REVERSES for theta>theta*=kappa-2m (impact surfing).")
    print("=" * 74)

    A = 2 * kap * gam + lam
    m0 = kap * np.sqrt(lam / A)
    print(f"\n[eta=0 reference]  theta* = kappa-2m = {kap - 2*m0:+.3f}  "
          f"(rate reverses above this speed)")
    for th in (0.5, 1.5, 3.0, 6.0):
        Rp = R_analytic(th, 0.0, gam, kap, lam)
        Rm, Xm = measure_2ema(n, dt, th, 1e-4, gam, kap, lam)  # tiny eta ~ singular limit
        print(f"   theta={th:4.1f}:  R_analytic(eta=0)={Rp:+.4f}   "
              f"R_discrete(eta=1e-4)={Rm:+.4f}   X={Xm:+.4f}")

    print("\n[eta>0: the 2-EMA filter]   R = theta^2/Phi^2 > 0 for every theta (no surfing)")
    for eta in (0.05, 0.2, 1.0):
        b1, b2 = b1b2(eta, gam, kap, lam)
        a = np.sqrt(lam / eta)
        print(f"\n  eta={eta}:  b1={b1:.3f}, b2={b2:.3f}  (aim rate a=sqrt(lam/eta)={a:.3f}; "
              f"value saturates for theta>~a)")
        for th in (0.5, 1.5, 3.0, 6.0):
            Rp = R_analytic(th, eta, gam, kap, lam)
            Rm, Xm = measure_2ema(n, dt, th, eta, gam, kap, lam)
            print(f"     theta={th:4.1f}:  R_analytic={Rp:+.4f}   R_discrete={Rm:+.4f}   "
                  f"(match {abs(Rp-Rm):.1e})   R>0: {Rm > 0}")

    print("\n" + "=" * 74)
    print("Value at fixed appreciation variance V=1:  v(theta) = theta^2/(2 Phi^2)")
    print("eta=0 grows ~theta^2; eta>0 SATURATES at V/2eta (temporary cost caps fast signals)")
    print("=" * 74)
    print(f"{'theta':>7} | {'eta=0 (surf)':>13} | {'eta=0.05':>10} | {'eta=0.2':>9} | {'eta=1.0':>9}")
    for th in (0.5, 1, 2, 4, 8, 16, 32):
        row = [value_fixed_var(th, e, gam, kap, lam) for e in (0.0, 0.05, 0.2, 1.0)]
        print(f"{th:7.1f} | {row[0]:13.3f} | {row[1]:10.4f} | {row[2]:9.4f} | {row[3]:9.4f}")
    print(f"\nsaturation limits V/2eta:  eta=0.05 -> {1/(2*0.05):.1f}, "
          f"eta=0.2 -> {1/(2*0.2):.2f}, eta=1.0 -> {1/(2*1.0):.2f}")
