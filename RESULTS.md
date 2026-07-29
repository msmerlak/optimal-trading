# Optimal Trading Filters — Results

Fourier convention $\hat f(\omega)=\int_{\mathbb R} e^{i\omega t}f(t)\,dt$; causal kernels have transforms analytic in $\{\operatorname{Im}\omega>0\}$. $\overline{\,\cdot\,}$ denotes complex conjugation; $A^\ast$ the $L^2$-adjoint. $\mathbb E_t$ is conditional expectation given $\mathcal F_t$.

## 1. Definitions

**D1 (Problem).** A position $x_t$ traded at rate $u_t=\dot x_t$, $x_t=\int^t u$, against a return signal $\mu_t$. Objective on the whole line
$$
J(x)=\mathbb E\!\int x_t\mu_t\,dt-\tfrac{\eta}{2}\mathbb E\!\int\dot x_t^2\,dt-\tfrac{\gamma}{2}\mathbb E\!\iint g(|t-s|)\dot x_t\dot x_s\,dt\,ds-\tfrac{\lambda}{2}\mathbb E\!\int x_t^2\,dt,
$$
maximized over $\mathcal F_t$-adapted $x$ of finite friction energy. On $[0,T]$: the same with a terminal constraint $x_T=0$.

**D2 (Friction operator).** Position-referred $N=-\eta\partial_t^2-\gamma\partial_t^2(g\ast\cdot)+\lambda I$, symbol
$$
\hat n(\omega)=\eta\omega^2+\gamma\hat g(\omega)\omega^2+\lambda,\qquad \hat g(\omega)=\int e^{i\omega t}g(|t|)\,dt.
$$
Rate-referred $Q=N(-\partial_t^2)^{-1}$, symbol $\hat q=\hat n/\omega^2=\eta+\gamma\hat g+\lambda/\omega^2$.

**D3 (Signals).** Return $\mu_t=\mathbb E_t[\text{drift}]$, adapted, mean zero. Appreciation $\alpha_t=\mathbb E_t\int_t^\infty\mu_s\,ds$; $\mu=\mathbb E_t[-\dot\alpha]$. Forecast curves $\bar\mu(t,s)=\mathbb E_t[\mu_s]$, $\bar\alpha(t,s)=\mathbb E_t[\alpha_s]=\int_s^\infty\bar\mu(t,r)\,dr$ ($s\ge t$).

**D4 (Wiener–Hopf factorization).** $N=N_-N_+$ with $\hat n=\hat n_-\hat n_+$, $\hat n_-=\overline{\hat n_+}$, $\hat n_+$ outer (analytic and zero-free in $\operatorname{Im}\omega>0$); $N_+$ causal with causal inverse, $N_-=N_+^\ast$. Rate factors $\hat q_\pm=\hat n_\pm/(\mp i\omega)$. Outer factor by the Szegő formula
$$
\hat n_+(\omega)=\exp\Big(\tfrac{1}{2\pi i}\int\big(\tfrac{1}{t-\omega}-\tfrac{t}{1+t^2}\big)\log\hat n(t)\,dt\Big),\quad \operatorname{Im}\omega>0,
$$
and $\Phi(\theta):=\hat n_+(i\theta)=\exp\big[\tfrac{\theta}{2\pi}\int\tfrac{\log\hat n(t)}{\theta^2+t^2}\,dt\big]>0$.

**D5 (Projection).** $P_+$ = optional projection onto adapted processes, $(P_+X)_s=\mathbb E_s[X_s]$. On symbols of stationary filters of the innovations, $P_+$ acts as the plus-part $[\,\cdot\,]_+$ (truncation of the moving-average kernel to lags $\ge0$).

**D6 (Innovations / spectral factor).** For $\mu$ purely non-deterministic Gaussian generating its own filtration: Wold representation $\mu=\psi\ast\dot W$, $\dot W$ unit white noise generating $\mathcal F_t$, $S_\mu=|\hat\psi|^2$, $\hat\psi$ outer. $\hat\varphi$ = outer factor of $\alpha$, $S_\alpha=|\hat\varphi|^2$.

