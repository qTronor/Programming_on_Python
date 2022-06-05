# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fast_mul_gen(y):

    x = 2
    got = 0
    print("def func(x1 = 1):")
    print("    x2 = x1 + x1")
    while x*2 < y:
        print("    x{0} = x{1} + x{1}".format(x*2, x))
        x = x * 2
        got = x
    while got < y:#8<15 #12<15 #14<15
        if got + x // 2 <= y: #8 + 8 // 2 <= 15 #12 + 4/2 < 15
            print("    x{0} = x{1} + x{2}".format(got + x//2, got, x//2)) #x12 = x8 + x4 #x(12+4/2) = x12 + x2 #x15 = x14+x1
            got = got + x//2 #got = 8 + 4 = 12 #got = 12 + 2
        x = x//2 #x = 4
    print("    return x{0}".format(y))


fast_mul_gen(15)

