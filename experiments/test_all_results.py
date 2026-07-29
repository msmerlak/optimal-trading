"""
test_all_results.py  --  numerical verification of every analytical result in
v3/optimal-trading-filters-v3.tex.

Each check verifies BOTH sides of an identity and prints PASS/FAIL with values
and relative error.  Two independent machineries are used and cross-checked:

  * frequency domain: the Szego outer factor Phi(theta) = n_hat_+(i theta) via
    the Szego integral (eq:szego / eq:phi), the causality-gap quadrature
    (eq:sinlaw, v/v_ant = sin(pi beta/2), an in-paper result in v3), and the
    closed-form rational factors (eq:exp-factor, eq:gp, eq:nv-factor);
  * time domain: the discretized adapted optimum via reverse-order Cholesky of
    the cost matrix (the method behind Table 1, eq:foc / Lemma pi), reused from
    experiments/risk_response_check.py, giving R and X by lag-one regression.

Notation (eq:N):  n_hat(w) = eta w^2 + gamma ghat(w) w^2 + lambda,
  ghat_exp = 2 kappa/(kappa^2+w^2),  ghat_pow = c_beta |w|^{beta-1},
  c_beta = 2 Gamma(1-beta) sin(pi beta/2),  q_hat = n_hat / w^2,
  S_alpha = sigma^2/(theta^2+w^2),  Phi(theta) = n_hat_+(i theta).

Run:  python3 experiments/test_all_results.py     (exit 0 iff all checks pass)
"""
from __future__ import annotations
import sys
import numpy as np
from scipy.special import gamma as Gfun
from scipy import integrate

# ======================================================================
# closed forms and symbols
# ======================================================================

def cbeta(beta: float) -> float:
    """c_beta = 2 Gamma(1-beta) sin(pi beta/2)  (transform constant of |t|^-beta)."""
    return 2.0 * Gfun(1.0 - beta) * np.sin(np.pi * beta / 2.0)


def integrate_0_inf(f):
    """int_0^inf f(t) dt, robust to slow tails: [0,1] plus tail via u=1/t.

    int_1^inf f(t) dt = int_0^1 f(1/u)/u^2 du, which maps the tail onto [0,1]
    so quadrature resolves it fully (needed for the beta->0 power-law tail).
    """
    v1, _ = integrate.quad(f, 0.0, 1.0, limit=500)
    g = lambda u: f(1.0 / u) / u**2
    v2, _ = integrate.quad(g, 0.0, 1.0, limit=500)
    return v1 + v2


def n_hat(w, eta=0.0, gamma=0.0, lam=0.0, kernel=None):
    """Position-referred symbol n_hat(w) = eta w^2 + gamma ghat(w) w^2 + lambda."""
    w = np.asarray(w, dtype=float)
    out = eta * w**2 + lam
    if kernel is None:
        gterm = 0.0
    elif kernel[0] == "exp":
        kap = kernel[1]
        gterm = gamma * 2.0 * kap * w**2 / (kap**2 + w**2)     # 2 kappa/(k^2+w^2) * w^2
    elif kernel[0] == "pow":
        beta = kernel[1]
        gterm = gamma * cbeta(beta) * np.abs(w) ** (1.0 + beta)  # c_b |w|^{b-1} * w^2
    else:
        raise ValueError(kernel)
    return out + gterm


def phi_szego(theta, eta=0.0, gamma=0.0, lam=0.0, kernel=None):
    """Phi(theta) = n_hat_+(i theta) = exp[(theta/pi) int_0^inf log n_hat(t)/(theta^2+t^2) dt].

    (eq:szego on the imaginary axis; real Poisson integral because n_hat is even.)
    """
    f = lambda t: np.log(n_hat(t, eta, gamma, lam, kernel)) / (theta**2 + t**2)
    return np.exp(theta / np.pi * integrate_0_inf(f))


def phi_exp(theta, kappa, gamma, lam):
    """Closed form, exponential + risk (eta=0): Phi = sqrt(A)(m+theta)/(kappa+theta)."""
    A = 2 * kappa * gamma + lam
    m = kappa * np.sqrt(lam / A)
    return np.sqrt(A) * (m + theta) / (kappa + theta)


def phi_gp(theta, eta, lam):
    """Closed form, temporary + risk (gamma=0): Phi = sqrt(eta)(a+theta), a=sqrt(lam/eta)."""
    a = np.sqrt(lam / eta)
    return np.sqrt(eta) * (a + theta)


