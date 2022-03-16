def f1(s):
    return [int(x) for x in s]


def f2(s):
    return len(set(s))


def f3(s):
    return s[::-1]


def f4(s, x):
    return [index for index, el in enumerate(s) if el == x]


def f5(s):
    return sum(s[::2])


def f6(s):
    return max(s, key=len)


print(f4([1,2,1,3,1,2], 1))