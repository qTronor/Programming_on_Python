import csv

from matplotlib import pyplot as plt

with open('C:/Users/Home/PycharmProjects/pythonProject/ClassWork/Prak3/GAMES.csv', encoding='utf8') as f:
    games = list(csv.reader(f, delimiter=';'))
print(games[0][-1])

for i in games:
    if(i[-1].isdigit()):
        plt.hist(i[-1], bins = 10)
        plt.xticks()



