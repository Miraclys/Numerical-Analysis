import math
import matplotlib.pyplot as plt
eps = 1e-5

def f(x):
    return 1 / 2 + 1 / 4 * x **2 - x * math.sin(x) - 1 /2 * math.cos(2 * x)

def f_(x):
    return 0.5 * x - math.sin(x) - x * math.cos(x) + math.sin(2 * x)

def calculate_x(x):
    k = 0
    timer = 0
    while True:
        x_k = x[k]
        cur = x_k - f(x_k) / f_(x_k)
        x.append(cur)
        if (abs(cur - x_k) < eps) or (timer > 10000):
            break
        k += 1
        timer += 1
    return timer

x1 = [math.pi / 2]
x2 = [5 * math.pi]
x3 = [10 * math.pi]

cot1 = calculate_x(x1)
cot2 = calculate_x(x2)
cot3 = calculate_x(x3)

print("x1: ", x1[-1])
print("x2: ", x2[-1])
print("x3: ", x3[-1])
print("cot1: ", cot1)
print("cot2: ", cot2)
print("cot3: ", cot3)

plt.plot(range(len(x1)), x1, label='x1')
plt.plot(range(len(x2)), x2, label='x2')
plt.plot(range(len(x3)), x3, label='x3')
plt.xlabel("iteration")
plt.ylabel("x")
plt.legend()
plt.show()
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# axs[0].plot(range(len(x1)), x1, label='x1')
# axs[0].set_xlabel("iteration")
# axs[0].set_ylabel("x")
# axs[0].set_title("x_0 = pi / 2")
# axs[1].plot(range(len(x2)), x2, label='x2')
# axs[1].set_xlabel("iteration")
# axs[1].set_ylabel("x")
# axs[1].set_title("x_0 = 5 * pi")
# axs[2].plot(range(len(x3[:300])), x3[:300], label='x3')
# axs[2].set_xlabel("iteration")
# axs[2].set_ylabel("x")
# axs[2].set_title("x_0 = 10 * pi")
# plt.tight_layout()
# plt.show()