# Söhngen–Tricomi inversion for finite-interval singular integral equations

Reference note for §3.1 of `papers/markowitz-of-cost-pnas.md`. Collects the
classical inversion formulas for the airfoil / finite-Hilbert-transform
equation and the closely related finite-interval fractional integrals of Abel
type, together with the primary sources.

## 1. The airfoil equation (Söhngen 1939, Tricomi 1951)

On the interval $(-1,1)$, the *airfoil equation* (equivalently, the
finite Hilbert transform inversion problem) asks for $\phi$ solving
$$ (T\phi)(x) := \frac{1}{\pi}\, \mathrm{p.v.}\!\int_{-1}^{1}\!\frac{\phi(y)}{x-y}\,dy = f(x), \qquad x\in(-1,1), \tag{A} $$
where the integral is taken in the Cauchy principal-value sense.

**Söhngen's inversion formula.** For $f$ Hölder-continuous on $[-1,1]$, the
general solution of (A) that is integrable at both endpoints is
$$ \phi(x) = -\frac{1}{\pi}\sqrt{\frac{1-x}{1+x}}\;\mathrm{p.v.}\!\int_{-1}^{1}\!\sqrt{\frac{1+y}{1-y}}\,\frac{f(y)}{x-y}\,dy \;+\; \frac{C}{\sqrt{1-x^2}}, $$
with $C\in\mathbb{R}$ arbitrary (Söhngen 1939, §III; Tricomi 1951, Thm.
in §2). The homogeneous equation $T\phi=0$ has the one-dimensional
solution space spanned by $(1-x^2)^{-1/2}$, giving the free parameter $C$.

Requiring $\phi$ bounded at $x=1$ removes the free parameter and forces the
solvability condition
$$ \int_{-1}^{1}\sqrt{\frac{1+y}{1-y}}\,f(y)\,dy = 0; $$
requiring $\phi$ bounded at $x=-1$ gives the analogous condition on the other
side. Both endpoints bounded is over-determined and generically has no
solution.

Tricomi (1951, *Quart. J. Math.*) proved the $L^p$-boundedness of the finite
Hilbert transform for $1<p<\infty$ and established the inversion formulas
above as bounded operators between appropriate weighted $L^p$ spaces.

## 2. Tricomi's equation and its fractional-integral cousin

The equation directly relevant to power-law market impact is not the Cauchy-
kernel airfoil equation but the **weakly singular Fredholm equation of the
first kind**
$$ (G_T u)(t) := \int_0^T |t-v|^{-\beta}\, u(v)\,dv = f(t), \qquad t\in(0,T),\ \beta\in(0,1). \tag{B} $$

The kernel is symmetric (not Cauchy anti-symmetric) and integrable rather than
principal-value singular. This equation is called **Tricomi's equation** in
the singular-integral-equation literature (Samko–Kilbas–Marichev,
*Fractional Integrals and Derivatives*, §13.5).

### 2.1 The two-dimensional null space

The operator $G_T$ on $L^2((0,T))$ has a two-dimensional kernel spanned by
$$ \phi_1(t) = \bigl(t(T-t)\bigr)^{(\beta-1)/2}, \qquad \phi_2(t) = \tfrac{T-2t}{2}\,\phi_1(t), \tag{C} $$
both integrable on $(0,T)$ (the endpoint exponent $(\beta-1)/2 \in
(-1/2,0)$ gives integrable singularities), and both blowing up at $t=0$
and $t=T$. The Fourier / Plancherel argument used by Forde–Sánchez-
Betancourt–Smith (2022, Thm. 2.2 proof) shows that in fact $G_T$ has no
null space on $H^{-\gamma/2}((0,T))$ with $\gamma=1-\beta$, but on
$L^2((0,T))$ the modes (C) are genuine null vectors — they lie in $L^2$ but
not in the fractional Sobolev space where $G_T$ is invertible.

Interpretation: $\phi_1$ is a symmetric U-shape (mass piled up near both
endpoints); $\phi_2$ is an antisymmetric variant. In the airfoil analogy,
$\phi_1$ and $\phi_2$ correspond to the two degrees of freedom in matching
pressure-jump data at the leading and trailing edges of a thin airfoil.

### 2.2 Reduction to Abel and inversion via weight conjugation

Substituting $u(t) = w(t)^{-1}\, g(t)$ with the endpoint weight
$$ w(t) = \bigl(t(T-t)\bigr)^{(1-\beta)/2}, $$
Tricomi's equation (B) transforms into a form solvable by inversion of a
one-sided Riemann–Liouville / Abel operator. Concretely, Forde–Sánchez-
Betancourt–Smith (2022, p.591) write the finite-interval cost operator
$G_T$ as
$$ G_T \;=\; B^{-1}\,I^\nu\,B, \qquad \nu = (1-\beta)/2, $$
where $B$ is multiplication by an endpoint weight of the form
$t^{-(1-\nu)/2}$ (or the symmetrised $w(t)^{-1}$) and $I^\nu$ is a
one-sided Riemann–Liouville fractional integral on $[0,T]$. This is a
**similarity transform**, not a Wiener–Hopf factorization; the two-sided
nature of the kernel $|t-v|^{-\beta}$ is absorbed into the weights $B^{\pm 1}$,
after which the remaining operator is one-sided.

