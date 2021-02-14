# Portfolio Optimization

## Correlation between stocks

Consider time series $S_{k} \left( t \right)$, $k = 1, 2, \ldots, K$ of stock
prices for $K$ companies. The values $S_{k} \left( t \right)$ are taken in
fixed time steps $\Delta t$.

In general, the data contain an exponential increase due to the drift. Thus, to
measure the correlations independently of this trend, it is better to use
logarithmic differences instead of returns.

$$
G_{k} \left( t \right) = \ln S_{k} \left( t + \Delta t \right) - \ln S_{k} \left(t \right)
                       = \ln \frac{S_{k} \left( t + \Delta t \right)}{S_{k} \left(t \right)}
$$

Anyway, logarithmic differences and returns almost coincide if the time steps
$\Delta t$ are sufficiently short.

The mean of the logarithmic differences reads

$$
\left\langle G_{k} \left( t \right) \right\rangle =
\frac{1}{T} \sum_{t = 1}^{T} G_{k} \left( t \right)
$$

To compare the different $K$ companies, it is necessary to normalize the time
series. The normalized time series are defined by

$$
M_{k} \left( t \right) =
\frac{G_{k} \left( t \right) - \left\langle G_{k} \left( t \right) \right\rangle}
{\sqrt{\left\langle G_{k}^{2} \left( t \right) \right\rangle - \left\langle G_{k} \left( t \right) \right\rangle^2}}
$$

These values can be viewed as the elements of a $K \times T$ (companies times
length of time) rectangular matrix $M$. With these normalizations and
rescalings, it can be measured correlations in such a way that all companies
and all stocks are treated on equal footing.

The correlation coefficient for the stocks $k$ and $l$ is defined as

$$
C_{kl} = \left\langle M_{k} \left( t \right) M_{l} \left( t \right) \right\rangle
       = \frac{1}{T} \sum_{t=1}^{T} M_{k} \left( t \right) M_{l} \left( t \right)
$$

$$
C_{kl} =
\frac{\left\langle G_{k} \left( t \right) G_{l} \left( t \right) \right\rangle
      - \left\langle G_{k} \left( t \right) \right\rangle
        \left\langle G_{l} \left( t \right) \right\rangle}
{\sqrt{\left\langle G_{k}^{2} \left( t \right) \right\rangle - \left\langle G_{k} \left( t \right) \right\rangle^2}
\sqrt{\left\langle G_{l}^{2} \left( t \right) \right\rangle - \left\langle G_{l} \left( t \right) \right\rangle^2}}
$$

The coefficients $C_{kl}$ are the elements of a $K \times K$ square matrix $C$,
the correlation matrix. The limiting values of these correlation coefficients

$$
C_{kl}^{\text{lim}} =
\left\{ \begin{array}{cc}
+1 & \text{completely correlated}\\
0 & \text{completely uncorrelated}\\
-1 & \text{completely anticorrelated}
\end{array}\right.
$$

The time average of $C_{kl}$ can be viewed as the matrix product of the
rectangular matrix $M$ ($K \times T$) with its transpose matrix $M^{\dagger}$
($T \times K$), divided by $T$. Thus, the correlation matrix can be written in
the form

$$
C = \frac{1}{T} M M^{\dagger}
$$

The correlation matrix $C$ is real and symmetric.