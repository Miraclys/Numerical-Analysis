import math
import numpy as np
import matplotlib.pyplot as plt

def P(x, a, h):
    num = x // h
    x0 = a + num * h
    x1 = x0 + h
    Ln1 = (x - x0) / (x1 - x0) * np.sin(x1)
    Ln0 = (x - x1) / (x0 - x1) * np.sin(x0)
    return Ln0 + Ln1

h = 0.002
a = 0
b = math.pi * 100

x = np.arange(a, b, h / 10)
y = np.sin(x)
y_pred = [P(x[i], a, h) for i in range(len(x))]

distance = y - y_pred

# print(distance)

Max = np.max(np.abs(distance))
print(Max)