The one-sided operator $I^\nu$ is then inverted by the Chakrabarti–George
(1994) formula for general Abel integral equations, giving an explicit form
$$ u^\star(t) = -\frac{w(t)^{-1}}{\gamma\,\pi^2\,\Gamma(1-\beta)}\, \frac{d}{dt}\!\int_0^T \frac{w(y)\,f(y)}{y-t}\,dy \;+\; \mu_1\phi_1(t) + \mu_2\phi_2(t), $$
with $\mu_{1,2}$ set by whatever boundary or normalisation conditions the
application imposes (initial inventory, terminal liquidation, etc.).

## 3. Causal × anticausal factorization on $[0,T]$

What Forde–Sánchez-Betancourt–Smith (2022, pp. 590–591) actually establish
— following Porter & Stirling (1990), *Integral Equations: A Practical
Treatment from Spectral Theory to Applications*, Examples 6.2 and 9.2 — is
the factorization
$$ G_T \;=\; T\, T^\ast, \tag{D} $$
where $T$ is the **causal** (Volterra) operator on $L^2([0,T])$ with kernel
supported on $\{s\le t\}$,
$$ (T\varphi)(t) = \int_0^t \kappa(s,t)\,\varphi(s)\,ds, \qquad \kappa(s,t) = c_\nu\,(t/s)^{(1-\beta)/2}\,(t-s)^{-(1+\beta)/2}, \tag{E} $$
and $T^\ast$ is its **anticausal** adjoint,
$$ (T^\ast\varphi)(s) = \int_s^T \kappa(s,t)\,\varphi(t)\,dt, $$
both of order $\nu = (1-\beta)/2$. This is the finite-interval analog of the
whole-line Wiener–Hopf factorization $C = C_-C_+$ used in the main paper: a
causal fractional-integration-type operator $T$ against its anticausal
adjoint $T^\ast$, with product $G_T$.

The kernel $\kappa(s,t)$ differs from the whole-line causal kernel $c_+(t-s)^{\nu-1}\mathbf 1_{s\le t}$ only by the weight factor $(t/s)^{(1-\beta)/2}$, which
encodes the left endpoint $t=0$. The identity
$$ T \;=\; B^{-1}\, I_+^\nu\, B \tag{F} $$
with $B$ the multiplication operator $(Bf)(t) = t^{-(1-\beta)/4}f(t)$ (or the
symmetrised endpoint weight $(t(T-t))^{-(1-\beta)/4}$ used with the double
boundary) exhibits $T$ as the standard causal Riemann–Liouville integral
$I_+^\nu$ conjugated by a local multiplication. Multiplication operators are
local in time and preserve both causal and anticausal structure, so (F)
leaves the causal character of $T$ intact. Dually $T^\ast = B\, I_-^\nu\,
B^{-1}$ with $I_-^\nu$ the anticausal Riemann–Liouville integral on $[0,T]$.

Substituting (F) into (D):
$$ G_T \;=\; B^{-1}\, I_+^\nu\, B^2\, I_-^\nu\, B^{-1}. \tag{G} $$
Read left to right, (G) is a causal fractional integration $I_+^\nu$
followed by a local reweighting $B^2$ followed by an anticausal fractional
integration $I_-^\nu$, sandwiched between two local reweightings
$B^{-1}$. The two boundary weights $B^{\pm 1}$ replace the role played on the
whole line by the vanishing Fourier symbol at infinity: they absorb the
boundary defects that would otherwise prevent a clean
$I_-^\nu\cdot I_+^\nu$ factorization on the finite interval.

### 3.1 Comparison table

| | Whole line $\mathbb{R}$ | Finite interval $[0,T]$ |
|---|---|---|
| Cost kernel | $\|t-v\|^{-\beta}$ | $\|t-v\|^{-\beta}\,\mathbf{1}_{[0,T]^2}$ |
| Symbol / spectral tool | Fourier transform | Not available (no translation invariance) |
| Factorization | $C = c_\beta\, I_-^\nu\, I_+^\nu$ | $G_T = T\,T^\ast$ with $T = B^{-1}I_+^\nu B$ |
| Causal factor | $C_+ = c_\beta^{1/2}\,I_+^\nu$ | $T = B^{-1}\,I_+^\nu\,B$ |
| Anticausal factor | $C_- = c_\beta^{1/2}\,I_-^\nu$ | $T^\ast = B\,I_-^\nu\,B^{-1}$ |
| Null space of the operator | $\{0\}$ on $\dot H^{-\nu}(\mathbb R)$ | $\{0\}$ on $H^{-\nu}([0,T])$, 2-dim on $L^2$ |
| Boundary correction | none | Two Söhngen–Tricomi modes $\phi_1, \phi_2$ |

