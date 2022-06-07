def main(x):
    x = x.replace('\n', ' ').replace('\t', ' ')[1:]
    x_parts = x.split('},')
    #print('x_parts = ', x_parts)
    result = dict()
    for path in x_parts:
        p = path.split('#')
        #print('p =', p)
        for q in p:
            k = path.find('=:')
            if path.find('=:') != -1:
                value = path[path.rfind('#', 0, k - 1) + 1: k].strip()
                #print('value:"' + value + '"')
                key = path[path.find(':', k) + 1:].strip()
                #print('key:"' + key + '"')
                result[key] = value

    return result


line_1 = 'do { glob #-1972=: lara_960 }, {glob #4221 =: orte_609 }, { glob' \
        '#-9256 =: lais_581}, end'
line_2 = '.do <section> declare arus_446 : raat_286.</section>;<section>' \
         'do {glob#-3479 =:eres_444 }, { glob #-1807=: beis }, { glob#-5310 =:' \
            'teeres}, end'
print('Example_1:\n', main(line_1))
print('\nExample_2:\n', main(line_2))
