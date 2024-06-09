import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x, y):
    return 1 + y ** 2

def Euler(a, b, h):
    x = np.arange(a, b, h)
    w = []
    w.append(a)
    n = len(x)
    for index in range(1, n):
        w.append(w[index - 1] + h * f(x[index - 1], w[index - 1]))
    return w

def Trapezoid(a, b, h):
    x = np.arange(a, b, h)
    w0 = []
    w = []
    w0.append(a)
    w.append(a)
    n = len(x)
    for index in range(1, n):
        w0.append(w0[index - 1] + h * f(x[index - 1], w[index - 1]))
        w.append(w[index - 1] + h / 2 * (f(x[index - 1], w[index - 1]) + f(x[index], w0[index])))
    return w

def Runge_kutta_4th_order(a, b, h):
    x = np.arange(a, b + h, h)
    y = np.zeros(len(x))
    for i in range(1, len(x)):
        k1 = h * f(x[i-1], y[i-1])
        k2 = h * f(x[i-1] + h / 2, y[i-1] + k1 / 2)
        k3 = h * f(x[i-1] + h / 2, y[i-1] + k2 / 2)
        k4 = h * f(x[i-1] + h, y[i-1] + k3)
        y[i] = y[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y[:-1]

a = 0
b = 1.5
h = 0.01

x = np.arange(a, b, h)
y = np.tan(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='True Value')
plt.title('The Result of the Equation')

ans_euler = Euler(a, b, h)
# plt.plot(x, ans_euler, 'o', label='Euler Method')
cs_euler = CubicSpline(x, ans_euler)
y_euler = cs_euler(x)

ans_trapezoid = Trapezoid(a, b, h)
cs_trapezoid = CubicSpline(x, ans_trapezoid)
y_trapezoid = cs_trapezoid(x)  

ans_runge_kutta = Runge_kutta_4th_order(a, b, h)
cs_runge_kutta = CubicSpline(x, ans_runge_kutta)
y_runge_kutta = cs_runge_kutta(x)

plt.plot(x, y_euler, label='Euler Method')
plt.plot(x, y_trapezoid, label='Trapezoid Method')
plt.plot(x, y_runge_kutta, label='Runge Kutta Method')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()