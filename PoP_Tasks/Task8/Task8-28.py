def main(str):
    str1 = str.split('set ')
    print(str1)
    result = dict()
    for path in str1:
        q = path.find(":=")
        if(path.find(':=')) != -1:
            value = path[path.find("'", q) + 1:path.rfind("'")].strip()
            key = path[path.rfind(" ", 0, q - 1) + 1: q].strip()
            result[key] = value
    return result



print("1: = ", main("do do set orat := @'edza' od do set orrebe_330 :=@'anen_426' od done"))
print("2: = ", main("do do set quus_793 := @'lateus'od do set beat_886 := @'xete' od do"\
            "set isle_984 :=@'veis_303' od do set timaso:= @'geraed' od done"))