soma = 0
lixo = 0

for i in range(1, 7):
    num = float(input('digite um numero quantas vezes pedir '))

    if num % 2 == 0:
        soma = soma + num
    else:
        lixo = lixo + num

print(soma)
