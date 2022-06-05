import math


def main(x):
    if x < 66:
        return pow((71 * pow(x, 3) - x - 10 * pow(x, 2)), 2) - 1
    elif 66 <= x < 161:
        return 84 * x - 1
    elif 161 <= x < 198:
        return pow(x, 6)
    elif 198 <= x < 259:
        return x + pow((80 * x - pow(x, 3) - 38), 4)
    elif x >= 259:
        return 88 * pow(x, 4) - pow((1 + pow(x, 2) + (pow(x, 3) / 92)), 5)


print(main(-2))
print(main(191))
print(main(136))
print(main(164))
print(main(215))
