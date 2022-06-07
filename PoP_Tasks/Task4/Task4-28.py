import math


def f(n):
    if n == 0:
        return -0.67
    elif n == 1:
        return 0.17
    elif n >= 2:
        return f(n - 2) - (((f(n - 2)) ** 3) / 72) - \
               (math.log10((f(n - 1) ** 3) + 35 + 43 * f(n - 1) ** 2)) ** 2


print(f(8))
print(f(4))
print(f(6))
print(f(3))
print(f(5))