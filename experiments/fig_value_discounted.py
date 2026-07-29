"""
Value vs signal speed with a DISCOUNTED predictor (regularizes alpha = E_t int_t^inf mu).

Signal:  alpha^rho_t = E_t int_t^inf e^{-rho(s-t)} mu_s ds = mu_t/(rho+theta)   (OU).
Value at fixed return variance Var(mu)=1:  v^rho(theta) = theta^2 / (2 Phi(theta)^2 (rho+theta)^2).

Frictions (no inventory risk, lambda=0; the discount alone regularizes):
  temporary cost eta >= 0  and a transient-impact kernel (exponential or power law).
  n(w) = eta w^2 + gam * g_hat(w) * w^2,   g_hat_exp = 2kap/(kap^2+w^2),  g_hat_pow = c_beta|w|^{beta-1}.

Pure power law:  v^rho = theta^{1-beta}/(2 gam c_beta (rho+theta)^2), hump at theta* = rho(1-beta)/(1+beta),
  v->0 as theta->0 (constant signal: D^nu of a constant is zero) and as theta->inf.
Exponential kernels do NOT vanish at theta->0: a constant signal is traded to a nonzero position.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as Gf
from scipy.integrate import quad
import os

os.makedirs("figures", exist_ok=True)
os.environ["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "text.usetex": True, "font.family": "serif",
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"})

def cbeta(b): return 2*Gf(1-b)*np.sin(np.pi*b/2)
gam, kap, beta, eta, rho = 1.0, 2.0, 0.5, 0.5, 1.0     # lambda = 0

def n_pow(e): return lambda w: e*w**2 + gam*cbeta(beta)*np.abs(w)**(1+beta)
def n_exp(e): return lambda w: e*w**2 + 2*gam*kap*w**2/(kap**2+w**2)
def Phi(th, nf):
    val, _ = quad(lambda t: np.log(nf(t))/(th**2+t**2), 0, np.inf, limit=400)
    return np.exp(th/np.pi*val)
def vrho(th, nf): return np.array([t**2/(2*Phi(t, nf)**2*(rho+t)**2) for t in th])

th = np.logspace(-2.6, 1.35, 300)

fig, ax = plt.subplots(figsize=(7.0, 4.6))
curves = [
    (r"exponential $+$ temp. cost",  n_exp(eta), "C0", "-"),
    (r"power-law $+$ temp. cost",    n_pow(eta), "C3", "-"),
    (r"exponential (pure)",          n_exp(0.0), "C0", ":"),
    (r"power-law (pure)",            n_pow(0.0), "C3", ":"),
]
for lbl, nf, c, ls in curves:
    lw = 2.1 if ls == "-" else 1.6
    ax.loglog(th, vrho(th, nf), c, ls=ls, lw=lw, label=lbl)

# analytic pure-power-law peak
thstar = rho*(1-beta)/(1+beta)
vpl = vrho(np.array([thstar]), n_pow(0.0))[0]
ax.plot([thstar], [vpl], "o", color="C3", ms=6, zorder=5)
ax.annotate(r"$\theta^\star=\rho\dfrac{1-\beta}{1+\beta}$", xy=(thstar, vpl),
            xytext=(0.02, vpl*1.5), fontsize=10.5, color="C3",
            arrowprops=dict(arrowstyle="->", color="C3", lw=0.8))
ax.text(0.0028, 0.055, "power-law:\nconstant signal\n"
        r"$(\theta\to0)$" "\nhas value $0$", fontsize=8.6, color="C3", ha="left", va="top")

ax.set_title(r"value with discounted predictor  $\alpha^\rho=E_t\!\int_t^\infty e^{-\rho(s-t)}\mu\,ds$   ($\rho=1,\ \lambda=0$)")
ax.set_xlabel(r"signal speed $\theta$")
ax.set_ylabel(r"value rate $v^\rho(\theta)$   (fixed $\mathrm{Var}(\mu)=1$)")
ax.legend(fontsize=9.0, loc="lower center")
fig.tight_layout()
fig.savefig("figures/fig_value_discounted.png"); fig.savefig("figures/fig_value_discounted.pdf")
print("wrote figures/fig_value_discounted.png")
print(f"pure power-law peak theta* = {thstar:.4f}")
for lbl, nf, *_ in curves:
    v = vrho(th, nf)
    print(f"  {lbl:28s} v(theta->0)={v[0]:.3e}  peak@theta={th[np.argmax(v)]:.3f}")
