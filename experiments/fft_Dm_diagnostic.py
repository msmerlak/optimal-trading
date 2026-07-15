"""Diagnostic: FFT computation of D_-^{1-gamma} on a pure exponential tail.

Setup: f(s) = exp(-theta s) for s > 0, f(s) = 0 for s <= 0.
Closed form (Marchaud, evaluated at s = 0+):
   D_-^{1-g} f(0+) = ((1-g)/Gamma(g)) * int_0^inf (f(0+) - f(u))/u^{2-g} du
                   = ((1-g)/Gamma(g)) * (1 * Gamma(g) theta^{1-g}/(1-g)) = theta^{1-g}.

Variations:
  (A) f(0) = 1 (right-continuous, jump down to 0 on s < 0).
  (B) f(0) = 0 (left-continuous, value at the discontinuity).
  (C) Smooth extension: f(s) = exp(-theta |s|) (continuous, slope-discontinuous).
  (D) Even smoother: f(s) = exp(-theta^2 s^2 / 2) Gaussian.

The Marchaud closed form for D_-^{1-g} at s=0 uses f(0+) = 1 in all cases (A)-(C) at the right limit.
"""
import numpy as np
from scipy.special import gamma as gamma_fn

gamma_p = 0.5
one_mg = 1.0 - gamma_p
theta = 1.0

N = 2**18
L = 1000.0
dx = 2*L/N
idx_t = N//2
s = -L + dx*np.arange(N)

xi = 2*np.pi*np.fft.fftfreq(N, d=dx)
xi_abs = np.abs(xi); sgn = np.sign(xi); nz = xi != 0
xi_safe = np.where(nz, xi_abs, 1.0)
ixi_p  = xi_safe**one_mg * np.exp( 1j*one_mg*np.pi/2*sgn)
mixi_p = xi_safe**one_mg * np.exp(-1j*one_mg*np.pi/2*sgn)
m_riesz = np.where(nz, xi_safe**one_mg, 0.0).astype(complex)
m_p = np.where(nz, ixi_p, 0.0)
m_m = np.where(nz, mixi_p, 0.0)

def get0(f, m):
    fa = np.fft.fft(np.fft.ifftshift(f))
    return np.fft.fftshift(np.fft.ifft(m*fa))[idx_t].real

# Case A: Heaviside * exp, value 1 at s=0
fA = np.where(s > 0, np.exp(-theta*s), 0.0)
fA[idx_t] = 1.0
# Case B: Heaviside * exp, value 0 at s=0
fB = np.where(s > 0, np.exp(-theta*s), 0.0)
# Case C: symmetric exp
fC = np.exp(-theta*np.abs(s))
# Case D: Gaussian with same scale
fD = np.exp(-theta**2 * s**2 / 2)

closed_Dm = theta**one_mg

print(f"theta={theta}, gamma={gamma_p}, closed form D_-^(1-g)[exp tail](0) = theta^(1-g) = {closed_Dm}")
print(f"{'case':<40} {'D_-':>14} {'D_+':>14} {'Riesz':>14}")
for name, f in [("(A) jump, f(0)=1", fA),
                ("(B) jump, f(0)=0", fB),
                ("(C) symmetric exp e^{-theta|s|}", fC),
                ("(D) Gaussian e^{-theta^2 s^2/2}", fD)]:
    Dm = get0(f, m_m)
    Dp = get0(f, m_p)
    Dr = get0(f, m_riesz)
    print(f"{name:<40} {Dm: 14.10f} {Dp: 14.10f} {Dr: 14.10f}")

# Analytic Riesz on (C) symmetric exp: theta^{1-g}/cos(pi g/2)
print(f"\nAnalytic for (C) Riesz: theta^(1-g)/cos(pi g/2) = {theta**one_mg/np.cos(np.pi*gamma_p/2): .10f}")
print(f"Analytic for (C) D_+ = D_- = theta^(1-g) = {theta**one_mg: .10f}")

# Analytic Riesz on (D) Gaussian: sqrt(2/pi) * 2^{-g/2} * (1/theta)^{g-1} * Gamma(1-g/2) (with w=1/theta)
w = 1.0/theta
analytic_D = np.sqrt(2/np.pi) * 2**(-gamma_p/2) * w**(gamma_p-1) * gamma_fn(1 - gamma_p/2)
analytic_Dp_g = 2**(-(1-gamma_p)/2) * w**(-(1-gamma_p)) * gamma_fn(1 - (1-gamma_p)/2) / gamma_fn(gamma_p)
print(f"Analytic for (D) Riesz: {analytic_D: .10f}")
print(f"Analytic for (D) D_+ = D_-: {analytic_Dp_g: .10f}")
