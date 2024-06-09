import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([1, 2, 3])
y = np.array([1, 1, 2])

bc_type = ((1, 0.0), (1, 3.0))

cs = CubicSpline(x, y, bc_type=bc_type)

x_new = np.linspace(1, 3, 100)
y_new = cs(x_new)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='o', label='Data points', color='red')
plt.plot(x_new, y_new, label='Cubic Spline Interpolation')
plt.axvline(x=1, linestyle='--', color='gray')
plt.axvline(x=2, linestyle='--', color='gray')
plt.axvline(x=3, linestyle='--', color='gray')
plt.legend()
plt.xlabel('x')
plt.ylabel('s(x)')
plt.title('Cubic Spline Interpolation with Specified Conditions')
plt.grid(True)
plt.show()

print(f"s'(1) = {cs(1, 1)}")
print(f"s'(3) = {cs(3, 1)}")
