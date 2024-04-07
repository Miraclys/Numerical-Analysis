
### 背景

对于没有显式原函数或者原函数不容易得到的函数，在求解它的定积分的时候，我们经常使用

$$
\sum\limits_{i = 0}^{n} a_i f(x_i)
$$

来近似求解 $\int_a^{b}f(x)\mathrm{d}x$ 的值。

本节介绍的方法是以前面的插值多项式为基础来近似求解积分。

对于 $n + 1$ 个点的 Lagrange 插值多项式和截断误差在 $[a, b]$ 上进行积分，得到

$$
\begin{aligned}
\int_{a}^{b}f( x )\mathrm{d}x& =\int_{a}^{b} \sum_{i=0}^{n} f\big( x_{i} \big)L_{i} \big( x \big)\mathrm{d}x+\int_{a}^{b} \prod_{i=0}^{n} \big( x-x_{i} \big)\frac{f^{(n+1)} \big( \xi( x ) \big)}{\big( n+1 \big) !}\mathrm{d}x \\
&= \sum_{i=0}^{n} a_{i}f\bigl( x_{i} \bigr)+\frac{1}{\bigl( n+1 \bigr)!}\int_{a}^{b} \prod_{i=0}^{n} \bigl( x-x_{i} \bigr)f^{\bigl( n+1 \bigr)} \bigl( \xi\bigl( x \bigr) \bigr)\mathrm{d}x
\end{aligned}
$$

在讨论求积公式的一般情况之前，我们先考虑用等距节点的一次和二次 Lagrange 多项式所产生的公式，也就是基础的梯形公式(Trapezoidal Rule)和 Simpson 公式。

### Trapezoidal Rule

$$
\int_{a}^{b}f( x ) \mathrm{d}x=\frac{h}{2}\Big[ f\big( x_{0}\big)+f\big( x_{1}\big) \Big]-\frac{h^{3}}{12}f^{\prime\prime}( \xi )
$$

（推导过程中运用了积分的中值定理）

因为梯形公式的误差项包含了二阶导数，所以对于二阶导数恒为 0 的任何函数，梯形公式都是精确的。

### Midpoint Rule

我们可以使用 Taylor 多项式的方式来推导中点法则。我们使用二阶的 Taylor 多项式，然后进行定积分，可以得到一个 $O(h^{3})$ 的中点法则。

$$
\int_{x_0}^{x_1}f(x)\mathrm{d}x = hf(\frac{x_0 + x_1}{2}) + \frac{h^3}{24}f^{''}(\xi)
$$

我们可以发现，中点法则的误差项比梯形法则的误差项要小，尽管梯形法则使用了更多的点。这是因为中点法则使用了更高阶的 Taylor 多项式。

### Simpson's Rule

按照上面的思路，通过对于 Lagrange 插值多项式以及误差项进行积分，我们可以得到 Simpson 公式。但是，这一种方式只能得到包含 $f^{(3)}$ 的 $O(h^{4})$ 误差项。

$$
\begin{equation}
\begin{aligned}
\int_{a}^{b}f(x) \,dx = & \int_{x_{0}}^{x_{2}} \left[ \frac{(x-x_{1})(x-x_{2})}{(x_{0}-x_{1})(x_{0}-x_{2})}f(x_{0}) \right. \\
& + \frac{(x-x_{0})(x-x_{2})}{(x_{1}-x_{0})(x_{1}-x_{2})}f(x_{1}) \\
& + \left. \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} f(x_2) \right] dx \\
& + \int_{x_0}^{x_2}\frac{(x - x_0)(x - x_1)(x - x_2)}{6} f^{(3)}(\xi(x)) \,dx,
\end{aligned}
\end{equation}
$$

其中的最后一项误差，因为是三次的 x 项，所以说正负无法判断，没有办法使用积分的中值定理来进行进一步简化。

我们使用三阶的 Taylor 多项式，然后进行定积分，可以得到一个 $O(h^{5})$ 的 Simpson 公式。

$$
\int_{x_{0}}^{x_{2}}f( x ) \mathrm{d}x=2hf( x_{1} )+\frac{h^{3}}{3}f^{\prime\prime}( x_{1} )+\frac{f^{( 4 )}( \xi_{1} )}{60}h^{5}
$$

其中，$f^{''}(x_1)$ 我们可以通过前面所说的使用 Taylor 公式来求解。

最后使用这一种方式，Simpson 法则可以化简为

$$
\int_{x_{0}}^{x_{2}}f( x ) \mathrm{d}x=\frac{h}{3}\Big[ f\big( x_{0}\big)+4f\big( x_{1}\big)+f\big( x_{2}\big) \Big]-\frac{h^{5}}{90}f^{(4)} ( \xi )
$$

### Newton-Cotes

梯形法则和 Simpson 法则都是 Newton-Cotes 公式的一类方法的例子。有两种类型的 Newton-Cotes 公式，开的和闭的。

#### 误差分析

