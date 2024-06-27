import math
import numpy as np
import matplotlib.pyplot as plt

def Householder(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    for k in range(n):
        x = R[k:, k]
        y = np.linalg.norm(x) * (-1 * np.sign(x[0]))
        omega = x.copy()
        omega[0] -= y
        Hk = np.eye(m)
        Hk[k:, k:] -= 2 * np.outer(omega, omega) / np.dot(omega, omega)
        R = np.dot(Hk, R)
        Q = np.dot(Q, Hk)
        print("Hk = \n", Hk)
        # print("Q = \n", Q)
    return Q, R

A = np.array([[1, 0, 0],
              [1, 1, 0],
              [1, 1, 1], 
              [1, 1, 1]], dtype=float)

Q, R = Householder(A)
# Q, R = householder_reflection(A)

print("Q = \n", Q)
print("R = \n", R)

# A_reconstructed = Q @ R

# print("A_reconstructed = ", A_reconstructed)
# print("original A:")
# print(A)
