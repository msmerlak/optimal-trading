"""
Numerical verification of the two Riesz-derivative decompositions for the
bulk optimal-execution policy under an OU signal.

Three computations of  D^{1-gamma} bar_alpha(t, .)(t)  at t = 0:

  (M1) Riesz symbol:        |xi|^{1-gamma}                              [reference]
  (M2) Multiplicative W-H:  (i xi)^{(1-gamma)/2} * (-i xi)^{(1-gamma)/2}
  (M3) Additive half-sum:   (1/(2 sin(pi gamma/2))) * [(i xi)^{1-gamma} + (-i xi)^{1-gamma}]

(M1)=(M2)=(M3) as Fourier multipliers, so FFT-side answers must agree to fp.

Independent time-domain checks:
  - Marchaud quadrature for  D_-^{1-gamma} bar_alpha(t,.)(t)  vs the OU closed
    form  theta^{1-gamma} * alpha_t.
  - Marchaud quadrature for  D_+^{1-gamma} alpha(t)  on the realized OU path.
  - Plug both into the additive form and compare to the FFT result.
"""

import numpy as np
from scipy.special import gamma as gamma_fn
from scipy.interpolate import interp1d

np.random.seed(42)

# --- parameters ---
theta = 1.0
sigma = 1.0
gamma_param = 0.5
beta = (1.0 - gamma_param) / 2.0
one_minus_gamma = 1.0 - gamma_param

print(f"Parameters: theta={theta}, sigma={sigma}, gamma={gamma_param}, "
      f"beta=(1-gamma)/2={beta}")

# --- grid (centered at s = 0; N power of 2 for FFT) ---
N = 2**18                 # 262144 pts
L = 500.0                 # half-window; forecast tail decays as exp(-theta s)
dx = 2 * L / N
idx_t = N // 2            # s[idx_t] = 0 exactly
s = -L + dx * np.arange(N)
assert abs(s[idx_t]) < 1e-12
print(f"Grid: N={N}, L={L}, dx={dx:.6e}")

# --- simulate stationary OU forward from s = -L ---
alpha_realized = np.empty(N)
alpha_realized[0] = sigma / np.sqrt(2 * theta) * np.random.randn()
exp_dec = np.exp(-theta * dx)
noise_std = sigma * np.sqrt((1 - np.exp(-2 * theta * dx)) / (2 * theta))
noise = noise_std * np.random.randn(N - 1)
for i in range(1, N):
    alpha_realized[i] = exp_dec * alpha_realized[i-1] + noise[i-1]

alpha_t = alpha_realized[idx_t]
print(f"alpha_t = alpha(0) = {alpha_t:.8f}")

# --- forecast curve: realized on s <= 0, exponential decay on s > 0 ---
alpha_bar = alpha_realized.copy()
alpha_bar[idx_t+1:] = np.exp(-theta * s[idx_t+1:]) * alpha_t

# --- FFT-side multipliers ---
xi = 2 * np.pi * np.fft.fftfreq(N, d=dx)
xi_abs = np.abs(xi)
sgn = np.sign(xi)
nonzero = xi != 0
xi_abs_safe = np.where(nonzero, xi_abs, 1.0)

m1 = np.where(nonzero, xi_abs_safe ** one_minus_gamma, 0.0).astype(complex)

ixi_b  = xi_abs_safe**beta             * np.exp( 1j * beta * np.pi / 2 * sgn)
mixi_b = xi_abs_safe**beta             * np.exp(-1j * beta * np.pi / 2 * sgn)
m2 = np.where(nonzero, ixi_b * mixi_b, 0.0)

ixi_p  = xi_abs_safe**one_minus_gamma  * np.exp( 1j * one_minus_gamma * np.pi / 2 * sgn)
mixi_p = xi_abs_safe**one_minus_gamma  * np.exp(-1j * one_minus_gamma * np.pi / 2 * sgn)
m3 = np.where(nonzero, (ixi_p + mixi_p) / (2 * np.sin(np.pi * gamma_param / 2)), 0.0)

print("\n--- Symbol-level pointwise check (all three should be ~identical) ---")
print(f"  max |m1 - m2| over xi:  {np.max(np.abs(m1 - m2)):.3e}")
print(f"  max |m1 - m3| over xi:  {np.max(np.abs(m1 - m3)):.3e}")
print(f"  max |Im(m2)|        :   {np.max(np.abs(m2.imag)):.3e}")
print(f"  max |Im(m3)|        :   {np.max(np.abs(m3.imag)):.3e}")

