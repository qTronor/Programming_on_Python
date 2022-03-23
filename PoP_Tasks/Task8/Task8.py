def main(x):
    x = x.replace(' ', '').replace('\n', '').replace('\t', '')[1:-1]
    print(x)
    x_parts = x.split(';')
    print(x_parts)
    result = dict()

    for part in x_parts:
        sym1 = part.find(':')
        sym2 = part.find('.')
        part = part.split("declare")
        print(part)
        key, value = part.split(':')
        result[key[1:-1]] = value
        print(key, value)
    '''for part in x_parts:
        part = part[6:-8].replace('declare', '')
        key, value = part.split(':')
        result[key[1:-1]] = value
        print(part)'''
    return result


print(main(".do <section> declare tirequ_821: ralera_555. </section>;<section> declare teor : iste_941. </section>; <section> declare geza :atedti. </section>;.end'))"))
