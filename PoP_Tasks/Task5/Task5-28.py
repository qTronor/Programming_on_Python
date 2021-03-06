import math


def f(x, y):
    ans = 0
    n = len(y)
    for i in range(1, len(y)):
        ans += (math.sin((y[len(y) - 1 - math.floor(i/3)])**2 + 58 * x[i])) ** 7

    return 13 * ans


print(f([-0.22, -0.76, -0.89],
[-0.14, -0.14, 0.54]))
print(f([0.26, 0.03, -0.66],
[-0.92, -0.84, 0.22]))
print(f([-0.84, 0.1, -0.24],
[0.96, -0.81, -0.04]))
print(f([-0.05, 0.56, 0.81],
[-0.95, 0.14, -0.4]))
print(f([-0.44, -0.48, 0.17],
[0.8, 0.95, -0.2]))