**D7 (Markov signal, order $d$).** $\bar\mu(t,s)=\sum_{k=0}^{d-1}\mu_t^{(k)}g_k(s-t)$, $g_k(0)=\delta_{k0}$ ($s\ge t$); equivalently $S_\mu$ rational of degree $d$. $d=1$ is Ornstein–Uhlenbeck: $\bar\mu(t,s)=\mu_t e^{-\theta(s-t)}$, $\alpha=\mu/\theta$, $\hat\psi=\sigma\theta/(\theta-i\omega)$.

**D8 (Fractional operators).** Liouville integral $(I^\nu_+f)(t)=\frac{1}{\Gamma(\nu)}\int_{-\infty}^t(t-s)^{\nu-1}f(s)\,ds$, $I^\nu_-$ its reflection, $\nu\in(0,1)$; symbols $(\mp i\omega)^{-\nu}$. Marchaud derivative $D^\nu_\pm=(I^\nu_\pm)^{-1}$, $(D^\nu_\pm f)(t)=\frac{\nu}{\Gamma(1-\nu)}\int_0^\infty\frac{f(t)-f(t\mp s)}{s^{1+\nu}}\,ds$, symbols $(\mp i\omega)^\nu$.

**D9 (Gohberg–Krein factors).** On $[0,T]$: $G_T=$ rate-referred friction $=\eta I+$ integral operator; $G_T=C_-C_+$, $C_+$ causal Volterra with causal inverse, $C_-=C_+^\ast$.

**D10 (Constants).** $c_\beta=2\Gamma(1-\beta)\sin(\pi\beta/2)$ (so $\hat g(\omega)=c_\beta|\omega|^{\beta-1}$ for $g=|t|^{-\beta}$); $\nu=(1-\beta)/2$.

**D11 (Value; nonanticipativity multiplier).** $v=$ adapted value rate (profit per unit time); $v_{\rm ant}=$ value with the whole signal path in hand; causality gap $v/v_{\rm ant}\le1$. $\xi^\star$ = nonanticipativity multiplier: $P_+\xi^\star=0$.

## 2. Assumptions

**(A1) Friction.** $\eta,\gamma,\lambda\ge0$; $g$ locally integrable and positive-definite ($\hat g\ge0$); $\hat n>0$ a.e.; Szegő condition $\int|\log\hat n(\omega)|/(1+\omega^2)\,d\omega<\infty$. (Satisfied by every $\eta,\gamma,\lambda\ge0$ with $g\in\{e^{-\kappa|t|},|t|^{-\beta}\ (0<\beta<1)\}$ and their sums; for $\eta=\lambda=0$, $g=|t|^{-\beta}$, the zero $\hat n\sim\gamma c_\beta|\omega|^{1+\beta}$ at $0$ is log-integrable.)

**(A2) Signal.** $\mu$ stationary, Gaussian, purely non-deterministic, generating its own filtration, with Wold representation $\mu=\psi\ast\dot W$ and $S_\mu=|\hat\psi|^2$, $\hat\psi$ outer. (Special case: Markov of order $d$, D7.)

**(A3) Decay.** $\int(1+\omega^2)S_\mu(\omega)/\hat n(\omega)\,d\omega<\infty$ (rate filter in $L^2$; for the rate-referred power-law form, $\int(1+\omega^2)S_\alpha/\hat q\,d\omega<\infty$).

## 3. Results

### 3.1 Whole line

**R1 (Adapted projected inverse).** Let $A=A_-A_+$ be positive with $A_+$ causal, causal inverse, $A_-=A_+^\ast$ anticausal, anticausal inverse. Then on adapted processes
$$
(P_+AP_+)^{-1}=A_+^{-1}P_+A_-^{-1}.
$$

**R2 (Optimal policy, general adapted signal).** Under (A1) the maximizer of $J$ is unique and
$$
x^\star=N_+^{-1}P_+N_-^{-1}\mu=\big(N_+^{-1}\zeta\big),\qquad \zeta_s=\big(N_-^{-1}\bar\mu(s,\cdot)\big)(s).
$$

