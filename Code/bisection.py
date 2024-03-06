# Input: a, b, f
# Output: the root of f in [a, b]

def func(x):
    return x**3 - 6*x**2 + 4*x + 12

def bisection(l, r, f):
    if f(l) * f(r) > 0:
        return None
    while r - l > 1e-9:
        mid = (l + r) / 2
        if f(mid) * f(l) < 0:
            r = mid
        else:
            l = mid
    return l

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(bisection(a, b, func))