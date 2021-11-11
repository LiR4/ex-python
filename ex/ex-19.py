from datetime import date

cont = 0
contm = 0
hano = date.today().year
for i in range(1,8):
    ano = int(input('Digite o ano de nascimento '))
    maior = hano - ano 
    if maior >= 18:
        cont = cont + 1
    else:
        contm = contm + 1
print('são ', cont , 'maiores de idade ')
print('são ', contm , 'menores de idade ')
