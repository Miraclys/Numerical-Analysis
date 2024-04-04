
前一节利用迭代插值，讨论了在一些指定点上逐次产生高次的多项式逼近。这一节介绍差商，它用于逐次产生多项式本身。

### 差商插值

假设$P_n(x)$是与函数$f$在不同的点$x_0, x_1, \cdotp \cdotp , x_n$一致的n 次 Lagrange 多项式。$f$关于$x_0, $ $x_1,\cdotp\cdotp\cdotp,x_n$的差商被用于将$P_n(x)$表为下面的形式

$$
\begin{aligned}
P_n\left(x\right)=a_0+a_1\left(x-x_0\right)+a_2\left(x-x_0\right)\left(x-x_1\right)+ \\ \cdotp\cdotp \cdotp+a_n(x-x_0)(x-x_1)\cdotp\cdotp\cdotp(x-x_{n-1})
\end{aligned}
$$
 
其中，$a_0,a_1,\cdots,a_n$为适当的常数。

我们可以通过逐个代入 $x_0, x_1, ..., x_n$ 来获得系数 $a$。其中，系数 $a_k$ 其实就是 $k$ 阶差商。 

对于 $k$ 阶差商，由下面的式子给出定义

$$
f[\left.x_i,x_{i+1},\cdots,x_{i+k-1},x_{i+k}\right.]=\frac{f[\left.x_{i+1},x_{i+2},\cdots,x_{i+k}\right.]-f[\left.x_i,x_{i+1},\cdots,x_{i+k-1}\right]}{x_{i+k}-x_i}
$$

所以，上面的 $P_n$ 可以写为

$$
P_n(x)=f[\left.x_0\right]+\sum_{k=1}^nf[\left.x_0,x_1,\cdots,x_k\right](\left.x-x_0\right)\cdotp\cdotp\cdotp(\left.x-x_{k-1}\right)
$$

这一个公式，称为差商型 Newton 插值公式。

### 定理

#### 定理 3.6

设 $f{\in}C^n[a,b]$且 $x_0,x_1,\cdotp\cdotp,x_n$ 为$[a,b]$内的不同点。则在$(a,b)$内存在一点 $\xi$ 使得

$$
f[x_0,x_1,\cdots,x_n]=\frac{f^{(n)}(\xi)}{n!}
$$

### 等距时的不同形式

当插值节点为等距的情形时，Newton 差商公式可以表示成更简单的形式。

注意阿特金方法和差商符号之间的关系

### 牛顿插值的特点

牛顿插值法的特点在于：每增加一个点，不会导致之前的重新计算，只需要算和新增点有关的就可以了。

