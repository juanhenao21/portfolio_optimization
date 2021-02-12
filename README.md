# Portfolio Optimization

## Correlation between stocks

Consider time series $S_{k} \left( t \right)$, $k = 1, 2, \ldots, K$ of stock prices for $K$ companies.
The values $S_{k} \left( t \right)$ are taken in fixed time steps $\Delta t$.

In general, the data contain an exponential increase due to the drift. Thus, to measure the correlations
independently of this trend, it is better to use logarithmic differences instead of returns.

$$G_{k} \left( t \right) = \ln S_{k} \left( t + \Delta t \right) - \ln S_{k} \left(t \right) = \ln \frac{S_{k} \left( t + \Delta t \right)}{S_{k} \left(t \right)}$$

Anyway, logarithmic differences and returns almost coincide if the time steps $\Delta t$ are sufficiently short.

The mean of the logatihmic differences reads

\leftangle G_{k} \left( t \right) \rightangle = \frac{1}{T} \sum_{t = 1}^{T} G_{k} \left( t \right)

To compare the different $K$ companies, it is necessary to normalize the time series. The normalized time
series are defined by

$$M_{k} \left( t \right) =  \frac{G_{k} \left( t \right) - \leftangle G_{k} \left( t \right) \rightangle}{\sqrt{\leftangle G_{k}^{2} \left( t \right) \rightangle} - \leftangle G_{k} \left( t \right) \rightangle^2}$$

These values can be viewed as the elements of a $K \times T$ (companies times lenght of time) rectangular
matrix $M$. With these normalizations and rescalings, it can be measured correlations in such a way that
all companies and all stocks are treated on equal footing.