**R3 (Nonanticipativity multiplier).** With $x^\star$ from R2,
$$
Nx^\star=\mu-\xi^\star,\qquad \xi^\star=N_-(I-P_+)N_-^{-1}\mu,\qquad P_+\xi^\star=0,
$$
and $\mathbb E\langle x,\xi^\star\rangle=0$ for adapted $x$; the value forgone to adaptedness per unit time is $\tfrac12\mathbb E\langle\xi^\star,N^{-1}\xi^\star\rangle$.

**R4 (Optimal trading filter).** Under (A1)–(A3) and $\lambda>0$: $x^\star=\pi\ast\dot W$ with
$$
\hat\pi=\hat n_+^{-1}[h]_+,\qquad h=\hat\psi\,\hat n_-^{-1},\qquad \hat\chi=(-i\omega)\hat\pi,\qquad v=\tfrac{1}{4\pi}\big\|[h]_+\big\|_{L^2}^2.
$$

**R5 (Markov collapse; Ornstein–Uhlenbeck).** For a Markov signal (D7), $\zeta_s=\sum_{k=0}^{d-1}\rho_k\mu_s^{(k)}=P(\partial)\mu_s$, $\rho_k=(N_-^{-1}g_k)(0)$, and $\hat x^\star=P(-i\omega)\hat\mu/\hat n_+$. For $d=1$ (OU), $P(\partial)=1/\Phi(\theta)$ and
$$
\hat x^\star(\omega)=\frac{\hat\mu(\omega)}{\Phi(\theta)\,\hat n_+(\omega)},\qquad v=\frac{\sigma^2\theta}{4\Phi(\theta)^2},
$$
$\theta^2\sigma^2$ the innovation variance of $\mu$.

**R6 (Anticipative value; causality gap).** For $\lambda>0$,
$$
v_{\rm ant}=\tfrac{1}{4\pi}\int\frac{S_\mu}{\hat n}\,d\omega\ (\ge v),\qquad v_{\rm ant}-v=\tfrac{1}{4\pi}\big\|[h]_-\big\|^2=\tfrac12\mathbb E\langle\xi^\star,N^{-1}\xi^\star\rangle,
$$
$[h]_-$ the anticausal part of $h$.

### 3.2 Power-law kernel ($g=|t|^{-\beta}$, $0<\beta<1$)

**R7 (Rate-referred solution).** At $\lambda=0$ the position is non-stationary; the stationary object is the rate. With $\hat q=\gamma\hat g=\gamma c_\beta|\omega|^{\beta-1}$ and $\hat q_\pm=\hat n_\pm/(\mp i\omega)$, R1 applies to $Q=Q_-Q_+$ and
$$
u^\star=Q_+^{-1}P_+Q_-^{-1}\alpha,\qquad \hat\chi=\hat q_+^{-1}[h_\alpha]_+,\quad h_\alpha=\hat q_-^{-1}\hat\varphi,\quad v=\tfrac{1}{4\pi}\|[h_\alpha]_+\|^2,
$$
finite in $L^2$ at $\lambda=0$; the whitened forecasts agree, $(Q_-^{-1}\bar\alpha(s,\cdot))(s)=(N_-^{-1}\bar\mu(s,\cdot))(s)$.

**R8 (Fractional-derivative policy).** $Q_\pm=(\gamma c_\beta)^{1/2}I^\nu_\pm$, $\nu=(1-\beta)/2$, so
$$
u^\star=\frac{1}{\gamma c_\beta}D^\nu_+\zeta,\qquad \zeta_s=\big(D^\nu_-\bar\alpha(s,\cdot)\big)(s).
$$
OU: $\zeta_s=\theta^\nu\alpha_s$, $u^\star=\dfrac{\theta^\nu}{\gamma c_\beta}D^\nu_+\alpha$, $v=\dfrac{\sigma^2\theta^{-\beta}}{4\gamma c_\beta}$.

