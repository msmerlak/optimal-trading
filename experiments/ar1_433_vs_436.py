"""
AR(1) numerical identity check: (4.3.3) vs (4.3.6).

The two formulas are equivalent **as continuous-symbol operator identities**.
Numerically evaluating each on the same discretized AR(1) forecast curve requires
a consistent choice of interpolation/operator-realization, otherwise the comparison
mixes the identity check with discretization error.

This experiment makes the comparison along two consistent computational pipelines:

  Pipeline F (FFT-only):  apply each formula's Fourier multiplier to the FFT of
                          the windowed forecast curve and invert. Both formulas
                          MUST give the same number to machine precision because
                          their multipliers are equal as complex functions. This
                          verifies the algebraic identity at the discrete level.

  Pipeline M (Marchaud-only): compute (4.3.3) via double Marchaud quadrature
                          (D_-^beta on a grid of s values, then D_+^beta applied
                          to the result), and compute (4.3.6) via single Marchaud
                          quadrature on the realized past plus the closed-form OU
                          collapse for the forecast tail. Both formulas should give
                          the same number up to quadrature error.

Both pipelines are run on the SAME windowed AR(1) forecast curve.

Hybrid pipeline (the one of most practical interest for the paper): (4.3.3) via
FFT multiplicative, (4.3.6) via FFT-D_+ on the realized portion + closed-form
theta^{1-g} alpha_t. The hybrid mixes representations and so includes both the
symbol-equivalence (machine-eps) and the FFT-vs-closed-form discrepancy on the
forecast tail (small but nonzero due to discretization).
"""

import numpy as np
from scipy.special import gamma as gamma_fn
from scipy.interpolate import interp1d

np.random.seed(2024)

gamma_p = 0.5
theta = 1.0
sigma = 1.0
c_cost = 1.0
beta = (1.0 - gamma_p) / 2.0
one_mg = 1.0 - gamma_p
kappa = 1.0 / (2 * c_cost * gamma_fn(1 - gamma_p) * np.sin(np.pi * gamma_p / 2))
two_sin = 2 * np.sin(np.pi * gamma_p / 2)

# ----- grid -----
N = 2**18
L = 1000.0
dx = 2 * L / N
idx_t = N // 2
s = -L + dx * np.arange(N)

# ----- AR(1) realization -----
phi = np.exp(-theta * dx)
sigma_eps = sigma * np.sqrt((1 - phi**2) / (2 * theta))
alpha_realized = np.empty(N)
alpha_realized[0] = sigma / np.sqrt(2*theta) * np.random.randn()
eps = sigma_eps * np.random.randn(N-1)
for i in range(1, N):
    alpha_realized[i] = phi*alpha_realized[i-1] + eps[i-1]
alpha_t = alpha_realized[idx_t]

# ----- left-side window (preserves AR(1) for s in [-L_keep, 0]) -----
L_keep, L_taper = 500.0, 100.0
def smooth_window(x):
    w = np.ones_like(x)
    mask = (x >= -L) & (x <= -L_keep)
    if mask.any():
        u = (x[mask] + L) / (L - L_keep)
        w[mask] = u*u*(3 - 2*u)
    w[x < -L] = 0.0
    return w
window = smooth_window(s)
alpha_windowed = alpha_realized * window
assert window[idx_t] == 1.0
assert window[idx_t - int(L_keep/dx)] == 1.0  # AR(1) preserved on [-L_keep, 0]

# ----- forecast curve (windowed past + exponential future) -----
alpha_bar = alpha_windowed.copy()
alpha_bar[idx_t+1:] = np.exp(-theta * s[idx_t+1:]) * alpha_t

# ----- FFT multipliers -----
xi = 2*np.pi*np.fft.fftfreq(N, d=dx)
xi_abs, sgn, nz = np.abs(xi), np.sign(xi), xi != 0
xi_safe = np.where(nz, xi_abs, 1.0)
ixi_b  = xi_safe**beta  * np.exp( 1j*beta*np.pi/2*sgn)
mixi_b = xi_safe**beta  * np.exp(-1j*beta*np.pi/2*sgn)
ixi_p  = xi_safe**one_mg * np.exp( 1j*one_mg*np.pi/2*sgn)
mixi_p = xi_safe**one_mg * np.exp(-1j*one_mg*np.pi/2*sgn)
m_riesz = np.where(nz, xi_safe**one_mg, 0.0).astype(complex)
m_mult  = np.where(nz, ixi_b*mixi_b, 0.0)
m_add   = np.where(nz, (ixi_p + mixi_p)/two_sin, 0.0)
m_p     = np.where(nz, ixi_p, 0.0)
m_m     = np.where(nz, mixi_p, 0.0)

