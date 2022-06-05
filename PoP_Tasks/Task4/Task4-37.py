def main(n):
    if n == 0:
        return 0.08
    elif n == 1:
        return 0.12
    elif n >= 2:
        return 1 - ((39 * pow(main(n - 2), 2)) / 98) - pow(main(n - 1), 3)


print(main(4))
print(main(6))
print(main(2))
print(main(8))
print(main(3))