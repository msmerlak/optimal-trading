# No-Dynamic-Arbitrage and Market Impact

> Source: https://pdfs.semanticscholar.org/3683/ecb4dae470f4df219d65bb6491d3c7fd4b78.pdf
> Pages: 47
> Author: Jim Gatheral

---

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion No-Dynamic-Arbitrage and Market Impact Jim Gatheral Ecole Polytechnique January 5, 2009

<!-- Page 2 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Market impact and its estimation Our aim is to make a connection between the shape of the market impact function and the decay of market impact. Market impact is estimated in practice by aggregating all executions of a certain type, for example all VWAP executions. We will assume that price impacts are estimated as unconditional averages. We average over different market conditions. We average buys and sells (with appropriate sign adjustments). This accurately mimics the estimation of market impact functions in practice (cf Almgren 2005 for example).

<!-- Page 3 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Model setup We suppose that the stock price S t at time t is given by S t = S 0 + ∫ t 0 f ( ˙ x s ) G ( t − s ) ds + ∫ t 0 σ dZ s (1) where ˙ x s is our rate of trading in dollars at time s < t , f ( ˙ x s ) represents the impact of trading at time s and G ( t − s ) is a decay factor. S t follows an arithmetic random walk with a drift that depends on the accumulated impacts of previous trades. The cumulative impact of (others’) trading is implicitly in S 0 and the noise term. Drift is ignored. Drift is a lower order effect. We are averaging buys and sells.

<!-- Page 4 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Model setup continued We refer to f ( · ) as the instantaneous market impact function and to G ( · ) as the decay kernel. (1) is a generalization of processes previously considered by Almgren, Bouchaud and Obizhaeva and Wang. (1) corresponds to the “bare propagator” formulation of Bouchaud et al. rather than the state-dependent formulation of Farmer, Lillo et al.

<!-- Page 5 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Model as limit of discrete time process The continuous time process (1) can be viewed as a limit of a discrete time process (see Bouchaud et al. for example): S t = ∑ i < t f ( δ x i ) G ( t − i ) + noise where δ x i = ˙ x i δ t is the quantity traded in some small time interval δ t characteristic of the stock, and by abuse of notation, f ( · ) is the market impact function. δ x i > 0 represents a purchase and δ x i < 0 represents a sale. δ t could be thought of as 1 /ν where ν is the trade frequency. Increasing the rate of trading ˙ x i is equivalent to increasing the quantity traded each δ t .

<!-- Page 6 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Price impact and slippage The cost of trading can be decomposed into two components: The impact of our trading on the market price (the mid-price for example). We refer to this effect as price impact . Frictions such as effective bid-ask spread that affect only our execution price. We refer to this effect as slippage . For small volume fractions, we can think of slippage as being proxied by VWAP slippage. In what follows, we will neglect slippage. The inequality relationships we derive will all be weakened in practice to the extent that slippage becomes important.

<!-- Page 7 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Cost of trading Denote the number of shares outstanding at time t by x t . Then from (1), neglecting slippage, the cost C [Π] associated with a given trading strategy Π = { x t } is given by C [Π] = ∫ T 0 ˙ x t dt ∫ t 0 f ( ˙ x s ) G ( t − s ) ds (2) The dx t = ˙ x t dt shares liquidated at time t are traded at a price S t = S 0 + ∫ t 0 f ( ˙ x s ) G ( t − s ) ds which reflects the residual cumulative impact of all prior trading.

<!-- Page 8 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Almgren et al. In our notation, the temporary component of Almgren’s model corresponds to setting G ( t − s ) = δ ( t − s ) and f ( v ) = η σ v β with β = 0 . 6. In this model, temporary market impact decays instantaneously. Our trading affects only the price of our own executions; other executions are not affected. The cost of trading becomes: C [Π] = ∫ T 0 ˙ x t dt ∫ t 0 f ( ˙ x s ) G ( t − s ) ds = η σ ∫ T 0 ˙ x 1+ β t dt where V is the average daily volume.

<!-- Page 9 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Obizhaeva and Wang In the setup of Obizhaeva and Wang, we have G ( t − s ) = exp {− ρ ( t − s ) } and f ( v ) ∝ v . In this model, market impact decays exponentially and instantaneous market impact is linear in the rate of trading. The cost of trading becomes: C [Π] = ∫ T 0 ˙ x t dt ∫ t 0 f ( ˙ x s ) G ( t − s ) ds ∝ ∫ T 0 ˙ x t dt ∫ t 0 ˙ x s exp {− ρ ( t − s ) } ds

