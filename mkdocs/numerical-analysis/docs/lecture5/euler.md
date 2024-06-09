
### 背景

实际上，我们很少使用 Euler 法，但是它简单的推导方法可用于说明如何构造一些更高级的方法，而在构造过程中不需要繁琐的代数运算。

Euler 法的目的是获得适定的初值问题

$$
\frac{\mathrm{d}y}{\mathrm{d}t}=f( t ,y ) ,\quad a\leqslant t\leqslant b ,\quad y( a )=\alpha 
$$

的近似解。

实际上，我们并不会得到解 $y(t)$ 的一个连续的近似解；而是在区间 $[a, b]$ 内的不同点（称为网格点）产生 $y$ 的近似解。一旦在这些点获得了近似解，在此区间内的其他点的近似解可以通过插值获得。

### 具体步骤

首先，我们将区间 $[a, b]$ 分成 $n$ 个子区间，每个子区间的长度为 $h = (b - a) / n$。我们将在 $t_i = a + i h$ 处计算 $y_i$ 的近似解，其中 $i = 0, 1, 2, \ldots, n$。

我们将使用 Taylor 定理来推导 Euler 法。假设 $y(t)$ 具有足够多的连续导数，我们可以将 $y(t)$ 在 $t = t_i$ 处展开为

$$
y(t_{i+1})=y(t_{i})+(t_{i+1}-t_{i})y^{\prime}(t_{i})+\frac{(t_{i+1}-t_{i})^{2}}{2}y^{\prime\prime}(\xi_{i})
$$

因为 $y^{\prime}(t) = f(t, y(t))$，我们可以将上式写为

$$
y(t_{i+1})=y(t_{i})+hf(t_{i},y(t_{i}))+\frac{h^{2}}{2}y^{\prime\prime}(\xi_{i})
$$

Euler 法通过消去余项构造 $w_{i}\approx y( t_{i} )( i=1,2,\cdots,N)$。因而，我们可以有

$$
\begin{aligned}
w_0 &= \alpha \\
w_{i + 1} &= w_i + hf(t_i, w_i), i = 0, 1, \cdots, N - 1
\end{aligned}
$$

所以我们可以看出来，Euler 方法其实是很不精确的，因为直接舍弃了误差项。

### 误差分析

#### 引理 5.7

对所有的 $x \geq -1$ 和任何正整数 $m$，有 $0 \leq (1+x)^{m} \leq e^{mx}$

#### 引理 5.8

如果 $s$ 和 $t$ 是正实数，$\{a_i\}_{i = 0}^{k}$ 是满足 $a_0 \geq -t / s$ 和

$$
a_{i + 1} \leq (1+s)a_i + t, i = 0, 1, \cdots, k
$$

的一个序列，则

$$
a_{i + 1} \leq e^{(i + 1)s}(a_0 + \frac{t}{s}) - \frac{t}{s}
$$

#### 定理 5.9

假设 $f$ 是连续的，且在 $D=\{(t,y)|a\leqslant t\leqslant b,-\infty<_y<\infty\}$ 上满足常数为 L 的 Lipschitz 条件，又假设存在常数 M 使得

$$|y^{\prime\prime}(t)|\leqslant M$$

对一切 $t\in[a,b]$成立。设 y(t)表示初值问题

$$y^{\prime}=f(t,y),\quad a\leqslant t\leqslant b,\quad y(a)=\alpha$$

的唯一解，$w_0,w_1,...,w_N$是由 Euler 法对某个正整数 N 产生的近似。则对于 $i=0,1,2,\cdots,N$, 有

$$
\mid y(t_{i})-w_{i}\mid\leqslant\frac{hM}{2L}[\mathrm{e}^{L(t_{i}-a)}-1\:]
$$
 
这一个定理的不足之处是我们需要解的二阶导数的界是已知的。但是我们可以通过求偏导的脸是法则来转换得到这个界。

