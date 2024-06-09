import math
import numpy as np
import matplotlib.pyplot as plt

def LEN(x):
    return np.sqrt(np.sum(x ** 2))

def Seidel(A, b):
    n = len(A)
    x = np.zeros(n)
    x_pre = np.zeros(n)
    cot = 0
    while True:
        for i in range(n):
            x[i] = (b[i] - sum(A[i, j] * x[j] for j in range(n) if j != i)) / A[i, i]
        if LEN(x - x_pre) / LEN(x) < 1e-6:
            break
        x_pre = x.copy()
        cot += 1
    return cot, x

A = np.array([[4, -1, 1], 
              [4, -8, 1], 
              [-2, 1, 5]])
b = np.array([7, -21, 15])
n = len(A)

cot, x = Seidel(A, b)
print("Iteration: ", cot)
print("Vector: ", x)