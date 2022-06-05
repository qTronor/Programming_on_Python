x, y = 0, 0
# Умножение на 12: 4 сложения
x = int(input())
y = x
print('Умножение числа', x, 'на 12 равно', end = ' ')
y += x # y = 2x0
y += y # y = 4x0
y = y + y + y # y = 12x0
print(y)
# Умножение на 16: 4 сложения
x = int(input())
y = x
print('Умножение числа', x, 'на 16 равно', end = ' ')
y += y # y = 2x0
y += y # y = 4x0
y += y # y = 8x0
y += y # y = 16x0
print(y)
# Умножение на 15: 3 сложения и 2 вычитания
x = int(input())
print('Умножение числа', x, 'на 15 равно', end = ' ')
y = x
y += x # y = 2x0
y += y # y = 4x0
y += y # y = 8x0
x -= y # y = 8x0, x = -7x0
y -= x # y = 15x0
print(y)
# Умножение на 29: 6 сложений и 1 вычитание
x = int(input())
y = x
print('Умножение числа', x, 'на 29 равно', end = ' ')
y += x # y = 2x0
x = y + x # x = 3x0
y += y # y = 4x0
y += y # y = 8x0
y += y # y = 16x0
y += y # y = 32x0
y -= x # y = 29x0
print(y)