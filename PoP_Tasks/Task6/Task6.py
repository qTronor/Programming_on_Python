def main(x):
    if x[3] == 1995:
        return x2(x)
    elif x[3] == 2014:
        return 6
    elif x[3] == 2020:
        return x1_1(x)


def x0(x):
    if x[0] == 'SQL':
        return 0
    elif x[0] == 'URWEB':
        return 1
    elif x[0] == 'NIX':
        return 2


def x1_1(x):
    if x[1] == 1995:
        return 7
    elif x[1] == 1957:
        return 8
    elif x[1] == 1986:
        return 9


def x1_2(x):
    if x[1] == 1995:
        return 3
    elif x[1] == 1957:
        return 4
    elif x[1] == 1986:
        return 5


def x2(x):
    if x[2] == 2000:
        return x0(x)
    elif x[2] == 1975:
        return x1_2(x)


print(main(['URWEB', 1986, 2000, 1995]))