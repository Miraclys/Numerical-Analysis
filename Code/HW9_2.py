import numpy as np

def householder_reflection(A):
    (rows, cols) = np.shape(A)
    Q = np.identity(rows)
    R = np.copy(A)

    for i in range(cols - 1):
        x = R[i:, i]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_i = np.identity(rows)
        Q_i[i:, i:] -= 2.0 * np.outer(v, v)
        R = np.dot(Q_i, R)
        Q = np.dot(Q, Q_i.T)
    
    return Q, R

A = np.array([
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 1],
    [1, 1, 1]
])

Q, R = householder_reflection(A)
print("Q:\n", Q)
print("R:\n", R)
