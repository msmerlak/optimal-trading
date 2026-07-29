"""
Transfer function and impulse response of the optimal trading filter,
exponential vs power-law transient impact, with a small risk term lambda and a
small instantaneous (temporary) cost eta.  Scales separated so BOTH kernels show
their full structure: Markowitz plateau -> transient region -> temporary-cost tail,
plus the exponential's extra finite-memory plateau.

n(w) = eta w^2 + gam g_hat(w) w^2 + lambda,
  exp: g_hat = 2 kap/(kap^2+w^2)  -> transient SATURATES at 2 gam kap (bounded, finite memory)
  pow: g_hat = c_beta |w|^{beta-1} -> transient grows as gam c_beta |w|^{1+beta} (long memory)
H(w) = 1/n_+(w),  |H| = 1/sqrt(n);  h(tau) = FT^{-1}[1/n_+], causal.

Crossovers:
  w_c1  = (lam/gam c_beta)^{1/(1+beta)}   Markowitz -> transient
  exp:  w_e = sqrt(2 gam kap/eta)          plateau -> temporary cost
  pow:  w_p = (gam c_beta/eta)^{1/(1-beta)} fractional -> temporary cost
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import gamma as Gf
import os

os.makedirs("figures", exist_ok=True)
os.environ["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "text.usetex": True, "font.family": "serif",
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"})

def cbeta(b): return 2*Gf(1-b)*np.sin(np.pi*b/2)
gam, kap, beta, lam, eta = 1.0, 2.0, 0.5, 0.1, 0.05      # small lambda, small eta

def n_exp(w): return eta*w**2 + 2*gam*kap*w**2/(kap**2+w**2) + lam
def n_pow(w): return eta*w**2 + gam*cbeta(beta)*np.abs(w)**(1+beta) + lam

wc1    = (lam/(gam*cbeta(beta)))**(1/(1+beta))       # Markowitz -> transient
w_exp  = np.sqrt(2*gam*kap/eta)                       # exp plateau -> temp
w_pow  = (gam*cbeta(beta)/eta)**(1/(1-beta))          # power-law fractional -> temp
markow = 1/np.sqrt(lam)
plateau = 1/np.sqrt(2*gam*kap)

def impulse_response(nfun, N=2**19, wmax=16384.0):
    dw = 2*wmax/N
    wf = np.linspace(-wmax, wmax, N, endpoint=False)
    nw = nfun(wf); logn = np.log(nw)
    L = np.fft.fft(np.fft.ifftshift(logn))
    k = np.fft.fftfreq(N); sgn = np.sign(k); sgn[0] = 0.0; sgn[N//2] = 0.0
    HT = np.fft.fftshift(np.real(np.fft.ifft(1j*sgn*L)))
    n_plus = np.sqrt(nw)*np.exp(0.5j*HT)
    g = np.fft.ifft(np.fft.ifftshift(1.0/n_plus)).real * N*dw/(2*np.pi)
    dt = 2*np.pi/(N*dw); t = np.arange(N)*dt
    return t[:N//2], g[:N//2]

te, ge = impulse_response(n_exp)
tp, gp = impulse_response(n_pow)

fig, ax = plt.subplots(1, 2, figsize=(12.0, 4.6))

# ---- (a) transfer function ----
w = np.logspace(-2.5, 5.0, 1600)
ax[0].loglog(w, 1/np.sqrt(n_exp(w)), "C0", lw=2.1, label="exponential")
ax[0].loglog(w, 1/np.sqrt(n_pow(w)), "C3", lw=2.1, label="power-law")
ax[0].axhline(markow,  color="0.5", lw=0.8, ls="--")
ax[0].text(1.8e-2, markow*1.12, r"$1/\sqrt{\lambda}$ (Markowitz)", fontsize=8.6, color="0.4")
ax[0].axhline(plateau, color="C0", lw=0.8, ls="--")
ax[0].text(1.8e-2, plateau*1.16, r"$1/\sqrt{2\kappa\gamma}$ (exp.\ plateau)", fontsize=8.6, color="C0")
for wc, txt in [(wc1, r"$\omega_c$"), (w_exp, r"$\omega_e$"), (w_pow, r"$\omega_*$")]:
    ax[0].axvline(wc, color="0.75", lw=0.8, ls=":")
    ax[0].text(wc*1.15, 1.5e-4, txt, fontsize=9, color="0.4")
# power-law slope guide, placed to overlay the power-law transfer curve
gg = np.logspace(0.4, 2.6, 20)
ax[0].loglog(gg, 0.62*gg**(-(1+beta)/2), "C3", lw=0.9, ls=":")
ax[0].text(gg[len(gg)//2]*1.1, 0.62*gg[len(gg)//2]**(-(1+beta)/2)*1.7, r"$\omega^{-(1+\beta)/2}$",
           fontsize=8.6, color="C3")
# high-frequency instantaneous-cost roll-off: both curves -> 1/(sqrt(eta) * omega)
gh = np.logspace(3.3, 4.5, 20)
ax[0].loglog(gh, (1/np.sqrt(eta))*gh**(-1.0), "0.5", lw=0.9, ls=":")
ax[0].text(gh[2], (1/np.sqrt(eta))*gh[2]**(-1.0)*2.0, r"$\omega^{-1}$ (instant.)", fontsize=8.6, color="0.4")
ax[0].set_ylim(6e-5, 6)
ax[0].set_title(r"(a) transfer function $|H(\omega)|=1/\sqrt{n(\omega)}$")
ax[0].set_xlabel(r"frequency $\omega$"); ax[0].set_ylabel(r"$|H(\omega)|$")
ax[0].legend(fontsize=9.5, loc="lower left")

# ---- (b) impulse response (log-log) ----
me = (te > 0) & (te < 80); mp = (tp > 0) & (tp < 80)
ax[1].loglog(te[me], np.abs(ge[me]), "C0", lw=2.1, label="exponential: short memory")
ax[1].loglog(tp[mp], np.abs(gp[mp]), "C3", lw=2.1, label="power-law: long memory")
ax[1].axhline(1/np.sqrt(eta), color="0.5", lw=0.8, ls="--")
ax[1].text(1.3e-2, 1/np.sqrt(eta)*0.56, r"$h(0^+)=1/\sqrt{\eta}$", fontsize=8.6, color="0.4")
ax[1].annotate("exponential\ncutoff", xy=(30, 2e-3), xytext=(7, 3e-4), fontsize=8.6, color="C0",
               arrowprops=dict(arrowstyle="->", color="C0", lw=0.7))
ax[1].text(22, 0.10, "algebraic tail", fontsize=8.8, color="C3")
ax[1].set_ylim(1e-4, 40)
ax[1].set_title(r"(b) impulse response $h(\tau)=\mathcal{F}^{-1}[1/n_+]$")
ax[1].set_xlabel(r"lag $\tau$"); ax[1].set_ylabel(r"$|h(\tau)|$")
ax[1].legend(fontsize=9.0, loc="lower left")

fig.suptitle(r"trading filter: exponential vs power-law "
             r"($\gamma=1,\ \kappa=2,\ \beta=0.5$; $\lambda=0.1,\ \eta=0.05$)",
             fontsize=11.5, y=1.02)
fig.tight_layout()
fig.savefig("figures/fig_transfer_impulse.png"); fig.savefig("figures/fig_transfer_impulse.pdf")
print("wrote figures/fig_transfer_impulse.png")
print(f"wc1={wc1:.3f}, w_exp(plateau->temp)={w_exp:.1f}, w_pow(fractional->temp)={w_pow:.0f}")
