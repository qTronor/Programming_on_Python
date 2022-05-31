def main(x):
    x = x.replace('\n', ' ').replace('\t', ' ')[1:]
    x_parts = x.split('.')
    # print(x_parts)
    result = dict()
    for path in x_parts:
        k = path.find(':')
        if path.find(':') != -1:
            key = path[path.rfind(' ', 0, k - 1) + 1: k].strip()
            # print('key:"' + key + '"')
            value = path[path.find(':', k) + 1:].strip()
            # print('value:"' + value + '"')
            result[key] = value

    return result


line_1 = '.do <section> declare tirequ_821: ralera_555. </section>;' \
         '<section>\ndeclare teor : iste_941. </section>;' \
         '<section> declare geza :atedti.\n</section>; .end'
line_2 = '.do <section> declare arus_446 : raat_286.</section>;<section>' \
         'declare veenra_510: aedla_797.</section>;<section>declare eneres_687 :' \
         'qute_342. </section>; .end'
print('Example_1:\n', main(line_1))
print('\nExample_2:\n', main(line_2))
