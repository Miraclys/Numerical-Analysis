import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def LU_decompose(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    
    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i]
    return x

A = np.zeros((3, 3))
# A = np.array([[4, -1, 1], 
#               [4, -8, 1], 
#               [-2, 1, 5]])
# b = np.array([7, -21, 15])
# A = np.array([[5, 0, 10],
#               [0, 10, 0],
#               [10, 0, 34]])
# b = np.array([4, 0, 2])
A = np.array([[4, 7], 
              [7, 21]])
b = np.array([-0.21085770732205933, -3.60562061083028])

L, U = LU_decompose(A)
print("L =\n", L)
print("U =\n", U)

# 解 Lz = b
y = forward_substitution(L, b)
print("y =\n", y)

# 解 Ux = y
x = backward_substitution(U, y)
print("the answer of LU: ")
print(x)

