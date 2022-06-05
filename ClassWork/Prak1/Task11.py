def fast_mul(x, y):
    result = 0
    if x == 0 or y == 0:
        return 0

    while x // 2 != 0:
        y *= 2
        x //= 2
        if x % 2 == 1:
            result += y
    return result


def fast_mul_gen(y):
    x = 2
    middle = 0
    print("def func(x1 = 1):")
    print("    x2 = x1 + x1")
    while x * 2 < y:
        print("    x{0} = x{1} + x{1}".format(x * 2, x))
        x = x * 2
        middle = x
    while middle < y:
        if middle + x // 2 <= y:
            print("    x{0} = x{1} + x{2}".format(middle + x // 2, middle, x // 2))
            middle = middle + x // 2
        x = x // 2
    print("    return x{0}".format(y))


if __name__ == "__main__":
    fast_mul_gen(int(input()))