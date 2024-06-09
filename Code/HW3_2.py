import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x):
    return np.sin(x)

x0 = np.linspace(0, math.pi, 11)
x1 = np.linspace(0, math.pi, 21)

y0 = np.sin(x0)
y1 = np.sin(x1)

cs_natural = CubicSpline(x0, y0)  # 默认的自然边界条件

cs_fixed = CubicSpline(x0, y0, bc_type=((1, 1.0), (1, -1)))  # 边界的一阶导数为0

cs_periodic = CubicSpline(x0, y0, bc_type='periodic')

x_new = np.linspace(0, math.pi, 100)
y_fixed = cs_fixed(x_new)
y_natural = cs_natural(x_new)
y_periodic = cs_periodic(x_new)
y_true = f(x_new)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x0, y0, 'o', label='Data points')
plt.plot(x_new, y_fixed, label='Fixed boundary')
plt.plot(x_new, y_natural, label='Natural boundary')
plt.plot(x_new, y_periodic, label='Periodic boundary')
plt.plot(x_new, y_true, label='True function')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation with Different Boundary Conditions')
plt.show()
# plt.savefig('HW3_2.png')