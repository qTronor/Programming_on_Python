import math


def main(n, m, a, b, y):
    firstSum = 0
    firstMul = 1
    second = 0
    for c in range(1, m + 1):
        for j in range(1, n + 1):
            firstSum += j - 80 * (c ** 5)
        firstMul *= firstSum
    for k in range(1, b + 1):
        for i in range(1, a + 1):
            second += 11 * (math.e ** 4) * (k ** 2 - 62 * i - 64 * y ** 3)

    return firstMul - second


print(main(5, 7, 7, 4, -0.65))
print(main(3, 4, 7, 7, 0.63))
print(main(4, 6, 3, 6, 0.6))
print(main(2, 4, 2, 6, 0.42))
print(main(5, 2, 8, 8, -0.14))
