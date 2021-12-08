series = {}
cont = 0
while True:
    nomeS = input('informe o nome da serie ')
    ator1 = input('informe o nome de um ator principal ')
    ator2 = input('informe o nome de outro ator principal ')

    series.update({nomeS:[ator1, ator2]})
    resp = input('deseja continuar ? S/N ')
    if resp != 's' or resp == 'n':
        print('\n')
        del series
        break

    ordem= sorted(series.items(), key=lambda x: x[1], reverse=True)

    for i in ordem:
        print(i[0], i[1])