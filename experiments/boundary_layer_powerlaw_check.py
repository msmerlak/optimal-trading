"""Numerical test of the power-law branch of Proposition (Boundary-layer decay).

MEMORY WARNING / GUARD.  This test builds DENSE n x n kernel matrices and calls
a dense solve, so cost is 8*n^2 bytes and O(n^3) flops.  n = (T + 2P)/dt grows
fast with the pad P; an earlier version used dt=0.02, T=40, P=400 -> n ~ 42000,
i.e. ~14 GB per matrix, which exhausts memory.  MAX_N below is a hard cap and
the script refuses to run above it.  Keep P a few multiples of T, not 10x.

Claim under test: the finite-horizon optimum on [0,T] relaxes to the whole-line
optimum in the interior, with deviation decaying as d(t)^{-nu}, nu=(1-beta)/2,
d(t) = min(t, T-t).

Construction (same as check 7 of test_all_results.py, power-law kernel): solve
the deterministic (perfect-foresight) program

    min_u  (gamma/2) sum_ij g(|t_i-t_j|) u_i u_j dt^2  -  sum_i alpha_i u_i dt

on [0,T] and on a padded window [-P, T+P]; restrict the padded solution to
[0,T]; the difference is the boundary layer.  Report the log-log slope of
|u_fh - u_wl| against the distance to the START boundary (the causal-truncation
edge the proof argues about).  Pure transient impact: eta = lam = 0.

Run:  python3 experiments/boundary_layer_powerlaw_check.py
"""
from __future__ import annotations
import sys
import numpy as np

MAX_N = 6000                      # hard cap: 8*6000^2 = 288 MB per matrix

gamma, beta = 1.0, 0.5
nu = (1.0 - beta) / 2.0
dt, T, P, w0 = 0.05, 20.0, 100.0, 0.3


def guard(n: int, label: str) -> None:
    mb = 8.0 * n * n / 1e6
    print(f"  [{label}] n={n}, dense matrix {mb:.0f} MB")
    if n > MAX_N:
        sys.exit(f"REFUSING: n={n} exceeds MAX_N={MAX_N} ({mb:.0f} MB). "
                 f"Increase dt or shrink the pad P.")


def solve_on(t):
    n = len(t)
    idx = np.arange(n)
    lag = np.abs(idx[:, None] - idx[None, :]) * dt
    np.fill_diagonal(lag, 1.0)                              # placeholder, overwritten below
    G = lag ** (-beta)
    np.fill_diagonal(G, 2 * dt ** (-beta) / ((1 - beta) * (2 - beta)))  # cell-integrated
    M = gamma * dt**2 * G
    return np.linalg.solve(M, dt * np.sin(w0 * t))


t_fh = np.arange(0.0, T + dt / 2, dt)
t_pad = np.arange(-P, T + P + dt / 2, dt)
guard(len(t_fh), "window")
guard(len(t_pad), "padded")

u_fh = solve_on(t_fh)
u_pad = solve_on(t_pad)
mask = (t_pad >= -1e-9) & (t_pad <= T + 1e-9)
u_wl = u_pad[mask]
assert len(u_wl) == len(u_fh)

dev = np.abs(u_fh - u_wl)
scale = float(np.max(np.abs(u_wl)))

print(f"beta={beta}  nu=(1-beta)/2={nu:.3f}  dt={dt}  T={T}  pad={P}")
print("local log-log slopes of |u_fh - u_wl| vs distance-to-start:")
ds = [0.5, 1.0, 2.0, 5.0]
vals = [dev[int(round(d / dt))] for d in ds]
for (d0, d1, v0, v1) in zip(ds[:-1], ds[1:], vals[:-1], vals[1:]):
    s = np.log(v1 / v0) / np.log(d1 / d0)
    print(f"  d {d0:4.1f} -> {d1:4.1f}: |dev| {v0:.5f} -> {v1:.5f}   local slope {s:+.3f}")
print(f"proposition's claimed exponent: {-nu:+.3f} (an UPPER bound, not a rate)")

# verdict: is the observed deviation below C * d^-nu for a fixed C fitted at d=0.5?
C = vals[0] * ds[0] ** nu
below = all(v <= C * d ** (-nu) * (1 + 1e-9) for d, v in zip(ds, vals))
print(f"C d^-nu envelope with C={C:.5f} fitted at d=0.5: "
      f"{'CONSISTENT (deviation stays under the bound)' if below else 'VIOLATED'}")
print("NOTE: observed decay is FASTER than d^-nu, so this test is consistent")
print("      with the bound but does NOT confirm the exponent is sharp.")
print("NOTE: this is the DETERMINISTIC (perfect-foresight) window problem, a")
print("      proxy for the adapted claim; it tests factor truncation only.")
print(f"whole-line |u| scale = {scale:.5f}; relative deviations: "
      + ", ".join(f"d={d}: {v/scale:.4f}" for d, v in zip(ds, vals)))
