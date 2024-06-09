import math
import numpy as np
import matplotlib.pyplot as plt

def power(A, max_iter=10000, tol=1e-6):
    n = A.shape[0]
    # u = np.random.rand(n)
    u = np.array([1, 1, 1])
    # u /= np.linalg.norm(u)
    timer = 0
    while True:
        v = np.dot(A, u)
        Max = np.max(v)
        cur = v / Max
        if np.linalg.norm(cur - u) < tol or timer > max_iter:
            return Max, cur, timer
        timer += 1
        u = cur

def accelerated_power(A, max_iter=10000, tol=1e-6):
    n = A.shape[0]
    u = np.random.rand(n)
    u /= np.max(u)
    A = A - np.eye(n) * 2
    # print(A)
    v = np.dot(A, u)
    timer = 0
    while True:
        v = np.dot(A, u)
        Max = np.max(v)
        cur = v / Max
        if np.linalg.norm(cur - u) < tol or timer > max_iter:
            return Max + 2, cur, timer
        timer += 1
        u = cur

# A = np.array([[1.0, 1.0, 0.5], 
#               [1.0, 1.0, 0.25], 
#               [0.5, 0.25, 2.0]])
A = np.array([[4, -1, 1], 
              [-1, 3, -2], 
              [1, -2, 3]])

p, v, timer = power(A)

print("Eigenvalue: ", p)
print("Eigenvector: ", v)
print("Iteration: ", timer)

p, v, timer = accelerated_power(A)
print("Eigenvalue: ", p)
print("Eigenvector: ", v)
print("Iteration: ", timer)