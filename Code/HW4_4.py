import math
import pandas as np

def f(x):
    return 2 + math.sin(2 * math.sqrt(x))

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

a = 1
b = 6
h = [0.5, 0.25, 0.125]

ans_t_1 = Trapezoid(f, a, b, h[0])
ans_s_1 = Simpson(f, a, b, h[0])

ans_t_2 = Trapezoid(f, a, b, h[1])
ans_s_2 = Simpson(f, a, b, h[1])

ans_t_3 = Trapezoid(f, a, b, h[2])
ans_s_3 = Simpson(f, a, b, h[2])

ans_true = 8.1834792076628

print(ans_t_1, ans_t_2, ans_t_3)
print(ans_s_1, ans_s_2, ans_s_3)