# --- apply multipliers via FFT, evaluate at s = 0 ---
# Shift so that s = 0 is at index 0 of the FFT input.
alpha_bar_shifted = np.fft.ifftshift(alpha_bar)
fa = np.fft.fft(alpha_bar_shifted)

def apply_and_get_at_zero(m):
    out_shifted = np.fft.ifft(m * fa)
    out = np.fft.fftshift(out_shifted)
    return out[idx_t].real

D1 = apply_and_get_at_zero(m1)
D2 = apply_and_get_at_zero(m2)
D3 = apply_and_get_at_zero(m3)

print("\n--- FFT bulk operator at s = t = 0 ---")
print(f"  (M1) Riesz       D^(1-g) bar_alpha(t,.)(t):  {D1: .12f}")
print(f"  (M2) Multiplic.  D_+^b D_-^b bar_alpha:       {D2: .12f}")
print(f"  (M3) Additive    (1/2sin)(D_+ + D_-):         {D3: .12f}")
print(f"  |M1 - M2| = {abs(D1 - D2):.3e}")
print(f"  |M1 - M3| = {abs(D1 - D3):.3e}")
print(f"  |M2 - M3| = {abs(D2 - D3):.3e}")

# --- Time-domain Marchaud quadrature for D_-^{1-gamma} bar_alpha(t,.)(t) ---
# Marchaud form:
#   D_-^{1-g} f(t) = (1-g)/Gamma(g) * int_0^inf (f(t) - f(t+u)) / u^{2-g} du
# Forecast tail: f(t+u) = exp(-theta u) * alpha_t for u > 0.
# Closed form (OU): theta^{1-gamma} * alpha_t.

closed_form_Dm = theta ** one_minus_gamma * alpha_t

# log-spaced quadrature on u in [u_min, u_max]
# Tail correction: for u_max chosen so e^{-theta u_max} is negligible,
#   int_{u_max}^infty (1 - e^{-theta u})/u^{2-gamma} du ~ u_max^{gamma-1}/(1-gamma)
# Add this analytically to avoid power-law tail truncation error.
u_min = 1e-8
u_max = 50.0
n_u = 400_000
u_grid = np.exp(np.linspace(np.log(u_min), np.log(u_max), n_u))
integrand_m = (alpha_t - np.exp(-theta * u_grid) * alpha_t) / u_grid ** (2 - gamma_param)
tail_m = alpha_t * u_max**(gamma_param - 1) / (1 - gamma_param)
Dm_quad_raw = np.trapezoid(integrand_m, u_grid)
Dm_quad = (1 - gamma_param) / gamma_fn(gamma_param) * (Dm_quad_raw + tail_m)

print("\n--- Marchaud quadrature for D_-^(1-g) bar_alpha(t,.)(t) (OU forecast tail) ---")
print(f"  Closed form (theta^(1-g) * alpha_t): {closed_form_Dm: .12f}")
print(f"  Marchaud quadrature:                  {Dm_quad: .12f}")
print(f"  Relative error: {abs(Dm_quad - closed_form_Dm)/abs(closed_form_Dm):.3e}")

# --- Time-domain Marchaud quadrature for D_+^{1-gamma} alpha(t) (realized path) ---
# D_+^{1-g} f(t) = (1-g)/Gamma(g) * int_0^inf (f(t) - f(t-u)) / u^{2-g} du
alpha_interp = interp1d(s, alpha_realized, kind='cubic',
                        fill_value='extrapolate', bounds_error=False)
t_eval = 0.0
u_max_causal = t_eval - s[0] - dx   # use full past grid
u_grid_c = np.exp(np.linspace(np.log(u_min), np.log(u_max_causal), n_u))
alpha_past_vals = alpha_interp(t_eval - u_grid_c)
integrand_p = (alpha_t - alpha_past_vals) / u_grid_c ** (2 - gamma_param)
# Tail beyond u_max_causal: in expectation alpha(t-u) -> 0, so tail integrand ~ alpha_t/u^{2-gamma}.
tail_p = alpha_t * u_max_causal**(gamma_param - 1) / (1 - gamma_param)
Dp_quad_raw = np.trapezoid(integrand_p, u_grid_c)
Dp_quad = (1 - gamma_param) / gamma_fn(gamma_param) * (Dp_quad_raw + tail_p)

