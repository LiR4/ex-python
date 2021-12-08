voos = {}
while True :
    numero = input('\n informe o númro do voo ')
    origem = input('origem ')
    dest = input('destino ')

    voos.update({numero:[origem, dest]})
    resp = input('deseja continuar ? S/N')
    if resp != 's' or resp == 'n':
        print('\n')
        break

voos_nat = 0

for trecho in voos.values():
    if trecho[0].upper() == 'NATAL':
        voos_nat += 1

print(voos_nat)