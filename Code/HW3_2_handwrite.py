import numpy as np
import math
import matplotlib.pyplot as plt

class Cubic_Spline_Interpolator:
    def __init__(self, x, y, boundary_type='natural', fp0=None, fpn=None):
        self.x = x
        self.y = y
        self.h = np.diff(x)
        self.boundary_type = boundary_type
        self.fp0 = fp0
        self.fpn = fpn
        self.C = self.get_Cubic_Spline_C()
        self.A = y
        self.B = np.zeros(len(self.h))
        self.D = np.zeros(len(self.h))
        self.compute_B_D()

    def LU_decompose(self, A):
        n = len(A)
        L = np.eye(n)
        U = np.zeros((n, n))

        for i in range(n):
            for j in range(i, n):
                U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
            for j in range(i + 1, n):
                L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
        
        return L, U

    def forward_substitution(self, L, b):
        n = len(b)
        y = np.zeros(n)
        for i in range(n):
            y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
        return y

    def backward_substitution(self, U, y):
        n = len(y)
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i]
        return x

    def solve_equation(self, A, b):
        L, U = self.LU_decompose(A)
        y = self.forward_substitution(L, b)
        x = self.backward_substitution(U, y)
        return x

    def get_Cubic_Spline_C(self):
        n = len(self.h)
        A = np.zeros((n + 1, n + 1))
        b = np.zeros(n + 1)

        if self.boundary_type == 'natural':  # 自由边界条件
            A[0, 0] = 1
            A[n, n] = 1
        elif self.boundary_type == 'clamped':  # 固定边界条件
            A[0, 0] = 2 * self.h[0]
            A[0, 1] = self.h[0]
            A[n, n] = 2 * self.h[-1]
            A[n, n - 1] = self.h[-1]
            b[0] = 3 * (self.y[1] - self.y[0]) / self.h[0] - 3 * self.fp0
            b[n] = 3 * self.fpn - 3 * (self.y[n] - self.y[n - 1]) / self.h[-1]
        elif self.boundary_type == 'periodic':  # 周期边界条件
            A[0, 0] = self.h[0]
            A[0, 1] = 2 * self.h[0]
            A[0, n] = 2 * self.h[-1]
            A[0, n - 1] = self.h[-1]
            A[n, 0] = 1
            A[n, n] = -1
            b[n] = 0
            b[0] = 3 * (self.y[1] - self.y[0]) / self.h[0] - 3 * (self.y[n] - self.y[n - 1]) / self.h[-1]
        elif self.boundary_type == 'special':
            A[0, 0] = -self.h[1]
            A[0, 1] = self.h[0] + self.h[1]
            A[0, 2] = -self.h[0]
            A[n, n - 2] = -self.h[-1]
            A[n, n - 1] = self.h[-2] + self.h[-1]
            A[n, n] = -self.h[-2]
            b[0] = 0
            b[n] = 0

        for i in range(1, n):
            A[i, i] = 2 * (self.h[i - 1] + self.h[i])
            A[i, i - 1] = self.h[i - 1]
            A[i, i + 1] = self.h[i]

        for i in range(1, n):
            b[i] = 3 * (self.y[i + 1] - self.y[i]) / self.h[i] - 3 * (self.y[i] - self.y[i - 1]) / self.h[i - 1]

        C = self.solve_equation(A, b)
        return C

    def compute_B_D(self):
        n = len(self.h)
        for i in range(n):
            self.D[i] = (self.C[i + 1] - self.C[i]) / (3 * self.h[i])
            self.B[i] = (self.A[i + 1] - self.A[i]) / self.h[i] - self.h[i] * (self.C[i + 1] + 2 * self.C[i]) / 3

    def __call__(self, x_new):
        y_new = np.zeros_like(x_new)
        for i in range(len(x_new)):
            # index = np.searchsorted(self.x, x_new[i]) - 1
            index = int(x_new[i] // ((b - a) / len(self.h)))
            if index >= len(self.h):
                index = len(self.h) - 1
            dx = x_new[i] - self.x[index]
            y_new[i] = self.A[index] + self.B[index] * dx + self.C[index] * dx**2 + self.D[index] * dx**3
        return y_new

def f(x):
    return np.sin(x)

if __name__ == '__main__':
    a = 0
    b = math.pi
    num = 11
    x0 = np.linspace(a, b, num)
    y0 = f(x0)

    # 自由边界
    cubic_spline_natural = Cubic_Spline_Interpolator(x0, y0, boundary_type='natural')
    x_new = np.linspace(a, b, 100)
    y_new_natural = cubic_spline_natural(x_new)
    y_true = f(x_new)
    plt.plot(x_new, y_new_natural - y_true, label='Cubic Spline Natural')
    # plt.plot(x_new, y_new_natural, label='Cubic Spline Natural')

    # 固定边界
    fp0 = math.cos(a)
    fpn = math.cos(b)
    cubic_spline_clamped = Cubic_Spline_Interpolator(x0, y0, boundary_type='clamped', fp0=fp0, fpn=fpn)
    y_new_clamped = cubic_spline_clamped(x_new)
    plt.plot(x_new, y_new_clamped - y_true, label='Cubic Spline Clamped')
    # plt.plot(x_new, y_new_clamped, label='Cubic Spline Clamped')

    # 周期边界
    cubic_spline_periodic = Cubic_Spline_Interpolator(x0, y0, boundary_type='periodic')
    y_new_periodic = cubic_spline_periodic(x_new)
    # plt.plot(x_new, y_new_periodic, label='Cubic Spline Periodic')

    # 特殊边界
    cubic_spline_special = Cubic_Spline_Interpolator(x0, y0, boundary_type='special')
    y_new_special = cubic_spline_special(x_new)
    # plt.plot(x_new, y_new_special, label='Cubic Spline Special')
    plt.plot(x_new, y_new_special - y_true, label='Cubic Spline Special')

    # plt.plot(x_new, y_true, label='ture function')

    # plt.scatter(x0, y0, label='Data points', color='red')
    plt.legend()
    # plt.title("Cubic Spline Interpolation with Different Boundary Conditions")
    plt.title("Cubic Spline Interpolation Error with Different Boundary Conditions")
    plt.show()
