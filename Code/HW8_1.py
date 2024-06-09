import numpy as np
import matplotlib.pyplot as plt

# 给定的数据点
x = np.array([-2, -1, 0, 1, 2])
y = np.array([0, 1, 2, 1, 0])

# 拟合二次多项式
coefficients = np.polyfit(x, y, 2)

# 打印拟合的多项式系数
print(f"拟合的多项式系数: a={coefficients[0]}, b={coefficients[1]}, c={coefficients[2]}")

# 生成拟合的多项式曲线
p = np.poly1d(coefficients)
x_fit = np.linspace(-2, 2, 100)
y_fit = p(x_fit)

# 绘制数据点和拟合曲线
plt.scatter(x, y, label='Data points')
plt.plot(x_fit, y_fit, label='Fitted polynomial')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Quadratic Polynomial Fit')
plt.show()
