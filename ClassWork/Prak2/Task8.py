import random
soglBIG = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
soglsmol = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'ч', 'ц', 'ч', 'ш', 'щ']
glasBIG = ['А', 'Е', 'И', 'О', 'У', 'Ю', 'Я', 'Э']
glassmol = ['а', 'е', 'и', 'о', 'у', 'ю', 'я', 'э', 'ы', 'ё']
surnamesEnd = ["ов", "ич", "ко", "ин", "ий", "ев", "ый", "ых", "ян", "ич", "ас"]
names = ["Григорий", "Лев", "Андрей", "Роман", "Арсений", "Степан", "Владислав", "Никита", "Глеб", "Марк", "Давид", "Ярослав", "Евгений", "Матвей", "Фёдор", "Николай", "Алексей", "Андрей", "Артемий", "Виктор", "Никита", "Даниил", "Денис", "Егор", "Игорь", "Лев", "Леонид", "Павел", "Петр", "Роман", "Руслан", "Сергей", "Семён", "Тимофей"]

Full = ""
for n in range(20):
    Full += random.choice(names) + ' ' + random.choice(soglBIG) + ". " + random.choice(soglBIG) + random.choice(glassmol)

    for slog in range(random.randint(1, 2)):
        Full += random.choice(soglsmol) + random.choice(glassmol)
    Full += random.choice(soglsmol) + random.choice(surnamesEnd)
    print(Full)
    Full = ""