import math


def main(n):
    if n == 0:
        return 0.48
    elif n == 1:
        return 0.02
    elif n >= 2:
        return pow(math.sin(main(n - 1)), 2) - 40 * main(n - 2)


main(3)
