"""
Temporary impact + power-law propagator.

Setup.  Cost (equivalent forms, same functional):
    J[u] = gamma * int_0^T u_t (int_0^t (t-s)^{-beta} u_s ds) dt
         + (eta/2) int u_t^2 dt - int alpha_t u_t dt
         = (gamma/2) int int |t-s|^{-beta} u_s u_t ds dt + (eta/2) int u^2 - int alpha u.

The two writings are equal (change of variables), so the FOC is the SAME:
    (FOC-opt)   gamma * int_0^T |t-s|^{-beta} u_s ds + eta u_t = alpha_t.
Symbol on Fourier side: gamma c_beta |xi|^{beta-1} + eta.

A common wrong shortcut yields a Volterra equation
    (FOC-myopic)  gamma * int_0^t (t-s)^{-beta} u_s ds + eta u_t = alpha_t
which is the FOC of a myopic controller who ignores future costs from own
current trades.  This has a Mittag-Leffler resolvent kernel
    R(tau) = (gamma/eta^2) Gamma(1-beta) tau^{-beta}
             E_{1-beta,1-beta}(-lambda_eq tau^{1-beta}),
    lambda_eq = (gamma/eta) Gamma(1-beta).

Question. Does the optimal FOC also admit a Mittag-Leffler / Prabhakar closed
form?  We test by comparing three solutions on the same deterministic alpha:

  u_OPT  from (FOC-opt), symmetric operator, dense solve on [0,T]  (truth)
  u_MYO  from (FOC-myopic), causal Volterra, dense solve on [0,T]  (ML resolvent)
  u_FFT  from (FOC-opt), FFT inverse on R                          (cross-check)

If u_OPT == u_MYO, then Mittag-Leffler solves the true problem.  If not, the
ML closed form is for a different (myopic) surrogate equation and does not
generalize the Marchaud (eta=0) reduction to the true optimal policy.
"""

import numpy as np
from math import gamma as Gamma, pi

# ---------- Problem setup ----------
beta = 0.4
gamma_c = 1.0
eta = 0.5
nu = (1 - beta) / 2
c_beta = 2 * Gamma(1 - beta) * np.sin(pi * beta / 2)
print(f"beta={beta}, nu={nu}, c_beta={c_beta:.6f}, gamma={gamma_c}, eta={eta}")

# Grid on R for FFT
L = 60.0
N = 2**15
dt = 2 * L / N
t = np.linspace(-L + dt/2, L - dt/2, N)
xi = 2 * np.pi * np.fft.fftfreq(N, d=dt)

# Test signal
alpha_raw = np.exp(-((t - 2.0)**2) / 2.0) * (t >= 0)
alpha_hat = np.fft.fft(alpha_raw) * dt

# Restrict to [0, T_end] for dense solve
T_end = 12.0
mask = (t >= 0) & (t <= T_end)
t_pos = t[mask]
alpha_pos = alpha_raw[mask]
Np = len(t_pos)
one_minus_beta = 1 - beta

# ---------- Build kernels ----------
# Causal (lower triangular) K_c: cell integral of (t-s)^{-beta}
K_c = np.zeros((Np, Np))
for k in range(Np):
    for j in range(k):
        a_edge = t_pos[k] - t_pos[j] - dt/2
        b_edge = t_pos[k] - t_pos[j] + dt/2
        K_c[k, j] = (b_edge**one_minus_beta - a_edge**one_minus_beta) / one_minus_beta
    K_c[k, k] = (dt/2)**one_minus_beta / one_minus_beta   # int_0^{dt/2} s^{-beta} ds

# Symmetric K_sym: cell integral of |t-s|^{-beta} (both sides)
K_sym = np.zeros((Np, Np))
for k in range(Np):
    for j in range(Np):
        if k == j:
            K_sym[k, j] = 2 * (dt/2)**one_minus_beta / one_minus_beta
        else:
            d = abs(t_pos[k] - t_pos[j])
            a_edge = d - dt/2
            b_edge = d + dt/2
            K_sym[k, j] = (b_edge**one_minus_beta - a_edge**one_minus_beta) / one_minus_beta

# Sanity: K_sym should equal K_c + K_c^T (diagonals already match: 2*K_c_diag)
sym_check = np.max(np.abs(K_sym - (K_c + K_c.T)))
print(f"K_sym == K_c + K_c^T check: max abs diff = {sym_check:.2e}")

# ---------- Solve ----------
A_myo = eta * np.eye(Np) + gamma_c * K_c        # myopic Volterra (ML resolvent applies)
A_opt = eta * np.eye(Np) + gamma_c * K_sym      # true optimal FOC

