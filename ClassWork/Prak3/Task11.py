import csv
import datetime

from matplotlib import pyplot as plt

with open('C:\Users\Home\PycharmProjects\pythonProject\ClassWork\Prak3\GAMES.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))

years = []