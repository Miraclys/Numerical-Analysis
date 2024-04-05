
### n + 1 点公式

一个显然的方法是我们可以通过比较小的 $h$ 通过 $\dfrac{f(x_0 + h) - f(x_0)}{h}$ 来近似点 $x_0$ 处的导数。

但是这样我们对于「误差」的大小并没有一个度量。

我们可以通过 Lagrange 多项式来构造函数的插值多项式，然后进行求导，就可以获得导数的多项式表示以及误差分析。

$$
\begin{aligned}
f^{\prime}(x)& =\frac{f(\left.x_0+h\right.)-f(\left.x_0\right.)}h+D_x\left[\frac{(\left.x-x_0\right.)(\left.x-x_0-h\right.)}2f^{\prime\prime}(\left.\xi(x)\right)\right] \\
&=\frac{f(x_0+h)-f(x_0)}h+\frac{2(x-x_0)-h}2f^{\prime\prime}(\boldsymbol{\xi}(x)) \\
&+\frac{(x-x_0)(x-x_0-h)}2D_x(f^{\prime\prime}(\xi(x)))
\end{aligned}
$$

但是，这样有一个困难是我们并没有关于 $D_x(f^{\prime\prime}(\xi(x)))$ 的相关信息，所以不能估计截断误差，但是，当 $x = x_0$ 的时候，这一项的系数是 0，所以对于我们给定点的导数来说，有

$$
f^{\prime}(x_0)=\frac{f(x_0+h)-f(x_0)}h-\frac h2f^{\prime\prime}(\xi)
$$

同样的，我们可以对于这一个公式进行推广，推广到 k 次的 Lagrange 多项式的形式。

$$
\begin{aligned}f^{\prime}(x)&=\sum_{k=0}^nf(x_k)L^{\prime}_k(x)+D_x\left[\frac{(x-x_0)\cdotp\cdotp\cdotp(x-x_n)}{(n+1)!}\right]f^{(n+1)}(\boldsymbol{\xi}(x))\\&+\frac{(\left.x-x_0\right)\cdotp\cdotp\cdotp(\left.x-x_n\right)}{\left(n+1\right)!}D_x\left[f^{(n+1)}\left(\boldsymbol{\xi}(x)\right)\right]\end{aligned}
$$

同样，我们缺乏对于 $D_x[f^{(n+1)}(\xi(x))]$ 的信息，所以无法估计截断误差。但是对于给定的点 $x_i$ 其系数为 0，所以有

$$
f^{\prime}(x_j)=\sum_{k=0}^nf(x_k)L^{\prime}{}_k(x_j)+\frac{f^{(n+1)}(\boldsymbol{\xi}(x_j))}{(n+1)!}\prod_{k\neq j}^n(x_j-x_k)
$$