### 3.2 Adapted version

On the whole line, Lemma 1 of the main paper gives $(P_+CP_+)^{-1} = C_+^{-1}
P_+ C_-^{-1}$ using causality of $C_+$ (adaptedness-preserving). The
finite-interval analog would give
$$ (P_+ G_T P_+)^{-1} \;=\; (T^\ast)^{-1}\, P_+\, T^{-1}, $$
provided the causality identities $P_+^\perp T P_+ = 0$ (the kernel of $T$ is
supported on $\{s\le t\}$) and $P_+ T^\ast P_+^\perp = 0$ still hold on
$[0,T]$. Both do: $T$ is Volterra (kernel supported on $s\le t$), so it
preserves adapted processes; $T^\ast$ is anti-Volterra and its adjoint
action is dual. The optimal adapted trading rate is therefore
$$ u^\star_t \;=\; \gamma^{-1}\,(T^\ast)^{-1}\, P_+\, T^{-1}\, \alpha^{\rm eff}, $$
which is the finite-interval analog of equation (11) of the main paper. The
inversions $T^{-1}$ and $(T^\ast)^{-1}$ are given by (F): $T^{-1} = B^{-1}
D_+^\nu B$ with $D_+^\nu = \Gamma(1-r) D^r$ the causal Marchaud derivative,
and dually for $(T^\ast)^{-1}$. Combined with the endpoint constraints (which
add the two Söhngen–Tricomi modes $\phi_1, \phi_2$ via KKT multipliers) this
gives the exact finite-interval, signal-adaptive solution.

Forde–Sánchez-Betancourt–Smith (2022) present the same content in a slightly
different notation: their Theorem 2.2 gives the kernel $k(u,t)$ of the
Gaussian-Volterra representation $u^\star_t = \int_0^t k(u,t)\,dW_u$, obtained
by applying $T^{-1}$ and $(T^\ast)^{-1}$ (via Chakrabarti–George's explicit
Abel inversion) to the effective signal built from the Gaussian process $P$.

### 3.3 The $T\to\infty$ limit: recovering whole-line WH

The finite-interval factorization (D)–(G) converges to the whole-line
Wiener–Hopf factorization $C = c_\beta\, I_-^\nu\, I_+^\nu$ in the deep
interior as $T\to\infty$, in the following precise sense.

**Kernel of the causal factor.** The finite-interval causal kernel is
$$ \kappa(s,t) = c_\nu\,(t/s)^{(1-\beta)/2}\,(t-s)^{\nu-1}, \qquad \nu = (1-\beta)/2. $$
Center coordinates at the midpoint: $s = T/2 + s'$, $t = T/2 + t'$ with $s',
t'$ bounded. Then $t/s = 1 + (t'-s')/(T/2 + s') \to 1$ as $T\to\infty$, and
$$ \kappa(T/2+s',\, T/2+t') \;\longrightarrow\; c_\nu\,(t'-s')^{\nu-1}, $$
which (with the correct normalization $c_\nu = c_\beta^{1/2}/\Gamma(\nu)$) is
exactly the causal Riemann–Liouville kernel of $C_+ = c_\beta^{1/2}\,I_+^\nu$
on $\mathbb{R}$. The endpoint-weight factor $(t/s)^{(1-\beta)/2}$ absorbs the
left boundary at $t=0$ and vanishes locally in the interior.

**Weight $B$.** For the symmetrised weight $B(t) = (t(T-t))^{-(1-\beta)/4}$,
centered at the midpoint,
$$ B(T/2 + t') = \bigl((T/2+t')(T/2-t')\bigr)^{-(1-\beta)/4} = (T/2)^{-(1-\beta)/2}\,\bigl(1 - (2t'/T)^2\bigr)^{-(1-\beta)/4}. $$
The overall $T$-dependent prefactor cancels in the conjugation $B^{-1}\cdot B$;
the remaining $t'$-dependence $\bigl(1-(2t'/T)^2\bigr)^{-(1-\beta)/4}$
converges to $1$ uniformly on any bounded set of $t'$. So the conjugation
$B^{-1}I_+^\nu B$ converges to $I_+^\nu$ itself on compactly supported test
functions in the interior.

