"""
Вариант 15
table = [[1,2,3],
        [4,5,6]]
zip(*table) = [(1,4),(2,5),(3,6)]
copy input data when error send answer
"""
from pprint import pprint


def main(table):
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:  # =~ del empty row and similar row
            new_table.append(row)
    table = list(map(list, zip(*new_table)))  # transposition
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:  # =~ del empty row and similar row
            new_table.append(row)
    table = list(map(list, zip(*new_table)))  # transposition -> original
    for row in table:
        logical, email = row[0].split(';')
        if logical.strip() == 'true':
            logical = '1'
        elif logical.strip() == 'false':
            logical = '0'
        row[0] = email[email.rfind('@') + 1:]  # email
        row.append(logical)  # bool
        row[1] = str(round(float(row[1].strip()), 1))  # digit
        number = '(' + row[2][3:6] + ')' + row[2][6:]
        row[2] = number.strip()  # number
    # new_table.sort(key=lambda x: x[3])
    return table


input_str_1 = [[None, None, None, None, None],
               [None, None, 'false;ajdar19@mail.ru', '0.187', '+7 301 840-48-57'],
               [None, None, None, None, None],
               [None, None, None, None, None],
               [None, None, 'false;marsel_24@yahoo.com', '0.299', '+7 187 544-32-58'],
               [None, None, 'false;miroslav75@rambler.ru', '0.472', '+7 860 433-33-58']]

print("Table 1:")
pprint(main(input_str_1))

input_str_2 = [[None, None, None, None, None],
               [None, None, 'true;damir11@mail.ru', '0.619', '+7 016 898-99-87'],
               [None, None, None, None, None],
               [None, None, 'true;sutubuk95@yandex.ru', '0.181', '+7 247 311-59-08'],
               [None, None, 'false;grigorij32@gmail.com', '0.452', '+7 367 417-27-27']]

print("Table 2:")
pprint(main(input_str_2))
