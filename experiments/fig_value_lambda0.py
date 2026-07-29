"""
Exploratory: the value-vs-speed figure at lambda = 0 (no inventory risk, pure
execution / impact regime).  Same construction as fig_value panel (a), Var(mu)=1,
v = 1/(2 Phi^2), Phi = Szego factor of n(w) = eta w^2 + gam*g_hat*w^2  (lambda=0).

At lambda=0 the friction symbol vanishes at w=0, so the position is non-stationary
(Section 3), but the value RATE v is finite.  There is no speed-free pure-risk
baseline (v_risk = 1/2 lambda -> infinity), so it is dropped.

Scalings at lambda=0:
  power-law (eta=0)       : n ~ gam c_beta |w|^{1+beta}   -> Phi ~ theta^{(1+beta)/2}, v ~ theta^{-(1+beta)}  (exact, scale-free)
  power-law + temp (eta>0): low theta ~ theta^{-(1+beta)}, high theta ~ theta^{-2} (temp cost takes over)
  exp (eta=0)             : n ~ (2 gam/kap) w^2 near 0, -> theta^{-2} at low theta, bounded floor 1/(4 gam kap) at high theta
  exp + temp (eta>0)      : ~ theta^{-2} throughout (n ~ c w^2 at both ends)
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as Gf
from scipy.integrate import quad
import os

os.makedirs("figures", exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight"})

def cbeta(b): return 2*Gf(1-b)*np.sin(np.pi*b/2)
gam, kap, beta, eta, lam = 1.0, 2.0, 0.5, 0.5, 0.0     # lambda = 0

def n_exp(eta): return lambda w: eta*w**2 + 2*gam*kap*w**2/(kap**2+w**2) + lam
def n_pow(eta): return lambda w: eta*w**2 + gam*cbeta(beta)*np.abs(w)**(1+beta) + lam
def Phi(theta, nf):
    val, _ = quad(lambda t: np.log(nf(t))/(theta**2+t**2), 0, np.inf, limit=500)
    return np.exp(theta/np.pi*val)
def v_of(nf, th): return np.array([2.0/(4*Phi(t, nf)**2) for t in th])   # v = 1/(2 Phi^2)

th = np.logspace(-1.2, 1.5, 300)
v_et = v_of(n_exp(eta), th); v_pt = v_of(n_pow(eta), th)     # + temporary cost (solid)
v_e0 = v_of(n_exp(0.0), th); v_p0 = v_of(n_pow(0.0), th)     # eta=0 (dotted)
def nrm(v): return v/np.interp(1.0, th, v)

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))

# (a) value vs speed, lambda = 0
ax[0].loglog(th, nrm(v_et), "C0", lw=2.0, label=r"exp + temp")
ax[0].loglog(th, nrm(v_pt), "C3", lw=2.0, label=r"power-law + temp")
ax[0].loglog(th, nrm(v_e0), "C0", ls=":", lw=1.5, alpha=0.7, label=r"exp ($\eta{=}0$)")
ax[0].loglog(th, nrm(v_p0), "C3", ls=":", lw=1.5, alpha=0.7, label=r"power-law ($\eta{=}0$, pure)")
g = np.logspace(0.55, 1.45, 30)
ax[0].loglog(g, 0.45*g**(-2.0), "0.5", lw=0.8, ls=":")
ax[0].text(g[-1]*1.03, 0.45*g[-1]**(-2.0), r"$\propto\theta^{-2}$", fontsize=9, color="0.4")
ax[0].loglog(g, 0.9*g**(-(1+beta)), "0.5", lw=0.8, ls=":")
ax[0].text(g[-1]*1.03, 0.9*g[-1]**(-(1+beta)), r"$\propto\theta^{-(1+\beta)}$", fontsize=9, color="0.4")
ax[0].set_title(r"(a) value vs signal speed, $\lambda=0$ (no inventory risk)")
ax[0].set_xlabel(r"signal speed $\theta$"); ax[0].set_ylabel(r"$v(\theta)/v(1)$")
ax[0].legend(fontsize=8.2, loc="lower left")

# (b) causality gap (lambda-independent: this is the pure power-law result)
b = np.linspace(0.001, 0.999, 400)
ax[1].plot(b, np.sin(np.pi*b/2), "C3")
ax[1].axvspan(0.2, 0.6, color="grey", alpha=0.12); ax[1].text(0.24, 0.2, "empirical\n$\\beta$", fontsize=8)
ax[1].set_title(r"(b) cost of causality: $v/v_{\rm ant}=\sin(\pi\beta/2)$")
ax[1].set_xlabel(r"$\beta$"); ax[1].set_ylabel(r"$v/v_{\rm ant}$"); ax[1].set_ylim(0, 1.02)

fig.tight_layout()
fig.savefig("figures/fig_value_lambda0.png"); fig.savefig("figures/fig_value_lambda0.pdf")
print("wrote figures/fig_value_lambda0.png")
# report high-theta slopes
def slope(v): m = th > 6; return np.polyfit(np.log(th[m]), np.log(v[m]), 1)[0]
def slope_lo(v): m = th < 0.4; return np.polyfit(np.log(th[m]), np.log(v[m]), 1)[0]
for lbl, v in [("exp+temp", v_et), ("pow+temp", v_pt), ("exp eta0", v_e0), ("pow eta0", v_p0)]:
    print(f"  {lbl:10s}  low-theta slope={slope_lo(v):+.2f}   high-theta slope={slope(v):+.2f}")
