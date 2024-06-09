import numpy as np
import matplotlib.pyplot as plt

def van_der_pol(mu, t0, t1, y0, dy0, h):
    def f(t, y):
        y1, y2 = y
        return np.array([y2, mu * (1 - y1**2) * y2 - y1])

    n_steps = int((t1 - t0) / h)
    t = np.linspace(t0, t1, n_steps + 1)
    y = np.zeros((n_steps + 1, 2))
    y[0] = [y0, dy0]

    for i in range(n_steps):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(t[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(t[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    return t, y[:, 0]

# 参数设置
t0, t1 = 0, 20  # 时间区间
y0, dy0 = 1, 0  # 初始条件
h = 0.01        # 步长
mus = [0.01, 0.1, 1.0]  # 不同的 mu 值

# 求解并绘图
plt.figure(figsize=(12, 8))

for mu in mus:
    t, y = van_der_pol(mu, t0, t1, y0, dy0, h)
    plt.plot(t, y, label=f'$\mu={mu}$')

plt.legend()
plt.xlabel('Time t')
plt.ylabel('Solution y')
plt.title('Van der Pol Oscillator Solutions with Different $\mu$ values')
plt.grid(True)
plt.show()