print("\n--- Marchaud quadrature for D_+^(1-g) alpha(t) on realized path ---")
print(f"  D_+ alpha(t) (numerical) = {Dp_quad: .12f}")

# --- Plug into additive form ---
additive_from_quad = (Dp_quad + Dm_quad) / (2 * np.sin(np.pi * gamma_param / 2))
additive_from_closed = (Dp_quad + closed_form_Dm) / (2 * np.sin(np.pi * gamma_param / 2))

print("\n--- Cross-check: additive-form bulk operator from quadrature vs FFT ---")
print(f"  FFT  (M3):                                       {D3: .12f}")
print(f"  Marchaud quad (D_+ quad + D_- quad)/(2 sin):     {additive_from_quad: .12f}")
print(f"  Marchaud quad (D_+ quad + D_- closed)/(2 sin):   {additive_from_closed: .12f}")
print(f"  |FFT - quad|         = {abs(D3 - additive_from_quad):.3e}")
print(f"  |FFT - closed-form|  = {abs(D3 - additive_from_closed):.3e}")

# --- Compute D_+ and D_- separately via FFT and compare to quadrature directly ---
# This isolates whether the discrepancy is in FFT (boundary artifacts) or quadrature.
m_plus  = np.where(nonzero, ixi_p,  0.0)   # symbol (i xi)^{1-gamma}
m_minus = np.where(nonzero, mixi_p, 0.0)   # symbol (-i xi)^{1-gamma}
Dp_fft = apply_and_get_at_zero(m_plus).real
Dm_fft = apply_and_get_at_zero(m_minus).real

print("\n--- Isolate FFT vs quadrature for D_+ and D_- individually ---")
print(f"  D_-^(1-g) bar_alpha(t,.)(t):")
print(f"    closed form (OU):     {closed_form_Dm: .10f}")
print(f"    Marchaud quadrature:  {Dm_quad: .10f}   (rel err vs CF: {abs(Dm_quad-closed_form_Dm)/abs(closed_form_Dm):.2e})")
print(f"    FFT (symbol (-ixi)^(1-g)): {Dm_fft: .10f}   (rel err vs CF: {abs(Dm_fft-closed_form_Dm)/abs(closed_form_Dm):.2e})")
print(f"  D_+^(1-g) bar_alpha(t,.)(t):")
print(f"    Marchaud quadrature:        {Dp_quad: .10f}")
print(f"    FFT (symbol (ixi)^(1-g)):   {Dp_fft: .10f}")
print(f"    |FFT - quad|: {abs(Dp_fft - Dp_quad):.3e}")
print(f"  Sum check (1/(2 sin))*(D_+ + D_-):")
print(f"    FFT D_+ + FFT D_-:    {(Dp_fft + Dm_fft)/(2*np.sin(np.pi*gamma_param/2)): .10f}  vs Riesz FFT M1: {D1: .10f}")
print(f"    Quad D_+ + Quad D_-:  {(Dp_quad + Dm_quad)/(2*np.sin(np.pi*gamma_param/2)): .10f}")

print("\n--- Diagnosis: FFT wrap-around contamination on realized OU path ---")
print(f"  alpha at left FFT boundary  s=-L: {alpha_realized[0]: .6f}")
print(f"  alpha at right FFT boundary s=+L: {alpha_bar[-1]: .6e}")
print("  The realized OU path does NOT decay at s=-L; FFT periodic extension")
print("  wraps these O(sigma/sqrt(2 theta)) values into what D_- (anticausal)")
print("  perceives as 'future', contaminating the FFT result.")
print("  Marchaud quadrature does not periodically extend; it is the correct value.")

# --- Clean test on a Schwartz function (Gaussian) where wrap-around vanishes ---
print("\n" + "=" * 70)
print("CLEAN TEST: Gaussian curve  f(s) = exp(-s^2/(2 w^2))  (Schwartz, no wrap)")
print("=" * 70)
w = 1.5
f = np.exp(-s**2 / (2 * w**2))
print(f"  f at FFT boundaries: f(-L)={f[0]:.3e}, f(+L)={f[-1]:.3e}")

