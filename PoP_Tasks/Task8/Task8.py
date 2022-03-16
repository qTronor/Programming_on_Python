def main(x):
    x = x.replace('', '').replace('\n', '').replace('\t', '')[1:-1]
    x_parts = x.split(';')
    result = dict()
    for path in x_parts:
        part = part[6:-8].replace('var@', '')
        key, value = part.split('=')
        result[key[1:-1]] = value
    return result


print(main(".do <section> declare tirequ_821: ralera_555. </section>; <section> declare teor : iste_941. </section>; <section> declare geza :atedti. </section>; .end'))"))
