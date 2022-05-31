a = []
spisok = ["ИВБО", "ИКБО", "ИНБО", "ИМБО"]

def generate_groups(s):
    global a
    for i in range(1, 10):
        if (s == "ИВБО" and i == 9):
            continue
        if (s == "ИМБО" and i >= 3):
            continue
        a.append((s + "-0" + str(i) + "-20"))
    for i in range(10, 31):
        if (s == "ИВБО" and i != 13):
            continue
        if (s == "ИКБО" and (i == 28 or i == 29)):
            continue
        if (s == "ИНБО" and (i == 12 or i == 14 or i >= 16)):
            continue
        if (s == "ИМБО"):
            continue
        a.append((s + "-" + str(i) + "-20"))

for group in spisok:
    generate_groups(group)

print(a)
for item in a:
    print(item)