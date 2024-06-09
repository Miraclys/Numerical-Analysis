import math
import numpy as np
import matplotlib.pyplot as plt

def P(x, a, b, h):
    num = x // h
    x0 = a + num * h
    x1 = x0 + h
    Ln0 = (x - x0) / (x1 - x0) * np.sin(x0)
    Ln1 = (x - x1) / (x0 - x1) * np.sin(x1)
    return Ln0 + Ln1

h = 0.003
a = 0
b = math.pi / 2

x = np.arange(a, b, h / 3)
y = np.sin(x)
y_pred = [P(x[i], a, b, h) for i in range(len(x))]

distance = y - y_pred

Max = np.max(np.abs(distance))
print(Max)