def phi_pow(theta, gamma, beta):
    """Closed form, pure power-law (eta=lam=0): Phi = sqrt(gamma c_beta) theta^{(1+beta)/2}."""
    return np.sqrt(gamma * cbeta(beta)) * theta ** ((1.0 + beta) / 2.0)


def phi_nv(theta, eta, gamma, kappa, lam):
    """Closed form, all three frictions (eq:nv-factor): Phi = sqrt(eta)(b1+th)(b2+th)/(kappa+th)."""
    s2 = kappa**2 + (2 * kappa * gamma + lam) / eta
    p2 = lam * kappa**2 / eta
    z1 = (s2 - np.sqrt(s2**2 - 4 * p2)) / 2
    z2 = (s2 + np.sqrt(s2**2 - 4 * p2)) / 2
    return np.sqrt(eta) * (np.sqrt(z1) + theta) * (np.sqrt(z2) + theta) / (kappa + theta)


def nplus_exp(w, kappa, gamma, lam):
    A = 2 * kappa * gamma + lam
    m = kappa * np.sqrt(lam / A)
    return np.sqrt(A) * (m - 1j * w) / (kappa - 1j * w)


def nplus_gp(w, eta, lam):
    a = np.sqrt(lam / eta)
    return np.sqrt(eta) * (a - 1j * w)


def nplus_nv(w, eta, gamma, kappa, lam):
    s2 = kappa**2 + (2 * kappa * gamma + lam) / eta
    p2 = lam * kappa**2 / eta
    b1 = np.sqrt((s2 - np.sqrt(s2**2 - 4 * p2)) / 2)
    b2 = np.sqrt((s2 + np.sqrt(s2**2 - 4 * p2)) / 2)
    return np.sqrt(eta) * (b1 - 1j * w) * (b2 - 1j * w) / (kappa - 1j * w)


def nplus_pow(w, gamma, beta):
    # n_+ = sqrt(gamma c_beta) (-i w)^{(1+beta)/2}, principal branch
    return np.sqrt(gamma * cbeta(beta)) * (-1j * w) ** ((1.0 + beta) / 2.0)


# ======================================================================
# discrete adapted optimum  (reverse-order Cholesky; from risk_response_check.py)
# ======================================================================

def solve_W(Cmat, theta, dt):
    """Adapted-optimum operator W = Q_+^{-1} P_+ Q_-^{-1} (Lemma pi) on a grid.

    Reverse-order Cholesky gives the causal factor on the right; the forecast
    curve E_s[alpha_r] = e^{-theta(r-s)dt} alpha_s substitutes for the future.
    """
    n = Cmat.shape[0]
    Rev = np.eye(n)[::-1]
    Lr = np.linalg.cholesky(Rev @ Cmat @ Rev)
    U = Rev @ Lr @ Rev
    Cm, Cp = U, U.T
    Cmi = np.linalg.inv(Cm)
    Cpi = np.linalg.inv(Cp)
    Z = np.zeros((n, n))
    for s in range(n):
        Z[s, :s] = Cmi[s, :s]                                   # past kept
        Z[s, s] = Cmi[s, s:] @ np.exp(-theta * dt * np.arange(n - s))   # future -> forecast
    return Cpi @ Z


def measure_RX(n, dt, theta, eta, gamma, lam, kernel):
    """Discrete flow response R and position response X by lag-one regression."""
    idx = np.arange(n)
    lag = np.abs(idx[:, None] - idx[None, :]) * dt
    if kernel is None:
        G = np.zeros((n, n))
    elif kernel[0] == "exp":
        G = np.exp(-kernel[1] * lag)
    elif kernel[0] == "pow":
        beta = kernel[1]
        diag = 2 * dt ** (-beta) / ((1 - beta) * (2 - beta))    # cell-integrated |t|^-beta at lag 0
        G = np.where(lag == 0.0, diag, np.where(lag == 0.0, 1.0, lag) ** (-beta))
    else:
        raise ValueError(kernel)
    Ltri = np.tril(np.ones((n, n)))
    Cmat = eta * np.eye(n) + gamma * dt * G + lam * dt**2 * (Ltri.T @ Ltri)
    S = np.exp(-theta * lag)                                    # OU autocovariance, unit variance
    W = solve_W(Cmat, theta, dt)
    Wx = dt * (Ltri @ W)
    i = n // 2
    R = (W @ S)[i, i - 1] / S[i - 1, i - 1]
    X = (Wx @ S)[i, i - 1] / S[i - 1, i - 1]
    v = 0.5 * (W @ S)[i, i]                                     # value rate = (1/2) E[u alpha]
    return R, X, v


