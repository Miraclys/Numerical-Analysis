import math
import numpy as np

eps = 1e-4

def f(x):
    return 5 * x - math.exp(x)

def f_(x):
    return 5 - math.exp(x)

def bisection(f, a, b, tol):
    cot = 0
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * f(b) > 0:
        print("f(a) and f(b) must have opposite signs")
        return None
    while abs(b - a) > tol:
        cot += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
    return (a + b) / 2, cot
    
def Newton(a, b):
    cot = 0
    x = (a + b) / 2
    while True:
        x_k = x
        x = x_k - f(x_k) / f_(x_k)
        cot += 1
        if abs(x - x_k) < eps or cot > 10000:
            break
    return x, cot

def Secant(a, b):
    cot = 0
    x_k = a
    x_k_1 = b
    while True:
        x_k_2 = x_k_1 - f(x_k_1) * (x_k_1 - x_k) / (f(x_k_1) - f(x_k))
        cot += 1
        if abs(x_k_2 - x_k_1) < eps or cot > 10000:
            break
        x_k = x_k_1
        x_k_1 = x_k_2
    return x_k_2, cot

def Falsi(a, b):
    p0 = a
    p1 = b
    pre = 0
    timer = 0
    p = 0
    while True:
        l = f(p0)
        r = f(p1)
        p = p1 - r * (p1 - p0) / (r - l)
        if np.sign(f(p)) * np.sign(f(p0)) < 0:
            pre = p1
            p1 = p
        else:
            pre = p0
            p0 = p
        if abs(pre - p) <= eps or timer >= 10000:
            break
        timer += 1
    return p, timer

a = 1 / 4
b = 1 / (6 - math.e)

x_0, cot1 = bisection(f, a, b, eps)
mid = (a + b) / 2
x_1, cot2 = Newton(a, b)
x_2, cot3 = Secant(a, b)
x_3, cot4 = Falsi(a, b)

print("Bisection: ", x_0, cot1)
print("Newton: ", x_1, cot2)
print("Secant: ", x_2, cot3)
print("Falsi: ", x_3, cot4)