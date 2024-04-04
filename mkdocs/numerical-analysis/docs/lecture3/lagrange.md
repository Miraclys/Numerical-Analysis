
因为 Taylor 多项式不适于插值，所以我们需要探讨别的方法。

### 定理

#### 定理 3.2

如果 $x_0,x_1,...,x_n$是$n+1$ 个不同的点且函数 $f$ 在这些点处的函数值是已知的， 则唯一存在一个次数不超过 n 的多项式 $P(x)$满足

$$
f(x_k)=P(x_k),\quad k=0,1,\cdots,n
$$

这个多项式由下式给出

$$
P(x)=f(x_0)L_{n,0}(x)+\cdots+f(x_n)L_{n,n}(x)=\sum_{k=0}^nf(x_k)L_{n,k}(x)
$$

这里，对每一个$k=0,1,\cdots,n$,有

$$
L_{n,k}(x)=\frac{(x-x_0)(x-x_1)\cdotp\cdotp\cdotp(x-x_{k-1})(x-x_{k+1}^{'})\cdotp\cdotp\cdotp(x-x_n)}{(x_k-x_0)(x_k-x_1)\cdotp\cdotp\cdotp(x_k-x_{k-1})(x_k-x_{k+1})\cdotp\cdotp\cdotp(x_k-x_n)}
$$
  
当和它的次数不发生混淆时，将$L_{n,k}(x)$简写为 $L_k(x_0)$

### 误差

下面给出拉格朗日插值法逼近函数的余项或者说误差。由下面的定理给出

#### 定理3.3

假设 $x_0,x_1,...,x_n$是区间$[a,b]$内的不同的点且 $f\in C^{n+1}[a,b]$,则对$[a,b]$内的每个$x$,在$(a,b)$内存在一点 $\xi(x)$使得

$$
f(x)=P(x)+\frac{f^{(x+1)}(\xi(x))}{(n+1)!}(x-x_0)(x-x_1)\cdotp\cdotp\cdotp(x-x_n)
$$
 
关于这一个误差的公式的证明，是构造了一个辅助函数，好像很多公式的误差分析都可以这样来构造，见 http://staff.ustc.edu.cn/~rui/ppt/num/num-interpolation-hermite.html 中对于 Hermite 插值误差项的分析和数学分析课本上对于 Taylor 公式的误差分析。

这一个误差公式是一个重要的理论结果，因为 Lagrange 多项式广泛地用于导出数值微分和数值积分方法，这些方法的误差界根据 Lagrange 误差公式得到。

和 Taylor 公式的误差项相比，Lagrange 多项式的误差项使用了 $n + 1$ 个点的信息。

### 递归求 Lagrange 多项式

用 Lagrange 插值的一个实际困难在于因为误差项不易应用，所以在进行实际计算之前为达到精度要求所需的多项式次数通常是未知的。一般的做法是计算根据不同的多项式得出的结果直到获得合适的一致性为止。所以，我们现在想获得一种可以充分利用低次 Lagrange 多项式来求解高次 Lagrange 多项式的方法。

#### 定理 3.5

设 $f$ 在$x_0,x_1,\cdotp\cdotp\cdotp,x_k$有定义，又设 $x_j$ 和$x_i$是这个集合中的两个不同的数，则

$$
P(x)=\frac{(x-x_j)P_{0,1,\cdots,j-1,j+1,\cdots,k}(x)-(x-x_i)P_{0,1,\cdots,i-1,i+1,\cdots,k}(x)}{(x_i-x_j)}
$$

描述了对 $f$在$k+ 1$ 个点 $x_0,x_1,\cdotp\cdotp\cdotp,x_k$插值的k 次 Lagrange 多项式（证明可以直接自己使用 Lagrange 插值的定义推导一遍）。

这一个定理说明 Lagrange 插值多项式可以通过递归的方式产生。这一个递归的过程称为 **Neville 方法**

为了避免复杂的下标（$P$ 的下标比较繁琐），我们使用 $Q_{i, j}(0 \leq j \leq i)$ 表示在 $(j + 1)$ 个点 $x_{i - j}, x_{i - j + 1}, ..., x_{i - 1}, x_i$ 上次数为 $j$ 的插值多项式，即

$$
Q_{i, j} = P_{i - j, i - j + 1, ..., i - 1, i}
$$

