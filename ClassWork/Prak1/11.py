def fast_mult_gen(num1):
    print('def fast_mult_', num1, ':', sep='')
    x = 1
    while num1 > 0:
        if (num1 % 2 != 0):
            print('x =', x)
        num1 = num1 >> 1
        x *= 2
        print('x1 =', x)


fast_mult_gen(int(input()))