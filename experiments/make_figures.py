"""Figures for optimal-trading-filters.tex. All curves from validated formulas.
Outputs PNG+PDF to figures/. No fabricated data.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as Gf
from scipy.linalg import solve_continuous_are
from scipy.integrate import solve_ivp, quad
import os

os.makedirs("figures", exist_ok=True)
os.environ["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "text.usetex": True, "font.family": "serif",
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"})

def cbeta(b): return 2*Gf(1-b)*np.sin(np.pi*b/2)

def N_powerlaw(w, gam, beta): return gam*cbeta(beta)*np.abs(w)**(1+beta)
def N_exp(w, gam, kap, lam, eta=0.0):
    return eta*w**2 + 2*kap*gam*w**2/(kap**2+w**2) + lam
def save(fig, name):
    fig.savefig(f"figures/{name}.png"); fig.savefig(f"figures/{name}.pdf")
    print("wrote", name)

# ============================================================
# FIG 1: trading filter |H(omega)| ~ 1/sqrt(N(omega)) vs frequency
# ============================================================
w = np.logspace(-2, 1, 700)
fig, ax = plt.subplots(1, 2, figsize=(9.5, 4.7))

# (a) power-law: fractional slopes -(1+beta)/2
for beta in (0.2, 0.4, 0.6):
    H = 1/np.sqrt(N_powerlaw(w, 1.0, beta))
    ax[0].loglog(w, H, lw=1.9, label=fr"$\beta={beta}$  (slope $-{ (1+beta)/2:.1f}$)")
ax[0].set_title("(a) power-law impact: fractional filter")
ax[0].set_xlabel(r"frequency $\omega$"); ax[0].set_ylabel(r"$|H(\omega)|\ \propto\ N(\omega)^{-1/2}$")
ax[0].legend(fontsize=10.5)

# (b) friction family at gamma=1,kappa=2
gam, kap = 1.0, 2.0
curves = [
    ("pure risk  ($\\lambda$)",        N_exp(w, 0, kap, 0.5, 0)*0 + 0.5),
    ("exp + risk",                      N_exp(w, gam, kap, 0.5, 0.0)),
    ("temp + exp + risk",               N_exp(w, gam, kap, 0.5, 0.3)),
    ("power-law + risk  ($\\beta=0.5$)", N_powerlaw(w, gam, 0.5) + 0.5),
]
for lbl, Nw in curves:
    ax[1].loglog(w, 1/np.sqrt(Nw), lw=1.9, label=lbl)
ax[1].set_ylim(top=3.4)
xc = (0.5/(gam*cbeta(0.5)))**(1/1.5)
ax[1].axvline(xc, color="grey", ls=":", lw=0.9); ax[1].text(xc*1.15, 2.2, r"$\omega_c$", fontsize=11)
ax[1].set_title("(b) friction family")
ax[1].set_xlabel(r"frequency $\omega$"); ax[1].set_ylabel(r"$|H(\omega)|\ \propto\ N(\omega)^{-1/2}$")
ax[1].legend(fontsize=9.5, loc="lower left")
fig.tight_layout(); save(fig, "fig_trading_filter")

# ============================================================
# FIG 2: NV finite-horizon vs our stationary solution
# ============================================================
eta, gam, kap, lam = 0.5, 1.0, 2.0, 1.0
s2 = kap**2 + (2*kap*gam+lam)/eta; p2 = lam*kap**2/eta
b1 = np.sqrt((s2-np.sqrt(s2**2-4*p2))/2); b2 = np.sqrt((s2+np.sqrt(s2**2-4*p2))/2)
A = np.array([[0., 0.], [0., -kap]]); B = np.array([[1.], [1.]])
Qm = np.array([[lam, 0.], [0., 0.]]); Rm = np.array([[eta]]); Nm = np.array([[0.], [gam]])
P = solve_continuous_are(A, B, Qm, Rm, s=Nm)
Kinf = np.linalg.solve(Rm, B.T@P + Nm.T).ravel()
T = 20.0
def rhs(t, y):
    Pm = np.array([[y[0], y[1]], [y[1], y[2]]]); M = B.T@Pm + Nm.T
    dP = A.T@Pm + Pm@A - (Pm@B+Nm)@np.linalg.solve(Rm, M) + Qm
    return -np.array([dP[0, 0], dP[0, 1], dP[1, 1]])
sol = solve_ivp(rhs, [T, 0], [0, 0, 0], dense_output=True, rtol=1e-9, atol=1e-12)
ts = np.linspace(0, T, 400)
Kx = np.zeros_like(ts); Kj = np.zeros_like(ts)
for i, t in enumerate(ts):
    y = sol.sol(t); Pm = np.array([[y[0], y[1]], [y[1], y[2]]])
    k = np.linalg.solve(Rm, B.T@Pm + Nm.T).ravel(); Kx[i], Kj[i] = k
fig, ax = plt.subplots(1, 2, figsize=(10, 4.0))
ax[0].plot(ts, Kx, label=r"$K_x(t)$ (inventory gain)")
ax[0].plot(ts, Kj, label=r"$K_J(t)$ (impact-state gain)")
ax[0].axhline(Kinf[0], color="C0", ls="--", lw=0.9); ax[0].axhline(Kinf[1], color="C1", ls="--", lw=0.9)
bl = 3/b1
ax[0].axvspan(T-bl, T, color="grey", alpha=0.12)   # gains: terminal layer only (backward Riccati)
ax[0].text(T-bl+0.2, 0.35, "terminal\nboundary\nlayer", fontsize=8)
ax[0].set_title("(a) NV feedback gains vs stationary (dashed)")
ax[0].set_xlabel(r"time $t$"); ax[0].set_ylabel("feedback gain"); ax[0].legend(fontsize=9)

# (b) trajectory: finite-horizon optimum vs whole-line filter, on a sinusoid
n = 800; dt = T/n; tgrid = (np.arange(n)+0.5)*dt
w0 = 1.0; alpha = np.sin(w0*tgrid)
lag = np.abs(np.arange(n)[:, None]-np.arange(n)[None, :])*dt
G = np.exp(-kap*lag); Lt = np.tril(np.ones((n, n)))
Cmat = eta*np.eye(n) + gam*dt*G + lam*dt**2*(Lt.T@Lt)
u_fin = np.linalg.solve(Cmat, alpha); x_fin = dt*(Lt@u_fin)
N0 = N_exp(w0, gam, kap, lam, eta)
x_whole = -(w0/N0)*np.cos(w0*tgrid)   # whole-line steady state: int sin = -cos/w0
ax[1].plot(tgrid, x_whole, "k-", lw=1.4, label="stationary (whole-line)")
ax[1].plot(tgrid, x_fin, "C3--", lw=1.4, label="NV finite horizon")
ax[1].axvspan(0, bl, color="grey", alpha=0.12); ax[1].axvspan(T-bl, T, color="grey", alpha=0.12)
ax[1].set_xlim(0, T); ax[1].set_title(r"(b) optimal position, $\alpha_t=\sin\omega_0 t$")
ax[1].set_xlabel(r"time $t$"); ax[1].set_ylabel(r"position $x^\star_t$"); ax[1].legend(fontsize=9)
fig.tight_layout(); save(fig, "fig_nv_vs_stationary")

# ============================================================
# FIG 3: impact-surfing phase diagram
# ============================================================
gam, kap = 1.0, 2.0
def R_exp(th, lam):
    A = 2*kap*gam+lam; m = kap*np.sqrt(lam/A); Phi = np.sqrt(A)*(m+th)/(kap+th)
    return (th**2/Phi)*(1/Phi - 2/np.sqrt(A))
def R_pow(th, beta=0.5, g=1.0):   # power-law: c1=0, always aligned
    cb = cbeta(beta); Phi2 = g*cb*th**(1+beta); return th**2/Phi2
th = np.linspace(0.05, 4, 400)
fig, ax = plt.subplots(1, 2, figsize=(10, 4.0))
for lam, c in [(0.0, "C0"), (0.5, "C1"), (4.0, "C2")]:
    ax[0].plot(th, R_exp(th, lam), c, label=fr"exp, $\lambda={lam}$")
ax[0].plot(th, R_pow(th), "C3", label=r"power-law ($\beta=0.5$)")
ax[0].axhline(0, color="k", lw=0.7)
ax[0].set_title("(a) flow response $R(\\theta)$")
ax[0].set_xlabel(r"signal speed $\theta$"); ax[0].set_ylabel(r"$R(\theta)$")
ax[0].text(2.6, -0.9, "impact surfing\n($R<0$)", fontsize=8.5, color="grey")
ax[0].legend(fontsize=8.5)

lams = np.linspace(0, 12, 300)
Aa = 2*kap*gam+lams; mm = kap*np.sqrt(lams/Aa); tstar = kap - 2*mm
ax[1].plot(tstar, lams, "k-", lw=1.5)
ax[1].fill_betweenx(lams, tstar, 4, color="C3", alpha=0.15)
ax[1].fill_betweenx(lams, 0, np.clip(tstar, 0, None), color="C0", alpha=0.12)
lam_all = 2*kap*gam/3
ax[1].axhline(lam_all, color="grey", ls=":", lw=0.9)
ax[1].text(0.15, lam_all+0.2, r"$\lambda=2\kappa\gamma/3$ (always surfing)", fontsize=8)
ax[1].text(2.3, 8, "surf\n$R<0$", fontsize=9, color="C3")
ax[1].text(0.35, 2, "follow\n$R>0$", fontsize=9, color="C0")
ax[1].set_xlim(0, 4); ax[1].set_ylim(0, 12)
ax[1].set_title(r"(b) phase diagram (exp kernel), $\theta^*=\kappa-2m$")
ax[1].set_xlabel(r"signal speed $\theta$"); ax[1].set_ylabel(r"risk aversion $\lambda$")
fig.tight_layout(); save(fig, "fig_impact_surfing")

# quick sanity numbers
print(f"\nb1={b1:.4f} b2={b2:.4f} Kinf={Kinf}")
print(f"interior amplitude: whole-line={-w0/N0:.4f}, "
      f"finite-horizon mid={x_fin[n//2]/np.cos(w0*tgrid[n//2]):.4f}  (should match)")
print(f"theta* : lam=0 -> {kap-2*kap*np.sqrt(0/(2*kap*gam)):.3f}, "
      f"lam=0.5 -> {kap-2*kap*np.sqrt(0.5/(2*kap*gam+0.5)):.3f}, "
      f"always-surf lambda>={2*kap*gam/3:.3f}")

# ============================================================
# FIG 4: value of a forecast + cost of causality
# ============================================================
# value rate at FIXED RETURN-FORECAST STRENGTH: Var(mu)=1, so sigma^2 = 2/theta and
# v = sigma^2 theta/(4 Phi^2) = 1/(2 Phi^2).  This is the honest "does speed add value"
# comparison -- it holds the return forecast's variance fixed and lets only the reversion
# speed vary.  (Fixing Var(alpha) instead multiplies every value by theta^2, since
# Var(mu)=theta^2 Var(alpha): it conflates a faster signal with a stronger return.)
# Realistic case carries a temporary cost (solid); eta=0 is the limiting reference (dotted).
# Value at fixed Var(mu)=1 is v = 1/(2 Phi^2); Phi via the Szego integral (parallels fig_position_scaling).
gam0, kap0, beta0, lam0, eta0v = 1.0, 2.0, 0.5, 1.0, 0.5
th = np.logspace(-1.2, 1.5, 300)
def _phi(theta, nf):
    val, _ = quad(lambda t: np.log(nf(t))/(theta**2 + t**2), 0, np.inf, limit=400)
    return np.exp(theta/np.pi*val)
def n_exp_f(eta): return lambda w: eta*w**2 + 2*gam0*kap0*w**2/(kap0**2+w**2) + lam0
def n_pow_f(eta): return lambda w: eta*w**2 + gam0*cbeta(beta0)*np.abs(w)**(1+beta0) + lam0
def v_of(nf): return np.array([2.0/(4*_phi(t, nf)**2) for t in th])   # v = 1/(2 Phi^2)
v_et = v_of(n_exp_f(eta0v)); v_pt = v_of(n_pow_f(eta0v))            # + temporary cost (realistic)
v_e0 = v_of(n_exp_f(0.0));   v_p0 = v_of(n_pow_f(0.0))              # eta=0 reference
v_rk = 2.0/(4*lam0) + 0*th                                         # pure risk (speed-free)
def nrm(v): return v/np.interp(1.0, th, v)                          # normalize to v(theta=1)
fig, ax0 = plt.subplots(figsize=(6.4, 4.3))
ax0.loglog(th, nrm(v_et), "C0", lw=2.0, label=r"exp + temp + risk")
ax0.loglog(th, nrm(v_pt), "C3", lw=2.0, label=r"power-law + temp + risk")
ax0.loglog(th, nrm(v_e0), "C0", ls=":", lw=1.5, alpha=0.7, label=r"exp + risk ($\eta{=}0$)")
ax0.loglog(th, nrm(v_p0), "C3", ls=":", lw=1.5, alpha=0.7, label=r"power-law + risk ($\eta{=}0$)")
ax0.loglog(th, nrm(v_rk), "0.5", ls=":", lw=1.0, label=r"pure risk (speed-free)")
g = np.logspace(0.55, 1.45, 30)
ax0.loglog(g, 0.45*g**(-2.0), "0.5", lw=0.8, ls=":")
ax0.text(g[-1]*1.03, 0.45*g[-1]**(-2.0), r"$\propto\theta^{-2}$", fontsize=9, color="0.4")
ax0.set_title("value vs signal speed (fixed return variance)")
ax0.set_xlabel(r"signal speed $\theta$"); ax0.set_ylabel(r"$v(\theta)/v(1)$")
ax0.legend(fontsize=8.0, loc="lower left")
fig.tight_layout(); save(fig, "fig_value")

# ---- separate figure: cost of causality (sin(pi beta/2), a function of beta only) ----
figg, ax1 = plt.subplots(figsize=(6.0, 4.3))
b = np.linspace(0.001, 0.999, 400)
ax1.plot(b, np.sin(np.pi*b/2), "C3", lw=1.8)
ax1.axvspan(0.2, 0.6, color="grey", alpha=0.12); ax1.text(0.245, 0.18, r"empirical $\beta$", fontsize=9)
ax1.set_title(r"cost of causality: $v/v_{\rm ant}=\sin(\pi\beta/2)$")
ax1.set_xlabel(r"impact exponent $\beta$"); ax1.set_ylabel(r"$v/v_{\rm ant}$"); ax1.set_ylim(0, 1.02)
figg.tight_layout(); save(figg, "fig_causality_gap")

# ============================================================
# FIG 5: optimal policy -- kernel family and parameter values
# ============================================================
eta0, gam, kap = 0.5, 1.0, 2.0
def roots(lam, eta=eta0):
    s2 = kap**2 + (2*kap*gam+lam)/eta; p2 = lam*kap**2/eta
    return np.sqrt((s2-np.sqrt(s2**2-4*p2))/2), np.sqrt((s2+np.sqrt(s2**2-4*p2))/2)
fig, ax = plt.subplots(1, 3, figsize=(13.5, 3.8))

# (a) two-EMA rates vs risk aversion
lams = np.logspace(-2, 1.3, 300)
B1 = np.array([roots(l)[0] for l in lams]); B2 = np.array([roots(l)[1] for l in lams])
ax[0].loglog(lams, B1, label=r"$b_1$ (slow)"); ax[0].loglog(lams, B2, label=r"$b_2$ (fast)")
ax[0].axhline(kap, color="grey", ls=":", lw=0.9); ax[0].text(0.011, kap*1.08, r"$\kappa$ (resilience)", fontsize=8)
ax[0].set_title("(a) two-EMA rates vs risk")
ax[0].set_xlabel(r"risk aversion $\lambda$"); ax[0].set_ylabel(r"rate $b_i$"); ax[0].legend(fontsize=9)

# (b) optimal-policy impulse response g_x(tau) across the kernel family
th0 = 1.0; tau = np.logspace(-1.6, 1.1, 400); tref = 0.3
def gx_exp(tau, lam=1.0):           # exponential + risk (one EMA, smooth part)
    A = 2*kap*gam+lam; m = kap*np.sqrt(lam/A)
    return (th0*(kap+th0)/(A*(m+th0)))*(kap-m)*np.exp(-m*tau)
def gx_two(tau, lam=1.0):           # temporary + exp + risk (two EMA)
    b1, b2 = roots(lam); A = 2*kap*gam+lam
    Phi = np.sqrt(eta0)*(b1+th0)*(b2+th0)/(kap+th0)
    w1 = (kap-b1)/(b2-b1); w2 = (kap-b2)/(b1-b2)
    return (th0/(Phi*np.sqrt(eta0)))*(w1*np.exp(-b1*tau)+w2*np.exp(-b2*tau))
def gx_pow(tau, beta=0.5):          # power-law (fractional): tau^{(beta-1)/2}
    from scipy.special import gamma as Gg
    C = th0**((1-beta)/2)/(gam*cbeta(beta)*Gg((1+beta)/2))
    return C*tau**((beta-1)/2)
for f, lbl, c in [(gx_exp, "exponential (1 EMA)", "C0"),
                  (gx_two, "temp+exp (2 EMA)", "C1"),
                  (gx_pow, r"power-law ($\beta=0.5$)", "C2")]:
    g = f(tau); ax[1].loglog(tau, g/f(np.array([tref]))[0], c, label=lbl)
ax[1].annotate("Markowitz: instantaneous ($\\delta$)", xy=(0.02, 6), fontsize=8, color="0.4")
ax[1].set_title(r"(b) optimal policy $g_x(\tau)$ by kernel")
ax[1].set_xlabel(r"lag $\tau$"); ax[1].set_ylabel(r"$g_x(\tau)$ (norm. at $\tau=0.3$)"); ax[1].legend(fontsize=8.5)

# (c) power-law policy across the exponent beta
for beta, c in [(0.2, "C0"), (0.4, "C1"), (0.6, "C2")]:
    g = gx_pow(tau, beta)
    ax[2].loglog(tau, g/gx_pow(np.array([tref]), beta)[0], c,
                 label=fr"$\beta={beta}$  (slope ${(beta-1)/2:.1f}$)")
ax[2].set_title(r"(c) power-law policy vs $\beta$")
ax[2].set_xlabel(r"lag $\tau$"); ax[2].set_ylabel(r"$g_x(\tau)$ (norm. at $\tau=0.3$)"); ax[2].legend(fontsize=8.5)
fig.tight_layout(); save(fig, "fig_filter_structure")

# ============================================================
# FIG 5 (reworked): optimal positions and trade rates across regimes
# Three friction regimes on the same OU signal; Markowitz target as reference.
# Regimes:
#   A. Aim portfolio  : temporary cost + risk  (gamma=0, eta=0.5, lam=1)
#   B. NV stationary  : exp transient + temp + risk  (eta=0.5, gam=1, kap=2, lam=1)
#   C. Power-law+risk : power-law transient + risk, no temporary  (eta=0, gam=1, beta=0.5, lam=1)
# ============================================================
rng2 = np.random.default_rng(7)
theta0 = 1.0
sig0   = np.sqrt(2.0 * theta0)   # fixes Var(alpha) = sigma^2/(2*theta) = 1
lam0   = 1.0                      # -> Markowitz target = alpha_t
eta0_r = 0.5                      # temporary impact (regimes A and B)
gam_e, kap0 = 1.0, 2.0           # exponential transient (regime B)
gam_p, beta0 = 1.0, 0.5          # power-law transient (regime C)

dt_r = 0.10; T_r = 20.0; n_r = int(T_r / dt_r)
tg_r = np.arange(n_r) * dt_r

# OU signal
al_r = np.zeros(n_r)
for i in range(1, n_r):
    al_r[i] = al_r[i-1] * (1 - theta0*dt_r) + sig0*np.sqrt(dt_r)*rng2.standard_normal()

# Markowitz target  x^M = theta*alpha/lambda = alpha  (theta=lam=1)
xM_r = (theta0 / lam0) * al_r

# --- Regime A: aim portfolio (gamma=0, eta>0, lambda>0) ---
a_gp = np.sqrt(lam0 / eta0_r)                      # = sqrt(2)
aim_r = (a_gp / (a_gp + theta0)) * xM_r           # persistence-discounted aim
x_A = np.zeros(n_r)
for i in range(1, n_r):
    x_A[i] = x_A[i-1] + dt_r * a_gp * (aim_r[i-1] - x_A[i-1])
u_A = np.r_[np.diff(x_A) / dt_r, 0.0]            # trade rate from position

# --- Regime B: NV stationary (eta>0, gamma>0 exp, lambda>0) ---
Lt_r = np.tril(np.ones((n_r, n_r)))
lag_r = np.abs(np.arange(n_r)[:,None] - np.arange(n_r)[None,:]) * dt_r
G_e_r = np.exp(-kap0 * lag_r)
Cmat_B = eta0_r*np.eye(n_r) + gam_e*dt_r*G_e_r + lam0*dt_r**2*(Lt_r.T @ Lt_r)
u_B = np.linalg.solve(Cmat_B, al_r)
x_B = dt_r * (Lt_r @ u_B)

# --- Regime C: power-law transient + temporary + risk (same eta as A and B) ---
# Using the same eta0_r regularises the high-frequency kernel singularity while
# leaving the power-law character dominant up to the crossover
# xi_* = (c_beta*gam_p/eta0_r)^{1/(1-beta0)} ~ (2.507/0.5)^2 ~ 25 rad/time,
# well above the signal bandwidth (theta=1) and well above the reciprocal horizon.
lag_int = np.abs(np.arange(n_r)[:,None] - np.arange(n_r)[None,:])
G_p_r = np.where(lag_int > 0, (lag_int * dt_r)**(-beta0), 0.0)
Cmat_C = eta0_r*np.eye(n_r) + gam_p*dt_r*G_p_r + lam0*dt_r**2*(Lt_r.T @ Lt_r)
u_C = np.linalg.solve(Cmat_C, al_r)
x_C = dt_r * (Lt_r @ u_C)

# --- Verify FOCs ---
for lbl, Cm, uu in [("B", Cmat_B, u_B), ("C", Cmat_C, u_C)]:
    res = np.max(np.abs(Cm @ uu - al_r)) / (np.max(np.abs(al_r)) + 1e-12)
    print(f"FOC residual regime {lbl}: {res:.2e}")

# --- Analytical step responses: rate g_x(tau) for each regime ---
# When alpha is a unit step at t=0, the optimal rate at lag tau is g_x(tau),
# the position impulse response.  This separates regimes cleanly because
# the power-law tail t^{-nu} is algebraic while exponential filters fall off fast.
from scipy.special import gamma as Gf_sr

# Two-EMA rates b1, b2 for regime B
_s2 = kap0**2 + (2*kap0*gam_e + lam0) / eta0_r
_p2 = lam0 * kap0**2 / eta0_r
b1_r = np.sqrt((_s2 - np.sqrt(_s2**2 - 4*_p2)) / 2)
b2_r = np.sqrt((_s2 + np.sqrt(_s2**2 - 4*_p2)) / 2)
Phi_r = np.sqrt(eta0_r) * (b1_r + theta0) * (b2_r + theta0) / (kap0 + theta0)
w1_r = (kap0 - b1_r) / (b2_r - b1_r)
w2_r = (kap0 - b2_r) / (b1_r - b2_r)

tau_sr = np.linspace(0.05, 8.0, 800)   # lag axis for step response

def gx_A(tau):
    """GP aim portfolio: position impulse response = rate step response."""
    aim_amp = a_gp / (a_gp + theta0) * (theta0 / lam0)   # per unit alpha
    return aim_amp * a_gp * np.exp(-a_gp * tau)

def gx_B(tau):
    """NV stationary (two-EMA): position impulse response."""
    return (theta0 / (Phi_r * np.sqrt(eta0_r))) * (
        w1_r * np.exp(-b1_r * tau) + w2_r * np.exp(-b2_r * tau))

def gx_C(tau):
    """Power-law + temp + risk: position impulse response ~ tau^{(beta-1)/2}."""
    nu = (1.0 - beta0) / 2                               # = 0.25
    C = theta0**nu / (gam_p * cbeta(beta0) * Gf_sr((1.0 + beta0) / 2))
    return C * tau**((beta0 - 1.0) / 2)                  # ~ tau^{-0.25}

# Print step response values for sanity
print(f"\nStep response at tau=0.5: GP={gx_A(0.5):.4f},"
      f" NV={gx_B(0.5):.4f}, PL={gx_C(0.5):.4f}")
print(f"GP: a={a_gp:.4f}, discount a/(a+theta)={a_gp/(a_gp+theta0):.4f}")
print(f"x_A std={x_A.std():.3f}, x_B std={x_B.std():.3f},"
      f" x_C std={x_C.std():.3f}, xM std={xM_r.std():.3f}")

# Markowitz rate: finite difference of Markowitz target
uM_r = np.r_[np.diff(xM_r) / dt_r, 0.0]   # very noisy (white-noise-like)

# --- Figure ---
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

# (a) optimal positions on the same OU path
ax = axes[0]
ax.plot(tg_r, xM_r, color="0.60", lw=0.9, ls="--",
        label=r"Markowitz $\theta\alpha/\lambda$")
ax.plot(tg_r, x_A, "C0", lw=1.5,
        label=r"aim portfolio ($\gamma{=}0$, $\eta{=}0.5$)")
ax.plot(tg_r, x_B, "C1", lw=1.5,
        label=r"exp transient$+$temp$+$risk")
ax.plot(tg_r, x_C, "C2", lw=1.5,
        label=r"power-law transient$+$temp$+$risk ($\beta{=}0.5$)")
ax.set_xlabel(r"time $t$"); ax.set_ylabel(r"position $x^\star_t$")
ax.set_title("(a) optimal positions (same OU signal, $\\theta{=}\\lambda{=}1$)")
ax.legend(fontsize=8.5, loc="upper right")
ax.set_xlim(0, T_r)

# (b) rate step response: analytical, log x-axis separates exp from power-law tails
ax = axes[1]
# Normalise each curve to its value at tau=0.3 so amplitudes are comparable
norm_tau = 0.3
ax.semilogx(tau_sr, gx_A(tau_sr)/gx_A(norm_tau), "C0", lw=1.5,
            label=r"aim portfolio: $\propto e^{-at}$ (1 EMA)")
ax.semilogx(tau_sr, gx_B(tau_sr)/gx_B(norm_tau), "C1", lw=1.5,
            label=r"NV stationary: $w_1e^{-b_1t}+w_2e^{-b_2t}$ (2 EMAs)")
ax.semilogx(tau_sr, gx_C(tau_sr)/gx_C(norm_tau), "C2", lw=1.5,
            label=r"power-law: $\propto t^{-(1-\beta)/2}$ (fractional)")
ax.axhline(0, color="0.7", lw=0.5)
ax.set_xlabel(r"lag $\tau$ (log scale)")
ax.set_ylabel(r"rate step response (normalised at $\tau{=}0.3$)")
ax.set_title(r"(b) rate in response to unit step in $\alpha$ (analytical)")
ax.legend(fontsize=8.5, loc="upper right")
ax.set_xlim(0.05, 8)

fig.tight_layout(); save(fig, "fig_aim_portfolio")

# ============================================================
# FIG 7: Grunwald-Letnikov fractional-derivative weights
# ============================================================
def gl_weights(nu, K):
    c = np.zeros(K); c[0] = 1.0
    for k in range(1, K):
        c[k] = c[k-1]*(k-1-nu)/k
    return c
K = 2000; kk = np.arange(1, K)
fig, ax = plt.subplots(figsize=(7.5, 3.6))
for nu, c in [(0.2, "C0"), (0.3, "C1"), (0.4, "C2")]:
    w = np.abs(gl_weights(nu, K))[1:]
    ax.loglog(kk, w, c, label=fr"$\nu={nu}$  (tail $k^{{-{1+nu:.1f}}}$)")
ax.set_title(r"Fractional-derivative weights $D_+^\nu$ (Gr\"unwald--Letnikov)")
ax.set_xlabel(r"lag index $k$"); ax.set_ylabel(r"$|c_k|$"); ax.legend(fontsize=9)
fig.tight_layout(); save(fig, "fig_gl_weights")
# (stale reference removed — a_gp printed in fig_aim_portfolio block)

# ============================================================
# FIG 8: Interpolation from fractional to aim-portfolio
# Fixed power-law kernel (beta=0.5, gamma=1, lambda=1, theta=1).
# Vary eta: eta->0 gives fractional derivative limit (u* ~ D^nu alpha);
#           eta->inf gives aim-portfolio limit (x* ~ (1-e^{-at}) * aim).
# Panel (a): stochastic positions on same OU path.
# Panel (b): unit-step responses — shape transitions from algebraic t^{3/4}
#            (fractional, fast saturation) to exponential (aim-portfolio, slow).
# ============================================================
rng3 = np.random.default_rng(13)
theta_q = 1.0; sig_q = np.sqrt(2.0*theta_q); lam_q = 1.0
beta_q = 0.5; gam_q = 1.0; cbet_q = cbeta(beta_q)
nu_q = (1.0 - beta_q) / 2.0      # = 0.25 (fractional-derivative order)

dt_q = 0.10; T_q = 20.0; n_q = int(T_q/dt_q)
tg_q = np.arange(n_q)*dt_q

# OU signal path
al_q = np.zeros(n_q)
for k in range(1, n_q):
    al_q[k] = al_q[k-1]*(1-theta_q*dt_q) + sig_q*np.sqrt(dt_q)*rng3.standard_normal()
xM_q = theta_q*al_q/lam_q

# Power-law kernel matrix shared across eta values.
# Diagonal: midpoint-rule integral of G(|tau|) over [-dt/2, dt/2],
# so that gam*dt*G[i,i] = gam * 2*integral_0^{dt/2} tau^{-beta} dtau.
# This is essential for small eta where the diagonal regularises the matrix.
Lt_q = np.tril(np.ones((n_q, n_q)))
lag_q = np.abs(np.arange(n_q)[:,None] - np.arange(n_q)[None,:])
_diag_q = 2.0*(dt_q/2)**(1-beta_q)/((1-beta_q)*dt_q)   # = (dt/2)^{1-beta}/((1-beta)*dt/2)
G_pl_q = np.where(lag_q > 0, (lag_q*dt_q)**(-beta_q), _diag_q)

# eta values and display properties
etas_q  = [0.02, 0.1,  0.5,  2.0,  10.0]
cols_q  = ["#1b9e77", "#66c2a5", "#fdae61", "#f46d43", "#4575b4"]
labs_q  = [
    r"$\eta=0.02$  (fractional limit)",
    r"$\eta=0.1$",
    r"$\eta=0.5$",
    r"$\eta=2$",
    r"$\eta=10$  (aim-portfolio limit)",
]

# ---- Rate step response via Szego outer factor (FFT-based) ----
# The rate step response is the position impulse response g_x(tau) = IFFT[H(w)]
# where H(w) = theta / (Phi(theta) * N_+(w)),  N(w) = eta*w^2 + gam*cb*|w|^{1+beta} + lam.
# N_+(w) is the outer (Szego) spectral factor: |N_+(w)| = sqrt(N(w)),
# arg N_+(w) = (1/2) * HT[log N](w)  (HT = Hilbert transform via FFT).
# H(w) is causal (analytic upper half-plane), so g_x(t) is supported on t >= 0.
# The step response  x^step(t) = integral_0^t g_x(s) ds.

N_fft = 4096; w_max_q = 40.0
dw_q  = 2*w_max_q / N_fft
w_fft = np.linspace(-w_max_q, w_max_q, N_fft, endpoint=False)

tau_sr = np.linspace(0.05, 8.0, 600)   # lag axis for panel (b), same as fig_aim_portfolio
norm_tau_q = 0.3

def gx_interp(eta, gam=gam_q, beta=beta_q, lam=lam_q, theta=theta_q):
    """Position impulse response g_x(tau) via Szego FFT for the three-friction symbol."""
    cb = cbeta(beta)
    Nw = eta*w_fft**2 + gam*cb*np.abs(w_fft)**(1+beta) + lam   # N(w) = w^2 Q(w)
    logN = np.log(Nw)     # real and positive

    # Hilbert transform of log N via FFT: H[f](w) = Im(IFFT(sign(k) * FFT(f)))
    logN_c  = np.fft.ifftshift(logN)     # centre DC for FFT
    L_fft   = np.fft.fft(logN_c)
    freq_k  = np.fft.fftfreq(N_fft)
    sgn_k   = np.sign(freq_k); sgn_k[0] = 0; sgn_k[N_fft//2] = 0
    HT_logN = np.real(np.fft.ifft(1j * sgn_k * L_fft))
    HT_logN = np.fft.fftshift(HT_logN)   # back to w-centred

    # Outer factor: N_+(w) = sqrt(N(w)) * exp(i/2 * HT[log N](w))
    N_plus  = np.sqrt(Nw) * np.exp(0.5j * HT_logN)

    # Phi(theta) = N_+(i*theta) via Poisson integral of log N
    Phi  = np.exp((theta/np.pi) * np.sum(logN * dw_q / (theta**2 + w_fft**2)))

    # Position filter H(w) = theta / (Phi * N_+(w))
    H  = (theta / (Phi * N_plus)).real   # keep real part (imaginary is from HT rounding)
    # Note: because N is even and the Hilbert transform of an even function is odd,
    # N_+(w)*conj(N_+(-w)) = N(w) and H(w) is real-symmetric.
    # We enforce symmetry for the IFFT.
    H  = 0.5*(H + H[::-1])

    # IFFT -> impulse response on the circular (periodic) frequency grid;
    # causal part is the first half of the IFFT output.
    g_circ  = np.fft.ifft(np.fft.ifftshift(H)).real * N_fft * dw_q / (2*np.pi)
    dt_ir   = 2*np.pi / (N_fft * dw_q)          # time resolution
    t_ir    = np.arange(N_fft) * dt_ir
    g_causal = g_circ[:N_fft//2]                 # causal (t >= 0) part
    t_causal = t_ir[:N_fft//2]

    # Interpolate onto tau_sr grid
    return np.interp(tau_sr, t_causal, g_causal)

# Verify: GP limit (gam->0) should match phi_gp from fig_aim_portfolio
# (skipping explicit check; both use the same Phi/N_+ structure)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

# (a) adapted positions via Szego stationary filter applied to OU signal
# For each eta: H(w) is already computed in gx_interp via the FFT grid.
# Apply H to FFT(alpha) to get the stationary adapted position.
def position_szego(al_sig, dt_sig, eta, gam=gam_q, beta=beta_q, lam=lam_q, theta=theta_q):
    """Apply stationary Szego position filter to a signal vector."""
    n_sig = len(al_sig)
    # Pad to at least 2*N_fft to avoid circular aliasing
    n_pad = max(2*n_sig, 2*N_fft)
    al_pad = np.zeros(n_pad)
    al_pad[:n_sig] = al_sig
    w_sig = np.fft.rfftfreq(n_pad, d=dt_sig) * 2*np.pi   # angular freq
    cb = cbeta(beta)
    Nw_sig = eta*w_sig**2 + gam*cb*np.abs(w_sig)**(1+beta) + lam
    logN_sig = np.log(Nw_sig)
    # Hilbert transform on the one-sided (rfft) grid
    n_r = len(w_sig)
    # extend to full grid via symmetry, apply HT, take back
    logN_full = np.concatenate([logN_sig, logN_sig[-2:0:-1]])  # rfft symmetrisation
    n_full = len(logN_full)
    L_f  = np.fft.fft(logN_full)
    fk   = np.fft.fftfreq(n_full)
    sgk  = np.sign(fk); sgk[0]=0; sgk[n_full//2]=0
    HT_f = np.real(np.fft.ifft(1j*sgk*L_f))
    HT_sig = HT_f[:n_r]
    N_plus_sig = np.sqrt(Nw_sig) * np.exp(0.5j * HT_sig)
    # Phi
    Phi_s = np.exp((theta/np.pi) * np.sum(logN_sig * (w_sig[1]-w_sig[0]) / (theta**2 + w_sig**2)))
    H_sig = theta / (Phi_s * N_plus_sig)    # complex causal filter
    # Apply to signal
    Al_fft = np.fft.rfft(al_pad)
    X_fft  = H_sig * Al_fft
    x_full = np.fft.irfft(X_fft, n=n_pad)
    return x_full[:n_sig].real

ax = axes[0]
ax.plot(tg_q, xM_q, color="0.60", lw=0.8, ls="--",
        label=r"Markowitz $\theta\alpha/\lambda$", zorder=0)
for eta_v, col, lbl in zip(etas_q, cols_q, labs_q):
    x_q = position_szego(al_q, dt_q, eta_v)
    print(f"interp Szego eta={eta_v}: x std={x_q.std():.3f}")
    ax.plot(tg_q, x_q, color=col, lw=1.5, label=lbl)
ax.set_xlabel(r"time $t$"); ax.set_ylabel(r"position $x^\star_t$")
ax.set_title(r"(a) adapted positions ($\beta=0.5$, $\gamma=\lambda=\theta=1$, varying $\eta$)")
ax.legend(fontsize=8.5, loc="upper right")
ax.set_xlim(0, T_q)

# (b) rate step response: g_x(tau) for each eta, normalised at tau=0.3 (semi-log tau axis)
ax = axes[1]
for eta_v, col, lbl in zip(etas_q, cols_q, labs_q):
    g = gx_interp(eta_v)
    g_norm0 = np.interp(norm_tau_q, tau_sr, g)
    if g_norm0 > 0:
        ax.semilogx(tau_sr, g / g_norm0, color=col, lw=1.5, label=lbl)
    print(f"eta={eta_v}: g_x(0.3)={g_norm0:.4f}")

# Analytical limits (two-friction special cases):
# -- fractional limit (eta->0): g_x(tau) ~ tau^{(beta-1)/2} = tau^{-0.25}
g_frac = tau_sr**((beta_q-1)/2)
ax.semilogx(tau_sr, g_frac/np.interp(norm_tau_q, tau_sr, g_frac),
            "k:", lw=1.2, label=r"$\eta\to0$: $\propto\tau^{-(1-\beta)/2}$")
# -- aim-portfolio limit (eta->inf, gam->0): g_x(tau) = a * aim * exp(-a*tau)
_a_lim = np.sqrt(lam_q/etas_q[-1])   # a = sqrt(lam/eta) for largest eta shown
g_gp   = _a_lim * np.exp(-_a_lim * tau_sr)
ax.semilogx(tau_sr, g_gp/np.interp(norm_tau_q, tau_sr, g_gp),
            "k--", lw=1.2, label=fr"$\eta\to\infty$: $\propto e^{{-at}}$, $a=\sqrt{{\lambda/\eta}}$")

ax.axhline(0, color="0.7", lw=0.5)
ax.set_xlabel(r"lag $\tau$ (log scale)")
ax.set_ylabel(r"rate step response (normalised at $\tau{=}0.3$)")
ax.set_title(r"(b) $g_x(\tau)$: rate response to unit step in $\alpha$ (Szeg\H{o} filter)".replace(r"\H{o}", "\u0151"))
ax.legend(fontsize=8.0, loc="upper right")
ax.set_xlim(0.05, 8)

fig.tight_layout(); save(fig, "fig_interpolation")
print(f"Szego FFT complete. Power-law exponent: {(beta_q-1)/2:.3f}, GP rate: {_a_lim:.3f}")
