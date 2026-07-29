"""
fig_position_scaling.py -- position scaling vs OU speed theta, exp vs power-law.

(a) position response  X(theta) = theta/Phi(theta)^2   (position gain per unit alpha)
(b) position size at fixed return variance  Var(mu)=1:  std(x) = sqrt(J)/Phi,
    J(theta) = (1/2pi) int 2 theta/((theta^2+w^2) n(w)) dw,  Var(x)=J/Phi^2.

Kernels (position-referred symbol n):
  exp : n = eta w^2 + 2 gam kap w^2/(kap^2+w^2) + lam
  pow : n = eta w^2 + gam c_beta |w|^{1+beta}    + lam
Four curves: {exp, power-law} x {no temp (eta=0), temp (eta>0)}.

Findings (see explore_position_scaling.py):
  eta=0 : X_exp ~ theta^{+1} (grows),  X_pow ~ theta^{-beta} (throttled).
  eta>0 : both X ~ theta^{-1} (temporary cost 1/(eta theta) dominates).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as Gf
from scipy import integrate
import os, shutil

os.makedirs("figures", exist_ok=True)
os.environ["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "text.usetex": True, "font.family": "serif",
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"})

def cbeta(b): return 2*Gf(1-b)*np.sin(np.pi*b/2)
def n_exp(w, gam, kap, lam, eta): return eta*w**2 + 2*gam*kap*w**2/(kap**2+w**2) + lam
def n_pow(w, gam, beta, lam, eta): return eta*w**2 + gam*cbeta(beta)*np.abs(w)**(1+beta) + lam

def Phi(theta, nfun):
    val, _ = integrate.quad(lambda t: np.log(nfun(t))/(theta**2+t**2), 0, np.inf, limit=400)
    return np.exp(theta/np.pi*val)
def Jint(theta, nfun):
    val, _ = integrate.quad(lambda w: 2*theta/((theta**2+w**2)*nfun(w)), 0, np.inf, limit=400)
    return val/np.pi

gam, kap, beta, lam, eta = 1.0, 2.0, 0.5, 1.0, 0.5
th = np.logspace(-1, 1.8, 160)

# realistic (temporary cost) drawn solid; eta=0 idealization drawn dotted/faded
configs = [
    (r"exp + temp + risk",              lambda w: n_exp(w, gam, kap, lam, eta),  "C0", "-"),
    (r"power-law + temp + risk",        lambda w: n_pow(w, gam, beta, lam, eta), "C3", "-"),
    (r"exp + risk ($\eta{=}0$)",        lambda w: n_exp(w, gam, kap, lam, 0.0),  "C0", ":"),
    (r"power-law + risk ($\eta{=}0$)",  lambda w: n_pow(w, gam, beta, lam, 0.0), "C3", ":"),
]
def style(ls): return (2.1, 1.0) if ls == "-" else (1.5, 0.7)   # (lw, alpha)

X = {}; S = {}
for lbl, nf, c, ls in configs:
    Ph = np.array([Phi(t, nf) for t in th])
    X[lbl] = th/Ph**2
    S[lbl] = np.array([np.sqrt(Jint(t, nf)) for t in th])/Ph

fig, ax = plt.subplots(1, 2, figsize=(11.2, 4.3))

# (a) position response X(theta) = theta/Phi^2
for lbl, nf, c, ls in configs:
    lw, al = style(ls)
    ax[0].loglog(th, X[lbl], c, ls=ls, lw=lw, alpha=al, label=lbl)
# slope guides (short segments beside the relevant tails)
g = np.logspace(1.0, 1.75, 30)
ax[0].loglog(g, 0.30*g,           "0.5", lw=0.8, ls=":")
ax[0].text(g[-1]*1.03, 0.30*g[-1], r"$\propto\theta$", fontsize=9, color="0.4")
ax[0].loglog(g, 0.30*g**(-beta),  "0.5", lw=0.8, ls=":")
ax[0].text(g[-1]*1.03, 0.30*g[-1]**(-beta), r"$\propto\theta^{-\beta}$", fontsize=9, color="0.4")
ax[0].loglog(g, 0.9*g**(-1.0),    "0.5", lw=0.8, ls=":")
ax[0].text(g[-1]*1.03, 0.9*g[-1]**(-1.0), r"$\propto\theta^{-1}$", fontsize=9, color="0.4")
ax[0].set_title(r"(a) position response $X(\theta)=\theta/\Phi(\theta)^2$")
ax[0].set_xlabel(r"signal speed $\theta$"); ax[0].set_ylabel(r"$X(\theta)$")
ax[0].legend(fontsize=8.4, loc="lower left")

# (b) position size at fixed Var(mu)=1
for lbl, nf, c, ls in configs:
    lw, al = style(ls)
    ax[1].loglog(th, S[lbl], c, ls=ls, lw=lw, alpha=al, label=lbl)
ax[1].axhline(1.0/lam, color="0.5", lw=0.8, ls=":")
ax[1].text(th[0]*1.05, 1.0/lam*1.05, r"Markowitz $1/\lambda$", fontsize=8.5, color="0.4")
# the exp+risk floor exists ONLY at eta=0; any temporary cost sends every kernel to zero
floor = 1.0/(2*gam*kap+lam)
ax[1].axhline(floor, color="C0", lw=0.7, ls=":")
ax[1].annotate(r"$\dfrac{1}{2\kappa\gamma+\lambda}$: floor only at $\eta=0$",
               xy=(th[-1], floor), xytext=(1.4, 0.30), fontsize=8.0, color="C0",
               arrowprops=dict(arrowstyle="->", color="C0", lw=0.7))
ax[1].text(3.2, 0.005, r"any $\eta>0:\ \Phi\sim\sqrt{\eta}\,\theta,\ \mathrm{std}(x^\star)\to0$",
           fontsize=8.0, color="0.35")
ax[1].set_title(r"(b) position size $\mathrm{std}(x^\star)$ at fixed $\mathrm{Var}(\mu)=1$")
ax[1].set_xlabel(r"signal speed $\theta$"); ax[1].set_ylabel(r"$\mathrm{std}(x^\star)$")
ax[1].legend(fontsize=8.4, loc="lower left")

fig.tight_layout()
fig.savefig("figures/fig_position_scaling.png"); fig.savefig("figures/fig_position_scaling.pdf")
print("wrote figures/fig_position_scaling.png")
for ext in ("png", "pdf"):
    shutil.copy(f"figures/fig_position_scaling.{ext}", f"v3/figures/fig_position_scaling.{ext}")
# print slopes for the record
def slope(y): return np.polyfit(np.log(th[th>6]), np.log(y[th>6]), 1)[0]
for lbl, *_ in configs:
    print(f"  {lbl:26s}  X slope={slope(X[lbl]):+.2f}   std slope={slope(S[lbl]):+.2f}")
