"""Numerical checks for review of tex/factorization-optimal-trading.tex.

Check A: does the explicit finite-interval Volterra kernel
    k(s,t) = c_b^{1/2} (t/s)^nu (t-s)^{nu-1} / Gamma(nu),  nu=(1-beta)/2
satisfy (T T*)(t,v) = |t-v|^{-beta}  (paper Prop 2 + eq (volterra-kernel))?
And is T*T T-dependent (hence != G_T)?

Check B: which factorization order makes the projected-inverse identity
    (P_+ C P_+)^{-1} = C_+^{-1} P_+ C_-^{-1}
true on a discrete Gaussian adapted-control problem:
  C = C_- C_+  (UL: anticausal x causal)  vs  C = C_+ C_-  (LU / Cholesky).
Direct adapted optimum computed by matching coefficients in the FOC.
"""
import numpy as np
from scipy.special import gamma as G
from scipy import integrate

rng = np.random.default_rng(0)

# ---------------- Check A ----------------
def check_A(beta, t, v):
    nu = (1 - beta) / 2
    cb = 2 * G(1 - beta) * np.sin(np.pi * beta / 2)
    m = min(t, v)
    # TT* kernel: int_0^m k(s,t) k(s,v) ds
    f = lambda s: (t / s) ** nu * (v / s) ** nu * (t - s) ** (nu - 1) * (v - s) ** (nu - 1)
    val, err = integrate.quad(f, 0, m, points=[m], limit=400)
    lhs = cb * val / G(nu) ** 2
    rhs = abs(t - v) ** (-beta)
    return lhs, rhs, lhs / rhs

print("=== Check A: TT* kernel vs |t-v|^-beta ===")
for beta in (0.3, 0.5, 0.7):
    for (t, v) in ((1.0, 0.4), (2.0, 1.7), (0.9, 0.2)):
        lhs, rhs, r = check_A(beta, t, v)
        print(f"beta={beta} t={t} v={v}:  TT*={lhs:.6f}  G={rhs:.6f}  ratio={r:.6f}")

# T*T depends on horizon T -> cannot equal G_T for T-independent kernel
def TstarT(beta, t, v, T):
    nu = (1 - beta) / 2
    cb = 2 * G(1 - beta) * np.sin(np.pi * beta / 2)
    lo = max(t, v)
    f = lambda s: (s / t) ** nu * (s / v) ** nu * (s - t) ** (nu - 1) * (s - v) ** (nu - 1)
    val, _ = integrate.quad(f, lo, T, points=[lo], limit=400)
    return cb * val / G(nu) ** 2

print("\n=== Check A2: T*T kernel at (t,v)=(0.5,0.3) vs horizon T ===")
for T in (1.0, 2.0, 4.0):
    print(f"T={T}: T*T={TstarT(0.5,0.5,0.3,T):.6f}   (G=|t-v|^-0.5={0.2**-0.5:.6f})")

# ---------------- Check B ----------------
# Discrete times i=0..n-1. Signal alpha Gaussian, zero mean, covariance S.
# Filtration F_i = sigma(alpha_0..alpha_i). Adapted control u_i = sum_{j<=i} W[i,j] alpha_j.
# FOC: E_i[(C u)_i] = alpha_i (gamma=1).
# E_i[alpha_j] = (S[j,0:i+1] @ inv(S[0:i+1,0:i+1])) @ alpha_{0:i+1}  for j>i.
def pred_matrix(S, i):
    """P^(i): n x n matrix with (P X)_j = E_i[alpha_j] coefficients on alpha (uses first i+1)."""
    n = S.shape[0]
    P = np.zeros((n, n))
    P[: i + 1, : i + 1] = np.eye(i + 1)
    Sii = S[: i + 1, : i + 1]
    for j in range(i + 1, n):
        P[j, : i + 1] = np.linalg.solve(Sii, S[: i + 1, j])
    return P

def direct_adapted(C, S):
    """Solve FOC by coefficient matching. Returns W lower-triangular: u = W alpha."""
    n = C.shape[0]
    W = np.zeros((n, n))
    # solve row by row: FOC at i involves E_i[u_v] for all v.
    # u_v = W[v,:] alpha ; E_i[u_v] = W[v,:] P^(i) alpha.
    # FOC_i: sum_v C[i,v] W[v,:] P^(i) = e_i  restricted to coeffs on alpha_0..alpha_i
    # Unknowns: all rows of W. Build full linear system in vec(W) (lower-tri entries).
    idx = [(i, j) for i in range(n) for j in range(i + 1)]
    m = len(idx)
    A = np.zeros((m, m))
    b = np.zeros(m)
    Ps = [pred_matrix(S, i) for i in range(n)]
    row = 0
    for i in range(n):
        Pi = Ps[i]
        for k in range(i + 1):  # coefficient on alpha_k of FOC_i
            for col, (v, j) in enumerate(idx):
                # term C[i,v] * W[v,j] * Pi[j,k]... careful: E_i[u_v] = sum_j W[v,j] E_i[alpha_j]
                # coefficient on alpha_k of E_i[alpha_j] is Pi[j,k]
                A[row, col] += C[i, v] * Pi[j, k]
            b[row] = 1.0 if k == i else 0.0
            row += 1
    w = np.linalg.solve(A, b)
    for col, (v, j) in enumerate(idx):
        W[v, j] = w[col]
    return W

