"""Fig 1 (Sec 3): the optimal filter per unit signal, across kernels.
(a) trade (rate) filter   |u*/alpha|  ~ |w| * n_hat(w)^{-1/2}
(b) position filter        |x*/alpha|  ~        n_hat(w)^{-1/2}
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as G

w = np.logspace(-1.3, 1.3, 1500)   # ~0.05 to 20: enough to show the plateaus, shelves and slopes
def cb(b): return 2*G(1-b)*np.sin(np.pi*b/2)

# n_hat(w) = eta w^2 + gamma ghat(w) w^2 + lambda
def n_pow(w, gamma=1, beta=0.5, eta=0, lam=0):
    return eta*w**2 + gamma*cb(beta)*np.abs(w)**(1+beta) + lam
def n_exp(w, gamma=1, kappa=2, eta=0, lam=0):
    return eta*w**2 + gamma*2*kappa*w**2/(kappa**2+w**2) + lam

curves = {
    r"power-law only  ($\eta=\lambda=0$)":                 n_pow(w, lam=0, eta=0),
    r"exp + risk  ($\eta=0,\ \lambda=0.5$)":                n_exp(w, lam=0.5, eta=0),
    r"exp + risk + temporary cost  ($\eta=0.3,\ \lambda=0.5$)":        n_exp(w, lam=0.5, eta=0.3),
    r"power-law + risk + temporary cost  ($\eta=0.3,\ \lambda=0.5$)":   n_pow(w, lam=0.5, eta=0.3),
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 4.4))
for lab, n in curves.items():
    ax1.loglog(w, w*n**-0.5, lw=2, label=lab)   # trade (rate) filter
    ax2.loglog(w, n**-0.5,   lw=2, label=lab)   # position filter

ax1.set_xlabel(r"frequency $\omega$")
ax1.set_ylabel(r"$|\hat u^\star(\omega)/\hat\alpha(\omega)|\ \propto\ |\omega|\,\hat n(\omega)^{-1/2}$")
ax1.set_title(r"(a) trade (rate) filter")
ax1.legend(fontsize=7.5, loc="lower center"); ax1.grid(True, which="both", alpha=0.25)

ax2.set_xlabel(r"frequency $\omega$")
ax2.set_ylabel(r"$|\hat x^\star(\omega)/\hat\alpha(\omega)|\ \propto\ \hat n(\omega)^{-1/2}$")
ax2.set_title(r"(b) position filter")
ax2.legend(fontsize=7.5, loc="lower left"); ax2.grid(True, which="both", alpha=0.25)

fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(f"../figures/fig1_filter_magnitude.{ext}", dpi=150)
print("fig1 done")
