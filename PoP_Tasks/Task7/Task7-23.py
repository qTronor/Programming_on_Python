def main(x):
    a = x & 0b1111_1111_11
    b = (x >> 10) & 0b1111_1111_1111_1111
    c = (x >> 26) & 0b1111
    d = (x >> 30) & 0b11

    return b | a << 16 | c << 26 | d << 30


print(hex(main(0x7ce0049b)))
print(hex(main(0x78fd2e4e)))
print(hex(main(0x8b164fa6)))
print(hex(main(0x24a11481)))
print(hex(main(0xf4de0cec)))
