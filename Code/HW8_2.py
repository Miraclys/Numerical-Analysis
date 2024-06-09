import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(0.5946095 - 0.36989939 * x)

x = np.linspace(0, 4, 1000)
y = f(x)

data_x = [0, 1, 2, 4]
data_y = [2.010, 1.210, 0.740, 0.450]

plt.plot(x, y, label='y = exp(0.5946095 - 0.36989939 * x)', color='blue')
plt.scatter(data_x, data_y, color='red', label='Data Points')
plt.title('y = exp(0.5946095 - 0.36989939 * x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
