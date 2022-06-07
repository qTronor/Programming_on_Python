def main(x):
    if x[3] == 2008:
        return x1_1(x)
    elif x[3] == 2007:
        return x0(x)
    elif x[3] == 1974:
        return 9


def x0(x):
    if x[0] == 1980:
        return x1_2(x)
    elif x[0] == 1975:
        return x2_2(x)
    elif x[0] == 1985:
        return x1_3(x)


def x1_1(x):
    if x[1] == 'PLSQL':
        return x2_1(x)
    elif x[1] == "XPROC":
        return 2


def x1_2(x):
    if x[1] == 'PLSQL':
        return 3
    elif x[1] == "XPROC":
        return 4


def x1_3(x):
    if x[1] == 'PLSQL':
        return 7
    elif x[1] == "XPROC":
        return 8


def x2_1(x):
    if x[2] == "COBOL":
        return 0
    elif x[2] == "COQ":
        return 1


def x2_2(x):
    if x[2] == "COBOL":
        return 5
    elif x[2] == "COQ":
        return 6


print(main([1985, 'PLSQL', 'COBOL', 2008]))
print(main([1980, 'PLSQL', 'COBOL', 1974]))
print(main([1985, 'PLSQL', 'COQ', 2008]))
print(main([1975, 'XPROC', 'COQ', 2007]))
print(main([1975, 'XPROC', 'COQ', 2008]))