fa = np.fft.fft(np.fft.ifftshift(alpha_bar))
def get0(m): return np.fft.fftshift(np.fft.ifft(m*fa))[idx_t].real

# ===== Pipeline F (FFT throughout) =====
D_mult_F  = get0(m_mult)                       # for (4.3.3)
D_add_F   = get0(m_add)                        # for (4.3.4) bulk operator
Dp_F      = get0(m_p)                          # for (4.3.6) past piece via FFT
Dm_F      = get0(m_m)                          # FFT D_-^{1-g} on forecast curve
u_433_F   = kappa * D_mult_F                   # (4.3.3) via FFT multiplicative
u_436_F   = (kappa/two_sin) * (Dp_F + Dm_F)    # (4.3.6) all-FFT (Dm via FFT)

# ===== Pipeline H (hybrid: (4.3.3) FFT-mult; (4.3.6) FFT D_+ + closed-form D_-) =====
Dm_closed = theta**one_mg * alpha_t            # eq. (4.3.5)
u_436_H   = (kappa/two_sin) * (Dp_F + Dm_closed)

# ===== Pipeline M (Marchaud throughout) =====
# D_+^{1-g} alpha(t) by Marchaud quadrature on the windowed AR(1) realized signal
u_min = 1e-8
u_max_c = (0.0 - s[0]) - dx
n_u = 400_000
u_grid = np.exp(np.linspace(np.log(u_min), np.log(u_max_c), n_u))
alpha_interp = interp1d(s, alpha_windowed, kind='cubic',
                        fill_value=0.0, bounds_error=False)
past_vals = alpha_interp(0.0 - u_grid)
integrand_p = (alpha_t - past_vals) / u_grid**(2 - gamma_p)
tail_p = alpha_t * u_max_c**(gamma_p - 1) / (1 - gamma_p)
Dp_M = (1 - gamma_p)/gamma_fn(gamma_p) * (np.trapezoid(integrand_p, u_grid) + tail_p)

# (4.3.6) via Marchaud:
u_436_M = (kappa/two_sin) * (Dp_M + Dm_closed)

# (4.3.3) via Marchaud double quadrature:
# Step 1: g(s) = D_-^{beta} bar_alpha(t,.)(s) on a grid of s-values <= 0 (for D_+ step)
# Step 2: D_+^{beta} g(t) by Marchaud
#
# Computing g(s) requires:  ((beta)/Gamma(1-beta)) * int_0^inf (f(s) - f(s+u))/u^{1+beta} du
# where f = bar_alpha. The integrand splits at u = -s (when s+u crosses 0):
#   for s+u <= 0 (i.e., u <= -s): f(s+u) = alpha_windowed(s+u)
#   for s+u >  0:                 f(s+u) = exp(-theta(s+u)) alpha_t
#
# Use a moderate grid of evaluation points s_eval near t=0.
# Spacing matched to the FFT grid; need enough nearby points for the D_+^beta quadrature.
S_eval_max = 30.0     # range of s_eval values back from 0
n_se = 30000
s_eval = -np.linspace(1e-6, S_eval_max, n_se)  # negative s values, dense near 0
# Forecast function values
def bar_alpha_at(s_query):
    out = np.where(s_query > 0,
                   np.exp(-theta*np.maximum(s_query, 0)) * alpha_t,
                   alpha_interp(s_query))
    return out

# Inner quadrature: for each s_e in s_eval, compute g(s_e) = D_-^beta bar_alpha at s_e.
# This is expensive (O(n_se * n_u_inner)) — use a smaller inner grid with tail correction.
u_inner = np.exp(np.linspace(np.log(1e-7), np.log(50.0), 10000))
g_values = np.empty(n_se)
for i, s_e in enumerate(s_eval):
    fs = bar_alpha_at(np.array([s_e]))[0]
    fsu = bar_alpha_at(s_e + u_inner)
    integrand = (fs - fsu) / u_inner**(1 + beta)
    # tail correction beyond u = 50: integrand asymptotes to (fs - 0)/u^{1+beta} since
    # bar_alpha(s_e + u) -> 0 super-fast for large u (exponential decay)
    tail = fs * 50.0**(-beta) / beta
    g_values[i] = (beta / gamma_fn(1 - beta)) * (np.trapezoid(integrand, u_inner) + tail)

# Also need g(0) for the D_+^beta(g)(0) formula: g(0) = D_-^beta bar_alpha(t,.)(0)
# For OU forecast, this equals theta^beta * alpha_t (analog of eq. 4.3.5 at half-order)
g_at_0_closed = theta**beta * alpha_t

