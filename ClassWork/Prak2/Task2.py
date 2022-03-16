# num3

def generate_groups():
    print("ИВБО")
    for n in range(1, 10):
        for i in range(1,n):
            if n < 10:
                i.rstrip('ИВБО-0%d-20' % (n))
            else:
                i.rstrip('ИВБО-%d-20' % (n))
    print("ИКБО")

    print("ИНБО")

    print("ИМБО")
    return 0


generate_groups()