**R9 (Position as fractional integral; stationarity).** From R5, $\hat n_+\propto(-i\omega)^{(1+\beta)/2}$, so
$$
\hat x^\star\propto(-i\omega)^{-(1+\beta)/2}\hat\mu,\qquad x^\star\propto I^{(1+\beta)/2}_+\mu,
$$
with spectral density $\propto|\omega|^{-(1+\beta)}S_\mu(\omega)$. The position is stationary iff $\int|\omega|^{-(1+\beta)}S_\mu\,d\omega<\infty$, i.e. $S_\mu(\omega)=o(|\omega|^\beta)$ as $\omega\to0$. For OU, $S_\mu(0)\ne0$: non-stationary (a fractional random walk). Any $\lambda>0$ restores stationarity.

**R10 (Causality gap).** Under pure power-law impact,
$$
\frac{v}{v_{\rm ant}}=\sin\frac{\pi\beta}{2},
$$
independent of the signal.

### 3.3 Finite horizon $[0,T]$

**R11 (Finite-horizon factorization).** $G_T$ is positive; $G_T=C_-C_+$ (D9) exists. R1 applies verbatim, and
$$
u^\star=C_+^{-1}P_+C_-^{-1}\alpha^{\rm eff},\qquad \alpha^{\rm eff}=\alpha+\sum_k\xi_k e_k,
$$
one multiplier $\xi_k$ per linear constraint $\langle e_k,x\rangle=0$ (a process-valued multiplier for $x_T=0$), each confined to its constraint's annihilator.

**R12 (Boundary-layer decay).** Let $u^{\star,T}$, $u^\star$ be the finite-horizon and whole-line optima for the same bounded signal, $d(t)=\min(t,T-t)$. Then
$$
|u^{\star,T}_t-u^\star_t|\le
\begin{cases}
C(\beta)\|\alpha\|_\infty\,d(t)^{-\nu}, & g=|t|^{-\beta},\\
C\|\alpha\|_\infty\,e^{-b_1 d(t)}, & \text{rational }\hat n,\ b_1=\text{slowest zero of }\hat n_+.
\end{cases}
$$

**R13 (Power-law GK factor).** For $g=|t|^{-\beta}$, $\eta=\lambda=0$, the causal factor of $G_T$ is the terminal-anchored Volterra operator
$$
c_+(t,s)=(\gamma c_\beta)^{1/2}\Big(\frac{T-s}{T-t}\Big)^{\!\nu}\frac{(t-s)^{\nu-1}}{\Gamma(\nu)},\qquad 0\le s\le t\le T,\qquad C_-C_+=G_T,
$$
i.e. the whole-line factor $(\gamma c_\beta)^{1/2}I^\nu_+$ conjugated by multiplication by $(T-t)^\nu$. No endpoint atoms.

**R14 (Exponential GK factor).** For $g=e^{-\kappa|t|}$, $\eta=\lambda=0$, $G_T$ has kernel $\gamma e^{-\kappa|t-s|}$ and $G_T=C_-C_+$ with the **local** inverse factors
$$
C_+^{-1}=\frac{1}{\sqrt{2\gamma\kappa}}\,(\partial_t+\kappa),\qquad C_-^{-1}=\frac{1}{\sqrt{2\gamma\kappa}}\,(\kappa-\partial_t),
$$
equivalently the causal Green's function $c_+(t,s)=\sqrt{2\gamma\kappa}\,e^{-\kappa(t-s)}$ ($0\le s\le t\le T$), together with the two Robin endpoint conditions $h'(0)=\kappa h(0)$, $h'(T)=-\kappa h(T)$ carried by rank-one endpoint atoms. More generally a rational symbol with $\hat n_+=\eta^{1/2}\prod_{i=1}^d(b_i-i\omega)/\prod(\kappa_j-i\omega)$ gives $C_+^{-1}=\eta^{-1/2}\prod_i(\partial_t+b_i)$ (up to the pole factors) with $d$ atoms per endpoint.

