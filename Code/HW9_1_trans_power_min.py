import numpy as np

def trans_power(A, max_iter=10000, tol=1e-8):
    n = A.shape[0]
    x = np.random.rand(n)
    x /= np.linalg.norm(x)
    # Choosing a sigma value close to the smallest eigenvalue we are interested in
    sigma = np.min(np.linalg.eigvals(A)) - 1  # Shift value, can be fine-tuned
    A_shifted = A - np.eye(n) * sigma
    A_inv = np.linalg.inv(A_shifted)
    p = 0
    timer = 0
    while True:
        y = np.dot(A_inv, x)
        cur = np.linalg.norm(y)
        y /= cur
        if abs(cur - p) / abs(cur) < tol or timer > max_iter:
            break
        timer += 1
        p = cur
        x = y
    # Reverse the shift
    eigenvalue = 1 / cur + sigma
    return eigenvalue, y

A = np.array([[4, -1, 1], 
              [-1, 3, -2],  
              [1, -2, 3]])

eigenvalue, eigenvector = trans_power(A)
print("Eigenvalue: ", eigenvalue)
print("Eigenvector: ", eigenvector)
