def main(x):
    if x[3] == 2015:
        return x2(x)
    elif x[3] == 1979:
        return 11


def x2(x):
    if x[2] == 1966:
        return x1_up(x)
    elif x[2] == 2018:
        return 6
    elif x[2] == 1970:
        return x4_up(x)


def x4_up(x):
    if x[4] == "NSIS":
        return x1_down(x)
    elif x[4] == "FREGE":
        return 10


def x1_down(x):
    if x[1] == 2010:
        return 7
    elif x[1] == 1967:
        return 8
    elif x[1] == 1995:
        return 9


def x1_up(x):
    if x[1] == 2010:
        return x0_up(x)
    elif x[1] == 1967:
        return x0_down(x)
    elif x[1] == 1995:
        return x4_down(x)


def x4_down(x):
    if x[4] == "NSIS":
        return 4
    elif x[4] == "FREGE":
        return 5


def x0_up(x):
    if x[4] == 2009:
        return 0
    elif x[4] == 2004:
        return 1


def x0_down(x):
    if x[0] == 2009:
        return 2
    elif x[0] == 2004:
        return 3


print(main([2004, 1995, 1970, 1979, 'NSIS']))
print(main([2009, 1995, 2018, 2015, 'NSIS']))
print(main([2004, 1995, 1966, 2015, 'FREGE']))
print(main([2004, 1995, 1966, 2015, 'NSIS']))
print(main([2009, 1967, 1966, 2015, 'NSIS']))