**R15 (Endpoint anchoring).** The finite-horizon GK factor is the whole-line Wiener–Hopf factor modified only at the endpoints: by a scalar terminal weight $(T-t)^\nu$ for a homogeneous kernel (R13), by rank-one endpoint atoms for a local/rational kernel (R14). In the interior it equals the whole-line factor (R12). Consequently the optimal liquidation is continuous when $g(0)=\infty$ (power-law) and block-plus-continuous when $g(0)<\infty$ (rational).

### 3.4 Recoveries

**R16.**
- **(a) Markowitz** ($\eta=\gamma=0$): $\hat n\equiv\lambda$, $x^\star_t=\mu_t/\lambda$, $v=\theta\sigma^2/4\lambda$.
- **(b) Aim portfolio** ($\gamma=0$): $\hat n_+=\sqrt\eta(a-i\omega)$, $a=\sqrt{\lambda/\eta}$; $u^\star_t=a(\mathrm{aim}_t-x^\star_t)$, $\mathrm{aim}_t=\frac{a}{a+\theta}\frac{\theta\alpha_t}{\lambda}$.
- **(c) Exponential resilience** ($g=e^{-\kappa|t|}$, $\eta=0$): $\hat n_+=\sqrt A(m-i\omega)/(\kappa-i\omega)$, $A=2\kappa\gamma+\lambda$, $m=\kappa\sqrt{\lambda/A}$;
  $x^\star_t=\frac{\kappa+\theta}{A(m+\theta)}\big[\mu_t+(\kappa-m)\int_{-\infty}^t e^{-m(t-s)}\mu_s\,ds\big]$.
- **(d) Two-average** ($g=e^{-\kappa|t|}$, all frictions): $\hat n_+=\sqrt\eta(b_1-i\omega)(b_2-i\omega)/(\kappa-i\omega)$, $b_1^2b_2^2=\lambda\kappa^2/\eta$, $b_1^2+b_2^2=\kappa^2+(2\kappa\gamma+\lambda)/\eta$; $x^\star_t=\frac{1}{\Phi\sqrt\eta}\sum_i w_i\int_{-\infty}^t e^{-b_i(t-s)}\mu_s\,ds$, $w_i=(\kappa-b_i)/(b_j-b_i)$. Degenerations: $\gamma\to0\Rightarrow$ (b); $\eta\to0\Rightarrow$ (c).
- **(e) Block-plus-continuous** (exp, finite horizon): endpoint blocks (R14 atoms) + continuous interior; risk aversion replaces the horizon in the stationary limit (c).
- **(f) U-shape** (power-law, finite horizon, constant signal): $u^\star(t)\propto[t(T-t)]^{(\beta-1)/2}$; continuous (no blocks, $g(0)=\infty$).
- **(g) Fredholm** (power-law, finite horizon, Gaussian Volterra signal): R11 with R13 is the solution operator of the stochastic Fredholm equation; $C_-^{-1}$ is the left-anchored reflection of R13.

## 4. Proofs

**P1 (R1).** Causality of $A_+$ gives $(I-P_+)A_+P_+=0$, so $A_+,A_+^{-1}$ preserve the adapted subspace; adjointness ($A_-=A_+^\ast$) gives $P_+A_-(I-P_+)=0$, so $A_-,A_-^{-1}$ preserve the complement. For adapted $v$, $A_-v=P_+A_-v+(I-P_+)A_-v$; applying $A_-^{-1}$ the second image stays in the complement and $P_+$ kills it, so $P_+A_-^{-1}P_+A_-v=P_+v=v$. Hence for adapted $u$, $A_+^{-1}P_+A_-^{-1}(P_+AP_+)u=A_+^{-1}[P_+A_-^{-1}P_+A_-]A_+u=A_+^{-1}A_+u=u$, using $P_+A_+u=A_+u$. The reverse composition is the identity by positivity of $P_+AP_+$ on the adapted subspace. For unbounded (power-law) factors the identity holds on the dense domain (A3). $\square$