fa_g = np.fft.fft(np.fft.ifftshift(f))
def get0(m):
    out = np.fft.fftshift(np.fft.ifft(m * fa_g))
    return out[idx_t].real

D1_g = get0(m1)
D2_g = get0(m2)
D3_g = get0(m3)
Dp_g_fft = get0(np.where(nonzero, ixi_p,  0.0))
Dm_g_fft = get0(np.where(nonzero, mixi_p, 0.0))

# Marchaud quadrature for Gaussian at s=0 (symmetric, so D_+ = D_-)
# Integrand far from origin: f(u) -> 0 super-exponentially, so tail behaves as 1/u^{2-gamma}.
# Add analytic tail correction: int_{u_max}^infty 1/u^{2-gamma} du = u_max^{gamma-1}/(1-gamma).
u_max_g = 20 * w
u_grid_g = np.exp(np.linspace(np.log(1e-8), np.log(u_max_g), 400_000))
f_u = np.exp(-u_grid_g**2 / (2 * w**2))
quad_g = np.trapezoid((1.0 - f_u) / u_grid_g**(2 - gamma_param), u_grid_g)
tail_g = u_max_g**(gamma_param - 1) / (1 - gamma_param)
Dm_g_quad = (1 - gamma_param) / gamma_fn(gamma_param) * (quad_g + tail_g)
Dp_g_quad = Dm_g_quad   # symmetry
additive_g_quad = (Dp_g_quad + Dm_g_quad) / (2 * np.sin(np.pi * gamma_param / 2))

# Analytic value for Gaussian via Fourier:
#   D^{1-gamma} f(0) = (2/pi)^{1/2} * 2^{-gamma/2} * w^{gamma-1} * Gamma(1 - gamma/2)
# (derived by integrating |xi|^{1-gamma} * w*sqrt(2*pi)*exp(-w^2 xi^2/2) / (2*pi) over xi)
analytic_riesz_g = np.sqrt(2/np.pi) * 2**(-gamma_param/2) * w**(gamma_param-1) * gamma_fn(1 - gamma_param/2)
# Analytic value for D_+ on Gaussian at 0:
#   D_+^{1-g} f(0) = 2^{-(1-g)/2} * w^{-(1-g)} * Gamma(1 - (1-g)/2) / Gamma(g)
analytic_Dp_g = 2**(-(1-gamma_param)/2) * w**(-(1-gamma_param)) * gamma_fn(1 - (1-gamma_param)/2) / gamma_fn(gamma_param)

print(f"\n  Bulk operator D^(1-g) f at s=0:")
print(f"    Analytic Riesz (closed form):  {analytic_riesz_g: .12f}")
print(f"    (M1) FFT Riesz:                {D1_g: .12f}")
print(f"    (M2) FFT multiplicative:       {D2_g: .12f}")
print(f"    (M3) FFT additive:             {D3_g: .12f}")
print(f"    Marchaud additive (quad+tail): {additive_g_quad: .12f}")
print(f"    |FFT  - analytic|:    {abs(D1_g - analytic_riesz_g):.3e}")
print(f"    |Quad - analytic|:    {abs(additive_g_quad - analytic_riesz_g):.3e}")
print(f"    |FFT  - Marchaud|:    {abs(D1_g - additive_g_quad):.3e}")
print(f"\n  Component (D_+) check:")
print(f"    analytic D_+ on Gaussian: {analytic_Dp_g: .12f}")
print(f"    Marchaud quad+tail:       {Dp_g_quad: .12f}    err: {abs(Dp_g_quad - analytic_Dp_g):.2e}")
print(f"    FFT (i xi)^(1-g):         {Dp_g_fft: .12f}    err: {abs(Dp_g_fft - analytic_Dp_g):.2e}")

# --- Summary table ---
print("\n" + "=" * 70)
print("SUMMARY: bulk operator D^(1-gamma) bar_alpha(t,.)(t)")
print("=" * 70)
print(f"  (M1) FFT Riesz:                {D1: .10f}")
print(f"  (M2) FFT multiplicative W-H:   {D2: .10f}   diff={D2-D1:+.2e}")
print(f"  (M3) FFT additive half-sum:    {D3: .10f}   diff={D3-D1:+.2e}")
print(f"  Marchaud additive (full quad): {additive_from_quad: .10f}   "
      f"diff={additive_from_quad-D1:+.2e}")
