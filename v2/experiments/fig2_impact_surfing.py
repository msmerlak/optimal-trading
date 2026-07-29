"""Fig 4 (Sec 4.3): impact surfing.
(a) flow response R(theta) for the exponential kernel at several lambda; power-law never flips.
(b) phase diagram in (theta, lambda): follow (R>0) vs reverse (R<0), boundary theta*(lambda).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as G
from scipy import integrate

gamma, kappa = 1.0, 2.0

def Phi_exp(theta, lam):
    A = 2*kappa*gamma + lam
    m = kappa*np.sqrt(lam/A)
    return np.sqrt(A)*(m+theta)/(kappa+theta)
def c1_exp(lam):
    return 1.0/np.sqrt(2*kappa*gamma + lam)
def R_exp(theta, lam):
    Ph = Phi_exp(theta, lam)
    return (theta**2/Ph)*(1.0/Ph - 2*c1_exp(lam))

def Phi_pow(theta, lam, beta=0.5, gamma=1.0):    # Szego outer factor n_+(i theta) of n = gamma cb |w|^{1+beta} + lam
    cb = 2*G(1-beta)*np.sin(np.pi*beta/2)
    f = lambda t: np.log(gamma*cb*t**(1+beta) + lam)/(theta**2 + t**2)
    val = 0.0
    for a, b in [(1e-9, 1e-3), (1e-3, 1), (1, 1e3), (1e3, 1e7)]:
        v, _ = integrate.quad(f, a, b, limit=200); val += v
    return np.exp(theta/np.pi*val)               # exp[(theta/2pi) int_R] = exp[(theta/pi) int_0^inf]
def R_pow(theta, lam):                           # cusp: c_1=0 -> R = theta^2/Phi^2 > 0
    Ph = np.array([Phi_pow(t, lam) for t in np.atleast_1d(theta)])
    return theta**2/Ph**2

th = np.linspace(0.05, 3, 300)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))
for lam, col in zip([0.0, 0.3, 0.6], ["C0", "C1", "C2"]):
    ax1.plot(th, R_exp(th, lam), color=col, ls="-",  lw=2, label=fr"$\lambda={lam}$")
    ax1.plot(th, R_pow(th, lam), color=col, ls="--", lw=2)
ax1.axhline(0, color="0.5", lw=0.8)
ax1.set_xlabel(r"signal speed $\theta$"); ax1.set_ylabel(r"rate response $R(\theta)$")
ax1.set_title(r"(a) $R(\theta)$: solid $=$ exponential, dashed $=$ power-law")
ax1.legend(fontsize=9, loc="lower left", title="risk aversion")
ax1.grid(alpha=0.25); ax1.set_xlim(0, 3); ax1.set_ylim(-1.2, 1.15)

# phase diagram
TH = np.linspace(0.01, 3, 300); LAM = np.linspace(0.0, 2, 300)
TG, LG = np.meshgrid(TH, LAM)
RG = R_exp(TG, LG)
ax2.contourf(TG, LG, np.sign(RG), levels=[-1.5,0,1.5], colors=["#f4a582", "#92c5de"])
# boundary theta*(lambda) = kappa - 2 m
lam_line = np.linspace(0, 2*kappa*gamma/3, 200)
m_line = kappa*np.sqrt(lam_line/(2*kappa*gamma+lam_line))
ax2.plot(kappa-2*m_line, lam_line, "k-", lw=2)
ax2.axhline(2*kappa*gamma/3, color="k", ls=":", lw=1)
ax2.axvline(kappa, color="k", ls=":", lw=1)
ax2.text(kappa+0.05, 1.80, r"$\theta=\kappa$", fontsize=8)
ax2.text(0.28, 0.20, "follow\n($R>0$)", fontsize=10)
ax2.text(1.05, 1.55, "reverse\n($R<0$)", fontsize=10)
ax2.text(2.02, 1.40, r"$\lambda=2\kappa\gamma/3$", fontsize=8)
ax2.set_xlabel(r"signal speed $\theta$"); ax2.set_ylabel(r"risk aversion $\lambda$")
ax2.set_title(r"(b) phase diagram (exponential kernel)")
ax2.set_xlim(0, 3); ax2.set_ylim(0, 2)

fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(f"../figures/fig2_impact_surfing.{ext}", dpi=150)
print("fig4 done")
