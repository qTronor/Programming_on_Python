def fast_mul_gen(x):
    print("def f(x):")
    if x == 0:
        print("retrun 0")
    else:
        print('    return x' + ' + x' * (x-1))

fast_mul_gen(0)