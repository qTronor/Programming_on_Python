import csv
import datetime

from matplotlib import pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('C:/Users/Home/PycharmProjects/pythonProject/ClassWork/Prak3/messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('C:/Users/Home/PycharmProjects/pythonProject/ClassWork/Prak3/results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

print(messages[0])
print(results[0])

'''hours = [parse_time(row[-1]).hour for row in messages]
plt.hist(hours, bins = 24)
plt.xtick(range(24))
plt.show()'''

'''days = [parse_time(row[-1]).weekday() for row in messages]
plt.hist(days, bins = 7)
plt.xticks(range(7))
plt.show()'''

'''groups = [row[-2] for row in messages]
groups_set = set(groups)
groups_dict = {group: groups.count(group) for group in groups_set}
sorted_groups = sorted(groups_dict.items(), key=lambda  x: x[1])

plt.bar([x[0] for x in sorted_groups], [x[1] for x in sorted_groups])
plt.xticks(rotation = 90)
plt.show()'''

'''groups = [row[-3] for row in results if row[-1] == '2']
groups_set = set(groups)
groups_dict = {group: groups.count(group) for group in groups_set}
sorted_groups = sorted(groups_dict.items(), key=lambda  x: x[1])

plt.bar([x[0] for x in sorted_groups], [x[1] for x in sorted_groups])
plt.xticks(rotation = 90)
plt.show()'''


tasks = [row[1] for row in messages]
plt.hist(tasks, bins = len(set(tasks)))
plt.xticks(range(len(set(tasks))))
plt.show()
