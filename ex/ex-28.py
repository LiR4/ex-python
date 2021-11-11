lista = []
cont = 0
contA = 0
for i in range(5):
    lista.append(str(input('informe 10 caracteres ')))
    listB = lista[i]
    if listB not in ('a','e','i','o','u'):
        cont = cont + 1     
        print(lista[i])
print('consoante', cont)