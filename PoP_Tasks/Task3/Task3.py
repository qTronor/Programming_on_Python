import math


def main(a, b, y):
    ans = 0
    for k in range(1, b + 1):
        for c in range(1, a + 1):
            ans += 12 * pow(math.fabs(c), 2) - (pow(math.log(k), 6) / 22) - pow(y, 3) / 13
    return ans


main(4, 6, 0.78)
