import numpy as np
import matplotlib.pyplot as plt
import random


def distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def is_happy(data, humanx, humany, xn, yn, t):
    neighbours = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = humanx + i
            y = humany + j
            if x == xn:
                x = 0
            if y == yn:
                y = 0
            if data[humanx, humany] == data[x, y]:
                neighbours[z] = 1
            z += 1
    my_favourite_neighbour = -1
    for i in range(8):
        if neighbours[i] == 1:
            my_favourite_neighbour += 1
    if float(my_favourite_neighbour / 8) >= t:
        return True
    else:
        return False


print('Размер популяции: ')
population = 300

print('Размер сетки: ')
x = y = 20

print('Население 1 группы агентов (в процентах): ')
xper = 30

print('Население 2 группы агентов (в процентах): ')
yper = 70
# yper = int(input())
print('Пороговое значение толерантности: ')
t = 0.5
# t = float(input())
print('Количество шагов моделирования: ')
n = 10000
# n = int(input())
if population > x * y:
    print('Населения слишком много')
elif xper + yper > 100:
    print('Неверно введено соотношение в процентах')
elif t > 1:
    print('Пороговое значение толерантности > 1')
else:
    fig, ax = plt.subplots(ncols=2)
    data = np.random.randint(1, 2, (y, x))
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    empty = x * y - population
    i = 0
    happy = []
    itHappy = []
    while i < empty:
        ex = int(random.uniform(0, x))
        ey = int(random.uniform(0, y))
        if data[ex, ey] == 1:
            data[ex, ey] = 0
        else:
            i -= 1
        i += 1
    anotherpopulation = int(yper / 100 * population)
    i = 0
    while i < anotherpopulation:
        ex = int(random.uniform(0, x))
        ey = int(random.uniform(0, y))
        if data[ex, ey] == 1:
            data[ex, ey] = 3
        else:
            i -= 1
        i += 1
    i = 0
    plt.ion()
    while i < n:
        isHappy = 0
        if i % 200 == 0:
            for j in range(x):
                for k in range(y):
                    if data[j, k] != 0:
                        if is_happy(data, j, k, x, y, t) is True:
                            isHappy += 1
            happy.append(float(isHappy / population * 100))
            itHappy.append(i)
        empty = False
        ex = int(random.uniform(0, x))
        ey = int(random.uniform(0, y))
        newex = newey = 0
        if is_happy(data, ex, ey, x, y, t) is False:
            while empty is False:
                newex = int(random.uniform(0, x))
                newey = int(random.uniform(0, y))
                if data[newex, newey] == 0:
                    empty = True
                    data[newex, newey] = data[ex, ey]
                    data[ex, ey] = 0
        if i % 500 == 0:
            h = 0
            j = 0
            data1.clear()
            data2.clear()
            data3.clear()
            data4.clear()
            data5.clear()
            data6.clear()
            while j < x:
                while h < x:
                    if data[j, h] == 1:
                        data1.append(j);
                        data2.append(h);
                    if data[j, h] == 3:
                        data3.append(j);
                        data4.append(h);
                    if data[j, h] == 0:
                        data5.append(j);
                        data6.append(h);
                    h += 1
                h = 0
                j += 1
            plt.clf()
            plt.plot(data1, data2, 's', markerfacecolor='royalblue', markersize=12, markeredgecolor='royalblue')
            plt.plot(data3, data4, 's', markerfacecolor='yellow', markersize=12, markeredgecolor='yellow')
            plt.plot(data5, data6, 's', markerfacecolor='purple', markersize=12, markeredgecolor='purple')
            plt.draw()
            plt.gcf().canvas.flush_events()
            plt.show()
        i += 1
    plt.ioff()
    plt.show()
    #Процент счастливого состояния автора
    plt.plot(itHappy, happy)
    plt.show()
