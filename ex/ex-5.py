addI = 0
add = 0 

km = float(input('Quantos kilometros foram rodados ? '))
dias = int(input('Por quantos dias você ficou com o carro ? '))
veiculo = input('Porte do veiculo (P) para pequeno, (m) para médio, (G) para grande ')
nome = input('Informe seu nome ')
cnh = input('Informe a CNH: ')
dia = input('informe o dia do nascimento ')
mes = input('informe o mês do nascimento ')
ano = int(input('informe o ano do nascimento '))

if veiculo == 'P':
    custoD = dias * 180
elif veiculo == 'M':
    custoD = dias * 220
elif veiculo == 'G':
    custoD = dias * 270
else:
    print('erro')

idade = int(2021 - ano)

if idade < 21:
    addI = dias * 120

add = float(km * 3.95) 

total = add + custoD + addI

print(nome)
print('Portador da CNH : ', cnh)
print('Nascido em: ', dia, '/', mes, '/', ano )
print('O total do aluguel é: ', total )