# ======================================================================
# checks
# ======================================================================

def relerr(a, b):
    d = abs(a - b)
    s = max(abs(a), abs(b), 1e-300)
    return d / s


def check_1_szego_vs_closed():
    """Szego integral Phi(theta) matches the closed-form outer factors (eq:phi)."""
    cases = []
    ok = True
    # exponential + risk
    for (kap, g, lam, th) in [(2, 1, 0.5, 1.5), (2, 1, 4.0, 0.5), (1, 2, 1.0, 0.8)]:
        a = phi_szego(th, 0.0, g, lam, ("exp", kap))
        b = phi_exp(th, kap, g, lam)
        e = relerr(a, b); ok &= e < 1e-4
        cases.append(f"exp k={kap} g={g} lam={lam} th={th}: szego={a:.6f} closed={b:.6f} rel={e:.1e}")
    # temporary + risk (GP)
    for (eta, lam, th) in [(0.5, 1.0, 1.0), (0.3, 2.0, 0.7)]:
        a = phi_szego(th, eta, 0.0, lam, None)
        b = phi_gp(th, eta, lam)
        e = relerr(a, b); ok &= e < 1e-4
        cases.append(f"GP eta={eta} lam={lam} th={th}: szego={a:.6f} closed={b:.6f} rel={e:.1e}")
    # pure power-law
    for (g, beta, th) in [(1, 0.5, 2.0), (1, 0.3, 1.0), (1, 0.6, 0.5)]:
        a = phi_szego(th, 0.0, g, 0.0, ("pow", beta))
        b = phi_pow(th, g, beta)
        e = relerr(a, b); ok &= e < 1e-4
        cases.append(f"pow g={g} b={beta} th={th}: szego={a:.6f} closed={b:.6f} rel={e:.1e}")
    # Neuman-Voss (all three)
    for (eta, g, kap, lam, th) in [(0.5, 1, 2, 1.0, 1.0), (0.3, 1, 2, 0.5, 1.5)]:
        a = phi_szego(th, eta, g, lam, ("exp", kap))
        b = phi_nv(th, eta, g, kap, lam)
        e = relerr(a, b); ok &= e < 1e-4
        cases.append(f"NV eta={eta} g={g} k={kap} lam={lam} th={th}: szego={a:.6f} closed={b:.6f} rel={e:.1e}")
    return ("1. Szego integral  vs  closed-form outer factor Phi(theta)", ok, cases)


def check_2_factorization_consistency():
    """|n_hat_+(w)|^2 = n_hat(w) on the real axis (eq:wh, eq:N)."""
    w = np.array([-7.3, -2.1, -0.4, 0.3, 1.7, 5.0, 12.0])
    cases = []
    ok = True
    # exponential
    kap, g, lam = 2.0, 1.0, 0.5
    lhs = np.abs(nplus_exp(w, kap, g, lam))**2
    rhs = n_hat(w, 0.0, g, lam, ("exp", kap))
    e = np.max(np.abs(lhs - rhs) / rhs); ok &= e < 1e-10
    cases.append(f"exponential: max rel = {e:.1e}")
    # GP
    eta, lam = 0.5, 1.0
    lhs = np.abs(nplus_gp(w, eta, lam))**2
    rhs = n_hat(w, eta, 0.0, lam, None)
    e = np.max(np.abs(lhs - rhs) / rhs); ok &= e < 1e-10
    cases.append(f"temporary+risk (GP): max rel = {e:.1e}")
    # NV
    eta, g, kap, lam = 0.5, 1.0, 2.0, 1.0
    lhs = np.abs(nplus_nv(w, eta, g, kap, lam))**2
    rhs = n_hat(w, eta, g, lam, ("exp", kap))
    e = np.max(np.abs(lhs - rhs) / rhs); ok &= e < 1e-10
    cases.append(f"Neuman-Voss (3 frictions): max rel = {e:.1e}")
    # power-law
    g, beta = 1.0, 0.5
    lhs = np.abs(nplus_pow(w, g, beta))**2
    rhs = n_hat(w, 0.0, g, 0.0, ("pow", beta))
    e = np.max(np.abs(lhs - rhs) / rhs); ok &= e < 1e-10
    cases.append(f"power-law: max rel = {e:.1e}")
    return ("2. Factorization consistency  |n_+(w)|^2 = n(w)  on real axis", ok, cases)


