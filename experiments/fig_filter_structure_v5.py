"""fig_filter_structure (v5): the rational friction family only, at ONE consistent
friction setting.  No pure-impact (eta=lambda=0) curves, no power-law -- those live
in fig_transfer_impulse.  All curves share eta=0.5, lambda=1, theta=1; only the
transient weight gamma changes across the family.

Panels:
 (a) the two moving-average rates b1,b2 of the full rational friction
     (eta=0.5, gamma=1, kappa=2) as risk aversion lambda varies.
 (b) the lag-domain position impulse response g_x(tau) across the rational family
     at fixed eta=0.5, lambda=1: Markowitz (0 EMA, a spike), aim portfolio
     (gamma=0, 1 EMA), and two-average (gamma=1, exponential resilience, 2 EMAs).

All formulas are the validated ones (RESULTS.md R5, R16).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "v5", "figures")
os.makedirs(OUT, exist_ok=True)
os.environ["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "text.usetex": True, "font.family": "serif",
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"})

# fixed friction family: temporary cost eta, exponential resilience kappa, risk lambda
eta0, gam0, kap0, th0 = 0.5, 1.0, 2.0, 1.0

def roots(lam, eta=eta0, gam=gam0, kap=kap0):
    """two-EMA rates b1<b2 of the full rational symbol (R16d)."""
    s2 = kap**2 + (2*kap*gam + lam)/eta
    p2 = lam*kap**2/eta
    b1 = np.sqrt((s2 - np.sqrt(s2**2 - 4*p2))/2)
    b2 = np.sqrt((s2 + np.sqrt(s2**2 - 4*p2))/2)
    return b1, b2

fig, ax = plt.subplots(1, 2, figsize=(9.6, 4.1))

# ---- (a) two-EMA rates vs risk aversion (full friction) ----
lams = np.logspace(-2, 1.3, 300)
B1 = np.array([roots(l)[0] for l in lams])
B2 = np.array([roots(l)[1] for l in lams])
ax[0].loglog(lams, B1, "C0", lw=1.9, label=r"$b_1$ (slow)")
ax[0].loglog(lams, B2, "C1", lw=1.9, label=r"$b_2$ (fast)")
ax[0].axhline(kap0, color="grey", ls=":", lw=0.9)
ax[0].text(0.011, kap0*1.08, r"$\kappa$ (resilience)", fontsize=8.5)
ax[0].set_title(r"(a) the two moving-average rates vs risk")
ax[0].set_xlabel(r"risk aversion $\lambda$")
ax[0].set_ylabel(r"rate $b_i$")
ax[0].legend(fontsize=9.5, loc="lower right")

# ---- (b) lag-domain policy g_x(tau) across the rational family (eta=0.5, lam=1) ----
lam0 = 1.0
tau = np.logspace(-1.6, 1.05, 500)
tref = 0.3

# aim portfolio: gamma=0, one EMA at rate a=sqrt(lam/eta) (R16b)
a_gp = np.sqrt(lam0/eta0)
aim_amp = a_gp/(a_gp + th0) * (th0/lam0)
def gx_aim(t):
    return aim_amp * a_gp * np.exp(-a_gp*t)

# two-average: gamma=1, exponential resilience, two EMAs (R16d)
b1, b2 = roots(lam0)
Phi = np.sqrt(eta0)*(b1 + th0)*(b2 + th0)/(kap0 + th0)
w1 = (kap0 - b1)/(b2 - b1)
w2 = (kap0 - b2)/(b1 - b2)
def gx_two(t):
    return (th0/(Phi*np.sqrt(eta0)))*(w1*np.exp(-b1*t) + w2*np.exp(-b2*t))

ax[1].semilogx(tau, gx_aim(tau)/gx_aim(tref), "C0", lw=1.9,
               label=r"aim portfolio ($\gamma{=}0$): 1 EMA")
ax[1].semilogx(tau, gx_two(tau)/gx_two(tref), "C1", lw=1.9,
               label=r"temporary $+$ resilience ($\gamma{=}1$): 2 EMAs")
# Markowitz: eta=gamma=0 gives an instantaneous response (a spike at tau=0)
ax[1].annotate(r"Markowitz ($\eta{=}\gamma{=}0$): spike at $\tau{=}0$",
               xy=(tau[0], gx_aim(tau[0])/gx_aim(tref)), xytext=(0.03, 2.4),
               fontsize=8.5, color="0.35",
               arrowprops=dict(arrowstyle="->", color="0.5", lw=0.7))
ax[1].axhline(0, color="0.7", lw=0.5)
ax[1].set_title(r"(b) policy $g_x(\tau)$ across the rational family")
ax[1].set_xlabel(r"lag $\tau$ (log scale)")
ax[1].set_ylabel(r"$g_x(\tau)$ (normalized at $\tau{=}0.3$)")
ax[1].legend(fontsize=9.0, loc="upper right")
ax[1].set_xlim(tau[0], tau[-1])

fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig_filter_structure.png"))
fig.savefig(os.path.join(OUT, "fig_filter_structure.pdf"))
print("wrote fig_filter_structure (v5, rational family only)")
print(f"eta={eta0} gam={gam0} kap={kap0} lam={lam0}: b1={b1:.4f} b2={b2:.4f} "
      f"Phi={Phi:.4f} a_gp={a_gp:.4f} w1={w1:.4f} w2={w2:.4f}")