**P2 (R2).** Strict convexity ($\hat n>0$ a.e.) makes the projected first-order condition $P_+NP_+x^\star=\mu$ necessary and sufficient with a unique solution; R1 with $A=N$ inverts it. Forecast form: $N_-^{-1}$ has a deterministic anticausal kernel, so by conditional Fubini $\mathbb E_s[(N_-^{-1}\mu)(s)]$ integrates that kernel against $\mathbb E_s[\mu_r]=\bar\mu(s,r)$, $r\ge s$. $\square$

**P3 (R3).** Apply $N$ to R2: $Nx^\star=N_-P_+N_-^{-1}\mu=\mu-N_-(I-P_+)N_-^{-1}\mu=:\mu-\xi^\star$. Since $N_-$ is anticausal, $(I-P_+)N_-^{-1}\mu$ is strictly anticausal and $N_-$ preserves the anticausal complement, so $P_+\xi^\star=0$; hence $\mathbb E\langle x,\xi^\star\rangle=0$ for adapted $x$. The quadratic loss $J(N^{-1}\mu)-J(x^\star)=\tfrac12\|N^{-1}\mu-x^\star\|_N^2=\tfrac12\mathbb E\langle\xi^\star,N^{-1}\xi^\star\rangle$. $\square$

**P4 (R4).** $N_-^{-1}\mu$ is the stationary filter of $\dot W$ with symbol $h=\hat\psi\hat n_-^{-1}$. Conditioning at $s$ annihilates innovations after $s$, so $P_+$ truncates the MA kernel at lag $0$: it acts as $[\,\cdot\,]_+$. Composing with $N_+^{-1}$ gives $\hat\pi$; for $\lambda>0$, $\hat n$ is bounded below so $h,\hat\pi\in L^2$, and (A3) places $h$ in a Sobolev class on which the half-line indicator multiplies boundedly, giving $\hat\chi\in L^2$. Value: first-order condition and adaptedness give $v=\tfrac12\mathbb E[x^\star_t\mu_t]$; by the Itô isometry with $\overline{\hat\psi}=\hat n_+\overline h$, $\mathbb E[x^\star\mu]=\tfrac1{2\pi}\|[h]_+\|^2$. $\square$

**P5 (R5).** For OU, $\hat\psi=\sigma\theta/(\theta-i\omega)$ and $h-\hat\psi/\Phi(\theta)=\sigma\theta[\hat n_-^{-1}(\omega)-\hat n_-^{-1}(-i\theta)]/(\theta-i\omega)$ is anticausal (the pole at $\omega=-i\theta$ cancels, $\hat n_-^{-1}$ analytic in the lower half-plane, $\hat n_-(-i\theta)=\hat n_+(i\theta)=\Phi$). Hence $[h]_+=\hat\psi/\Phi$, giving R5 and, with $\|\hat\psi\|^2=\pi\sigma^2\theta$, $v=\sigma^2\theta/4\Phi^2$. For general Markov $d$, $[h]_+$ is the sum of the $d$ residues, giving $P(\partial)$. $\square$

**P6 (R6).** Replacing $[\,\cdot\,]_+$ by the identity in R4 gives $v_{\rm ant}=\tfrac1{4\pi}\|h\|^2=\tfrac1{4\pi}\int|\hat\psi|^2/\hat n=\tfrac1{4\pi}\int S_\mu/\hat n$. By orthogonality of causal and anticausal parts, $v_{\rm ant}-v=\tfrac1{4\pi}\|[h]_-\|^2$; and $\tfrac1{4\pi}\|[h]_-\|^2=\tfrac12\mathbb E\langle\xi^\star,N^{-1}\xi^\star\rangle$ since $\hat\xi^\star=\hat n_-[h]_-$ (P3) and $|\hat n_-|^{-2}=\hat n^{-1}$... $|\hat\xi^\star|^2/\hat n=|[h]_-|^2$. $\square$

