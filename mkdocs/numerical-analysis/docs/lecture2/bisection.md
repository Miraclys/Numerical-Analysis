#### Bisection Method

求根的第一个方法就是二分法(bisection method)或者叫做二分搜索，是基于**介值定理**的。

> 我们在计算的时候，仅仅比较了 $f(\dfrac{a + b}{2})$ 和 $f(a)$ 的符号关系，没有必要去求 $f(b)$ 的值。

虽然党区间 $(a, b)$ 内有存在多个根的时候，我们下面的求解过程依然成立，但是为了简化，我们假设区间内的根是唯一的。

#### Code

```python
# Input: a, b, f
# Output: the root of f in [a, b]

def func(x):
    return x**3 - 6*x**2 + 4*x + 12

def bisection(l, r, f):
    if f(l) * f(r) > 0:
        return None
    iter = 0
    while iter < 10000000:
        mid = (l + r) / 2
        if f(mid) * f(l) < 0:
            r = mid
        else:
            l = mid
        iter = iter + 1
    return l

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(bisection(a, b, func))
```

#### 定理

##### **定理2.1**(P43) 
假设 $f \in \mathrm{C}[a, b]$ 且 $f(a) \times f(b) < 0$，则二分法产生出逼近 $f$ 的零点 $p$ 的序列 $\{p\}_{n = 1}^{\infty}$ 且 

$$
|p_n - p| \leq \dfrac{b - a}{2^{n}}, n \geq 1
$$

这一个定理只给出了近似误差的界，且这一个界可能是相当保守的，认识到这一点很重要。


#### 优点与缺点

二分法虽然在概念上十分清晰，但是收敛较慢，并且一个好的中间近似解也可能被无意地丢掉。但是这个方法有一个重要的特点，就是总是收敛于一个解。

#### 注意

1. 对于二分法求解的临界条件，或者说停机条件，我们可以选一个精度 $\varepsilon > 0$，产生 $p_1, p_2, ..., p_n$ 直到满足下面的条件之一：

    $$
    \begin{aligned}
        |p_n - p_{n - 1}| < \varepsilon \\
        \dfrac{|p_n - p_{n - 1}|}{|p_n|} < \varepsilon \\
        |f(p_n)| < \varepsilon
    \end{aligned}
    $$

    遗憾的是，使用上面任何一种停机条件都会出现一些问题。

    所以使用计算机进行近似计算的时候，最好的方式就是**设置一个迭代次数的上界**。

2. 选择越小的初始区间，越有优越性。

3. 当计算机上执行此算法的时候，我们必须考虑舍入误差的影响。例如，区间 $[a, b]$ 的中点的计算应该根据 $p_n = a_n + \dfrac{b_n - a_n}{2}$ 而不是 $p_n = \dfrac{a_n + b_n}{2}$

4. 为了确定哪一个区间包含了函数的根，我们最好使用 $\mathrm{sign}$ 函数，$\mathrm{sign}(f(a_n)) \mathrm{sign}(f(p_n)) < 0$，因为可以避免 $f(a_n)$ 与 $f(p_n)$ 做乘法时可能发生的下溢或者下溢出。