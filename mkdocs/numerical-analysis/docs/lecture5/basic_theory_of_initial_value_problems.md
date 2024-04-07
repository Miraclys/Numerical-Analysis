
### 定义

#### 定义 5.1

函数 $f(t,y)$称为关于集合 $D\subset\mathbb{R}^2$上的变量 y 满足 Lipschitz 条件，如果存在一个常数 L>0 使得

$$
\mid f(\:t\:,y_{1})-f(\:t\:,y_{2})\mid\leqslant L\mid y_{1}-y_{2}\mid 
$$

对所有$(t,y_1),(t,y_2)\in\mathcal{D}$ 都成立。常数 L 称为$f$ 的 Lipschitz 常数。  

#### 定义 5.2

集合 $D\subset\mathbb{R}^2$称为是凸的，如果只要当$(t_1,y_1)$和$(t_2,y_2)$属于 $D$ 且$\lambda$ 在[0,1]中时，就有点$((1-\lambda)t_1+\lambda t_2,(1-\lambda)y_1+\lambda y_2)$也属于 $D$ 。

#### 定理 5.3

假设 $f(t,y)$定义在凸集 $D\subset\mathbb{R}^2$上。如果存在一个常数 L >0 使得

$$
|\frac{\partial f}{\partial y}(t, y)| \leq L
$$
  
对一切$(t,y)\in D$ 成立，则 $f$ 在$D$ 上关于变量 y 满足 Lipschitz 常数为 $L$ 的 Lipschitz 条件。

#### 定理 5.4

假设 $D=\{(t,y)|a\leqslant t\leqslant b,-\infty<y<\infty\}$,且 $f(t,y)$在 $D$ 上连续。如果 $f$在 $D$ 上关于变量 $y$ 满足 Lipschitz 条件，则初值问题

$$
y^{\prime}(t)=f(t,y),\quad a\leqslant t\leqslant b,\quad y(a)=\alpha 
$$

对 $a \leq t \leq b$ 有唯一解 $y(t)$

我们已经在某种程度上考虑了初值问题何时具有唯一解的问题，现在我们转到另一个问题：如何确定在问题语句中小的变化（或摄动）对应地引起解的小变化？

#### 定义 5.5

初值问题

$$
\frac{\mathrm{d}y}{\mathrm{d}t}=f( t ,y ) ,\quad a\leqslant t\leqslant b ,\quad y( a )=\alpha 
$$

称为是一个**适定的问题**，如果：

1. 问题存在一个唯一的解 $y(t)$
2. 对任何 $\epsilon > 0$，存在一个正整数 $k(\epsilon)$，使得只要当 $|\epsilon_0| < \epsilon$，$\delta(t)$ 是连续的且在 $[a, b]$ 上 $|\delta(t)| < \epsilon$ 时，就有问题

$$
\frac{\mathrm{d}z}{\mathrm{d}t}=f( t ,z )+\delta( t ) ,\quad a\leqslant t\leqslant b ,\quad z( a )=\alpha+\varepsilon_{0}
$$

存在唯一解 $z(t)$，且

$$
\mid z(t)-y(t)\mid<k(\varepsilon)\varepsilon 
$$

对一切 $a \leq t \leq b$ 成立。

因为表示式中的任何舍入误差都使原问题摄动，所以数值方法总与求解摄动问题有关。

#### 定理 5.6

假设 $D=\{(t,y)|a\leqslant t\leqslant b,-\infty<y<\infty\}$。如果 $f$ 是连续的，且在 $D$ 上关于变量 y 满足 Lipschitz 条件，则初值问题

$$
\frac{\mathrm{d}y}{\mathrm{d}t}=f(\:t\:,y\:)\:,\quad a\leqslant t\leqslant b\:,\quad y(\:a\:)=\alpha 
$$

是适定的。

