"""
Explore how the optimal position scales with OU signal speed theta, for the two
transient-impact kernels (exponential vs power-law), with and without a temporary
(instantaneous) cost.  All quantities are closed-form / spectral integrals.

Two summaries:
  X(theta)   = theta / Phi(theta)^2                 (position response, per unit alpha;
                                                     the paper's position gain, eq in App.B)
  std_mu(th) = sqrt( J(theta) ) / Phi(theta),       (actual position std at fixed Var(mu)=1)
               J(theta) = (1/2pi) int S_mu/(Phi^2 n) ... factored as (1/2pi) int 2 theta/((th^2+w^2) n) dw
               so Var(x) = J/Phi^2 with S_mu = 2 theta/(theta^2+w^2)  (Var(mu)=1)

Friction symbols (position-referred):
  exp : n(w) = eta w^2 + 2 gam kap w^2/(kap^2+w^2) + lam
  pow : n(w) = eta w^2 + gam c_beta |w|^{1+beta}    + lam
Phi(theta) = n_+(i theta) via the Szego integral.
"""
import numpy as np
from scipy.special import gamma as Gf
from scipy import integrate

def cbeta(b): return 2*Gf(1-b)*np.sin(np.pi*b/2)

def n_exp(w, gam, kap, lam, eta): return eta*w**2 + 2*gam*kap*w**2/(kap**2+w**2) + lam
def n_pow(w, gam, beta, lam, eta): return eta*w**2 + gam*cbeta(beta)*np.abs(w)**(1+beta) + lam

def Phi(theta, nfun):
    f = lambda t: np.log(nfun(t))/(theta**2 + t**2)
    val, _ = integrate.quad(f, 0, np.inf, limit=400)
    return np.exp(theta/np.pi*val)

def Jint(theta, nfun):   # (1/2pi) int_{-inf}^{inf} 2 theta/((theta^2+w^2) n(w)) dw
    f = lambda w: 2*theta/((theta**2+w**2)*nfun(w))
    val, _ = integrate.quad(f, 0, np.inf, limit=400)
    return val/np.pi     # even integrand: (1/2pi)*2*int_0^inf = (1/pi) int_0^inf

def summarize(gam, kap, beta, lam, eta):
    thetas = np.logspace(-1, 1.6, 16)
    print(f"\n=== gam={gam} kap={kap} beta={beta} lam={lam} eta={eta} ===")
    print(" theta      Phi_exp  Phi_pow |  X_exp     X_pow  |  stdmu_exp stdmu_pow")
    for th in thetas:
        ne = lambda w: n_exp(w, gam, kap, lam, eta)
        npw = lambda w: n_pow(w, gam, beta, lam, eta)
        Pe, Pp = Phi(th, ne), Phi(th, npw)
        Xe, Xp = th/Pe**2, th/Pp**2
        se = np.sqrt(Jint(th, ne))/Pe
        sp = np.sqrt(Jint(th, npw))/Pp
        print(f"{th:7.3f}  {Pe:7.3f} {Pp:7.3f} | {Xe:8.4f} {Xp:8.4f} | {se:8.4f} {sp:8.4f}")

def slopes(gam, kap, beta, lam, eta, label):
    th = np.array([8., 16., 32., 64.])
    ne = lambda w: n_exp(w, gam, kap, lam, eta)
    npw = lambda w: n_pow(w, gam, beta, lam, eta)
    Xe = np.array([t/Phi(t, ne)**2 for t in th])
    Xp = np.array([t/Phi(t, npw)**2 for t in th])
    se = np.array([np.sqrt(Jint(t, ne))/Phi(t, ne) for t in th])
    sp = np.array([np.sqrt(Jint(t, npw))/Phi(t, npw) for t in th])
    def slp(y): return np.polyfit(np.log(th), np.log(y), 1)[0]
    print(f"[{label}] high-theta slopes:  X_exp={slp(Xe):+.3f} X_pow={slp(Xp):+.3f} "
          f"| stdmu_exp={slp(se):+.3f} stdmu_pow={slp(sp):+.3f}")

if __name__ == "__main__":
    gam, kap, beta, lam = 1.0, 2.0, 0.5, 1.0
    summarize(gam, kap, beta, lam, eta=0.0)
    summarize(gam, kap, beta, lam, eta=0.5)
    print("\n--- asymptotic (high-theta) log-log slopes ---")
    slopes(gam, kap, beta, lam, 0.0, "no temp (eta=0)")
    slopes(gam, kap, beta, lam, 0.5, "temp eta=0.5")
    print("\nExpected: eta=0  -> X_exp ~ +1 (theta/(2kg+lam)), X_pow ~ -beta (theta^{-beta});")
    print("          eta>0  -> X_exp ~ X_pow ~ -1 (temp cost 1/(eta theta)).")
    print("std at fixed Var(mu): eta=0 -> exp ~ const(0), pow ~ theta^{-(1+beta)/...}; see numbers.")
