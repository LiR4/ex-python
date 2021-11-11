chegadaH = int(input('Informe a chegada (em horas) '))
chegadaM = int(input('Informe a chegada (em minutos) '))
saidaH = int(input('informe a saida (em horas) '))
saidaM = int(input('informe a saida (em minutos) '))

minu = 0 
hora = 0

if chegadaH < saidaH:
    hora = saidaH - chegadaH
elif chegadaM < saidaM :
    minu = saidaM - chegadaM
elif chegadaH > saidaH:
    hora = (24 - chegadaH) + saidaH
elif chegadaM > saidaM:
    minu = (60 - chegadaM) + saidaM

if hora <= 2:
 print('você ficou ', hora, 'horas')
 print('O valor fica no valor de 20,00 R$')
elif hora >= 3 and hora <= 4:
 print('você ficou: ', hora, 'horas')
 print('O valor fica no valor de 32,00 R$')
else:
    horaD = hora - 4 
    preco = horaD * 8
    total = preco + 32
    print('Você ficou: ', hora, 'horas')
    print('Fica no valor de: ', total, 'R$')



#islpha == verifica se é letras
#len == conta caracteres
#isnumeric == verifica se é só numeros