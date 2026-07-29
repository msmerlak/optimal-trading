"""
Value vs signal speed in the mu-formulation, regularized by a FIXED FINITE risk term lambda.

Signal = the return mu directly (no alpha, no discount). Value at fixed Var(mu)=1:
    v(theta) = 1/(2 Phi(theta)^2),   Phi(theta) = n_+(i theta),  n = eta w^2 + gam g_hat w^2 + lambda.
theta->0: Phi->sqrt(lambda), so v -> 1/(2 lambda) (finite -- a constant return is traded
Markowitz-style x=mu/lambda; the risk term caps the divergence).  No blow-up.

Compare exponential vs power-law transient kernels, with and without a temporary cost.
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
gam, kap, beta, eta, lam = 1.0, 2.0, 0.5, 0.5, 0.5     # FIXED FINITE lambda

def n_pow(e): return lambda w: e*w**2 + gam*cbeta(beta)*np.abs(w)**(1+beta) + lam
def n_exp(e): return lambda w: e*w**2 + 2*gam*kap*w**2/(kap**2+w**2) + lam
def Phi(th, nf):
    val, _ = quad(lambda t: np.log(nf(t))/(th**2+t**2), 0, np.inf, limit=400)
    return np.exp(th/np.pi*val)
def vval(th, nf): return np.array([1.0/(2*Phi(t, nf)**2) for t in th])   # v = 1/(2 Phi^2)

th = np.logspace(-2, 1.5, 280)

fig, ax = plt.subplots(figsize=(7.0, 4.6))
curves = [
    (r"exponential $+$ temp. cost",  n_exp(eta), "C0", "-"),
    (r"power-law $+$ temp. cost",    n_pow(eta), "C3", "-"),
    (r"exponential (no temp.)",      n_exp(0.0), "C0", ":"),
    (r"power-law (no temp.)",        n_pow(0.0), "C3", ":"),
]
for lbl, nf, c, ls in curves:
    lw = 2.1 if ls == "-" else 1.6
    ax.loglog(th, vval(th, nf), c, ls=ls, lw=lw, label=lbl)

# the finite-lambda cap: v(theta->0) -> 1/(2 lambda) (constant signal = Markowitz value)
cap = 1.0/(2*lam)
ax.axhline(cap, color="0.5", lw=0.9, ls="--")
ax.text(0.013, 0.33, r"$v\to \dfrac{1}{2\lambda}$ as $\theta\to0$:"
        "\nconstant signal traded\nMarkowitz (finite, no blow-up)", fontsize=8.6, color="0.35",
        va="top")
# exp floor
floor = 1.0/(2*(2*kap*gam+lam))
ax.axhline(floor, color="C0", lw=0.7, ls=":")
ax.text(9.0, floor*1.12, r"$\dfrac{1}{2(2\kappa\gamma+\lambda)}$ (exp floor)", fontsize=8.0, color="C0")
# power-law slope guide
g = np.logspace(0.5, 1.4, 30)
ax.loglog(g, 0.55*g**(-(1+beta)), "0.5", lw=0.8, ls=":")
ax.text(g[-1]*1.03, 0.55*g[-1]**(-(1+beta)), r"$\propto\theta^{-(1+\beta)}$", fontsize=8.6, color="0.4")

ax.set_title(r"value vs speed, fixed finite risk $\lambda=0.5$  (mu-form, no discount, $\mathrm{Var}(\mu)=1$)")
ax.set_xlabel(r"signal speed $\theta$")
ax.set_ylabel(r"value rate $v(\theta)=1/2\Phi(\theta)^2$")
ax.legend(fontsize=9.0, loc="lower left")
fig.tight_layout()
fig.savefig("figures/fig_value_lambda.png"); fig.savefig("figures/fig_value_lambda.pdf")
print("wrote figures/fig_value_lambda.png")
print(f"cap 1/2lambda = {cap:.3f}, exp floor 1/2(2kg+lam) = {floor:.3f}")
for lbl, nf, *_ in curves:
    v = vval(th, nf)
    print(f"  {lbl:28s} v(theta->0)={v[0]:.3f}  v(theta->inf)={v[-1]:.4f}")