**Söhngen–Tricomi modes.** The two boundary null-space modes
$$ \phi_1(t) = \bigl(t(T-t)\bigr)^{(\beta-1)/2}, \qquad \phi_2(t) = \tfrac{T-2t}{2}\phi_1(t), $$
at interior point $t = T/2 + t'$ scale as
$$ \phi_1(T/2 + t') \;\asymp\; T^{(\beta-1)/2} = T^{-\nu}, \qquad \phi_2 \;\asymp\; t'\cdot T^{-\nu}, $$
so both vanish pointwise in the interior as $T\to\infty$ at rate $T^{-\nu}$.
The boundary contribution to the exact solution therefore decays uniformly
on compact interior subsets, and the whole-line WH-based solution (11) of
the main paper is the leading-order interior asymptotic.

**Consequence for the interior error.** Combining the pointwise decay
$|\phi_k(t)| \lesssim d(t)^{-\nu}\,T^{-\nu}$ (with $d(t) = \min(t, T-t)$) with
the Forde–SBS uniform-in-$T$ bound on the KKT multipliers, the boundary-
mode contribution to $u^{\star,T}(t) - u^{\star,\mathbb{R}}(t)$ is
$O(T^{-\nu} d(t)^{-\nu})$. The Marchaud-truncation contribution to the same
difference is $O(d(t)^{-\nu})$, coming from cutting the fractional-integral
tail at the boundary. Both terms decay as $d(t)^{-\nu}$ moving into the
interior, with the boundary-mode piece additionally suppressed by $T^{-\nu}$.
Slow decay $d(t)^{-\nu}$ with $\nu = (1-\beta)/2 \in (0.2, 0.4)$ for
empirical $\beta$ reflects the long spatial memory of the impact kernel.

**Operator convergence.** Read as operators, (G) becomes
$$ G_T \;=\; B^{-1}I_+^\nu B^2 I_-^\nu B^{-1} \;\xrightarrow{\;T\to\infty\;}\; I_+^\nu\, I_-^\nu \;\propto\; C $$
on the interior in the sense of matrix elements against test functions
compactly supported far from the boundary. This is a strong-operator-
topology-in-the-interior statement; it is not norm convergence, and cannot
be, because the boundary null space of $G_T$ (dimension 2) persists for
every finite $T$ while $C$ has trivial null space on $\dot H^{-\nu}(\mathbb
R)$.

## 4. Bibliographic pointers

**Primary sources.**
- H. Söhngen (1939). *Die Lösungen der Integralgleichung
  $g(x)=\tfrac{1}{2\pi}\int_{-a}^{a} f(\xi)/(x-\xi)\,d\xi$ und deren
  Anwendung in der Tragflügeltheorie.* Math. Zeitschrift **45**,
  245–264. DOI: 10.1007/BF01580284. EuDML: https://eudml.org/doc/168850.
- F. G. Tricomi (1951). *On the finite Hilbert transformation.* Quart. J.
  Math. **2**(1), 199–211. DOI: 10.1093/qmath/2.1.199.
- F. G. Tricomi (1951). *The airfoil equation for a double interval.*
  ZAMP **2**, 402–406. DOI: 10.1007/BF02579701.
- F. G. Tricomi (1957/1985). *Integral Equations.* Interscience (repr.
  Dover). Chapter 4 gives the airfoil-equation inversion in book form.

**Modern textbook exposition.**
- S. G. Samko, A. A. Kilbas, O. I. Marichev (1993). *Fractional Integrals
  and Derivatives: Theory and Applications.* Gordon & Breach. §13.5
  (Equations of Tricomi and generalized Abel equations) is the reference
  used throughout the fractional-execution literature.

**Constructive inversion and factorization machinery.**
- A. Chakrabarti, A. J. George (1994). *A formula for the solution of
  general Abel integral equation.* Appl. Math. Lett. **7**(2), 87–90.
- D. Porter, D. S. G. Stirling (1990). *Integral Equations: A Practical
  Treatment from Spectral Theory to Applications.* Cambridge Univ.
  Press. Examples 6.2 and 9.2 give the $G_T = TT^\ast$ factorization of a
  symmetric weakly-singular Fredholm kernel via its spectral square root.

**Application in optimal execution.**
- J. Gatheral, A. Schied, A. Slynko (2012). *Transient linear price impact
  and Fredholm integral equations.* Math. Finance **22**(3), 445–474.
  (No-signal case; Example 2.30 gives the U-shaped schedule
  $u^\star(t)\propto (t(T-t))^{-(1-\beta)/2}$.)
- M. Forde, L. Sánchez-Betancourt, B. Smith (2022). *Optimal trade
  execution for Gaussian signals with power-law resilience.* Quantitative
  Finance **22**(3), 585–596. DOI: 10.1080/14697688.2021.1950919. Extends
  Gatheral–Schied–Slynko to Gaussian signals via the weight-conjugation
  factorization $G_T = B^{-1}I^\nu B$.
