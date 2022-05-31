import matplotlib.pyplot as plt
import random


def mas_sv(digit):
    a = [[0 for i in range(5)] for j in range(5)]
    for i in range(5):
        for j in range(3):
            a[i][j] = random.randint(0, digit)
            if j != 2:
                a[i][4 - j] = a[i][j] #Симметрия
    # print(a)
    return a


def mas_sc(digit):
    a = [[0 for i in range(5)] for j in range(5)]
    for i in range(3):
        for j in range(3):
            a[i][j] = random.randint(0, digit)
            a[i][4 - j] = a[i][j]
            a[4 - i][j] = a[i][j]
            a[4 - i][4 - j] = a[i][j]

    # print(a)
    return a


if __name__ == "__main__":
    fig, axs = plt.subplots(20, 20, figsize=(10, 10))

    for i in range(20):
        for j in range(20):
            if i < 10 and j < 10:
                axs[i][j].imshow(mas_sv(1), cmap='inferno', interpolation='nearest')
            elif i >= 10 and j >= 10:
                axs[i][j].imshow(mas_sc(1), cmap='YlOrBr', interpolation='nearest')
            elif i < 10 and j >= 10:
                axs[i][j].imshow(mas_sv(5), cmap='cool', interpolation='nearest')
            elif i >= 10 and j < 10:
                axs[i][j].imshow(mas_sc(5), cmap='Spectral', interpolation='nearest')
            axs[i][j].axis('off')

    plt.show()
