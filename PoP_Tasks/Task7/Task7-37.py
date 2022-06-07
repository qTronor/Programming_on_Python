def main(x):
    a = x & 0b1111_1111_1111_1
    b = (x >> 13) & 0b1111_1111_1111_1
    c = (x >> 26) & 0b1111
    d = (x >> 30) & 0b11
    return a | (b << 13) | (d << 26) | (c << 28)


print(hex(main(0x2300ffbd)))
print(hex(main(0x158680d1)))
print(hex(main(0x7cf66c36)))
print(hex(main(0xab5d81b6)))
print(hex(main(0x4579e677)))