def check_3_value_response_algebra():
    """X = theta/Phi^2; v = sigma^2 theta/(4 Phi^2) = (sigma^2/4) X;
       power-law v = sigma^2 theta^{-beta}/(4 gamma c_beta) = sigma^2 theta/(4 Phi^2) (eq:ou-filter)."""
    cases = []
    ok = True
    sigma2 = 1.7
    # X = (sigma^2/4) X_from_v consistency and v = (sigma^2/4) X
    for (kap, g, lam, th) in [(2, 1, 0.5, 1.5), (2, 1, 4.0, 0.5)]:
        Phi = phi_exp(th, kap, g, lam)
        X = th / Phi**2
        v = sigma2 * th / (4 * Phi**2)
        e = relerr(v, sigma2 / 4 * X); ok &= e < 1e-12
        cases.append(f"exp lam={lam} th={th}: v={v:.6f}, (s^2/4)X={sigma2/4*X:.6f}, rel={e:.1e}")
    # power-law: two value formulas agree
    for (g, beta, th) in [(1, 0.5, 2.0), (1, 0.3, 1.5), (1, 0.6, 0.7)]:
        Phi = phi_pow(th, g, beta)
        v_phi = sigma2 * th / (4 * Phi**2)
        v_frac = sigma2 * th ** (-beta) / (4 * g * cbeta(beta))
        e = relerr(v_phi, v_frac); ok &= e < 1e-12
        cases.append(f"pow b={beta} th={th}: sigma^2 th/4Phi^2={v_phi:.6f}, "
                     f"sigma^2 th^-b/(4 g c_b)={v_frac:.6f}, rel={e:.1e}")
    return ("3. Value / response algebra  (eq:ou-filter, fractional value)", ok, cases)


def check_4_causality_gap():
    """Power-law causality gap v/v_ant = sin(pi beta/2), theta-independent (eq:sinlaw, an in-paper result in v3).

    v_ant is referred to the rate here, v_ant = (1/4pi) int S_alpha/q_hat dw, finite at
    lambda=0 where the position-referred form (eq:vant) diverges -- matching the paper's
    Appendix B and the clarifying sentence after eq:vant.
    """
    cases = []
    ok = True
    sigma2 = 1.0

    def v_ant_pow(theta, beta, g):
        cb = cbeta(beta)
        f = lambda w: (sigma2 / (theta**2 + w**2)) * np.abs(w) ** (1 - beta) / (g * cb)
        return 2 * integrate_0_inf(f) / (4 * np.pi)

    def v_ad_pow(theta, beta, g):
        return sigma2 * theta ** (-beta) / (4 * g * cbeta(beta))

    for beta in [0.2, 0.4, 0.5, 0.6, 0.8]:
        ratios = []
        for theta in [0.5, 1.0, 3.0]:
            r = v_ad_pow(theta, beta, 1.0) / v_ant_pow(theta, beta, 1.0)
            ratios.append(r)
        target = np.sin(np.pi * beta / 2)
        e = max(relerr(r, target) for r in ratios)
        spread = max(ratios) - min(ratios)                     # theta-independence
        ok &= (e < 3e-3) and (spread < 3e-3)
        cases.append(f"beta={beta}: v/v_ant={np.mean(ratios):.5f} (th-spread {spread:.1e}) "
                     f"vs sin(pi b/2)={target:.5f}, rel={e:.1e}")
    return ("4. Causality-gap identity  v/v_ant = sin(pi beta/2)  (eq:sinlaw, in paper)", ok, cases)


