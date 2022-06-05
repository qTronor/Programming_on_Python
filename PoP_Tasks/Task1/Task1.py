import math


def main(y, z):
    ans = (pow(y, 2) / 70) + (pow(math.sqrt(z + 57 + pow(y, 2)), 5) / 98) - ((
            66 * pow(76 * pow(z, 3) + pow(y, 2), 4) + 99 * pow(z, 2)) / (
            pow(math.acos(y - 1 - 26 * pow(z, 2)), 2)))
    return ans


print(main(0.94, 0.19))
print(main(0.56, -0.08))