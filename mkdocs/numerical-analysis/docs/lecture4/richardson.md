
### 背景

Richardson 用于产生高精度的结果，可是它使用低阶的公式。

具体来说，理查德森外推法用了不同步长下数值解的线性组合来逼近精确解。假设有某个数值方法对于步长为 $h$ 的近似解 $N(h)$，那么该方法对于步长为 $h / 2$ 的近似解可以表示为 $N(h / 2)$。理查森外推法通过对这些近似解进行适当的加权组合，能够有效地减少计算误差，从而获得更为精确的结果。

每当我们的截断误差有下面的形式

$$
\sum_{j=1}^{m-1}K_jh^{\alpha_j}+O\left(h^{\alpha_m}\right)
$$

对于一组常数 $K_j$ 和当 $\alpha_1 < \alpha_2 < ... < \alpha_m$ 成立时，就可以使用外推法。

### 朴素例子

考虑逼近 $M$ 的形如下式的公式

$$
M=N(h)+K_1h+K_2h^2+K_3h^3+\cdots 
$$

因为上述的 $h$ 对于所有的正数都成立，所以我们可以考虑使用 $h / 2$ 来替换 $h$，则有公式

$$
M=N\left(\frac h2\right)+K_1\frac h2+K_2\frac{h^2}4+K_3\frac{h^3}8+\cdots
$$

两个式子处理后相减可以得到

$$
M=\left[\left.N\left(\frac h2\right)+\left(N\left(\frac h2\right)-N\left(h\right)\right)\right]+K_2\left(\frac h2-h^2\right)+K_3\left(\frac h4-h^3\right)+\cdots\right. 
$$

我们可以发现，其实和我们初始时规定的逼近 $M$ 的形式是一致的。为了方便起见，我们规定

$$
\begin{aligned}
N_1(h_2)&\equiv N(h_2) \\
N_2\left(h\right.)&=N_1\left(\frac h2\right)+\left[N_1\left(\frac h2\right)-N_1\left(h\right)\right]
\end{aligned}
$$

从而，对于 $M$ 有 $O(h^{2})$ 的逼近公式

$$
M=N_2\left(h\right.)-\frac{K_2}2h^2-\frac{3K_3}4h^3-\cdots 
$$

同样的套路，我们可以得到

$$
M=\left[N_2\left(\frac h2\right)+\frac{N_2\left(h/2\right)-N_2\left(h\right)}3\right]+\frac{K_3}8h^3+\cdots 
$$

通过定义 $N_3\left(h\right.)\equiv N_2\left(\frac h2\right)+\frac{N_2\left(h/2\right)-N_2\left(h\right)}3$，我们又可以得到 $M$ 的 $O(h^{3})$ 的近似公式。如此递推下去。

一般地，如果 $M$ 可以写成形如

$$
M=N(h_1)+\sum_{j=1}^{m-1}K_jh^j+O(h^m)
$$

则对于$j=2,3,\cdots,m$,有形如下式的$O(h^j)$通近公式

$$
N_j\left(h\right.)=N_{j-1}\left(\frac h2\right)+\frac{N_{j-1}\left(h/2\right)-N_{j-1}\left(h\right)}{2^{j-1}-1}
$$

我们可以通过这一个过程构造一个外推表。其中第一列是 $N_1(h)、N_1(h / 2)、N_2(h / 4) ...$。后面的 $N_2、N_3...$ 这些其实都是前面一列的求一个加权平均。所以，本质上讲我们只需要求解第一列的值。

### 误差

通过外推表我们可以发现，除第一列以外的其余各列是用简单的平均过程得到的，所以这一个方法可以使用最小计算成本产出高阶近似。但是，当 $k$ 增加时，在 $N_1(h / 2^{k})$ 中的舍入误差一般将增加，因为数值微分的不稳定性与步长 $h / 2^{k}$ 有关。

### 再看 n+1 点公式

在上一节，我们通过给定函数 $f$ 不同的函数值，讨论了关于求解 $f^{'}(x_0)$ 的近似值的三点和五点方法。

我们当时的求解过程是通过求 $f$ 的 Lagrange 插值多项式的微分推导出来的。但是对于点越来越多的情况，这种推导方式是冗长的，外推法可以更加容易地导出这些公式。

> 这一部分的一个思路是，通过 Taylor 多项式，得到一个 $f^{'}(x_0)$ 的形式，但是这一个形式相比 Lagrange 插值多项式求导得到的形式，为止的求值点 $\xi$ 是在 $f^{(5)}$ 处，多了一项 $f^{'''}(x_0)$，所以可以使用外推法来缩写误差项，感觉很神奇