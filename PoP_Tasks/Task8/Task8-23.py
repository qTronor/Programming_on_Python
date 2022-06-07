def main(string):
    string1 = string.split(";")
    result = dict()
    for path in string1:
        q = path.find("<=")
        if(path.find("<=")) != -1:
            value = path[path.find("<=") + 2:].strip()
            key = path[path.rfind(" ", 0, q - 1) + 1: q].strip()
            result[key] = value

    return result

print(main("[ do global ongeri<= xeaisve; od do global ratera <= ritiri; od do\nglobal edisat_759<= sora_81; od]"))
print(main("[ do global ceusus_578<= qucebe;od do global georon <= biin_549;od do\nglobal soator_286 <=ala_956; od do global vear <= mainer_851; od]"))