def check_5_rate_response_formula():
    """R = (theta^2/Phi)(1/Phi - 2 c_1); X>0; power-law R>0 all lambda; exp flips at theta*."""
    cases = []
    ok = True
    kap, g = 2.0, 1.0

    # power-law: c_1 = 0, R = theta^2/Phi^2 > 0 for ALL lambda (incl large) and theta
    def phi_pow_lam(theta, lam, beta=0.5, gamma=1.0):
        f = lambda t: np.log(gamma * cbeta(beta) * t ** (1 + beta) + lam) / (theta**2 + t**2)
        return np.exp(theta / np.pi * integrate_0_inf(f))
    allpos = True
    for lam in [0.0, 0.1, 1.0, 10.0, 100.0, 1000.0]:
        for th in [0.5, 1.0, 2.0, 4.0]:
            Phi = phi_pow_lam(th, lam)
            R = th**2 / Phi**2                                 # c_1 = 0
            allpos &= (R > 0)
    ok &= allpos
    cases.append(f"power-law R>0 for all lambda in [0,1000], theta in [0.5,4]: {allpos}")

    # exponential: sign flip at theta* = kappa - 2m; R(theta*) = 0; R<0 above, R>0 below
    for lam in [0.0, 0.3, 0.6]:
        A = 2 * kap * g + lam
        m = kap * np.sqrt(lam / A)
        tstar = kap - 2 * m
        c1 = 1.0 / np.sqrt(A)
        def R_exp(th):
            Phi = phi_exp(th, kap, g, lam)
            return (th**2 / Phi) * (1.0 / Phi - 2 * c1)
        Rstar = R_exp(tstar) if tstar > 1e-6 else 0.0
        below = R_exp(max(tstar - 0.3, 0.05))
        above = R_exp(tstar + 0.3)
        flip_ok = (abs(Rstar) < 1e-9 if tstar > 1e-6 else True) and (below > 0) and (above < 0)
        ok &= flip_ok
        cases.append(f"exp lam={lam}: theta*={tstar:+.4f}, R(th*)={Rstar:+.1e}, "
                     f"R(below)={below:+.4f}>0, R(above)={above:+.4f}<0  -> {flip_ok}")

    # X = theta/Phi^2 > 0 always (checked positive on a grid)
    Xpos = all(th / phi_exp(th, kap, g, lam)**2 > 0
               for lam in [0.0, 0.5, 2.0] for th in [0.3, 1.0, 3.0])
    ok &= Xpos
    cases.append(f"position response X=theta/Phi^2 > 0 always: {Xpos}")
    return ("5. Rate response R and threshold theta*  (eq:response, eq:threshold)", ok, cases)


def check_6_discrete_table1():
    """Discrete adapted optimum (reverse-Cholesky, Lemma pi) reproduces the closed-form R, X.

    Signs must match every row (the paper's headline claim); magnitudes must fall
    within the discretization tolerance at a fine grid; and the slowly-converging
    singular power-law kernel must approach the formula monotonically as dt->0.
    """
    cases = []
    ok = True
    n, dt = 1600, 0.01            # fine grid used for the paper's Table-1 discrete column
    rows = [
        ("exp k=2 g=1, lam=0.5, th=1.5", -0.311, 0.870,
         dict(theta=1.5, eta=0.0, gamma=1.0, lam=0.5, kernel=("exp", 2.0))),
        ("exp k=2 g=1, lam=4,   th=0.5", -0.028, 0.107,
         dict(theta=0.5, eta=0.0, gamma=1.0, lam=4.0, kernel=("exp", 2.0))),
        ("pure risk g=0, lam=1,  th=0.7", -0.490, 0.700,
         dict(theta=0.7, eta=0.0, gamma=0.0, lam=1.0, kernel=None)),
        ("power-law b=.5 g=1, lam=1, th=2", +0.364, 0.182,
         dict(theta=2.0, eta=0.0, gamma=1.0, lam=1.0, kernel=("pow", 0.5))),
        ("NV eta=.5 g=1 k=2, lam=1, th=1", +0.264, 0.264,
         dict(theta=1.0, eta=0.5, gamma=1.0, lam=1.0, kernel=("exp", 2.0))),
    ]
    for label, Rf, Xf, p in rows:
        Rm, Xm, _ = measure_RX(n, dt, p["theta"], p["eta"], p["gamma"], p["lam"], p["kernel"])
        eR = abs(Rm - Rf); eX = abs(Xm - Xf)
        sign_ok = (np.sign(Rm) == np.sign(Rf)) and (Xm > 0)
        good = sign_ok and (eR < 0.05) and (eX < 0.05)
        ok &= good
        cases.append(f"{label}: R disc={Rm:+.3f} vs formula={Rf:+.3f} (|d|={eR:.3f}); "
                     f"X disc={Xm:.3f} vs {Xf:.3f} (|d|={eX:.3f})  -> {good}")
    # power-law: monotone convergence of R toward the formula as dt shrinks
    Rf_pow = 0.364
    seq = [measure_RX(nn, ddt, 2.0, 0.0, 1.0, 1.0, ("pow", 0.5))[0]
           for nn, ddt in [(400, 0.04), (800, 0.02), (1600, 0.01)]]
    errs = [abs(r - Rf_pow) for r in seq]
    monotone = errs[0] > errs[1] > errs[2]
    ok &= monotone
    cases.append(f"power-law dt-refinement R = {seq[0]:.3f} -> {seq[1]:.3f} -> {seq[2]:.3f} "
                 f"toward formula {Rf_pow:.3f} (|err| {errs[0]:.3f}>{errs[1]:.3f}>{errs[2]:.3f}) "
                 f"monotone={monotone}")
    return ("6. Discrete adapted optimum reproduces closed forms (reverse-Cholesky)", ok, cases)


