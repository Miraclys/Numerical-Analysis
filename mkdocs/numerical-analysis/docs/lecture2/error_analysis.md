
本节讨论函数式迭代法的收敛阶以及作为得到快速收敛的一个工具，重新发现 Newton 迭代法。考虑在一些特殊的情况下加速 Newton 法收敛的方法。

### 序列收敛快慢的度量

假设$\{p_n\}_{n=0}^{\infty}$是收敛于 p 的一个序列，其中$p_n\neq p$(对所有的 $n$)。如果存在正常数 $\alpha$ 和 $\lambda$ 使得
$$
\lim\limits_{n \to \infty} \dfrac{|p_{n + 1} - p|}{|p_{n} - p|^{\alpha}} = \lambda
$$
成立，则$\{p_n\}_{n=0}^{\infty}$以阶$\alpha$收敛于$p$,且渐近误差常数为$\lambda$。

二次收敛序列通常比仅仅线性收敛的序列收敛快得多，但是产生收敛序列的许多方法仅线性收敛。

### 定理

#### 定理 2.7

设 $g\in C[a,b]$且 $g(x)\in[a,b]$对所有 $x\in[a,b]$成立。又假设 $g^{\prime}$在$(a,b)$连续且存在正常数 $k<1$ 使得

$$|g^{\prime}(x)|\leqslant k$$
对所有 $x\in(a,b)$成立。如果 $g^{\prime}(p)\neq0$ ,则对$[a,b]$内的任何点 $p_{0}$ ,序列

$$
p_n = g(p_{n - 1}), \quad n \geq 1
$$

仅线性收敛于 $[a, b]$ 内的唯一不动点 $p（证明见 P87）。

证明过程中，我们可以得到：

$$
\lim\limits_{n \to \infty} \dfrac{p_{n + 1} - p}{p_n - p} = \lim\limits_{n \to \infty} g^{'}(\xi_{n}) = g^{'}(p)
$$

这说明，不动点方法的高阶收敛性仅当 $g^{'}(p) = 0$ 时发生。

#### 定理 2.8

设 p 是方程 $x=g(x)$的解。假设 $g^{\prime}(p)=0$ ,在含 p 的开区间 I 上 $g^{\prime\prime}$是连续的且严格地以 $M$ 为界。则存在一个 $\delta>0$ ,使得对 $p_{0}\in[p-\delta,p+\delta]$,由 $p_{i}=g(p_{n-1})$所定义的序列(当 $n{\geqslant}1$ 时)至少二次收敛于 p。另外，对充分大的 n 值还有

$$
|p_{n + 1} - p| < \dfrac{M}{2}|p_n - p|^{2}
$$

### 构造

通过上面收敛性的启发，我们尝试构造高阶收敛的迭代方式。一个容易想到的思路是构造一个不动点问题，从 $x$ 中减去 $f(x)$ 的倍数。考虑

$$
p_n = g(p_{n - 1}), \quad n \geq 1
$$

这里的 $g$ 具有形式

$$
g(x) = x - \phi(x)f(x)
$$

其中，$\phi(x)$ 是以后选取的可微函数。为了使 $g$ 导出的迭代法是二次收敛的，需要在 $f(p) = 0$ 时有 $g^{'}(p) = 0$。这样可以推得 $\phi(p) = 1 / f^{'}(p)$。所以，简便来取，我们可以直接令 $\phi(x) = \dfrac{1}{f^{'}(x)}$，这就是 Newton 迭代法。

### 多重零点

处理多重根问题的一个方法是定义

$$
\mu(x) = \dfrac{f(x)}{f^{'}(x)}
$$

此时，$p$ 就变为了 $\mu$ 的单重零点，对 $\mu$ 就可以再去使用朴素的 Newton 的迭代了。

会得到迭代式子

$$
g(x) = x - \dfrac{f(x)f^{'}(x)}{[f^{'}(x)]^{2} - f(x)f^{''}(x)}
$$

理论上，这一个方法的唯一缺点时附加的对 $f^{''}(x)$ 的计算和迭代过程中的更多计算。但是实际上，多重根会引起严重的误差舍入问题时因为上式中的分母由两个接近于 0 的数之差组成。

还有改进是 Halley's Method 和 Schroder Method？https://en.wikipedia.org/wiki/Halley's_method