"""Fig 5 (Sec 5): finite-horizon vs whole-line optimum -- interior agreement, boundary layers.

Same discretized cost operator M is inverted on [0,T] (finite horizon, Gohberg-Krein)
and on a large padded interval (whole line / Wiener-Hopf, restricted to [0,T]).
The two optimal *rates* coincide in the interior and deviate in start-up and terminal layers,
the content of Proposition (boundary-layer decay).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

eta, gamma, kappa, lam = 0.5, 1.0, 2.0, 1.0
dt = 0.05
T = 20.0
omega0 = 0.6   # signal frequency

def solve_on(t):
    n = len(t)
    idx = np.arange(n)
    Gmat = np.exp(-kappa*np.abs(idx[:, None]-idx[None, :])*dt)     # propagator kernel
    L = np.tril(np.ones((n, n)))                                    # cumulative-sum (position)
    M = eta*dt*np.eye(n) + gamma*dt**2*Gmat + lam*dt**3*(L.T @ L)
    alpha = np.sin(omega0*t)
    u = np.linalg.solve(M, dt*alpha)
    return u

# finite horizon [0,T]
t_fh = np.arange(0, T+dt/2, dt)
u_fh = solve_on(t_fh)

# whole line: pad by P on each side, restrict to [0,T]
P = 20.0
t_pad = np.arange(-P, T+P+dt/2, dt)
u_pad = solve_on(t_pad)
mask = (t_pad >= -1e-9) & (t_pad <= T+1e-9)
u_wl = u_pad[mask]
t_wl = t_pad[mask]

fig, ax = plt.subplots(figsize=(7.4, 4.2))
ax.plot(t_wl, u_wl, "k-", lw=2, label="whole-line (stationary) rate $u^\\star$")
ax.plot(t_fh, u_fh, "C3--", lw=1.8, label="finite-horizon rate $u^{\\star,T}$")
# shade boundary layers ~ 1/b1 (slowest zero); mark a nominal width
b1 = kappa*np.sqrt(lam/(2*kappa*gamma+lam))  # ~ slow EMA rate scale
width = 3.0/max(b1, 0.3)
ax.axvspan(0, width, color="0.85", alpha=0.6)
ax.axvspan(T-width, T, color="0.85", alpha=0.6, label="boundary layers")
ax.set_xlabel("time $t$"); ax.set_ylabel("trading rate")
ax.set_title("Finite horizon vs whole line: interior agreement, boundary layers")
ax.legend(fontsize=9, loc="upper right"); ax.grid(alpha=0.25)
ax.set_xlim(0, T)
fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(f"../figures/fig3_boundary_layer.{ext}", dpi=150)
print("fig5 done; max interior |u_fh-u_wl| =",
      float(np.max(np.abs(u_fh - u_wl)[(t_fh > width) & (t_fh < T-width)])))