def apply_formula(C, S, order):
    """Formula W: u = Cp^{-1} P_+ Cm^{-1} alpha, with C = Cm Cp (order='UL') or C = Cp Cm ('LU').
    Cp causal = lower triangular. Returns W (as matrix of coefficients on alpha, per row time i)."""
    n = C.shape[0]
    if order == "LU":
        L = np.linalg.cholesky(C)          # C = L L^T = Cp Cm
        Cp, Cm = L, L.T
    else:
        # UL: C = U L with U = L^T. Reverse-order Cholesky.
        Rev = np.eye(n)[::-1]
        Lr = np.linalg.cholesky(Rev @ C @ Rev)
        U = Rev @ Lr @ Rev                  # upper triangular, C = U U^T
        Cm, Cp = U, U.T                     # C = Cm Cp, Cp lower ✓
    Cpi = np.linalg.inv(Cp)
    Cmi = np.linalg.inv(Cm)
    # P_+ applied to X = Cmi alpha: row s of Cmi gives coeffs on alpha; project with P^(s)
    Z = np.zeros((n, n))
    for s in range(n):
        Z[s, :] = Cmi[s, :] @ pred_matrix(S, s)
    return Cpi @ Z

print("\n=== Check B: projected-inverse identity, order of factorization ===")
n = 5
# power-law-ish cost matrix on grid + ridge for positivity
tgrid = np.arange(n)
Cmat = np.abs(tgrid[:, None] - tgrid[None, :] + 0.0)
beta = 0.5
Cmat = np.where(Cmat == 0, 2.5, Cmat ** (-beta))
Cmat += 0.5 * np.eye(n)
# random signal covariance
Amat = rng.standard_normal((n, n))
S = Amat @ Amat.T + n * np.eye(n)

W_direct = direct_adapted(Cmat, S)
W_UL = apply_formula(Cmat, S, "UL")
W_LU = apply_formula(Cmat, S, "LU")
print("||W_direct - W_UL|| =", np.linalg.norm(W_direct - W_UL))
print("||W_direct - W_LU|| =", np.linalg.norm(W_direct - W_LU))
print("W_direct row0:", W_direct[0, :3])
print("W_UL     row0:", W_UL[0, :3])
print("W_LU     row0:", W_LU[0, :3])


# ---------------- Check C: corrected terminal-anchored causal factor ----------------
# Reflected causal factor C_+ = R T* R has kernel
#   kappa(s,t) = c^{1/2} ((T-s)/(T-t))^nu (t-s)^{nu-1}/Gamma(nu)  on {s<=t}.
# With C_- = C_+^*, (C_-C_+)(t,v) = sum_s kappa(t,s) kappa(v,s) over s>=max(t,v):
#   c/Gamma(nu)^2 * int_{max(t,v)}^T ((T-t)/(T-s))^nu ((T-v)/(T-s))^nu
#                                     (s-t)^{nu-1}(s-v)^{nu-1} ds  ==  |t-v|^{-beta}.
def check_C(beta, t, v, T):
    nu = (1 - beta) / 2
    cb = 2 * G(1 - beta) * np.sin(np.pi * beta / 2)
    lo = max(t, v)
    f = lambda s: ((T - t) / (T - s)) ** nu * ((T - v) / (T - s)) ** nu \
        * (s - t) ** (nu - 1) * (s - v) ** (nu - 1)
    val, _ = integrate.quad(f, lo, T, points=[lo], limit=400)
    lhs = cb / G(nu) ** 2 * val
    rhs = abs(t - v) ** (-beta)
    return lhs, rhs, lhs / rhs

print("\n=== Check C: reflected terminal-anchored causal factor  C_-C_+ = G_T (T=3) ===")
for beta in (0.3, 0.5, 0.7):
    for (t, v) in ((1.0, 0.4), (2.4, 1.9), (0.9, 0.2)):
        lhs, rhs, r = check_C(beta, t, v, 3.0)
        print(f"beta={beta} t={t} v={v}:  C_-C_+={lhs:.6f}  G={rhs:.6f}  ratio={r:.6f}")
