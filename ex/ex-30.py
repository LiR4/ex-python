from datetime import datetime, timedelta
print('programa para calcular a data de vencimento ')
dia = int(input('Informe a dia do emissão '))
mes = int(input('Informe a mês do emissão '))
ano = int(input('Informe a ano do emissão '))
diaV = int(input('Informe dia para o vencimento '))

dataH = datetime(day=dia, month=mes, year=ano)
dataS = timedelta(days = diaV)

dataV = dataS + dataH

print(dataV)