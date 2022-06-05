import math


def f(a, m, p, b):
    first_sum = 0
    first_mul = 1
    second_sum = 0
    for i in range(1, m + 1):
        for c in range(1, a + 1):
            first_mul *= (29 * i - 2 * pow(math.atan(31 * pow(p, 3) + 72 * c), 4))
        first_sum += first_mul
    for k in range(1, b + 1):
        for i in range(1, a+1):
            second_sum += (17 * pow((pow(i, 2) + 10 + 83 * k), 2) - pow(k, 3))
    return first_sum - second_sum


print(f(2, 4, -0.98, 4))
print(f(2, 6, -0.14, 5))
print(f(5, 2, 0.02, 8))
print(f(2, 7, -0.18, 3))
print(f(3, 7, -0.76, 8))
