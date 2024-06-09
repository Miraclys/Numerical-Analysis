import numpy as np

def Givens_rotation(A):
    # (rows, cols) = A.shape
    rows, cols = A.shape
    Q = np.eye(rows)
    R = A.copy()
    for j in range(cols):
        for i in range(rows-1, j, -1):
            G = np.eye(rows)
            a = R[i-1, j]
            b = R[i, j]
            r = np.hypot(a, b)
            c = a / r
            s = b / r
            G[[i-1, i], [i-1, i]] = c
            G[i-1, i] = s
            G[i, i-1] = -s
            R = G @ R
            Q = Q @ G.T
    return Q, R

# Matrix A
A = np.array([[1, 0, 0], 
              [1, 1, 0], 
              [1, 1, 1],
              [1, 1, 1]])

# Perform QR decomposition using Givens rotation
Q, R = Givens_rotation(A)

print("Q =")
print(Q)
print("R =")
print(R)
