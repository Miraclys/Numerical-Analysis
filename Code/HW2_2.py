import math

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def f(x):
    return 2 - 3 * x - math.sin(x)

def bisection(f, a, b, tol):
    cot = 0
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if sign(f(a)) == sign(f(b)):
        print("f(a) and f(b) must have opposite signs")
        return None
    # while abs(b - a) > tol:
    # while ()
    timer = 0
    while timer < 11:
        cot += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c
        timer += 1
    return (a + b) / 2, cot

a = (2 / (2 / math.pi + 3)) + 0.5
b = 0.5

# ans, cot = bisection(f, a, b, 1e-6)
ans, cot = bisection(f, 0, 1, 1e-6)
print("root: ", ans)
print("iteration: ", cot)