**P7 (R7).** R1 with $A=Q$ (positive, $Q_\pm$ causal/anticausal with the stated inverses; A3 in rate form). Differentiate R2: $\partial_t\circ N_+^{-1}=Q_+^{-1}$, and on forecast curves $Q_-^{-1}=N_-^{-1}\circ(-\partial_s)$ with $-\partial_s\bar\alpha(s,\cdot)=\bar\mu(s,\cdot)$, so the whitened forecasts coincide. In $L^2$ at $\lambda=0$ by A3. $\square$

**P8 (R8).** $\hat g(\omega)=c_\beta|\omega|^{\beta-1}$ gives $\hat q=\gamma c_\beta|\omega|^{\beta-1}$, whose outer factor is $(\gamma c_\beta)^{1/2}(\mp i\omega)^{-\nu}$, $\nu=(1-\beta)/2$; these are the symbols of $(\gamma c_\beta)^{1/2}I^\nu_\pm$. Inverses are $D^\nu_\pm$, symbols $(\mp i\omega)^\nu$. Substitute in R7; OU value by P5/P10. $\square$

**P9 (R9).** From R5, $\hat x^\star=\hat\mu/(\Phi\hat n_+)$ with $\hat n_+=(\gamma c_\beta)^{1/2}(-i\omega)^{(1+\beta)/2}$, so $\hat x^\star\propto(-i\omega)^{-(1+\beta)/2}\hat\mu$; $|\hat x^\star|^2=|\omega|^{-(1+\beta)}S_\mu$ up to constant. $\int|\hat x^\star|^2\,d\omega<\infty$ iff $|\omega|^{-(1+\beta)}S_\mu$ integrable at $0$ (the tail is controlled by $S_\mu$), i.e. $S_\mu=o(|\omega|^\beta)$. OU: $S_\mu(0)\ne0$, integral diverges. $\square$

**P10 (R10).** Rate forms: $v=\tfrac1{4\pi}\|[h_\alpha]_+\|^2$, $v_{\rm ant}=\tfrac1{4\pi}\|h_\alpha\|^2$, $h_\alpha=\hat q_-^{-1}\hat\varphi=(\gamma c_\beta)^{-1/2}(-i\omega)^\nu\hat\varphi$ ... for OU $\hat\varphi=\sigma/(\theta-i\omega)$. The plus/full norms differ by the argument of $(-i\omega)^{\beta-1}$ across the two half-lines, whose ratio is $\sin(\pi\beta/2)$: with $\hat q_-(-i\theta)\propto\theta^{(1+\beta)/2}$, $v=\sigma^2\theta^{-\beta}/4\gamma c_\beta$ (P8) and $v_{\rm ant}=\sigma^2\theta^{-\beta}/(4\gamma c_\beta\sin(\pi\beta/2))$, ratio $\sin(\pi\beta/2)$. $\square$

**P11 (R11).** $G_T\succ0$ factors triangularly relative to the nest of adapted subspaces (Gohberg–Krein / Arveson): $G_T=C_-C_+$, $C_+$ causal Volterra. R1 with $A=G_T$ inverts $P_+G_TP_+$. Each linear constraint adds a Lagrange multiplier that modifies the signal within the constraint's annihilator, exactly as $\xi^\star$ does for adaptedness (P3). $\square$

**P12 (R12).** R11 differs from R2 through the terminal-anchored weight and truncation of the factor kernels to $[0,T]$. Power-law (R13): truncation cuts the Marchaud tail at distance $d(t)$, cost $d(t)^{-\nu}$; the weight deviation $((T-s)/(T-t))^\nu=1+O(1/d(t))$ is subdominant. Rational: $\hat n_+^{-1}$ has kernel $\sim e^{-b_1\tau}$, truncation at $d(t)$ costs $e^{-b_1d(t)}$; feedback gains relax at rate $2b_1$. $\square$

