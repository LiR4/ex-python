voos = {}
while True :
    numero = str(input('\n informe o númro do voo '))
    origem = input('origem ')
    dest = input('destino ')

    voos.update({numero:[origem, dest]})
    resp = input('deseja continuar ? S/N')
    if resp != 's' or resp == 'n':
        print('\n')
        break

voos_nat = 0

for trecho in voos.values():
    if trecho[1].upper() == 'RECIFE':
        del trecho[1], trecho[0]
        print('voo', numero, 'cancelado')
        

print(voos)