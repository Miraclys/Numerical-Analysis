def quick_power(x):
    y = 31
    ans = 1
    while (y):
        if (y & 1 == 1):
            ans *= x
        x *= x
        y >>= 1
    return ans

x = int(input("Enter a number: "))
print(quick_power(x))