import math
import numpy as np
import matplotlib.pyplot as plt

def symmetry_power(A, max_iter = 10000, tol = 1e-8):
    n = A.shape[0]
    x = np.random.rand(n)
    x = x / np.linalg.norm(x)
    timer = 0
    while True:
        y = np.dot(A, x)
        mu = np.dot(x, y)
        if np.linalg.norm(y) == 0:
            return 0, x
        err = np.linalg.norm(x - y / np.linalg.norm(y))
        x = y / np.linalg.norm(y)
        if err < tol or timer > max_iter:
            return mu, x, timer
        timer += 1

A = np.array([[4, -1, 1], 
              [-1, 3, -2],  
              [1, -2, 3]])

p, a, cot = symmetry_power(A)

print("Eigenvalue: ", p)
print("Eigenvector: ", a)  
print("Iteration: ", cot)