import math


def main(x, y):
    return pow(math.tan(71 * x + 89 * pow(x, 3) + pow(y, 2)), 5) - \
           (pow((pow(y, 2) - 8 - pow(x, 3)), 5) - pow(y, 7))


print(main(0.69, 0.32))
print(main(-0.61, -0.49))
print(main(0.33, -0.72))
print(main(0.09, 0.67))
print(main(0.31, -0.58))