u_myo = np.linalg.solve(A_myo, alpha_pos)
u_opt = np.linalg.solve(A_opt, alpha_pos)

# Cross-check via FFT on R (WHOLE-LINE problem; differs from dense solve
# on [0,T] by boundary effects since dense solve has natural u=0 outside)
symb = gamma_c * c_beta * np.abs(xi)**(beta - 1) + eta
symb[0] = eta
inv_symb = 1.0 / symb
inv_symb[0] = 0.0
u_fft = np.real(np.fft.ifft(inv_symb * alpha_hat) / dt)[mask]

# Dense whole-line solve: extend the dense grid to include negative t and
# well past the signal, so the truncated problem approximates the R problem.
L_dense = 20.0
dt_dense = dt   # keep same resolution
t_full = np.arange(-L_dense, L_dense, dt_dense)
Nf = len(t_full)
alpha_full = np.exp(-((t_full - 2.0)**2) / 2.0) * (t_full >= 0)
K_sym_full = np.zeros((Nf, Nf))
for k in range(Nf):
    for j in range(Nf):
        if k == j:
            K_sym_full[k, j] = 2 * (dt_dense/2)**one_minus_beta / one_minus_beta
        else:
            d = abs(t_full[k] - t_full[j])
            K_sym_full[k, j] = ((d + dt_dense/2)**one_minus_beta - (d - dt_dense/2)**one_minus_beta) / one_minus_beta
u_full = np.linalg.solve(eta * np.eye(Nf) + gamma_c * K_sym_full, alpha_full)
# Extract on t_pos grid
full_mask = (t_full >= 0) & (t_full <= T_end)
u_opt_wholeline = np.interp(t_pos, t_full[full_mask], u_full[full_mask])

# eta -> 0 Riesz reference
R_symb = np.abs(xi)**(1 - beta) / c_beta
R_symb[0] = 0.0
u_R = np.real(np.fft.ifft(R_symb * alpha_hat) / dt)[mask] / gamma_c

# ---------- Results ----------
def rel(a, b):
    return np.max(np.abs(a - b)) / (np.max(np.abs(b)) + 1e-30)

print(f"\n||u_opt||_inf         = {np.max(np.abs(u_opt)):.5f}   (optimal, dense on [0,T], u=0 outside)")
print(f"||u_opt_wholeline||   = {np.max(np.abs(u_opt_wholeline)):.5f}   (optimal, dense on [-L,L])")
print(f"||u_fft||_inf         = {np.max(np.abs(u_fft)):.5f}   (optimal, FFT on R)")
print(f"||u_myo||_inf         = {np.max(np.abs(u_myo)):.5f}   (myopic Volterra / ML)")
print(f"||u_R  ||_inf         = {np.max(np.abs(u_R)):.5f}   (Riesz, eta=0)")

print(f"\nrel(u_opt_wholeline, u_fft) = {rel(u_opt_wholeline, u_fft):.3e}   <-- both solve wholeline: should be small")
print(f"rel(u_opt, u_myo)           = {rel(u_opt, u_myo):.3e}")
print(f"rel(u_opt_wholeline, u_myo) = {rel(u_opt_wholeline, u_myo):.3e}   <-- KEY: is ML the answer?")

print(f"\n     t        u_opt       u_myo       u_fft       u_R")
for k in [0, 5, 20, 50, 100, 200, 400, 800, 1500, 2500]:
    if k < Np:
        print(f"  {t_pos[k]:7.3f}  {u_opt[k]:10.5f}  {u_myo[k]:10.5f}  {u_fft[k]:10.5f}  {u_R[k]:10.5f}")

# eta scan
print(f"\n---- rel(u_opt, u_myo) across eta (deterministic alpha) ----")
for eta_test in [10.0, 2.0, 1.0, 0.5, 0.1, 0.01]:
    Aopt_t = eta_test * np.eye(Np) + gamma_c * K_sym
    Amyo_t = eta_test * np.eye(Np) + gamma_c * K_c
    uo = np.linalg.solve(Aopt_t, alpha_pos)
    um = np.linalg.solve(Amyo_t, alpha_pos)
    print(f"  eta={eta_test:7.4f}: rel(u_opt, u_myo) = {rel(uo, um):.4f}")

np.savez('/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/experiments/temp_impact_ml_out.npz',
         t=t_pos, u_opt=u_opt, u_myo=u_myo, u_fft=u_fft, u_R=u_R, alpha=alpha_pos,
         beta=beta, eta=eta, gamma_c=gamma_c, c_beta=c_beta)
print("\nSaved arrays.")
