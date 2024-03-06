#### Fixed Point Method

本节将讨不动点问题的解以及不动点和将要解决的求根问题之间的关系。

虽然我们要求解的问题以求根的形式出现，但是不同点的形式更加易于分析，且某些不动点的选取会导出非常有效的求根方法。

#### 定理

##### 定理2.3.1



##### 定理2.3.2


#### 不动点迭代

我们无法显式直接求解出一个不动点，但是却可以逼近它。可以先选择一个初始值 $p_0$，之后对于每一个 $n \geq 1$，利用 $p_n = g(p_{n - 1})$ 产生一个数列 $\{p_n\}_{n = 0}^{\infty}$。如果这一个数列收敛到 $p$，并且 $g$ 是连续的，则

$$
p = \lim\limits_{n \to \infty} p_n = \lim\limits_{n \to \infty} g(p_{n - 1}) = g\left(\lim\limits_{n \to \infty} p_{n - 1}\right) = g(p)
$$

$x = g(x)$ 的一个解就得到了。这种方法叫做 **不动点迭代** 或者 **泛函迭代**。

#### 定理

##### 定理2.3.4

##### 推论2.3.5

对于 $p_n$ 近似误差的估计。两个公式。