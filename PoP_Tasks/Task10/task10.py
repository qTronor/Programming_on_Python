# Variant 40

def main(table):
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {''}:
            new_table.append(row)
    table = list(map(list, zip(new_table)))  # Транспонирование матрицы
    del table[0]  # In my task 1
    del table[1]  # and 1
    table = list(map(list, zip(new_table)))
    new_table = list()
    for row in table:
        date, ratio = row[0].split('!')
        date.replace('.', '-')
        ratio = round(float(ratio[:-1]) / 100, 1)

        email = row(1).split('@')[1]
        number_code, *number_main = row[2].split('-')
        number = f'{number_code} {"-".join(number_main)}'
        new_table.append([date, email, ratio, number])
    new_table.sort(key=lambda x: x[3])
    table = list(map(list, zip(new_table)))
    return table
