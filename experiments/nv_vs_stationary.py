"""Neuman-Voss finite-horizon solution vs our stationary two-EMA filter.

Model (our parameterization; NV's with mapping in the note):
  minimize  int_0^T [ (eta/2) u^2 + gamma u J + (lambda/2) x^2 - u alpha ] dt
  s.t.  dx = u dt (x_0=0),  dJ = (u - kappa J) dt (J_0=0),
where J_t = int_0^t e^{-kappa(t-s)} u_s ds is the transient (exponential-resilience)
impact state and the transient cost gamma*int u J = (gamma/2) int int e^{-kappa|t-s|} u u.
This is the Neuman-Voss LQ problem (temporary eta, transient gamma/kappa, running
inventory risk lambda), finite horizon, free terminal (no terminal penalty).

NV solution: state feedback u* = -K(t) (x_t, J_t)^T + feedforward(signal), with
K(t) = R^{-1}(B^T P(t) + N^T) from the matrix Riccati P(t); interior gains are the
algebraic-Riccati constants. We check:
  (A) closed-loop poles of the stationary feedback = -b1,-b2, the EMA rates of our
      two-EMA filter (eq nv-factor);  K_infty stationary gains.
  (B) finite-horizon Riccati K(t) -> K_infty in the interior; terminal boundary layer.
  (C) full adapted OU optimum (discrete solver): local position/flow response across
      the horizon -> stationary X(theta), R(theta) in interior; boundary layers.
"""
import numpy as np
from scipy.linalg import solve_continuous_are
from scipy.integrate import solve_ivp

eta, gam, kap, lam = 0.5, 1.0, 2.0, 1.0     # matches paper table row 5
theta = 1.0                                  # OU signal rate (enters only signal part)

# --- our filter's EMA rates b1,b2 and Phi (eq nv-factor) ---
s2 = kap**2 + (2*kap*gam + lam)/eta
p2 = lam*kap**2/eta
b1 = np.sqrt((s2 - np.sqrt(s2**2 - 4*p2))/2)
b2 = np.sqrt((s2 + np.sqrt(s2**2 - 4*p2))/2)
Phi = np.sqrt(eta)*(b1+theta)*(b2+theta)/(kap+theta)
Xinf = theta/Phi**2
Rinf = theta**2/Phi**2                        # c1=0 since eta>0
print(f"our filter:  b1={b1:.5f}  b2={b2:.5f}  Phi(theta)={Phi:.5f}")
print(f"             X_inf={Xinf:.5f}  R_inf={Rinf:.5f}\n")

# --- (A) algebraic Riccati: stationary feedback + closed-loop poles ---
A = np.array([[0., 0.], [0., -kap]])
B = np.array([[1.], [1.]])
Qm = np.array([[lam, 0.], [0., 0.]])
Rm = np.array([[eta]])
Nm = np.array([[0.], [gam]])                  # cross term  2 z^T N u  (= 2*gamma*J*u)
P = solve_continuous_are(A, B, Qm, Rm, s=Nm)
Kinf = np.linalg.solve(Rm, B.T @ P + Nm.T)    # 1x2
Acl = A - B @ Kinf
poles = np.sort(-np.linalg.eigvals(Acl).real)
print("=== (A) stationary Riccati ===")
print(f"K_inf = [{Kinf[0,0]:.5f}, {Kinf[0,1]:.5f}]  (feedback on x, J)")
print(f"closed-loop poles  = {poles[0]:.5f}, {poles[1]:.5f}")
print(f"our EMA rates b1,b2 = {b1:.5f}, {b2:.5f}   (match: {np.allclose(poles,[b1,b2],atol=1e-6)})\n")

# --- (B) finite-horizon backward Riccati P(t), gains K(t) ---
def ricc_rhs(t, y):
    P = np.array([[y[0], y[1]], [y[1], y[2]]])
    M = B.T @ P + Nm.T
    dP = A.T @ P + P @ A - (P @ B + Nm) @ np.linalg.solve(Rm, M) + Qm
    return -np.array([dP[0, 0], dP[0, 1], dP[1, 1]])   # dP/dt (integrate T->0)

T = 20.0
sol = solve_ivp(ricc_rhs, [T, 0.0], [0., 0., 0.], dense_output=True, rtol=1e-9, atol=1e-12)
def Kt(t):
    y = sol.sol(t); P = np.array([[y[0], y[1]], [y[1], y[2]]])
    return (np.linalg.solve(Rm, B.T @ P + Nm.T)).ravel()
print("=== (B) finite-horizon Riccati gains K(t) vs stationary (T=20) ===")
print(f"{'d_to_T':>7} {'K_x(t)':>10} {'K_J(t)':>10} {'|K-Kinf|':>12}")
for tt in [10.0, 16.0, 18.0, 19.0, 19.5, 19.9]:
    k = Kt(tt); err = np.linalg.norm(k - Kinf.ravel())
    print(f"{T-tt:>7.2f} {k[0]:>10.5f} {k[1]:>10.5f} {err:>12.2e}")
print(f"K_inf = [{Kinf[0,0]:.5f}, {Kinf[0,1]:.5f}]\n")

# --- (C) full adapted OU optimum across the horizon (discrete solver) ---
def solve_W(Cmat, theta, dt):
    n = Cmat.shape[0]; Rev = np.eye(n)[::-1]
    U = Rev @ np.linalg.cholesky(Rev @ Cmat @ Rev) @ Rev  # reverse-order Cholesky
    Cmi, Cpi = np.linalg.inv(U), np.linalg.inv(U.T)
    Z = np.zeros((n, n))
    for s in range(n):
        Z[s, :s] = Cmi[s, :s]
        Z[s, s] = Cmi[s, s:] @ np.exp(-theta*dt*np.arange(n-s))
    return Cpi @ Z

n, dt = 800, 0.025                             # horizon 20
idx = np.arange(n); lag = np.abs(idx[:, None]-idx[None, :])*dt
G = np.exp(-kap*lag); Lt = np.tril(np.ones((n, n)))
Cmat = eta*np.eye(n) + gam*dt*G + lam*dt**2*(Lt.T@Lt)
S = np.exp(-theta*lag)
W = solve_W(Cmat, theta, dt); Wx = dt*(Lt@W)
WxS = Wx@S; WS = W@S
print("=== (C) adapted OU optimum: local response across horizon vs stationary ===")
print(f"stationary  X_inf={Xinf:.5f}  R_inf={Rinf:.5f}")
print(f"{'t':>6} {'d_to_bdry':>10} {'X_local':>10} {'R_local':>10} {'X err%':>8} {'R err%':>8}")
for t in [1.0, 2.0, 5.0, 10.0, 15.0, 18.0, 19.0]:
    i = int(t/dt); d = min(t, n*dt - t)
    Xl = WxS[i, i-1]/S[i-1, i-1]; Rl = WS[i, i-1]/S[i-1, i-1]
    print(f"{t:>6.1f} {d:>10.2f} {Xl:>10.5f} {Rl:>10.5f} "
          f"{100*abs(Xl-Xinf)/Xinf:>8.2f} {100*abs(Rl-Rinf)/Rinf:>8.2f}")
