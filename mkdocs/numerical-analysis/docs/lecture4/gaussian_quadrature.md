
### 背景

Guss 求积以最优的方式而不是等距的方式选择求值点。选取区间 $[a, b]$ 内的节点 $x_1, x_2, ..., x_n$ 和系数 $c_1, c_2, ..., c_n$，使得在近似

$$
\int_a^{b}f(x)\mathrm{d}x = \sum\limits_{i = 1}^{n}c_if(x_i)
$$

中所得到的误差最小。

### 定理

#### 定理 4.7

假设 $x_1, x_2, ..., x_n$ 是 $n$ 次 Legendre 多项式 $P_n(x)$ 的根，又假设对 $i = 1, 2, ..., n$ 数 $c_i$ 定义为 

$$
c_i = \int_{-1}^{1}\prod\limits_{j = 1, j \neq i}^{n}\frac{x - x_j}{x_i - x_j}\mathrm{d}x
$$

如果 $P(x)$ 是任何次数小于 $2n$ 的多项式，则

$$
\int_{-1}^{1} P(x) \mathrm{d}x = \sum\limits_{i = 1}^{n}c_i P(x_i)
$$