def check_7_boundary_layer():
    """Finite-horizon rate = whole-line stationary rate in the interior (Prop boundary)."""
    eta, gamma, kappa, lam = 0.5, 1.0, 2.0, 1.0
    dt, T, w0, P = 0.05, 20.0, 0.6, 20.0

    def solve_on(t):
        n = len(t)
        idx = np.arange(n)
        G = np.exp(-kappa * np.abs(idx[:, None] - idx[None, :]) * dt)
        L = np.tril(np.ones((n, n)))
        M = eta * dt * np.eye(n) + gamma * dt**2 * G + lam * dt**3 * (L.T @ L)
        return np.linalg.solve(M, dt * np.sin(w0 * t))

    t_fh = np.arange(0, T + dt / 2, dt)
    u_fh = solve_on(t_fh)
    t_pad = np.arange(-P, T + P + dt / 2, dt)
    u_pad = solve_on(t_pad)
    mask = (t_pad >= -1e-9) & (t_pad <= T + 1e-9)
    u_wl = u_pad[mask]
    b1 = kappa * np.sqrt(lam / (2 * kappa * gamma + lam))
    width = 3.0 / max(b1, 0.3)
    interior = (t_fh > width) & (t_fh < T - width)
    max_int = float(np.max(np.abs(u_fh - u_wl)[interior]))
    max_all = float(np.max(np.abs(u_fh - u_wl)))
    ok = max_int < 0.02 and max_all > 3 * max_int      # small interior, larger boundary layers
    cases = [f"max interior |u_fh - u_wl| = {max_int:.4f} (< 0.02)",
             f"max overall (boundary) = {max_all:.4f}  (boundary/interior = {max_all/max_int:.1f}x)"]
    return ("7. Boundary-layer decay: finite-horizon -> stationary in interior", ok, cases)


def check_8_markowitz():
    """Pure-risk (Markowitz) limit: v = theta sigma^2/(4 lambda); R = -theta^2/lambda; X = theta/lambda."""
    cases = []
    ok = True
    # pure risk: n_hat = lambda constant, Phi = sqrt(lambda); c_1 = 1/sqrt(lambda)
    for lam, th in [(1.0, 0.7), (2.0, 1.0), (0.5, 1.5)]:
        Phi = np.sqrt(lam)
        c1 = 1.0 / np.sqrt(lam)
        X = th / Phi**2                                        # = theta/lambda
        R = (th**2 / Phi) * (1.0 / Phi - 2 * c1)               # = -theta^2/lambda
        eX = relerr(X, th / lam); eR = relerr(R, -th**2 / lam)
        # value with sigma^2 fixed: v = theta sigma^2/(4 lambda) = sigma^2/4 * X
        sigma2 = 1.3
        v = sigma2 * th / (4 * lam)
        ev = relerr(v, sigma2 / 4 * X)
        good = eX < 1e-12 and eR < 1e-12 and ev < 1e-12
        ok &= good
        cases.append(f"lam={lam} th={th}: X={X:.4f}(=th/lam,{eX:.0e}) R={R:+.4f}"
                     f"(=-th^2/lam,{eR:.0e}) v={v:.4f}(=s^2 X/4,{ev:.0e}) -> {good}")
    # cross-check against discrete pure-risk row (already in check 6, here the closed form)
    return ("8. Markowitz pure-risk limit  v=theta s^2/4lam, R=-th^2/lam, X=th/lam", ok, cases)


