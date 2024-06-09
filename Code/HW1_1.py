import math

alpha = -1e9
beta = -1

a = 1
b = alpha + beta
c = 1e9
delta = b * b - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = 2 * c / (-b + math.sqrt(delta))

print("x1 = ", x1)
print("x2 = ", x2)