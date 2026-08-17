"""fig_boundary_layer: finite horizon vs whole line (rational friction).

Regenerates the figure used in Section "Finite-horizon solutions".  The v3/v4/v5
figure file was inherited from the v2 figure set without a generating script;
this script restores provenance.  It uses the same construction as check 7 of
experiments/test_all_results.py:

  * friction in the rate variable on a grid, eta I + gamma dt G + lam dt^2 L'L
    with G = exp(-kappa|t-s|) and L the cumulative-sum (position) operator;
  * the FINITE-HORIZON rate solves the program on [0,T];
  * the WHOLE-LINE rate is the same program solved on the padded window
    [-P, T+P] and then restricted to [0,T] (the pad supplies the past and the
    future the window truncates);
  * the deterministic (perfect-foresight) signal alpha_t = sin(w0 t) is used, so
    the figure isolates the boundary layers rather than mixing in signal noise.

Shading rule (stated in the caption): three e-folds of the slowest zero b1 of
n_hat_+, i.e. width 3/b1 -- a scale, not a fitted width.

Memory: dense (T+2P)/dt square matrices.  MAX_N caps the padded grid.
Run:  python3 experiments/fig_boundary_layer.py
"""
from __future__ import annotations
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MAX_N = 6000

os.environ["PATH"] = os.environ.get("PATH", "") + ":/Library/TeX/texbin"
plt.rcParams.update({"text.usetex": True, "font.family": "serif",
                     "font.serif": ["Computer Modern Roman"],
                     "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
                     "figure.dpi": 200, "savefig.bbox": "tight",
                     "axes.grid": True, "grid.alpha": 0.25, "font.size": 10})

eta, gamma, kappa, lam = 0.5, 1.0, 2.0, 1.0
dt, T, P, w0 = 0.05, 20.0, 20.0, 0.6

# slowest zero of n_hat_+ for the three-friction rational symbol
s2 = kappa**2 + (2 * kappa * gamma + lam) / eta
p2 = lam * kappa**2 / eta
b1 = np.sqrt((s2 - np.sqrt(s2**2 - 4 * p2)) / 2)
width = 3.0 / b1


def solve_on(t):
    n = len(t)
    if n > MAX_N:
        sys.exit(f"REFUSING: n={n} > MAX_N={MAX_N} ({8.0*n*n/1e6:.0f} MB)")
    idx = np.arange(n)
    G = np.exp(-kappa * np.abs(idx[:, None] - idx[None, :]) * dt)
    L = np.tril(np.ones((n, n)))
    M = eta * dt * np.eye(n) + gamma * dt**2 * G + lam * dt**3 * (L.T @ L)
    return np.linalg.solve(M, dt * np.sin(w0 * t))


t_fh = np.arange(0.0, T + dt / 2, dt)
u_fh = solve_on(t_fh)
t_pad = np.arange(-P, T + P + dt / 2, dt)
u_pad = solve_on(t_pad)
mask = (t_pad >= -1e-9) & (t_pad <= T + 1e-9)
u_wl = u_pad[mask]

interior = (t_fh > width) & (t_fh < T - width)
print(f"b1={b1:.4f}  boundary-layer scale 3/b1={width:.3f}")
print(f"max |u_fh - u_wl| interior = {np.max(np.abs(u_fh-u_wl)[interior]):.5f}")
print(f"max |u_fh - u_wl| overall  = {np.max(np.abs(u_fh-u_wl)):.5f}")

fig, ax = plt.subplots(figsize=(7.4, 4.2))
ax.axvspan(0, width, color="grey", alpha=0.13, label="boundary layers")
ax.axvspan(T - width, T, color="grey", alpha=0.13)
ax.plot(t_fh, u_wl, "k", lw=2.0, label=r"whole-line (stationary) rate $u^\star$")
ax.plot(t_fh, u_fh, "r--", lw=1.6, label=r"finite-horizon rate $u^{\star,T}$")
ax.set_xlim(0, T)
ax.set_xlabel(r"time $t$")
ax.set_ylabel("trading rate")
ax.set_title("Finite horizon vs whole line: interior agreement, boundary layers")
ax.legend(fontsize=9, loc="upper right")
fig.tight_layout()

for out in [os.path.join(os.path.dirname(__file__), "..", "arxiv", "figures"),
            os.path.join(os.path.dirname(__file__), "..", "figures")]:
    if os.path.isdir(out):
        fig.savefig(os.path.join(out, "fig_boundary_layer.png"))
        fig.savefig(os.path.join(out, "fig_boundary_layer.pdf"))
        print("wrote", os.path.normpath(os.path.join(out, "fig_boundary_layer.png")))
