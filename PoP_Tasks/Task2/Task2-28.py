import math


def main(z):
    if z < 31:
        return (abs(92 * z ** 2)) ** 7 + ((z ** 3) / 76) ** 5 / 18
    elif 31 <= z < 103:
        return 5 * (50 * z ** 2 - 1 - z / 79) ** 3 + (z ** 4) / 72 + 88 * (math.tan((z ** 3) / 92 + z ** 2 + 1)) ** 5
    elif 103 <= z < 131:
        return 8 + 54 * z ** 2
    elif 131 <= z < 193:
        return z ** 3 - (z ** 2) / 72 - math.log10(z ** 3 + 35 + 43 * z ** 2) ** 6
    elif z >= 193:
        return (abs(25 * z - (z ** 3) / 39)) ** 5 - (abs(33 + z ** 2 + 44 * z ** 3)) ** 7 - 68


print(main(108))
print(main(114))
print(main(107))
print(main(49))
print(main(91))