这一个公式称为逼近 $f^{'}(x_j)$ 的 $(n + 1)$ 点公式。

### 三点公式和五点公式

一般来讲，上面的公式使用的求值点越多，产出的结果越准确，即a使函数求值的树木和舍入误差的增长是这一个过程不尽人意。最普通的还是三个点和五个点的求值公式。

对于三点公式，有两个公式

$$
\begin{aligned}
f^{\prime}\left(x_0\right)=\frac1{2h}\left[-3f\left(x_0\right)+4f\left(x_0+h\right)-f\left(x_0+2h\right)\right]+\frac{h^2}3f^\text{(3)}{ \left ( \xi _ 0 \right )} \\
f^{\prime}(x_0)=\frac1{2h}[f(x_0+h)-f(x_0-h)]-\frac{h^2}6f^{(3)}(\xi_1)
\end{aligned}
$$

同样，一个五点公式是

$$
f^{\prime}(x_0)=\frac1{12h}[\left.f(x_0-2h)-8f(x_0-h)+8f(x_0+h)-f(x_0+2h)\right.]+\frac{h^4}{30}f^{(5)}(\xi)
$$

### 高阶导数近似

高阶导数近似的推导在代数上比较冗长，一个有代表性的做法是使用 Taylor 多项式来推导。

将函数 $f$ 在点 $x_{0}$展开为三阶 Taylor 多项式，并求在 $x_0+h$ 和$x_0-h$ 处的值。则有

$$
f(x_0+h)=f(x_0)+f^{\prime}(x_0)h+\frac12f^{\prime\prime}(x_0)h^2+\frac16f^{\prime\prime\prime}(x_0)h^3+\frac1{24}f^{(4)}(\xi_1)h^4
$$

和

$$
f(x_0-h)=f(x_0)-f^{\prime}(x_0)h+\frac12f^{\prime\prime}(x_0)h^2-\frac16f^{\prime\prime\prime}(x_0)h^3+\frac1{24}f^{(4)}(\xi_{-1})h^4
$$

将这两个方程相加，就可以得到

$$
f^{\prime\prime}(x_0)=\frac1{h^2}[f(x_0-h)-2f(x_0)+f(x_0+h)]-\frac{h^2}{24}[f^{(4)}(\xi_1)+f^{(4)}(\xi_{-1})]
$$

由介值定理，又可以得到

$$
f^{\prime\prime}(x_0)=\frac1{h^2}[f(x_0-h)-2f(x_0)+f(x_0+h)]-\frac{h^2}{12}f^{(4)}(\xi)
$$

### 误差分析

数值微分中一个非常重要的部分就是研究舍入误差在近似过程中的影响。


$$
f^{\prime}(x_0)=\frac1{2\overline{h}}[f(x_0+h)-f(x_0-h)]-\frac{h^2}6f^{(3)}(\xi_1)
$$

假设在求 $f(x_0+h)$和$f(x_0-h)$的值时，遇到了舍人误差 $e\left(x_0+h\right)$和$e\left(x_0-h\right)$。则计算出的值$\tilde{f}(x_0+h)$和$\tilde{f}(x_0-h)$与实际值$f(x_0+h)$和$f(x_0-h)$的关系由下面的公式表示

$f(x_0+h)=\tilde{f}(x_0+h)+e(x_0+h)$
和

$$
f(x_0-h)=\tilde{f}(x_0-h)+e(x_0-h)
$$

近似的总误差

$$
f^{\prime}\left(x_0\right)-\frac{\tilde{f}\left(x_0+h\right)-\tilde{f}\left(x_0-h\right)}{2h}=\frac{e\left(x_0+h\right)-e\left(x_0-h\right)}{2h}-\frac{h^2}6f^{\left(3\right)}\left(\xi_1\right)
$$

部分是由于舍入误差，部分是由于截断误差。如果摄入误差以某一个 $\epsilon$ 为界，函数的三阶导数以 $M$ 为界，则有

$$
\left.\left|f^{\prime}\left(x_0\right.\right)-\frac{\tilde{f}\left(\left.x_0+h\right.\right)-\tilde{f}\left(\left.x_0-h\right.\right)}{2h}\right|\leqslant\frac\varepsilon h+\frac{h^2}6M
$$

所以，这是一个综合调控误差的过程。因为如何为了减小截断误差，必须减小 $h$，但是 $h$ 减小时，舍入误差 $\epsilon / h$ 增大。

实际上，人们不能获取上面在微分计算的过程中最优的 $h$，因为我们并不知道三阶导数。但是我们必须清楚，减小步长并不总是改进近似计算。

微分中，产生问题的原因在于需要使用 $h$ 的幂相除，但是用小数相除趋于使舍入误差增大，这种操作应该尽可能避免。在数值微分的情况下，完全避免这一个问题是不可能的，尽管高阶方法使这方面的计算困难减小。

所以说，数值微分的近似方法是一种「不稳定」方法，因为减小截断误差意味着增大舍入误差。