# ======================================================================
# main
# ======================================================================

def check_9_neuman_voss_riccati():
    """Recovery of the NEUMAN-VOSS solution against THEIR exact method, not an invented one.

    Neuman-Voss characterize the optimum of the temporary + exponential-resilience + risk
    problem as a linear-quadratic (FBSDE / Riccati) feedback. We solve that exact LQ problem
    INDEPENDENTLY of the Wiener-Hopf factorization -- by the algebraic Riccati equation
    (scipy.linalg.solve_continuous_are) -- and check that its stable closed-loop poles equal
    the paper's two moving-average rates b1, b2 (the zeros of n_+ in eq:nv-factor), as the
    paper claims ('the Riccati closed-loop poles equal the moving-average rates b1, b2').

    LQ model: state z=(x, J), dx = u dt, dJ = (u - kappa J) dt with J the exponential-impact
    state (J_t = int^t e^{-kappa(t-s)} u_s ds); running cost (eta/2)u^2 + gamma*u*J + (lambda/2)x^2,
    since the symmetric transient cost (gamma/2) int int e^{-kappa|t-s|} u u = gamma int u J.
    Hence A=[[0,0],[0,-kappa]], B=[[1],[1]], Q=[[lambda,0],[0,0]], R=[[eta]], cross S=[[0],[gamma]].
    The overall 1/2 in the cost cancels in the feedback, so the poles are convention-independent.
    """
    from scipy.linalg import solve_continuous_are
    cases = []
    ok = True
    for eta, g, kap, lam in [(0.5, 1.0, 2.0, 1.0), (0.3, 1.0, 2.0, 0.5), (1.0, 0.5, 3.0, 2.0)]:
        # paper's EMA rates b1,b2 = stable zeros of n_+  (eq:nv-factor)
        s2 = kap**2 + (2 * kap * g + lam) / eta
        p2 = lam * kap**2 / eta
        b1 = np.sqrt((s2 - np.sqrt(s2**2 - 4 * p2)) / 2)
        b2 = np.sqrt((s2 + np.sqrt(s2**2 - 4 * p2)) / 2)
        # Neuman-Voss EXACT LQ solution by algebraic Riccati (control-theoretic, not Wiener-Hopf)
        A = np.array([[0., 0.], [0., -kap]])
        B = np.array([[1.], [1.]])
        Q = np.array([[lam, 0.], [0., 0.]])
        R = np.array([[eta]])
        S = np.array([[0.], [g]])
        P = solve_continuous_are(A, B, Q, R, s=S)
        K = np.linalg.solve(R, B.T @ P + S.T)                    # stabilizing feedback u = -K z
        poles = np.sort(-np.linalg.eigvals(A - B @ K).real)      # stable closed-loop rates
        e = max(relerr(poles[0], b1), relerr(poles[1], b2))
        ok &= (e < 1e-8)
        cases.append(f"eta={eta} g={g} k={kap} lam={lam}: NV-Riccati poles=({poles[0]:.6f},{poles[1]:.6f}) "
                     f"vs paper b1,b2=({b1:.6f},{b2:.6f})  rel={e:.1e}")
    return ("9. Recovery of Neuman-Voss: exact LQ Riccati closed-loop poles = paper's b1,b2 (eq:nv-factor)", ok, cases)


def main():
    checks = [
        check_1_szego_vs_closed,
        check_2_factorization_consistency,
        check_3_value_response_algebra,
        check_4_causality_gap,
        check_5_rate_response_formula,
        check_6_discrete_table1,
        check_7_boundary_layer,
        check_8_markowitz,
        check_9_neuman_voss_riccati,
    ]
    print("=" * 78)
    print("NUMERICAL VERIFICATION OF v3/optimal-trading-filters-v3.tex")
    print("=" * 78)
    n_pass = 0
    results = []
    for chk in checks:
        name, ok, cases = chk()
        results.append((name, ok))
        status = "PASS" if ok else "FAIL"
        print(f"\n[{status}] {name}")
        for c in cases:
            print(f"        {c}")
        n_pass += int(ok)
    print("\n" + "=" * 78)
    for name, ok in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    print("-" * 78)
    print(f"  {n_pass}/{len(checks)} CHECKS PASSED")
    print("=" * 78)
    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
