import math
import numpy as np

true_ans = 0.341344746069

def f(x):
    return math.exp(- x ** 2 / 2)

def Trapezoid(f, a, b, h):
    # x = np.arange(a, b, h)
    n = int((b - a) / h)
    ans = f(a) + f(b)
    for index in range(1, n):
        ans += 2 * f(a + index * h)
    return ans * h / 2

def Simpson(f, a, b, h):
    n = int((b - a) / h)
    ans = f(a) + f(b)
    for index in range(1, n):
        if index % 2 == 0:
            ans += 2 * f(a + index * h)
        else:
            ans += 4 * f(a + index * h)
    return ans * h / 3

a = 0
b = 1
# h = 0.01
# h = 0.25
h = 0.05
# h = 0.04

ans1 = 1 / math.sqrt(2 * math.pi) * Trapezoid(f, a, b, h)
ans2 = 1 / math.sqrt(2 * math.pi) * Simpson(f, a, b, h)
ans_true = 0.3413447460685

print("Trapezoid", ans1)
print("Simpson", ans2)