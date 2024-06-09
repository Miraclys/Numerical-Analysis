import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x, y):
    return (x - y) / 2

def true_y(x):
    return x - 2 + 3 * math.exp(-x / 2)

def Adams_Fourth_Order_Predictor_Corrector(a, b, h):
    x = np.arange(a, b + h, h)
    y = np.zeros(len(x))
    y[0] = 1
    n = len(x)
    for index in range(1, 4):
        k1 = h * f(x[index - 1], y[index - 1])
        k2 = h * f(x[index - 1] + h / 2, y[index - 1] + k1 / 2)
        k3 = h * f(x[index - 1] + h / 2, y[index - 1] + k2 / 2)
        k4 = h * f(x[index], y[index - 1] + k3)
        y[index] = y[index - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    for index in range(3, n):
        f_n = f(x[index - 1], y[index - 1])
        f_n1 = f(x[index - 2], y[index - 2])
        f_n2 = f(x[index - 3], y[index - 3])
        f_n3 = f(x[index - 4], y[index - 4])
        y[index] = y[index - 1] + h / 24 * (55 * f_n - 59 * f_n1 + 37 * f_n2 - 9 * f_n3)
        f_p = f(x[index], y[index])
        y[index] = y[index - 1] + h / 24 * (9 * f_p + 19 * f_n - 5 * f_n1 + f_n2)
    
    return y[:-1]

a = 0
b = 3
h = [1, 0.5, 0.25, 0.125]

for h_i in h:
    x = np.arange(a, b, h_i)
    y = Adams_Fourth_Order_Predictor_Corrector(a, b, h_i)
    plt.plot(x, y, label=f'h = {h_i}')

x = np.arange(a, b, h[-1])
y_true = [true_y(x_i) for x_i in x]

plt.plot(x, y_true, label='True Value')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Adams Fourth Order Predictor Corrector Method')
plt.grid(True)
plt.show()
