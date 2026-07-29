"""
fig_speed_position.py  --  new figure for v3.

Illustrates the DIFFERENT behaviour of two friction families on the optimal
ADAPTED position, across OU signal speeds theta:

    exponential + risk + instantaneous   :  N(w) = eta w^2 + 2*gam*kap*w^2/(kap^2+w^2) + lam
    power-law   + risk + instantaneous   :  N(w) = eta w^2 + gam*c_beta*|w|^{1+beta}    + lam

Both carry the same temporary (instantaneous) cost eta and inventory risk lam.
The only difference is the transient-impact kernel: exponential (finite memory,
single scale 1/kappa) versus power law (scale-free, long memory).

Method (validated machinery, from risk_response_check.py / test_all_results.py):
  - discrete friction quadratic form   C = eta I + gam dt G + lam dt^2 L^T L
  - adapted (causal) solution operator  W = solve_W(C, theta, dt)  via the
    reverse-order (UL) Cholesky factorization that imposes E_i[(Cu)_i] = alpha_i;
  - position operator  Wx = dt L W ;  adapted position path  x = Wx @ alpha.
The signal is a genuine OU(theta) path.  Because the position responds to the
RETURN mu = theta*alpha (Markowitz x = mu/lambda), the natural scale fixes the
return variance Var(mu)=1 (so Var(alpha)=1/theta^2).  The Markowitz reference
x = mu/lambda is then the SAME amplitude at every speed, and the friction
positions are its smoothed, shrunken images.  Speeds share one Brownian driver,
so the panels show the SAME return news at different persistence.

No fabricated data: every position path is the adapted optimum of the discrete
problem, and the interior (boundary layers trimmed) is the stationary response.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as Gfun
import os, shutil

os.makedirs("figures", exist_ok=True)
os.environ["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "text.usetex": True, "font.family": "serif",
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"})

def cbeta(b):
    return 2 * Gfun(1 - b) * np.sin(np.pi * b / 2)

# ---- validated adapted (causal) solver, copied verbatim from risk_response_check.py ----
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

def friction_matrix(n, dt, gam, lam, eta, kernel):
    idx = np.arange(n)
    lag = np.abs(idx[:, None] - idx[None, :]) * dt
    if kernel[0] == "exp":
        kap = kernel[1]
        G = np.exp(-kap * lag)
    elif kernel[0] == "pow":
        beta = kernel[1]
        # regularized diagonal (finite midpoint-rule value), off-diagonal |lag|^{-beta}
        G = np.where(lag == 0.0,
                     2 * dt ** (-beta) / ((1 - beta) * (2 - beta)),
                     np.where(lag == 0.0, 1.0, lag) ** (-beta))
    else:
        G = np.zeros((n, n))
    Lt = np.tril(np.ones((n, n)))
    C = eta * np.eye(n) + gam * dt * G + lam * dt ** 2 * (Lt.T @ Lt)
    return C, Lt

def position_operator(n, dt, theta, gam, lam, eta, kernel):
    C, Lt = friction_matrix(n, dt, gam, lam, eta, kernel)
    W = solve_W(C, theta, dt)
    return dt * (Lt @ W)          # Wx: maps signal path -> adapted position path

def ou_path(dW, dt, theta):
    """OU(theta) with Var(alpha)=1: sigma^2 = 2 theta. Shares the driver dW."""
    n = len(dW)
    sig = np.sqrt(2.0 * theta)
    a = np.zeros(n)
    for i in range(1, n):
        a[i] = a[i - 1] * (1 - theta * dt) + sig * np.sqrt(dt) * dW[i]
    return a

# ---------------------------------------------------------------------------
#  parameters (paper's canonical set)
# ---------------------------------------------------------------------------
gam, kap, beta, lam, eta = 1.0, 2.0, 0.5, 1.0, 0.5
speeds = [0.5, 2.0, 6.0]          # slow (<kappa), medium (=kappa), fast (>kappa)
n, dt = 700, 0.05                 # T = 35
T = n * dt
tg = np.arange(n) * dt

rng = np.random.default_rng(3)
# common Brownian driver with burn-in so all speeds start stationary
dW = rng.standard_normal(n)

# analytic position response X(theta) = theta / Phi(theta)^2  (for annotation/sanity)
def Phi_exp(th):
    A = 2 * kap * gam + lam
    s2 = kap ** 2 + A / eta; p2 = lam * kap ** 2 / eta
    b1 = np.sqrt((s2 - np.sqrt(s2 ** 2 - 4 * p2)) / 2)
    b2 = np.sqrt((s2 + np.sqrt(s2 ** 2 - 4 * p2)) / 2)
    return np.sqrt(eta) * (b1 + th) * (b2 + th) / (kap + th)
def Phi_pow(th):
    from scipy import integrate
    cb = cbeta(beta)
    N = lambda t: eta * t ** 2 + gam * cb * np.abs(t) ** (1 + beta) + lam
    f = lambda t: np.log(N(t)) / (th ** 2 + t ** 2)
    val, _ = integrate.quad(f, 0, np.inf, limit=400)
    return np.exp(th / np.pi * val)

# trim boundary layers: keep interior window
i0, i1 = int(0.28 * n), int(0.80 * n)

sl = slice(i0, i1)
fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.0), sharex=True, sharey=True)
for ax, th in zip(axes, speeds):
    al_raw = ou_path(dW, dt, th)     # Var(alpha)=1
    alpha = al_raw / th              # fix Var(mu)=1  ->  Var(alpha)=1/theta^2
    mu = th * alpha                  # = al_raw, Var(mu)=1
    xM = mu / lam                    # Markowitz (frictionless) position, constant amplitude
    Wx_e = position_operator(n, dt, th, gam, lam, eta, ("exp", kap))
    Wx_p = position_operator(n, dt, th, gam, lam, eta, ("pow", beta))
    x_e = Wx_e @ alpha
    x_p = Wx_p @ alpha

    fe = x_e[sl].std() / xM[sl].std()   # fraction of the frictionless position held
    fp = x_p[sl].std() / xM[sl].std()
    print(f"theta={th}: held-fraction exp={fe:.3f} pow={fp:.3f}  "
          f"| std xM={xM[sl].std():.3f} x_exp={x_e[sl].std():.3f} x_pow={x_p[sl].std():.3f}")

    ax.plot(tg[sl], xM[sl],  color="0.62", lw=0.8, ls="--", alpha=0.6, zorder=0,
            label=r"Markowitz $x=\mu/\lambda$")
    ax.plot(tg[sl], x_e[sl], "C0", lw=1.7, label="exp $+$ risk $+$ instant.")
    ax.plot(tg[sl], x_p[sl], "C3", lw=1.7, label="power-law $+$ risk $+$ instant.")
    ax.set_title(fr"$\theta={th:g}$" + ("  (slow, $\\theta<\\kappa$)" if th < kap
                 else "  (fast, $\\theta>\\kappa$)" if th > kap else "  ($\\theta=\\kappa$)"))
    ax.set_xlabel(r"time $t$")
    ax.text(0.03, 0.035, fr"held: exp ${fe:.2f}$, p-law ${fp:.2f}$",
            transform=ax.transAxes, fontsize=8.2, color="0.35")

axes[0].set_ylabel(r"adapted position $x^\star_t$")
axes[0].legend(fontsize=8.2, loc="upper left")
fig.tight_layout()
fig.savefig("figures/fig_speed_position.png")
fig.savefig("figures/fig_speed_position.pdf")
print("wrote figures/fig_speed_position.png")

# copy to arxiv/figures
for ext in ("png", "pdf"):
    shutil.copy(f"figures/fig_speed_position.{ext}", f"arxiv/figures/fig_speed_position.{ext}")
print("copied to arxiv/figures/")
