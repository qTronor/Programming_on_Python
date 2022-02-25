import math


def main(z):
    if z < 34:
        ans = 3 * pow(pow(z, 3) + 1 + pow(z, 2), 5)
    elif 34 <= z < 70:
        ans = pow(z, 5) + pow(z - 1 - pow(z, 3), 6)
    elif z >= 70:
        ans = pow(z, 2) - 93 * pow(math.sin(z), 5)
    return ans


main(67)
