import numpy as np
import math
import matplotlib.pyplot as plt

class Cubic_Spline_Interpolator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = np.diff(x)
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
        A[0, 0] = 1
        A[n, n] = 1
        for i in range(1, n):
            A[i, i] = 2 * (self.h[i - 1] + self.h[i])
            A[i, i - 1] = self.h[i - 1]
            A[i, i + 1] = self.h[i]
        b = np.zeros(n + 1)
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

    cubic_spline = Cubic_Spline_Interpolator(x0, y0)
    x_new = np.linspace(a, b, 100)
    y_new = cubic_spline(x_new)

    plt.plot(x0, y0, label='Data points')
    plt.plot(x_new, y_new, label='Cubic Spline 11')

    num = 21
    x0 = np.linspace(a, b, num)
    y0 = f(x0)

    cubic_spline = Cubic_Spline_Normal_Interpolator(x0, y0)
    x_new = np.linspace(a, b, 100)
    y_new = cubic_spline(x_new)
    plt.plot(x_new, y_new, label='Cubic Spline 21')
    plt.legend()
    plt.show()
