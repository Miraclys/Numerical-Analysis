import numpy as np

def shifted_inverse_power_method(A, sigma, max_iter=10000, tol=1e-8):
    n = A.shape[0]
    x = np.random.rand(n)
    x /= np.linalg.norm(x)
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
    return eigenvalue, y, timer

A = np.array([[4, -1, 1], 
              [-1, 3, -2],  
              [1, -2, 3]])

# Choose a sigma value, ideally a bit larger than the maximum eigenvalue
sigma = 5  # You may need to fine-tune this value based on your specific matrix

eigenvalue, eigenvector, cot = shifted_inverse_power_method(A, sigma)
print("Eigenvalue: ", eigenvalue)
print("Eigenvector: ", eigenvector)
print("Iteration: ", cot)