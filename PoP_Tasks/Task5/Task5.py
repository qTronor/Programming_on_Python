def main(y, z):
    ans = 0
    for i in range(len(y)):
        ans += (z[len(y) - 1 - i] ** 2 - 38 * y[i]) ** 4
    return ans


main([0.24, 0.23, 0.28], [-0.81, 0.86, 0.39])

# 25.02.2022
