cont = 0
maior = 0
menor = 0
contm = 0
contn = 0
somaI = 0
media = 0

for i in range (1, 5):
    nome = str(input('informe seu nome '))
    sexo = str(input('qual seu sexo (M) masculino (F) feminino (P) prefere não dizer '))
    idade = int(input('informe sua idade '))

    cont = cont + 1

    somaI = media + idade

    if idade > maior :
        maior = idade
        nomem = nome
    else:
        menor = idade

    if idade > 20 and sexo == 'f':
        contm = contm + 1
    elif idade < 20 and sexo == 'f':
        contn = contn + 1

media = somaI / cont

print('media de idade do grupo {:.2f} ' .format(media))
print('o nome do mais velho é ', nomem)
print('mulheres menores de 20 ', contn)