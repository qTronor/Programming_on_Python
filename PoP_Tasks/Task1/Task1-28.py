import math


def main(x, y):
    return (((70 * x) ** 3 - (y - y ** 2 - 35)) /
            (23 * ((x ** 3 - y ** 2 - 8 * y) ** 4))) \
           + math.sqrt((abs(((y / 85) - ((x ** 2) / 22) - y ** 3))) ** 5)


print(main(0.17, -0.6))
print(main(-0.08, -0.31))
print(main(0.36, -0.81))
print(main(-0.54, -0.6))
print(main(-0.42, -0.37))
