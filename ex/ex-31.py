lista = []
while True:
    lista.append(input('informe para colocar em ordem alfabetica '))
    sair = int(input('deseja continuar se sim pressione 0 se não 1 '))
    lista.sort()

    if sair == 1:
        break

print(lista)