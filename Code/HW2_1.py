import matplotlib.pyplot as plt
import sys
# sys.set_int_max_str_digits(1000000)

def calculate_x1(x):
    k = 0
    timer = 0
    while True:
        x_k = x[k]
        # print(timer)
        cur = 15 - 2 * x_k ** 2
        x.append(cur)
        print(cur)
        if (abs((cur - x_k) / cur) < 1e-6) or (timer > 3):
            break
        timer += 1
        k += 1

def calculate_x2(x):
    k = 0
    timer = 0
    while True:
        x_k = x[k]
        # print(x_k)
        cur = 15 / (2 * x_k + 1)
        x.append(cur)
        if (abs((cur - x_k) / cur) < 1e-6) or (timer > 10000):
        # if timer > 10000:
            print((x[-1] - 2.5) / (x[-2] - 2.5))
            break
        k += 1
        timer += 1

def calculate_x3(x):
    k = 0
    timer = 0
    while True:
        x_k = x[k]
        cur = x_k - (2 * x_k ** 2 + x_k - 15) / (4 * x_k + 1)
        x.append(cur)
        if (abs(cur - x_k) < 1e-6) or (timer > 10000):
        # if timer > 10000:
            break
        k += 1
        timer += 1

x1 = [2]
x2 = [2]
x3 = [2]

# calculate_x1(x1)
calculate_x2(x2)
# calculate_x3(x3)

# print(len(x1))
# print(len(x2))
# print(len(x3))

# time = 100
# time_x1 = min(len(x1), 3)  
# time_x2 = min(len(x2), 20) 
# time_x3 = min(len(x3), 20) 

# print(x1)

# plt.plot([0, 1, 1.5], [2, 7, -38], label="x1")
# plt.plot(range(time_x2), x2[:time_x2], label="x2")
# plt.plot(range(time_x3), x3[:time_x3], label="x3")
# plt.legend()

# plt.axhline(y=2.5, color='r', linestyle='--', label='y=2.5')

# plt.title("the process of solving the equation x = 15 - 2x^2")

# y_ticks = plt.yticks()[0]

# new_ticks = list(y_ticks) + [2.5]
# plt.yticks(new_ticks)

# plt.xlabel('iteration')
# plt.ylabel('x')

# plt.show()

flg, axs = plt.subplots(1, 2, figsize=(10, 10))

# axs[0].plot(range(len(x1)), x1, label="x1")
# axs[0].set_title('x1')
# axs[0].set_xlabel('iteration')
# axs[0].set_ylabel('x')
axs[0].plot(range(len(x2)), x2, label="x2")
axs[0].set_title('x2')
axs[0].set_xlabel('iteration')
axs[0].set_ylabel('x')
axs[1].plot(range(len(x3)), x3, label="x3")
axs[1].set_title('x3')
axs[1].set_xlabel('iteration')
axs[1].set_ylabel('x')

plt.tight_layout()
plt.show()