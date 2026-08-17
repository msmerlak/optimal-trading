# Numerical verification: additive vs multiplicative Riesz split

**Script:** `experiments/riesz_split_check.py`
**Log:**    `experiments/riesz_split_check.log`
**Date:**   2026-06-28
**Env:**    Python 3.11.11 in `.venv`; numpy 2.4.6, scipy 1.17.1
**Seed:**   42 (deterministic OU realization)

## What was tested

The bulk-policy operator $\mathbb{D}^{1-\gamma}$ admits three Fourier representations on $\mathbb{R}$:

| Label | Symbol | Operator form |
|---|---|---|
| (M1) Riesz | $\|\xi\|^{1-\gamma}$ | $\mathbb{D}^{1-\gamma}$ |
| (M2) Multiplicative W–H | $(i\xi)^{(1-\gamma)/2}(-i\xi)^{(1-\gamma)/2}$ | $D_+^{(1-\gamma)/2}\,D_-^{(1-\gamma)/2}$ |
| (M3) Additive half-sum | $\frac{1}{2\sin(\pi\gamma/2)}\bigl[(i\xi)^{1-\gamma} + (-i\xi)^{1-\gamma}\bigr]$ | $\frac{1}{2\sin(\pi\gamma/2)}(D_+^{1-\gamma} + D_-^{1-\gamma})$ |

Tested with $\gamma = 0.5$, $\theta = 1$, $\sigma = 1$, $N = 2^{18}$ FFT grid, $L = 500$.

## Result 1 — Symbol-level identity (FFT)

All three multipliers applied to the OU forecast curve $\bar\alpha(t,\cdot)$ via FFT:

```
(M1) FFT Riesz       D^(1-g) bar_alpha(t,.)(t):  -0.605010418490
(M2) FFT multipl.    D_+^b D_-^b bar_alpha:       -0.605010418490
(M3) FFT additive    (1/(2 sin))(D_+ + D_-):      -0.605010418490

|M1 - M2| = 2.22e-16   (machine epsilon)
|M1 - M3| = 2.22e-16   (machine epsilon)
|M2 - M3| = 4.44e-16   (machine epsilon)
```

Pointwise multiplier comparison over the FFT frequency grid:

```
max |m1 - m2| over xi:  1.07e-14
max |m1 - m3| over xi:  7.11e-15
```

**Verdict.** The additive (1.6) and multiplicative (1.7) representations are numerically equal to floating-point precision when applied via FFT — exactly as the symbol identities $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta = \frac{1}{2\sin(\pi\gamma/2)}[(i\xi)^{1-\gamma}+(-i\xi)^{1-\gamma}]$ require.

## Result 2 — Independent quadrature check on a Schwartz function

To rule out an artifact of the FFT setup, the same identity was checked on a Gaussian $f(s) = e^{-s^2/(2w^2)}$ with $w = 1.5$ via independent time-domain Marchaud quadrature with analytic tail correction, against the closed-form Fourier integral $\mathbb{D}^{1-\gamma}f(0) = \sqrt{2/\pi}\,2^{-\gamma/2}w^{\gamma-1}\Gamma(1-\gamma/2)$:

```
Analytic Riesz (closed form):  0.671306308659
FFT Riesz (M1):                0.671182392590    err = 1.24e-04
FFT multiplicative (M2):       0.671182392590    err = 1.24e-04
FFT additive (M3):             0.671182392590    err = 1.24e-04
Marchaud additive (quad+tail): 0.671306308856    err = 1.97e-10

Component D_+ on Gaussian at 0:
  analytic                     0.474685243106
  Marchaud quad+tail           0.474685243245    err = 1.40e-10
  FFT (i xi)^(1-g)             0.474597621213    err = 8.76e-05
```

**Verdict.** On a clean Schwartz function:
- Marchaud quadrature (with analytic $1/u^{2-\gamma}$ tail correction) matches the analytic Riesz to ~$10^{-10}$.
- FFT matches the analytic Riesz to ~$10^{-4}$, limited by grid resolution.
- All three FFT representations (M1, M2, M3) give the same FFT answer to machine precision.

## Result 3 — OU forecast curve, independent components

For the OU forecast curve $\bar\alpha(t,s) = \alpha_s$ for $s\le t$, $= e^{-\theta(s-t)}\alpha_t$ for $s>t$:

```
D_-^(1-g) bar_alpha(t,.)(t)  [forecast tail contribution]
  closed form (OU):    -0.1703380004      theta^(1-g) * alpha_t
  Marchaud quadrature: -0.1703283901      err = 5.64e-05 vs CF
  FFT (-ixi)^(1-g):    +0.0644886532      err = 1.38 (WRONG SIGN)

D_+^(1-g) bar_alpha(t,.)(t)  [realized-past contribution]
  Marchaud quadrature: -0.9546874042
  FFT (ixi)^(1-g):     -0.9201025924      diff = 3.46e-02
```

**Verdict.** The closed-form OU collapse $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t) = \theta^{1-\gamma}\alpha_t$ (eq. 4.3.5 of the paper) is confirmed by Marchaud quadrature to $6\times 10^{-5}$.

**The FFT result on the OU forecast curve is contaminated by wrap-around** at the level of $O(0.19)$, dominated by the failure of the realized OU path to decay at the left FFT boundary ($\alpha(-L) = 0.351$, compared to forecast at the right boundary $\alpha(+L) \sim 10^{-218}$). The FFT periodically extends the input, so the anticausal operator at $s=0$ sees the realized-past values wrapping back in as if they were the future — this is what produces the wrong-sign FFT $D_-$ value above. The Marchaud quadrature is the correct value for the actual (non-periodic) function.

This wrap-around issue does *not* affect Result 1: the symbol identity $\text{(M1)} = \text{(M2)} = \text{(M3)}$ holds at the multiplier level regardless of what the input is. All three FFT computations are equally wrong (or equally right) for any given input; they agree with each other to machine precision because the multipliers are identically equal as complex numbers.

## Bottom line

| Question | Answer | Evidence |
|---|---|---|
| Are the additive and multiplicative forms numerically equal as operators? | Yes, to machine epsilon | Result 1, Result 2 |
| Does the OU closed form $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)=\theta^{1-\gamma}\alpha_t$ hold? | Yes, to $6\times 10^{-5}$ | Result 3 |
| Is FFT a safe way to compute the Riesz derivative of a forecast curve in practice? | Only if the realized signal decays at the FFT boundary (e.g., after windowing or in a long-history setting where wrap-around contamination is negligible). For OU realized paths, Marchaud quadrature with tail correction is more reliable. | Result 3 |

## Notes for the paper

- Result 1 directly supports the claim in §4.3 that (4.3.2) and (4.3.4) are equivalent representations of $\mathbb{D}^{1-\gamma}$.
- Result 3 supports (4.3.5) and the OU policy formula (4.3.6) at the quadrature level.
- The wrap-around issue is a numerical-implementation caveat, not a flaw in either form. A practical implementation that wants to use FFT should window the realized signal or use a spectral method that does not impose periodicity.

## Reproducibility

```bash
.venv/bin/python experiments/riesz_split_check.py
```

Deterministic under the fixed seed.