# Sanity check: at s_e slightly below 0, g(s_e) -> g(0)
fs0 = bar_alpha_at(np.array([0.0]))[0]
fsu0 = bar_alpha_at(0.0 + u_inner)
integrand0 = (fs0 - fsu0) / u_inner**(1 + beta)
tail0 = fs0 * 50.0**(-beta) / beta
g_at_0_marchaud = (beta / gamma_fn(1 - beta)) * (np.trapezoid(integrand0, u_inner) + tail0)

# Outer quadrature: D_+^beta g(0) = (beta/Gamma(1-beta)) * int_0^inf (g(0) - g(-u))/u^{1+beta} du
# We have g at s_eval points (negative values close to 0).
g_interp = interp1d(-s_eval, g_values, kind='cubic',
                    fill_value=(g_values[-1], g_at_0_marchaud),
                    bounds_error=False)
# u = -s_e, so u in [1e-6, S_eval_max]
u_outer = np.exp(np.linspace(np.log(1e-7), np.log(S_eval_max - 1e-6), 50000))
g_neg_u = g_interp(u_outer)
integrand_outer = (g_at_0_marchaud - g_neg_u) / u_outer**(1 + beta)
# tail correction: beyond S_eval_max, g(-u) doesn't decay (the AR(1) has stationary
# fluctuations through D_-^beta). For OU realized, g(-u) fluctuates around 0 in
# expectation (g is mean-zero stationary if alpha is mean-zero stationary).
# Approximate tail: assume g(-u) ~ 0 for u > S_eval_max, so tail = g(0) * S_eval_max^{-beta}/beta.
tail_outer = g_at_0_marchaud * S_eval_max**(-beta) / beta
DpDm_M = (beta / gamma_fn(1 - beta)) * (np.trapezoid(integrand_outer, u_outer) + tail_outer)
u_433_M = kappa * DpDm_M

# ===== Report =====
print("=" * 76)
print("AR(1) numerical identity (4.3.3) vs (4.3.6)")
print("=" * 76)
print(f"  gamma = {gamma_p}, theta = {theta}, c = {c_cost}, kappa = {kappa:.10f}")
print(f"  N = {N}, L = {L}, alpha_t = {alpha_t:.10f}")

print(f"\n--- Pipeline F (FFT throughout) -----------------------------------------")
print(f"  (4.3.3) FFT multiplicative:        u_bulk = {u_433_F: .12f}")
print(f"  (4.3.6) FFT-D_+ + FFT-D_-:         u_bulk = {u_436_F: .12f}")
print(f"  |diff|                                  = {abs(u_433_F - u_436_F):.3e}  (machine eps: symbol identity)")

print(f"\n--- Pipeline H (hybrid: FFT for (4.3.3), FFT D_+ + closed form for (4.3.6)) ---")
print(f"  (4.3.3) FFT multiplicative:        u_bulk = {u_433_F: .12f}")
print(f"  (4.3.6) FFT-D_+ + theta^(1-g) a_t: u_bulk = {u_436_H: .12f}")
print(f"  |diff|                                  = {abs(u_433_F - u_436_H):.3e}  (FFT vs closed-form D_-^(1-g) error)")
print(f"    component check: FFT D_- = {Dm_F: .10f}  vs closed form theta^(1-g) a_t = {Dm_closed: .10f}")
print(f"    discrepancy on D_-: {abs(Dm_F - Dm_closed):.3e}  (FFT discretization on forecast tail)")

print(f"\n--- Pipeline M (Marchaud throughout) ------------------------------------")
print(f"  D_+^(1-g) alpha(t) Marchaud quad:  {Dp_M: .10f}")
print(f"  g(0) = D_-^beta bar_alpha at 0:    closed = {g_at_0_closed: .10f}, Marchaud = {g_at_0_marchaud: .10f}")
print(f"    err = {abs(g_at_0_closed - g_at_0_marchaud):.2e}")
print(f"  D_+^beta of g, at 0 (Marchaud):    {DpDm_M: .10f}")
print(f"  (4.3.3) Marchaud double quad:      u_bulk = {u_433_M: .12f}")
print(f"  (4.3.6) Marchaud + closed form:    u_bulk = {u_436_M: .12f}")
print(f"  |diff|                                  = {abs(u_433_M - u_436_M):.3e}  (quadrature consistency)")

print(f"\n--- Cross-pipeline summary ----------------------------------------------")
print(f"  (4.3.3) FFT:       {u_433_F: .12f}")
print(f"  (4.3.3) Marchaud:  {u_433_M: .12f}")
print(f"  (4.3.6) FFT:       {u_436_F: .12f}")
print(f"  (4.3.6) hybrid:    {u_436_H: .12f}")
print(f"  (4.3.6) Marchaud:  {u_436_M: .12f}")