**P13 (R13).** Direct integration $\int_0^T c_+(u,t)c_+(u,s)\,du=\gamma c_\beta\,\Gamma(\nu)^{-2}(T-t)^{-\nu}(T-s)^{-\nu}\int_{t\vee s}^T(T-u)^{2\nu}(u-t)^{\nu-1}(u-s)^{\nu-1}\,du=\gamma e^{-... }$; the Beta-type integral evaluates to $\gamma c_\beta\,\Gamma(\nu)^2\Gamma(1-2\nu)^{-1}...\,|t-s|^{-\beta}$ (using $2\nu=1-\beta$, $c_\beta=2\Gamma(1-\beta)\sin(\pi\beta/2)$), reproducing $C_-C_+=G_T$ including the constant. The factor is $I^\nu_+$ conjugated by $(T-t)^\nu$: homogeneity of $(t-s)^{\nu-1}$ makes the anchoring a scalar weight, and R11's placement of $C_+$ on the right forces the terminal anchor. $\square$

**P14 (R14).** For $E_\kappa$ with kernel $e^{-\kappa|t-s|}$: $(\kappa^2-\partial_t^2)(E_\kappa f)=2\kappa f$ on $(0,T)$, with $(E_\kappa f)'(0)=\kappa(E_\kappa f)(0)$ and $(E_\kappa f)'(T)=-\kappa(E_\kappa f)(T)$ (differentiate the kernel and evaluate). Hence $(\gamma E_\kappa)^{-1}=(2\gamma\kappa)^{-1}(\kappa^2-\partial_t^2)$ with these Robin conditions. Since $\partial_t^\ast=-\partial_t$, $\kappa^2-\partial_t^2=(\kappa-\partial_t)(\kappa+\partial_t)=(\kappa+\partial_t)^\ast(\kappa+\partial_t)$, so $(\gamma E_\kappa)^{-1}=C_+^{-1}(C_+^{-1})^\ast$ with $C_+^{-1}=(2\gamma\kappa)^{-1/2}(\partial_t+\kappa)$, $C_-^{-1}=(2\gamma\kappa)^{-1/2}(\kappa-\partial_t)$; $C_+^{-1}$ is causal (forward innovation of the OU Green's function), the two Robin conditions realized as rank-one endpoint terms. Its inverse has kernel $\sqrt{2\gamma\kappa}\,e^{-\kappa(t-s)}$. Verified numerically: the reverse-Cholesky factor of $e^{-\kappa|t-s|}$ has interior kernel $\sqrt{2\kappa}\,e^{-\kappa(t-s)}$ and bidiagonal inverse $\approx(2\kappa)^{-1/2}(\partial_t+\kappa)$. The order-$d$ case factors $\prod_i(b_i^2-\partial^2)$ analogously. $\square$

**P15 (R15).** R13 exhibits the homogeneous case (scalar weight, no atoms); R14 the local/rational case (differential factor, endpoint atoms). In both the interior operator is the whole-line factor, which is P12. An atom in $C_+$ at an endpoint is a jump in $x$ there; a jump costs $\propto g(0)$, finite for $g=e^{-\kappa|t|}$ and infinite for $g=|t|^{-\beta}$, so atoms occur iff $g(0)<\infty$. $\square$

**P16 (R16).** Each is a specialization of R5/R11. (a) $\hat n\equiv\lambda$, $\hat n_+=\sqrt\lambda$, $\Phi=\sqrt\lambda$. (b) $\hat n=\lambda+\eta\omega^2=\eta(a^2+\omega^2)$, one zero $a$; $\hat n_+^{-1}$ a single exponential, differentiation gives partial adjustment. (c) $\hat n=\lambda+2\gamma\kappa\omega^2/(\kappa^2+\omega^2)=A(m^2+\omega^2)/(\kappa^2+\omega^2)$; one zero $m$, one pole $\kappa$. (d) $\hat n=\lambda+2\gamma\kappa\omega^2/(\kappa^2+\omega^2)+\eta\omega^2$; two zeros $b_1,b_2$, one pole $\kappa$; the stated symmetric functions of $b_i$ from equating coefficients. Degenerations by pole–zero cancellation. (e)–(g) from R11 with R14/R13: constant signal makes $P_+$ trivial; (g) matches the Fredholm solution operator via the Neumann expansion summed by the factors. $\square$
