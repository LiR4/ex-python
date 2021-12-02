def voto():
    idade = 2021 - ano
    if dia < 30 and mes < 5:
        idade = idade - 1

    if idade < 16:
        return'não é eleitor '
    if idade >= 16 and idade < 18 or idade > 65:
        return'facultativo '
    if idade >= 18 and idade <= 65:
        return 'obrigatorio'

dia= int(input('dia do seu nascimento '))
mes = int(input('informe o mes do seu nascimento '))
ano = int(input('informe o ano do seu nascimento '))

print(voto())