<!-- Page 10 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Bouchaud et al. In the setup of Bouchaud et al., we have f ( v ) ∝ log( v ) and G ( t − s ) ∝ l 0 ( l 0 + t − s ) β with β ≈ (1 − γ ) / 2 where γ is the exponent of the power law of autocorrelation of trade signs. In this model, market impact decays as a power law and instantaneous market impact is concave in the rate of trading. The cost of trading becomes: C [Π] = ∫ T 0 ˙ x t dt ∫ t 0 f ( ˙ x s ) G ( t − s ) ds ∝ ∫ T 0 ˙ x t dt ∫ t 0 log( ˙ x s ) ( l 0 + t − s ) β ds

<!-- Page 11 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion The principle of No Dynamic Arbitrage A trading strategy Π = { x t } is a round-trip trade if ∫ T 0 ˙ x t dt = 0 We define a price manipulation to be a round-trip trade Π whose expected cost C [Π] is negative. The principle of no-dynamic-arbitrage Price manipulation is not possible. Corollary Pump and dump schemes cannot make money on average

<!-- Page 12 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Pump and Dump Schemes (From http://www.sec.gov/answers/pumpdump.htm) Definition “Pump and dump” schemes, also known as “hype and dump manipulation”, involve the touting of a company’s stock (typically microcap companies) through false and misleading statements to the marketplace. After pumping the stock, fraudsters make huge profits by selling their cheap stock into the market.

<!-- Page 13 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion $50M ’pump-and-dump’ scam nets 20 arrests By Greg Farrell, USA TODAY NEW YORK Mob influence on Wall Street might be waning. FBI swoops down on Wall Street Mob June 15, 2000 The FBI arrested 20 men Thursday morning on charges of running a massive pump-and-dump scheme that defrauded thousands of investors out of more than $50 million. Two alleged ringleaders Hunter Adams and Michael Reiter are said to be associates of the Gambino organized crime family.

<!-- Page 14 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Permanent impact Suppose we trade into a position at the rate + v and out at the same − v . If market impact is permanent, without loss of generality, G ( · ) = 1 and the cost of trading becomes C [Π] = v f ( v ) { ∫ T / 2 0 dt ∫ t 0 ds − ∫ T T / 2 dt ∫ T / 2 0 ds } + v f ( − v ) ∫ T T / 2 dt ∫ t T / 2 ds = v T 2 8 {− f ( − v ) − f ( v ) } If f ( v ) 6 = − f ( − v ), price manipulation is possible. No-dynamic-arbitrage thus imposes that if market impact is permanent, f ( v ) = − f ( − v ). We henceforth assume that f ( v ) = − f ( − v ).

<!-- Page 15 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion A specific strategy Consider a strategy where shares are accumulated at the (positive) constant rate v 1 and then liquidated again at the (positive) constant rate v 2 . According to equation (2), the cost of this strategy is given by C 11 + C 22 − C 12 with C 11 = v 1 f ( v 1 ) ∫ θ T 0 dt ∫ t 0 G ( t − s ) ds C 22 = v 2 f ( v 2 ) ∫ T θ T dt ∫ t θ T G ( t − s ) ds C 12 = v 2 f ( v 1 ) ∫ T θ T dt ∫ θ T 0 G ( t − s ) ds (3) where θ is such that v 1 θ T − v 2 ( T − θ T ) = 0 so θ = v 2 v 1 + v 2

<!-- Page 16 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Special case: Trade in and out at the same rate One might ask what happens if we trade into, then out of a position at the same rate v . If G ( · ) is strictly decreasing, C [Π] = v f ( v ) { ∫ T / 2 0 dt ∫ t 0 G ( t − s ) ds + ∫ T T / 2 dt ∫ t T / 2 G ( t − s ) ds − ∫ T T / 2 dt ∫ T / 2 0 G ( t − s ) ds } = v f ( v ) { ∫ T / 2 0 dt ∫ t 0 [ G ( t − s ) − G ( t + T / 2 − s )] ds + ∫ T T / 2 dt ∫ t T / 2 [ G ( t − s ) − G ( T − s )] ds } > 0 We conclude that if there is arbitrage, it must involve trading in and out at different rates.

<!-- Page 17 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Exponential decay Suppose that the decay kernel has the form G ( τ ) = e − ρ τ Then, explicit computation of all the integrals in (3) gives C 11 = v 1 f ( v 1 ) 1 ρ 2 { e − ρ θ T − 1 + ρ θ T } C 12 = v 2 f ( v 1 ) 1 ρ 2 { 1 + e − ρ T − e − ρ θ T − e − ρ (1 − θ ) T } C 22 = v 2 f ( v 2 ) 1 ρ 2 { e − ρ (1 − θ ) T − 1 + ρ (1 − θ ) T } (4) We see in particular that the no-arbitrage principle forces a relationship between the instantaneous impact function f ( · ) and the decay kernel G ( · ).

<!-- Page 18 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Exponential decay After making the substitution θ = v 2 / ( v 1 + v 2 ) and imposing the principle of no-dynamic-arbitrage, we obtain v 1 f ( v 1 ) [ e − v 2 ρ v 1 + v 2 − 1 + v 2 ρ v 1 + v 2 ] + v 2 f ( v 2 ) [ e − v 1 ρ v 1 + v 2 − 1 + v 1 ρ v 1 + v 2 ] − v 2 f ( v 1 ) [ 1 + e − ρ − e − y 1 ρ v 1 + v 2 − e − v 2 ρ v 1 + v 2 ] ≥ 0 (5) where, without loss of generality, we have set T = 1. We note that the first two terms are always positive so arbitrage can occur only if the third term dominates the others.

<!-- Page 19 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Example: f ( v ) = √ v Let v 1 = 0 . 2 , v 2 = 1 , ρ = 1. Then the cost of liquidation is given by C = C 11 + C 22 − C 12 = − 0 . 001705 < 0 Since ρ really represents the product ρ T , we see that for any choice of ρ , we can find a combination { v 1 , v 2 , T } such that a round trip with no net purchase or sale of stock is profitable. We conclude that if market impact decays exponentially, no arbitrage excludes a square root instantaneous impact function. Can we generalize this?

<!-- Page 20 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Expansion in ρ Expanding expression (5) in powers of ρ , we obtain v 1 v 2 [ v 1 f ( v 2 ) − v 2 f ( v 1 )] ρ 2 2( v 1 + v 2 ) 2 + O ( ρ 3 ) ≥ 0 We see that arbitrage is always possible for small ρ unless f ( v ) is linear in v . Taking the limit ρ → 0 + , we obtain Corollary Non-linear permanent market impact is inconsistent with the principle of no-dynamic-arbitrage.

<!-- Page 21 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Exponential decay of market impact and arbitrage Lemma If temporary market impact decays exponentially, price manipulation is possible unless f ( v ) ∝ v . Empirically, market impact is concave in v for small v . Also, market impact must be convex for very large v Imagine submitting a sell order for 1 million shares when there are bids for only 100,000. We conclude that the principle of no-dynamic-arbitrage excludes exponential decay of market impact for any reasonable instantaneous market impact function f ( · ).

<!-- Page 22 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Linear permanent market impact If f ( v ) = η v for some η > 0 and G ( t − s ) = 1, the cost of trading becomes C [Π] = η ∫ T 0 ˙ x t dt ∫ t 0 ˙ x s ds = η 2 ( x T − x 0 ) 2 The trading cost per share is then given by C [Π] | x T − x 0 | = η 2 | x T − x 0 | which is independent of the details of the trading strategy (depending only on the initial and final positions) and linear in the net trade quantity.

<!-- Page 23 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Power-law decay Suppose now that the decay kernel has the form G ( t − s ) = 1 ( t − s ) γ , 0 < γ < 1 Then, explicit computation of all the integrals in (3) gives C 11 = v 1 f ( v 1 ) T 2 − γ (1 − γ ) (2 − γ ) θ 2 − γ C 22 = v 2 f ( v 2 ) T 2 − γ (1 − γ ) (2 − γ ) (1 − θ ) 2 − γ C 12 = v 2 f ( v 1 ) T 2 − γ (1 − γ ) (2 − γ ) { 1 − θ 2 − γ − (1 − θ ) 2 − γ } (6)

<!-- Page 24 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Power-law decay According to the principle of no-dynamic-arbitrage, substituting θ = v 2 / ( v 1 + v 2 ), we must have f ( v 1 ) { v 1 v 2 1 − γ − ( v 1 + v 2 ) 2 − γ + v 1 2 − γ + v 2 2 − γ } + f ( v 2 ) v 1 2 − γ ≥ 0 (7) If γ = 0, the no-arbitrage condition (7) reduces to f ( v 2 ) v 1 − f ( v 1 ) v 2 ≥ 0 so again, permanent impact must be linear. If γ = 1, equation (7) reduces to f ( v 1 ) + f ( v 2 ) ≥ 0 So long as f ( · ) ≥ 0, there is no constraint on f ( · ) when γ = 1.

<!-- Page 25 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion The limit v 1 ≪ v 2 and 0 < γ < 1 In this limit, we accumulate stock much more slowly than we liquidate it. Let v 1 = ǫ v and v 2 = v with ǫ ≪ 1. Then, in the limit ǫ → 0, with 0 < γ < 1, equation (7) becomes f ( ǫ v ) { ǫ − (1 + ǫ ) 2 − γ + ǫ 2 − γ + 1 } + f ( v ) ǫ 2 − γ ∼ − f ( ǫ v ) (1 − γ ) ǫ + f ( v ) ǫ 2 − γ ≥ 0 so for ǫ sufficiently small we have f ( ǫ v ) f ( v ) ≤ ǫ 1 − γ 1 − γ (8) If the condition (8) is not satisfied, price manipulation is possible by accumulating stock slowly, maximally splitting the trade, then liquidating it rapidly.

<!-- Page 26 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Power-law impact: f ( v ) ∝ v δ If f ( v ) ∼ v δ (as per Almgren et al.), the no-dynamic-arbitrage condition (8) reduces to ǫ 1 − γ − δ ≥ 1 − γ and we obtain Small v no-dynamic-arbitrage condition γ + δ ≥ 1

<!-- Page 27 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Log impact: f ( v ) ∝ log( v / v 0 ) v 0 should be understood as a minimum trading rate. One could think of one share every trade as being the minimum rate. For example, for a stock that trades 10 million shares a day, 10,000 times, the average trade size is 1,000. That implies v 0 = 0 . 10%. Noting that log v = lim δ → 0 v δ − 1 δ , we would guess that there is arbitrage for all γ < 1. In practice, it depends on how small v 0 is. For example, substituting v 0 = 0 . 001, v 1 = 0 . 15, v 2 = 1 . 0 and γ = 1 / 2 into the arbitrage condition (7) with f ( v ) = log( v / v 0 ) gives a negative cost ( i.e. manipulation). Formally, for every γ < 1, we can find v 0 small enough to allow price manipulation.

<!-- Page 28 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Cost of VWAP with power-law market impact and decay From equation (6), the cost of an interval VWAP execution with duration T is proportional to C = v f ( v ) T 2 − γ Noting that v = n / ( VT ), and putting f ( v ) ∝ v δ , the impact cost per share is proportional to v 1+ δ T 1 − γ = ( n V ) δ T 1 − γ − δ If γ + δ = 1, the cost per share is independent of T and in particular, if γ = δ = 1 / 2, the impact cost per share is proportional to √ n / V , which is the well-known square-root formula for market impact as described by, for example, Grinold and Kahn.

<!-- Page 29 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion A heuristic derivation of the square-root market impact formula Suppose each trade impacts the mid-log-price of the stock by an amount proportional to √ n i where n i is the size of the i th trade. Then the change in mid-price over one day is given by ∆ P = N ∑ i η ǫ i √ n i where η is the coefficient of market impact, ǫ i is the sign of the i th trade and N is the (random) number of trades in a day. Note that both the number of trades and the size of each trade in a given time interval are random.

<!-- Page 30 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Derivation continued If N , ǫ i and n i are all independent, the variance of the one-day price change is given by σ 2 := Var(∆ P ) = η 2 E [ N ] E [ n i ] = η 2 V where V is the average daily volume. It follows that | ∆ P i | = η √ n i = σ √ n i V which is the familiar square-root market impact formula.

<!-- Page 31 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Why √ n ? An inventory risk argument: A market maker requires an excess return proportional to the risk of holding inventory. Risk is proportional to σ √ T where T is the holding period. The holding period should be proportional to the size of the position. So the required excess return must be proportional to √ n .

<!-- Page 32 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion The square-root formula, γ and δ The square-root market impact formula has been widely used in practice for many years. If correct, this formula implies that the cost of liquidating a stock is independent of the time taken. Fixing market volume and volatility, impact depends only size. We can check this prediction empirically. See for example Engle, Ferstenberg and Russell, 2008. Also, according to Almgren, δ ≈ 0 . 6 and according to Bouchaud γ ≈ 0 . 4. Empirical observation δ + γ ≈ 1!

<!-- Page 33 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Bouchaud’s power-law decay argument As before, assume that over one day ∆ P = N ∑ i η ǫ i √ n i The previous heuristic proof of the square-root model assumed that Cov[ ǫ i , ǫ j ] = 0 if i 6 = j and that all market impact is permanent. Empirically, we find that autocorrelation of trade signs shows power-law decay with a small exponent α (very slow decay).

<!-- Page 34 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Bouchaud’s power-law decay argument continued Var[∆ P ] = η 2 Var [ N ∑ i ǫ i √ n i ] = η 2    N Var[ √ n i ] + ∑ i 6 = j Cov[ ǫ i , ǫ j ]    ≈ η 2 { N Var[ √ n i ] + 2 C 1 (2 − α ) (1 − α ) E [ √ n ] 2 N 2 − α } ∼ N 2 − α as N → ∞ Empirically, we find that, to a very good approximation, Var[∆ P ] ∝ N . Otherwise returns would be serially correlated. The only way to reconcile these observations is to have market impact decay as a power law.

<!-- Page 35 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Computation of daily variance with power-law decay Assuming market impact decays as 1 / T γ , we have Var[∆ P ] = η 2 Var [ N ∑ i ǫ i √ n i ( N − i ) γ ] = η 2 { N − 1 ∑ i E [ n ] ( N − i ) 2 γ +2 C 1 N − 1 ∑ i =1 N − 1 ∑ j = i +1 E [ √ n ] 2 ( N − i ) γ ( N − j ) γ ( j − i ) α    ∼ N 2 − α − 2 γ as N → ∞ ∼ N only if γ ≈ (1 − α ) / 2 . For the French stocks considered by Bouchaud et al., the exponent α ≈ 0 . 2 so γ ≈ 0 . 4.

<!-- Page 36 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion The shape of the order book Bouchaud, M´ ezard and Potters (2002) derive the following approximation to the average density ρ ( ˆ ∆) of orders as a function of a rescaled distance ˆ ∆ from the price level at which the order is placed to the current price: ρ ( ˆ ∆) = e − ˆ ∆ ∫ ˆ ∆ 0 du sinh( u ) u 1+ μ + sinh( ˆ ∆) ∫ ∞ ˆ ∆ du e − u u 1+ μ (9) where μ is the exponent in the empirical power-law distribution of new limit orders.

<!-- Page 37 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Approximate order density The red line is a plot of the order density ρ ( ˆ ∆) with μ = 0 . 6 (as estimated by Bouchaud, M´ ezard and Potters). 0 2 4 6 8 10 0.0 0.5 1.0 1.5 ∆ ^ ρ ( ∆ ^ )

<!-- Page 38 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Virtual price impact Switching x − and y − axes in a plot of the cumulative order density gives the virtual impact function plotted below. The red line corresponds to μ = 0 . 6 as before. 0 2 4 6 8 10 Quantity: ⌠ ⌡ 0 ∆ ^ ρ ( u ) du Price impact: ∆ ^

<!-- Page 39 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Impact for high trading rates You can’t trade more than the total depth of the book so price impact increases without limit as n → n max . For a sufficiently large trading rate v , it can be shown that f ( v ) ∼ 1 (1 − v / v max ) 1 /μ Setting v = v max (1 − ǫ ) and taking the limit ǫ → 0, f ( v ) ∼ 1 ǫ 1 /μ as ǫ → 0 . Imagine we accumulate stock at a rate close to v max := 1 and liquidate at some (lower) rate v . This is the pump and dump strategy!

<!-- Page 40 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Impact for high trading rates continued Substituting into condition (7) gives 1 ǫ 1 /μ { (1 − ǫ ) v 1 − γ − (1 − ǫ + v ) 2 − γ + (1 − ǫ ) 2 − γ + v 2 − γ } + f ( v ) (1 − ǫ ) 2 − γ ≥ 0 We observe that arbitrage is possible only if h ( v , γ ) := v 1 − γ − (1 + v ) 2 − γ + 1 + v 2 − γ < 0 This can be shown to be equivalent to the condition: γ < γ ∗ := 2 − log 3 log 2 ≈ 0 . 415 So if γ > γ ∗ , there is no arbitrage.

<!-- Page 41 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion More on high trading rates It turns out that h ( v , γ ) decreases as v → v max (= 1) so the arbitrage is maximized near v = v max . However, we already know that there is no arbitrage when trading in and out at the same rate. A careful limiting argument nevertheless shows that arbitrage is still possible in principle for every γ < γ ∗ . We deduce that, independent of the particular exponent μ in the power law of limit order arrivals, the no-arbitrage condition is: Large size no arbitrage condition γ > γ ∗ = 2 − log 3 log 2

<!-- Page 42 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Summary Bouchaud et al. have previously noted that the market self-organizes in a subtle way such that the exponent γ of the power law of decay of market impact and the exponent α of the decay of autocorrelation of trade signs balance to ensure diffusion (variance increasing linearly with time). γ ≈ (1 − α ) / 2 By imposing the principle of no-dynamic-arbitrage we showed that if the market impact function is of the form f ( v ) ∝ v δ , we must have γ + δ ≥ 1 We excluded various other combinations of functional forms for market impact and decay such as exponential decay with nonlinear market impact.

<!-- Page 43 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Summary continued We then observe that if the average cost of a (not-too-large) VWAP execution is roughly independent of duration, the exponent δ of the power law of market impact should satisfy: δ + γ ≈ 1 By considering the tails of the limit-order book, we deduce that γ ≥ γ ∗ := 2 − log 3 log 2 ≈ 0 . 415 Finally, we note that empirical estimates are γ ≈ 0 . 4 (Bouchaud et al.) and δ ≈ 0 . 6 (Algren et al.) Our no-dynamic-arbitrage principle links these observations!

<!-- Page 44 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Constraint on α Assuming that autocorrelation of order signs is a long-memory process, we get γ = 1 − α 2 In particular, we must have γ ≤ 1 / 2. Combining this with γ > γ ∗ , we obtain α ≤ 1 − 2 γ ∗ ≈ 0 . 17 Faster decay is ruled out by no-dynamic-arbitrage.

<!-- Page 45 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Schematic presentation of results 0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 γ δ 0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 γ + δ ≥ 1 γ ≥ γ * γ ≤ 1 2 γ = 0.4 , δ = 0.6 γ = 0.5 , δ = 0.5

<!-- Page 46 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion Concluding remarks The ability of no-dynamic-arbitrage principles to explain patterns in empirical observations is related to the self-organizing properties of markets with heterogenous agents, specifically statistical arbitrageurs. Agents will act so as to cancel any local trend in the observed price series, ensuring that the autocorrelation of returns is zero to a good approximation: that is, ensuring that variance varies linearly with time. Agents continuously monitor the reaction of market prices to volume, trading to take advantage of under- or over-reaction, ensuring that on average, it costs money to trade stock.

<!-- Page 47 -->

Model Setup Dynamic arbitrage Exponential decay Power-law decay Market impact Very large size Conclusion References Robert Almgren, Chee Thum, Emmanuel Hauptmann, and Hong Li. Equity market impact. Risk , July:57–62, July 2005. Jean-Philippe Bouchaud, Yuval Gefen, Marc Potters, and Matthieu Wyart. Fluctuations and response in financial markets: the subtle nature of ‘random’ price changes. Quantitative Finance , 4:176–190, April 2004. Jean-Philippe Bouchaud, Marc M´ ezard, and Marc Potters. Statistical properties of stock order books: empirical results and models. Quantitative Finance , 2:251–256, August 2002. Robert F. Engle, Robert Ferstenberg, and Jeffrey Russell. Measuring and modeling execution cost and risk. Technical report, University of Chicago Graduate School of Business, 2008. J. Doyne Farmer, Austin Gerig, Fabrizio Lillo, and Szabolcs Mike. Market efficiency and the long-memory of supply and demand: is price impact variable and permanent or fixed and temporary? Quantitative Finance , 6:107–112, April 2006. Richard C. Grinold and Ronald N. Kahn. Active Portfolio Management . New York: The McGraw-Hill Companies, Inc., 1995. Anna Obizhaeva and Jiang Wang. Optimal trading strategy and supply/demand dynamics. Technical report, MIT Sloan School of Management, 2005.