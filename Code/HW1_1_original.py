import math

alpha = -10 ** 9
beta = -1

def f(x):
    return x ** 2 + (alpha + beta) * x + 10 ** 9

a = 1
b = alpha + beta
c = 10 ** 9

delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(x1)
print(x2)